"""Evalúa las dos capas (texto y registro) sobre las transcripciones en caché y escribe tablas y curva.

    python scripts/evaluar.py --task t1
    python scripts/evaluar.py --task t2 --ladder          # L0..L3 (requiere la escalera transcrita)
    python scripts/evaluar.py --task t2 --method llm      # extracción con LLM (necesita ANTHROPIC_API_KEY)

Config de caché por defecto: asr.cache_corpus. Salida: results/evaluacion_<task>.{md,json} y, con --ladder,
results/curva_degradacion.png.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine import cache                                  # noqa: E402
from engine.config import load_config, resolver_ruta      # noqa: E402
from metrics.evaluacion import contraste, evaluar, resumen_nivel   # noqa: E402


def pct(x: float) -> str:
    return f"{100 * x:.1f} %"


def tabla_md(res: dict[str, dict], schema: str, cfg: dict, metodo: str, conf: str) -> str:
    L = [f"# Evaluación {schema.upper()} — extracción {metodo} — ASR {conf}", ""]
    L += ["## Capa de texto y capa de registro por nivel", "",
          "| Nivel | Clips | WER (IC95) | CER | Campos correctos | Registros perfectos |", "|---|---|---|---|---|---|"]
    for n, r in res.items():
        L.append(f"| {n} | {r['n_clips']} | {pct(r['wer'])} ({pct(r['wer_ic'][0])}–{pct(r['wer_ic'][1])}) | {pct(r['cer'])} | "
                 f"{r['campos_ok']}/{r['campos_total']} | {r['registros_perfectos']}/{r['n_clips']} |")
    for n, r in res.items():
        L += ["", f"## Exactitud por campo — {n}", "", "| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |", "|---|---|---|---|---|"]
        for c, d in r["por_campo"].items():
            extra = []
            if "error_abs_medio" in d:
                extra.append(f"error abs. medio {d['error_abs_medio']:.2f}")
            if "f1_macro" in d:
                extra.append(f"F1 macro {d['f1_macro']:.2f}")
            L.append(f"| {c} | {d['aciertos']}/{d['n']} | {pct(d['exactitud'])} ({pct(d['ic_lo'])}–{pct(d['ic_hi'])}) | "
                     f"{d['sin_verificar']} | {'; '.join(extra)} |")
    if schema == "t2":
        L += ["", "## Validadores: registros malos atrapados vs perdidos", "",
              "| Nivel | Registros malos | Atrapados por aritmética | Atrapados por verificación literal | Atrapados (alguna) | Perdidos | Diagnóstico (ok/asr/hablante) |",
              "|---|---|---|---|---|---|---|"]
        for n, r in res.items():
            d = r["diagnosticos"]
            L.append(f"| {n} | {r['registros_malos']} | {r['atrapados_aritmetica']} | {r['atrapados_verificacion']} | "
                     f"{r['atrapados_alguna']} | {r['perdidos']} | {d['ok']}/{d['asr']}/{d['hablante']} |")
    return "\n".join(L) + "\n"


def curva(res: dict[str, dict], destino: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    niveles = list(res)
    wer = [100 * res[n]["wer"] for n in niveles]
    acc = [100 * res[n]["campos_ok"] / res[n]["campos_total"] for n in niveles]
    fig, ax = plt.subplots(figsize=(6.4, 3.8), dpi=150)
    ax.plot(niveles, wer, marker="o", color="#B3402A", label="WER (texto) — menos es mejor")
    ax.plot(niveles, acc, marker="s", color="#1F6F8B", label="Campos correctos (registro) — más es mejor")
    for x, y in zip(niveles, wer):
        ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8)
    for x, y in zip(niveles, acc):
        ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, -13), ha="center", fontsize=8)
    ax.set_ylim(0, 105)
    ax.set_ylabel("%")
    ax.set_xlabel("Nivel de degradación (L0 original → L3 ruido a 10 dB)")
    ax.set_title("T2: la degradación del audio en texto y en registro", fontsize=10)
    ax.grid(axis="y", alpha=0.3)
    ax.legend(fontsize=8, loc="center left")
    fig.tight_layout()
    fig.savefig(destino)


def barras_campos(r: dict, titulo: str, destino: Path) -> None:
    """Exactitud por campo con IC de Wilson 95 % (un nivel). Una sola serie: se lee con la etiqueta aciertos/n."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    campos = list(r["por_campo"])
    acc = [100 * r["por_campo"][c]["exactitud"] for c in campos]
    lo = [a - 100 * r["por_campo"][c]["ic_lo"] for a, c in zip(acc, campos)]
    hi = [100 * r["por_campo"][c]["ic_hi"] - a for a, c in zip(acc, campos)]
    fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=150)
    y = range(len(campos))
    ax.barh(list(y), acc, xerr=[lo, hi], color="#1F6F8B", capsize=3, ecolor="#555555")
    for i, c in enumerate(campos):
        d = r["por_campo"][c]
        ax.text(2, i, f"{d['aciertos']}/{d['n']}", va="center", ha="left", color="white", fontsize=9, fontweight="bold")
    ax.set_yticks(list(y))
    ax.set_yticklabels(campos, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Exactitud del campo (%), con IC de Wilson 95 %")
    ax.set_title(titulo, fontsize=10)
    ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    fig.savefig(destino)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", choices=["t1", "t2"], required=True)
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--method", choices=["rules", "llm"])
    ap.add_argument("--ladder", action="store_true")
    a = ap.parse_args()

    cfg = load_config(a.config)
    cc = cfg["asr"]["cache_corpus"]
    conf = cache.nombre_config(cc["model"], cc["device"], cc["compute_type"], cc.get("glossary", False))
    metodo = a.method or cfg["extraction"]["method"]
    niveles = cfg["ladder"]["niveles"] if (a.ladder and a.task == "t2") else ["L0"]
    filas, faltantes = evaluar(cfg, a.task, conf, niveles, metodo)
    if not filas:
        print(f"No hay transcripciones en caché para la configuración {conf}. Primero corre transcribir_corpus.py.")
        return 1
    res = {n: resumen_nivel([f for f in filas if f["nivel"] == n], a.task, cfg) for n in niveles
           if any(f["nivel"] == n for f in filas)}
    out = resolver_ruta(cfg, cfg["paths"]["results_dir"])
    out.mkdir(parents=True, exist_ok=True)
    md = tabla_md(res, a.task, cfg, metodo, conf)
    c = contraste(filas)
    md += ("\n## WER vs calidad del registro\n\n"
           f"- WER alto (≥ mediana {pct(c['mediana_wer'])}) pero registro perfecto: {', '.join(c['wer_alto_registro_perfecto']) or '—'}\n"
           f"- WER bajo pero registro con errores: {', '.join(c['wer_bajo_registro_roto']) or '—'}\n")
    if faltantes:
        md += f"\n> Sin transcripción en caché (no evaluados): {', '.join(faltantes)}\n"
    (out / f"evaluacion_{a.task}.md").write_text(md, encoding="utf-8")
    ligero = [{k: v for k, v in f.items() if k != "comparacion"} for f in filas]
    (out / f"evaluacion_{a.task}.json").write_text(json.dumps({"config_asr": conf, "metodo": metodo, "resumen": res,
                                                               "filas": ligero, "faltantes": faltantes},
                                                              ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    if "L0" in res:
        barras_campos(res["L0"], f"{a.task.upper()}: exactitud por campo (L0, método {metodo})", out / f"exactitud_campos_{a.task}.png")
    if a.ladder and len(res) > 1:
        curva(res, out / "curva_degradacion.png")
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
