from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

def create_pdf(file_name: str, title: str, contents: list):
    os.makedirs("pdfs", exist_ok=True)

    path = f"pdfs/{file_name}.pdf"
    doc = SimpleDocTemplate(path, pagesize=A4)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"<b>{title}</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    for item_type, value in contents:
        if item_type == "text":
            story.append(Paragraph(value, styles["Normal"]))
            story.append(Spacer(1, 12))

        if item_type == "image":
            story.append(Image(value, width=300, height=200))
            story.append(Spacer(1, 12))

    doc.build(story)
    return path
