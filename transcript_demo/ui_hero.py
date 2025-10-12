# ui_hero.py
import dash_bootstrap_components as dbc
from dash import html

def hero_card():
    return dbc.Card(
        dbc.CardBody([
            html.Div("Transcript Intelligence", className="fw-semibold text-white-50"),
            html.H2([
                html.I(className="fas fa-brain me-2"),
                "AI Transcript Analysis"
            ], className="text-white fw-bold"),
            html.P("Explainable insights with interactive highlights and exportable report.",
                   className="text-white-50 mb-0")
        ]),
        style={
            "background": "linear-gradient(135deg, #2f80ed, #56ccf2)",
            "borderRadius": "18px",
            "border": "none",
            "padding": "28px"
        },
        className="mb-4 shadow-sm"
    )
