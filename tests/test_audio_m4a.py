"""faster-whisper debe poder abrir audios .m4a (el formato típico del celular).

Por qué existe: faster-whisper 1.2.1 declara `av>=11` sin tope, así que pip instala la última `av`. Desde
av 19.0.0 `av.open()` ya no acepta `metadata_errors`, que faster-whisper sí le pasa, y TODA lectura de audio
falla con TypeError (da igual si es .m4a o .wav). Se fija av==18.1.0 (última versión verificada que funciona).
"""
import numpy as np
import pytest


def test_faster_whisper_decodifica_m4a(tmp_path):
    av = pytest.importorskip("av")
    pytest.importorskip("faster_whisper")
    from faster_whisper.audio import decode_audio

    sr = 16000
    t = np.arange(sr * 2) / sr
    x = (0.3 * np.sin(2 * np.pi * 440 * t)).astype(np.float32)
    ruta = tmp_path / "tono.m4a"
    salida = av.open(str(ruta), "w", format="mp4")
    flujo = salida.add_stream("aac", rate=sr)
    flujo.layout = "mono"
    frame = av.AudioFrame.from_ndarray(x.reshape(1, -1), format="flt", layout="mono")
    frame.sample_rate = sr
    for paquete in flujo.encode(frame):
        salida.mux(paquete)
    for paquete in flujo.encode(None):
        salida.mux(paquete)
    salida.close()

    try:
        audio = decode_audio(str(ruta), sampling_rate=16000)
    except TypeError as e:
        pytest.fail(f"av {av.__version__} es incompatible con faster-whisper: {e}. Fija av==18.1.0 en requirements.txt")
    assert audio.shape[0] >= 30000
    assert 0.15 < float(np.sqrt((audio ** 2).mean())) < 0.25     # el tono se leyó de verdad, no es silencio
