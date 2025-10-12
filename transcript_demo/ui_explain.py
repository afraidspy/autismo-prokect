# ui_explain.py
import dash_bootstrap_components as dbc
from dash import html

def explainability_card(analysis: dict):
    sem = analysis.get("semantic_analysis", {})
    coh = analysis.get("coherence_metrics", {})
    flags = analysis.get("flags", [])

    sem_ul = html.Ul([
        html.Li(f"Definition elements: {', '.join(sem.get('matched_keywords',{}).get('definition', []))}"),
        html.Li(f"Functions: {', '.join(sem.get('matched_keywords',{}).get('function', []))}"),
        html.Li(f"Examples: {', '.join(sem.get('matched_keywords',{}).get('examples', []))}"),
        html.Li(f"Sensory words: {', '.join(sem.get('matched_keywords',{}).get('sensory', []))}"),
    ], className="mb-2")

    flow = []
    flow.append(dbc.Alert("✔ Clear structure", color="success", className="py-2 mb-2") if coh.get("has_clear_structure") else dbc.Alert("✖ Structure unclear", color="danger"))
    flow.append(dbc.Alert("✔ Logical connectives present", color="success", className="py-2 mb-2") if coh.get("uses_connectives") else dbc.Alert("✖ Few connectives", color="danger"))
    flow.append(dbc.Alert(f"Repetition score: {coh.get('repetition_score',0)}", color="warning", className="py-2 mb-2"))

    alert_cards = []
    if not flags:
        alert_cards.append(dbc.Alert("No significant concerns detected.", color="success", className="py-2"))
    else:
        for f in flags:
            color = {"low":"info","medium":"warning","high":"danger"}.get(f.get("severity","low"),"secondary")
            alert_cards.append(
                dbc.Alert([
                    html.Strong(f.get("message","")), " ",
                    html.Small(f"({f.get('severity','low')})"),
                    html.Br(),
                    html.Small(f.get("evidence",""), className="text-muted")
                ], color=color, className="py-2 mb-2")
            )

    return dbc.Card(
        dbc.CardBody([
            html.H5([html.I(className="fas fa-brain me-2"), "AI Explainability"], className="mb-3"),
            html.H6("🔍 Semantic Breakdown"),
            sem_ul,
            html.Hr(),
            html.H6("🧩 Logic Flow"),
            *flow,
            html.Hr(),
            html.H6("🏥 Clinical Interpretation"),
            *alert_cards
        ]),
        className="shadow-sm border-0"
    )
