"""Utilidades comunes de extracción. Todo el texto se trabaja NORMALIZADO (metrics.texto.normalizar):
minúsculas, sin puntuación, números hablados convertidos a dígitos ("seis mil quinientos" -> "6500")."""
from __future__ import annotations

import re

from metrics.texto import normalizar


def norm(texto: str, cfg: dict) -> str:
    return normalizar(texto, cfg["normalization"])


def contiene(t: str, s: str) -> bool:
    """¿`s` aparece en `t` como palabra(s) completa(s)? (ambos ya normalizados)."""
    return bool(s) and re.search(rf"(?<!\S){re.escape(s)}(?!\S)", t) is not None


def posiciones(t: str, s: str) -> list[int]:
    return [m.start() for m in re.finditer(rf"(?<!\S){re.escape(s)}(?!\S)", t)] if s else []


def plural(palabra: str) -> str:
    """Regex de una palabra que acepta singular y plural: pollo/pollos, arroz/arroces, tallarín/tallarines,
    porción/porciones, personal/personales."""
    if palabra.endswith("z"):
        return rf"(?:{re.escape(palabra)}|{re.escape(palabra[:-1])}ces)"
    sin_tilde = {"ín": "in", "ón": "on", "án": "an", "én": "en", "ún": "un"}
    for con, sin in sin_tilde.items():
        if palabra.endswith(con):
            return rf"(?:{re.escape(palabra)}|{re.escape(palabra[:-2] + sin)}es)"
    return rf"{re.escape(palabra)}(?:es|s)?"
