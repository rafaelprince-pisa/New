# EXTRACT — Puente PVM (Vista Consejo) y Cubos de Down-trading

Frente PVM / down-trading del 14-jul-2026. Tres Excel hermanos en `/Users/rafaelprince/Downloads/`. Extracción fiel y exhaustiva, archivo por archivo y hoja por hoja. No se filtra ni se decide relevancia: el orquestador integra.

Convención de unidades: salvo que se indique lo contrario, **todas las cifras de estos archivos están en PESOS MXN completos** (no en millones). Se anota el equivalente en $M donde ayuda a comparar contra la referencia sell-in del deck (que sí está en $M). Periodo en los tres archivos: **Ene–Jun (meses 01–06), 2025 vs 2026**, cierre a junio.

Referencia sell-in fuente-de-verdad usada para cruzar (1S 2026, cierre junio, $M MXN): PISA 5 mercados 16,518.5 vs meta 17,678.3 = 93.4%, +1.5% vs 1S25; Retail 7,210.2 (Farmacias 2,958.0, Impulso 2,785.8, Expansión 1,466.4) / 92.3% / +0.4%; Gobierno FC 4,034.3 / 90.0% / -0.6%; Hospitales 3,054.5 / 95.2% / +5.1%; Servicios 2,219.4 / 102.1% / +4.0%. PVM 2 vías PISA: volumen -830.7 / precio+mezcla +1,070.0 (piezas -5.1%).

---

## ARCHIVO 1 (PRIORIDAD) — `Puente_PVM_VistaConsejo_5lineas_Ene-Jun_2025_vs_2026.xlsx`

Tamaño 65,929 bytes, 3 hojas. Esta es LA vista para Consejo del puente de ventas.

Aclaración de nombre: "5 líneas" NO se refiere a 5 filas ni a los 4 segmentos del deck. Se refiere a las **5 palancas (columnas)** del puente: Precio, Volumen, Mix, Nuevos Productos, Resto. Hay además dos columnas de conciliación (Devoluciones/Ajustes y Control) más Δ Venta.

Aclaración estructural crítica: el puente está desglosado **por CANAL COMERCIAL de PiSA (10 canales)**, NO por los 4 segmentos (Retail / Gobierno FC / Hospitales / Servicios) que usa la referencia y el storyline v5. Los 10 canales son: HP, AMSA Priv, SIMILARES, Rx, MP, Medicom, FRISO, Consumo, Meditec, FLP. El mapeo canal→segmento no es 1:1 (ver sección de choques).

### Hoja 1.1 — `Vista Consejo` (22 filas × 10 col)

Título: "Puente PVM — Vista Consejo (5 palancas) | Ene–Jun 2025 vs 2026".
Subtítulo: "Reconcilia a Δ Venta por canal. 'Nuevos Productos' = lanzamientos + extensiones comerciales. 'Resto' = expansión de canal + housekeeping de SKU + migración, neteado."

Columnas: `Canal | Precio | Volumen | Mix | Nuevos Productos | Resto (Desarrollo Neto Portafolio) | Devoluciones/Ajustes (no oper.) | Δ Venta | Control`

Tabla completa (pesos MXN):

| Canal | Precio | Volumen | Mix | Nuevos Productos | Resto | Devol./Ajustes | Δ Venta | Control |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HP | 14,051,757.07 | 11,522,270.11 | 60,129,591.77 | 30,005,665.96 | 6,138,277.35 | -10,809,710.85 | 111,037,851.42 | 0 |
| AMSA Priv | 47,561,531.53 | -88,265,459.49 | 122,603,486.73 | 9,079,425.40 | -19,939,444.56 | -522,571.48 | 70,516,968.14 | 0 |
| SIMILARES | 44,665,018.09 | 30,866,264.15 | 16,924,755.40 | 9,821,783.00 | -26,234,620.90 | -78,677,471.47 | -2,634,271.72 | 0 |
| Rx | 111,917,630.45 | -49,288,563.68 | -83,744,138.51 | 19,051,226.53 | 9,945,765.94 | -14,793,458.06 | -6,911,537.33 | 0 |
| MP | 17,857,737.73 | -163,925,683.13 | 117,988,470.62 | 6,714,562.57 | -12,321,225.63 | -21,947,266.13 | -55,633,403.97 | 0 |
| Medicom | 32,622,887.20 | 11,241,669.99 | -11,399,862.16 | 1,663,095.28 | 3,709,947.47 | -60,613.19 | 37,777,124.58 | 0 |
| FRISO | 70,156,384.79 | -110,558,423.40 | -42,021,003.00 | 61,654,133.45 | 13,274,309.65 | -6,357,405.71 | -13,852,004.22 | 0 |
| Consumo | 6,566,103.87 | 39,223,772.76 | -27,345,800.83 | 0.00 | 18,948,256.51 | 4,888,056.19 | 42,280,388.50 | 0 |
| Meditec | 22,877,091.47 | 30,665,826.06 | -21,456,789.29 | 427,014.18 | 3,515,453.55 | -314,022.04 | 35,714,573.93 | 0 |
| FLP | 28,641,494.47 | 74,002,813.09 | -99,756,680.19 | 6,858,334.48 | 4,432,619.24 | 0.00 | 14,178,581.09 | 0 |
| **TOTAL** | **396,917,636.68** | **-214,515,513.54** | **31,922,030.55** | **145,275,240.85** | **1,469,338.62** | **-128,594,462.74** | **232,474,270.42** | **0** |

Equivalentes en $M del TOTAL: Precio +$396.9M · Volumen -$214.5M · Mix +$31.9M · Nuevos Productos +$145.3M · Resto +$1.5M · Devoluciones/Ajustes -$128.6M · **Δ Venta +$232.5M**.

Verificación interna (reproducida): la suma de las 6 palancas iguala exactamente Δ Venta en el TOTAL (232,474,270.42 = 232,474,270.42) y la columna Control = 0 en todos los canales. El puente **cierra perfecto** dentro de este archivo.

Definición de cada palanca (5 líneas Consejo + conciliación):
- **Precio**: efecto de cambio de precio dentro del mismo SKU (Δprecio × unidades), sobre SKU continuos con unidades comparables.
- **Volumen**: crecimiento/caída de unidades (a precio base) de SKU continuos.
- **Mix**: residuo de migración entre presentaciones/marcas dentro del canal (down-trading si negativo) en SKU continuos.
- **Nuevos Productos** = Lanzamientos (molécula nueva a PiSA) + Extensiones comerciales (marca/forma nueva de molécula ya existente).
- **Resto (Desarrollo Neto Portafolio)** = Expansión de canal + Housekeeping de SKU (repack + recodificación + sustitución, neto) + Bajas (todas) + Migración, neteado.
- **Devoluciones/Ajustes (no operativo)**: renglón de conciliación aparte; limpieza de datos, no desarrollo de portafolio.

Desglose 'Nuevos Productos' (TOTAL), al pie de la hoja:
- Lanzamientos (molécula nueva a PiSA): **$128,819,523**
- Extensiones comerciales (marca/forma nueva): **$16,455,718**
- Suma = 145,275,241 = columna Nuevos Productos TOTAL ✓

Desglose 'Resto' (nota literal al pie): "Dentro de 'Resto': Salidas reales de portafolio $-2,086,308 | Expansión de canal $13,976,997 | Housekeeping SKU (repack+recod+sustit, neto) $-12,562,039 | Migración $8,511,600".
- Estos 4 componentes suman **$7,840,250**, NO los $1,469,339 de la columna Resto TOTAL. El desglose de la nota está **incompleto**: para cerrar a Resto TOTAL hay que sumar también Contracción de canal (-$16,615,418) e Indeterminado (+$10,244,507). Reconciliación completa reproducida: 13,976,997 - 12,562,039 - 2,086,308 - 16,615,418 + 10,244,507 + 8,511,600 = 1,469,339 ✓ (ver "Inconsistencias internas").

Nota literal al pie: "Devoluciones/Ajustes −$128,594,463 es no-operativo (dominado por la ruptura de unidades de SIMILARES −$79M). Es limpieza de datos, NO desarrollo de portafolio; por eso va como renglón de conciliación aparte." (En la tabla, SIMILARES tiene Devoluciones/Ajustes = -78,677,471, ~-$78.7M, consistente con el "−$79M".)

### Hoja 1.2 — `Detalle Portafolio` (1,063 filas × 8 col)

Título: "Detalle de Altas/Bajas clasificadas (auditoría)". Es el soporte SKU-por-SKU de las columnas Nuevos Productos y Resto (excluye Precio/Volumen/Mix de SKU continuos, excluye Migración y Devoluciones).

Columnas: `Canal | Alta/Baja | Clasificación | Material | Descripción | Molécula/Marca | Valor (MXN)`
Filas de datos: 1,060 (encabezado en fila 3). Suma total de Valor = **$138,232,979.60**.

Agregado por Alta/Baja:
- Alta: n=664, $252,807,252
- Baja: n=396, $-114,574,272

Agregado por Clasificación (ordenado por |valor|):

| Clasificación | n | Valor (MXN) |
|---|---:|---:|
| Lanzamiento nuevo a PiSA | 98 | 128,819,523 |
| Repack / recodificación | 269 | 83,277,493 |
| Recodificación (misma marca sigue) | 212 | -61,094,195 |
| Sustitución (molécula sigue, marca sale) | 32 | -34,745,337 |
| Contracción de canal | 70 | -16,615,418 |
| Extensión comercial (marca/forma nueva) | 120 | 16,455,718 |
| Expansión de canal | 150 | 13,976,997 |
| Indeterminado | 51 | 10,244,507 |
| Salida real de PiSA | 58 | -2,086,308 |

Cruce reproducido de esta hoja contra Vista Consejo:
- Lanzamiento 128,819,523 + Extensión comercial 16,455,718 = 145,275,241 = Nuevos Productos TOTAL ✓
- Housekeeping (Repack 83,277,493 + Recodificación -61,094,195 + Sustitución -34,745,337) = -12,562,039 = componente "Housekeeping" de la nota Resto ✓
- Suma total Detalle 138,232,980 = Nuevos Productos (145,275,241) + [Expansión 13,976,997 + Housekeeping -12,562,039 + Salida -2,086,308 + Contracción -16,615,418 + Indeterminado 10,244,507 = -7,042,261]. La Migración (+8,511,600) NO está en esta hoja (es ajuste externo al detalle), por eso Detalle (138.2M) + Migración (8.5M) ≈ Nuevos Productos + Resto = 146.7M. Consistente.

Agregado por Canal (de esta hoja de detalle; ordenado por |valor|):

| Canal | n | Valor (MXN) |
|---|---:|---:|
| FRISO | 7 | 74,928,443 |
| HP | 156 | 29,143,517 |
| Rx | 41 | 28,996,992 |
| Consumo | 5 | 18,948,257 |
| SIMILARES | 13 | -16,769,098 |
| FLP | 209 | 11,190,355 |
| AMSA Priv | 26 | -10,860,019 |
| MP | 138 | -6,660,453 |
| Medicom | 234 | 5,372,780 |
| Meditec | 231 | 3,942,205 |

Top registros individuales (muestra literal, para dar textura de qué mueve el número):
- AMSA Priv · Baja · Sustitución (molécula sigue, marca sale) · Material 4043287 · "AM INSULINA GLAR 100UI C/1FCO NVAIM" · INSULINA GLARGINA · -$23,178,656.76
- FRISO · Alta · Lanzamiento nuevo a PiSA · Material 4064294 · "FRISOLAC GOLD 2 1.2KG LN" · FRISOLAC GOLD 2 · +$21,824,625.63
- FRISO · Alta · Lanzamiento nuevo a PiSA · Material 4064300 · "FRISOLAC GOLD 1 1.2KG LN" · FRISOLAC GOLD 1 · +$18,623,551.27

### Hoja 1.3 — `Notas método` (15 filas × 2 col)

Título: "Vista Consejo — método de clasificación de Altas/Bajas". Contenido literal:
- Ancla = familia terapéutico-comercial: molécula canónica (Diccionario_PISA_SKUs.csv) y, para molecule-less (soluciones/dispositivos/nutrición), la marca.
- Referencia = PiSA consolidada (los 10 canales), año 2025, para distinguir lo nuevo-a-PiSA de lo que sólo cambia de canal.
- ALTAS se parten en: Lanzamiento (familia sin venta en ningún canal 2025) · Extensión comercial (molécula ya en el canal, marca/forma nueva) · Expansión de canal (familia en otro canal) · Repack/recodificación (misma marca ya en el canal) · Indeterminado.
- BAJAS: Salida real (sale de todo PiSA) · Contracción de canal · Sustitución (molécula sigue, marca sale) · Recodificación (misma marca sigue) · Indeterminado.
- 'Nuevos Productos' (línea Consejo) = Lanzamientos + Extensiones. 'Resto' = Expansión de canal + Repack + Bajas (todas) + Migración, neteado. Devoluciones/Ajustes va aparte (no-operativo).
- **PENDIENTE FASE 2** (refinan la clasificación, no disponibles hoy con el semestre + diccionario):
  - Maestro de fechas de lanzamiento — para no marcar como lanzamiento 2026 algo que salió a mediados de 2025.
  - Estatus de discontinuación — para separar salida real de desabasto/estacionalidad/rezago de facturación (hoy 'salida' = cero venta 2026, es proxy).
  - Linaje regulatorio — un biosimilar/genérico nuevo puede ser lanzamiento estratégico aunque comparta INN; hoy cae en 'Extensión'.
  - Maestro de conversión de unidades (gramos/ml/dosis) — para repacks 800g→1.2kg y para el Precio/Volumen de FRISO/nutrición/HP soluciones.
  - Resolver la ruptura de datos de SIMILARES (−$79M en Ajustes): ¿caída real o quiebre de captura de unidades?

---

## ARCHIVO 2 — `Downtrading_por_Segmento_Cubo_Ene-Jun_2025_vs_2026.xlsx`

Tamaño 111,704 bytes, 4 hojas. Down-trading por molécula, cortado **por SEGMENTO** (los 4 segmentos del deck), desde el cubo Sell-In-2023-2026-Cierre-JUN.xlsx (hoja MER-CAN-PROD). Es DIAGNÓSTICO: **NO reconcilia al Δ total**; cobertura parcial por segmento.

### Hoja 2.1 — `Resumen por Segmento` (13 filas × 10 col)

Título: "Down-trading por molécula, por segmento — desde el cubo (cierre-JUN), Ene–Jun 2025 vs 2026".
Subtítulo: "La venta migra dentro de la misma molécula hacia presentaciones/marcas de menor valor. Descompuesto a nivel molécula (el único nivel donde las unidades son comparables)."

Columnas: `Segmento | Venta 2025 | Venta 2026 | Δ Venta | Precio | Volumen | Mix (down-trading) | Cobertura | # moléculas`

Tabla completa (pesos MXN; Cobertura como fracción; # moléculas entero):

| Segmento | Venta 2025 | Venta 2026 | Δ Venta | Precio | Volumen | Mix (down-trading) | Cobertura | # mol |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Privado | 7,176,828,518.86 | 7,208,511,016.74 | 31,682,497.88 | 139,494,532.32 | -128,887,621.63 | -155,288,526.55 | 0.6369 (63.7%) | 183 |
| Hospitales | 2,900,270,395.16 | 3,050,729,363.34 | 150,458,968.18 | -43,300,447.63 | 85,935,558.42 | -7,371,178.75 | 0.4200 (42.0%) | 209 |
| Gob Frasco Cerrado | 4,059,222,660.84 | 4,034,326,413.30 | -24,896,247.54 | -147,494,764.60 | 97,336,590.53 | 112,817,783.66 | 0.5530 (55.3%) | 225 |
| Gob Servicios | 2,134,859,229.02 | 2,219,381,679.96 | 84,522,450.94 | -136,634,553.94 | 330,013,322.74 | -261,308,131.70 | 0.1823 (18.2%) | 94 |

Equivalentes Venta 2026 en $M: Privado $7,208.5M · Hospitales $3,050.7M · Gob FC $4,034.3M · Gob Servicios $2,219.4M. Total cubo 2026 = **$16,512.9M**.

Verificación interna (reproducida):
- Δ Venta = Venta2026 − Venta2025 en los 4 segmentos ✓ (Privado +31,682,497.88; Hospitales +150,458,968.18; Gob FC -24,896,247.54; Gob Servicios +84,522,450.94).
- **Precio + Volumen + Mix ≠ Δ Venta** (por diseño, cobertura parcial). Ej. Privado: 139,494,532 - 128,887,622 - 155,288,527 = -144,681,616 ≠ +31,682,498. Los efectos P/V/M se calculan solo sobre las moléculas cubiertas; el Δ Venta es del segmento total. El propio archivo lo declara: "NO reconcilia al Δ total".

Lectura literal al pie: "el down-trading se concentra en PRIVADO (tu negocio comercial). Hospitales es estable; Gob Frasco Cerrado sube de gama; Gob Servicios muestra caída fuerte en oncológicos pero con cobertura baja (18%) y unidades de biológicos dudosas — leer con reserva."

CAVEATS literales al pie: "diagnóstico a nivel molécula; cubre solo pharma con gramaje legible (cobertura por segmento arriba); NO reconcilia al Δ total. Excluye molecule-less (soluciones ml, nutrición). La descomposición volumen/mix a nivel segmento NO es válida (pooling de unidades heterogéneas explota) — por eso se hace por molécula."

### Hoja 2.2 — `Ranking Franquicias` (714 filas × 13 col)

Título: "Ranking de franquicias por down-trading (Mix), por segmento". Una fila por combinación molécula×segmento, ordenada por Mix (más negativo = mayor down-trading) arriba.

Columnas: `Segmento | Molécula | Venta 2025 | Venta 2026 | Δ Venta | Precio | Volumen | Mix (down-trade) | % Δ precio | #SKU | Bandera`
(La "Bandera" toma el valor "revisar unidades" cuando aplica; muchas filas la traen.)

Top 19 down-traders (Mix más negativo), literal:

| # | Segmento | Molécula | Venta 2025 | Venta 2026 | Δ Venta | Precio | Volumen | Mix | %Δprecio | #SKU | Bandera |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Gob Servicios | PEMBROLIZUMAB | 131,482,416 | 71,070,700 | -60,411,716 | -3,647,585 | 155,958,950 | -212,723,081 | -75.3% | 5 | revisar unidades |
| 2 | Privado | ACIDO CLAVULANICO + AMOXICILINA | 188,416,296 | 214,410,870 | 25,994,574 | 2,049,785 | 74,817,068 | -50,872,279 | -20.8% | 55 | revisar unidades |
| 3 | Privado | CEFTRIAXONA | 374,821,068 | 328,251,931 | -46,569,137 | -10,323,266 | -1,639,943 | -34,605,927 | -11.5% | 54 | |
| 4 | Privado | LEVOFLOXACINO | 95,782,640 | 58,157,271 | -37,625,369 | -4,303,599 | -99,570 | -33,222,200 | -38.3% | 20 | |
| 5 | Gob Servicios | TRASTUZUMAB | 44,065,779 | 35,148,593 | -8,917,186 | -1,268,622 | 21,927,322 | -29,575,886 | -48.3% | 35 | revisar unidades |
| 6 | Privado | PROBIOTICO | 5,180,978 | 10,500,705 | 5,319,727 | 274,989 | 33,408,235 | -28,363,497 | +10.8% | 5 | revisar unidades |
| 7 | Gob Servicios | BRENTUXIMAB VEDOTIN | 18,211,792 | 24,109,960 | 5,898,168 | 1,062,387 | 29,934,716 | -25,098,935 | -49.9% | 9 | revisar unidades |
| 8 | Gob Frasco Cerrado | OMEPRAZOL | 40,876,158 | 35,902,655 | -4,973,503 | -1,330,449 | 20,680,334 | -24,323,388 | -41.6% | 13 | revisar unidades |
| 9 | Privado | ENOXAPARINA DE SODIO | 98,702,248 | 107,584,452 | 8,882,204 | 14,813,293 | 14,134,162 | -20,065,251 | -5.5% | 8 | revisar unidades |
| 10 | Gob Servicios | DARATUMUMAB | 8,046,000 | 3,045,077 | -5,000,923 | -2,806,391 | 16,404,323 | -18,598,855 | -88.4% | 16 | revisar unidades |
| 11 | Gob Servicios | NIVOLUMAB | 18,414,075 | 6,389,548 | -12,024,527 | -16,158 | 5,762,560 | -17,770,929 | -74.0% | 20 | revisar unidades |
| 12 | Gob Frasco Cerrado | CEFTRIAXONA | 79,118,547 | 87,549,885 | 8,431,338 | -1,217,693 | 21,971,164 | -12,322,133 | -13.4% | 19 | revisar unidades |
| 13 | Privado | ARIPIPRAZOL | 24,111,265 | 28,535,892 | 4,424,627 | -94,165 | 15,926,828 | -11,408,036 | -27.1% | 13 | revisar unidades |
| 14 | Privado | PANTOPRAZOL | 109,070,954 | 94,698,976 | -14,371,978 | -3,310,520 | -2,553,482 | -8,507,976 | -12.8% | 48 | |
| 15 | Privado | CEFALEXINA | 81,372,360 | 85,040,963 | 3,668,604 | 7,656,993 | 4,020,982 | -8,009,371 | +0.6% | 18 | revisar unidades |
| 16 | Privado | FEXOFENADINA | 74,926,403 | 81,074,614 | 6,148,212 | 3,539,026 | 10,509,728 | -7,900,542 | -3.8% | 22 | revisar unidades |
| 17 | Gob Servicios | RITUXIMAB | 10,111,239 | 8,423,406 | -1,687,833 | -2,014,907 | 8,138,909 | -7,811,835 | -62.2% | 92 | revisar unidades |
| 18 | Privado | CIPROFLOXACINO | 62,780,017 | 65,820,491 | 3,040,475 | 5,308,013 | 5,512,416 | -7,779,954 | -5.3% | 24 | revisar unidades |
| 19 | Gob Servicios | CLORHIDRATO DE DOXORUBICINA | 4,644,766 | 1,030,962 | -3,613,804 | 100,604 | 3,201,230 | -6,915,638 | -84.9% | 65 | revisar unidades |

Observación: los mayores down-traders por Mix en Gob Servicios (Pembrolizumab, Trastuzumab, Brentuximab, Daratumumab, Nivolumab, Rituximab, Doxorubicina) están **todos marcados "revisar unidades"** — consistente con el caveat de biológicos/oncológicos de cobertura y unidades dudosas. El down-trading "limpio" (sin bandera) está en el Privado: CEFTRIAXONA (-34.6M) y LEVOFLOXACINO (-33.2M), y PANTOPRAZOL (-8.5M).

### Hoja 2.3 — `Detalle Top Franquicias` (256 filas × 10 col)

Título: "Detalle: hacia dónde migra el volumen (top 15 down-traders)". Muestra, para cada franquicia top, SKU por SKU la caída de la presentación cara y el alza de la barata.

Columnas: `Segmento/Molécula | Marca/Descripción | Unid 2025 | Precio 2025 | Venta 2025 | Unid 2026 | Precio 2026 | Venta 2026 | Δ Venta`
Estructura de bloques: fila de cabecera con "Segmento · MOLÉCULA" (trae Venta2025/Venta2026/ΔVenta agregados), seguida de filas SKU.

Ejemplo literal PEMBROLIZUMAB (Gob Servicios), cabecera Venta2025 131,482,416 / Venta2026 71,070,700 / Δ -60,411,716:
- KEYTRUDA 100MG/4ML: Unid 459.72→8, Precio $171,646.83→$167,502.25, Venta 78,909,482→1,340,018, Δ -77,569,464
- PEMBROLIZUMAB KEYTRUDA 100MG/4ML GOB: Unid 396.04→552.52, Precio $132,746.53→$126,204.81, Venta 52,572,934→69,730,682, Δ +17,157,748

Ejemplo literal ACIDO CLAVULANICO + AMOXICILINA (Privado), cabecera Venta2025 188,416,296.31 / Venta2026 214,410,870.41. La caída de presentaciones caras (AMOXICLAV BID 875/125 C/14, AMOXICLAV 500/125 C/15, PHARM 875/125) se compensa con alza de baratas de SIMILARES (AM GRAMAXIN 500/125 C/10 +$16.4M; AM AMOXICILIN/CLAV 875/125 10TAB +$8.2M; AM GRAMAXIN 250/62.5/5ml 60ml +$5.3M). Es el patrón de down-trading de marca de valor → marca económica dentro de la misma molécula.

### Hoja 2.4 — `Notas método` (15 filas × 2 col)

Título: "Down-trading por segmento desde el cubo — método y caveats". Contenido literal:
- FUENTE: Sell-In-2023-2026-Cierre-JUN.xlsx (cubo crudo, cierre a junio), hoja MER-CAN-PROD. Molécula NATIVA (100% cobertura). Ene-Jun (meses 01-06) 2025 vs 2026.
- SEGMENTOS: Privado = Mercado{Farmacias, Impulso, Expansión}; Hospitales = Mercado HP; Gob Frasco Cerrado = Gobierno & Canal 'FC Gob'; Gob Servicios = Gobierno & Canal 'Servicios Gob'. Mapeo exacto, cero filas sin clasificar.
- POR QUÉ A NIVEL MOLÉCULA Y NO SEGMENTO: "La descomposición volumen/mix con un solo factor de crecimiento sobre un segmento entero NO es válida: suma 'piezas' de miles de productos heterogéneos y explota (Gob Servicios daba Volumen -2,670M / Mix +2,665M). El nivel correcto es la molécula, donde las unidades sí son comparables (normalizadas a mg-equivalente)."
- MÉTODO: por molécula (nativa), unidades a mg-eq. Precio = Σ(Δprecio/mg)×unid26 dentro de SKU; Volumen = crecimiento de mg; Mix = residuo = migración entre presentaciones/marcas (down-trading si <0).
- CAVEATS: (a) DIAGNÓSTICO, no reconcilia al Δ total; cobertura por segmento en Resumen (64% Privado … 18% Gob Servicios). (b) Gob Servicios (oncológicos/biológicos): cobertura baja y unidades dudosas (mg vs piezas en licitación); franquicias marcadas 'revisar unidades' tienen Mix mayor que su propio Δ venta — leer con reserva. (c) 8 SKUs con cambio de unidad de medida entre años (ej. 4064138 SOL CS: 18 → 306,479 piezas, mismo valor) fueron aislados; distorsionan cualquier cálculo por unidad. (d) Fase siguiente para el puente completo reconciliado: maestro de conversión de unidades SAP (incl. soluciones ml y nutrición gramos) y normalización de biológicos.

---

## ARCHIVO 3 — `Downtrading_Moleculas_Ene-Jun_2025_vs_2026.xlsx`

Tamaño 75,744 bytes, 4 hojas. Down-trading por molécula **cruzando los 10 canales** (no cortado por segmento). Es la vista que "cose" la caída de la presentación cara con el alza de la barata a través de canales. También es DIAGNÓSTICO, **NO reconcilia al Δ total ($232.5M)**.

### Hoja 3.1 — `Resumen` (13 filas × 7 col)

Título: "Down-trading por molécula — Ene–Jun 2025 vs 2026".
Subtítulo: "Diagnóstico: la venta migra dentro de la misma molécula hacia presentaciones/marcas/canales de menor valor."

Tres KPIs (formato etiqueta | valor | glosa), literal:
- **Precio (dentro de SKU)**: **$69,409,006** — "Aguanta / sube: no estamos bajando precios de lista."
- **Volumen (mg de molécula)**: **$43,143,962** — "Los mg de principio activo se sostienen."
- **MIX = DOWN-TRADING**: **$-187,257,651** — "La venta se abarata por mezcla. Aquí está la fuga de valor."

Suma de los tres efectos (neto de moléculas cubiertas): 69,409,006 + 43,143,962 - 187,257,651 = **-74,704,683** (esto NO es el Δ total; es el neto de la cobertura del diagnóstico).

Textos literales al pie:
- "Down-trading bruto (mix<0): $-307M en 111 moléculas | compensado por +$119M donde subimos de gama." (-307 + 119 ≈ -188 ≈ Mix -187.3M ✓)
- "Cobertura del diagnóstico: 195 moléculas pharma con gramaje parseable. NO reconcilia al Δ total ($232.5M) — excluye soluciones/nutrición y SKU sin concentración legible. El puente completo reconciliado es la fase siguiente."
- "La paradoja para el Consejo: el pricing es POSITIVO; el valor se pierde por el mix hacia lo barato. La palanca no es precio de lista — es defender la mezcla (marca de valor, canal de valor)."

### Hoja 3.2 — `Ranking Franquicias` (198 filas × 11 col)

Título: "Ranking de franquicias por down-trading (Efecto Mix, mg-equivalente)". Una fila por molécula (agregada a través de canales), ordenada por Mix.

Columnas: `Molécula | Venta 2025 | Venta 2026 | Δ Venta | Efecto Precio | Efecto Volumen | Efecto Mix (down-trade) | % Δ precio realiz. | #SKU | #Canales`

Top 19 (Mix más negativo), literal:

| # | Molécula | Venta 2025 | Venta 2026 | Δ Venta | Precio | Volumen | Mix | %Δprecio | #SKU | #Can |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | ACIDO CLAVULANICO + AMOXICILINA | 187,157,534 | 212,844,106 | 25,686,572 | 3,435,729 | 77,390,343 | -55,139,500 | -21.9% | 83 | 8 |
| 2 | CEFTRIAXONA | 407,687,721 | 354,200,891 | -53,486,830 | -8,563,951 | 3,684,522 | -48,607,401 | -13.3% | 87 | 8 |
| 3 | LEVOFLOXACINO | 126,399,388 | 85,333,488 | -41,065,900 | -5,166,457 | -468,387 | -35,431,056 | -31.4% | 43 | 8 |
| 4 | ENOXAPARINA DE SODIO | 150,013,846 | 174,973,167 | 24,959,322 | 17,267,859 | 27,867,409 | -20,175,946 | -2.5% | 25 | 7 |
| 5 | ARIPIPRAZOL | 24,159,704 | 28,819,181 | 4,659,478 | -373,434 | 16,288,574 | -11,255,662 | -27.2% | 28 | 7 |
| 6 | CIPROFLOXACINO | 80,493,752 | 84,198,382 | 3,704,630 | 5,277,532 | 7,897,594 | -9,470,495 | -6.2% | 47 | 8 |
| 7 | FEXOFENADINA | 74,718,049 | 80,797,973 | 6,079,924 | 3,496,414 | 10,621,290 | -8,037,780 | -4.0% | 37 | 8 |
| 8 | CEFALEXINA | 81,198,747 | 84,106,301 | 2,907,554 | 7,344,796 | 3,553,410 | -7,990,651 | +0.2% | 30 | 8 |
| 9 | MOMETASONA | 43,385,590 | 40,728,528 | -2,657,062 | 724,701 | 3,872,050 | -7,253,813 | -13.8% | 25 | 8 |
| 10 | PARACETAMOL | 110,842,494 | 105,315,637 | -5,526,857 | -4,513,528 | 6,150,297 | -7,163,626 | -7.5% | 31 | 8 |
| 11 | PANTOPRAZOL | 116,633,635 | 100,724,217 | -15,909,418 | -6,446,131 | -3,064,783 | -6,398,504 | -13.1% | 85 | 9 |
| 12 | METOTREXATO | 9,411,297 | 11,761,590 | 2,350,293 | -2,041,107 | 10,750,347 | -6,358,948 | -17.1% | 10 | 4 |
| 13 | OMEPRAZOL | 84,903,197 | 84,941,885 | 38,688 | -1,736,812 | 8,099,326 | -6,323,826 | -8.6% | 20 | 7 |
| 14 | CIPROFIBRATO | 18,191,480 | 20,032,524 | 1,841,044 | 408,145 | 7,103,762 | -5,670,863 | -20.8% | 13 | 8 |
| 15 | HIDROCLOROTIAZIDA + TELMISARTAN | 105,393,581 | 146,121,394 | 40,727,812 | 7,777,497 | 38,274,934 | -5,324,618 | +1.6% | 37 | 8 |
| 16 | MOXIFLOXACINO | 12,827,734 | 12,228,300 | -599,434 | 173,612 | 4,241,546 | -5,014,592 | -22.6% | 14 | 6 |
| 17 | CITALOPRAM | 12,052,436 | 16,085,423 | 4,032,987 | 154,191 | 8,777,051 | -4,898,255 | -22.8% | 11 | 6 |
| 18 | DONEPECILO | 27,333,604 | 29,439,599 | 2,105,995 | 1,844,544 | 5,016,193 | -4,754,742 | -7.7% | 10 | 7 |
| 19 | ZOLMITRIPTAN | 7,131,229 | 9,393,041 | 2,261,812 | 815,740 | 6,099,322 | -4,653,251 | -29.0% | 11 | 8 |

Nota: esta vista cross-canal NO trae oncológicos/biológicos en el top (a diferencia del cubo por segmento), porque el guarda anti-explosión excluye moléculas con |Volumen| o |Mix| > 4× su venta. El top aquí es antibióticos/genéricos de alto volumen: CEFTRIAXONA (-48.6M), LEVOFLOXACINO (-35.4M), AC. CLAVULÁNICO+AMOXICILINA (-55.1M).

### Hoja 3.3 — `Detalle Top Franquicias` (518 filas × 12 col)

Título: "Detalle: hacia dónde migra el volumen (top 20 franquicias en down-trading)".
Subtítulo: "Cada franquicia, SKU por SKU y canal por canal. Se ve la caída de la presentación cara y el alza de la barata."

Columnas: `Molécula | Canal | Marca | Descripción | Unid 2025 | Precio 2025 | Venta 2025 | Unid 2026 | Precio 2026 | Venta 2026 | Δ Venta`
Estructura de bloques: cabecera con MOLÉCULA (trae Venta2025/Venta2026 y Mix como Δ Venta de la cabecera), seguida de filas SKU con su Canal y Marca.

Ejemplo literal ACIDO CLAVULANICO + AMOXICILINA (cabecera Venta2025 187,157,534 / Venta2026 212,844,106 / Mix -55,139,500). Muestra el patrón cross-canal: caen presentaciones caras de Rx (AMOXICLAV BID 875/125 C/14, AMOXICLAV 500/125 C/15) y MP (PHARM/F AHO 875/125), suben las económicas de SIMILARES (AM GRAMAXIN 500/125 C/10 $14.6M→$31.1M, +$16.4M; AM AMOXICILIN/CLAV 875/125 10TAB $16.9M→$28.7M, +$11.7M) y AMSA Priv (GRAMAXIN 500/125 C/12 +$3.2M). Cada SKU trae Unid, Precio unitario y Venta ambos años.

### Hoja 3.4 — `Notas método` (12 filas × 2 col)

Título: "Down-trading por molécula — método y caveats". Contenido literal:
- Unidad de análisis: la MOLÉCULA cruzando los 10 canales (no el canal). Así se conecta la caída de la presentación cara con el alza de la barata, que un puente por canal parte y no reconcilia.
- Unidades normalizadas a mg-equivalente (gramaje×unidades) para que sumar 1g y 500mg sea comparable y el factor de volumen no explote.
- Descomposición por molécula: Precio = Σ(Δ precio por mg)×unid26 dentro de cada SKU · Volumen = crecimiento de mg de la molécula a precio base · Mix = residuo = migración entre presentaciones/marcas/canales.
- Mix negativo = down-trading (la venta migra a lo barato). Mix positivo = premiumización.
- CAVEATS (por eso es DIAGNÓSTICO, no el puente final): (a) Cobertura: solo moléculas pharma con gramaje parseable de la descripción; excluye soluciones (ml), nutrición (gramos de fórmula) y SKU con concentración no legible. (b) No reconcilia al Δ total ($232.5M); el puente molécula completo y reconciliado requiere normalizar esos grupos y coser re-códigos dentro de molécula. (c) El parseo de concentración es heurístico; combinaciones y concentraciones/ml pueden quedar aproximadas; el ranking de las grandes franquicias es robusto. (d) Guardas anti-explosión: se excluye una molécula si |Volumen| o |Mix| > 4× su venta (señal de unidad aún no comparable o re-código sin coser).

---

## Cómo se relacionan los tres archivos (mapa de método)

- **Archivo 1 (Vista Consejo)** es el ÚNICO que reconcilia al Δ Venta ($232.5M). Cortado por **canal (10)**. Separa Nuevos Productos, Resto (portafolio) y Devoluciones del efecto Precio/Volumen/Mix de SKU continuos. Es el puente "oficial" para el Consejo.
- **Archivo 2 (por Segmento)** y **Archivo 3 (por Molécula cross-canal)** son DIAGNÓSTICOS de down-trading que **no reconcilian** (cobertura parcial de pharma con gramaje legible). Existen para responder "¿dónde está la fuga de valor por mezcla?" a nivel molécula, donde las unidades sí son comparables. El Archivo 2 lo corta por los 4 segmentos del deck; el Archivo 3 lo cose por molécula a través de canales.
- La "columna Mix" significa cosa distinta en cada archivo: en Vista Consejo es Mix de SKU continuos dentro de canal (+$31.9M neto); en los diagnósticos es el residuo de down-trading a nivel molécula (-$187.3M cross-canal / mezcla por segmento). No son la misma magnitud ni comparables directamente.

---

## Inconsistencias internas

1. **Desglose 'Resto' incompleto en la nota de Vista Consejo.** La nota al pie lista 4 componentes (Salidas -2,086,308 | Expansión +13,976,997 | Housekeeping -12,562,039 | Migración +8,511,600) que suman **$7,840,250**, pero la columna Resto TOTAL es **$1,469,339**. Faltan en la nota Contracción de canal (-$16,615,418) e Indeterminado (+$10,244,507). Con esos dos, cierra: 13,976,997 - 12,562,039 - 2,086,308 - 16,615,418 + 10,244,507 + 8,511,600 = 1,469,339. La nota no es errónea en sus cifras, es incompleta como reconciliación de Resto.

2. **Efectos Precio/Volumen/Mix distintos entre los dos diagnósticos de down-trading, para la misma molécula.** Ej. AC. CLAVULÁNICO+AMOXICILINA: en el cubo por segmento (solo Privado) Mix = -50,872,279; en la vista cross-canal (molécula) Mix = -55,139,500. CEFTRIAXONA: Privado -34,605,927 (segmento) vs -48,607,401 (cross-canal, incluye Gob FC -12.3M + otros). Es esperado (distinto alcance: un segmento vs los 10 canales), pero implica que **no se pueden sumar ni citar de forma intercambiable**. Los totales de efectos también difieren: cubo por segmento (suma de 4) Precio -$187.9M / Volumen +$384.3M / Mix -$311.2M; molécula cross-canal Precio +$69.4M / Volumen +$43.1M / Mix -$187.3M.

3. **Precio+Volumen+Mix no cierra a Δ Venta en el cubo por segmento** (por diseño y cobertura parcial; el propio archivo lo declara). Documentado, no es error, pero hay que evitar presentarlos como puente que cuadra.

4. **Venta 2026 del cubo por segmento vs Venta 2026 del Vista Consejo por canal**: no son directamente sumables al mismo total porque uno es cubo crudo por segmento y el otro es el universo de canales del puente. El cubo suma $16,512.9M; el Vista Consejo no publica un total de venta 2026 (solo deltas). No hay choque numérico verificable entre ambos aquí, solo distinta base.

---

## Posibles choques con la referencia sell-in (solo flagear, ambos lados)

1. **Total Δ / crecimiento PISA 1S.** Tres números de "delta total" coexisten y no empatan:
   - Vista Consejo Δ Venta TOTAL = **+$232.5M**.
   - Referencia PVM 2 vías, neto = precio+mezcla +1,070.0 + volumen -830.7 = **+$239.3M**.
   - Referencia +1.5% sobre 16,518.5 implica 2025 = 16,274.4 → Δ = **+$244.1M**.
   Brecha máx ~$11.6M entre extremos ($232.5M vs $244.1M).

2. **Descomposición P/V/M irreconciliable entre el puente y la referencia PVM 2 vías.**
   - Referencia: precio+mezcla **+$1,070.0M** ; volumen **-$830.7M** (piezas -5.1%).
   - Vista Consejo: Precio +$396.9M + Mix +$31.9M = **+$428.8M** (precio+mezcla) ; Volumen **-$214.5M**.
   Brecha ~$641M en precio+mezcla y ~$616M en volumen. Se explica porque el puente aísla Nuevos Productos (+$145.3M), Resto (+$1.5M) y Devoluciones (-$128.6M), y sus P/V/M solo aplican a SKU continuos con unidades comparables; la referencia 2 vías lo mete todo en 2 cubetas. Aun así, **son dos descomposiciones distintas del mismo semestre** y hay que decidir cuál cuenta la historia al Consejo sin contradecir la otra.

3. **Venta 2026 por segmento: cubo vs referencia (todo en $M).**
   - Privado/Retail: cubo **7,208.5** vs referencia Retail **7,210.2** → Δ -1.7M.
   - Hospitales: cubo **3,050.7** vs referencia **3,054.5** → Δ -3.8M.
   - Gob FC: cubo **4,034.3** vs referencia **4,034.3** → empata.
   - Gob Servicios: cubo **2,219.4** vs referencia Servicios **2,219.4** → empata.
   - Total: cubo **16,512.9** vs referencia PISA 5 mercados **16,518.5** → Δ -5.6M. Diferencias menores (<0.1%), probablemente redondeo/alcance del cubo crudo vs el reporte, pero se dejan flageadas.

4. **Signo del Δ por segmento: coherencia direccional.**
   - Gob FC: cubo Δ Venta **-$24.9M** (negativo) ↔ referencia Gob FC **-0.6%** (negativo) → coherente.
   - Hospitales: cubo Δ **+$150.5M** ↔ referencia **+5.1%** → coherente (150.5/2,900.3 = +5.2%).
   - Servicios: cubo Δ **+$84.5M** ↔ referencia **+4.0%** (84.5/2,134.9 = +4.0%) → coherente.
   - Privado/Retail: cubo Δ **+$31.7M** (+0.44%) ↔ referencia Retail **+0.4%** → coherente.
   No hay choque de signo; las magnitudes % implícitas del cubo empatan bien con la referencia.

5. **Estructura de corte incompatible con el storyline v5.** El deck y la referencia organizan por **4 segmentos** (Retail 43.6% / Gob FC 24.4% / Hospitales 18.5% / Servicios 13.4%). El puente que reconcilia (Vista Consejo) está por **10 canales comerciales** (HP, AMSA Priv, SIMILARES, Rx, MP, Medicom, FRISO, Consumo, Meditec, FLP). No hay en estos archivos un mapeo canal→segmento, así que el puente que cuadra ($232.5M) no se puede repartir directo a los 4 bloques del deck sin una tabla de correspondencia adicional (el cubo por segmento sí está por segmento, pero ese no reconcilia). Es el gap operativo #1 para armar la lámina PVM por segmento.

---

## Vacíos declarados

1. **El puente que reconcilia ($232.5M) está por canal, no por segmento.** No existe en estos archivos una tabla canal→segmento para pasar el bridge Vista Consejo a los 4 bloques del deck. Sin ese mapeo, no se puede afirmar "el PVM del segmento X" con el número que cuadra.

2. **Migración +$8,511,600 (dentro de Resto) no tiene soporte SKU-por-SKU** en la hoja Detalle Portafolio (esa hoja suma $138.2M y excluye Migración). Es un ajuste declarado sin auditoría visible en el archivo.

3. **Devoluciones/Ajustes -$128.6M es "no operativo" y no está desglosado por causa.** Se sabe que -$78.7M viene de la "ruptura de unidades de SIMILARES", pero el archivo no separa cuánto es devolución real vs quiebre de captura. Pendiente Fase 2 declarado.

4. **Cobertura parcial de los diagnósticos de down-trading** (declarada): Privado 63.7%, Gob FC 55.3%, Hospitales 42.0%, Gob Servicios 18.2% en el cubo por segmento; 195 moléculas pharma con gramaje parseable en la vista molécula. Excluye molecule-less (soluciones ml, nutrición gramos) y SKU con concentración no legible. El down-trading reportado (-$187.3M cross-canal) es piso, no total.

5. **Gob Servicios (oncológicos/biológicos) con unidades dudosas.** Toda la parte alta de su ranking está marcada "revisar unidades" (mg-eq vs piezas de licitación). El archivo pide leer ese segmento con reserva; el Mix -$261.3M / -$212.7M de Pembrolizumab pueden ser artefacto de unidad, no down-trading real.

6. **8 SKUs con cambio de unidad de medida entre años** (ej. Material 4064138 SOL CS: 18 → 306,479 piezas mismo valor) fueron aislados por distorsionar el cálculo por unidad. No se cuantifica su impacto agregado en el archivo.

7. **Fase 2 pendiente (declarada en Notas método del Archivo 1):** maestro de fechas de lanzamiento, estatus de discontinuación, linaje regulatorio, maestro de conversión de unidades SAP (gramos/ml/dosis), y resolución de la ruptura de SIMILARES. Hasta tenerlos, la clasificación Altas/Bajas y el Precio/Volumen de FRISO/nutrición/soluciones son proxy.

8. **Ninguno de los tres archivos trae meta/plan ni % de cumplimiento.** Solo 2025 vs 2026 real. El 93.4% vs meta de la referencia no se puede validar contra estos archivos.
