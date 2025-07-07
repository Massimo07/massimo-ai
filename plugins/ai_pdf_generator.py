# /plugins_ai/ai_pdf_generator.py

from fpdf import FPDF
import tempfile
import os

class AIPDFGenerator:
    def generate_pdf(self, title: str, content: str, output_name="documento_ai.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, content)
        temp_dir = tempfile.gettempdir()
        output_path = os.path.join(temp_dir, output_name)
        pdf.output(output_path)
        return output_path

# USO:
# pdf_plugin = AIPDFGenerator()
# path = pdf_plugin.generate_pdf("Titolo AI", "Testo creato da Massimo AI...")
