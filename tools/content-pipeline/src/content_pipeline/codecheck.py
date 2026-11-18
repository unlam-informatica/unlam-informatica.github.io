"""Verificación de código SQL Server y MongoDB contra contenedores Docker locales.

Cada materia declara en ``subject.yaml`` la sección ``engines`` (imagen fijada por digest y nombre de
contenedor). Los scripts de ``checks/sql/<ID>.sql`` y ``checks/mongo/<ID>.js`` se ejecutan en bases
descartables; la salida se compara con ``<ID>.expected`` si existe. Los contenedores no publican puertos:
todo pasa por ``docker exec``. La contraseña de SA nunca se escribe en archivos ni en la línea de comandos:
se lee de ``docker inspect`` y se entrega por variable de entorno heredada (``docker exec -e VAR``).
"""
from __future__ import annotations

import difflib
import os
import re
import secrets
import string
import subprocess
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

from .config import PipelineError, SubjectPaths
from .io_utils import atomic_write, read_yaml, write_json
from .logging_utils import get_logger

SQLCMD = "/opt/mssql-tools18/bin/sqlcmd"
CHECK_TIMEOUT = 60
SQL_LANGS = {"sql", "tsql"}
MONGO_LANGS = {"js", "javascript", "mongodb"}
CHECKED_LANGS = SQL_LANGS | MONGO_LANGS
REVIEW_FIELDS = ("id", "reason", "reviewer", "date", "page")
MARKER_RE = re.compile(r"<!--\s*check:\s*([A-Za-z0-9_.\-]+)\s*-->")
# Plantilla de sintaxis no ejecutable (SELECT ..., FUNCION(...) OVER (...)): no es pendiente ni verificada.
SYNTAX_RE = re.compile(r"<!--\s*sintaxis\s*-->")
# Una plantilla tiene marcadores de posición; sin ellos y con aspecto de sentencia completa, es sospechosa.
PLACEHOLDER_RE = re.compile(r"\.\.\.|…|<[^>]+>|\[[^\]]*\]|\|")
STATEMENT_RE = re.compile(r"\b(INSERT|CREATE\s+TABLE|UPDATE|DELETE|insertOne|insertMany)\b", re.I)
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})\s*([^\s`]*)")
PROTECTED_CONTAINERS = {"mssql"}


# --------------------------------------------------------------------------------------------------
# Runner inyectable
# --------------------------------------------------------------------------------------------------
@dataclass
class RunResult:
    returncode: int
    stdout: str = ""
    stderr: str = ""


class Runner(Protocol):
    """Interfaz que usan los tests con un runner falso (sin Docker)."""

    def ensure_ready(self, engines: set[str]) -> None:
        """Lanza PipelineError si algún motor requerido no responde."""

    def versions(self, engines: set[str]) -> dict[str, str | None]: ...

    def run_sql(self, database: str, script: str, timeout: int) -> RunResult:
        """Crea la base ``database``, ejecuta el script y la elimina."""

    def run_mongo(self, database: str, script: str, timeout: int) -> RunResult:
        """Ejecuta el script con ``db`` apuntando a ``database`` y la elimina al terminar."""


def _docker(args: list[str], *, env: dict[str, str] | None = None, stdin: str | None = None,
            timeout: int | None = None) -> RunResult:
    full_env = {**os.environ, **(env or {})}
    try:
        proc = subprocess.run(["docker", *args], input=stdin, capture_output=True, text=True, encoding="utf-8",
                              errors="replace", timeout=timeout, env=full_env)
    except FileNotFoundError as error:
        raise PipelineError("No se encontró el comando docker.") from error
    except subprocess.TimeoutExpired:
        return RunResult(124, "", f"timeout de {timeout} s")
    return RunResult(proc.returncode, proc.stdout, proc.stderr)


def load_engines(paths: SubjectPaths) -> dict[str, dict[str, Any]]:
    config = read_yaml(paths.subject_config) if paths.subject_config.exists() else None
    engines = (config or {}).get("engines")
    if not isinstance(engines, dict) or not engines:
        raise PipelineError(f"{paths.subject_config} no declara la sección engines.")
    for name, spec in engines.items():
        if name not in ("mssql", "mongo"):
            raise PipelineError(f"Motor desconocido en engines: {name}")
        if not isinstance(spec, dict) or not spec.get("image") or not spec.get("container"):
            raise PipelineError(f"engines.{name} requiere image y container.")
        if spec["container"] in PROTECTED_CONTAINERS:
            raise PipelineError(f"engines.{name}.container usa un nombre reservado: {spec['container']}")
    return engines


def _inspect(container: str) -> dict[str, Any] | None:
    import json

    result = _docker(["inspect", container], timeout=30)
    if result.returncode != 0:
        return None
    data = json.loads(result.stdout)
    return data[0] if data else None


def _container_env(info: dict[str, Any], key: str) -> str | None:
    for item in info.get("Config", {}).get("Env", []) or []:
        if item.startswith(key + "="):
            return item.split("=", 1)[1]
    return None


def generate_sa_password() -> str:
    """Contraseña aleatoria que cumple la política de SQL Server (mayúsculas, minúsculas, dígitos, símbolo)."""
    pools = [string.ascii_uppercase, string.ascii_lowercase, string.digits, "_-+="]
    chars = [secrets.choice(pool) for pool in pools]
    alphabet = string.ascii_letters + string.digits
    chars += [secrets.choice(alphabet) for _ in range(20)]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


class DockerRunner:
    """Ejecuta los scripts con ``docker exec`` en los contenedores declarados en ``engines``."""

    def __init__(self, engines: dict[str, dict[str, Any]]):
        self.engines = engines

    # -- utilidades ----------------------------------------------------------------------------
    def _container(self, engine: str) -> str:
        if engine not in self.engines:
            raise PipelineError(f"La materia no declara el motor {engine} en engines.")
        return self.engines[engine]["container"]

    def _running(self, engine: str) -> bool:
        info = _inspect(self._container(engine))
        return bool(info and info.get("State", {}).get("Running"))

    def _sa_env(self) -> dict[str, str]:
        info = _inspect(self._container("mssql"))
        password = _container_env(info or {}, "MSSQL_SA_PASSWORD") or _container_env(info or {}, "SA_PASSWORD")
        if not password:
            raise PipelineError("El contenedor de SQL Server no tiene contraseña de SA; recrealo con engines up.")
        return {"SQLCMDPASSWORD": password}

    def _sqlcmd(self, extra: list[str], stdin: str | None, timeout: int, database: str = "master") -> RunResult:
        args = ["exec", "-i", "-e", "SQLCMDPASSWORD", self._container("mssql"), SQLCMD, "-S", "localhost", "-U", "sa",
                "-b", "-I", "-C", "-d", database, *extra]
        return _docker(args, env=self._sa_env(), stdin=stdin, timeout=timeout)

    def _mongosh(self, script: str, timeout: int) -> RunResult:
        return _docker(["exec", "-i", self._container("mongo"), "mongosh", "--quiet", "--norc", "--file", "/dev/stdin"],
                       stdin=script, timeout=timeout)

    # -- interfaz Runner -----------------------------------------------------------------------
    def ensure_ready(self, engines: set[str]) -> None:
        for engine in sorted(engines):
            if not self._running(engine):
                raise PipelineError(
                    f"El motor {engine} (contenedor {self._container(engine)}) no está corriendo. "
                    "Ejecutá: content-pipeline engines up --subject <materia>"
                )

    def versions(self, engines: set[str]) -> dict[str, str | None]:
        out: dict[str, str | None] = {}
        if "mssql" in engines:
            result = self._sqlcmd(["-h", "-1", "-W", "-Q", "SET NOCOUNT ON; SELECT @@VERSION"], None, 60)
            lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            out["mssql"] = lines[0] if result.returncode == 0 and lines else None
        if "mongo" in engines:
            result = self._mongosh("print(db.version())", 60)
            lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            out["mongo"] = lines[-1] if result.returncode == 0 and lines else None
        return out

    def stage_files(self, engine: str, database: str, directory: Path) -> str:
        """Copia ``directory`` al contenedor del motor y devuelve la ruta destino."""
        target = f"/tmp/checks/{database}"
        container = self._container(engine)
        for args in (["exec", container, "rm", "-rf", target], ["exec", container, "mkdir", "-p", target],
                     ["cp", f"{directory}/.", f"{container}:{target}"],
                     ["exec", "-u", "0", container, "chmod", "-R", "a+rX", target]):
            result = subprocess.run(["docker", *args], capture_output=True, text=True, timeout=60)
            if result.returncode != 0:
                raise PipelineError(f"No se pudieron copiar los archivos auxiliares: {result.stderr.strip()[-200:]}")
        return target

    def run_sql(self, database: str, script: str, timeout: int) -> RunResult:
        quoted = database.replace("]", "]]")
        setup = (f"SET NOCOUNT ON; IF DB_ID(N'{database}') IS NOT NULL BEGIN ALTER DATABASE [{quoted}] SET SINGLE_USER "
                 f"WITH ROLLBACK IMMEDIATE; DROP DATABASE [{quoted}]; END; CREATE DATABASE [{quoted}];")
        created = self._sqlcmd(["-Q", setup], None, 120)
        if created.returncode != 0:
            return RunResult(created.returncode, created.stdout, "no se pudo crear la base: " + created.stderr)
        try:
            # NOCOUNT en un lote propio: el script puede empezar con CREATE SCHEMA o CREATE PROCEDURE.
            return self._sqlcmd(["-h", "-1", "-W", "-s", "|", "-i", "/dev/stdin"], "SET NOCOUNT ON;\nGO\n" + script,
                                timeout, database=database)
        finally:
            teardown = (f"SET NOCOUNT ON; IF DB_ID(N'{database}') IS NOT NULL BEGIN ALTER DATABASE [{quoted}] SET "
                        f"SINGLE_USER WITH ROLLBACK IMMEDIATE; DROP DATABASE [{quoted}]; END;")
            self._sqlcmd(["-Q", teardown], None, 120)

    def run_mongo(self, database: str, script: str, timeout: int) -> RunResult:
        prelude = f"db = db.getSiblingDB('{database}'); db.dropDatabase();\n"
        try:
            return self._mongosh(prelude + script, timeout)
        finally:
            self._mongosh(f"db.getSiblingDB('{database}').dropDatabase();", 60)


# --------------------------------------------------------------------------------------------------
# Ciclo de vida de los contenedores
# --------------------------------------------------------------------------------------------------
def engines_status(engines: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for name, spec in engines.items():
        info = _inspect(spec["container"])
        row: dict[str, Any] = {"engine": name, "container": spec["container"], "declared_image": spec["image"],
                               "state": "inexistente", "health": None, "image": None, "image_id": None,
                               "digest": None, "responds": False}
        if info:
            state = info.get("State", {})
            row["state"] = state.get("Status", "desconocido")
            row["health"] = (state.get("Health") or {}).get("Status")
            row["image"] = info.get("Config", {}).get("Image")
            row["image_id"] = info.get("Image")
            digests = _docker(["image", "inspect", "-f", "{{join .RepoDigests \",\"}}", info.get("Image", "")],
                              timeout=30)
            row["digest"] = digests.stdout.strip() or None if digests.returncode == 0 else None
            if state.get("Running"):
                row["responds"] = _probe(DockerRunner(engines), name)
        rows.append(row)
    return rows


def _probe(runner: DockerRunner, engine: str) -> bool:
    try:
        if engine == "mssql":
            return runner._sqlcmd(["-h", "-1", "-Q", "SELECT 1"], None, 20).returncode == 0
        return runner._mongosh("db.runCommand({ping:1}).ok", 20).returncode == 0
    except PipelineError:
        return False


def engines_up(engines: dict[str, dict[str, Any]], wait: int = 180) -> list[dict[str, Any]]:
    log = get_logger()
    runner = DockerRunner(engines)
    for name, spec in engines.items():
        container = spec["container"]
        info = _inspect(container)
        if info is None:
            args = ["run", "-d", "--name", container]
            env: dict[str, str] = {}
            if spec.get("platform"):
                args += ["--platform", spec["platform"]]
            if name == "mssql":
                env["MSSQL_SA_PASSWORD"] = generate_sa_password()
                args += ["-e", "ACCEPT_EULA=Y", "-e", "MSSQL_PID=Developer", "-e", "MSSQL_SA_PASSWORD"]
            args.append(spec["image"])
            log.info("creando contenedor %s", container)
            result = _docker(args, env=env, timeout=300)
            if result.returncode != 0:
                raise PipelineError(f"No se pudo crear {container}: {result.stderr.strip()[-400:]}")
        elif not info.get("State", {}).get("Running"):
            log.info("iniciando contenedor %s", container)
            result = _docker(["start", container], timeout=60)
            if result.returncode != 0:
                raise PipelineError(f"No se pudo iniciar {container}: {result.stderr.strip()[-400:]}")
    deadline = time.monotonic() + wait
    pending = set(engines)
    while pending and time.monotonic() < deadline:
        for name in sorted(pending):
            if _probe(runner, name):
                pending.discard(name)
                log.info("motor %s listo", name)
        if pending:
            time.sleep(3)
    if pending:
        raise PipelineError(f"Los motores {sorted(pending)} no respondieron en {wait} s.")
    return engines_status(engines)


def engines_down(engines: dict[str, dict[str, Any]]) -> list[str]:
    removed = []
    for spec in engines.values():
        container = spec["container"]
        if _inspect(container) is not None:
            result = _docker(["rm", "-f", container], timeout=120)
            if result.returncode != 0:
                raise PipelineError(f"No se pudo eliminar {container}: {result.stderr.strip()[-400:]}")
            removed.append(container)
    return removed


# --------------------------------------------------------------------------------------------------
# Verificación
# --------------------------------------------------------------------------------------------------
def sanitize_id(check_id: str) -> str:
    return "chk_" + re.sub(r"[^A-Za-z0-9]", "_", check_id)


# Directiva por check para mensajes del motor que no dependen del contenido (p. ej., los informativos de
# ALTER DATABASE ... WITH ROLLBACK IMMEDIATE, que aparecen o no según haya otras conexiones).
IGNORE_RE = re.compile(r"^\s*(?:--|//)\s*verify:\s*ignorar-salida\s+(.+?)\s*$", re.M)


def ignore_patterns(script: str) -> list[re.Pattern[str]]:
    return [re.compile(p) for p in IGNORE_RE.findall(script)]


def normalize_output(text: str, ignore: list[re.Pattern[str]] | None = None) -> str:
    lines = (line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"))
    return "\n".join(line for line in lines if line and not any(p.search(line) for p in ignore or []))


def _tail(text: str, lines: int = 8, limit: int = 600) -> str:
    chunk = "\n".join(text.strip().splitlines()[-lines:])
    return chunk[-limit:]


def _short_diff(expected: str, actual: str) -> str:
    diff = difflib.unified_diff(expected.splitlines(), actual.splitlines(), "esperado", "obtenido", lineterm="", n=0)
    lines = list(diff)
    shown = lines[:14] + ([f"... ({len(lines) - 14} líneas más)"] if len(lines) > 14 else [])
    return "\n".join(shown)[:800]


def discover_checks(paths: SubjectPaths) -> list[dict[str, Any]]:
    found = []
    for engine, folder, suffix in (("mssql", "sql", ".sql"), ("mongo", "mongo", ".js")):
        directory = paths.root / "checks" / folder
        if directory.is_dir():
            for file in sorted(directory.glob(f"*{suffix}")):
                found.append({"id": file.name[: -len(suffix)], "engine": engine, "file": file,
                              "script": f"checks/{folder}/{file.name}",
                              "expected_file": file.with_suffix(".expected")})
    return found


def load_reviewed(paths: SubjectPaths) -> list[dict[str, str]]:
    path = paths.root / "checks" / "reviewed.yaml"
    if not path.exists():
        return []
    data = read_yaml(path)
    if data is None:
        return []
    if not isinstance(data, list):
        raise PipelineError(f"{path.name} debe ser una lista de entradas {{id, reason, reviewer, date, page}}.")
    entries = []
    for index, item in enumerate(data, 1):
        if not isinstance(item, dict):
            raise PipelineError(f"{path.name}: la entrada {index} no es un mapa.")
        missing = [f for f in REVIEW_FIELDS if item.get(f) in (None, "")]
        if missing:
            raise PipelineError(f"{path.name}: la entrada {index} ({item.get('id', '?')}) no tiene {', '.join(missing)}.")
        entries.append({f: str(item[f]) for f in REVIEW_FIELDS})
    return entries


def scan_docs(docs_root: Path, known_ids: set[str],
              syntax: list[dict[str, Any]] | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Devuelve (pendientes, marcadores huérfanos) recorriendo los .md/.mdx de ``docs_root``.

    Los bloques precedidos por ``<!-- sintaxis -->`` se agregan a ``syntax`` (si se pasa), con
    ``suspicious=True`` cuando parecen una sentencia completa sin marcadores de posición.
    """
    pending: list[dict[str, Any]] = []
    orphans: list[dict[str, Any]] = []
    if not docs_root.is_dir():
        return pending, orphans
    for file in sorted([*docs_root.rglob("*.md"), *docs_root.rglob("*.mdx")]):
        page = file.relative_to(docs_root).as_posix()
        lines = file.read_text(encoding="utf-8").splitlines()
        fence: str | None = None
        template: dict[str, Any] | None = None
        body: list[str] = []
        for number, line in enumerate(lines, 1):
            match = FENCE_RE.match(line)
            if fence is None:
                if match:
                    fence = match.group(1)
                    language = match.group(2).lower()
                    if language in CHECKED_LANGS:
                        previous = [l for l in lines[: number - 1] if l.strip()][-3:]
                        marked = any((m := MARKER_RE.search(p)) and m.group(1) in known_ids for p in previous)
                        if previous and SYNTAX_RE.search(previous[-1]):
                            template = {"page": page, "line": number, "language": language}
                            body = []
                        elif not marked:
                            pending.append({"page": page, "line": number, "language": language})
                    continue
                for marker in MARKER_RE.finditer(line):
                    if marker.group(1) not in known_ids:
                        orphans.append({"id": marker.group(1), "page": page, "line": number})
            elif match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) and not match.group(2):
                fence = None
                if template is not None:
                    text = "\n".join(body)
                    template["suspicious"] = bool(STATEMENT_RE.search(text)) and not PLACEHOLDER_RE.search(text)
                    if syntax is not None:
                        syntax.append(template)
                    template = None
            elif template is not None:
                body.append(line)
    return pending, orphans


FIXTURES_TOKEN = "{{FIXTURES}}"


def _run_check(runner: Runner, check: dict[str, Any], timeout: int) -> dict[str, Any]:
    script = check["file"].read_text(encoding="utf-8")
    database = sanitize_id(check["id"])
    started = time.monotonic()
    try:
        # Archivos auxiliares (CSV, JSON, XML) en <ID>.files/: se copian al contenedor y el script
        # los referencia con {{FIXTURES}} (ruta absoluta dentro del contenedor).
        fixtures = check["file"].with_suffix(".files")
        if fixtures.is_dir():
            stage = getattr(runner, "stage_files", None)
            if stage is None:
                raise PipelineError("El runner no admite archivos auxiliares")
            script = script.replace(FIXTURES_TOKEN, stage(check["engine"], database, fixtures))
        elif FIXTURES_TOKEN in script:
            raise PipelineError(f"El script usa {FIXTURES_TOKEN} pero no existe {fixtures.name}/")
        if check["engine"] == "mssql":
            result = runner.run_sql(database, script, timeout)
        else:
            result = runner.run_mongo(database, script, timeout)
    except Exception as error:  # noqa: BLE001 - el runner puede fallar de cualquier forma
        result = RunResult(1, "", f"{type(error).__name__}: {error}")
    seconds = round(time.monotonic() - started, 2)
    expected_file: Path = check["expected_file"]
    has_expected = expected_file.exists()
    entry: dict[str, Any] = {"id": check["id"], "engine": check["engine"], "status": "aprobado",
                             "script": check["script"], "expected": has_expected, "seconds": seconds, "message": ""}
    if result.returncode != 0:
        entry["status"] = "error"
        entry["message"] = _tail((result.stderr + "\n" + result.stdout) if result.stderr.strip() else result.stdout) \
            or f"código de salida {result.returncode}"
    elif has_expected:
        ignore = ignore_patterns(script)
        expected = normalize_output(expected_file.read_text(encoding="utf-8"), ignore)
        actual = normalize_output(result.stdout, ignore)
        if expected != actual:
            entry["status"] = "fallido"
            entry["message"] = _short_diff(expected, actual)
    return entry


def run_verify_code(paths: SubjectPaths, runner: Runner, *, docs_root: Path, ids: list[str] | None = None,
                    report_path: Path | None = None, timeout: int = CHECK_TIMEOUT) -> dict[str, Any]:
    reviewed = load_reviewed(paths)
    all_checks = discover_checks(paths)
    selected = [c for c in all_checks if not ids or c["id"] in ids]
    if ids:
        unknown = sorted(set(ids) - {c["id"] for c in all_checks})
        if unknown:
            raise PipelineError(f"Checks inexistentes: {', '.join(unknown)}")
    needed = {c["engine"] for c in selected}
    versions: dict[str, str | None] = {}
    if needed:
        runner.ensure_ready(needed)
        versions = runner.versions(needed)
    known = {c["id"] for c in all_checks} | {r["id"] for r in reviewed}
    syntax: list[dict[str, Any]] = []
    pending, orphans = scan_docs(docs_root, known, syntax)
    results = [_run_check(runner, c, timeout) for c in selected]
    try:
        engines_cfg = read_yaml(paths.subject_config).get("engines", {})
    except Exception:  # noqa: BLE001
        engines_cfg = {}
    report: dict[str, Any] = {
        "subject": paths.subject,
        "generated": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "engines": {name: {"image": (engines_cfg.get(name) or {}).get("image"), "version": versions.get(name)}
                    for name in ("mssql", "mongo")},
        "checks": results,
        "reviewed": reviewed,
        "pending": pending,
        "orphan_markers": orphans,
        "syntax_templates": syntax,
        "summary": {"executed": len(results),
                    "passed": sum(r["status"] == "aprobado" for r in results),
                    "failed": sum(r["status"] == "fallido" for r in results),
                    "errors": sum(r["status"] == "error" for r in results),
                    "reviewed": len(reviewed), "pending": len(pending), "syntax_templates": len(syntax)},
    }
    out = report_path or paths.root / "reports" / "code-verification.json"
    write_json(out, report)
    atomic_write(out.with_suffix(".md"), render_markdown(report))
    return report


def render_markdown(report: dict[str, Any]) -> str:
    def cell(text: str) -> str:
        return text.replace("|", "\\|").replace("\n", " ⏎ ")

    s = report["summary"]
    out = [f"# Verificación de código: {report['subject']}", "", f"Generado: {report['generated']}", ""]
    for name, info in report["engines"].items():
        out.append(f"- {name}: {info['version'] or 'sin ejecutar'} (`{info['image']}`)")
    out += ["", f"Ejecutados {s['executed']} (aprobados {s['passed']}, fallidos {s['failed']}, errores {s['errors']}) · "
            f"pendientes de verificación específica {s['reviewed']} · sin verificar {s['pending']}", "", "## Ejecutados", ""]
    if report["checks"]:
        out += ["| ID | Motor | Estado | Salida esperada | Segundos | Mensaje |", "|---|---|---|---|---|---|"]
        for c in report["checks"]:
            out.append(f"| {c['id']} | {c['engine']} | {c['status']} | {'sí' if c['expected'] else 'no'} | "
                       f"{c['seconds']} | {cell(c['message'])} |")
    else:
        out.append("Ninguno.")
    out += ["", "## Pendientes de verificación específica (revisados sin ejecución; no cuentan como verificados)", ""]
    if report["reviewed"]:
        out += ["| ID | Página | Revisor | Fecha | Motivo |", "|---|---|---|---|---|"]
        for r in report["reviewed"]:
            out.append(f"| {r['id']} | {r['page']} | {r['reviewer']} | {r['date']} | {cell(r['reason'])} |")
    else:
        out.append("Ninguno.")
    out += ["", "## Pendientes", ""]
    if report["pending"]:
        by_page: dict[str, list[dict[str, Any]]] = {}
        for p in report["pending"]:
            by_page.setdefault(p["page"], []).append(p)
        for page, items in by_page.items():
            out.append(f"### {page} ({len(items)})")
            out += [f"- línea {i['line']}: {i['language']}" for i in items]
            out.append("")
    else:
        out += ["Ninguno.", ""]
    templates = report.get("syntax_templates") or []
    out += ["## Plantillas de sintaxis (no ejecutables; no cuentan como verificadas)", "",
            f"{len(templates)} bloques marcados con `<!-- sintaxis -->`."]
    suspicious = [t for t in templates if t.get("suspicious")]
    if suspicious:
        out += ["", "Sospechosas (parecen sentencias completas sin marcadores de posición):"]
        out += [f"- {t['page']}:{t['line']}" for t in suspicious]
    out.append("")
    if report["orphan_markers"]:
        out += ["## Marcadores sin script (sin-script)", ""]
        out += [f"- {o['id']}: {o['page']}:{o['line']}" for o in report["orphan_markers"]]
        out.append("")
    return "\n".join(out).rstrip() + "\n"
