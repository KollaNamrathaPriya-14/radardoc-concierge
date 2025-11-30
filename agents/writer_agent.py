import logging
from jinja2 import Template
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os, textwrap

logger = logging.getLogger("writer_agent")

HTML_TEMPLATE = """
RadarDoc Concierge — Generated Technical Note

Title: {{ title }}

SUMMARY
-------
{{ summary }}

DERIVATION
----------
{{ derivation }}

DIAGRAM
-------
Caption: {{ diagram_caption }}
Image Path: {{ diagram_path }}

REFERENCES
----------
{% for r in references %}
- {{ r['title'] }} - {{ r['url'] }}
{% endfor %}
"""

class WriterAgent:
    def __init__(self, tools=None):
        self.tools = tools or {}

    async def run(self, title, research_out, math_out, diagram_out):
        logger.info("WriterAgent started")
        # Compose text using the template
        tpl = Template(HTML_TEMPLATE)
        text = tpl.render(
            title=title,
            summary=research_out.get("summary", ""),
            derivation=math_out.get("derivation", ""),
            diagram_caption=diagram_out.get("caption", ""),
            diagram_path=diagram_out.get("image_path", ""),
            references=research_out.get("references", [])
        )

        # Create output directory & PDF
        out_dir = "examples"
        os.makedirs(out_dir, exist_ok=True)
        pdf_path = os.path.join(out_dir, f"{title.replace(' ','_')}.pdf")

        # Use ReportLab to write the text into a simple PDF
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        y = height - 72
        for paragraph in text.split("\n"):
            wrapped = textwrap.wrap(paragraph, width=100)
            if not wrapped:
                y -= 12
            for line in wrapped:
                c.drawString(72, y, line)
                y -= 12
                if y < 72:
                    c.showPage()
                    y = height - 72
        c.save()

        return {"pdf_path": pdf_path, "text": text}
