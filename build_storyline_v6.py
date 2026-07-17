"""Build the v6 Word storyline for the July 27 Consejo presentation.

v6 (16-jul) integra los insumos nuevos del 14-16 jul sobre la base del v5:
 1. NUEVA CONVENCION DE PUENTE (decision Rafael 16-jul, sustituye las llaves
    volumen/precio+mezcla del v5): lamina de 3 columnas 15/50/35 por segmento
    (mercado vs PISA / puente 5 conceptos maquinaria Downtrading v4 /
    comparativo 1S25 vs 1S26 de venta perdida, PIN no solicitado, NC
    comerciales y NC logisticas).
 2. Puente Retail LISTO con el v4 (Precio +392.9 / Volumen -169.7 /
    Mix -197.9 / Lanzamientos +43.8 genuino / Gestion -37.8 = +31.3 bruto);
    Gobierno FC, Hospitales y Servicios en construccion.
 3. EBITDA real en la tablita (Estado de Resultados v18 Finanzas) con el
    hueco FC/Servicios declarado (Finanzas los funde en GOBIERNO).
 4. Research externo bajado (12 cifras citables + 12 correcciones:
    Baxter/Vantive, bianual 28-ago, India reliance...; el % PIB salud quedo
    descartado por trillado, decision Rafael 16-jul: BBVA y ANTAD cargan el macro).
 5. Entorno retail re-fundado: Entry Market KB MAT may-26 + IQVIA abril +
    forecast IQVIA; muere el "-3% sin GLP-1".
 6. Burbujas L12: la fuente ya existe (deck canal Farmacias L14-L17,
    TACC5 vs LY por linea terapeutica).
 7. Hospitales: tres frentes con numeros duros del canal; plan 2S 57/47.
 8. Gobierno: universo PEDIDOS como candidatos (463/859) + cartera
    junio-junio; nada canonico hasta los datos formales.
 9. Servicios: sizing DP vs Baxter/Vantive, SANEFRO, dos caras; las lineas
    YTD cuadran exacto con el sell-in (2,219.4).
10. Pendientes renovados (resueltos fuera, nuevos adentro) y calendario a hoy.

Los numeros del transcript 07-15 viajan como [candidato]: NO son canonicos.

Run:  python3 build_storyline_v6.py
"""

from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

OUT = Path(__file__).parent / "storyline_consejo_27jul_v6_2026-07-16.docx"

NAVY_900 = RGBColor(0x0F, 0x28, 0x45)
NAVY_700 = RGBColor(0x0F, 0x4C, 0x81)
GRAY_900 = RGBColor(0x1A, 0x23, 0x32)
GRAY_500 = RGBColor(0x5A, 0x66, 0x79)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Calibri Light"
FONT_BOLD = "Calibri"
BODY_SIZE = Pt(9.5)
TABLE_SIZE = Pt(8.5)


def style_run(run, size=BODY_SIZE, color=GRAY_900, bold=False, italic=False, font=None):
    run.font.name = font or (FONT_BOLD if bold else FONT)
    run.font.size = size
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return run


def para(doc, before=0, after=1.5, style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    return p


def body(doc, segments, before=0, after=1.5, style=None):
    p = para(doc, before, after, style)
    if isinstance(segments, str):
        segments = [(segments, False)]
    for text, bold in segments:
        style_run(p.add_run(text), bold=bold)
    return p


def note(doc, text, after=1.5):
    p = para(doc, after=after)
    style_run(p.add_run(text), size=Pt(8), color=GRAY_500, italic=True)
    return p


def bullet(doc, segments, after=1.5):
    p = body(doc, segments, after=after, style="List Bullet")
    p.paragraph_format.left_indent = Inches(0.2)
    return p


def sub_bullet(doc, segments, after=1.2):
    p = body(doc, segments, after=after, style="List Bullet 2")
    p.paragraph_format.left_indent = Inches(0.42)
    return p


def chapter(doc, text, before=10):
    p = para(doc, before=before, after=2)
    style_run(p.add_run(text), size=Pt(12), color=NAVY_900, bold=True)
    bottom_rule(p, color="0F4C81", size="8")
    return p


def lamina(doc, text, before=4):
    p = para(doc, before=before, after=1.2)
    style_run(p.add_run(text), size=Pt(9.5), color=NAVY_700, bold=True)
    return p


def bottom_rule(p, color="0F4C81", size="12"):
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def shade_cell(cell, hex_color):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(shd)


def set_table_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    inside_h = OxmlElement("w:insideH")
    inside_h.set(qn("w:val"), "single")
    inside_h.set(qn("w:sz"), "4")
    inside_h.set(qn("w:color"), "E5E9EE")
    borders.append(inside_h)
    tbl_pr.append(borders)


def cell_text(cell, text, bold=False, color=GRAY_900, align=WD_ALIGN_PARAGRAPH.LEFT,
              size=TABLE_SIZE):
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(0.5)
    p.paragraph_format.space_after = Pt(0.5)
    style_run(p.add_run(text), size=size, color=color, bold=bold)


def cell_bullets(cell, items, size=TABLE_SIZE):
    first = True
    for item in items:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        p.paragraph_format.space_before = Pt(0.5)
        p.paragraph_format.space_after = Pt(1.5)
        p.paragraph_format.line_spacing = 1.0
        style_run(p.add_run("- " + item), size=size, color=GRAY_900)


def keep_table_together(table):
    for r, row in enumerate(table.rows):
        tr_pr = row._tr.get_or_add_trPr()
        cant_split = OxmlElement("w:cantSplit")
        tr_pr.append(cant_split)
        if r == 0:
            header = OxmlElement("w:tblHeader")
            tr_pr.append(header)


def simple_table(doc, headers, rows, widths, right_from=1, bold_rows=()):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    for i, w in enumerate(widths):
        table.columns[i].width = w
    for row in table.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = w
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        shade_cell(cell, "0F4C81")
        cell_text(cell, h, bold=True, color=WHITE,
                  align=WD_ALIGN_PARAGRAPH.LEFT if i < right_from else WD_ALIGN_PARAGRAPH.RIGHT)
    for r, data in enumerate(rows, start=1):
        is_bold = (r - 1) in bold_rows
        if r % 2 == 0:
            for cell in table.rows[r].cells:
                shade_cell(cell, "E8F1F8")
        for i, value in enumerate(data):
            cell_text(table.rows[r].cells[i], value, bold=is_bold,
                      align=WD_ALIGN_PARAGRAPH.LEFT if i < right_from else WD_ALIGN_PARAGRAPH.RIGHT)
    keep_table_together(table)
    return table


def bf_table(doc, bien, falto):
    """Lamina 'que hicimos bien / que nos falto' a DOS columnas (decision Rafael 10-jul)."""
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    widths = [Inches(3.55), Inches(3.55)]
    for i, w in enumerate(widths):
        table.columns[i].width = w
    for row in table.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = w
    heads = ["Qué hicimos bien en el 1S", "Qué nos faltó en el 1S"]
    for i, h in enumerate(heads):
        cell = table.rows[0].cells[i]
        shade_cell(cell, "0F4C81")
        cell_text(cell, h, bold=True, color=WHITE)
    for i, items in enumerate((bien, falto)):
        cell_bullets(table.rows[1].cells[i], items)
    keep_table_together(table)
    return table


# ============================================================ document ======
doc = Document()

sec = doc.sections[0]
sec.page_width = Inches(8.5)
sec.page_height = Inches(11)
for attr in ("top_margin", "bottom_margin"):
    setattr(sec, attr, Inches(0.55))
for attr in ("left_margin", "right_margin"):
    setattr(sec, attr, Inches(0.7))

normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = BODY_SIZE
normal.font.color.rgb = GRAY_900

# ---------------------------------------------------------------- header ---
p = para(doc, after=1)
style_run(p.add_run("Storyline v6 · Presentación al Consejo, lunes 27 de julio de 2026"),
          size=Pt(14), color=NAVY_900, bold=True)

p = para(doc, after=3)
style_run(
    p.add_run("Versión 6 · 16 de julio de 2026 · Integra los insumos nuevos del 14-16 jul: decks de "
              "canal (Farmacias, Hospitales, Servicios), IQVIA caída de abril, Estado de Resultados "
              "v18 (EBITDA), puente Downtrading v4 (nueva convención de cascadas) y research externo "
              "consolidado. Fuentes previas: Sell-In cierre junio (fuente-de-verdad); Knobloch; "
              "INEFAM; plan NADAL. Pendientes de dato o decisión van [entre corchetes con "
              "responsable]; las cifras aún no canónicas van marcadas [candidato]."),
    size=Pt(8), color=GRAY_500)
bottom_rule(p)

# --------------------------------------------------- índice de la sesión ---
chapter(doc, "Índice de la sesión", before=6)
idx_rows = [
    ("M0", "Apertura y resumen ejecutivo", "5",
     "Compromiso al minuto uno ([96]); dónde estamos + comparativa mercado vs PISA con datos frescos; "
     "dato ganador Q2 con su asterisco (jun #2 / may #6, verificado); hueco year-to-go anticipado "
     "(98.5% jul-dic); mapa de la sesión"),
    ("M1", "Mapa del negocio y boleta competitiva", "2",
     "La tablita de los cuatro segmentos (% venta, cumplimiento, crecimiento PISA y del mercado, "
     "EBITDA $ y %, % del total, ya con datos de Finanzas) y la posición competitiva por segmento: "
     "dónde ganamos, dónde perdemos, quién es el villano"),
    ("M2", "PISA total: qué pasó en el 1S", "3",
     "Lámina de puente rectora (nueva convención 15/50/35); desempeño por canal; síntesis y "
     "reconocimiento a cadena de suministro"),
    ("M3", "Retail: entorno, 1S, 2S (43.6% de la venta)", "6",
     "Se gesta una recesión en el retail farmacéutico (Entry Market + IQVIA abril); burbujas por "
     "línea terapéutica (corto vs largo plazo, fuente ya existente); puente Retail v4 con "
     "down-trading; doble clic; qué hicimos bien / qué nos faltó; plan 2S con NADAL"),
    ("M4", "Gobierno: entorno, 1S, 2S (24.4%)", "4",
     "El gobierno subfinanciado que ejecuta mal y no paga (tres hechos con fuente) + tendencias; "
     "puente Gobierno FC; bien/faltó; plan 2S y bianual con fallo 28-ago dicho por nosotros"),
    ("M5", "Hospitales: entorno, 1S, 2S (18.5%)", "5",
     "El pagador cambia el juego (datos duros) + vista IQVIA del mercado; la amenaza en tres frentes "
     "con números (Mindray infusión, Baxter/Vantive soluciones, Kener dimensionado) y la respuesta; "
     "puente Hospitales; bien/faltó; plan 2S (7 palancas, $47M/mes vs gap $57M/mes)"),
    ("M6", "Servicios: entorno, 1S, 2S (13.4%)", "5",
     "Primera vez en una junta de Consejo; dinámica competitiva por modelo con sizing real (DP vs "
     "Baxter/Vantive); puente Servicios; bien/faltó; plan 2S (dos caras del portafolio)"),
    ("M7", "La ruta consolidada al número", "2",
     "Cascada year-to-go (servicio normalizado implícito; NADAL, precios, invernal); riesgos que "
     "decimos nosotros y mecanismo de seguimiento (KPIs mensuales)"),
    ("M8", "Proyectos críticos, habilitadores y conclusiones", "3",
     "E-commerce a venta y transformación a gasto; pipeline con lista autoritativa de lanzamientos + "
     "pincelada inorgánica (moléculas, marcas y registros); conclusiones con el largo plazo deslizado"),
    ("Anexos", "El detalle para Santiago", "5-7",
     "Detalle por segmento y canal con EBITDA y margen; cartera y contratos de gobierno; sizing "
     "diálisis peritoneal; banco Hospitales (Muguerza, convenios PxV, oncológicos); elasticidad; "
     "fuentes y universos"),
]
simple_table(doc, ["#", "Momento", "Lám.", "Qué lleva"], idx_rows,
             [Inches(0.55), Inches(2.15), Inches(0.5), Inches(3.9)], right_from=99)
note(doc, "~35 láminas de cuerpo + anexos (~41 total). Orden de bloques por peso de ventas. Cada bloque de "
          "segmento: entorno y competencia; lámina de puente propia del 1S (nueva convención); qué hicimos "
          "bien / qué nos faltó; plan 2S (el 'qué haremos' vive aquí).")

# ---------------------------------------------------- qué cambió en v6 -----
chapter(doc, "Qué cambió en la v6 (integración de insumos nuevos, 16-jul)")
bullet(doc, [("1 · Nueva convención de puente, sustituye a las llaves del v5. ", True),
             ("Cada segmento lleva una lámina de 3 columnas (15/50/35): crecimiento del mercado vs "
              "PISA; puente de ventas en 5 conceptos (Precio, Volumen, Mix/down-trading, Lanzamientos, "
              "Gestión de Portafolio, maquinaria Downtrading v4); y comparativo 1S-2025 vs 1S-2026 de "
              "venta perdida, PIN no solicitado, NC comerciales y NC logísticas.", False)])
bullet(doc, [("2 · El puente de Retail ya está construido y auditado ", True),
             ("(Downtrading Privado v4 FINAL): precio de lista +$392.9M, volumen -$169.7M, "
              "down-trading -$197.9M, lanzamientos +$43.8M, gestión de portafolio -$37.8M = +$31.3M "
              "(+0.4%). Gobierno FC, Hospitales y Servicios se construyen con la misma maquinaria.", False)])
bullet(doc, [("3 · La tablita gana EBITDA real ", True),
             ("(Estado de Resultados v18, Finanzas): Retail $2,479.1M (34.4%), Hospitales $1,196.8M "
              "(39.2%), Gobierno+Servicios combinado $804.8M (12.9%). Finanzas NO separa FC de "
              "Servicios; el hueco se declara [VJ/Finanzas].", False)])
bullet(doc, [("4 · Research externo bajado a láminas: ", True),
             ("Baxter pasa a 'Baxter/Vantive', bianual con fallo diferido al 28-ago-26, India vía "
              "reliance, ocupación hospitalaria 59%, siniestralidad GMM ~$131,000M, primas +6-10%. El "
              "% del PIB en salud queda descartado por trillado (decisión Rafael 16-jul): el mensaje "
              "macro lo cargan BBVA y ANTAD.", False)])
bullet(doc, [("5 · Entorno retail re-fundado con datos comparables: ", True),
             ("Entry Market -4.2% valor / -7.9% unidades vs PiSA -0.1% / -9.4% (mismo universo "
              "Knobloch); mercado sin GLP-1 +1.4% valor / -4.8% unidades (muere el '-3% sin GLP-1'); "
              "tesis IQVIA 'abril no es outlier' y forecast al cierre.", False)])
bullet(doc, [("6 · Las burbujas ya tienen fuente: ", True),
             ("el deck del canal Farmacias trae TACC 5 años vs último año por línea terapéutica "
              "(mercado total, ético, genérico, OTC); falta rotular valores [CC].", False)])
bullet(doc, [("7 · Hospitales con números duros del canal: ", True),
             ("Mindray $110-121 vs $227 por equipo de bomba; Baxter ejecutando $17 (-40%) en cuentas "
              "puntuales; terapia de infusión $1,473M; Kener catálogo cruzado ~$850M; plan 2S de 7 "
              "palancas $47M/mes contra gap de $57M/mes.", False)])
bullet(doc, [("8 · Gobierno con el universo PEDIDOS como candidatos: ", True),
             ("pedidos $3,901M vs meta $3,993M; no atendido $704M; 'la acabó la factura $463M, la "
              "acabó comercial $859M'; NC devoluciones $330M; sanciones $108M aparte. TODO viaja "
              "[candidato] hasta los datos formales de venta perdida / PIN / NC.", False)])
bullet(doc, [("9 · Servicios con sizing real: ", True),
             ("diálisis peritoneal pública PiSA 31% vs Baxter/Vantive 69% (en IMSS 42/58); Bienestar "
              "e ISSSTE hoy 100% Baxter; SANEFRO 12 clínicas / 4,110 pacientes / ~$1,005M anuales; "
              "las líneas YTD cuadran exacto con el sell-in ($2,219.4M).", False)])
bullet(doc, [("10 · Pendientes y calendario renovados: ", True),
             ("resueltos salen (EBITDA existe, burbujas tienen fuente), nuevos entran (split "
              "FC/Servicios, definición única de venta perdida de gobierno, puente "
              "pedidos-facturación-venta neta).", False)])

# ------------------------------------------------------------------ marco ---
chapter(doc, "Marco de la sesión")
bullet(doc, [("Doble objetivo fijado por Dirección General: ", True),
             ("(1) explicar el desempeño comercial del 1S y (2) presentar cómo llegamos al número del 2S. "
              "90% del contenido es comercial; presentan Felipe y Rafael.", False)])
bullet(doc, [("Doble audiencia: ", True),
             ("los consejeros reciben cuatro modelos de negocio; la familia piensa en el detalle de canales. "
              "El doble clic por modelo responde esa lectura sin fragmentar en 17 canales, y los anexos "
              "cargan el detalle profundo (Santiago pide transparencia: las cosas crudas y duras).", False)])
bullet(doc, [("La aritmética que dicta el tono: ", True),
             ("el 1S cerró en 93.4% ($16,518.5M de $17,678.3M, gap de $1,159.8M); un [96%] anual exige "
              "$18,115.1M en jul-dic, 98.5% sostenido de la meta del semestre. Con contribución de 53 "
              "centavos por peso, ese [96%] alcanza la meta de utilidad del año.", False)])
bullet(doc, [("Fechas duras: ", True),
             ("número del 2S negociado con Heriberto antes del 20; PowerPoint con datos financieros finales "
              "a Presidencia el miércoles 22; pre-read ejecutivo de 3 páginas al cerrar láminas; junta el "
              "lunes 27. Storyboard: revisión el viernes 17 [confirmar con Michelle].", False)])
bullet(doc, [("Principio rector (escrito arriba de la hoja): que no parezca justificación. ", True),
             ("Entorno con datos duros, no adjetivos; desempeño como radiografía; cero escenarios "
              "contrafactuales; meta contra real sin aplauso.", False)])
bullet(doc, [("Nomenclatura y alcance: ", True),
             ("cuatro segmentos / modelos de negocio: Retail, Gobierno (frasco cerrado), Hospitales y "
              "Servicios (= Gobierno Servicios; SAFE/SIA privados viven en Hospitales; terapia de infusión "
              "se reporta dentro del frasco cerrado DE HOSPITALES, no confundir con Gobierno FC). Pesos "
              "sobre los 5 mercados sell-in; el consolidado agrega ~$2.0B de segmentos no desglosados "
              "[alcance por cerrar: RC/CC]. [Cuadre por declarar: el canal Hospitales reporta FC $3,050M "
              "+ SERV $432M = $3,482M contra el segmento sell-in $3,054.5M: RC/IC.]", False)])

# --------------------------------------------- convención del puente -------
chapter(doc, "Convención de la lámina de puente (3 columnas, 15/50/35; sustituye a la del v5)")
bullet(doc, [("Columna 1 (15% del espacio) · Mercado vs PISA: ", True),
             ("barra que compara el crecimiento del mercado del segmento contra el crecimiento de PISA "
              "en ese segmento. Retail: Entry Market -4.2% vs PISA +0.4% [unificar corte de mercado: "
              "CC]; Gobierno: INEFAM -3.8% vs -0.6%; Hospitales: [-5% validar IQVIA] vs +5.1%; "
              "Servicios: n/a, modelos propios (se declara).", False)])
bullet(doc, [("Columna 2 (50%) · El puente de ventas, clasificación nueva (maquinaria Downtrading v4): ", True),
             ("bridge sell-in 1S25 a 1S26 en cinco conceptos que suman exacto (control = 0): Precio "
              "(tarifario puro en familias continuas), Volumen (unidades estándar en continuas), Mix / "
              "down-trading (recomposición interna hacia SKUs baratos, Shapley exacto), Lanzamientos "
              "(lista autoritativa de Rafael) y Gestión de Portafolio (bajas, recodificaciones, valor "
              "no normalizado). Nada se fuerza: el control cierra en cero por construcción.", False)])
bullet(doc, [("Columna 3 (35%) · Comparativo 1S-2025 vs 1S-2026 de las cuatro palancas comerciales: ", True),
             ("venta perdida, PIN no solicitado (planeación de la demanda equivocada que no logramos "
              "vender), NC comerciales y NC logísticas. Niveles lado a lado, no escalones del bridge "
              "(evita el doble conteo del v5). Donde no exista el comparador 2025 (PIN), se declara el "
              "vacío, no se inventa. [Datos formales por segmento: los envía Rafael.]", False)])
bullet(doc, [("Estado de construcción: ", True),
             ("Retail LISTO (v4 FINAL, auditado, dos constructores independientes convergen); Gobierno "
              "FC, Hospitales, Servicios y el consolidado PISA en construcción con la misma maquinaria "
              "[equipo PVM, semana en curso].", False)])
bullet(doc, [("Doble vista de Retail (decisión pendiente de Rafael): ", True),
             ("la vista BRUTA cierra a +$31.3M y cuadra con el +0.4% oficial del sell-in; la "
              "reclasificada (+$58.7M) mueve $27.3M de venta de cierre nov-dic-25 de lanzamientos a "
              "2026 y es analítica. Recomendación: lámina con la bruta y nota al pie de la "
              "reclasificación; nunca citar +$58.7M como crecimiento sell-in.", False)])
bullet(doc, [("Si el Consejo exige el 2-vías clásico: ", True),
             ("sigue disponible como validación (PISA: volumen -$830.7M / precio+mezcla +$1,070.0M, "
              "piezas -5.1%); el puente nuevo es su desglose fino, no otra fuente.", False)])

# -------------------------------------------------------------- momento 0 ---
chapter(doc, "Momento 0 · Apertura y resumen ejecutivo (5 láminas densas y lentas)")
body(doc, [("Mensaje: ", True),
           ("la Dirección General nos puso el número; sí vamos a llegar, y hoy explicamos cómo, empezando "
            "por reconocer que el 1S quedó corto y por qué. Resumen de toda la sesión.", False)])
lamina(doc, "Lámina 1 · Los dos objetivos y el compromiso")
body(doc, [("\"El compromiso del año es [96]; para lograrlo, el 2S debe correr 98.5% de su plan. Vamos "
            "a llegar. Esta sesión explica el primer semestre, el "
            "entorno que enfrentamos segmento por segmento y las iniciativas para lograrlo.\" Al minuto "
            "uno nadie está adivinando cuándo llegamos (Edmundo).", False)])
lamina(doc, "Lámina 2 · Dónde estamos: comparativa mercado vs PISA")
bullet(doc, [("Cerramos el 1S en ", False), ("93.4% del plan con +1.5% de crecimiento", True),
             (" ($16,518.5M contra $17,678.3M; gap $1,159.8M). El +1.5% es enteramente precio y mezcla: el "
              "volumen resta $831M y las piezas caen 5.1%.", False)])
bullet(doc, [("Comparativa mercado vs PISA, mismo universo donde existe: ", True),
             ("en nuestro mercado foco de retail (Entry Market, Knobloch MAT may-26) el mercado cae "
              "-4.2% en valor y -7.9% en unidades; PiSA/AMSA queda -0.1% en valor con -9.4% en piezas: "
              "defendemos valor en un mercado que se hunde. Sector público: INEFAM -3.8% en valor vs "
              "Gobierno FC -0.6%. Hospitales: [-5% por validar IQVIA] vs +5.1%. Crecemos contra "
              "corriente en tres de cuatro segmentos [lámina única: CC].", False)])
bullet(doc, [("El mercado total solo crece por GLP-1 y precio: ", True),
             ("privado sin GLP-1 +1.4% en valor y -4.8% en unidades (Knobloch MAT may-26); la demanda "
              "física cae. Consumo débil: BBVA -4.9% anual a jun-26 (quinta caída consecutiva) y ANTAD "
              "+0.8% nominal, es decir, caída real.", False)])
bullet(doc, [("La cadena de suministro se estabilizó; el reto se movió a acelerar la venta.", False)])
note(doc, "Fuentes: Sell-In cierre jun-26; Knobloch MAT may-26 (Entry Market = mercado foco PiSA/AMSA sin "
          "electrolitos, FI y GLP-1); INEFAM ene-may-26; BBVA Research 15-jul-26. El '-3% sin GLP-1' del v2 "
          "queda retirado: la cifra defendible es +1.4% valor / -4.8% unidades.")
lamina(doc, "Lámina 3 · Dato ganador, con su asterisco declarado")
body(doc, [("Q2 facturó ", False), ("$8,495.7M, +$473.0M contra Q1 (+5.9%)", True),
           ("; junio es el mes #2 ($2,986.9M) y mayo el #6 ($2,843.9M) de los últimos 36 (verificado "
            "contra sell-in, ventana jul-23 a jun-26; el #2 le gana al #3, sep-25, por $1.6M: decir \"el "
            "segundo mejor\" con esa conciencia). El asterisco lo ponemos nosotros: junio trae ~$104M de compra adelantada "
            "identificable (Simi $30M, Nadro $30M, Fanasa $27M, JMP $17M) [cerrar cifra: CC] y en "
            "Hospitales un calendario favorable (5 lunes y ~$10M one-off de mezclas por paros ABC/OCA). "
            "Meta contra real, sin aplauso.", False)])
lamina(doc, "Lámina 4 · El hueco year-to-go, anticipado")
body(doc, [("\"Vamos a llegar al [96%] anual; eso exige $18,115.1M en jul-dic (98.5% del semestre). El "
            "hueco contra el ritmo del 1S se cierra con palancas propias que iremos mostrando segmento por "
            "segmento.\" [Cifra fina del hueco por segmento: RC, con los puentes.]", False)])
lamina(doc, "Lámina 5 · Mapa de la sesión")
body(doc, [("Cuatro bloques por segmento (entorno y competencia, 1S, 2S), ruta consolidada al número, "
            "proyectos críticos y habilitadores. Presupuesto de tiempo por bloque: esta vez sí llegamos a "
            "Servicios.", False)])

# -------------------------------------------------------------- momento 1 ---
chapter(doc, "Momento 1 · Mapa del negocio y boleta competitiva (2 láminas)")
body(doc, [("Mensaje: ", True),
           ("PISA no es un ente único; son cuatro modelos de negocio con mercados y sets competitivos "
            "distintos, y ésta es nuestra posición en cada uno.", False)])
lamina(doc, "Lámina 6 · Los cuatro segmentos en una tabla (la tablita)")
simple_table(
    doc,
    ["Segmento", "% venta 1S", "Cumpl. 1S", "Crec. PISA", "Crec. mercado", "EBITDA $M y %", "% del total"],
    [
        ("Retail", "43.6%", "92.3%", "+0.4%", "-4.2% EM KB", "2,479.1 · 34.4%", "63.9%"),
        ("Gobierno (FC)", "24.4%", "90.0%", "-0.6%", "-3.8% INEFAM", "comb. 804.8 · 12.9%", "20.7%"),
        ("Hospitales", "18.5%", "95.2%", "+5.1%", "-5% [validar IQVIA]", "1,196.8 · 39.2%", "30.8%"),
        ("Servicios", "13.4%", "102.1%", "+4.0%", "n/a (modelos propios)", "[en comb. Gobierno]", "·"),
        ("Soporte (no distribuido)", "·", "·", "·", "·", "-601.1 · n/a", "-15.5%"),
        ("Total Farma MX (5 mercados)", "100.0%", "93.4%", "+1.5%", "·", "3,879.6 · 23.5%", "100.0%"),
    ],
    [Inches(1.15), Inches(0.80), Inches(0.80), Inches(0.80), Inches(1.40), Inches(1.35), Inches(0.80)],
    right_from=1, bold_rows=(5,),
)
note(doc, "Pesos sobre los 5 mercados sell-in ($16,518.5M); Farma MX en el P&L de Finanzas = estos mismos "
          "5 mercados (venta neta $16,519.8M, delta $1.3M por redondeo); el consolidado (~$2.0B "
          "adicionales) queda FUERA de esta vista [alcance y sobre qué universo es el [96]: RC/CC/Rafael]. "
          "EBITDA: Estado de Resultados v18 (Finanzas, acumulado ene-jun-26, EBITDA final $3,879.6M = "
          "23.5% de la venta contra 19.7% en 1S-2025; el salto de +380 pb se explica, no se esconde "
          "[Finanzas/VJ]). Finanzas NO separa Gobierno FC de Servicios: el bloque GOBIERNO combinado trae "
          "venta $6,253.7M, EBITDA $804.8M (12.9%); el split del deck está pendiente [VJ/Finanzas]. "
          "Crecimiento de mercado: Retail = Entry Market Knobloch MAT may-26; Gobierno = INEFAM genéricos "
          "ene-may; Hospitales por validar con IQVIA [CC].")
body(doc, [("Efecto buscado: el Consejo descubre aquí que ", False),
           ("Servicios existe, pesa 13.4% y tiene buen margen", True),
           (". Nunca se ha presentado en junta de Consejo (Madero ha pedido su junta especial). Y el "
            "contraste de márgenes por modelo (Hospitales 39% de EBITDA vs Gobierno combinado 13%) explica "
            "por qué defender cada segmento pide armas distintas.", False)])
lamina(doc, "Lámina 7 · Boleta competitiva: dónde ganamos, dónde perdemos y quién es el villano")
bullet(doc, [("Retail: ", True),
             ("en RX somos #1 en un mercado que se contrae: 16.3% de share en unidades y 14.5% en valores "
              "(el #2 trae 12.3%); en marca propia ~50% de share en cadenas nacionales y ~41% del mercado "
              "direccionable (#2 con 9%). Villano: la migración de valor a volumen, ahora medida: el "
              "down-trading nos costó $197.9M en el semestre (puente v4). Ganamos share, pierde el "
              "pastel.", False)])
bullet(doc, [("Gobierno: ", True),
             ("#1 en volumen del sector público (82.5M de piezas INEFAM); en nuestra canasta de 105 claves "
              "el mercado cae 31.7% y PISA sube a 42.7% de participación (+17.7 pts). Villano: un cliente "
              "subfinanciado que ejecuta mal y paga tarde. Amenaza estructural nueva y citable: India "
              "entra a inyectables vía reliance regulatorio (292 autorizaciones Cofepris oct-nov-25).", False)])
bullet(doc, [("Hospitales: ", True),
             ("proveedor #1 del hospital privado (~45% de los inyectables) con share estable hace años. "
              "Villanos en tres frentes: Mindray en terapia de infusión (la carta de entrada de PISA al "
              "hospital: $1,473M de línea), Baxter/Vantive en soluciones (el negocio base) y Kener en "
              "inyectables (dimensionado: vende ~$1,000M con meta ~$5,000M al 2030, estimación propia de "
              "la industria).", False)])
bullet(doc, [("Servicios: ", True),
             ("líder en hemodiálisis y mezclas; en nutrición somos únicos; en diálisis peritoneal pública "
              "tenemos 31% de los pacientes contra 69% de Baxter/Vantive (en IMSS 42/58). En SIA el líder "
              "es Biossmann, ~4 veces nuestro tamaño, pero concentrado en gobierno (85% de su venta): en "
              "el privado la brecha es menor. Villano: los centros de mezclas (COI y similares) en "
              "Onco.", False)])
note(doc, "[Shares retail por confirmar contra Knobloch: CC. El ~45% hospitalario se citó en revisión "
          "interna; validar antes de imprimir. 'FESA' como razón social no se confirma públicamente: "
          "confirmar nombre legal antes de lámina. Kener sin cifras públicas: se presenta como estimación "
          "propia. Dimensionar Mindray y Baxter/Vantive: Martín/CC.]")

# -------------------------------------------------------------- momento 2 ---
chapter(doc, "Momento 2 · PISA total: qué pasó en el 1S (3 láminas)")
body(doc, [("Mensaje: ", True),
           ("el 93.4% no es una historia, son cuatro: dos tristes (Retail vía farmacias, Gobierno frasco "
            "cerrado) y dos alegres (Hospitales, Servicios); los alegres no compensan a los tristes. "
            "Radiografía honesta, cero contrafactuales.", False)])
lamina(doc, "Lámina 8 · Puente rectora PISA del 1S (nueva convención, 3 columnas)")
bullet(doc, [("Col 1 · Mercado vs PISA: ", True),
             ("mercado total farmacéutico 2025 +9.2% valor / -2.4% volumen (INEFAM); PISA 1S26 +1.5%. "
              "[Elegir el comparador de mercado del 1S para la barra: CC.]", False)])
bullet(doc, [("Col 2 · Puente PISA 1S25 a 1S26 (+$239.3M): ", True),
             ("en 5 conceptos, consolidando los cuatro segmentos [EN CONSTRUCCIÓN, equipo PVM; hoy solo "
              "Retail está terminado]. La física que ya sabemos del 2-vías: el crecimiento es "
              "enteramente precio y mezcla (+$1,070.0M) contra volumen -$830.7M (piezas -5.1%).", False)])
bullet(doc, [("Col 3 · Comparativo 1S25 vs 1S26: ", True),
             ("venta perdida $758.8M a $901.9M (deterioro concentrado en gobierno, con definición en "
              "cierre); PIN no solicitado: nivel 2026 privado $635M, sin comparador 2025 (se declara); "
              "NC logísticas [-$100M candidato, validar cifra y universo: RC]; NC comerciales [VJ]. "
              "[Datos formales 1S25 vs 1S26: los envía Rafael.]", False)])
body(doc, [("Lectura de la lámina: ", True),
           ("el precio de lista defiende el valor, el down-trading y el volumen lo erosionan, los "
            "lanzamientos suman, y las palancas comerciales de la col 3 muestran dónde se ganó y perdió "
            "ejecución contra el año pasado.", False)])
lamina(doc, "Lámina 9 · Desempeño por canal (sustituye al semáforo)")
simple_table(
    doc,
    ["Canal (por segmento)", "Venta ($M)", "Meta ($M)", "Cumplimiento", "Crec. vs 2025"],
    [
        ("Retail · Farmacias", "2,958.0", "3,327.8", "88.9%", "-2.2%"),
        ("Retail · Impulso", "2,785.8", "2,921.1", "95.4%", "+1.8%"),
        ("Retail · Expansión", "1,466.4", "1,564.1", "93.8%", "+3.4%"),
        ("Retail (subtotal)", "7,210.2", "7,813.0", "92.3%", "+0.4%"),
        ("Gobierno · Frasco Cerrado", "4,034.3", "4,484.9", "90.0%", "-0.6%"),
        ("Hospitales", "3,054.5", "3,207.1", "95.2%", "+5.1%"),
        ("Servicios (Gob Servicios)", "2,219.4", "2,173.3", "102.1%", "+4.0%"),
        ("PISA (5 mercados)", "16,518.5", "17,678.3", "93.4%", "+1.5%"),
    ],
    [Inches(2.30), Inches(1.30), Inches(1.30), Inches(1.00), Inches(1.10)],
    right_from=1, bold_rows=(3, 7),
)
note(doc, "Sell-In cierre junio, apertura por canal según los segmentos de la lámina 6. La frontera "
          "FC/Servicios difiere ~$835M contra el universo neto: usar siempre la de Sell-In. Diferencias de "
          "$0.1M por redondeo. [Alcance del consolidado (~$2.0B restantes): RC/CC.]")
lamina(doc, "Lámina 10 · Síntesis y reconocimiento a cadena de suministro")
body(doc, [("Dos tristes y dos alegres; los alegres no compensan: por eso 93.4%. El logro operativo del "
            "semestre se dice como logro, no como excusa:", False)])
bullet(doc, [("Producto negado mejorando de XX a YY [candidato: 640 a 78, abril a junio; validar unidad "
              "(claves vs miles de piezas): FM].", False)])
bullet(doc, [("Fill rate ~95-96% sostenido seis semanas.", False)])
bullet(doc, [("WMAPE de XX a YY [candidato: 51 a 33].", False)])
bullet(doc, [("El servicio recuperado ya vale ZZ al mes de facturación [candidato: $9-12M/mes].", False)])
body(doc, [("Ahora en el 2S el juego es demanda. Puente: \"cuatro realidades exigen cuatro conversaciones; "
            "vamos segmento por segmento\".", False)])

# -------------------------------------------------------------- momento 3 ---
chapter(doc, "Momento 3 · Retail: entorno, 1S, 2S (6 láminas · 43.6% de la venta)")
body(doc, [("Apertura de bloque: \"Retail es el 43.6% de la venta de PISA: Farmacias, Impulso (AMSA) y "
            "Expansión (Medicom, Meditec, La Paz), con marcas propias y Friso adentro. Todo lo que sigue "
            "impacta ese 43.6%.\"", False)])
lamina(doc, "Lámina 11 · Entorno y posición: PISA defiende el valor en un retail que entra en recesión de volumen")
bullet(doc, [("Abril no fue un mal mes: es la tendencia (IQVIA, retail sell-out). ", True),
             ("YTD ene-abr el mercado retail pierde -7.7% en unidades y el +7.8% de valor es 72% GLP-1 "
              "(+176% anual). Abril fue el peor mes: -13.6% en unidades con +3.1% en valores (debajo "
              "del INPC 4.45%); sin GLP-1 el valor de abril CAE [-2.4% p6 / -1.2% p43 del propio "
              "reporte: fijar cifra con IQVIA, CC]. Las recetas confirman lo estructural: "
              "antiinfecciosos -19.7% y respiratorio -30.6% anual; antibióticos -7.7% MAT en valor "
              "(Knobloch).", False)])
sub_bullet(doc, [("Los exógenos están medidos, no son excusa: ", True),
                 ("vacunación institucional +77% (respiratorias +121%), el invierno más cálido de la "
                  "serie (18.9 grados C), gripe acumulada -19.1% (FAN), y el gobierno gana peso en "
                  "respiratorio y antiinfecciosos (su participación en ATC R sube de 24% a 32% y en J "
                  "de 62% a 68%): lo que el sector público surte ya no pasa por el mostrador.", False)])
bullet(doc, [("Nuestro mercado foco (Entry Market, Knobloch MAT may-26): ", True),
             ("-4.2% en valor y -7.9% en unidades; PiSA/AMSA -0.1% en valor con -9.4% en piezas. La "
              "visita médica es el subsegmento más golpeado: -6.7% valor / -13.8% unidades. El "
              "crecimiento del mercado total es GLP-1 ($19.8B, +162.6%), que no jugamos.", False)])
bullet(doc, [("Consumo y canal: ", True),
             ("BBVA -4.9% anual a jun-26 (quinta caída consecutiva) y ANTAD +0.8% nominal, es decir, "
              "caída real; canal saturado con ~90 días de "
              "inventario contra 60 de estándar (mayoristas RX 113-146); la industria entera está "
              "igual.", False)])
bullet(doc, [("El tablero de distribución se reordena: ", True),
             ("cadenas grandes +13% en valor sostienen el mercado; el independiente ya cae (-4% en valor, "
              "-7% en unidades, IQVIA YTD abr); drogueros modernos (Nadro +25%, Fanasa +34%) desplazan al tradicional (Difarmer "
              "-25%); Marzam terminó rescatada por Grupo OMNi (ago-25); Fanasa migra de cliente a "
              "competidor. Regulación de controlados: Tramadol -29% en Simi.", False)])
bullet(doc, [("Terceros que validan (intel de canal, se dice como tal): ", True),
             ("Nadro ajustó su meta de crecimiento de 5% a 3%; Ultra crece 0%. Y el capital de trabajo "
              "del canal se va a GLP-1: los mayoristas financian Mounjaro y no financian el resto.", False)])
note(doc, "Fuentes: IQVIA jul-26 (caída de abril; universo = retail sell-out Rx+OTC, NO cubre canal "
          "hospitalario ni licitación), Knobloch MAT may-26, BBVA Research, INEFAM. Forecast IQVIA para "
          "encuadre interno del 2S: retail 2026e +6.4% en valor con -4.8% en unidades; sin GLP-1 el "
          "year-to-go ronda +2.7-3% (sesión 01-jul); presupuestos 2027 por debajo de 2025.")
lamina(doc, "Lámina 12 · Burbujas por línea terapéutica: dónde crece el mercado, a corto y a largo plazo")
body(doc, [("Gráfica de burbujas por línea terapéutica que separa el crecimiento de corto plazo del de "
            "largo plazo: eje X = TAC 3-5 años, eje Y = crecimiento último año, tamaño = tamaño del "
            "mercado. LA FUENTE YA EXISTE: el deck del canal Farmacias trae las cuatro vistas (mercado "
            "total, ético, genérico, OTC) con TACC 5 años vs último año, base Knobloch; falta rotular "
            "valores por burbuja para imprimir [CC]. Lectura buscada: en qué líneas el corto plazo "
            "castiga a un mercado estructuralmente sano (ahí se aguanta) y en cuáles el deterioro es de "
            "largo plazo (ahí se re-asigna). Solo crecen con fuerza Diabetes/Obesidad (GLP-1) y marcas "
            "propias.", False)])
lamina(doc, "Lámina 13 · Puente Retail 1S (3 columnas; el puente v4 está LISTO)")
bullet(doc, [("Col 1 · Mercado vs PISA: ", True),
             ("Entry Market -4.2% (valor, KB MAT may-26) contra PISA Retail +0.4% (sell-in 1S). "
              "[Unificar periodo del corte de mercado antes de imprimir: CC.]", False)])
bullet(doc, [("Col 2 · Puente Retail 1S25 a 1S26 ($7,178.5M a $7,210.2M, 92.3% de meta): ", True),
             ("Precio +$392.9M; Volumen -$169.7M; Mix / down-trading -$197.9M; Lanzamientos 2026 "
              "+$43.8M; Gestión de Portafolio -$37.8M = +$31.3M en el universo del modelo (control = 0 "
              "dentro de ese universo). Contra el delta del cubo completo (+$31.8M) quedan ~$0.4M de "
              "FLP sin código de material: exclusión estructural, declarada, no forzada. La historia: "
              "subimos precio de lista con éxito, pero el down-trading (la marca cede al genérico "
              "propio) y el volumen se comen dos terceras partes; el neto lo sostienen los "
              "lanzamientos.", False)])
sub_bullet(doc, [("El down-trading tiene nombre y apellido: ", True),
                 ("Amox/Clavulánico -$45.6M, Levofloxacino -$32.9M, Ceftriaxona -$24.7M, Enoxaparina "
                  "-$21.3M, Fexofenadina -$15.9M = 71% del efecto. Caso tipo: Cefaxona ($0.21 por mg) "
                  "cede a los genéricos de la casa a $0.017-0.020 por mg. Friso migra al revés: +$16.4M "
                  "de mezcla positiva (Comfort, AR, etapas superiores).", False)])
sub_bullet(doc, [("Poder de precio neto (el techo real del pricing se lee neto): ", True),
                 ("+$392.9M de lista menos $197.9M de down-trading = ~+$195M efectivos en Retail; la "
                  "mitad de la ganancia de precio se la come el cliente que migra a lo barato.", False)])
sub_bullet(doc, [("Nota de la doble vista: ", True),
                 ("los lanzamientos facturaron además $27.3M de cierre en nov-dic-25; reclasificados a "
                  "2026 la delta analítica es +$58.7M. La lámina usa la vista bruta (+$31.3M), que "
                  "cuadra con el +0.4% oficial [decisión de vista: Rafael].", False)])
bullet(doc, [("Col 3 · Comparativo 1S25 vs 1S26: ", True),
             ("venta perdida $359.0M a $343.5M (mejora, fuente DP); PIN no solicitado: nivel 2026 "
              "$564M (Farmacias 251, Impulso 151, Expansión 162), sin comparador 2025 declarado; NC "
              "comerciales y NC logísticas [por llegar: VJ/RC].", False)])
lamina(doc, "Lámina 14 · Doble clic del 1S: farmacias concentra el deterioro")
bullet(doc, [("Farmacias 88.9% y -2.2%: ", True),
             ("concentra el gap (-$369M, 56% es marca propia). MP -10.5% (81.2% de meta) fue capacidad y "
              "liberación, no demanda, y ya se corrigió: MP crece desde mayo (+$21M el bimestre). Consumo "
              "crece fuerte [dos cortes en la mesa: sublínea OTC +46.1% (102.6% de meta) vs UDN Consumo "
              "+23.7% (81%); elegir cuál cuenta la historia: Rafael+IC].", False)])
bullet(doc, [("Impulso 95.4% y +1.8%: ", True),
             ("valor sobre volumen deliberado: la elasticidad funcionó (+$51M de beneficio de precio contra "
              "$32M plan; subimos precio sin perder el volumen esperado).", False)])
bullet(doc, [("Expansión 93.8% y +3.4%. ", True),
             ("Friso gana share y migra hacia arriba en un mercado premium que se hunde (-5.1% contra "
              "-8.5% del mercado; mezcla +$16.4M).", False)])
lamina(doc, "Lámina 15 · Retail: qué hicimos bien, qué nos faltó")
bf_table(
    doc,
    bien=[
        "Elasticidad en Impulso: +$51M de precio contra $32M plan, con el volumen esperado",
        "Corrección de raíz en marca propia: negados a la baja; MP crece desde mayo",
        "Servicio 95%+ seis semanas: RX cerró junio en 101% de meta",
        "Friso gana share y defiende valor vía mezcla (+$16.4M) en mercado que cae",
        "Lanzamientos aportan +$43.8M al puente (Sitagliptina, Votripax B+L, Pisagot)",
    ],
    falto=[
        "Farmacias 88.9%: el gap de MP del 1S ya estaba hecho cuando el servicio volvió",
        "Down-trading -$197.9M: la marca cede al genérico propio en 5 franquicias identificadas",
        "Faltantes largos cedieron share caro de recuperar (Bufigen, Pisartra)",
        "Venta perdida de Farmacias empeoró (+$27M vs 1S25)",
        "El canal quedó saturado: 90-120 días de inventario",
    ],
)
lamina(doc, "Lámina 16 · Plan 2S de Retail y su aporte al hueco")
bullet(doc, [("Segundo incremento de precios en julio con gestión de elasticidad por canal [VJ].", False)])
bullet(doc, [("Defensa de la mezcla como palanca nueva: ", True),
             ("las 5 franquicias down-trader (Amox/Clav, Levo, Ceftriaxona, Enoxaparina, Fexofenadina) "
              "son la lista de trabajo inicial: defensa de marca de visita médica, surtido y condiciones "
              "por canal, arquitectura de precios del genérico propio.", False)])
bullet(doc, [("Ventana de 90 días en MP: $21M YTG ya cotizados + proyecto de 20 moléculas (top-to-top con "
              "Ahorro).", False)])
bullet(doc, [("Q3 de drenaje por diseño: DDI top de 120 a 70, concursos, CEDIs de drogueros, fachadas 100 "
              "(caso a 1,000).", False)])
bullet(doc, [("NADAL Retail YTG ~$244M farmacias + $70M impulso, con KPIs mensuales y el real de junio "
              "declarado (MP 98%, Consumo 87%, Impulso 66%, EXP 186%, RX 0%: la palanca RX se corrige "
              "en julio).", False)])
bullet(doc, [("Lanzamientos con foco: el GAP anual proyecta 83% (Votripax 57%, Pisalak 68%, Pixiba 73%); "
              "plan invernal se factura en septiembre (orden 25-sep).", False)])
body(doc, [("Aporte de Retail al hueco del [96%] [cifra: RC]. Riesgo del bloque, dicho por nosotros: julio "
            "arranca hipotecado por la compra adelantada de junio y el sobre-inventario; el drenaje es la "
            "secuencia planeada para llegar sanos al Q4 estacional, no una sorpresa de octubre.", False)])

# -------------------------------------------------------------- momento 4 ---
chapter(doc, "Momento 4 · Gobierno: entorno, 1S, 2S (4 láminas · 24.4% de la venta)")
body(doc, [("Apertura de bloque: \"Gobierno frasco cerrado es el 24.4% de la venta.\" (Servicios se "
            "presenta como cuarto bloque.)", False)])
lamina(doc, "Lámina 17 · Entorno: caemos seis veces menos que el mercado de un cliente que ejecuta mal y no paga")
bullet(doc, [("Dos hechos con fuente que no se pueden revirar: ", True),
             ("ejecución fallida (compra consolidada anulada por sobreprecio ~13,000 mdp; la ronda "
              "cubrió solo 50.5% de claves) y no pagan (adeudos ~14,000 mdp según industria contra "
              "~5,000 reconocidos). Matiz anti-revire en reserva: el presupuesto 2026 creció +5.9% "
              "real y aun así está -4.7% contra lo ejercido en 2024. [Numerito macro único por elegir: "
              "Edmundo/Rafa; el % del PIB en salud quedó descartado por trillado, decisión Rafael "
              "16-jul.]", False)])
bullet(doc, [("Tendencias con información privilegiada ", True),
             ("(lo que le abre la mente al Consejo): (1) retraso relevante de la compra consolidada; (2) "
              "subatención y subagotamiento de contratos: nos piden por debajo de la meta [candidato, "
              "universo pedidos: piden $3,901M de una meta de $3,993M y facturamos $3,235M; puente "
              "pedidos-facturación-venta neta por declarar: DS/Dani]; (3) cambios fuertes de cuadros: "
              "baja de la Dra. Karla en la Secretaría de Salud, la principal aliada del abasto; (4) la "
              "PI se endurece PRO-innovador: reformas DOF abr-2026 (5 años de protección de datos + "
              "certificado que extiende patente hasta +5 años), México en Priority Watch List y revisión "
              "anual del T-MEC desde el 1-jul (no hay arbitraje: es Special 301); los genéricos se "
              "retrasan; (5) [tendencias SS / Birmex / IMSS / ISSSTE: Felipe + Hugo Bobadilla].", False)])
bullet(doc, [("Mercado opaco que se descapitaliza: ", True),
             ("INEFAM genéricos -3.8% en valor y -12.5% en piezas (ene-may); el no pago quiebra a jugadores "
              "débiles: a mediano plazo (2027) consolida el mercado a nuestro favor, en 2026 juega en "
              "contra (liquidan inventario vía impulso y presionan precios). [El +30-35% que arroja "
              "AlphaDog para pedidos de genéricos está RECHAZADO y en re-validación con definiciones "
              "correctas: Chery. Bullets de competidores por clave, erosión y % de compras directas, "
              "con dato: Chery/DS.]", False)])
bullet(doc, [("Regla de la sección: ", True),
             ("NO abrir el debate \"queremos venderle a quien no paga\"; está superado hace dos años. Si lo "
              "sacan, el racional está listo: margen ~25%, PISA tiene el capital para aguantar la cartera, "
              "y da ventaja de compras/volumen/costos. En reserva: gobierno es ~60% del volumen de plantas "
              "(insulinas y soluciones ~80% [dato preciso: Víctor]) y la nueva fábrica de oncológicos "
              "destinará 95% de su volumen ahí. [Alinear postura con Juan Jaime: Dirección.]", False)])
lamina(doc, "Lámina 18 · Puente Gobierno FC 1S (3 columnas)")
bullet(doc, [("Col 1 · Mercado vs PISA: ", True),
             ("INEFAM -3.8% en valor contra Gobierno FC -0.6%: caemos seis veces menos que el "
              "mercado.", False)])
bullet(doc, [("Col 2 · Puente Gobierno FC 1S25 a 1S26 ($4,059.2M a $4,034.3M, -$24.9M, 90.0% de meta): ", True),
             ("[EN CONSTRUCCIÓN con la maquinaria v4: equipo PVM]. Referencia 2-vías mientras tanto: "
              "volumen -$8.1M / precio y mezcla -$16.8M. Dato del diagnóstico parcial: FC sube de gama "
              "(mix +$112.8M en las moléculas medibles), al revés del privado.", False)])
bullet(doc, [("Col 3 · Comparativo 1S25 vs 1S26 [TODO candidato hasta datos formales]: ", True),
             ("venta perdida: 'la acabó la factura' $463M [candidato; definición única en cierre entre "
              "restricto $342M, DP $443.9M y el criterio de Fer Mendoza $595-600M: DS/FM]; PIN no "
              "solicitado ('la acabó comercial'): $859M [candidato; planchar 859 vs 869 con Hugo y "
              "Daniel Torres]; NC por devoluciones: $330M vs ~$357M en 2025 [candidato; verificar si "
              "excluye sanciones: Dani]; sanciones pagadas $108M, renglón aparte, no se mezclan.", False)])
note(doc, "El universo PEDIDOS (pedidos, no atendido, PIN) NO es el universo sell-in: se declara en la "
          "lámina y el puente entre ambos vive en anexo [DS]. Los $704M no atendidos = $544M negados + "
          "$90M sin inventario con pedido vigente + $70M con inventario confirmado que factura julio; de "
          "esos $704M solo $342M estaban pineados.")
lamina(doc, "Lámina 19 · Gobierno: qué hicimos bien, qué nos faltó")
bf_table(
    doc,
    bien=[
        "PISA #1 en volumen del sector público (82.5M pzs INEFAM)",
        "En nuestra canasta de 105 claves el mercado cae 31.7% y subimos a 42.7% de share (+17.7 pts): ganamos share en la contracción",
        "Q2 de FC al 99% en junio; IMSS +12.1%",
        "NC totales -53% vs 2025 [candidato: 428M vs cifra 25 por cerrar]",
    ],
    falto=[
        "FC quedó en 90.0% y -0.6% (Q1 ~88%)",
        "No nos piden lo suficiente: subatención de contratos [candidato, universo pedidos]",
        "Venta perdida de gobierno se deterioró [definición única en cierre: DS/FM]",
        "PIN no solicitado ~$859M: planeación de demanda equivocada que no logramos vender [candidato]",
        "Cartera: +22% vs cierre 2025 ($4,834M al 30-jun; FC 5.3 meses de venta, Servicios 3.4); IMSS Bienestar -43.1%",
    ],
)
lamina(doc, "Lámina 20 · Plan 2S de Gobierno y su aporte al hueco")
bullet(doc, [("NADAL Gobierno FC: palancas de claves, PIN y Bienestar ($110M en may-jun a 60%; YTG con "
              "KPIs).", False)])
bullet(doc, [("Cumplimiento de contratos y cobranza como foco del semestre, con meta en pesos y fecha "
              "[cifra cobrada al 30-sep: DS] (cartera medida junio contra junio, cartera entre venta de "
              "últimos doce meses).", False)])
bullet(doc, [("Separar sanciones de NC para leer el síntoma correcto [DS].", False)])
bullet(doc, [("Bianual consolidada, dicho por nosotros: no es viento a favor en 2026; el fallo se difirió "
              "al 28-ago-26 (3,831 claves) y los primeros pedidos llegan hasta enero 2027 (lámina "
              "soporte de contratos: DS).", False)])
body(doc, [("Aporte al hueco [RC]. Riesgo del bloque: gobierno sin pagar; el plan del 2S no depende de que "
            "pague pronto, depende de surtir bien lo contratado y cobrar con disciplina.", False)])

# -------------------------------------------------------------- momento 5 ---
chapter(doc, "Momento 5 · Hospitales: entorno, 1S, 2S (5 láminas · 18.5% de la venta)")
body(doc, [("Apertura de bloque: \"Hospitales es el 18.5% de la venta.\" El contraste que gobierna el "
            "bloque: el segmento de mayor crecimiento, en el entorno competitivo más agresivo.", False)])
lamina(doc, "Lámina 21 · Entorno 1: crecemos +5.1% mientras el pagador cambia el juego")
bullet(doc, [("Crisis de aseguradoras, con datos duros: ", True),
             ("siniestralidad GMM ~$131,000M al cierre 2025 (+14.7%); primas 2026 subiendo +6-10% "
              "general y hasta +40% en adultos mayores; inflación médica 14.8% (cuatro veces la "
              "general); IVA 16% no acreditable encarece pólizas. Las aseguradoras cubren 80-85% del "
              "costo e intervienen el flujo. El efecto duro llega en Q4-2026 al vencer las últimas "
              "pólizas.", False)])
bullet(doc, [("El hospital pierde tráfico: ", True),
             ("ocupación hospitalaria privada 59% (21 pts bajo el estándar de 80%), quirófanos ~50%. El "
              "pagador redirige el flujo oncológico: el hospital marca 300-400% la quimio (según "
              "nuestras conversaciones con pagadores) y los centros de infusión crecen (Alivia ~15 "
              "clínicas, COI 12 sedes); las mezclas se commoditizan.", False)])
bullet(doc, [("Vista IQVIA del mercado hospitalario: ", True),
             ("tamaño y crecimiento del mercado [CC; la lámina del canal venía vacía, y el reporte "
              "IQVIA de abril NO cubre el canal hospitalario: el -5% de la tablita no sale de ahí; es "
              "otro corte que hay que conseguir; valida de paso el -5%].", False)])
bullet(doc, [("Tráfico hospitalario, proxy propio: ", True),
             ("venta de equipo de bomba y soluciones contra promedio 2025 (existe en el deck del canal: "
              "junio recupera, 105.1 mil piezas de Eq/Bomba vs base 104.5) [cifras mismas tiendas vs "
              "totales: equipo].", False)])
lamina(doc, "Lámina 22 · Entorno 2: la amenaza viene en tres frentes, y la respuesta")
bullet(doc, [("Mindray, en terapia de infusión (frente 1): ", True),
             ("la terapia de infusión es la carta de entrada de PISA al hospital ($1,473M de línea; "
              "soluciones + equipo de bomba = $930M, 63% de la línea): colocamos bombas en comodato y "
              "vendemos el consumible. Mindray llega con equipos desde $110-121 contra $227 de "
              "PISA/ZMIN, con consumible propio (InfusoSafe) para capturar el flujo recurrente; 200 "
              "clientes nos compran arriba de $200. Es amenaza estructural, no oportunista: su negocio "
              "internacional necesita mercados como México.", False)])
bullet(doc, [("Baxter/Vantive, en soluciones (frente 2): ", True),
             ("amenaza directa al negocio base; ya ejecuta $17 por pieza (-40%) en cuentas puntuales "
              "contra nuestros 21-25. Matiz del research: las plantas de sueros de Cuernavaca y "
              "Atlacomulco son de VANTIVE (Carlyle) desde ene-25; Baxter México queda a la mitad de "
              "tamaño y declara pivote al hospital privado. [La respuesta del canal a este frente está "
              "'por definir': cerrar con Martín antes del 27.]", False)])
bullet(doc, [("Kener, en inyectables (frente 3, dimensionado): ", True),
             ("compra mercado a pérdida con Grupo Ángeles como vehículo (meropenem a $75 de lista contra "
              "$600-800; 35,000 médicos credencializados). Nuestro catálogo cruzado con el suyo vale "
              "~$850M (~$300M en corporativos) y en Ángeles ya nos desplazó ~$43M en 2025. En "
              "proporción: vende ~$1,000M con meta ~$5,000M al 2030 (estimación propia; lo público: "
              "GEA lo compró en ~200 mdd e invierte ~5,200 mdp con mezclas oncológicas en 1T-2027). No "
              "es el foco de la sesión de hospitales.", False)])
bullet(doc, [("El cliente también cambia: ", True),
             ("fondos comprando hospitales (Polar con PC Capital: 10 en 3.5 años y +3 en plan; MAC con "
              "General Atlantic ~160 mdd; Amerimed pasó a Hospiten) y compradores-auditores (Star "
              "Médica: \"me deben $32M\", exige facturas de competidores y rebates tipo innovador). "
              "[El nombre 'Asura' no existe públicamente: verificar con Martín.]", False)])
bullet(doc, [("La respuesta (héroe: Martín): ", True),
             ("defensa de la base instalada de infusión y soluciones (comodatos, servicio, costo total); "
              "Plan Kener con defensa selectiva y gobierno central de precios de pelea (\"láser\", no barra "
              "libre); ~40 convenios multi-hospital por ~$25M/mes con business reviews; fidelidad "
              "estructural (tecnología de infusión, consigna, quirófano inteligente). Donde no hay solución "
              "todavía, se dice: \"identificado, esto estamos haciendo\". [Decidir mención de talento "
              "ex-PISA: Felipe/Rafa.]", False)])
lamina(doc, "Lámina 23 · Puente Hospitales 1S (3 columnas)")
bullet(doc, [("Col 1 · Mercado vs PISA: ", True),
             ("[-5% por validar IQVIA] contra +5.1% de PISA: crecemos contra corriente.", False)])
bullet(doc, [("Col 2 · Puente Hospitales 1S25 a 1S26 ($2,906.6M a $3,054.5M, +$147.9M, 95.2% de meta): ", True),
             ("[EN CONSTRUCCIÓN con la maquinaria v4: equipo PVM]. Referencia 2-vías mientras tanto: "
              "volumen +$14.8M / precio y mezcla +$133.2M (piezas +0.5%). La cascada propia del canal "
              "(precio -8, volumen +93, altas y bajas +25, servicios +41) se usa como insumo, no se "
              "hereda: taxonomía distinta y errores de armado detectados.", False)])
bullet(doc, [("Col 3 · Comparativo 1S25 vs 1S26: ", True),
             ("venta perdida $188.2M a $114.5M (la gran mejora del segmento, -$73.7M); PIN no "
              "solicitado: nivel $71M (bolsa real ~$42M, $30M comprometidos al 2S), sin comparador "
              "2025; NC comerciales y logísticas [por llegar: VJ/RC].", False)])
lamina(doc, "Lámina 24 · Hospitales: qué hicimos bien, qué nos faltó")
bf_table(
    doc,
    bien=[
        "+5.1%: el mayor crecimiento, en el entorno más agresivo",
        "Anestesia/SIA privado +18.1% (102.3% de meta); mezclas/SAFE privado +9.5% (103.7%)",
        "Venta perdida mejoró $74M contra 1S25",
        "Convenios multi-hospital: ~$25M/mes desde marzo",
        "Cartera respondiendo: liberación al 90% capturó 40% de lo proyectado en 2 semanas; Dalinde paga $4M/semana",
    ],
    falto=[
        "Abr-may costó la mitad del crecimiento (+9/10% a +5%): ocupación (exógena), crédito (autoinfligida, ya respondiendo) y presión de precios (estructural); 89% de meta esos dos meses",
        "Pérdida de Grupo Ángeles CDMX en mezclas (-$10M/mes; -22% el semestre)",
        "El PIN usado como meta y no como señal de demanda (bolsa mal ajustada)",
        "Junio 99% (+12%) lleva asterisco: 5 lunes y ~$10M one-off de mezclas (paros ABC/OCA)",
    ],
)
lamina(doc, "Lámina 25 · Plan 2S de Hospitales y su aporte al hueco")
bullet(doc, [("Brecha 2S dimensionada ($57M/mes: venta promedio ene-may $429M contra meta promedio "
              "jul-dic $485M) y cubierta con 7 palancas ~$47M/mes: recuperación de cuentas $14M, Plan "
              "Kener $9M, liberación de cartera $7M, nuevos productos $6M, PIN no solicitado $5M, "
              "convenios $4M, cambio de tecnología $2M; medición formal desde julio (piloto jun: $11M, "
              "23%).", False)])
bullet(doc, [("Defensa de la base instalada: comodatos de infusión y soluciones frente a Mindray y "
              "Baxter/Vantive (servicio, costo total, contratos) [plan frente Baxter por cerrar: "
              "Martín].", False)])
bullet(doc, [("Plan Kener: defensa selectiva con precio gobernado, no guerra de descuentos.", False)])
bullet(doc, [("Apriete de cumplimiento de convenios (+$3-4M/mes identificados; 32 hospitales en PxV, "
              "$9.4M/mes de beneficio negociado).", False)])
bullet(doc, [("Híbrido con centros de infusión: PISA mezcla con cumplimiento regulatorio, ellos ponen "
              "pagadores (primer gate 14-jul).", False)])
bullet(doc, [("Riesgo declarado: las últimas pólizas con IVA deducible vencen en Q4.", False)])
body(doc, [("Aporte al hueco [RC]. Julio es el mes de la prueba: sin quinto lunes, el run-rate de palancas "
            "tiene que compensar el calendario.", False)])

# -------------------------------------------------------------- momento 6 ---
chapter(doc, "Momento 6 · Servicios: entorno, 1S, 2S (5 láminas · 13.4% de la venta)")
body(doc, [("Apertura de bloque: \"Servicios es el 13.4% de la venta, con buen margen, y es la primera vez "
            "que lo presentamos en una junta de Consejo.\" Información nueva: va a sorprender; proteger el "
            "tiempo para llegar aquí. Se cuenta Servicios como conjunto, no negocio por negocio "
            "(instrucción Rafael 15-jul).", False)])
lamina(doc, "Lámina 26 · Qué es Servicios y por qué importa")
body(doc, [("Nefrología (hemodiálisis y diálisis peritoneal), mezclas (oncología y nutrición) y servicios "
            "integrales de anestesia. 13.4% de la venta, 102.1% de cumplimiento, +4.0%, con demanda "
            "estructural creciente (enfermedades crónicas y diabetes sostienen hemodiálisis y mezclas). "
            "Las líneas cuadran exacto con el sell-in: mezclas $886M (-4%), diálisis $735M (+10%), "
            "hemodiálisis $545M (+13%), anestesia $53M (-13%) = $2,219.4M. Es el positivo natural del "
            "deck: pocos competidores y ventaja propia, sin decir jamás \"no hay competencia\".", False)])
lamina(doc, "Lámina 27 · Dinámica competitiva por modelo de negocio (no es un mercado clásico)")
bullet(doc, [("Nefrología · diálisis peritoneal, el sizing completo: ", True),
             ("mercado público ~53,400 pacientes/año (~$5,631M): PISA 31% de los pacientes contra 69% "
              "de Baxter/Vantive; en IMSS somos 42% (16,000 pacientes) y dominamos 17 de 47 "
              "delegaciones. Baxter es 27-49% más caro por bolsa. IMSS Bienestar (7,800 pacientes) e "
              "ISSSTE (6,100) hoy son 100% Baxter: espacio de entrada, limitado por restricciones "
              "técnicas y cobranza. El foso real no es la bolsa: es la logística de entrega mensual a "
              "domicilio en todo el país. Ojo research: el rival renal ahora es Vantive-Carlyle con "
              "capital fresco (USD 70M en Cuernavaca).", False)])
bullet(doc, [("Nefrología · hemodiálisis: ", True),
             ("relativamente blindada por infraestructura y costo (SANEFRO: 12 clínicas en 6 estados, "
              "4,110 pacientes, ~$1,005M anuales); crece +13% (6% sesiones, 7% precio). Riesgo "
              "tecnológico a declarar: que no nos pase lo de bombas de infusión; adelantar la inversión "
              "en tecnología antes de que llegue el jugador chino.", False)])
bullet(doc, [("Mezclas: ", True),
             ("en nutrición somos únicos; en oncología la competencia es creciente y seria: centros de "
              "mezclas (COI de Fanasa, 12 sedes), consorcios y oncólogos con clínicas propias "
              "['FESA': confirmar razón social antes de imprimir]. Nuestro precio de mezclado onco está "
              "muy por arriba de la competencia (~$831 vs ~$600): sostiene margen hoy, es fragilidad "
              "mañana; se dice con elegancia como riesgo gestionado.", False)])
bullet(doc, [("SIA: ", True),
             ("un solo competidor, pero es el líder y ~4 veces nuestro tamaño (Biossmann), concentrado "
              "en gobierno (85% de su venta): en el privado la brecha es menor.", False)])
lamina(doc, "Lámina 28 · Puente Servicios 1S (3 columnas)")
bullet(doc, [("Col 1 · Mercado vs PISA: ", True),
             ("n/a: modelos propios sin mercado auditado comparable (se declara en lámina).", False)])
bullet(doc, [("Col 2 · Puente Servicios 1S25 a 1S26 ($2,134.9M a $2,219.4M, +$84.5M, 102.1% de meta): ", True),
             ("[EN CONSTRUCCIÓN con la maquinaria v4: equipo PVM]. Referencia 2-vías mientras tanto: "
              "volumen -$671.6M / precio y mezcla +$756.1M, con churn de claves (628 nuevas, 836 "
              "perdidas) que hace frágil cualquier split fino; se lee como mezcla de contratos y "
              "precio. El diagnóstico parcial de mix trae unidades de biológicos dudosas (cobertura "
              "18.2%): no se imprime sin revisión.", False)])
bullet(doc, [("Col 3 · Comparativo 1S25 vs 1S26: ", True),
             ("venta perdida ~0; PIN no solicitado n/d (se declara el vacío); NC [DS].", False)])
bullet(doc, [("[Cifras finales e historia por modelo (HD/DP/Onco/Nutri/SIA): DS y equipo, storyline de "
              "Servicios en construcción por David y Dani.]", False)])
lamina(doc, "Lámina 29 · Servicios: qué hicimos bien, qué nos faltó")
bf_table(
    doc,
    bien=[
        "102.1% de cumplimiento y +4.0%: el único segmento arriba de meta",
        "Hemodiálisis +13% con precio y sesiones; blindada por infraestructura y costo",
        "Diálisis +10% (disciplina de precio); nutrición sin competencia: somos únicos",
        "Mezclas: mejor margen operativo con menos centros (bruto 63%, operativo 22% en 2025)",
    ],
    falto=[
        "Mezclas -4% YTD: salidas de capacidad y -$50M en hospitales privados",
        "Onco: la competencia seria ya está adentro (COI, centros de infusión) y el flujo migra",
        "Anestesia -13% YTD",
        "Presión de descuentos en diálisis peritoneal",
    ],
)
lamina(doc, "Lámina 30 · Plan 2S de Servicios")
bullet(doc, [("Las dos caras del portafolio, dichas por nosotros: ", True),
             ("lo que achicamos por decisión (SAFE y NPT: salida en curso; mezclas de gobierno de "
              "~$1,800M hacia ~$1,600M por decisión de riesgo, no por derrota) y lo que crecemos e "
              "invertimos (hemodiálisis, diálisis, anestesia; ampliaciones de ~4,100 a ~5,200 "
              "pacientes) [inversiones con bendición de Finanzas antes de presentarse: César/DS].", False)])
bullet(doc, [("Mantener: Servicios es una de las dos patas del compromiso del 2S.", False)])
bullet(doc, [("Disciplina de precio en DP (descuentos con contraparte) y defensa de Onco coordinada con el "
              "capítulo Hospitales (híbrido con centros de infusión).", False)])
bullet(doc, [("Adelantar la renovación tecnológica de diálisis (el espejo de Mindray como argumento de "
              "inversión).", False)])
note(doc, "El EBITDA de Servicios llega contaminado de reclasificaciones en disputa con Finanzas (diálisis "
          "al 0% con margen bruto ~70%): al Consejo solo sube el dato conciliado o el hueco declarado "
          "[VJ/Finanzas/DS]. El pleito no se menciona en la junta.")

# -------------------------------------------------------------- momento 7 ---
chapter(doc, "Momento 7 · La ruta consolidada al número (2 láminas)")
body(doc, [("Mensaje: ", True),
           ("el 2S se construye con palancas propias, no con esperanza de mercado. Aquí solo se consolida "
            "lo que ya se fue mostrando bloque por bloque.", False)])
lamina(doc, "Lámina 31 · Cascada year-to-go consolidada")
bullet(doc, [("De la base jul-dic al [96 anual / 98.5% del semestre].", True)])
bullet(doc, [("El punto de partida ya incorpora el servicio normalizado ", True),
             ("(mejor fill rate, menos devoluciones): no se argumenta como escenario, queda implícito en el "
              "dibujo; la tendencia logística es favorable y va a poner su parte.", False)])
bullet(doc, [("NADAL: ", True),
             ("bruto full-year $2,337.1M, $1,402.2M a 60% de efectividad; seguimiento semanal y KPIs "
              "mensuales jul-dic, con el real de junio ya medido por palanca.", False)])
bullet(doc, [("Segundo incremento de precios de julio.", False)])
bullet(doc, [("Nuevos productos [VW]; en Retail ya medidos: +$43.8M del puente v4.", False)])
bullet(doc, [("Disciplina comercial: corrección de descuentos y NC, y defensa de la mezcla (las 5 "
              "franquicias down-trader como lista de trabajo).", False)])
bullet(doc, [("Plan invernal (orden 25-sep); inventarios y coberturas mejores que en el 1S.", False)])
bullet(doc, [("Todo respalda dos afirmaciones: ", True),
             ("el plan NADAL en frasco cerrado va a funcionar y Servicios se va a mantener.", False)])
note(doc, "Los ahorros de $350M siguen fuera de esta lámina (decisión Rafael 10-jul). [Decidir si se "
          "presenta el ROI de un ejecutivo de ventas dentro de disciplina de gasto: Felipe/Rafa. El "
          "encuadre externo del forecast IQVIA (mercado ~+3.5-4.5% valores) vive en anexo, no aquí.]")
lamina(doc, "Lámina 32 · Riesgos que decimos nosotros y mecanismo de seguimiento")
body(doc, [("Riesgos declarados antes de que los digan ellos: julio arranca hipotecado por la compra "
            "adelantada de junio y el sobre-inventario del canal (90-120 días); las últimas pólizas con IVA "
            "deducible vencen en Q4; el gobierno sigue sin pagar. Mecanismo: KPIs NADAL mensuales por "
            "segmento y tablero de hipótesis del 2S con métrica y fecha. Calibrar con Felipe la narrativa "
            "\"junio bueno / julio hipotecado\" para que no choque con el 98.5% sostenido (objeción de Fer): "
            "la salida es presentar el drenaje del Q3 como secuencia planeada con Q4 estacional detrás.", False)])

# -------------------------------------------------------------- momento 8 ---
chapter(doc, "Momento 8 · Proyectos críticos, habilitadores y conclusiones (3 láminas)")
body(doc, [("Mensaje: ", True),
           ("además de cerrar el año, sembramos dónde jugar. Pinceladas explícitamente acotadas: la "
            "estrategia completa viene en el plan de largo plazo de septiembre, no se improvisa aquí.", False)])
lamina(doc, "Lámina 33 · Habilitadores con efecto en el 2S")
body(doc, [("E-commerce contribuye a la venta del 2S; transformación digital y estructural, al gasto; y el "
            "motor de elasticidad con IA capitaliza 18-24 meses de experimentos de precio (insumo directo "
            "de la meta 2027).", False)])
lamina(doc, "Lámina 34 · Portafolio: pipeline discreto y pincelada inorgánica")
bullet(doc, [("Pipeline con credibilidad reconstruida: ", True),
             ("hoy jugamos en la parte menos atractiva de un mercado que sí crece (GLP-1 se lleva el "
              "crecimiento) y el plan es movernos a las albercas que crecen. Sin prometer al Gran Salvador: "
              "aprendemos de los chiquitos para no equivocarnos cuando lleguen los grandotes (Pixiba 28% de "
              "share en unidades a meses del lanzamiento; Sitagliptina con objetivo 10% si no hay pausas de "
              "suministro; los lanzamientos 2026 ya aportan +$43.8M al puente de Retail con lista "
              "autoritativa y GAP anual proyectado de 83%). El detalle vive en el comité de nuevos "
              "productos.", False)])
bullet(doc, [("La ventana GLP-1, dicha con precisión: ", True),
             ("la patente base de semaglutida venció (mar-26) pero México queda bloqueado por protección "
              "de datos clínicos; genéricos posibles hacia 4T-26/2027, y las reformas de abril alargan la "
              "fricción para todos (arma de doble filo para nuestro propio pipeline).", False)])
bullet(doc, [("Pincelada inorgánica acotada a moléculas, marcas y registros (no compañías): ", True),
             ("comprar registros sanitarios atorados para ahorrar 12-18 meses de trámite; licenciar o "
              "comprar moléculas del innovador que se repliega; y adquirir o crear marcas para rejuvenecer "
              "el portafolio (hoy 14% de la venta AMSA con marca contra 68% del mercado). [Casos y sizing: "
              "Estrategia; sin comprometer montos en esta junta.]", False)])
lamina(doc, "Lámina 35 · Conclusiones")
body(doc, [("Reafirmar el compromiso del [96] y el mecanismo de seguimiento mensual. Y aquí, solo aquí, "
            "se desliza en una línea la nota de largo plazo: población envejeciendo, enfermedades crónicas "
            "al alza (diabetes 17-18% de adultos, hipertensión 29.4%, ERC quinta causa de muerte: "
            "Ensanut/INSP), nearshoring; vientos de cola no para 2026, pero sí para los siguientes 20 "
            "años. Una mención, sin abrir sesión de estrategia: esta junta es táctica y ya tiene "
            "número.", False)])
note(doc, "[Definir el ASK explícito al Consejo (hallazgo del consejo adversarial): qué se le pide, si "
          "tomar nota y endosar el compromiso y su mecanismo de seguimiento, o además respaldar las "
          "inversiones de Servicios. Hoy el deck no lo dice: Rafael/Felipe.]")

# ----------------------------------------------------------------- anexos ---
chapter(doc, "Anexos (el detalle para Santiago; 5-7 láminas)")
body(doc, [("Dos audiencias, un deck: el cuerpo es simple y los anexos cargan la profundidad. Santiago no "
            "necesita ver todo el detalle en sesión; necesita evidencia de que nosotros lo vemos y "
            "decidimos con él.", False)])
bullet(doc, [("Anexo A · Detalle por segmento y canal: ", True),
             ("evolución mensual, share por competidor donde exista fuente (Knobloch, INEFAM, Close-Up) y "
              "detalle de EBITDA y margen por segmento del Estado de Resultados v18 (incluye margen bruto "
              "por bloque: Hospitales 61.0%, Farmacias 62.0%, Expansión 68.9%, Impulso 41.8%, Gobierno "
              "34.2%) [split FC/Servicios: VJ/Finanzas].", False)])
bullet(doc, [("Anexo B · Cartera y contratos de gobierno ", True),
             ("(soporte de la bianual con fallo 28-ago y de la cobranza; cartera junio a junio, por "
              "cliente; puente pedidos-facturación-venta neta) [DS].", False)])
bullet(doc, [("Anexo C · Sizing diálisis peritoneal y banco Hospitales: ", True),
             ("DP público por institución y delegación (deck Servicios); Muguerza (licitación 274 claves, "
              "potencial $220M), convenios PxV (32 hospitales, $9.4M/mes), oncológicos costo SAFE vs "
              "precio GASS, desaceleración de distribuidores (deck DG 29-may).", False)])
bullet(doc, [("Anexo D · Elasticidad y precio ponderado ", True),
             ("(experimentos 18-24 meses, capturas del incremento de julio) [VJ].", False)])
bullet(doc, [("Anexo E · Fuentes y universos: ", True),
             ("qué mide cada universo (sell-in, sell-out/neto, DP, NADAL, PEDIDOS de gobierno, P&L "
              "Finanzas) y por qué no se mezclan; definiciones de PIN, venta perdida (restricto vs "
              "irrestricto), fill rate, DDI; método del puente v4 (5 conceptos, Shapley, control = "
              "0).", False)])

# ------------------------------------------------------------------- tono ---
chapter(doc, "Reglas de tono transversales (checklist antes de ensamblar)")
rules = [
    "Que no parezca justificación: probar cada lámina contra esta frase",
    "Compromiso y objetivos en la primera lámina; nada de guardar el número",
    "Datos duros y fuentes de terceros (BBVA, IQVIA, Knobloch, INEFAM, CIEP, AMIS) en el entorno; adjetivos fuera",
    "Vocabulario matizado: 'se está gestando una recesión en el retail farmacéutico', nunca statements absolutos",
    "Cero 'hubiera': la simulación de servicio vive solo implícita en la base del year-to-go",
    "Radiografía en el 1S: esto estuvo bien, esto duele; lo que haremos vive en el plan 2S",
    "Sin autofelicitación: meta contra real sin aplauso; junio siempre con su asterisco (~$104M adelantados, 5 lunes)",
    "Problema-solución en cada bloque: cada villano tiene respuesta; donde no la hay, 'identificado, esto estamos haciendo'",
    "No abrir debates viejos (venderle al gobierno) ni cajas mal definidas (terapia de infusión como categoría)",
    "Positivos no forzados; el natural es Servicios",
    "Los [candidatos] no se imprimen: o se vuelven canónicos o no van; nada de confiabilidad media/baja del research sin validar",
    "Intel de canal (Nadro, Ultra, markup quimio) se dice como 'lo que nos dice el mercado', nunca con fuente inventada",
    "Los universos no se mezclan (sell-in / pedidos / sell-out / P&L): cada lámina declara el suyo",
    "Presupuesto de tiempo por bloque: esta vez sí llegamos a Servicios",
]
for i, r in enumerate(rules, start=1):
    bullet(doc, [(f"{i} · ", True), (r, False)], after=1.2)

# ------------------------------------------------------------- pendientes ---
chapter(doc, "Pendientes de datos y decisiones")
simple_table(
    doc,
    ["#", "Pendiente", "Responsable", "Para cuándo"],
    [
        ("1", "Puentes v4 de Gobierno FC, Hospitales, Servicios y consolidado PISA (col 2 de las láminas de puente)", "Equipo PVM", "Semana en curso"),
        ("2", "Venta perdida, PIN no solicitado y NC (comerciales y logísticas) formales: por segmento, 1S25 vs 1S26, definición y universo declarados (col 3)", "Rafael / FM / DS / VJ / RC", "Esta semana"),
        ("3", "Definición única de venta perdida de gobierno (342 / 443.9 / 463 / 595-600)", "DS / FM / Rafael", "Antes de lámina"),
        ("4", "PIN no solicitado de gobierno: planchar 859 vs 869 con Hugo y Daniel Torres", "DS", "16-17 jul"),
        ("5", "NC gobierno una sola cifra (428 total vs 330 devoluciones + 108 sanciones): universo y si excluye sanciones", "Dani / DS", "Semana en curso"),
        ("6", "EBITDA split Gobierno FC vs Servicios (hoy combinado 804.8 · 12.9%) o bendecir el combinado; tratamiento de Soporte -601.1", "VJ / Finanzas", "Antes del 22"),
        ("7", "Vista IQVIA del mercado hospitalario + validar el -5% (la lámina del canal venía vacía)", "CC", "Semana en curso"),
        ("8", "Burbujas: rotular valores TAC 1 año / TACC 5 años por línea (base ya existe en deck Farmacias L14-17)", "CC", "Semana en curso"),
        ("9", "Efecto mercado monetizado / corte de mercado por segmento para la col 1 (y unificar Entry Market vs foco -3.4%)", "CC / DS", "Semana en curso"),
        ("10", "Nuevos productos 1S en Gobierno, Hospitales y Servicios (Retail ya: +43.8M)", "VW", "Semana en curso"),
        ("11", "OTC vs Consumo en L14: definir el corte con la definición honesta, no el favorable (+46.1%/102.6% vs +23.7%/81%)", "Rafael + IC", "Antes del 22"),
        ("12", "Puente pedidos-facturación-venta neta de gobierno declarado (3,901 / 3,993 / 3,235 / 4,034.3)", "DS / Dani", "Antes de lámina"),
        ("13", "Frente Baxter/Vantive: respuesta 'por definir' del canal vs narrativa de defensa; dimensionar Mindray y Baxter", "Martín / CC", "Antes de ensamblar"),
        ("14", "Mercado gobierno: validación AlphaDog (+30-35% rechazado) y bullets con datos (competidores por clave, erosión, % directas)", "Chery / DS", "Semana en curso"),
        ("15", "Aclarar universo del '9% de junio' y la frase 'llegamos con volumen, no valores' (sesión IQVIA) antes de cualquier uso", "Felipe / Rafael", "Revisión"),
        ("16", "Placeholders de la L10: negados XX a YY (validar unidad), WMAPE, valor mensual del servicio recuperado", "FM / RC", "Semana en curso"),
        ("17", "Cerrar cifra de compra adelantada (~$104M) y cuantificar efecto 5 lunes de junio en Hospitales", "CC / Rafael + IC", "Antes del 22"),
        ("18", "Numerito macro único de gobierno por elegir (el % PIB salud quedó descartado por trillado); candidatos: adeudos 14k vs 5k, consolidada anulada con 50.5% de claves", "Edmundo / Rafa", "Semana en curso"),
        ("19", "Tendencias SS / Birmex / IMSS / ISSSTE / regulatorio (tendencias, no anécdotas)", "Felipe + Hugo Bobadilla", "Semana en curso"),
        ("20", "Dato preciso de volumen de plantas a gobierno (insulinas, soluciones); alinear postura con Juan Jaime", "Víctor / Dirección", "Antes del 20"),
        ("21", "Número del 2S negociado", "Heriberto / Dirección", "Antes del 20"),
        ("22", "Decisiones Rafael sobre el puente: col 3 = 1S25 vs 1S26 (confirmar); vista bruta vs reclasificada en Retail; Vista Consejo 5 líneas superseded por maquinaria v4", "Rafael", "Con el v6"),
        ("23", "Cifras finales de Servicios por modelo + storyline de Servicios (David y Dani); inversiones con bendición de Finanzas", "DS / Dani / César", "Semana en curso"),
        ("24", "Calibrar narrativa 'junio bueno / julio hipotecado' vs 98.5% sostenido; presupuesto de tiempo; pre-read ejecutivo 3pp", "Felipe / Rafa / Todos", "Revisión / al cerrar"),
        ("25", "Cuadre TI/SAFE/SIA a segmento: canal Hospitales FC 3,050 + SERV 432 = 3,482 vs segmento sell-in 3,054.5 (trazabilidad de la amenaza L22 vs el P&L L6)", "RC / IC / Martín", "Antes del 22"),
        ("26", "Puente ingreso a utilidad de los 53 centavos por peso (o bajar el rango de la afirmación); costo de caja/cartera de llegar al [96]", "VJ / Finanzas / Rafael", "Antes del 22"),
    ],
    [Inches(0.3), Inches(4.05), Inches(1.5), Inches(1.25)],
    right_from=99,
)

# -------------------------------------------------------------- calendario ---
chapter(doc, "Calendario")
bullet(doc, [("Jueves 16: ", True),
             ("esta v6 (insumos nuevos integrados) a validación de Rafael; síntesis de integración "
              "adjunta (SINTESIS_integracion_inputs_2026-07-16.md).", False)])
bullet(doc, [("Viernes 17: ", True),
             ("storyboard (revisión con Michelle según llamada del 15-jul [confirmar]); arranque con "
              "agentes en cuanto Rafael valide el v6.", False)])
bullet(doc, [("Antes del 20: ", True), ("número del 2S cerrado con Heriberto.", False)])
bullet(doc, [("Semana en curso: ", True),
             ("puentes v4 restantes, datos formales de venta perdida / PIN / NC, EBITDA split, y cierre "
              "de pendientes por responsable.", False)])
bullet(doc, [("Miércoles 22: ", True),
             ("PowerPoint con datos financieros finales a Presidencia.", False)])
bullet(doc, [("Lunes 27: ", True), ("junta de Consejo.", False)])

p = para(doc, before=8)
style_run(p.add_run("Regenerable: python3 build_storyline_v6.py · No editar el .docx a mano · "
                    "Inteligencia Comercial / Estrategia · 16 de julio de 2026"),
          size=Pt(8), color=GRAY_500)

doc.save(OUT)
print(f"OK -> {OUT}")
