# ui_kpis.py
import dash_bootstrap_components as dbc
from dash import html

def kpi_row(analysis: dict):
    score = analysis.get("overall_score", 0)
    words = analysis.get("complexity_metrics", {}).get("word_count", 0)
    sentences = analysis.get("coherence_metrics", {}).get("sentence_count", 0)

    if score >= 75: color = "success"
    elif score >= 50: color = "warning"
    else: color = "danger"

    return dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div("Overall Score", className="text-muted small"),
            html.Div(f"{score}/100", className=f"fs-3 fw-bold text-{color}"),
            dbc.Progress(value=score, color=color, striped=True, animated=True, className="mt-2")
        ]), className="shadow-sm border-0", style={"borderRadius":"16px"}), lg=4, sm=12, className="mb-3"),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div("Words", className="text-muted small"),
            html.Div(words, className="fs-3 fw-bold text-primary"),
            html.Div("Word count", className="text-secondary small")
        ]), className="shadow-sm border-0", style={"borderRadius":"16px"}), lg=4, sm=12, className="mb-3"),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div("Sentences", className="text-muted small"),
            html.Div(sentences, className="fs-3 fw-bold text-info"),
            html.Div("Structure", className="text-secondary small")
        ]), className="shadow-sm border-0", style={"borderRadius":"16px"}), lg=4, sm=12, className="mb-3"),
    ], className="g-3")
