"""Extracción con un modelo de lenguaje que devuelve JSON estructurado.

Proveedores (config: extraction.llm_provider): `anthropic` (ANTHROPIC_API_KEY) o `gemini` (GEMINI_API_KEY, vía REST con la
biblioteca estándar: no añade dependencias). El cliente se puede inyectar (así se prueba sin red ni credenciales).
Lo que el modelo devuelva pasa por la MISMA verificación literal que las reglas: si un valor no aparece en la
transcripción, queda `sin_verificar` aunque el modelo "acierte" (un modelo que corrige lo que el ASR oyó mal y
a veces acierta es tan peligroso como uno que inventa).
"""
from __future__ import annotations

import json
import os
import re
import urllib.request
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


def _llamar_gemini(modelo: str, sistema: str, texto: str) -> str:
    from dotenv import load_dotenv

    load_dotenv()
    clave = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not clave:
        raise RuntimeError("Falta GEMINI_API_KEY en .env")
    cuerpo = {"systemInstruction": {"parts": [{"text": sistema}]},
              "contents": [{"role": "user", "parts": [{"text": texto}]}],
              "generationConfig": {"temperature": 0, "responseMimeType": "application/json"}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
        data=json.dumps(cuerpo).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": clave}, method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        data = json.loads(r.read().decode("utf-8"))
    return "".join(p.get("text", "") for p in data["candidates"][0]["content"]["parts"])


def parsear_json(texto: str) -> dict[str, Any]:
    ini, fin = texto.find("{"), texto.rfind("}")
    if ini < 0 or fin < ini:
        raise ValueError(f"El modelo no devolvió JSON: {texto[:120]!r}")
    return json.loads(re.sub(r",\s*([}\]])", r"\1", texto[ini:fin + 1]))


def extraer_llm(schema: str, transcript: str, cfg: dict, cliente=None) -> dict[str, Any]:
    ex = cfg["extraction"]
    sistema = ex["prompts"][schema].replace("{fecha_referencia}", ex["reference_date"])
    if cliente is None and ex.get("llm_provider", "anthropic") == "gemini":
        crudo = _llamar_gemini(ex["llm_model"], sistema, transcript)
    else:
        crudo = _llamar(cliente or _cliente(), ex["llm_model"], sistema, transcript)
    return parsear_json(crudo)
