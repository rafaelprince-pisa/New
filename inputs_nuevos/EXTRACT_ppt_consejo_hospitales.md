# EXTRACT — "Presentacion RP HP_Consejo_Hospitales.pptx"

**Archivo fuente:** `/Users/rafaelprince/Downloads/Presentacion RP HP_Consejo_Hospitales.pptx`
**Peso / fecha:** 934 KB, modificado 16-jul-2026 09:09
**Láminas:** 16
**Qué es:** Deck del canal **Hospitales (HP)** de PiSA preparado como insumo para el Consejo del 27-jul-2026. El sufijo "RP HP" sugiere versión para Rafael Prince, foco Hospital Privado. Mezcla láminas de contexto de mercado (estilo "Google Slides", texto) con láminas analíticas nativas think-cell (charts + cajas "Consideraciones").
**Método de extracción:** texto de todos los shapes (incl. grupos, tablas, notas) vía python-pptx; datos de gráficas nativas vía `chart.series/values`; render a PDF (LibreOffice) → PNG 150 dpi (PyMuPDF) leído lámina por lámina. Unidades $ en **MDP (millones de pesos MXN)** salvo donde se indique piezas o pesos por unidad.
**Nota de método sobre montos:** las cascadas y barras traen las etiquetas visibles en $M redondeados; los `SERIES` nativos traen el dato crudo en pesos (ej. `92,575,756` = $93M). Reporto ambos donde aplica.
**Speaker notes:** NINGUNA lámina tiene notas del orador (se revisaron las 16; todas vacías).

---

## LÁMINA 1 — Contexto de mercado (texto)

- **Banner (esquina sup. der.):** "Intervención de aseguradoras:"
- **Título asertivo (arriba):** "Inflación médica y cambios fiscales fuerzan una reestructuración del ecosistema de salud privada."
- **Título de bloque (azul):** "La relación rota entre aseguradoras y hospitales: un sistema bajo presión"
- **Bullets (columna izq.):**
  - **Inflación Desbordada:** México alcanza **14.8% en inflación médica (2026)**, cuadruplicando la inflación general y rompiendo presupuestos.
  - **Impacto Fiscal Severo:** El **IVA del 16%** en pagos directos ya no es acreditable (Ley 2026). Este costo definitivo encarece pólizas **hasta un 40%** en segmentos [frase cortada en el original].
- **Bullet (columna der.):**
  - **Pérdida de Control:** Históricamente, el hospital dictaba precios discrecionales; hoy, las aseguradoras (que cubren **80-85% del costo**) no pueden sostener este esquema.
- **Fuente (pie):** "Análisis de Mercado, El Economista (10 de mayo, 2026)."

---

## LÁMINA 2 — Contexto de mercado (texto)

- **Banner:** "Intervención de aseguradoras:"
- **Título asertivo:** "Transición de coberturas ilimitadas hacia modelos de estricta vigilancia y contención de abusos."
- **Bloque izquierdo — "El Caso AXA: Fuga de Hospitales":**
  - **Sobrecostos Extremos:** Detección de márgenes abusivos del **300% al 400%** en tratamientos de quimioterapia dentro de la red hospitalaria.
  - **Redirección Estratégica:** AXA instruye explícitamente **no atender oncología** en hospitales tradicionales, desviando el flujo.
  - **Auge Clínico:** Explosión de **centros de infusión independientes**, impulsando la comoditización acelerada de las mezclas.
- **Bloque derecho — "Suministro directo en quirófano":**
  - **Control de Insumos:** Aseguradoras implementan modelos de **compra directa** para cirugías de trauma y ortopedia.
  - **Bypass al Hospital:** Proveen los consumibles **directamente al quirófano** para neutralizar la inflación impuesta por el hospital.
  - **Nuevos Procesos:** Exigencia de **programación anticipada estricta** para garantizar la cobertura del GMM sin fricciones de precio.
- **Sin fuente al pie.**

---

## LÁMINA 3 — "Pisa HP vs Mercado | VDM IQVIA"  ⚠️ VACÍO (no renderizable)

- **Banner/título:** "Pisa HP vs Mercado | VDM IQVIA"
- **Contenido:** un objeto OLE think-cell ("think-cell data - do not delete"). **La lámina NO tiene texto adicional ni gráfica recuperable.**
- **Por qué no hay datos:** el render think-cell está guardado como `image1.emf` de **204 bytes = placeholder vacío** (LibreOffice lo exporta en blanco). python-pptx no detecta gráfica nativa. El workbook embebido de 106 KB (`Microsoft_Excel_Worksheet.xlsx`) corresponde a la **burbuja de la Lámina 8** (mismos valores de precio), no a esta lámina.
- **Qué debería mostrar (inferido del título):** comparativa de **PiSA HP vs total del mercado** en **VDM (Venta Directa a Mercado) de IQVIA**. **Los números no son recuperables de este archivo.** → Ver "Vacíos declarados".

---

## LÁMINA 4 — "Trafico Hospitalario" (2 líneas + caja)

- **Banner:** "Trafico Hospitalario"
- **Título asertivo:** "Desempeño Equipo para Bomba y soluciones evidencia de desaceleración reciente frente al desempeño histórico con nuestros clientes"
- **Gráfica 1 (línea) — "Desempeño Eq/Bomba 26 vs promedio 25 (en miles de piezas)":**
  - Eje Y: 80–110 (miles de piezas). Eje X: Ene–Jun.
  - Serie **Eq/Bomba 26** (valores crudos en piezas): Ene 96,325 · Feb 94,595 · Mar 100,621 · Abr 94,211 · May 92,391 · Jun 105,076. (Se grafican como 96.3, 94.6, 100.6, 94.2, 92.4, 105.1 mil.)
  - Línea base **CPM 25 EB** (constante): **104,519** (≈104.5 mil).
  - Lectura: promedio 1S26 ≈97.2 mil, por debajo del CPM base; sólo Jun (105.1) supera la base.
- **Gráfica 2 (línea) — "Desempeño Soluciones 26 vs promedio 25 (en millones de piezas)":**
  - Eje Y: 1.6–2.6 (millones de piezas). Eje X: Ene–Jun.
  - Serie **Soluciones 26** (crudos en piezas): Ene 2,161,069 · Feb 2,092,704 · Mar 2,320,736 · Abr 1,991,371 · May 1,954,304 · Jun 2,324,060. (Grafican 2.16, 2.09, 2.32, 1.99, 1.95, 2.32 M.)
  - Línea base **CPM 25 SOL** (constante): **2,140,677** (≈2.14 M).
- **Caja "Consideraciones":**
  - Estos productos se consideran para analizar **ocupación de hospitales** porque dominamos ese mercado.
  - **Equipos para Bomba** se mantiene por debajo del promedio de venta del año anterior en el acumulado (YTD), con desaceleración más marcada en **abril y mayo**.
  - **Soluciones** registra desempeño cercano al promedio del año previo en el acumulado; caída por debajo de ese nivel en **abril y mayo**.
  - El comportamiento en ambos sugiere **pérdida de dinamismo** en los meses recientes respecto al LY.

---

## LÁMINA 5 — "La amenaza en tres frentes" (mapa de competidores)

- **Banner:** "La amenaza en tres frentes"
- **Título asertivo:** "La línea de **Terapia de Infusión vale $1,473 MDP** y es nuestra carta de entrada a los hospitales. **Soluciones y Equipos para bomba representan el 63% de la línea con $930 MDP** y el **18% de la venta total del mercado HP**."
- **Centro:** logo PiSA con leyenda "¿Dónde estamos?" y silueta de mapa de México.
- **Frente 1 — Kener Inyectables (izq.):**
  - Kener desplaza nuestra venta en **Grupo Ángeles**, en 2025 con **$43 MDP**.
  - **Directores Regionales:** reportan presencia en todos los hospitales corporativos y hospitales importantes en las regiones, con precios por debajo de los nuestros.
  - Este catálogo cruzado con Kener representa un importe de **~$850 MDP**, con **~$300 MDP** sólo en corporativos que podrían representar un riesgo.
- **Frente 2 — Baxter / Soluciones (der. arriba):**
  - **Amenaza directa al negocio base:** si nos sustituye en soluciones el daño es mayor que el de cualquier otro competidor (ya compite en **Tijuana/Chihuahua** y propone precios por debajo de los nuestros en cuentas puntuales).
  - **Directores Regionales:** reportan presencia en hospitales corporativos **MAC, MEDICA SUR** y clientes al norte del país.
- **Frente 3 — Mindray / Equipo para Bomba (der. abajo):**
  - **Mindray con tecnología china:** llega con precios muy baratos en equipos y consumibles.
  - **Amenaza directa a la línea más sólida:** PiSA coloca **bombas en comodato (equipo B.Braun)**, lo que da acceso a los hospitales; sólo la venta de los equipos complementarios de la bomba vale **~$600 MDP**.

---

## LÁMINA 6 — "La amenaza en tres frentes": Kener Inyectables (columnas + caja)

- **Banner:** "La amenaza en tres frentes"  ·  **Chip:** "Kener Inyectables"
- **Título asertivo:** "Kener desplaza nuestra venta en Grupo Angeles, en 2025 con **~$43 MDP** y se empieza a desplazar a Corporativos con códigos del catálogo que tiene un valor a **Sell-In Pisa de ~$300 MDP**."
- **Gráfica (columnas) — "Cat Pisa Kener" (azul) + "Meta 7-12" (tramada):** valores en $ MDP.
  - 2022: **$790** · 2023: **$833** · 2024: **$894** · 2025: **$826**
  - 2026FY: **$386** (real 1S / Cat Pisa Kener) **+ $443** (Meta 7-12) = **$829** total
  - Flechas de crecimiento: **2022→2024 +6%** · **2024→2025 −8%** · **2025→2026FY (total) 0%**
  - Series nativas: serie1 (Cat) [790.18, 832.94, 893.95, 826.22, 386.22] M · serie2 (Meta 7-12) [—, —, —, —, 442.57] M.
- **Caja "Consideraciones":**
  - **Compra mercado con Grupo Ángeles como vehículo:** ejemplo **meropenem a $75 de lista** contra **$600-800 precio promedio**; **35,000 médicos** y centros de mezclas propios anunciados.
  - **Amenaza real pero en proporción:** vende **~$1,000 M** con meta de **~$5,000 M al 2030**; **no es el foco de la sesión de hospitales**.

---

## LÁMINA 7 — "Guerra de Precios: Defensa Competitiva" (texto)

- **Banner:** "Guerra de Precios: Defensa Competitiva"
- **Título asertivo:** "El mercado de bombas de infusión **(+$600 MDP)** enfrenta presiones de comoditización extremas."
- **Bullets:**
  - **Ataque a Cuentas Clave:** Mindray despliega ofertas predatorias **(desde $110)** impactando la ejecución en grupos estratégicos como **Ángeles y Muguerza**.
  - **Resiliencia Operativa:** PiSA mantiene rentabilidad, logrando la retención de **más de 200 clientes institucionales** con ticket promedio superior a **$200**.
  - **Ventaja Estructural:** posición sólida frente a otros competidores en soluciones (Ej. **PiSA −35% vs Baxter, $17 vs $25**).

---

## LÁMINA 8 — "La amenaza en tres frentes": Mindray / Equipo para Bomba (burbuja)

- **Banner:** "La amenaza en tres frentes"  ·  **Chip:** "Equipo para Bomba" (Mindray)
- **Título asertivo:** "La ejecución se ve afectada en Hospitales por ofertas agresivas de **Mindray desde $110.00** cuando nuestra oferta está entre los **$150 - $200**."
- **Callout rojo:** "**200 clientes compran por arriba de $200.00**"
- **Gráfica de burbujas:** eje Y = **Precio** ($100–$240), eje X = **Unidades** (0–200,000), tamaño = venta.
  - Línea de referencia **ZMIN / PiSA $227** (superior, azul) y **Mindray $110-121** (inferior, roja).
  - Etiqueta contexto: "MINDRAY (Muguerza, Angeles, AZURA, Hospitaria, Ginequito)".
  - Serie nativa de **Precio 26** (18 burbujas): 216.34, 152.89, 173.71, 152.08, 206.43, 189.85, 162.51, 151.21, 113.49, 223.09, 229.50, 220.70, 174.64, 127.05, 227.19, 230.51, 225.47, 204.84.
  - Cuentas rotuladas (Venta 26 / Uds 26 / Precio 26, de workbook embebido):
    | Cuenta | Venta 26 ($) | Uds 26 | Precio 26 ($) |
    |---|---:|---:|---:|
    | Gpo. Ángeles (Operadora de Hospitales Ángeles) | 37,027,860 | 171,200 | 216.34 |
    | Star Medica | 13,193,350 | 81,203 | 152.89 |
    | Muguerza (Christus Muguerza Sistemas) | 6,995,738 | 40,903 | 173.71 |
    | UANL | 4,075,651 | 26,800 | 152.08 |
    | San Javier | 3,302,925 | 16,000 | 206.43 |
    | Sinergia | 2,944,938 | 15,500 | 189.85 |
    | CM del Mayab | 2,222,130 | 13,674 | 162.51 |
    | Distribuidora VASE | 1,947,585 | 12,880 | 151.21 |
    | H. San José Hermosillo | 1,775,378 | 7,822 | 113.49 |
    | H. del Country | 1,745,113 | 7,850 | 268.42 |
    | H. Aranda de la Parra | 1,561,603 | 7,000 | 223.09 |
    | Andalucía | 1,324,210 | 6,000 | 220.70 |
    | Administradora Hospitalaria | 1,246,634 | 4,906 | 127.05 |
    | H. Terranova | 1,188,661 | 5,330 | 227.19 |
    | Promotora Poblana | 1,106,470 | 4,800 | 230.51 |
    | Moscati Querétaro | 1,025,515 | 4,900 | 204.84 |
  - (El workbook embebido lista **>400 filas por Solicitante×Material**, productos FLEBOTEK BOMEDI y FLEBOPLAST BC PLUS, con Venta/Uds/Precio 25 y 26. Aquí van las burbujas rotuladas + top; el detalle completo está en el archivo fuente.)
- **Anotaciones sobre burbujas:** "$110 - 121" (Mindray), grupos: Gpo. Angeles, Star Medica, Muguerza, UANL, San Javier, Sinergia, Promotora Poblana; "ZMIN $227".

---

## LÁMINA 9 — "La amenaza en tres frentes": Baxter / Soluciones (columnas + caja)

- **Banner:** "La amenaza en tres frentes"  ·  **Chip:** "Soluciones" (Baxter)
- **Título asertivo:** "Amenaza directa al negocio base; si nos sustituye en soluciones el daño es mayor que el de cualquier otro competidor."
- **Gráfica (columnas) — "Soluciones" (azul) + "Meta 7-12" (tramada):** $ MDP.
  - 2023: **$396** · 2024: **$455** · 2025: **$467**
  - 2026FY: **$232** (real 1S) **+ $267** (Meta 7-12) = **$499** total
  - Flechas: **2023→2024 +15%** · **2024→2025 +3%** · **2025→2026FY (total) +7%**
  - Series nativas: serie1 [396.10, 454.78, 466.98, 232.21] M · serie2 (Meta 7-12) [—, —, —, 266.85] M.
- **Caja "Consideraciones":**
  - **Baxter está ofertando en $17.00 → −40% precio ejecutado.**
  - Precios ejecutados por cuenta: **ABC $25 · SM $25 · Christus $23 · G. Ángeles $21 · Español $24**.
  - **Riesgo:** el precio sería **impuesto y no acordado**; el cliente tomará medidas de castigo a la cuenta con el resto de productos.

---

## LÁMINA 10 — "¿Cómo defendemos estos frentes?" (mapa de respuestas)

- **Banner:** "Como defendemos estos frentes?"
- **Centro:** PiSA "¿Dónde estamos?"
- **Frente 1 — Kener Inyectables:**
  - **Proyecto NADAL:** **PLAN KENER** con defensa selectiva y gobierno central de precios de pelea ("láser", no barra libre); **~40 convenios multi-hospital por ~$25 M/mes** con business reviews.
- **Frente 2 — Baxter / Soluciones:**
  - **Por definir:** se cuenta con el antecedente, pero **no se ha analizado el impacto** y aún no se trabaja el complemento de respuesta. ⚠️ (pendiente)
- **Frente 3 — Mindray / "Blindar Terapia de Infusión":**
  - **Cambio de tecnología:** Muguerza, Hospitaria, Auna, GASS? (con signo de interrogación en el original)
  - **Campaña de "Servicio de Infusión":** Calidad Producto Pisa · Congreso enfermería · Cursos Hospitales/Pisa.
  - **Cambio de Rol:** Promotor TF → "Consultor TF".

---

## LÁMINA 11 — "Cascada Hospitales 1S-26 vs 1S-25" (waterfall, scope FC)

- **Banner:** "Cascada Hospitales 1S-26 vs 1S-25"
- **Waterfall ($ MDP):** Venta Neta 2025 **2,907** → Venta Neta 2026 **3,056**; total **+149 (+5%)**.
  - Precio **−$8** · Volumen **+$93** · Descuentos **$0** · Altas y Bajas **+$25** · Servicios **+$41**.
  - Series nativas (magnitud del brinco, pesos): Precio 8,462,622 · Volumen 92,575,757 · Descuentos 241,086 · Altas y Bajas 24,773,805 · Servicios 40,615,355.
  - **Nota aritmética:** −8+93+0+25+41 = **+151** vs el **+149** rotulado (Δ2 por redondeo/base fina).
- **Desglose regional por palanca (globos):**
  - **Precio:** Reg A +$4M · Reg B −$6M · Reg C −$13M · Reg D +$7M
  - **Volumen:** Reg A +$28M · Reg B +$38M · Reg C +$30M · Reg D −$3M
  - **Descuentos:** Reg A +$1M · Reg B −$1M · Reg C +$0M · Reg D +$0M
  - **Altas y Bajas:** Reg A +$4M · Reg B +$7M · Reg C +$9M · Reg D +$5M
  - **Servicios:** Mezclas +$33M · HD −$0M · Anest. +$8M
- **Notas al pie:**
  - **Precio:** estrategia de decremento de precios para ganar empuje en la venta por volumen (**Heparina y Ondansetron**).
  - **Volumen:** principal Inc. por estrategias de bajadas de precio y aumento orgánico en volumen.
  - **Altas y Bajas:** crecimiento por lanzamientos (**Parecoxib, Ertapenem, Urología**).
  - **Servicios:** el Inc. principal por **moléculas MAB (negociación de precio Keytruda)**.

---

## LÁMINA 12 — "Cascada Hospitales 1S-26 vs Meta 26" (waterfall, scope FC)

- **Banner:** "Cascada Hospitales 1S-26 vs Meta 26"
- **Waterfall ($ MDP):** Venta Neta 2026 **3,207** (nota: aquí "3,207" es la **Meta 1S**, ver abajo) → Venta Neta Meta 2026 **3,056**; total **−151 (−5%)**.
  - **Aclaración de lectura:** la barra izquierda rotula "Venta Neta 2026 = 3,207" y la derecha "Venta Neta Meta 2026 = 3,056". Por la etiqueta **−151 (−5%)** y por el 95.2% de alcance, la lógica correcta es **Meta 1S = 3,207 → Real 1S = 3,056** (3,056/3,207 = 95.3%). **Los rótulos de las barras parecen invertidos** (ver Inconsistencias).
  - Precio **−$67** · Volumen **−$67** · Descuentos **+$5** · Altas y Bajas **−$38** · Servicios **+$15**.
  - Series nativas (magnitud del brinco, pesos): Precio 66,629,024 · Volumen 66,508,118 · Descuentos 5,214,532 · Altas y Bajas 38,298,390 · Servicios 15,028,349.
  - **Nota aritmética:** −67−67+5−38+15 = **−152** vs el **−151** rotulado.
- **Desglose regional por palanca (globos):** **IDÉNTICO al de la Lámina 11** (mismos Reg A/B/C/D y Mezclas/HD/Anest.). Ver Inconsistencias.

---

## LÁMINA 13 — "Hospitales: qué hicimos bien, qué nos faltó" (mensual FC+SERV)

- **Banner:** "Hospitales: qué hicimos bien, qué nos faltó"  ·  **Subtítulo:** "Desempeño General HP 1S-26"
- **Gráfica mensual (columna apilada):** **FC** (navy) + **SERV.** (azul claro), $ MDP.
  | Mes | FC | SERV | Total | Alc. Meta | GAP vs Meta | Crec. (%) |
  |---|---:|---:|---:|---:|---:|---:|
  | Ene | 421 | 84 | 506 | 101% | +$4 | +6% |
  | Feb | 415 | 70 | 485 | 96% | −$21 | +11% |
  | Mar | 477 | 69 | 546 | 99% | −$8 | +10% |
  | Abr | 424 | 62 | 486 | 91% | −$46 | −5% |
  | May | 407 | 67 | 474 | 86% | −$76 | −2% |
  | Jun | 474 | 80 | 553 | 99% | −$8 | +12% |
  | **Acumulado** | **3,050** | **432** | **3,482** | **95%** | **−$156** | **5%** |
  - Series nativas FC (M): 421.30, 414.71, 476.89, 423.94, 407.24, 473.55; acumulado 3,049.67.
  - Series nativas SERV (M): 84.33, 70.29, 68.77, 62.20, 66.75, 79.70; acumulado 432.04.
  - Anotación: flecha **+17%** de May ($474) a Jun ($553).
  - Etiquetas de totales por mes: $506, $485, $546, $486, $474, $553; Acumulado $3,482.

---

## LÁMINA 14 — "Hospitales: qué hicimos bien, qué nos faltó" (regiones + cuentas)

- **Banner:** "Hospitales: qué hicimos bien, qué nos faltó"
- **Título asertivo:** "Junio fue el mejor mes del semestre en las 4 regiones; cada una aporta una fortaleza distinta a replicar."
- **Barra 1 — "Crecimiento en venta 2025 vs 2026" (SEM1):** 2025 **$2,900** → 2026 **$3,050**, **+5%**; alc **95%**, gap **−$155.7**, crec **5%**. (Series: 2,900.27 M → 3,049.67 M.)
- **Barra 2 — "Crecimiento en venta SAFE/SIA 25 vs 26" (SEM1):** 2025 **$391** → 2026 **$432**, **+10%**; alc **104%**, gap **+$14.7**, crec **10%**. (Series: 390.91 M → 431.67 M.)
- **Panel "Regiones" (A/B/C/D):**
  - **A:** Mejor cierre de Junio de **FC**. Cuentas ancla sólidas (**Dalinde 159%, Ángeles Mty**). Base amplia y diversificada.
  - **B:** Mayor crecimiento anual. Palancas de alto valor: **Equipo para Bomba, Sol HM, Antifex**. Impulso sostenido.
  - **C:** Cuentas estrella muy por encima de meta (**SYG Zambrano 132%, UANL**). Buena calidad de venta y menor devolución.
  - **D:** Fuerte recuperación en Junio desde el mínimo de Mayo. **Multivitamínico y Equipo para Bomba** lideraron el repunte.
- **Panel "Clientes que superaron meta S1"** (cuenta · región · alc% · aporte $):
  | Cliente | Región | Alcance | Aporte |
  |---|:--:|---:|---:|
  | FUND. TELETON VIDA | B | 675% | +$6.0M |
  | UANL | C | 110% | +$5.4M |
  | GRUPO SYG (ZAMBRANO) | C | 117% | +$4.9M |
  | GRUPO MUGUERZA (BETANIA) | A | 125% | +$3.7M |
  | DU MOUNT CI | C | 232% | +$3.0M |
  | COM. ONCORED MEDICA | B | 205% | +$3.0M |
  | SWISS HOSPITAL | C | 146% | +$3.0M |

---

## LÁMINA 15 — "Qué nos faltó en el 1S" (3 comparativos + narrativa)

- **Banner/título:** "Qué nos faltó en el 1S"
- **Leyenda:** S1 2025 (gris) vs S1 2026 (navy). $ MDP salvo indicación.
- **Bloque 1 — Abril-Mayo:** 2025 **$998** → 2026 **$960**; **−4%**; alc **89%**; gap **−$122.5**.
- **Bloque 2 — SEM1 (Ángeles):** 2025 **$114** → 2026 **$89**; **−22%**; alc **73%**; gap **−$32.7**.
- **Bloque 3 — Junio:** 2025 **$492** → 2026 **$553**; **+12%**; alc **99%**; gap **−$8**.
- **Narrativa (der.):**
  1. **Impacto Abril-Mayo:** costó **la mitad del crecimiento proyectado** (de un ritmo de **+9/10%** a solo **+5%**). Factores clave: **baja ocupación, liberación de crédito a clientes estratégicos y fuerte presión de precios**.
  2. **Pérdida en Grupo Ángeles CDMX:** impacto directo en la **línea SAFE** con merma constante de **−$10 M/mes** arrastrada desde inicio de año, afectando el acumulado del semestre (**−22% vs. periodo anterior**).
  3. **El asterisco de Junio (+12%):** el 99% lleva nota al pie: el mes contó con **5 lunes y ~$10 M one-off en mezcla de SAFE**. Mix temporal favorable que potenció la ejecución.

---

## LÁMINA 16 — "Desempeño 1S y Plan de Ejecución 2S"

- **Banner:** "Desempeño 1S y Plan de Ejecución 2S"
- **Barra izq. (gap a meta):** **Venta Prom. (Ene-Mayo) $429** + **"Monto excedente para meta Jul-Dic" $57** (tramado) → **Meta Prom. (Jul-Dic) $485**. (Series nativas %: 88.35% venta / 11.65% excedente vs 100% meta; rótulos $429, $57, $485.)
- **Cascada de palancas de recuperación (apilada, suma $47 M/mes):**
  | Palanca | $ M |
  |---|---:|
  | Cambio de tecnología | $2 |
  | Convenios | $4 |
  | PIN no solicitado | $5 |
  | Nuevos Productos | $6 |
  | Plan liberación cartera | $7 |
  | Plan Kener | $9 |
  | Recuperación | $14 |
  | **Total** | **$47** |
  - Series nativas (M): 13.74, 8.88, 7.47, 5.93, 5.23, 3.60, 2.43 (= 14, 9, 7, 6, 5, 4, 2 de abajo hacia arriba).
- **Caja "Plan de Acción (Jul-Dic)":**
  - **Defensa Base Instalada:** fortalecer **comodatos de infusión** basando la oferta en **Costo Total de Propiedad vs Mindray**.
  - **Plan Kener:** implementar modelo de **"precio gobernado"** para defensa selectiva, evitando desgaste en guerras de descuentos.
  - **Apriete de Convenios:** auditoría y cumplimiento estricto para recuperar entre **$3 M y $4 M mensuales** identificados.
  - **Alianzas Híbridas:** integración temprana con **centros de infusión externos**; PiSA aporta infraestructura de mezclas y ellos los pagadores.

---

# Inconsistencias internas

1. **Láminas 11 y 12 — desglose regional idéntico.** Los globos de Reg A/B/C/D por palanca (Precio, Volumen, Descuentos, Altas y Bajas) y el de Servicios (Mezclas/HD/Anest.) son **exactamente los mismos** en la cascada vs-LY (+149) y en la vs-Meta (−151). Es imposible que los desgloses regionales coincidan cuando los brincos totales de cada palanca son distintos (ej. Precio −$8 vs −$67; Volumen +$93 vs −$67). Parece **copy-paste** de los globos de L11 a L12.
2. **Lámina 12 — rótulos de barras probablemente invertidos.** La barra inicial dice "Venta Neta 2026 = 3,207" y la final "Venta Neta Meta 2026 = 3,056". Por el −151 (−5%) y por el alcance 95.3%, lo correcto es **Meta = 3,207 (barra inicial) y Real = 3,056 (barra final)**. Tal como está rotulado, "Venta Neta 2026" aparece con dos valores distintos entre L11 (3,056) y L12 (3,207).
3. **Sumas de cascada ≠ total rotulado (redondeo).** L11: palancas suman **+151** pero el total dice **+149**. L12: palancas suman **−152** pero el total dice **−151**. Δ de 1-2 M por redondeo de etiquetas.
4. **GAP acumulado −$156 (L13) vs −$155.7 (L14).** Mismo dato con redondeo distinto; consistente pero conviene unificar.
5. **FC acumulado $3,050 (L13/L14) vs Venta Neta 2026 = 3,056 (cascada L11).** Diferencia de **6 M** entre la barra mensual acumulada y la cascada para el mismo concepto (Hospitales FC 1S-26).
6. **SYG Zambrano: 132% (texto Región C, L14) vs 117% (tabla "Clientes que superaron meta", L14).** El mismo cliente aparece con dos alcances en la misma lámina.
7. **Crecimiento SEM1 rotulado como "+5%" con base $2,900→$3,050 (L14) = +5.2%**, mientras el acumulado exacto es 3,049.67/2,900.27 = **+5.15%**. Consistente, sólo precisión de etiqueta.
8. **Kener 2026FY "0%" (L6):** real $386 + Meta 7-12 $443 = **$829** vs 2025 **$826** = **+0.4%**, redondeado a 0%. OK, pero el $386 es sólo 1S mientras las barras 2022-2025 son año completo; la comparación "0%" mezcla 1S+meta-2S contra año completo (correcto conceptualmente pero no evidente en la lámina).

---

# Posibles choques con la referencia sell-in (solo se flagea, no se resuelve)

> Referencia dada: PISA 5 mercados 1S26 **16,518.5** vs meta 17,678.3 = 93.4%, +1.5%. **Hospitales 3,054.5 / 95.2% / +5.1%**. **Servicios 2,219.4 / 102.1% / +4.0%**. PVM 2 vías PISA: volumen −830.7 / precio+mezcla +1,070.0 (piezas −5.1%).

1. **Hospitales 1S-26 — nivel.** Referencia **3,054.5**. Deck: **3,056** (cascada L11) / **3,050** (barra FC acumulada L13-L14). Muy cercano; probablemente el mismo agregado con redondeos y corte ligeramente distintos.
2. **Hospitales — alcance de meta.** Referencia **95.2%**. Deck **95%** (L13/L14). Consistente.
3. **Hospitales — crecimiento vs 1S25.** Referencia **+5.1%**. Deck **+5%** (L11, L13, L14). Consistente.
4. **Meta 1S Hospitales.** Deck L12 implica Meta 1S = **3,207** (3,054.5/3,207 = 95.2% ✓ con la referencia). Coherente, aunque el rótulo de barra de L12 confunde (ver Inconsistencia #2).
5. **"Servicios / SERV" — colisión de nombre y magnitud.** El deck usa **SERV = $432 M** (1S, componente dentro de HP: SAFE/SIA, mezclas, MAB) y lo apila con FC $3,050 para llegar a HP $3,482. La referencia tiene un **segmento "Servicios" = 2,219.4 M**, que es un bloque distinto de PiSA, **no** el $432 del deck. **Riesgo de que en el Consejo se confunda el "Servicios/SERV" del deck HP con el segmento Servicios de la referencia.** Números de ambos lados: **deck SERV $432M** vs **referencia Servicios $2,219.4M**.
6. **PVM — signo de Precio.** Referencia total PiSA: **precio+mezcla +1,070.0** (positivo). Deck Hospitales L11: **Precio −$8 M** (negativo, estrategia de decremento en Heparina/Ondansetron). Scopes distintos (Hospitales-only vs 5 mercados) y descomposición distinta (el deck separa Precio, Volumen, Descuentos, Altas/Bajas, Servicios; la referencia usa 2 vías volumen vs precio+mezcla), por lo que **no es comparable 1:1**; se marca sólo para evitar que se lea el signo del precio de Hospitales como contradictorio con el total PiSA. Números: **deck Precio Hospitales −$8M (vs LY)** vs **referencia precio+mezcla PiSA +$1,070.0M**.
7. **Alcance SAFE/SIA 104% (L14) — no tiene contraparte directa en la referencia** (la referencia no abre SAFE/SIA). Se reporta como dato del deck sin par.

---

# Vacíos declarados

1. **Lámina 3 "Pisa HP vs Mercado | VDM IQVIA" — datos NO recuperables.** El render think-cell está guardado como EMF vacío (204 bytes) y no hay tabla asociada legible en el archivo. Se desconoce qué números compara (participación PiSA HP vs total mercado en VDM IQVIA, presumiblemente). **No inventar; hace falta el archivo fuente think-cell o una captura de esa lámina.**
2. **Lámina 1 — bullet truncado:** "…encarece pólizas hasta un **40% en segmentos** [texto cortado en el original]". Falta el complemento de la frase.
3. **Lámina 10 — respuesta a Baxter/Soluciones "Por definir":** el deck declara explícitamente que **no se ha analizado el impacto ni se ha construido el complemento de respuesta** para el frente Baxter. Pendiente real (exógeno) del propio deck.
4. **Lámina 10 — "Cambio de tecnología: Muguerza, Hospitaria, Auna, GASS?"** con signo de interrogación en "GASS?" → cuenta/target **no confirmada** en el original.
5. **Ejes de las burbujas (L8) sin categorías nativas:** python-pptx devolvió `CATEGORIES: []`; las cuentas se leyeron del render y del workbook embebido. El **detalle completo (>400 filas Solicitante×Material con Venta/Uds/Precio 25 y 26)** vive en el workbook embebido `Microsoft_Excel_Worksheet.xlsx` dentro del pptx, no se transcribe entero aquí.
6. **Sin fuentes al pie** en las láminas analíticas (4, 6, 8, 9, 11, 12, 13, 14, 16). Sólo L1 cita fuente (El Economista, 10-may-2026). No se declara la base (SAP sell-in, IQVIA, periodo de corte) de las cifras internas.
7. **Sin speaker notes** en ninguna lámina (revisadas las 16).
8. **Meta anual (FY) por palanca — no explícita:** las barras "Meta 7-12" (L6 Kener $443, L9 Soluciones $267) dan el 2S pero no se declara el supuesto detrás de esas metas.
