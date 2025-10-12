# Transcript Demo (Standalone)

Demo de análisis de transcripción con UI moderna, datos fake y exportación a PDF.

## Requisitos
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar
```bash
python app.py
```
Abre: http://localhost:8051

## Qué incluye
- Hero con gradiente y texto guía.
- KPIs (score con barra, palabras, frases).
- Tarjeta de transcripción con resaltados por categoría (definition/function/examples/sensory).
- Panel de explicabilidad (semántica, flujo lógico y banderas clínicas).
- **Sección de Reporte PDF** (reemplaza tabs): visor embebido + botón de descarga.
- **Sin backend**: datos fake precargados.

## Personalizar
- Cambia el texto y métricas en `data.py`.
- Ajusta estilos en `assets/custom.css`.
- Extiende el PDF en `pdf_service.py`.
