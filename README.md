# De la voz al registro: captura de entrevistas y llamadas de venta

Proyecto integrador individual (entrega 30-oct-2026). Audio → transcripción (Whisper) → campos estructurados →
verificación literal y validación aritmética → métricas en **dos capas** (texto y registro).

- Pipeline (documento visual): **[COMPLETAR: enlace público de Notion/Miro]**
- Video (≤ 8 min): **[COMPLETAR: enlace al video]**

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate            # Windows PowerShell  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env             # Linux/macOS: cp .env.example .env   (solo si usarás el método LLM)
```
Requiere `ffmpeg` en el PATH solo para generar la escalera de degradación (`scripts/ladder.py`). La app y las pruebas no lo necesitan.

## Ejecutar la app (un solo comando)
```bash
streamlit run app.py
```
Muestra los clips del corpus desde la caché (sin GPU) y permite subir un audio propio (modelo `small`, funciona en CPU).
Pestañas: Procesar audio · Resultados T1 · Resultados T2 y degradación · Cómo funciona. Para T2 muestra el pedido final y la validación aritmética.

## Pruebas
```bash
pytest -q        # 46 pruebas; no necesitan GPU ni pesos de modelos
grep -rEn "streamlit|gradio|tkinter|flask" engine/ || echo "OK: el motor no importa UI"
```

## Reproducir los resultados
```bash
python scripts/benchmark_asr.py --task t1                     # benchmark ASR (GPU: Kaggle/Colab, ver notebooks/)
python scripts/ladder.py                                      # L1, L2, L3 desde los audios t2_* (escribe data/audio_ladder/)
python scripts/transcribir_corpus.py --task t2 --model large-v3 --device cuda --compute float16
python scripts/transcribir_corpus.py --task t2 --dir data/audio_ladder --model large-v3 --device cuda --compute float16
python scripts/evaluar.py --task t1
python scripts/evaluar.py --task t2 --ladder                  # tablas + results/curva_degradacion.png
```
Las transcripciones en caché (`data/cache/asr/`) se commitean: con ellas `evaluar.py` y la app corren sin GPU.
La configuración completa (rutas, modelos, glosarios, esquemas, promociones, escalera) está en `config.yaml`; las credenciales, solo como nombres, en `.env.example`.

## Arquitectura
| Módulo | Función |
|---|---|
| `engine/` | Motor único `process_audio(audio, schema)` para T1 y T2; lee el dispositivo de la librería (sin caída silenciosa a CPU); no importa UI. |
| `extraction/` | Extracción por reglas (`t1_rules.py`, `t2_rules.py`) o LLM (`llm.py`) + verificación literal (`verificar.py`). |
| `validation/` | Validador aritmético de T2 y diagnóstico ASR vs hablante. |
| `metrics/` | WER/CER con normalización, IC por bootstrap, exactitud por campo con IC de Wilson, F1 macro, error absoluto. |
| `scripts/` | Benchmark, transcripción del corpus, escalera de degradación, evaluación, guiones y verdad de terreno. |

**Normalización antes de WER/CER** (igual en referencia e hipótesis): minúsculas; moneda y porcentaje a palabras; sin separadores de miles; dígitos separados de letras; sin puntuación; números hablados a dígitos (`seis mil quinientos` → `6500`); los acentos se conservan.

**Verificación literal:** todo valor extraído debe existir en la transcripción normalizada; si no, queda como `sin_verificar` y no entra al registro como dato.

**Validación aritmética (T2):** cantidad × precio unitario − promoción = total dicho. Si falla, `diagnostico` compara con la referencia: error del *hablante* (la referencia ya es inconsistente) o del *ASR*.

## Dominio de la Tarea 2
Restaurante (cevichería ficticia «Marea Norte»): carta con precios por tamaño, dos promociones (descuento de S/ 10 desde S/ 80; 2×1 en chicha morada en vaso), pedidos con autocorrecciones, totales mal sumados a propósito y direcciones con dígitos.

## Resultados
Corpus propio: 5 entrevistas (T1) y 5 llamadas (T2) de 2 a 3 min, una sola voz. Con 5 clips los intervalos son anchos: léelos como orden de magnitud.

### Benchmark de ASR (T1, GPU Tesla T4, faster-whisper 1.2.1)
| Experimento | WER [IC95] | CER | s por min de audio | VRAM pico (MB) |
|---|---|---|---|---|
| small · GPU · float16 | 7.6 % [6.4–9.3] | 3.3 % | 1.9 | 884 |
| small · GPU · int8 | 7.8 % [6.7–9.4] | 3.4 % | 1.9 | 426 |
| small · CPU · int8 (solo 2 clips) | 6.2 % [6.2–6.3] | 2.5 % | 22.6 | — |
| **large-v3 · GPU · float16** | **3.1 % [2.0–4.2]** | 1.5 % | 6.1 | 4010 |
| large-v3 · GPU · int8 | 3.2 % [2.2–4.3] | 1.5 % | 6.0 | 2250 |
| small + glosario | 7.0 % [5.9–8.1] | 2.8 % | 2.0 | 746 |
| large-v3 + glosario | 3.3 % [1.9–4.6] | 1.7 % | 6.2 | 4010 |

- large-v3 reduce el WER 4.4 pp frente a small (IC [+2.96, +5.95]), a cambio de ~3× el tiempo.
- float16 vs int8 no se distinguen en large-v3 (IC incluye 0) y int8 usa ~44 % menos VRAM.
- El glosario sube el recall de términos técnicos (small: 76 → 100 %; large-v3: 96 → 100 %) sin cambio significativo en WER.
- Decisión: corpus transcrito con **large-v3 · GPU · float16**; la app usa `small` para audios subidos (corre en CPU) y glosario apagado por defecto.

### Tabla T1 — entrevistas (extracción por reglas, large-v3 float16)
WER 3.1 % (IC 2.0–4.2), CER 1.5 %. Campos correctos 25/30; registros perfectos 1/5.

| Campo | Aciertos | Exactitud (Wilson 95 %) | Nota |
|---|---|---|---|
| anios_experiencia | 5/5 | 100 % (56.6–100) | error abs. 0 |
| ultimo_puesto | 2/5 | 40 % (11.8–76.9) | 3 fallos por el ASR («ciencias», «Análisa», «ingeniería») |
| tecnologias | 4/5 | 80 % (37.6–96.4) | «JIT» por «Git» |
| pretension_salarial | 4/5 | 80 % (37.6–96.4) | el ASR escribió 1,800 por 1200 |
| disponibilidad | 5/5 | 100 % (56.6–100) | |
| nivel_ingles | 5/5 | 100 % (56.6–100) | F1 macro 1.00 |

### Tabla T2 — llamadas y escalera de degradación (extracción por reglas)
L0 original · L1 Opus 16 kbps mono (nota de voz) · L2 banda 300–3400 Hz a 8 kHz (teléfono) · L3 L1 + ruido rosa a SNR 10 dB (medida sobre tramas con voz; `results/snr_ladder.json`).

| Nivel | WER (IC95) | CER | Campos correctos | Registros perfectos | Registros malos | Atrapados | Perdidos |
|---|---|---|---|---|---|---|---|
| L0 | 5.1 % (4.2–6.1) | 2.7 % | 24/25 | 4/5 | 1 | 1 | 0 |
| L1 | 5.7 % (4.8–7.0) | 3.0 % | 24/25 | 4/5 | 1 | 1 | 0 |
| L2 | 5.4 % (4.5–6.5) | 2.7 % | 22/25 | 2/5 | 3 | 2 | 1 |
| L3 | 6.5 % (5.0–7.9) | 3.4 % | 24/25 | 4/5 | 1 | 1 | 0 |

Curva: `results/curva_degradacion.png`. Tablas completas por campo en `results/evaluacion_t1.md` y `results/evaluacion_t2.md`.

### Lectura
- **WER y calidad del registro no son lo mismo.** `t2_04` y `t2_03` tienen WER alto (≥ mediana) y registro perfecto en casi todos los niveles; `t2_02` y `t2_05@L2` tienen WER bajo y registro con errores. En T1, `t1_05` tiene WER bajo y el cargo mal escrito por una sola palabra.
- **La degradación fue suave para large-v3.** El WER sube de 5.1 % a 6.5 % entre L0 y L3 con intervalos que se traslapan; con 5 clips no se puede afirmar una caída real. L2 (banda telefónica) es el nivel que más campos rompe.
- **Los errores de registro vienen de cómo Whisper escribe nombres y palabras ambiguas** («Girón» por «Jirón», «Análisa», «JIT», «en cacola»), no de la degradación.
- **La verificación literal no detecta errores del ASR.** `1,800` (oído mal) sí está en el texto y pasa la verificación; solo protege contra valores que no aparecen en la transcripción.
- **El validador aritmético detecta errores del hablante** (3 clips con total mal sumado a propósito: `diagnostico` = *hablante*), pero no ve errores de dirección. Un campo vacío tampoco activa ninguna alarma.
- Un registro defectuoso en L2 no fue detectado por ninguna validación («Perdidos» = 1).

## Declaración de herramientas de IA y MCP
- **Claude (Anthropic) / Claude Code**: asistente de programación del repositorio (motor, extracción, métricas, validador, escalera, evaluación, app, pruebas, scripts y notebooks), de los guiones de las grabaciones y de la redacción de este README. Las decisiones de diseño y la revisión de resultados son de la autora.
- **faster-whisper (Whisper `small` y `large-v3`)**: reconocimiento de voz; pesos descargados automáticamente, no incluidos en el repo.
- **API de Claude (opcional)**: solo si se elige `extraction.method: llm`; **no se evaluó en esta entrega** (ver limitaciones).
- **Servidores MCP**: **[COMPLETAR: lista de servidores MCP usados y qué hizo cada uno; si no se usó ninguno, escribir «ninguno»]**.

## Datos inventados y consentimiento
- Todo lo dicho en las grabaciones es inventado: nombres, salarios, direcciones, la cevichería y sus precios. No hay datos personales reales.
- Las voces que aparecen pertenecen a personas que aceptaron participar. No se nombra a nadie que no haya aceptado.

## Audios y pesos de modelos
Los audios (`data/audio/`, `data/audio_ladder/`) y los pesos de los modelos no se commitean. Los audios se pueden solicitar a la autora. Lo que sí está en el repo: guiones, verdad de terreno y transcripciones en caché.

## Limitaciones
- **Muestra pequeña:** 5 clips por tarea y una sola voz; los intervalos son anchos y no hay conclusiones estadísticas fuertes.
- **Reglas calibradas con los mismos guiones:** las reglas se ajustaron mirando la transcripción de referencia; por eso se probaron también sobre un corpus no visto de otra persona (T1 29/30, T2 24/25 campos). Siguen sin cubrir algunas correcciones («tres tallarines» tras un cambio de idea).
- **Método LLM no evaluado:** el código existe (`extraction/llm.py`) y se ejecuta con `python scripts/evaluar.py --task t1 --method llm`, pero no se corrió para esta entrega; todas las tablas son de reglas.
- **Benchmark en CPU:** solo 2 clips; el tiempo por minuto es orientativo.
- **Escalera suave:** con large-v3, Opus 16 kbps, banda telefónica y 10 dB de ruido degradan poco; una escalera más dura podría separar mejor los niveles.
- **Campos vacíos sin alarma:** una dirección no encontrada queda como «sin dato» y ninguna validación la marca.
- **Dominio fijo:** las reglas de T2 dependen de la carta y las promociones de `config.yaml`; otro negocio requiere nueva configuración.
