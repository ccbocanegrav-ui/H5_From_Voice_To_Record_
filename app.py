"""De la voz al registro — app Streamlit. Un solo comando:  streamlit run app.py

La app NO transcribe ni extrae por su cuenta: llama a engine.process_audio (el mismo motor que los scripts).
Para los clips del corpus usa la caché de transcripciones (no necesita GPU); para un audio subido corre el modelo.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import pandas as pd
import streamlit as st

from engine import process_audio
from engine.config import load_config, resolver_ruta
from metrics import registro as mr
from validation import validar

st.set_page_config(page_title="De la voz al registro", layout="wide")
CFG = load_config("config.yaml")
ETIQUETA = CFG["extraction"]["unverified_label"]
NOMBRES = {"t1": "Entrevista de trabajo", "t2": "Llamada de venta (restaurante)"}


@st.cache_data
def gt(schema: str) -> dict:
    return mr.cargar_gt(schema, resolver_ruta(CFG, CFG["paths"][f"ground_truth_{schema}"]))


def leer_md(nombre: str) -> str | None:
    """Lee un .md de results/. Quita las comillas de código (se verían verdes) y baja un nivel los títulos."""
    p = resolver_ruta(CFG, CFG["paths"]["results_dir"]) / nombre
    if not p.exists():
        return None
    out = []
    for linea in p.read_text(encoding="utf-8").replace("`", "").splitlines():
        if linea.startswith("## "):
            linea = "#### " + linea[3:]
        elif linea.startswith("# "):
            linea = "### " + linea[2:]
        out.append(linea)
    return "\n".join(out)


def mostrar_imagen(nombre: str) -> None:
    img = resolver_ruta(CFG, CFG["paths"]["results_dir"]) / nombre
    if img.exists():
        st.image(str(img))


def mostrar_campos(schema: str, r: dict) -> None:
    filas = []
    for c in CFG["schemas"][schema]:
        v = r["fields"].get(c)
        if c == "items" and isinstance(v, list):
            v = "; ".join(f"{i['cantidad']}× {i['producto']}" + (f" ({i['tamano']})" if i.get("tamano") else "") for i in v)
        if isinstance(v, list):
            v = ", ".join(map(str, v))
        ok = r["verified"].get(c)
        estado = "sin dato" if v is None else ("✔ verificado" if ok else "✘ sin verificar")
        filas.append({"Campo": c, "Valor": "—" if v is None else str(v), "Estado": estado})
    st.dataframe(pd.DataFrame(filas), hide_index=True, width="stretch")
    if schema == "t1":
        st.caption(f"Moneda detectada: {r['fields'].get('moneda') or '—'}")


def mostrar_pedido(r: dict) -> None:
    f = r["fields"]
    items = f.get("items")
    st.subheader("Pedido final")
    if isinstance(items, list) and items:
        df = pd.DataFrame([{"Producto": i["producto"], "Tamaño": i.get("tamano") or "—", "Cant.": i["cantidad"],
                            "Precio": i.get("precio_unitario"),
                            "Subtotal": (i["cantidad"] * i["precio_unitario"]) if i.get("precio_unitario") is not None else None,
                            "Verificado": "✔" if i.get("verificado") else "✘"} for i in items])
        st.dataframe(df, hide_index=True, width="stretch")
    else:
        st.info("No se pudo armar el pedido (ítems ausentes o sin verificar).")
    v = validar(items, f.get("promocion"), f.get("total_dicho"), CFG)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total dicho", f"S/ {v['total_dicho']}" if v["total_dicho"] is not None else "—")
    c2.metric("Total calculado", f"S/ {v['total_calculado']}" if v["total_calculado"] is not None else "—")
    c3.metric("Diferencia", f"{v['diferencia']:+}" if v["diferencia"] is not None else "—")
    if v["estado"] == "ok":
        st.success("El total dicho coincide con cantidad × precio − promoción.")
    elif v["estado"] == "inconsistente":
        st.error("El total dicho NO coincide con el cálculo. Revisar: puede ser un error del hablante o del reconocimiento.")
    else:
        st.warning("No se puede validar la aritmética (faltan ítems, precios o total).")


def comparar_con_referencia(schema: str, clip: str, r: dict) -> None:
    real = gt(schema)[clip]
    comp = mr.comparar_registro(schema, r["fields"], real, CFG)
    filas = [{"Campo": c, "¿Correcto?": "✔" if v["ok"] else "✘", "Obtenido": str(v["pred"]), "Referencia": str(v["real"])}
             for c, v in comp.items()]
    st.subheader("Comparación con la verdad de terreno")
    st.dataframe(pd.DataFrame(filas), hide_index=True, width="stretch")
    t = __import__("metrics.texto", fromlist=["tasas"]).tasas(real["transcripcion_referencia"], r["transcript"], CFG["normalization"])
    st.caption(f"WER {100 * t['wer']:.1f} % · CER {100 * t['cer']:.1f} % para este clip")


tab1, tab2, tab3, tab4 = st.tabs(["Procesar audio", "Resultados T1", "Resultados T2 y degradación", "Cómo funciona"])

with tab1:
    st.title("De la voz al registro")
    schema = st.radio("Tipo de audio", ["t1", "t2"], format_func=NOMBRES.get, horizontal=True)
    fuente = st.radio("Fuente", ["Clip del corpus (usa la caché, sin GPU)", "Subir un audio"], horizontal=True)
    metodo = st.selectbox("Método de extracción", ["rules", "llm"], index=0 if CFG["extraction"]["method"] == "rules" else 1,
                          help="rules: expresiones regulares. llm: requiere ANTHROPIC_API_KEY en .env")
    r, clip = None, None
    if fuente.startswith("Clip"):
        clip = st.selectbox("Clip", list(gt(schema)))
        if st.button("Procesar", type="primary"):
            r = process_audio(f"data/audio/{clip}.m4a", schema, cache_only=True, metodo=metodo)
    else:
        modelo = st.selectbox("Modelo", ["small", "large-v3"], help="small funciona en CPU; large-v3 conviene con GPU")
        archivo = st.file_uploader("Audio", type=["m4a", "wav", "mp3", "ogg", "flac"])
        if archivo and st.button("Transcribir y extraer", type="primary"):
            with tempfile.NamedTemporaryFile(suffix=Path(archivo.name).suffix, delete=False) as tmp:
                tmp.write(archivo.getbuffer())
            with st.spinner("Transcribiendo… en CPU puede tardar varios minutos"):
                r = process_audio(tmp.name, schema, use_cache=False, model_name=modelo, metodo=metodo)
    if r is not None:
        if r["error"]:
            st.error(r["error"])
        else:
            c1, c2, c3 = st.columns(3)
            c1.metric("Dispositivo (leído de la librería)", r["device"])
            c2.metric("Tiempo", f"{r['elapsed_s']} s")
            c3.metric("Origen", "caché" if r["cache_hit"] else f"modelo {r['model']}")
            st.subheader("Transcripción")
            st.text_area("Transcripción", r["transcript"], height=220, label_visibility="collapsed")
            st.subheader("Registro extraído")
            mostrar_campos(schema, r)
            if schema == "t2":
                mostrar_pedido(r)
            if clip:
                comparar_con_referencia(schema, clip, r)

with tab2:
    st.header("Resultados T1 — entrevistas")
    mostrar_imagen("exactitud_campos_t1.png")
    mostrar_imagen("curva_degradacion_t1.png")
    st.markdown(leer_md("asr_benchmark_t1.md") or "_Falta results/asr_benchmark_t1.md_")
    st.markdown(leer_md("evaluacion_t1.md") or "_Falta results/evaluacion_t1.md (python scripts/evaluar.py --task t1)_")

with tab3:
    st.header("Resultados T2 — llamadas y escalera de degradación")
    mostrar_imagen("curva_degradacion_t2.png")
    mostrar_imagen("exactitud_campos_t2.png")
    st.markdown(leer_md("evaluacion_t2.md") or "_Falta results/evaluacion_t2.md (python scripts/evaluar.py --task t2 --ladder)_")

with tab4:
    st.header("Cómo funciona")
    st.markdown(
        "1. **Transcripción** con faster-whisper (el dispositivo se lee de la librería; sin caída silenciosa a CPU).\n"
        "2. **Extracción** de campos por reglas o por LLM.\n"
        "3. **Verificación literal**: un valor que no está en la transcripción queda como `sin_verificar`.\n"
        "4. **Validación aritmética** (T2): cantidad × precio − promoción = total dicho.\n"
        "5. **Dos capas de métricas**: WER/CER del texto y exactitud por campo del registro.\n\n"
        "Detalle, comandos y limitaciones en el README del repositorio.")
