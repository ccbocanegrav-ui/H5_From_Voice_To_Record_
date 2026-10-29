"""Medición de memoria de GPU con nvidia-smi.

Por qué así: faster-whisper usa CTranslate2, que NO pasa por el asignador de PyTorch; por eso
torch.cuda.max_memory_allocated() daría 0. Lo que prueba que la GPU se usó es la memoria que
nvidia-smi ve ocupada mientras corre el modelo (pico menos la memoria base antes de cargarlo).
"""
from __future__ import annotations

import subprocess
import threading
import time


def memoria_gpu_mb() -> int | None:
    """Memoria usada (MB) de la primera GPU, o None si no hay nvidia-smi / GPU."""
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                           capture_output=True, text=True, timeout=5)
        if r.returncode != 0:
            return None
        vals = [int(x) for x in r.stdout.split() if x.strip().isdigit()]
        return vals[0] if vals else None
    except Exception:
        return None


def info_gpu() -> dict:
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=name,driver_version,memory.total",
                            "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=5)
        if r.returncode != 0 or not r.stdout.strip():
            return {}
        nombre, driver, total = [x.strip() for x in r.stdout.splitlines()[0].split(",")]
        return {"gpu": nombre, "driver": driver, "memoria_total_mb": int(total)}
    except Exception:
        return {}


class MuestreadorGPU:
    """Muestrea la memoria de GPU en un hilo y devuelve base, pico y delta (pico - base)."""

    def __init__(self, intervalo: float = 0.25):
        self.intervalo = intervalo
        self._parar = threading.Event()
        self._hilo: threading.Thread | None = None
        self.base: int | None = None
        self.pico: int | None = None

    def _loop(self) -> None:
        while not self._parar.is_set():
            v = memoria_gpu_mb()
            if v is not None and (self.pico is None or v > self.pico):
                self.pico = v
            time.sleep(self.intervalo)

    def iniciar(self) -> None:
        self.base = memoria_gpu_mb()
        self.pico = self.base
        self._parar.clear()
        if self.base is not None:
            self._hilo = threading.Thread(target=self._loop, daemon=True)
            self._hilo.start()

    def detener(self) -> dict:
        self._parar.set()
        if self._hilo:
            self._hilo.join(timeout=3)
        delta = None if self.base is None or self.pico is None else max(self.pico - self.base, 0)
        return {"vram_base_mb": self.base, "vram_pico_mb": self.pico, "vram_delta_mb": delta}
