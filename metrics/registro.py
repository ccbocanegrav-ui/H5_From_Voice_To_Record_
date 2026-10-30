"""Métricas de la capa de REGISTRO (no de la transcripción): ¿el campo extraído es el correcto?

Comparación por campo contra la verdad de terreno (CSV). `sin_verificar` y None cuentan como error
(no coincide con el valor real) pero se cuentan aparte para ver cuánto protege la verificación literal.
"""
from __future__ import annotations

import csv
import json
import math
from collections import Counter
from pathlib import Path

from .texto import normalizar


def cargar_gt(schema: str, ruta: str | Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    with open(ruta, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if schema == "t1":
                out[r["clip_id"]] = {
                    "anios_experiencia": float(r["anios_experiencia"]),
                    "ultimo_puesto": r["ultimo_puesto"],
                    "tecnologias": [x for x in r["tecnologias"].split("|") if x],
                    "pretension_salarial": float(r["pretension_salarial"]),
                    "disponibilidad": r["disponibilidad"],
                    "nivel_ingles": r["nivel_ingles"],
                    "moneda": r["moneda"],
                    "transcripcion_referencia": r["transcripcion_referencia"]}
            else:
                out[r["clip_id"]] = {
                    "items": json.loads(r["items"]),
                    "promocion": r["promocion"] or None,
                    "direccion_entrega": r["direccion_entrega"],
                    "metodo_pago": r["metodo_pago"],
                    "total_dicho": float(r["total_dicho"]),
                    "total_calculado": float(r["total_calculado"]),
                    "transcripcion_referencia": r["transcripcion_referencia"]}
    return out


def _n(x, cfg) -> str:
    return normalizar(str(x), cfg["normalization"]) if x is not None else ""


def _clave_item(i: dict, cfg) -> tuple:
    return (_n(i.get("producto"), cfg), _n(i.get("tamano"), cfg), i.get("cantidad"), i.get("precio_unitario"))


def comparar_campo(campo: str, pred, real, cfg: dict) -> dict:
    """{ok, sin_verificar, error (solo numéricos), pred, real}."""
    etiqueta = cfg["extraction"]["unverified_label"]
    sv = pred == etiqueta or (isinstance(pred, list) and etiqueta in pred)
    if campo == "items":
        if not isinstance(pred, list) or sv:
            ok = False
        else:
            ok = Counter(_clave_item(i, cfg) for i in pred) == Counter(_clave_item(i, cfg) for i in real)
        return {"ok": ok, "sin_verificar": sv, "pred": pred, "real": real}
    if campo == "tecnologias":
        ok = isinstance(pred, list) and not sv and {_n(x, cfg) for x in pred} == {_n(x, cfg) for x in real}
        return {"ok": ok, "sin_verificar": sv, "pred": pred, "real": real}
    if campo == "promocion":
        return {"ok": (pred or None) == (real or None), "sin_verificar": False, "pred": pred, "real": real}
    if campo in ("anios_experiencia", "pretension_salarial", "total_dicho"):
        num = isinstance(pred, (int, float)) and not isinstance(pred, bool)
        tol = 0.01 if campo == "anios_experiencia" else 0.0
        return {"ok": num and abs(pred - real) <= tol, "sin_verificar": sv,
                "error": abs(pred - real) if num else None, "pred": pred, "real": real}
    return {"ok": _n(pred, cfg) == _n(real, cfg) and not sv and pred is not None, "sin_verificar": sv,
            "pred": pred, "real": real}


def comparar_registro(schema: str, pred: dict, real: dict, cfg: dict) -> dict[str, dict]:
    return {c: comparar_campo(c, pred.get(c), real[c], cfg) for c in cfg["schemas"][schema]}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def f1_macro(preds: list, reales: list) -> float:
    clases = sorted(set(reales) | set(preds))
    fs = []
    for c in clases:
        tp = sum(p == c and r == c for p, r in zip(preds, reales))
        fp = sum(p == c and r != c for p, r in zip(preds, reales))
        fn = sum(p != c and r == c for p, r in zip(preds, reales))
        pr = tp / (tp + fp) if tp + fp else 0.0
        rc = tp / (tp + fn) if tp + fn else 0.0
        fs.append(2 * pr * rc / (pr + rc) if pr + rc else 0.0)
    return sum(fs) / len(fs) if fs else 0.0


def agregar(schema: str, comparaciones: list[dict[str, dict]], cfg: dict) -> dict[str, dict]:
    """Por campo: n, aciertos, exactitud con IC Wilson 95 %, sin_verificar, error absoluto medio (numéricos);
    macro-F1 para nivel_ingles."""
    out = {}
    for c in cfg["schemas"][schema]:
        filas = [x[c] for x in comparaciones if c in x]
        k = sum(f["ok"] for f in filas)
        lo, hi = wilson(k, len(filas))
        d = {"n": len(filas), "aciertos": k, "exactitud": k / len(filas) if filas else 0.0, "ic_lo": lo, "ic_hi": hi,
             "sin_verificar": sum(f["sin_verificar"] for f in filas)}
        errs = [f["error"] for f in filas if f.get("error") is not None]
        if errs:
            d["error_abs_medio"] = sum(errs) / len(errs)
        if c == "nivel_ingles":
            d["f1_macro"] = f1_macro([f["pred"] for f in filas], [f["real"] for f in filas])
        out[c] = d
    return out
