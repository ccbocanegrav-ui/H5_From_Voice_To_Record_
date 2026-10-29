"""Benchmark de ASR (Tarea 1, Fase 2). Se corre en Colab con GPU:

    python scripts/benchmark_asr.py --task t1

Mide, por experimento (modelo x dispositivo x precisión x glosario):
  WER y CER (con IC95 por bootstrap sobre clips), segundos por minuto de audio, VRAM pico,
  dispositivo LEÍDO de la librería y si el texto cambió respecto a otro experimento.
Guarda results/asr_benchmark_<tarea>.{json,csv,md} y una transcripción en caché por clip y experimento.
"""
from __future__ import annotations

import argparse
import csv
import gc
import importlib.metadata as md
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine import asr, cache, gpu                      # noqa: E402
from engine.config import load_config, resolver_ruta    # noqa: E402
from metrics import texto as mt                         # noqa: E402

EXTS = (".m4a", ".wav", ".mp3", ".ogg", ".flac", ".aac", ".opus", ".mp4", ".webm")


def cargar_referencias(cfg: dict, tarea: str) -> dict[str, str]:
    ruta = resolver_ruta(cfg, cfg["paths"][f"ground_truth_{tarea}"])
    with open(ruta, encoding="utf-8") as f:
        return {r["clip_id"]: r["transcripcion_referencia"] for r in csv.DictReader(f)}


def buscar_audio(cfg: dict, clip: str) -> Path | None:
    base = resolver_ruta(cfg, cfg["paths"]["audio_dir"])
    for ext in EXTS:
        p = base / f"{clip}{ext}"
        if p.exists():
            return p
    return None


def info_entorno() -> dict:
    def ver(pkg):
        try:
            return md.version(pkg)
        except md.PackageNotFoundError:
            return None

    return {"fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "python": platform.python_version(),
            "faster_whisper": ver("faster-whisper"), "ctranslate2": ver("ctranslate2"), "jiwer": ver("jiwer"),
            **gpu.info_gpu()}


def correr_experimento(exp: dict, clips: list[str], refs: dict, cfg: dict, mod_asr=asr) -> dict:
    """Corre un experimento sobre `clips` y devuelve métricas por clip y agregadas."""
    bench, norm = cfg["benchmark"], cfg["normalization"]
    terminos = cfg["asr"]["glossary"].get(exp.get("tarea", "t1")) if exp.get("glosario") else None
    usados = clips[: exp["max_clips"]] if exp.get("max_clips") else clips

    muestreador = gpu.MuestreadorGPU()
    muestreador.iniciar()
    modelo, info = mod_asr.cargar_modelo(exp["model"], exp["device"], exp["compute_type"], cfg)
    if exp["device"] == "cuda" and usados:       # calentamiento: la 1ª pasada incluye inicialización de CUDA
        mod_asr.transcribir(modelo, buscar_audio(cfg, usados[0]), cfg, terminos)

    filas = []
    for clip in usados:
        audio = buscar_audio(cfg, clip)
        out = mod_asr.transcribir(modelo, audio, cfg, terminos)
        t = mt.tasas(refs[clip], out["texto"], norm)
        g_hits, g_tot = mt.glosario_recall(refs[clip], out["texto"], cfg["asr"]["glossary"].get("t1", []), norm)
        cache.escribir(cache.ruta(cfg, exp["model"], info["device_leido"], exp["compute_type"], bool(terminos), clip), {
            "clip": clip, "audio": audio.name, "texto": out["texto"], "segmentos": out["segmentos"],
            "duracion_audio_s": out["duracion_audio_s"], "tiempo_transcripcion_s": out["tiempo_transcripcion_s"],
            "modelo": exp["model"], "device_leido": info["device_leido"], "compute_leido": info["compute_leido"],
            "compute_pedido": exp["compute_type"], "glosario": bool(terminos),
            "mecanismo_glosario": out["mecanismo_glosario"], "experimento": exp["id"],
            "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds")})
        filas.append({"clip": clip, "texto": out["texto"], "dur_s": out["duracion_audio_s"],
                      "t_s": out["tiempo_transcripcion_s"], "glos_hits": g_hits, "glos_total": g_tot, **t})
    vram = muestreador.detener()
    del modelo
    gc.collect()
    time.sleep(1.5)                              # deja que nvidia-smi vea la memoria liberada antes del siguiente

    errs_w = [f["w_err"] for f in filas]
    refs_w = [f["w_ref"] for f in filas]
    errs_c = [f["c_err"] for f in filas]
    refs_c = [f["c_ref"] for f in filas]
    dur_min = sum(f["dur_s"] for f in filas) / 60
    usa_gpu = (info["device_leido"] == "cuda" and vram["vram_delta_mb"] is not None
               and vram["vram_delta_mb"] >= bench["vram_minima_mb"])
    return {
        "id": exp["id"], "modelo": exp["model"], "precision": info["compute_leido"], "glosario": bool(terminos),
        "device_pedido": exp["device"], "device_leido": info["device_leido"], "n_clips": len(filas),
        "fallback_silencioso": info["fallback_silencioso"], "carga_s": info["carga_s"],
        "wer": mt.agregado(errs_w, refs_w), "wer_ic95": mt.bootstrap_ci(errs_w, refs_w, bench["bootstrap_n"], bench["bootstrap_seed"]),
        "cer": mt.agregado(errs_c, refs_c), "cer_ic95": mt.bootstrap_ci(errs_c, refs_c, bench["bootstrap_n"], bench["bootstrap_seed"]),
        "seg_por_min_audio": sum(f["t_s"] for f in filas) / dur_min if dur_min else None,
        "glosario_recall": (sum(f["glos_hits"] for f in filas) / max(sum(f["glos_total"] for f in filas), 1)),
        **vram, "gpu_verificada": bool(usa_gpu), "filas": filas,
    }


def comparar(a: dict, b: dict, cfg: dict) -> dict:
    """A frente a B sobre los clips que ambos procesaron (pareado)."""
    bench, norm = cfg["benchmark"], cfg["normalization"]
    fa, fb = {f["clip"]: f for f in a["filas"]}, {f["clip"]: f for f in b["filas"]}
    comunes = sorted(set(fa) & set(fb))
    ea, ra = [fa[c]["w_err"] for c in comunes], [fa[c]["w_ref"] for c in comunes]
    eb, rb = [fb[c]["w_err"] for c in comunes], [fb[c]["w_ref"] for c in comunes]
    diff, lo, hi = mt.bootstrap_diff(ea, ra, eb, rb, bench["bootstrap_n"], bench["bootstrap_seed"])
    cambian = sum(mt.normalizar(fa[c]["texto"], norm) != mt.normalizar(fb[c]["texto"], norm) for c in comunes)

    def spm(f, cl):
        return sum(f[c]["t_s"] for c in cl) / (sum(f[c]["dur_s"] for c in cl) / 60)

    def rec(f, cl):
        return sum(f[c]["glos_hits"] for c in cl) / max(sum(f[c]["glos_total"] for c in cl), 1)

    return {"a": a["id"], "b": b["id"], "n_clips": len(comunes), "clips": comunes,
            "wer_a": sum(ea) / sum(ra), "wer_b": sum(eb) / sum(rb), "dif_wer_a_menos_b": diff, "dif_ic95": (lo, hi),
            "clips_con_texto_distinto": cambian, "spm_a": spm(fa, comunes), "spm_b": spm(fb, comunes),
            "velocidad_b_sobre_a": spm(fb, comunes) / spm(fa, comunes),
            "vram_a_mb": a["vram_delta_mb"], "vram_b_mb": b["vram_delta_mb"],
            "glos_recall_a": rec(fa, comunes), "glos_recall_b": rec(fb, comunes)}


def pct(x):
    return "—" if x is None else f"{100 * x:.1f}%"


def tabla_md(res: list[dict], comps: dict[str, list[dict]], entorno: dict, tarea: str) -> str:
    L = [f"# Benchmark ASR — {tarea.upper()}", "",
         f"Entorno: {entorno.get('gpu', 'sin GPU')} · driver {entorno.get('driver', '—')} · "
         f"faster-whisper {entorno.get('faster_whisper')} · ctranslate2 {entorno.get('ctranslate2')} · {entorno['fecha_utc']}", "",
         "IC95% por bootstrap sobre clips. Con pocos clips los intervalos son anchos: léelos como orden de magnitud.", "",
         "## Experimentos", "",
         "| Experimento | Modelo | Dispositivo leído | Precisión | Clips | WER [IC95] | CER | s por min de audio | VRAM pico (MB) | GPU verificada |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        vram = "—" if r["vram_delta_mb"] is None else f"{r['vram_delta_mb']}"
        L.append(f"| {r['id']} | {r['modelo']}{' + glosario' if r['glosario'] else ''} | {r['device_leido']} | {r['precision']} | "
                 f"{r['n_clips']} | {pct(r['wer'])} [{pct(r['wer_ic95'][0])}–{pct(r['wer_ic95'][1])}] | {pct(r['cer'])} | "
                 f"{r['seg_por_min_audio']:.1f} | {vram} | {'sí' if r['gpu_verificada'] else 'no'} |")
    titulos = {"precision": "Precisión numérica (¿cambió el texto?)", "dispositivo": "CPU frente a GPU (mismos clips)",
               "glosario": "Glosario de dominio: plano (A) frente a con vocabulario (B)", "tamano": "Tamaño de modelo"}
    for clave, lista in comps.items():
        if not lista:
            continue
        L += ["", f"## {titulos.get(clave, clave)}", "",
              "| A | B | Clips | WER A | WER B | A − B [IC95] | Clips con texto distinto | s/min A → B | VRAM A → B (MB) | Recall glosario A → B |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for c in lista:
            L.append(f"| {c['a']} | {c['b']} | {c['n_clips']} | {pct(c['wer_a'])} | {pct(c['wer_b'])} | "
                     f"{100 * c['dif_wer_a_menos_b']:+.2f} pp [{100 * c['dif_ic95'][0]:+.2f}, {100 * c['dif_ic95'][1]:+.2f}] | "
                     f"{c['clips_con_texto_distinto']} de {c['n_clips']} | {c['spm_a']:.1f} → {c['spm_b']:.1f} | "
                     f"{c['vram_a_mb']} → {c['vram_b_mb']} | {pct(c['glos_recall_a'])} → {pct(c['glos_recall_b'])} |")
    L += ["", "Lectura: «A − B» positivo en precisión/dispositivo significa que B es MEJOR (menos errores) que A; "
          "en glosario, positivo significa que el glosario (B) mejora. Si el IC incluye 0, no se distingue del azar.", ""]
    return "\n".join(L)


def ejecutar(cfg: dict, tarea: str, solo: list[str] | None, sin_cpu: bool, mod_asr=asr, salida: Path | None = None) -> dict:
    refs = cargar_referencias(cfg, tarea)
    clips = sorted(refs)
    faltan = [c for c in clips if buscar_audio(cfg, c) is None]
    if faltan:
        raise SystemExit(f"Faltan audios en {cfg['paths']['audio_dir']}: {faltan}")
    exps = [e for e in cfg["benchmark"]["experimentos"] if (not solo or e["id"] in solo)
            and not (sin_cpu and e["device"] == "cpu")]
    entorno = info_entorno()
    print(f"Entorno: {entorno}\nClips: {clips}\nExperimentos: {[e['id'] for e in exps]}\n")

    resultados = []
    for e in exps:
        print(f"==> {e['id']} ...", flush=True)
        r = correr_experimento({**e, "tarea": tarea}, clips, refs, cfg, mod_asr)
        print(f"    WER {pct(r['wer'])} · CER {pct(r['cer'])} · {r['seg_por_min_audio']:.1f} s/min · "
              f"dispositivo leído: {r['device_leido']} · VRAM Δ {r['vram_delta_mb']} MB · GPU verificada: {r['gpu_verificada']}")
        if r["fallback_silencioso"]:
            print("    ¡¡ ATENCIÓN: se pidió", r["device_pedido"], "pero la librería usó", r["device_leido"], "!!")
        resultados.append(r)

    por_id = {r["id"]: r for r in resultados}
    comps = {k: [comparar(por_id[a], por_id[b], cfg) for a, b in pares if a in por_id and b in por_id]
             for k, pares in cfg["benchmark"]["comparaciones"].items()}
    out_dir = salida or resolver_ruta(cfg, cfg["paths"]["results_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"asr_benchmark_{tarea}"
    payload = {"entorno": entorno, "experimentos": resultados, "comparaciones": comps}
    stem.with_suffix(".json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(stem.with_suffix(".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["experimento", "modelo", "glosario", "device_leido", "precision", "clips", "wer", "wer_lo", "wer_hi",
                    "cer", "seg_por_min", "vram_pico_mb", "gpu_verificada"])
        for r in resultados:
            w.writerow([r["id"], r["modelo"], r["glosario"], r["device_leido"], r["precision"], r["n_clips"], r["wer"],
                        r["wer_ic95"][0], r["wer_ic95"][1], r["cer"], r["seg_por_min_audio"], r["vram_delta_mb"], r["gpu_verificada"]])
    stem.with_suffix(".md").write_text(tabla_md(resultados, comps, entorno, tarea), encoding="utf-8")
    print(f"\nListo: {stem}.md / .json / .csv")
    return payload


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", choices=["t1", "t2"], default="t1")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--solo", nargs="*", help="ids de experimentos a correr (por defecto, todos)")
    ap.add_argument("--sin-cpu", action="store_true", help="omite los experimentos en CPU (más rápido)")
    a = ap.parse_args()
    ejecutar(load_config(a.config), a.task, a.solo, a.sin_cpu)
