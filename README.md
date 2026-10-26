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
