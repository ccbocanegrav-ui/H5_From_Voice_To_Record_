"""Normalización de texto y métricas de transcripción (WER, CER) con intervalos de confianza.

REGLA DE NORMALIZACIÓN (se aplica IGUAL a la referencia y a la hipótesis antes de comparar):
  1. Unicode NFC y minúsculas.
  2. Moneda y porcentaje: "S/ 6,500" -> "6500 soles"; "$900" -> "900 dólares"; "30 %" -> "30 por ciento".
  3. Separadores de miles se eliminan ("6.500" / "6,500" -> "6500"); coma decimal -> punto ("3,5" -> "3.5").
  4. Se separan dígitos de letras ("4B" -> "4 b", "C1" -> "c 1") y se quitan marcas ordinales (1º -> 1).
  5. Se elimina la puntuación (se conserva el punto entre dígitos).
  6. Números hablados -> dígitos ("seis mil quinientos" -> "6500"), ver numeros.py.
  7. "primero de" -> "1 de" (fechas).
  8. Los acentos NO se eliminan (config: strip_accents=false); se colapsan espacios.
Sin esta normalización, un punto o una mayúscula contarían como error y el WER saldría inflado.
"""
from __future__ import annotations

import re
import unicodedata

import numpy as np

from . import numeros

NORM_DEFAULT = {
    "lowercase": True,
    "strip_punctuation": True,
    "strip_accents": False,
    "collapse_whitespace": True,
    "numbers_to_digits": True,
}

_RE_SOLES = re.compile(r"\bs/\.?\s*(\d(?:[\d.,]*\d)?)")
_RE_DOLAR = re.compile(r"(?:\bus)?\$\s*(\d(?:[\d.,]*\d)?)")
_RE_USD = re.compile(r"(\d(?:[\d.,]*\d)?)\s*usd\b")
_RE_PCT = re.compile(r"(\d)\s*%")
_RE_MILES = re.compile(r"(?<![\d.,])(\d{1,3})((?:[.,]\d{3})+)(?!\d)")
_RE_DECIMAL = re.compile(r"(?<=\d),(?=\d{1,2}(?!\d))")
_RE_ORDINAL = re.compile(r"(?<=\d)[º°ª]")
_RE_DIGLET = re.compile(r"(?<=\d)(?=[^\W\d_])|(?<=[^\W\d_])(?=\d)")
_RE_PUNT = re.compile(r"[^\w\s.]")
_RE_PUNTO = re.compile(r"(?<!\d)\.|\.(?!\d)")


def normalizar(texto: str, cfg: dict | None = None) -> str:
    c = {**NORM_DEFAULT, **(cfg or {})}
    s = unicodedata.normalize("NFC", texto or "")
    if c["lowercase"]:
        s = s.lower()
    s = _RE_SOLES.sub(r"\1 soles", s)
    s = _RE_DOLAR.sub(r"\1 dólares", s)
    s = _RE_USD.sub(r"\1 dólares", s)
    s = _RE_PCT.sub(r"\1 por ciento", s)
    s = _RE_MILES.sub(lambda m: m.group(1) + re.sub(r"[.,]", "", m.group(2)), s)
    s = _RE_DECIMAL.sub(".", s)
    s = _RE_ORDINAL.sub("", s)
    s = _RE_DIGLET.sub(" ", s)
    if c["strip_punctuation"]:
        s = _RE_PUNT.sub(" ", s)
        s = _RE_PUNTO.sub(" ", s)
    toks = s.split()
    if c["numbers_to_digits"]:
        toks = numeros.palabras_a_digitos(toks)
    s = " ".join(toks)
    s = re.sub(r"\bprimero de\b", "1 de", s)
    if c["strip_accents"]:
        s = numeros.sin_acentos(s)
    if c["collapse_whitespace"]:
        s = " ".join(s.split())
    return s


def _conteos(ref: str, hip: str, nivel: str) -> tuple[int, int]:
    """(errores, tamaño_de_la_referencia) a nivel 'palabras' o 'caracteres'."""
    import jiwer

    if not ref:
        raise ValueError("La referencia normalizada quedó vacía")
    if not hip:
        n = len(ref.split()) if nivel == "palabras" else len(ref)
        return n, n
    if nivel == "palabras":
        o = jiwer.process_words(ref, hip)
        return o.substitutions + o.deletions + o.insertions, o.substitutions + o.deletions + o.hits
    o = jiwer.process_characters(ref, hip)
    return o.substitutions + o.deletions + o.insertions, o.substitutions + o.deletions + o.hits


def tasas(referencia: str, hipotesis: str, cfg: dict | None = None) -> dict:
    """WER y CER de un clip (ambos textos se normalizan igual)."""
    r, h = normalizar(referencia, cfg), normalizar(hipotesis, cfg)
    w_err, w_ref = _conteos(r, h, "palabras")
    c_err, c_ref = _conteos(r, h, "caracteres")
    return {"w_err": w_err, "w_ref": w_ref, "c_err": c_err, "c_ref": c_ref,
            "wer": w_err / w_ref, "cer": c_err / c_ref}


def agregado(errs, refs) -> float:
    return float(np.sum(errs) / np.sum(refs))


def bootstrap_ci(errs, refs, n: int = 2000, seed: int = 0, nivel: float = 0.95) -> tuple[float, float]:
    """IC por bootstrap sobre CLIPS (se remuestrean clips, se recalcula la tasa agregada)."""
    errs, refs = np.asarray(errs, float), np.asarray(refs, float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(errs), size=(n, len(errs)))
    vals = errs[idx].sum(1) / refs[idx].sum(1)
    a = (1 - nivel) / 2
    return float(np.quantile(vals, a)), float(np.quantile(vals, 1 - a))


def bootstrap_diff(errs_a, refs_a, errs_b, refs_b, n: int = 2000, seed: int = 0,
                   nivel: float = 0.95) -> tuple[float, float, float]:
    """Diferencia pareada de tasas (a - b) con IC. Los clips deben ser los mismos y estar en el mismo orden."""
    ea, ra = np.asarray(errs_a, float), np.asarray(refs_a, float)
    eb, rb = np.asarray(errs_b, float), np.asarray(refs_b, float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(ea), size=(n, len(ea)))
    vals = ea[idx].sum(1) / ra[idx].sum(1) - eb[idx].sum(1) / rb[idx].sum(1)
    a = (1 - nivel) / 2
    obs = float(ea.sum() / ra.sum() - eb.sum() / rb.sum())
    return obs, float(np.quantile(vals, a)), float(np.quantile(vals, 1 - a))


def _apariciones(texto_norm: str, termino_norm: str) -> int:
    return len(re.findall(rf"(?<!\S){re.escape(termino_norm)}(?!\S)", texto_norm))


def glosario_recall(referencia: str, hipotesis: str, terminos: list[str],
                    cfg: dict | None = None) -> tuple[int, int]:
    """(términos del glosario acertados, términos del glosario presentes en la referencia).

    Mide lo que el glosario debería mejorar: nombres propios técnicos dentro del español.
    """
    r, h = normalizar(referencia, cfg), normalizar(hipotesis, cfg)
    hits = total = 0
    for t in terminos:
        tn = normalizar(t, cfg)
        n_ref = _apariciones(r, tn)
        total += n_ref
        hits += min(_apariciones(h, tn), n_ref)
    return hits, total
