# app.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from data import EXAMPLE_ANALYSIS
from ui_hero import hero_card
from ui_kpis import kpi_row
from ui_transcript import transcript_card
from ui_explain import explainability_card
from ui_report import report_card

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
)

app.layout = dbc.Container([
    hero_card(),
    kpi_row(EXAMPLE_ANALYSIS),

    dbc.Row([
        dbc.Col(transcript_card(EXAMPLE_ANALYSIS), lg=6, sm=12, className="mb-3"),
        dbc.Col(explainability_card(EXAMPLE_ANALYSIS), lg=6, sm=12, className="mb-3"),
    ], className="g-3"),

    report_card(EXAMPLE_ANALYSIS),
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8051)
