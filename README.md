# De la voz al registro: captura de entrevistas y llamadas de venta

Proyecto integrador individual. ASR (Whisper) → campos estructurados → verificación literal y validación aritmética.

> Estado: esqueleto inicial. Se completa al final (tarea #14).

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # completar credenciales
```

## Ejecutar
```bash
streamlit run app.py
```

## Verificar que el motor no importa UI
```bash
grep -rEn "streamlit|gradio|tkinter|flask" engine/ || echo "OK: el motor no importa ninguna librería de UI"
```

## Pruebas
```bash
pytest -q        # 36 pruebas: normalización de números, WER/CER/IC, motor, lógica del benchmark (no necesitan GPU ni pesos)
```

## Motor: una función, dos esquemas
Toda la transcripción y la extracción viven en `engine/`. La app y los scripts solo llaman a:
```python
from engine import process_audio
r = process_audio("data/audio/t1_01.m4a", schema="t1")   # entrevista
r = process_audio("data/audio/t2_01.m4a", schema="t2")   # llamada de venta (mismo motor)
# r = {transcript, fields, verified, device, elapsed_s, error, ...}
```
`schema` solo cambia qué campos se extraen (definidos en `config.yaml`); el código de transcripción es el mismo.
El dispositivo (`device`) se **lee de la librería** (`ctranslate2`), no de la configuración, y pedir `cuda` sin GPU
da error en vez de caer a CPU en silencio.

## Benchmark de ASR en GPU (Tarea 1, Fase 2)
Se corre en Google Colab (T4 gratis) con `notebooks/colab_benchmark.ipynb`, que ejecuta:
```bash
python scripts/benchmark_asr.py --task t1            # small y large-v3, GPU/CPU, float16/int8, glosario plano/con vocabulario
python scripts/transcribir_corpus.py --task t2 --model large-v3 --device cuda --compute float16
```
Resultados en `results/asr_benchmark_t1.{md,json,csv}`; transcripciones en `data/cache/asr/` (se commitean).
La VRAM se mide con `nvidia-smi` (CTranslate2 no pasa por el asignador de PyTorch) y se reporta junto al
dispositivo leído de la librería: eso es lo que prueba que se usó la GPU.

## Regla de normalización (antes de calcular WER/CER)
Se aplica igual a la referencia y a la hipótesis: minúsculas; moneda y porcentaje a palabras
(`S/ 6,500` → `6500 soles`); se quitan separadores de miles; dígitos separados de letras (`4B` → `4 b`);
sin puntuación; números hablados a dígitos (`seis mil quinientos` → `6500`); `primero de` → `1 de`;
los acentos se conservan. Detalle y tests en `metrics/texto.py`, `metrics/numeros.py` y `tests/`.

## Pipeline (documento visual)
- Notion/Miro: _pendiente (tarea #13)_

## Dominio de la Tarea 2
_pendiente: restaurante o telefonía móvil_

## Resultados
_Tabla T1 y tabla T2 + curva de degradación: pendientes._

## Declaración de herramientas de IA y MCP
_pendiente: una línea por agente/servidor MCP y qué hizo._

## Datos inventados y consentimiento
- Todo lo dicho en las grabaciones es inventado: no hay salarios, direcciones ni datos personales reales de nadie.
- Todas las personas que aparecen en las grabaciones aceptaron participar. No se nombra a nadie que no haya aceptado.

## Audios y pesos de modelos
Los audios y los pesos de los modelos no se commitean. Los audios están en `data/audio/` (ignorado por git); se pueden solicitar a la autora. Los pesos se descargan automáticamente al ejecutar `faster-whisper`.

## Limitaciones
_pendiente_
