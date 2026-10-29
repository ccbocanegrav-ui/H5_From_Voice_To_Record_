"""Carga de config.yaml. Las rutas relativas se resuelven contra la carpeta del config (raíz del repo)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path = "config.yaml") -> dict[str, Any]:
    p = Path(path)
    if not p.is_absolute() and not p.exists():
        p = Path(__file__).resolve().parent.parent / p     # fallback: raíz del repo
    with open(p, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    cfg["_root"] = str(p.resolve().parent)
    return cfg


def resolver_ruta(cfg: dict[str, Any], relativa: str | Path) -> Path:
    p = Path(relativa)
    return p if p.is_absolute() else Path(cfg["_root"]) / p
