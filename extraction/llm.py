"""Extracción con un modelo de lenguaje que devuelve JSON estructurado.

Necesita ANTHROPIC_API_KEY en .env. El cliente se puede inyectar (así se prueba sin red ni credenciales).
Lo que el modelo devuelva pasa por la MISMA verificación literal que las reglas: si un valor no aparece en la
transcripción, queda `sin_verificar` aunque el modelo "acierte" (un modelo que corrige lo que el ASR oyó mal y
a veces acierta es tan peligroso como uno que inventa).
"""
from __future__ import annotations

import json
import re
from typing import Any


def _cliente():
    from dotenv import load_dotenv
    import anthropic

    load_dotenv()
    return anthropic.Anthropic()


def _llamar(cliente, modelo: str, sistema: str, texto: str) -> str:
    base = dict(model=modelo, max_tokens=1500, system=sistema, messages=[{"role": "user", "content": texto}])
    try:
        msg = cliente.messages.create(temperature=0, **base)
    except Exception as e:                                   # algunos modelos no aceptan `temperature`
        if "temperature" not in str(e).lower():
            raise
        msg = cliente.messages.create(**base)
    return "".join(getattr(b, "text", "") for b in msg.content)


def parsear_json(texto: str) -> dict[str, Any]:
    ini, fin = texto.find("{"), texto.rfind("}")
    if ini < 0 or fin < ini:
        raise ValueError(f"El modelo no devolvió JSON: {texto[:120]!r}")
    return json.loads(re.sub(r",\s*([}\]])", r"\1", texto[ini:fin + 1]))


def extraer_llm(schema: str, transcript: str, cfg: dict, cliente=None) -> dict[str, Any]:
    ex = cfg["extraction"]
    sistema = ex["prompts"][schema].replace("{fecha_referencia}", ex["reference_date"])
    cliente = cliente or _cliente()
    crudo = _llamar(cliente, ex["llm_model"], sistema, transcript)
    return parsear_json(crudo)
