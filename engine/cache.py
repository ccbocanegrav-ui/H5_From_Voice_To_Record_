"""Caché de transcripciones (se commitea; los audios y los pesos no).

Un archivo por clip y por configuración:
    data/cache/asr/<modelo>__<device>__<compute>__<plano|glosario>/<clip>.json
Así CPU vs GPU, float16 vs int8 y plano vs glosario conviven sin pisarse, y la app/CI solo leen.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import resolver_ruta


def nombre_config(modelo: str, device: str, compute: str, glosario: bool) -> str:
    return f"{modelo}__{device}__{compute}__{'glosario' if glosario else 'plano'}"


def ruta(cfg: dict[str, Any], modelo: str, device: str, compute: str, glosario: bool, clip: str) -> Path:
    base = resolver_ruta(cfg, cfg["paths"]["cache_dir"]) / "asr"
    return base / nombre_config(modelo, device, compute, glosario) / f"{clip}.json"


def leer(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def escribir(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
