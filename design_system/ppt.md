# PROFILE — PPT (presentaciones widescreen 16:9)

> Spec visual para decks PPT: Consejo de Administración, presentaciones internas formales, executive briefs. Hereda paleta de [`tokens.json`](../tokens.json). Complementa narrativa en [`BEST_PRACTICES.md`](../BEST_PRACTICES.md).

**Fuente vigente en producción:** `/Users/rafaelprince/Documents/Claude/Projects/PPT Consejo Mayo 2026/_design/DESIGN_SYSTEM_PPT.md` (refleja este perfil).

**Estilo:** Consulting Modern — IQVIA navy-grises sobre blanco.
**Formato:** PowerPoint 16:9 widescreen (13.333" × 7.5" / 12,192,000 × 6,858,000 EMU).
**Idioma:** Español (México).

---

## 1. TIPOGRAFÍA — Calibri Light (decisión consciente)

> **Bifurcación tipográfica documentada:** PPT usa **Calibri Light** (no Inter como el Tablero web). Razón: continuidad con deck madre `Plan de Acción Cierre 2026.pptx` y compatibilidad con PowerPoint sin necesidad de embed. Esta decisión está alineada en [`tokens.json`](../tokens.json) §typography.ppt.

### Familias

- **Body, títulos, charts, tablas:** Calibri Light (peso 300).
- **Énfasis bold puntual:** Calibri (peso regular/bold sin "Light"). Solo para headers de tabla, KPI grande, palabras-clave dentro del title.
- **NO** usar otras familias (ni Georgia, ni Arial, ni Inter, ni nada más).
- Stack fallback: `Calibri Light > Calibri > Arial`.

### Escala canónica

| Elemento | Familia | Tamaño | Color |
|---|---|---|---|
| **Insight title** | Calibri Light | **32 pt** | `#0F2845` (primary.900) |
| **So-what / subtitle** | Calibri Light | **14 pt** | `#44546A` (ppt_only.gris_navy) |
| Section header (interno) | Calibri (bold) | 20 pt | `#0F2845` |
| Body / tabla cell compacta | Calibri Light | 11 pt | `#3D4A5F` (gray.700) |
| Body / tabla cell cómoda | Calibri Light | 12 pt | `#3D4A5F` |
| Table header | Calibri (bold) | 11 pt | `#FFFFFF` sobre `#0F2845` |
| KPI grande (hero) | Calibri (bold) | **40 pt** | `#0F2845` |
| KPI hero único | Calibri (bold) | 54 pt | `#0F2845` |
| KPI label | Calibri Light | 10.5 pt | `#5A6679` UPPERCASE + tracking |
| Chart axis labels | Calibri Light | 10 pt | `#5A6679` |
| Chart data labels | Calibri Light | 10 pt | `#1A2332` |
| Footnote / fuente | Calibri Light | **9 pt** italic | `#8A95A8` (gray.400) |

### Reglas tipográficas

- **Una sola familia**: Calibri Light por default; Calibri (bold) solo donde el sistema lo pide.
- **Insight title** = 1 línea, ≤ 110 caracteres. Si necesitas más → revisa el título, no rompas el límite.
- **Sentence case** en títulos (no Title Case, no UPPERCASE salvo KPI labels y section headers).
- **Negritas en body**: máximo 3-4 palabras por lámina. Subraya el insight, no decora.
- **NO subrayar texto.**
- **NO ALL CAPS** en body (solo KPI labels y section headers).
- **Tabular figures** en celdas numéricas: Format → Font → OpenType → Tabular figures.

### Reglas de números

- Alinear a la **derecha** en tablas.
- Mismos decimales por columna (todos 1 o todos 0).
- Separador miles `,` y decimales `.` (formato MX/US estándar internacional para Consejo).
- Símbolo `$` solo en primera fila de columna o al primer KPI; resto sin repetir.

---

## 2. PALETA

Generar desde [`tokens.json`](../tokens.json) con `python generators/tokens_to_python.py`. Ver ahí los hex exactos.

### Navy (primarios PPT)

| Token | Hex | Uso |
|---|---|---|
| `primary.900` | `#0F2845` | Color brand. Títulos, headers tabla, banners, axis primary |
| `ppt_only.navy_deep` | `#002060` | KPIs principales, accents fuertes (PPT-only, heredado deck madre) |
| `primary.700` | `#0F4C81` | KPIs activos, segunda serie de chart |
| `ppt_only.gris_navy` | `#44546A` | Subtítulos so-what, texto secundario (PPT-only) |
| `gray.700` | `#3D4A5F` | Body text en tablas y bullets |

### Grises

| Token | Hex | Uso |
|---|---|---|
| `gray.900` | `#1A2332` | Texto principal |
| `gray.500` | `#5A6679` | Labels, eyebrow, ejes de chart |
| `gray.400` | `#8A95A8` | Placeholders, **fuentes al pie** |
| `gray.300` | `#C5CDD9` | Bordes prominentes, connectors waterfall |
| `gray.200` | `#E5E9EE` | Bordes sutiles, gridlines |
| `gray.100` | `#F0F3F7` | Fila alterna tabla, fondos tenues, total row |
| `white` | `#FFFFFF` | Surface / fondo slide |

### Semáforos (uso quirúrgico — solo deltas)

| Token | Hex | Uso |
|---|---|---|
| `success.500` | `#2E7D4F` | Texto delta positivo |
| `success.100` | `#D4EDDA` | Fondo badge positivo |
| `warning.500` | `#C97A2B` | Texto delta intermedio |
| `warning.100` | `#FCEBD5` | Fondo badge ámbar |
| `danger_ppt` | `#C00000` | Texto delta negativo (PPT). Más saturado que `danger.500` web (#B23A3A); compat con deck madre |
| `danger.100` | `#F5D5D5` | Fondo badge rojo |

**Reglas:**
- Cualquier delta numérico se colorea por semáforo, **nunca decorativamente**.
- El semáforo es para magnitud cuantitativa, NO para "este tema es serio".
- Si el valor es plano (0% o ±0.1%), neutralizar en `gray.700`.

---

## 3. LAYOUT — Anatomía estándar de slide (16:9)

```
┌──────────────────────────────────────────────────────────────────────┐
│  INSIGHT TITLE  (Calibri Light 32pt, color #0F2845)                  │
│  So-what subtitle (Calibri Light 14pt italic, color #44546A)         │
│  ─────── (línea 0.5pt #E5E9EE, separador opcional) ───────           │
│                                                                       │
│                                                                       │
│                   ZONA DE BODY                                        │
│                                                                       │
│             Chart, tabla, KPIs, layout multi-columna                  │
│             Padding interno mínimo 0.2" entre elementos               │
│                                                                       │
│                                                                       │
│  ─────── (línea 0.5pt #E5E9EE) ───────                                │
│  Fuente: ...  (Calibri Light 9pt italic, color #8A95A8)               │
│                                            PiSA Confidencial  |  12   │
└──────────────────────────────────────────────────────────────────────┘
```

### Márgenes y safe area

| Margen | Tamaño |
|---|---|
| Izquierda / Derecha | 0.40" |
| Arriba | 0.30" |
| Abajo | 0.30" |
| Gutter entre columnas | 0.15" |
| Padding interno boxes/cards | 0.20" |
| Espacio entre title y body | 0.30" |
| Espacio entre body y footer | 0.20" |

### Anatomía obligatoria

1. **Insight title** (línea 1) — afirmación con verbo y dato. (Ver `BEST_PRACTICES.md` §3.)
2. **So-what subtitle** (línea 2) — qué hacer / contexto / implicación. (Ver `BEST_PRACTICES.md` §4.)
3. **Body** — chart/tabla/visual que **prueba** el insight.
4. **Footer** — fuente + confidencial + page #.

Excepciones: portada, divider de sección, slide de agradecimiento.

---

## 4. LAYOUTS MAESTROS (11 layouts en Slide Master del .pptx)

| # | Layout | Uso típico |
|---|---|---|
| L01 | **Portada** | Título del deck, fecha, presentador, logo (ver §10) |
| L02 | **Divider sección** | Fondo navy pleno, número + título sección (ver §11) |
| L03 | **Insight + 1 chart** | 60% de las láminas |
| L04 | **Insight + 2 charts lado a lado** | Comparativos / antes-después |
| L05 | **Insight + tabla full-width** | Detalle granular |
| L06 | **Insight + KPI row (3-4 KPIs) + chart** | Resúmenes ejecutivos |
| L07 | **Insight + texto narrativo 2 columnas** | Lecturas estratégicas |
| L08 | **Insight + matriz / quadrant** | Posicionamiento, prioritización |
| L09 | **Quote slide** | Citas literales (cadenas, transcripts) |
| L10 | **Plan de acción / semáforo** | Iniciativas con dueño + fecha + estatus |
| L11 | **Anexo** | Marca de agua "ANEXO" arriba derecha |

Definir UNA vez en Slide Master. Cada lámina nueva se inserta desde aquí.

---

## 5. CHARTS — Especificación

### Paleta de chart (orden)

1. `#0F2845` (primary.900) — serie principal
2. `#0F4C81` (primary.700) — segunda serie / comparativo
3. `#8A95A8` (gray.400) — tercera serie / benchmark
4. `#C00000` (danger_ppt) — delta o serie negativa **solo si aplica**
5. `#2E7D4F` (success.500) — delta positivo **solo si aplica**

### Reglas

- **Eje Y empieza en 0** salvo justificación explícita.
- **Ejes**: color `#5A6679`, labels Calibri Light 10pt.
- **Gridlines**: solo horizontales si indispensable; `#E5E9EE` 0.5pt.
- **Sin leyenda flotante** cuando se pueda etiquetar series directamente.
- **Data labels**: Calibri Light 10pt sobre/junto a las barras.
- **Sin sombras 3D, sin biselados, sin gradientes**.

### Tipos preferidos por mensaje

| Mensaje | Chart |
|---|---|
| Evolución temporal | Línea |
| Comparar categorías | Barras horizontales si labels largos |
| Cumplimiento vs meta | Barras + línea meta |
| Composición % | Barra apilada 100% (no pie salvo 2-3 slices) |
| Variance / decomposition | **Waterfall** |
| Pareto / 80-20 | Pareto (barras + línea acumulada) |
| Posicionamiento | Scatter con cuadrantes |

### Waterfall específico

- Barras start/end: navy `#0F2845`
- Delta positivo: verde `#2E7D4F`
- Delta negativo: rojo `#C00000`
- Líneas connector: gris `#C5CDD9` 0.5pt punteadas

### Prohibido

- ❌ Pie charts con 4+ slices
- ❌ Donuts decorativos / speedometers
- ❌ 3D anything, biselados, sombras infladas
- ❌ Más de 4 series en una línea/columna
- ❌ Eje Y dual sin justificación
- ❌ Charts sin fuente

---

## 6. TABLAS

### Estructura

- **Header**: fondo `#0F2845`, texto blanco **bold 11pt**, alineado center si numérico / left si texto.
- **Body**: filas alternas blanco / `#F0F3F7`.
- **Border inferior** de cada fila: 1px `#E5E9EE`.
- **Total row**: fondo `#F0F3F7`, border-top 2px `#0F2845`, texto bold.
- **Border interno** entre celdas: ninguno (relying on row striping).
- **Border externo** de la tabla: 0.5pt `#C5CDD9`.

### Reglas numéricas

- Números a la **derecha**, texto a la izquierda.
- Decimales consistentes por columna.
- Símbolo `$` solo en primera fila o no usarlo si el header lo declara.
- Deltas: signo explícito `+` o `–`, color semáforo.
- Tabular figures activos.

### Tamaño máximo en main deck

- **8 filas × 6 columnas** visibles. Si excede → mover detalle a anexo, mostrar resumen.

---

## 7. KPI CARDS

```
┌────────────────────────────────┐
│ VENTA NETA ABR 26              │ ← KPI label: Calibri Light 10.5pt #5A6679 UPPERCASE
│                                │
│ $1,847 MDP                     │ ← KPI value: Calibri 40pt bold #0F2845 (tabular)
│                                │
│ ▲ +5.2% YoY                    │ ← delta: Calibri Light 14pt bold con color semáforo
│ vs Abr 25 $1,757 MDP           │ ← context: Calibri Light 10pt #5A6679
└────────────────────────────────┘
```

### Reglas

- Padding interno **0.20"**.
- **Una sola técnica de separación**: border 0.5pt `#E5E9EE` **o** fondo `#F0F3F7`. NO ambos.
- **Flecha unicode** delta: `▲` positivo / `▼` negativo / `▬` plano.
- **KPI hero** (único y grande): valor a 54pt.
- KPIs en row de 3-4 máximo.

---

## 8. ICONOGRAFÍA

- **Cero iconos decorativos.**
- Permitidos: flechas direccionales, check/cross para semáforos de cumplimiento.
- **Estilo:** outline 1.5pt, color `#5A6679` o `#0F2845`. Nunca filled colorful.
- Tamaño estándar: 20×20 o 24×24 px.

---

## 9. BORDES Y BLOQUES

- **Prohibido `border-left`** en bloques o callouts.
- **Top border permitido** (1-2 pt sólido en `#0F4C81` o `accent.gold`) para destacar bloques o secciones.
- Esquinas con border-radius 4-8 px según jerarquía.
- Sombras sutiles solamente.

### Caja de Insight (al pie de lámina analítica)

Bloque con la implicación de negocio + acción recomendada en 1-2 oraciones. Fondo `gray.050` con top border 2pt en `primary.700`. Sin border-left. Permite usar gold en una palabra clave si es la cifra/concepto pivotal.

---

## 10. PORTADA — Especificación L01

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   [Logo PiSA, alineado izquierda, alto 0.7"]               │
│                                                            │
│   CONSEJO DE ADMINISTRACIÓN                                │
│   Calibri Light 14pt UPPERCASE tracking +100 color #44546A │
│                                                            │
│   Avances Cierre 2026 · Resultados Abril                   │
│   Calibri Light 40pt color #0F2845                         │
│                                                            │
│   Estrategia y Crecimiento Comercial                       │
│   Calibri Light 18pt color #44546A                         │
│                                                            │
│   ─── (línea 1pt #0F2845, ancho 2") ───                    │
│                                                            │
│   Mayo 2026 · Rafael Prince                                │
│   Calibri Light 12pt color #5A6679                         │
│                                                            │
│   [banda inferior 0.3" alto color #0F2845]                 │
└────────────────────────────────────────────────────────────┘
```

---

## 11. DIVIDER DE SECCIÓN — Especificación L02

Fondo pleno `#0F2845`.

```
┌────────────────────────────────────────────────────────────┐
│  [fondo pleno #0F2845]                                     │
│                                                            │
│   02                                                       │
│   Calibri 120pt bold color #FFFFFF (numerador grande)      │
│                                                            │
│   VISITA MÉDICA                                            │
│   Calibri 36pt bold UPPERCASE color #FFFFFF                │
│                                                            │
│   ─── (línea 1.5pt #FFFFFF, ancho 1.5") ───                │
│                                                            │
│   "Cita o quote bajo el título"                            │
│   Calibri Light 16pt italic color #FFFFFF                  │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 12. FOOTER UNIFORME

Toda lámina de contenido (no portada, no divider):

```
─── (línea 0.5pt #E5E9EE) ───
Fuente: IQVIA Knobloch MAT26 · SAP P12 · Análisis interno    PiSA Confidencial  |  12
```

- Fuente: Calibri Light **9pt italic** color `#8A95A8`, alineado izquierda.
- Confidencial + page #: Calibri Light 9pt color `#8A95A8`, alineado derecha.

---

## 13. IMPLEMENTACIÓN python-pptx

Snippet base para builders Python:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE

# Importar paleta generada
from palette_pisa import PALETTE  # genera con generators/tokens_to_python.py

prs = Presentation()
prs.slide_width = Inches(13.333333)
prs.slide_height = Inches(7.5)

# Helper estándar
def add_text(slide, x, y, w, h, text, size=12,
             color=PALETTE["gray"]["900"], bold=False, italic=False,
             align=PP_ALIGN.LEFT, font="Calibri Light"):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = str(text)
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return box
```

Ver referencia completa en `outputs/corne-ficha/build_corne_pptx.py` (helpers `add_text`, `add_rect`, `add_metric_card`, `add_footer`, `add_header`).

---

## 14. CONSISTENCIA — Reglas de cierre

- **Página numerada** en TODA lámina excepto portada.
- **Confidencialidad** ("PiSA Confidencial") en TODA lámina de contenido.
- **Fuente citada** en TODA lámina con dato cuantitativo.
- **Misma unidad** en una serie (no mezclar MDP con MUSD).
- **Misma escala** en charts comparables.
- **Formato fecha** consistente ("Abril 2026" o "Abr 26", no mezclar).
- **Glosario** de jerga (PDM, MAT, BRICS, Mercado de Actuación) en anexo si aplica.

---

## 15. CHECKLIST DE CALIDAD (cada lámina)

- [ ] Slide 16:9 (13.333" × 7.5")
- [ ] Insight title en 1 línea ≤ 110 caracteres, acción + dato + implicación
- [ ] So-what subtitle 14pt gris bajo el title
- [ ] Calibri Light en todo (Calibri bold solo en énfasis puntual + headers)
- [ ] Paleta restringida a tokens listados
- [ ] Cero emojis
- [ ] Números: separador `,` miles, `.` decimal, alineados derecha
- [ ] Fuente al pie en 9pt italic gris `#8A95A8`
- [ ] Si tabla: header navy + texto blanco bold
- [ ] Si chart: paleta navy primaria, semáforos solo en deltas
- [ ] TODA cifra verificada contra data fuente
- [ ] Page # + "PiSA Confidencial" en footer

---

## 16. DON'TS PPT

- ❌ **Emojis** en cualquier lugar
- ❌ **Gradientes** en chart o background
- ❌ **Negro puro `#000000`** — usar `#1A2332`
- ❌ **Blanco puro** como elemento decorativo — sí como fondo
- ❌ **Fonts adicionales** más allá de Calibri / Calibri Light
- ❌ **Sombras infladas** — usar borde 1px `#E5E9EE` para separación
- ❌ **Iconos saturados** — solo gris `#5A6679` o navy `#0F2845`
- ❌ **3D, biselados**, animaciones, transiciones
- ❌ **Pie charts con 4+ slices**
- ❌ **Eje Y dual** sin justificación
- ❌ **Stock photos genéricas**
- ❌ **Títulos descriptivos** — siempre insight + so-what
- ❌ **Bullets de 5+ niveles**
- ❌ **>7 bullets por lámina**
- ❌ **Tablas >8×6** visibles
- ❌ **Charts sin fuente**
- ❌ **"Boquete"** como término — usar **"Gap"**
- ❌ Más de **1 elemento gold** por slide
- ❌ Frase literal **"So What"** como label
