"""Rutas y configuración declarativa por materia.

Cada materia vive en ``academic-sources/<materia>/``:

- ``subject.yaml``: reglas de clasificación (versionado).
- ``catalog.yaml``: inventario con hashes y procedencia (versionado, sin rutas absolutas).
- ``curriculum-map.yaml``: matriz de cobertura curricular (versionado).
- ``raw/`` y ``processed/``: fuentes privadas y derivados (ignorados por Git).
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .io_utils import read_yaml


class PipelineError(Exception):
    """Error esperado del pipeline; la CLI lo informa sin traza."""


def find_repo_root(start: Path | None = None) -> Path:
    """Sube desde ``start`` hasta encontrar la carpeta que contiene ``academic-sources``."""
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "academic-sources").is_dir():
            return candidate
    raise PipelineError(
        "No se encontró la carpeta academic-sources/. Ejecutá el comando dentro del "
        "repositorio o indicá --sources-root."
    )


def default_sources_root() -> Path:
    env = os.environ.get("CONTENT_PIPELINE_SOURCES")
    return Path(env).resolve() if env else find_repo_root() / "academic-sources"


@dataclass(frozen=True)
class SubjectPaths:
    """Ubicación de cada artefacto de una materia."""

    subject: str
    root: Path

    @property
    def raw(self) -> Path:
        return self.root / "raw"

    @property
    def processed(self) -> Path:
        return self.root / "processed"

    @property
    def markdown(self) -> Path:
        return self.processed / "markdown"

    @property
    def json(self) -> Path:
        return self.processed / "json"

    @property
    def images(self) -> Path:
        return self.processed / "images"

    @property
    def normalized(self) -> Path:
        return self.processed / "normalized"

    @property
    def index(self) -> Path:
        return self.processed / "index"

    @property
    def context(self) -> Path:
        return self.processed / "context"

    @property
    def reports(self) -> Path:
        return self.processed / "reports"

    @property
    def manifest(self) -> Path:
        return self.processed / "manifest.json"

    @property
    def catalog(self) -> Path:
        return self.root / "catalog.yaml"

    @property
    def subject_config(self) -> Path:
        return self.root / "subject.yaml"

    @property
    def curriculum(self) -> Path:
        return self.root / "curriculum-map.yaml"


def subject_paths(subject: str, sources_root: Path | None = None) -> SubjectPaths:
    if not subject or "/" in subject or subject.startswith("."):
        raise PipelineError(f"Identificador de materia inválido: {subject!r}")
    root = (sources_root or default_sources_root()) / subject
    if not root.is_dir():
        raise PipelineError(f"No existe la carpeta de la materia: {root}")
    return SubjectPaths(subject=subject, root=root)


DEFAULT_SUBJECT_CONFIG: dict[str, Any] = {
    "defaults": {
        "doc_type": "otro",
        "license": "sin-determinar",
        "distribution": "privado",
        "extraction": "full",
        "units": [],
        "topics": [],
        "source": None,
        "version": None,
    },
    "rules": [],
}


def load_subject_config(paths: SubjectPaths) -> dict[str, Any]:
    """Lee ``subject.yaml`` y completa los valores por defecto."""
    config: dict[str, Any] = {
        "id": paths.subject,
        "id_prefix": paths.subject,
        "defaults": dict(DEFAULT_SUBJECT_CONFIG["defaults"]),
        "rules": [],
    }
    if paths.subject_config.exists():
        data = read_yaml(paths.subject_config) or {}
        if not isinstance(data, dict):
            raise PipelineError(f"{paths.subject_config.name} debe ser un mapa YAML")
        config.update({k: v for k, v in data.items() if k not in ("defaults", "rules")})
        config["defaults"].update(data.get("defaults") or {})
        config["rules"] = list(data.get("rules") or [])
    for position, rule in enumerate(config["rules"], start=1):
        if not isinstance(rule, dict) or "match" not in rule:
            raise PipelineError(f"La regla {position} de subject.yaml necesita la clave 'match'")
    return config
