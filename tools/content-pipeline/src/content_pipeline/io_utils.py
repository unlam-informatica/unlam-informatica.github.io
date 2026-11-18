"""Lectura y escritura determinista de archivos (YAML, JSON, texto) y utilidades de texto."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import unicodedata
from pathlib import Path
from typing import Any

import yaml


def sha256_file(path: Path, chunk_size: int = 1 << 20) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def atomic_write(path: Path, data: str | bytes) -> bool:
    """Escribe de forma atómica. Devuelve False si el contenido ya era idéntico."""
    payload = data.encode("utf-8") if isinstance(data, str) else data
    if path.exists() and path.read_bytes() == payload:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
        os.replace(temporary, path)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise
    return True


def read_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


class _NoAliasDumper(yaml.SafeDumper):
    """Escribe cada valor completo: un catálogo editable a mano no debe tener anclas (&id001)."""

    def ignore_aliases(self, data: Any) -> bool:
        return True


def write_yaml(path: Path, data: Any, header: str | None = None) -> bool:
    body = yaml.dump(data, Dumper=_NoAliasDumper, allow_unicode=True, sort_keys=False, width=100)
    prefix = "".join(f"# {line}\n" for line in header.splitlines()) if header else ""
    return atomic_write(path, prefix + body)


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> bool:
    return atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n")


def nfc(text: str) -> str:
    """macOS guarda nombres en NFD; los catálogos usan siempre NFC."""
    return unicodedata.normalize("NFC", text)


def fold(text: str) -> str:
    """Minúsculas sin diacríticos, para comparar palabras clave y patrones."""
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(c for c in decomposed if unicodedata.category(c) != "Mn").casefold()
