import os
import sys
import argparse
import re

# Intentar importar python-docx, si no está instalado avisar amablemente
try:
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
except ImportError:
    print("⚠️ python-docx no está instalado. Ejecuta: pip install python-docx")

sys.stdout.reconfigure(encoding='utf-8')

def set_cell_background(cell, hex_color):
    """Aplica color de fondo a una celda de tabla."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Ajusta márgenes internos de celda."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_report_docx(markdown_path, output_docx, author_name="Creador / Autor"):
    """Convierte el informe de auditoría Markdown en un documento Word elegante y profesional."""
    if not os.path.exists(markdown_path):
        print(f"❌ Error: Archivo markdown no encontrado: {markdown_path}")
        return

    doc = Document()
    
    # Configurar márgenes estándar de 1 pulgada
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Colores de marca Arqueólogo Creativo
    COLOR_PRIMARY = RGBColor(26, 36, 56)     # Navy oscuro elegante
    COLOR_SECONDARY = RGBColor(180, 115, 30) # Dorado / Oro arqueológico
    COLOR_DARK = RGBColor(40, 40, 40)
    COLOR_MUTED = RGBColor(100, 100, 100)

    # 1. PORTADA EDITORIAL
    p_title_space = doc.add_paragraph()
    p_title_space.paragraph_format.space_before = Pt(40)
    
    p_badge = doc.add_paragraph()
    r_badge = p_badge.add_run("💎 ARQUEÓLOGO CREATIVO / CREATIVE ARCHAEOLOGIST")
    r_badge.font.name = "Arial"
    r_badge.font.size = Pt(11)
    r_badge.font.bold = True
    r_badge.font.color.rgb = COLOR_SECONDARY
    p_badge.alignment = WD_ALIGN_PARAGRAPH.LEFT

    p_title = doc.add_paragraph()
    r_title = p_title.add_run("INFORME MAESTRO DE AUDITORÍA & RESCATE DE ACTIVOS")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY
    p_title.paragraph_format.space_after = Pt(10)

    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run(f"Dictamen Forense de Portafolio, Desentierro de IPs y Roadmap Estratégico para: {author_name}")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = COLOR_MUTED
    p_sub.paragraph_format.space_after = Pt(40)

    # Línea decorativa
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_after = Pt(30)
    
    doc.add_page_break()

    # 2. PROCESAMIENTO DEL CONTENIDO MARKDOWN
    with open(markdown_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    in_table = False
    table_rows = []

    for line in lines:
        raw = line.strip()
        if not raw:
            continue

        # Detección de Tablas Markdown
        if raw.startswith('|') and raw.endswith('|'):
            # Ignorar separador |---|---|
            if re.match(r'^\|[\s\-:|]+\|$', raw):
                continue
            cells = [c.strip() for c in raw.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            continue
        elif in_table:
            # Fin de tabla detectada: renderizar tabla en Word
            if table_rows:
                table = doc.add_table(rows=len(table_rows), cols=len(table_rows[0]))
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.autofit = True
                
                for r_idx, row in enumerate(table_rows):
                    for c_idx, val in enumerate(row):
                        cell = table.cell(r_idx, c_idx)
                        cell.text = val
                        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
                        
                        if r_idx == 0:
                            set_cell_background(cell, "1A2438")
                            for p in cell.paragraphs:
                                for r in p.runs:
                                    r.font.name = "Arial"
                                    r.font.size = Pt(9.5)
                                    r.font.bold = True
                                    r.font.color.rgb = RGBColor(255, 255, 255)
                        else:
                            if r_idx % 2 == 1:
                                set_cell_background(cell, "F8F9FA")
                            for p in cell.paragraphs:
                                for r in p.runs:
                                    r.font.name = "Arial"
                                    r.font.size = Pt(9)
                                    r.font.color.rgb = COLOR_DARK
                doc.add_paragraph() # Espacio post tabla
            table_rows = []
            in_table = False

        # Encabezados
        if raw.startswith('# '):
            h = doc.add_heading(raw.replace('# ', '').strip(), level=1)
            h.paragraph_format.space_before = Pt(20)
            h.paragraph_format.space_after = Pt(8)
            for r in h.runs:
                r.font.name = "Arial"
                r.font.size = Pt(16)
                r.font.color.rgb = COLOR_PRIMARY
        elif raw.startswith('## '):
            h = doc.add_heading(raw.replace('## ', '').strip(), level=2)
            h.paragraph_format.space_before = Pt(16)
            h.paragraph_format.space_after = Pt(6)
            for r in h.runs:
                r.font.name = "Arial"
                r.font.size = Pt(13)
                r.font.color.rgb = COLOR_SECONDARY
        elif raw.startswith('### '):
            h = doc.add_heading(raw.replace('### ', '').strip(), level=3)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
            for r in h.runs:
                r.font.name = "Arial"
                r.font.size = Pt(11)
                r.font.color.rgb = COLOR_PRIMARY
        elif raw.startswith('> '):
            # Cita o llamada destacada
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(raw.replace('> ', '').strip())
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.italic = True
            r.font.color.rgb = COLOR_SECONDARY
        elif raw.startswith('- ') or raw.startswith('* '):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(raw[2:].strip())
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.color.rgb = COLOR_DARK
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(raw)
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.color.rgb = COLOR_DARK

    doc.save(output_docx)
    print(f"🎉 Informe maquetado en Word generado con éxito: {output_docx}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de Informe Word (.docx) para Arqueólogo Creativo")
    parser.add_argument("--input", required=True, help="Ruta del archivo Markdown (.md)")
    parser.add_argument("--output", default="Informe_Arqueologo_Creativo.docx", help="Ruta del archivo Word de salida")
    parser.add_argument("--author", default="Creador", help="Nombre del autor o estudio auditado")
    args = parser.parse_args()

    create_report_docx(args.input, args.output, args.author)
