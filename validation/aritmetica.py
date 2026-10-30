"""Validador aritmético de T2: cantidad × precio unitario − promoción = total que dijo el vendedor.

Es una validación que NO depende del ASR: si el registro es internamente inconsistente, algo falló
(el ASR oyó mal un precio/cantidad, o el HABLANTE se equivocó al sumar). `diagnostico` los separa
comparando contra el registro de referencia (lo que realmente se dijo).
"""
from __future__ import annotations

from math import floor
from typing import Any


def _regla_promo(promocion: str | None, cfg: dict) -> dict | None:
    for p in cfg["extraction"]["t2"]["promos"]:
        if p["etiqueta"] == promocion:
            return p["regla"]
    return None


def total_calculado(items: list[dict], promocion: str | None, cfg: dict) -> float | None:
    """None si no se puede calcular (ítems ausentes, sin_verificar, o sin precio)."""
    if not isinstance(items, list) or not items:
        return None
    if any(i.get("precio_unitario") is None or i.get("cantidad") is None for i in items):
        return None
    subtotal = sum(i["cantidad"] * i["precio_unitario"] for i in items)
    r = _regla_promo(promocion, cfg)
    if r is None:
        return subtotal
    if r["tipo"] == "descuento_fijo":
        return subtotal - r["monto"] if subtotal >= r["minimo"] else subtotal
    if r["tipo"] == "n_por_m":
        desc = 0
        for i in items:
            if i["producto"] == r["producto"] and (r.get("tamano") is None or i.get("tamano") == r["tamano"]):
                desc += floor(i["cantidad"] / r["lleva"]) * (r["lleva"] - r["paga"]) * i["precio_unitario"]
        return subtotal - desc
    return subtotal


def validar(items: Any, promocion: str | None, total_dicho: Any, cfg: dict) -> dict:
    tol = cfg["validation"]["tolerancia_soles"]
    calc = total_calculado(items, promocion, cfg) if isinstance(items, list) else None
    if calc is None or not isinstance(total_dicho, (int, float)):
        return {"total_calculado": calc, "total_dicho": total_dicho, "diferencia": None,
                "consistente": None, "estado": "no_calculable"}
    dif = round(total_dicho - calc, 2)
    ok = abs(dif) <= tol
    return {"total_calculado": calc, "total_dicho": total_dicho, "diferencia": dif,
            "consistente": ok, "estado": "ok" if ok else "inconsistente"}


def diagnostico(val_asr: dict, val_ref: dict) -> str:
    """'hablante' si la referencia ya es inconsistente (el error está en lo que se dijo);
    'asr' si la referencia cuadra pero el registro obtenido de la transcripción no;
    'ok' si cuadra; 'no_calculable' si no se pudo validar el registro del ASR."""
    if val_ref.get("consistente") is False:
        return "hablante"
    if val_asr.get("consistente") is False:
        return "asr"
    if val_asr.get("consistente") is None:
        return "no_calculable"
    return "ok"
