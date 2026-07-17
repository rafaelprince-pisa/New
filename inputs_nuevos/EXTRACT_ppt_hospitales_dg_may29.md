# EXTRACT — "20260529 PPT Hospitales DG.pptx"

> **Archivo fuente:** `/Users/rafaelprince/Downloads/20260529 PPT Hospitales DG.pptx` (md5 `3db83eab3972bf333a7c0159ebc4cbb4`, 20 láminas, 16:9).
> **Qué es:** deck de la División **Hospitales Privados (HP)** presentado a **Dirección General** el **29-may-2026**. Autor rotulado en portada: **Inteligencia Comercial, Mayo 2026**. Ventana de datos declarada en portada: **Enero–Abril 2026** (YTD a abril, 4 meses). Banco de láminas / contexto histórico para el Consejo del 27-jul.
> **Método de extracción:** texto/tablas/series de gráfica nativas vía python-pptx (incluye shapes agrupados, tablas celda a celda y speaker notes); render visual vía LibreOffice→PDF→PNG a 150 dpi leído lámina por lámina. Las series de gráfica se leyeron del XML nativo; los tamaños de burbuja y ejes de la L6 se leyeron del texto del PDF y del PNG.
>
> **ADVERTENCIA DE PROCESO (leer antes de usar):** durante la extracción, un proceso concurrente en la misma máquina estaba modificando otros archivos del Consejo en `~/Downloads` (`Presentacion RP HP_Consejo_Hospitales.pptx`, `Consejo Farmacias.pptx`, `CONSEJO 27 DE JULIO_Servicios.pptx`, todos con timestamp 16-jul 09:07–09:12) y llegó a alterar mi script y a contaminar una primera tanda de PNG. **Todo lo que sigue proviene EXCLUSIVAMENTE del archivo DG verificado por checksum.** En particular, cualquier lámina tipo "Cascada Hospitales 1S-26 vs Meta 26", "Acumulado $3,482", bocadillos por Región (Reg. A/B/C/D), "Venta Neta 2026 / Precio / Volumen / Descuentos" o "Pisa HP vs Mercado | VDM IQVIA" **NO pertenece a este deck DG** — pertenece al otro archivo (`Presentacion RP HP_Consejo_Hospitales.pptx`) y no se incluye aquí.

---

## Mapa del deck (estructura)

| # | Título / rol | Tipo |
|---|---|---|
| 1 | Portada "Hospitales Privados" | Portada |
| 2 | Agenda (3 secciones) | Índice |
| 3 | Panorama HP — nota de prensa aseguradoras vs hospitales | Texto |
| 4 | Panorama HP — build 1/4 (frente 01) | Bloques numerados |
| 5 | Panorama HP — build 2/4 (frentes 01–02) | Bloques numerados |
| 6 | Bubble: negocio equipos de bomba +600MDP / amenaza Mindray | Gráfica burbuja |
| 7 | Riesgo por incremento de precio | Tabla |
| 8 | Panorama HP — build 3/4 (frentes 01–03) | Bloques numerados |
| 9 | Panorama HP — oncológicos Costo SAFE vs Precio GASS | Tabla |
| 10 | Panorama HP — build 4/4 (frentes 01–04) | Bloques numerados |
| 11 | 4 Frentes Prioritarios de Ejecución | 4 columnas |
| 12 | 4 Frentes — Parrillas dinámicas primera fase | Tablas |
| 13 | Desempeño HP 2026 YTD (Total HP mensual + anual) | Gráficas + tabla |
| 14 | Desempeño HP YTD. FC — Total HP + Frasco Cerrado + puntos a favor/dolor | Gráficas + texto |
| 15 | Desempeño HP YTD. FC — G. Muguerza + retos | Gráfica + texto |
| 16 | Seguimiento Muguerza (captura Power BI) | Imagen dashboard |
| 17 | Desempeño HP YTD. FC — G. AUNA + retos | Gráfica + texto |
| 18 | Desempeño HP YTD. FC — Negociaciones P×V | Tabla + texto |
| 19 | Desempeño HP YTD. FC — G. Ángeles + retos | Gráfica + texto |
| 20 | Desaceleración venta distribuidor — Distribuidores | Tablas + texto |

Nota de plantilla: a la izquierda de las láminas 13–20 se repite **idéntica** la gráfica "Total HP" (mensual Ene–Abr) con su tabla resumen (Alc. Meta / GAP vs Meta / Crec. $). Es un panel-ancla fijo; sus valores se listan una sola vez en la L13 y se marcan como reutilizados.

---

## LÁMINA 1 — Portada
- Título: **"Hospitales Privados"**
- Subtítulo: **"Enero -Abril 2026"**
- Pie: **"Inteligencia Comercial"** / **"Mayo 2026"**
- Branding del footer (visible en L2): logo PiSA Farmacéutica + **"FARMA MX 25"**.

## LÁMINA 2 — Agenda
- Título: **"Agenda"**
- **1.0 Panorama Hospitales Privados**
- **2.0 Frentes de Ejecución**
- **3.0 Desempeño HP YTD**

## LÁMINA 3 — Panorama HP: nota de prensa
- Título de sección: **"Panorama Hospitales Privados"**
- Encabezado de nota: **"La relación rota entre aseguradoras y hospitales: un sistema bajo presión"** — fuente citada: **"El economista, 10 de mayo 2026"**.
- Cuerpo (verbatim, 4 párrafos):
  1. "Las aseguradoras pagan directamente el **80-85% de los siniestros de gastos médicos mayores (GMM)**, pero desde hace rato ya no controlan el costo: el hospital factura lo que considera necesario y la aseguradora paga. (el antes)"
  2. "Este modelo convirtió a los hospitales en quienes definen el precio del siniestro. Mientras tanto, la **inflación médica alcanza ya 14.8% en 2026 —la más alta del mundo—, más del cuádruple de la inflación general**. Los costos hospitalarios, honorarios y medicamentos suben sin freno"
  3. "El último golpe es el **cambio fiscal del IVA**. Desde la **Ley de Ingresos 2026**, las aseguradoras ya no pueden acreditar el IVA que pagan en los pagos directos a hospitales. **Ese 16% se convirtió en costo definitivo.** los ajustes en GMM **superan el 20-35% en muchas pólizas, y en adultos mayores pueden llegar al 40%**."
  4. "Frente al doble apretón —fiscal y hospitalario—, las aseguradoras ya están tomando medidas concretas, en principio **renegociar los convenios con hospitales**. Lo que se ve venir es el fin de esa etapa de esplendor de hospitales, donde había coberturas ilimitadas y los hospitales cobraban lo que querían; tendrá ahora que haber mucha vigilancia y control… y del lado de los hospitales también ofrecer **paquetes transparentes realistas y aterrizados**."

> Nota: en el render, esta lámina aparece con encabezado gris **"Intervención de aseguradoras:"** y so-what **"Inflación médica y cambios fiscales fuerzan una reestructuración del ecosistema de salud privada."**, con caja de bullets: *Inflación Desbordada* (14.8% médica 2026, cuadruplica la general), *Impacto Fiscal Severo* (IVA 16% no acreditable Ley 2026, encarece pólizas hasta 40%), *Pérdida de Control* (hospital dictaba precios; aseguradoras cubren 80-85% del costo y ya no sostienen el esquema). Fuente al pie: **"Análisis de Mercado, El Economista (10 de mayo, 2026)"**.

## LÁMINAS 4 / 5 / 8 / 10 — Panorama HP: los 4 frentes de amenaza (build progresivo)
Mismo título de sección **"Panorama Hospitales Privados"**. Cuatro bloques numerados que se revelan acumulativamente: **L4 = solo 01**, **L5 = 01+02**, **L8 = 01+02+03**, **L10 = 01+02+03+04**. Contenido consolidado (texto verbatim; hay variantes menores de redacción entre L4 y L8 en el bloque 01, se anotan):

- **01. Modelos agresivos de adquisiciones.**
  - Variante L4/L5: *GASS* "Si encuentro más barato te cambio, tengo que bajar costos". *SM* "Me enteré que compra más barato mi competencia, te voy a pedir el mismo GAS y HSAI".
  - Variante L8/L10: "Si encuentro más barato te cambio, tengo que bajar costos" **GAS** / "Me enteré que compra más barato mi competencia" **SM**.
- **02. Entorno Competitivo.** "La presión por bajar costos los obliga a buscar opciones. **Mindray, Baxter, Kener, Vitalis, Fresenius, Innovadores\***".
- **03. Percepción de valor / Serv. Integrales.** "Existen opciones en región centro de mezclas oncológicas (**COI, ATRYS**), **Kener Anestesia**".
- **04. Efectividad de FdV.** "Amplios tramos de control, gestión administrativa (ej. refacturaciones y seguimiento pedidos), portafolio / parrillas con muchos productos – pérdida de enfoque".

## LÁMINA 6 — Bubble: negocio de equipos de bomba y amenaza Mindray
- Título superior: **"El negocio de equipos de bomba tiene un valor de +600MDP anual"**.
- Banner inferior (insight): **"La ejecución se ve afectada en Hospitales por ofertas agresivas de Mindray desde $110.00"**.
- Callout: **"200 clientes compran por arriba de $200.00"**.
- **Tipo:** gráfica de burbuja. **Eje Y = Precio** (escala $100 → $240, marcas cada $20). **Eje X = Unidades** (0 → 200,000, marcas cada 20,000). Tamaño de burbuja = valor de venta ($).
- **Líneas de referencia:** línea roja punteada en **$110 – 121** rotulada **"MINDRAY (Muguerza, Angeles, AZURA, hospitaria, Ginequito, )"** (piso de precio Mindray); línea verde punteada en ~**$227** rotulada **"ZMIN $227"**.
- **Burbujas rotuladas con cliente:** Grpo. Angeles (burbuja mayor, esquina superior-derecha ~170k unidades, ~$227), STAR MEDICA (~80k unidades, ~$150), MUGUERZA (~40k unidades, ~$180), UANL, San Javier, Sinergia, Promotora Poblana (grupo denso a la izquierda con precio alto y pocas unidades).
- **Tamaños de burbuja legibles (valor $ de venta), 10 rotulados:** $37,027,860 (Grpo. Angeles, junto a "ZMIN $227"); $13,193,350 (Star Medica); $6,995,738 (Muguerza); $4,075,651; $3,302,925; $2,944,938; $2,222,130; $1,947,585; $1,449,304 (Promotora Poblana); $1,299,642.
- **Serie completa de precios (Eje Y) de las 18 burbujas, del XML** ($/unidad): 216.3, 152.9, 173.7, 152.1, 206.4, 189.9, 162.5, 151.2, 113.5, 223.1, 229.5, 220.7, 174.6, 127.1, 227.2, 230.5, 225.5, 204.8.
- Otros textos: **"Precio"** (rótulo eje Y), **"Unidades"** (rótulo eje X). Speaker notes: ninguna.

## LÁMINA 7 — Riesgo por incremento de precio
- Título: **"Riesgo por incremento de precio"**.
- Banner inferior (insight): **"El precio sería impuesto y no acordado, el cliente tomará medidas de castigo a la cuenta con el resto de productos"**.
- Tabla (Marca | Incremento propuesto | Benchmark competitivo):

| Marca | Incremento | Referencia competitiva |
|---|---|---|
| SOLUCIONES | 3% – 9% | BAXTER $17 vs $25 PiSA (**-35%**) |
| DISP. MÉDIC. | 3% – 8% | Mindray (Eq. Inf) $110 (**-50%**) |
| FENODID | 10% | PSICOFARMA $650 vs $1,000 PiSA (**-35%**) |
| BOLENTAX | 10% | SANOFI 40mg $280–$400 vs PiSA $420 (GAS) |
| RELACUM | 6% | Somoncal Kener $165 vs $270–340 PiSA |
| KRUNAMINA | 6% | KENER $1,000 vs $2,232 PiSA (**-60%**) |
| ROPICONEST | 6% | Alvartis $300 (MAC) vs $750–$890 PiSA |

- **Speaker notes (verbatim):** "ABC 25 / SM 24.60 / Christus 23 / G. Ángeles 21 / Español 24.10 / MAC / AZURA" (parecen precios/índices de referencia por cuenta; sin unidad declarada).

## LÁMINA 9 — Panorama HP: oncológicos, Costo SAFE vs Precio GASS
- Título de sección: **"Panorama Hospitales Privados"**.
- Banner inferior (insight): **"20 MDP GAP vs Meta CORP, Angeles principal caída"**.
- Tabla (Molécula | Laboratorio | Costo SAFE $ | Precio GASS $ | Diff Precio):

| Molécula | Laboratorio | Costo SAFE | Precio GASS | Diff |
|---|---|---:|---:|---:|
| RITUXIMAB | ROCHE | 50,376 | 51,300 | 2% |
| PEMBROLIZUMAB | MSD | 96,385 | 91,139 | -5% |
| OCRELIZUMAB | ROCHE | 200,275 | 190,000 | -5% |
| BEVACIZUMAB | ROCHE | 51,030 | 49,400 | -3% |
| INMUNOGLOBULINA | CSL BEHRING | 16,345 | 15,002 | -8% |
| DARATUMUMAB | JANSSEN | 120,375 | 113,050 | -6% |
| ATEZOLIZUMAB | ROCHE | 123,028 | 114,950 | -7% |
| TRASTUZUMAB | ROCHE | 55,183 | 53,797 | -3% |
| DARATUMUMAB | JANSSEN | 38,507 | 35,921 | -7% |
| PERTUZUMAB | ROCHE | 88,782 | 86,051 | -3% |
| IPILIMUMAB | BRISTOL | 68,007 | 81,700 | 20% |
| NIVOLUMAB | BRISTOL | 14,733 | 17,404 | 18% |
| INFLIXIMAB | JANSSEN | 19,215 | 18,953 | -1% |
| TRASTUZUMAB EMTANSINA | ROCHE | 49,151 | 42,750 | -13% |
| BEVACIZUMAB | ROCHE | 14,045 | 12,350 | -12% |

(Lectura: "Diff Precio" = Precio GASS vs Costo SAFE; la mayoría negativos = PiSA/GASS vende por debajo del costo SAFE de referencia salvo Rituximab, Ipilimumab, Nivolumab.)

## LÁMINA 11 — 4 Frentes Prioritarios de Ejecución
Título: **"4 Frentes Prioritarios de Ejecución"**. Cuatro columnas:

- **01 · Defender y crecer en medicamentos.** Convenios por volumen con grupos clave (**Azura, Polar, San José, CM, Country**). Listados de consumo + propuestas integrales de portafolio.
- **02 · Blindar Terapia de infusión.** Cambio de Tecnología (**Muguerza, Hospitaria, Auna, GASS?**). Proyecto de Conectividad. Campaña "Servicio de Infusión": Calidad de Sets, Congreso Enfermería, Cursos Hospitales/PiSA. Cambio de Rol: "Promotor TF" → "Consultor TF".
- **03 · Renovar / Recuperar Servicios Integrales.** Negociaciones con Corporativos (**TecSalud, Star Medica**). Centros de infusión compiten con hospitales en oncología. Co-inversión hospital + PiSA; **Qx Inteligente VCZ**. Almacén PiSA/Hospital (Caso Nadro) — **Español, Medica Sur, Muguerza**.
- **04 · Reorganización Comercial.** Generación de demanda (Enfermería / Medicamentos / Servicios hospitalarios). Parrillas dinámicas por hospital: "lo que el hospital necesita", 3 parrillas base, 8–10 productos máx. % Ponderación de productos, **NP (nuevos productos) con mayor peso**.

## LÁMINA 12 — 4 Frentes: Parrillas dinámicas (primera fase)
Título: **"4 Frentes Prioritarios de Ejecución / Parrillas dinámicas – primera fase"**.
- **Parrillas actuales medicamentos:**
  - **QX-40** (columna): BENSITRAK, CIRCUITOS, FLOVES, HOMEPUMP, KRUNAMINA, LUFCUREN, ONEMER DT, RECOFOL QX, ROPICONEST, VINALTRO.
  - **HS–UTI-48** (dos columnas): BOLENTAX, CUSTODIOL, FLUCOXAN INY, FLUONING, FUCEROX, IMATION, LIBONIDE, PIPTABAC, PISARPEK, **PIXIBA** (destacado verde), PIXIRIV, PLAUTIS | **PRAGMA** (verde), SALPIFAR, SUPACID INY, VINZA, ARZOMEBA, LEZOPISA, MALIPAFED, PISAPEM, RECOFOL UT, RELACUM UT, SUVEPUR.
- **EJEMPLO parrillas dinámicas** (3 perfiles, tope 8-10 SKU; PIXIBA y PRAGMA destacados verde en las 3):
  - **MED A:** PIXIBA, PRAGMA, SALPIFAR, VINALTRO, FLUCOXAN, FLUONING, LEZOPISA, PISAPEM, PIPTABAC.
  - **MED B:** PIXIBA, PRAGMA, VINALTRO, FLOVES, KRUNAMINA, RECOFOL, RELACUM, SUVEPUR, CIRCUITOS.
  - **MED C:** PIXIBA, PRAGMA, SALPIFAR, SUPACID INY, VINZA, ARZOMEBA, PISARPEK, SUPACID INY, MALIPAFED.
- Nota al pie: "**Se agregarán parrillas de acuerdo a la necesidad de cada hospital (perfiles hospitalarios)**".

## LÁMINA 13 — Desempeño HP 2026 YTD (Total HP)
Título: **"Desempeño HP 2026 YTD"**. (Ventana Ene–Abr 2026; unidades en $MDP.)

- **Gráfica de columnas agrupadas mensual (Total HP), Ene–Abr.** Series: **25** (gris), **26** (navy), **Meta** (rombo verde). Data labels y series (del XML, $MDP):

| Mes | 2025 | 2026 | Meta | Var 26 vs 25 (rótulo) |
|---|---:|---:|---:|---:|
| Enero | $476 (476.05) | $506 (505.63) | 523.79 | **6%** |
| Febrero | $436 (435.85) | $485 (485.00) | 520.47 | **11%** |
| Marzo | $498 (497.83) | $546 (545.65) | 543.26 | **10%** |
| Abril | $513 (512.73) | $486 (486.14) | 556.50 | **-5%** |

- **Tabla resumen Total HP (mensual):** Alc. Meta **96.6% / 93.9% / 98.3% / 91.3%**; GAP vs Meta **-$14.8 / -$26.8 / -$8.1 / -$40.6**; Crec. ($) **+$0.5 / +$38.9 / +$42.5 / -$20.9**.
- **Bloque anual Total HP (columnas apiladas, 2 años):** 2025 = **$1,922** (1,922,463,294.58) · 2026 = **$2,022** (2,022,425,155.48) · crecimiento **+5%**.
- **Tabla resumen anual Total HP:** Alc. Meta **94.3%**; GAP vs Meta **-$121.6** (impreso "**-$-121.6**", doble signo, ver Inconsistencias); Crec. ($) **+$99.9**.

## LÁMINA 14 — Desempeño HP YTD. FC (Total HP + Frasco Cerrado)
Título: **"Desempeño HP 2026 YTD. FC"**. Panel izquierdo = **Total HP** idéntico a L13 (mismos $476/$506… y misma tabla resumen 96.6/93.9/98.3/91.3, GAP -14.8/-26.8/-8.1/-40.6, Crec +0.5/+38.9/+42.5/-20.9). Panel derecho = **Frasco Cerrado**:

- **Gráfica columnas agrupadas mensual (Frasco Cerrado), Ene–Abr** — series (XML, $MDP):

| Mes | 2025 | 2026 | Meta | Var (rótulo) |
|---|---:|---:|---:|---:|
| Enero | $421 (420.82) | $421 (421.30) | 436.09 | **0%** |
| Febrero | $376 (375.79) | $415 (414.71) | 441.49 | **10%** |
| Marzo | $434 (434.43) | $477 (476.89) | 485.02 | **10%** |
| Abril | $445 (444.86) | $424 (423.94) | 464.56 | **-5%** |

- **Puntos a favor:** 1. **G. Muguerza** +$18.3MDP (107%); 2. **H. OCA** +$8.1MDP (109%); 3. **T. Infusión** +$36.9MDP (97.8%).
- **Puntos de dolor:** 1. **G. Ángeles** -$8.2MDP (91%); 2. **Canal Dist.** -$18.8MDP (73%); 3. **Hospitalización** -$18.8MDP (73%).

## LÁMINA 15 — Desempeño HP YTD. FC — G. Muguerza
Título: **"Desempeño HP 2026 YTD. FC"**. Panel izq = Total HP (repetido). Panel der = **G. Muguerza**:

- **Gráfica mensual G. Muguerza, Ene–Abr** — series (XML, $MDP):

| Mes | 2025 | 2026 | Meta | Var (rótulo) |
|---|---:|---:|---:|---:|
| Enero | $25 (24.68) | $29 (28.76) | 25.54 | **17%** |
| Febrero | $19 (18.65) | $31 (31.37) | 27.72 | **68%** |
| Marzo | $30 (29.70) | $30 (30.18) | 29.35 | **2%** |
| Abril | $28 (27.74) | $29 (28.77) | 28.77 | **4%** |

- **Retos Futuros (texto):**
  1. **Licitación 2026:** De **Abril 2026 a Marzo 2027** corre su licitación de medicamentos. Ganamos la asignación de **274 claves** con potencial para el cliente **$220MDP** (hoy nuestra facturación es de **$175MDP**). Necesitamos empujar la prescripción médica en los **15 hospitales** el primer año.
  2. **Cambio de tecnología:** El negocio de infusión (Eq. BI) con el cliente tiene un **V.E.A. de $40MDP (2025)**. Mindray ofertó consumibles a **$107** mientras la oferta PiSA es de **$180 (+54%)**. Se negoció un precio de **$127** para blindar el segmento. Impacto esperado de **-$1.6MDP/mes**.

## LÁMINA 16 — Seguimiento Muguerza (captura Power BI)
Título: **"Seguimiento Muguerza"**. Imagen de dashboard Power BI **"SEGUIMIENTO DE CONVENIOS HP 26"**. KPIs y tabla legibles:
- **Hospital: 15** · **Skus: 274** · **AH: 8**.
- **VENTA 26: $26,289,506**.
- **100% CONVENIO: $139,670,292**.
- **Beneficio Esperado: $13,486,854**.
- **ALCANCE NEGOCIACIÓN: 19%** (donut).
- Filtros visibles: Mes {4,5,6,7,8,9,10,11,12}, Gpo {Amerimed, Azura, Muguerza, Polar, Real San Jo…}, Región {A}. Gráfica "MENSUAL PZAS" (VTA PZA vs OBJETIVO).
- Panel "GAE" (lista de moléculas): ABEFEN, ADENOSINA, AGRIFEN, AGUA INYECT…, AGUA P/IRRI…, ALEGORIA, ALNEX, AMFOTERICINA, AMK, AMOFILIN, AMOXICLAV, ANGIOPOHL, ANTADONA, ANTIVON QX, ARZOMEBA, BENSITRAK (…).
- **Tabla "CLIENTES BOTTOM DESEMPEÑO"** (Solicitante | Cliente | Mes Ant | Vol | Vta $$ | GAP PZA | GAP $$):

| Cliente | Mes Ant | Vol | Vta $$ | GAP PZA | GAP $$ |
|---|---:|---:|---:|---:|---:|
| G. MUGUERZA (SALTILLO) | 44,166 | 26,628 | $3,086,227 | -91,215 | -$15,235,882 |
| G. MUGUERZA (A ESP.) | 38,990 | 24,706 | $3,966,434 | -97,181 | -$14,940,885 |
| GRUPO MUGUERZA (CHIH) | 33,380 | 21,297 | $2,643,982 | -72,848 | -$12,000,672 |
| G. MUGUERZA (CONCHITA) | 26,273 | 16,510 | $1,983,876 | -67,130 | -$10,999,270 |
| GRUPO MUGUERZA (MAYAB) | 25,647 | 15,628 | $2,180,404 | -61,315 | -$9,790,764 |
| GRUPO MUGUERZA (UPAEP) | 9,089 | 1,549 | $283,676 | -61,370 | -$9,599,266 |
| GRUPO MUGUERZA (SUR) | 23,222 | 15,037 | $2,128,604 | -57,291 | -$9,101,679 |
| GRUPO MUGUERZA (BETANIA) | 47,938 | 32,935 | $4,228,312 | -44,492 | -$7,684,619 |
| G. MUGUERZA (A GRACIA LEON) | 13,693 | 8,048 | $963,121 | -31,290 | -$5,169,582 |
| GRUPO MUGUERZA (VIDRIERA) | 20,846 | 13,685 | $2,030,654 | -27,168 | -$4,260,787 |
| GRUPO MUGUERZA (REYNOSA) | 13,208 | 8,432 | $801,792 | -22,023 | -$3,934,253 |
| GRUPO MUGUERZA (MTY) | 16,914 | 9,797 | $1,140,441 | -22,812 | -$3,911,606 |
| GRUPO MUGUERZA (CAM) | 5,838 | 4,412 | $454,668 | -12,667 | -$2,200,587 |
| GRUPO MUGUERZA (ZANITAS) | 4,583 | 2,910 | $329,438 | -12,255 | -$2,032,654 |
| GRUPO MUGUERZA (MURANO) | 1,655 | 748 | $67,879 | -5,537 | -$914,456 |
| **Total** | **325,442** | **202,322** | **$26,289,506** | **-686,595** | **-$111,776,962** |

(Los encabezados de columna "Mes Ant" y "Vol" no traen unidad explícita; parecen piezas. Vta $$ del Total coincide con el KPI VENTA 26.)

## LÁMINA 17 — Desempeño HP YTD. FC — G. AUNA
Título: **"Desempeño HP 2026 YTD. FC"**. Panel izq = Total HP (repetido). Panel der = **G. AUNA**:

- **Gráfica mensual G. AUNA, Ene–Abr** — series (XML, $MDP):

| Mes | 2025 | 2026 | Meta | Var (rótulo) |
|---|---:|---:|---:|---:|
| Enero | $3 (3.42) | $6 (5.89) | 5.85 | **72%** |
| Febrero | $4 (3.94) | $6 (5.76) | 5.38 | **46%** |
| Marzo | $5 (5.38) | $9 (9.06) | 6.50 | **68%** |
| Abril | $5 (5.20) | $5 (5.38) | 6.15 | **3%** |

- **Retos Futuros:** 1. Cambio en su estructura administrativa. 2. Apertura a negociaciones con aseguradoras. 3. Oportunidad nuevo proyecto de infusión (**520 BIs**). 4. Oportunidad negociación por convenio volumen. (Los 4 retos aparecen enunciados sin desarrollo de texto adicional.)

## LÁMINA 18 — Desempeño HP YTD. FC — Negociaciones P×V
Título: **"Desempeño HP 2026 YTD. FC"**. Panel izq = Total HP (repetido). Panel der = **Negociaciones P×V**:

- **Tabla (Cliente | # Hospitales | Beneficio Incremental Esperado, mensual $MDP):**

| Cliente | # Hospitales | Beneficio mensual |
|---|---:|---:|
| H. Amerimed | 3 | $0.7 |
| G. Azura | 4 | $0.6 |
| G. Muguerza | 15 | $6.3 |
| G. Polar | 8 | $1.6 |
| **Total** | **32** | **$9.4** |

- **Texto:** "Incrementar convenios con hospitales de gran potencial: **Grupo AUNA, Hospital Real San José, Hospital Country, Hospital Ginequito, Hospitales Puerta de Hierro**. Todas las negociaciones involucran cerrar volúmenes superiores al **70% del consumo** de los clientes en moléculas de alto interés comercial y potencial para PiSA."

## LÁMINA 19 — Desempeño HP YTD. FC — G. Ángeles
Título: **"Desempeño HP 2026 YTD. FC"**. Panel izq = Total HP (repetido). Panel der = **G. Ángeles**:

- **Gráfica mensual G. Ángeles, Ene–Abr** — series (XML, $MDP):

| Mes | 2025 | 2026 | Meta | Var (rótulo) |
|---|---:|---:|---:|---:|
| Enero | $39 (39.01) | $38 (38.12) | 43.83 | **-2%** |
| Febrero | $41 (40.75) | $42 (41.96) | 46.61 | **3%** |
| Marzo | $52 (52.28) | $49 (48.88) | 49.66 | **-7%** |
| Abril | $47 (46.88) | $43 (43.03) | 46.93 | **-8%** |

- **Retos Futuros:**
  1. **Descatalogación de Productos:** en 2025 perdimos **+$70MDP** por descatalogación (**Cefaxona IV: -$10.7MDP, Salpifar: -$9.8MDP, Pentren: -$8.2MDP, Pisapem: -$5.8MDP**). En 2026 ya se ven nuevos impactos (**Dexmedetomidina, Clorhexidina, Gasas**).
  2. **Nuevos Negocios Kener:** Lanzamiento de **Kener Qx** (equivalente a nuestro servicio SIA). Posible lanzamiento **2027 de Centros de Mezcla** (equivalente SAFE).

## LÁMINA 20 — Desaceleración venta distribuidor
Título: **"Estamos teniendo una desaceleración en la venta distribuidor"**. Panel izq = Total HP (repetido). Panel der = **Distribuidores**. Banner inferior: **"El"** (texto incompleto/cortado, ver Vacíos).

- **Tabla clientes distribuidores (Cliente | Región | Venta 2026 | Venta 2025 | GAP $ | Crec %), $MDP:**

| Cliente | Región | Venta 2026 | Venta 2025 | GAP $ | Crec % |
|---|---|---:|---:|---:|---:|
| Surtidora Médica del Carmen* | Sur | $14.5 | $18.3 | -$6.0 | -21% |
| Serv. Integral Farmalogístico | Sur | $2.5 | $6.3 | -$4.4 | -59% |
| GIFYT* | Centro | $11.8 | $13.5 | -$4.1 | -43% |
| VITALMEX Internacional* | Centro | $8.6 | $11.7 | -$2.3 | -26% |

- **Tabla productos (Producto | Venta 2026 | Meta 2026 | Venta 2025 | GAP $ | Crec $), $MDP:**

| Producto | Venta 2026 | Meta 2026 | Venta 2025 | GAP $ | Crec $ |
|---|---:|---:|---:|---:|---:|
| EXETIN-A | $0.4 | $2.7 | $3.9 | -$2.3 | -$3.5 |
| MULTIVITAMINICO | $1.6 | $6.4 | $4.2 | -$4.8 | -$2.6 |
| CUSTODIOL | $7.1 | $8.5 | $9.5 | -$1.5 | -$2.5 |
| SOL CS | $5.6 | $7.4 | $7.3 | -$1.8 | -$1.6 |
| SOL HT | $1.3 | $2.7 | $2.5 | -$1.4 | -$1.3 |
| INHEPAR | $1.7 | $3.5 | $2.9 | -$1.8 | -$1.2 |

- **Retos Futuros (texto):**
  1. "Dist con venta a gobierno FC por oportunidad (se disminuyeron por contratos con gobierno, ej. **Eritropoyetina**): **Farmalogístico, Disermer, Bienestar**."
  2. "**Subrogaciones HD: GIFYT, COSAR, MED Santa Carmen, Vitalmex.** **Exetin-A** (ya no incluye paquetes, gobierno lo entrega). **Vitafusin** (dejaron de comprar por precio). **Inhepar** (gobierno no lo incluye en paquete para GIFYT)."

---

## Inconsistencias internas

1. **Tabla resumen Total HP no reconcilia con las columnas graficadas (L13/L14 y repetidas en L15/17/18/19/20).** Las diferencias 2026−2025 de los data labels mensuales son Ene +30 ($476→$506), Feb +49 ($436→$485), Mar +48 ($498→$546), Abr −27 ($513→$486); pero la fila **"Crec. ($)"** de la tabla dice **+$0.5 / +$38.9 / +$42.5 / -$20.9**. No coinciden mes a mes. Igual, la fila **"GAP vs Meta"** (-14.8/-26.8/-8.1/-40.6) no equivale a (2026 − Meta) de las series (que daría ≈ -18.2 / -35.5 / +2.4 / -70.4). La tabla resumen parece de un agregado distinto al de las barras mensuales.
2. **Los montos mensuales de la tabla resumen no suman a los totales anuales.** Crec. mensual +0.5+38.9+42.5−20.9 = **+60.9**, pero el total anual dice **+$99.9**. GAP mensual −14.8−26.8−8.1−40.6 = **−90.3**, pero el total anual dice **−$121.6**. (En cambio, las barras sí cuadran: 2026 Ene–Abr 506+485+546+486 ≈ $2,022 y 2025 476+436+498+513 ≈ $1,922, Δ ≈ +$100 ≈ +$99.9.) La fila resumen y las barras cuentan historias numéricas distintas.
3. **Doble signo en el GAP anual (L13):** impreso **"-$-121.6"** (celda `Tabla 92`). Presumible **−$121.6MDP**, pero el texto tal cual es ambiguo.
4. **"Alc. Meta" mensual no deriva limpio de las series.** Con 2026/Meta del XML daría Ene 96.5% (tabla 96.6% ✓), Feb 93.2% (tabla 93.9%), Mar 100.4% (tabla **98.3%** ✗), Abr 87.4% (tabla **91.3%** ✗). Marzo y Abril divergen.
5. **Variante de redacción del frente 01 entre L4/L5 y L8/L10** (una versión atribuye la cita a "GASS"/"SM" con "GAS y HSAI"; la otra a "GAS"/"SM" sin "HSAI"). Mismo mensaje, texto distinto en el build.
6. **"T. Infusión +$36.9MDP (97.8%)" listado como "punto a favor" (L14)** aunque su alcance es <100% (97.8%); conviven un crecimiento en monto con un alcance de meta por debajo del 100%. No es error, pero la clasificación "a favor" con 97.8% es discutible.
7. **Escala de "Total HP" ($2,022M Ene–Abr) vs "Frasco Cerrado" ($1,737M Ene–Abr, suma de 421.3+414.7+476.9+423.9).** FC ≈ 86% de Total HP; el ~14% restante (~$285M) no se descompone explícitamente en el deck (queda implícito: infusión/SIA/SAFE/servicios).

## Posibles choques con la referencia sell-in (solo flagear; no resolver)

> Referencia dada (sell-in 1S 2026 = Ene–Jun, cierre junio, $M MXN). Este deck es **Ene–Abril 2026** (4 meses, cierre a mayo) y usa el rótulo **"HP / Hospitales Privados"**. Ventanas y posiblemente definiciones de segmento distintas.

1. **Total del segmento Hospitales — ventana y monto.** Deck: **Total HP 2026 Ene–Abr = $2,022M**, alcance **94.3%**, GAP **−$121.6M**, crecimiento **+5%**. Referencia: **Hospitales 1S = $3,054.5M**, **95.2%**, **+5.1%**. Son ventanas distintas (4 vs 6 meses); no comparables directo. El crecimiento +5% (deck, 4M) vs +5.1% (ref, 6M) es cercano pero de bases distintas.
2. **Colisión de nombre "Frasco Cerrado / FC".** El deck titula las láminas 14–20 **"Desempeño HP YTD. FC"** y grafica un "Frasco Cerrado" **dentro de Hospitales Privados** (FC 2026 Ene–Abr ≈ $1,737M). La referencia tiene un segmento aparte **"Gobierno Frasco Cerrado = $4,034.3M, 90.0%, −0.6%"**. Son cosas distintas con el mismo apodo "FC"; riesgo de confusión al integrar. (Deck FC ≈ $1,737M/4M dentro de HP privado ↔ Ref Gobierno FC = $4,034.3M/6M.)
3. **Crecimiento por cuenta contradice el signo agregado.** El deck muestra **G. Ángeles decreciendo** (Mar −7%, Abr −8%; "punto de dolor" −$8.2MDP, 91%) y **Canal Distribuidor / Hospitalización −$18.8MDP c/u (73%)**, mientras Muguerza/AUNA crecen fuerte. La referencia reporta **Hospitales 1S +5.1%** en positivo. No es choque directo (niveles distintos), pero el mix de este deck (fuerte caída en Ángeles y distribuidores) conviene reconciliar contra el +5.1% agregado del 1S.
4. **PVM.** El deck no presenta un puente Precio-Volumen-Mezcla; sí trae señales de precio (piso Mindray $110-121, ZMIN $227, oncológicos GASS por debajo de Costo SAFE, tabla de incrementos 3-10%). La referencia PVM 2 vías (vol −830.7 / precio+mezcla +1,070.0 / piezas −5.1%) es del total PiSA, no de Hospitales; no hay número comparable en este deck para chocar.
5. **Servicios.** El deck menciona SAFE/SIA/T. Infusión como líneas de servicio dentro de HP, sin cifra de "Servicios" agregada. La referencia trae "Servicios 2,219.4 / 102.1% / +4.0%" como segmento separado. Definiciones distintas (aquí Servicios es un segmento del total PiSA; en el deck es sub-línea de HP); no comparables sin puente.

## Vacíos declarados

1. **No hay lámina de cierre / conclusiones ni plan 2S cuantificado.** El deck termina en distribuidores (L20) con banner **incompleto ("El")**. No hay total-a-diciembre, YTG, ni consolidación de los "beneficios esperados" mencionados por cuenta.
2. **Ventana corta:** todo es **Ene–Abril 2026**. No hay mayo ni cifras de 1S (Ene–Jun) — que es la base de la referencia del Consejo. Para el 27-jul habrá que actualizar a 1S.
3. **Sin nota de fuente sistemática.** Solo la L3 cita "El Economista, 10-may-2026". Las cifras de venta/meta/alcance (L13–20) no traen nota de fuente (¿SAP sell-in? ¿qué corte?). La L6 no rotula fuente del "+600MDP" ni de "200 clientes >$200". Los oncológicos (L9) no citan fuente de "Costo SAFE" ni "Precio GASS".
4. **Unidades implícitas.** Las tablas de desempeño (L13–20) están en $MDP por contexto pero sin rótulo de unidad en la lámina. La L16 (Power BI) mezcla piezas ($Vol, GAP PZA) y pesos ($$) sin encabezado de unidad. Las speaker notes de L7 (ABC 25 / SM 24.60 / …) no declaran qué miden.
5. **Definición de "HP / Total HP" no explicitada.** No se aclara si "Hospitales Privados" incluye o excluye canal Distribuidor, gobierno vía distribuidor, SAFE/SIA. La L20 sugiere que Distribuidores está dentro de HP, pero la L14 lo lista como "punto de dolor" separado. Falta el diccionario de perímetro.
6. **Retos de AUNA (L17) enunciados sin desarrollo:** los 4 retos aparecen como títulos sin cuerpo (a diferencia de Muguerza y Ángeles que sí traen detalle).
7. **Speaker notes:** solo la L7 tiene notas; el resto de láminas no trae notas del orador.
8. **Meta de infusión / equipos de bomba sin cierre:** L6 dice negocio "+600MDP anual" y "200 clientes >$200", pero no cuantifica cuánto está en riesgo por Mindray ni la meta de defensa (solo aparece el impacto −$1.6MDP/mes de Muguerza en L15).

---

*Fin de la extracción. Render y PNG de trabajo en el scratchpad de sesión (no en el proyecto): `.../scratchpad/DGpure.pdf`, `.../scratchpad/dg_p01..20.png`, texto crudo `.../scratchpad/dg_extract.txt`.*
