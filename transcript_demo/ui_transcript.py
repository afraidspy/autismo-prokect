# ui_transcript.py
import dash_bootstrap_components as dbc
from dash import html

def _chip_style(bg, border):
    return {
        "backgroundColor": bg, "borderBottom": f"3px solid {border}", "borderRadius":"6px",
        "padding":"1px 4px", "cursor":"pointer"
    }

def transcript_card(analysis: dict):
    transcript = analysis.get("transcript","")
    mk = analysis.get("semantic_analysis", {}).get("matched_keywords", {})
    definition = set(mk.get("definition", []))
    function   = set(mk.get("function", []))
    examples   = set(mk.get("examples", []))
    sensory    = set(mk.get("sensory", []))

    styled = []
    for w in transcript.split():
        lw = w.lower().strip('.,!?;"()[]')
        if lw in definition:
            styled.append(html.Span(w+" ", style=_chip_style("#e9f9ee","#2ecc71"), title="Definition"))
        elif lw in function:
            styled.append(html.Span(w+" ", style=_chip_style("#eaf6ff","#17a2b8"), title="Function"))
        elif lw in examples:
            styled.append(html.Span(w+" ", style=_chip_style("#fff5e6","#f39c12"), title="Example"))
        elif lw in sensory:
            styled.append(html.Span(w+" ", style=_chip_style("#f5ecff","#9b59b6"), title="Sensory"))
        else:
            styled.append(w+" ")

    legend = dbc.Row([
        dbc.Col(dbc.Badge("Definition", color="success", className="me-2"), width="auto"),
        dbc.Col(dbc.Badge("Function",  color="info", className="me-2"), width="auto"),
        dbc.Col(dbc.Badge("Examples",  color="warning", className="me-2"), width="auto"),
        dbc.Col(dbc.Badge("Sensory",   style={"backgroundColor":"#9b59b6"}, className="me-2"), width="auto"),
    ], className="gy-2 mb-2")

    return dbc.Card(
        dbc.CardBody([
            html.H5([html.I(className="fas fa-comment-dots me-2"), "Transcript with AI Annotations"], className="mb-2"),
            legend,
            html.P(styled, style={"fontSize":"1.06rem","lineHeight":"2"})
        ]),
        className="shadow-sm border-0"
    )
