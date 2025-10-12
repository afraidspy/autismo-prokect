# pdf_service.py
import base64
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def create_pdf_bytes(analysis: dict) -> bytes:
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph("Clinical Report", styles["Title"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"Session ID: {analysis.get('session_id','N/A')}", styles["Normal"]))
    story.append(Paragraph(f"Overall Score: {analysis.get('overall_score',0)}/100", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Transcript</b>", styles["Heading2"]))
    story.append(Paragraph(analysis.get("transcript",""), styles["BodyText"]))
    story.append(Spacer(1, 12))

    comp = analysis.get("complexity_metrics", {})
    coh = analysis.get("coherence_metrics", {})
    table = Table([
        ["Metric", "Value"],
        ["Words", comp.get("word_count", 0)],
        ["Sentences", coh.get("sentence_count", 0)],
        ["Lexical Diversity (%)", f"{comp.get('unique_word_ratio', 0)*100:.1f}"],
        ["Average Word Length", f"{comp.get('avg_word_length',0):.1f}"],
    ], colWidths=[200, 300])
    table.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.lightgrey),
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#e9f2f9")),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.whitesmoke, colors.HexColor("#f9f9f9")]),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Semantic Highlights</b>", styles["Heading2"]))
    sem = analysis.get("semantic_analysis", {}).get("matched_keywords", {})
    for k in ["definition","function","examples","sensory"]:
        story.append(Paragraph(f"{k.title()}: {', '.join(sem.get(k, [])) or '—'}", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Clinical Flags</b>", styles["Heading2"]))
    flags = analysis.get("flags", [])
    if not flags:
        story.append(Paragraph("No significant concerns detected.", styles["Normal"]))
    else:
        for f in flags:
            story.append(Paragraph(f"- {f.get('message','')} ({f.get('severity','low')}) — {f.get('evidence','')}", styles["Normal"]))

    doc.build(story)
    buf.seek(0)
    return buf.getvalue()

def as_data_uri(pdf_bytes: bytes) -> str:
    b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    return f"data:application/pdf;base64,{b64}"
