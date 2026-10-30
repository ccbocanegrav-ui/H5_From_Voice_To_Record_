import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from engine import cache
from engine.config import load_config
from metrics.evaluacion import evaluar

task = sys.argv[1] if len(sys.argv) > 1 else "t1"
cfg = load_config("config.yaml")
cc = cfg["asr"]["cache_corpus"]
conf = cache.nombre_config(cc["model"], cc["device"], cc["compute_type"], cc.get("glossary", False))
filas, _ = evaluar(cfg, task, conf, ["L0"], "rules")
for f in filas:
    for campo, v in f["comparacion"].items():
        if not v["ok"]:
            print(f["clip"], campo, "| obtuvo:", v["pred"], "| real:", v["real"])