# ui_report.py
import dash_bootstrap_components as dbc
from dash import html
from pdf_service import create_pdf_bytes, as_data_uri

def report_card(analysis: dict):
    pdf_bytes = create_pdf_bytes(analysis)
    pdf_uri = as_data_uri(pdf_bytes)

    return dbc.Card(
        dbc.CardBody([
            html.H4("📄 AI Analysis Report", className="mb-3"),
            html.P("Preview of the automatically generated report below. Click to download.", className="text-muted"),
            html.Iframe(src=pdf_uri, style={"width":"100%","height":"520px","border":"1px solid #e5e5e5","borderRadius":"12px"}),
            dbc.Button("⬇️ Download PDF", color="primary", className="mt-3", href=pdf_uri, download="Transcript_Report.pdf"),
        ]),
        className="shadow-sm border-0 mt-2 mb-5"
    )
