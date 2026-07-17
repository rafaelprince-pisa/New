# EXTRACT — Estado de Resultados Farma MX, Junio 2026 (v18.0 "nueva version")

**Archivo fuente (nombre exacto, dobles espacios y doble `.xlsx` incluidos):**
`/Users/rafaelprince/Downloads/Grupo PiSA - Estado de Resultados Jun26 (Farma MX).xlsx  -  version 18.0. 14.07.26 6.33 p.m--- nueva version.xlsx`

- Emisor: Finanzas Grupo PiSA. Tamaño 12.6 MB. Fecha en nombre: 14-jul-2026 6:33 p.m.
- Herramienta: `openpyxl` (read_only, data_only) sobre valores cacheados. **No se modificó el original.** No se requirió recalcular con LibreOffice (todas las celdas relevantes traían valor cacheado; las excepciones se declaran como vacío).
- Existen en Downloads dos versiones previas con nombre casi idéntico (`...6.33 p.m..xlsx` de 13.9 MB, 15-jul; y `...Jun26 (Farma MX).xlsx` de 13.9 MB, 14-jul) que **NO se usaron**. Había también un lockfile `~$...` (archivo abierto en Excel al momento de la extracción).

---

## 0. Resumen de lo más relevante para la tablita L6 del deck

**Segmentación de Finanzas ≠ segmentación del deck.** Finanzas parte Farma MX en **6 bloques**: 5 mercados con venta (Gobierno, Impulso, Hospitales Privados, Farmacias, Expansión) + **1 centro de costo sin venta (SOPORTE)**. El deck usa 4 segmentos (Retail / Gobierno FC / Hospitales / Servicios). El mapeo posible y sus huecos están en §5.

**EBITDA 1S-2026 (Acumulado a junio) por bloque de Finanzas, $M MXN — línea "EBITDA" final (fila 170):**

| Bloque Finanzas | Venta Neta 2026 | EBITDA 2026 | % s/Venta | % del total EBITDA | EBITDA 2025 |
|---|---:|---:|---:|---:|---:|
| Gobierno (01 GOB) | 6,253.7 | 804.8 | 12.9% | 20.7% | 550.1 |
| Impulso (02 IM) | 2,785.8 | 954.5 | 34.3% | 24.6% | 758.7 |
| Hospitales Privados (03 HP) | 3,055.9 | 1,196.8 | 39.2% | 30.8% | 1,071.8 |
| Farmacias (04 F) | 2,958.0 | 962.7 | 32.5% | 24.8% | 914.3 |
| Expansión (05 EXP) | 1,466.4 | 561.9 | 38.3% | 14.5% | 519.9 |
| **SOPORTE (centro de costo, sin venta)** | 0.0 | **-601.1** | n/a | -15.5% | -605.9 |
| **TOTAL FARMA MX** | **16,519.8** | **3,879.6** | **23.5%** | **100.0%** | 3,209.0 |

- Todas las cifras: **$M MXN, Acumulado enero–junio 2026 (1S), cierre a junio; base de comparación = mismo periodo 1S-2025** salvo donde se indique PPTO o PIN.
- Existe una segunda línea de EBITDA, **"EBITDA UN"** (fila 131, antes de "Nuevos Productos"): total 3,941.9; GOB 808.4; IM 956.0; HP 1,198.1; F 964.0; EXP 562.5; SOP -547.1. La diferencia contra EBITDA final (3,879.6) son los "Gastos por Proyectos / Nuevos Productos" (62.3). Ver §4.
- **Corporativo (Grupo) NO está cargado dentro de Farma MX** (filas 134-153 en cero para este archivo). El único bucket de costo compartido dentro de Farma MX es SOPORTE.

---

## 1. Mapa de hojas (23 hojas; 1 visible, 22 ocultas)

| # | Hoja | Filas×Cols | Estado | Contenido |
|---|---|---|---|---|
| 1 | BC | 254×47 | oculta | Listas desplegables y catálogos (Periodo: Acumulado/Anual/Mensual; Medidas: ∑Vta, ∑Gto, ∑Meta_Vta, ∑C1, Costo1; llaves CMATERIAL, GASTO, METACMATERIAL). Parámetros de la herramienta. |
| 2 | DS Gasto | 8,544×379 | oculta | **Data source de gastos SG&A / Corporativo.** Estructura tabular: P&L x Mercado / PAIS / N1..N5 / Año / Valores2 (∑Gto, ∑Gto YTD) / columnas "Suma de FARMA 01..08" (por segmento). Detalle línea a línea. No leído celda por celda (volumen). |
| 3 | Hoja1 | 1×1 | oculta | Vacía. |
| 4 | Gasto Fijo | 665×97 | oculta | Data source de Costo Indirecto (clasificación Fijo/Variable). Estructura CONSOLIDADO / N1 P&L / N2 P&L / Valores2 / Año / "Suma de FARMA 01..08". |
| 5 | DS | 2,610×262 | oculta | **Data source de Venta y Devoluciones.** Estructura División / ID RUN N1..N4 / Año / Valores / columnas 01..06 (por segmento/mes). Cubo base de ventas. |
| 6 | Dicc datos | 175×7 | oculta | **Diccionario de líneas del P&L con clasificación Fijo (CF) / Variable (CV) y justificación en prosa.** Ver §6. |
| 7 | FyV Resumen | 86×35 | oculta | Resumen de Fijos y Variables, "Anualizado (Real+PIN)", comparativos 2025 vs 2023 y 2025 vs AA (año anterior). |
| 8 | Indicadores | 95×112 | oculta | Cartera (responsable Felipe Medeles) y otros indicadores por división/marca (Salud Animal, Electrolit, etc.), series 2021+. |
| 9 | OP | 20×31 | oculta | Bloque "P&L" con EBITDA Meta, Venta Electrolit/FarmaMX/Resto. Contiene varios `#REF!`. Celda viva: Venta FarmaMX = -1,158,471,019.8 (= el VAR de Venta Neta vs PPTO, ver §3). |
| 10 | Dashboard | 42×59 | oculta | **Dashboard Financiero MTD/YTD** por unidad (Grupo PiSA / Electrolit / Farma MX / Farma Internacional / Salud Animal). Muchas celdas `#VALUE!` (dependen de recálculo). Bloques: Crecimiento, Venta Neta, etc. |
| 11 | % Dashboard | 94×36 | oculta | Ratios (%) por bloque y unidad: Logística y Almacenaje, SG&A Com, SG&A Sop, Venta Neta (crecimientos), columnas 01..11. |
| 12 | Tablas | 290×141 | oculta | Tablas dinámicas de apoyo (AJUSTECORPORATIVO y otras), series mensuales 2020+. |
| 13 | Comp elec anual | 220×174 | oculta | P&L anual comparativo de ELECTROLIT (otra unidad). |
| 14 | Comp anual | 210×155 | oculta | P&L anual comparativo GRUPO PISA. |
| 15 | FyV Grupo | 218×145 | oculta | Fijos y Variables a nivel GRUPO PISA. |
| 16 | Grupo | 205×258 | oculta | P&L GRUPO PISA (misma plantilla que FarmaMX). |
| 17 | Elec | 220×258 | oculta | P&L ELECTROLIT (contiene `#REF!` en volumen). |
| 18 | Elec LATAM | 235×311 | oculta | P&L ELECTROLIT LATAM. |
| 19 | **FarmaMX** | **229×258** | **VISIBLE** | **P&L Farma MX, Acumulado a Junio 2026, por 6 segmentos + total. HOJA CENTRAL de esta extracción.** Ver §2–§4. |
| 20 | FarmaINT | 229×258 | oculta | P&L Farma Internacional (misma plantilla). |
| 21 | FarmaINT LATAM | 220×16384 | oculta | P&L Farma Internacional LATAM. |
| 22 | S.Animal | 230×258 | oculta | P&L Salud Animal. |
| 23 | Corporativo | 222×270 | oculta | P&L Corporativo (Grupo). |

> Nota: las hojas 13-23 son la misma plantilla de P&L aplicada a otras unidades de negocio del Grupo. Para el deck de Farma MX la fuente es **FarmaMX** (hoja 19). No se extrajeron celda por celda las hojas de otras unidades (fuera de alcance del deck) ni los data sources DS/DS Gasto/Gasto Fijo (8.5k+ filas).

---

## 2. Estructura de la hoja FarmaMX (la que alimenta el deck)

- **Encabezado (filas 1-5):** fila 1 = "Acumulado"; fila 2 = "Junio" → **todo el P&L es YTD acumulado enero–junio 2026 (1S)**. No hay vista mensual (MTD) por segmento en esta hoja; la vista MTD/YTD agregada por unidad vive en la hoja "Dashboard".
- **Columnas por bloque (patrón repetido para cada segmento):** REAL 2020 · 2021 · 2022 · 2023 · 2024 · 2025 (+ %Vtas) · **2026 REAL (+ %Vtas)** · **VAR vs PPTO (+ %)** · **PPTO 2026 (+ %Vtas)** · **VAR vs PIN (+ %)** · **PIN 2026 (+ %Vtas)** · VAR (+ %).
- **Bloques (segmentos) y su columna 2026-REAL:**

| Código fila 1 | Nombre (fila 3) | Col inicio bloque | Col 2026 REAL | Col %Vtas 2026 | Col PPTO 2026 | Col PIN 2026 |
|---|---|---|---|---|---|---|
| — | FARMA MX (total) | H (8) | P (16) | Q (17) | T (20) | X (24) |
| 01 GOB | GOBIERNO | AC (29) | AK (37) | AL (38) | AO (41) | AS (45) |
| 02 IM | IMPULSO | AX (50) | BF (58) | BG (59) | BJ (62) | BN (66) |
| 03 HP | HOSPITALES PRIVADOS | BS (71) | CA (79) | CB (80) | CE (83) | CI (87) |
| 04 F | FARMACIAS | CN (92) | CV (100) | CW (101) | CZ (104) | DD (108) |
| 05 EXP | EXPANSION | DI (113) | DQ (121) | DR (122) | DU (125) | DY (129) |
| (06) | SOPORTE | ED (134) | EL (142) | EM (143) | EP (146) | ET (150) |

> El código "06" para SOPORTE es inferido (no aparece rótulo numérico en fila 1 para ese bloque; sí aparecen 01-05 para los demás). Las columnas EZ..FG (156+) son un bloque de verificación con valores ~1e-5 (errores de redondeo del cuadre), no datos de segmento.

- **Unidades:** todas las líneas monetarias están en **pesos completos (MXN)**. En este documento se reportan divididas entre 1e6 → **$M MXN**. Las líneas de "% margen" y "%Vtas" ya vienen como proporción (0-1); se reportan como %.
- **"VOLUMEN" (filas 6-10: Saldo inicial, Producción, Venta, Saldo final):** sin valores numéricos cacheados (celdas con texto "dic-24"/"dic-23" como marca de periodo o vacías). **No hay piezas/unidades utilizables en esta hoja** — ver §Vacíos.
- **Etiquetas auxiliares (columnas A, C, D):** cada línea trae su ruta jerárquica (col A, ej. `COGS/Costo Indirecto/Nómina`), su clase costo (col C: CV=Costo Variable, CF=Costo Fijo, VN=Venta Neta) y su tipo (col D: CT=Costo Total, GT=Gasto Total, VN). Hay algunos `#REF!` en col C (filas 85, 90, 105, 108) por referencias rotas en rótulos, no en las cifras.

---

## 3. P&L completo — TOTAL FARMA MX (1S / Acumulado junio, $M MXN)

Columnas: **2025** (1S-2025 real) · **2026** (1S-2026 real) · **%Vtas 2026** (sobre Venta Neta) · **PPTO 2026** (presupuesto/meta 1S) · **PIN 2026** (ver nota de definición al pie).

| Fila | Concepto | 2025 | 2026 | %Vtas | PPTO | PIN |
|---|---|---:|---:|---:|---:|---:|
| 12 | Venta/Ingresos Bruta | 17,857.6 | 17,994.7 | — | 19,080.8 | 37,711.2 |
| 13 | — Manufacturados | 15,047.7 | 15,024.7 | — | 16,235.6 | 31,903.0 |
| 14 | — Comercializados | 2,809.9 | 2,970.0 | — | 2,845.3 | 5,808.2 |
| 15 | Devoluciones y rechazos | -1,024.6 | -849.4 | — | -633.0 | 0.0 |
| 16 | Descuentos | -553.8 | -625.4 | — | -769.5 | -1,634.6 |
| **18** | **VENTA/INGRESOS NETA** | **16,279.2** | **16,519.8** | 100% | **17,678.3** | **36,076.6** |
| 20 | Costo de Ventas | 8,849.7 | 8,507.0 | 51.5% | 9,350.8 | 18,313.2 |
| 21 | — Manufacturados | 7,324.0 | 6,954.9 | 42.1% | 7,912.2 | 15,316.1 |
| 22 | — — Materiales (CD) | 3,174.6 | 2,961.9 | 17.9% | 3,303.8 | 6,728.3 |
| 23 | — — Mano de Obra (CD) | 587.9 | 649.1 | 3.9% | 766.6 | 1,538.3 |
| 24 | — — Maquinaria y energía | 374.9 | 386.5 | 2.3% | 454.9 | 896.0 |
| 25 | — — Costo Indirecto | 2,810.5 | 2,877.4 | 17.4% | 2,957.9 | 5,866.5 |
| 26 | — — — Nómina | 1,409.2 | 1,511.8 | 9.2% | 1,492.4 | 2,969.3 |
| 27 | — — — Laboratorio | 155.6 | 155.2 | 0.9% | 172.5 | 338.8 |
| 28 | — — — Refacc. y H. Mant. | 113.8 | 74.7 | 0.5% | 81.9 | 162.4 |
| 29 | — — — Materiales | 186.7 | 183.3 | 1.1% | 187.3 | 375.7 |
| 30 | — — — Lotes Pruebas | 11.9 | 6.4 | 0.0% | 13.8 | 23.1 |
| 31 | — — — Proyectos | 31.5 | 64.4 | 0.4% | 64.9 | 131.4 |
| 32 | — — — Recuperación de la inversión | 77.6 | 78.8 | 0.5% | 88.2 | 169.4 |
| 33 | — — — Desperdicios PT | 26.6 | 21.3 | 0.1% | 26.7 | 48.9 |
| 34 | — — — D&A (Costo) | 555.9 | 572.4 | 3.5% | 590.4 | 1,169.4 |
| 35 | — — — Resto | 241.7 | 209.1 | 1.3% | 239.7 | 478.1 |
| 36 | — — Variaciones | 376.1 | 80.0 | 0.5% | 428.9 | 287.0 |
| 37 | — — — Variaciones (Línea) | 397.7 | 236.7 | 1.4% | 428.9 | 287.0 |
| 38 | — — — — Var. Línea Compras | 20.7 | 13.3 | 0.1% | 91.3 | 85.8 |
| 39 | — — — — Var. Línea Manufactura | 221.8 | 129.7 | 0.8% | 227.7 | 113.6 |
| 40 | — — — — Desperdicios MP | 155.1 | 93.7 | 0.6% | 110.0 | 87.5 |
| 41 | — — — Variaciones (TC) | -21.5 | -156.7 | -0.9% | 0.0 | 0.0 |
| 42 | — Comercializados | 1,525.7 | 1,552.1 | 9.4% | 1,438.7 | 2,997.1 |
| 43 | — — Costo del producto | 1,479.7 | 1,575.7 | 9.5% | 1,438.7 | 2,997.1 |
| 44 | — — Variaciones (Línea) | 53.6 | -2.9 | -0.0% | 0.0 | 0.0 |
| 45 | — — Variaciones (TC) | -7.6 | -20.6 | -0.1% | 0.0 | 0.0 |
| **47** | **UTILIDAD/PÉRD BRUTA** | **7,429.5** | **8,012.8** | **48.5%** | **8,327.5** | **17,763.4** |
| 48 | — % margen bruto | 45.6% | 48.5% | — | 47.1% | 49.2% |
| 50 | Logística y almacenaje | 2,174.7 | 2,082.3 | 12.6% | 2,031.5 | 4,035.6 |
| 51 | — Fletes | 1,090.8 | 941.0 | 5.7% | 853.9 | 1,703.9 |
| 53 | — — Primario | 291.6 | 241.1 | 1.5% | 215.1 | 432.6 |
| 54 | — — Secundario | 799.2 | 699.9 | 4.2% | 638.9 | 1,271.3 |
| 55 | — — — CABL | 631.0 | 521.7 | 3.2% | 465.3 | 936.1 |
| 56 | — — — Otras sociedades | 168.1 | 178.1 | 1.1% | 173.5 | 335.2 |
| 59 | — Almacenaje | 994.4 | 1,021.0 | 6.2% | 1,057.4 | 2,095.2 |
| 60 | — — Nómina | 448.7 | 503.2 | 3.0% | 449.1 | 900.9 |
| 61 | — — Herramientas de personal | 56.5 | 48.6 | 0.3% | 57.3 | 114.8 |
| 62 | — — Renta y mtto | 166.1 | 163.5 | 1.0% | 211.8 | 425.0 |
| 63 | — — Muestras y salidas ALM | 60.8 | 45.4 | 0.3% | 33.9 | 68.1 |
| 64 | — — Gastos de Empaque | 28.0 | 17.2 | 0.1% | 33.1 | 66.0 |
| 65 | — — Administrativos y Otros | 108.9 | 89.5 | 0.5% | 114.6 | 222.5 |
| 66 | — — Desperdicios PT | 37.6 | 50.5 | 0.3% | 58.9 | 102.0 |
| 67 | — D&A | 87.7 | 103.1 | 0.6% | 98.6 | 196.0 |
| 71 | Soporte Logística | 89.5 | 120.3 | 0.7% | 120.2 | 236.5 |
| 72 | — Nómina | 66.7 | 92.1 | 0.6% | 92.2 | 181.3 |
| 74 | — Gastos Generales | 14.7 | 17.4 | 0.1% | 16.1 | 31.8 |
| **81** | **UTILIDAD/PÉRD MARGINAL** | **5,254.9** | **5,930.5** | **35.9%** | **6,296.0** | **13,727.8** |
| 82 | — % margen marginal | 32.3% | 35.9% | — | 35.6% | 38.1% |
| 84 | Gastos SG&A | 2,760.4 | 2,958.3 | 17.9% | 3,047.8 | 5,179.2 |
| 85 | — Comercial | 1,693.3 | 1,784.6 | 10.8% | 1,753.8 | 3,552.9 |
| 86 | — — Nómina (fijo+social+herr.) | 1,016.2 | 1,105.5 | 6.7% | 1,121.2 | 2,245.4 |
| 87 | — — — Fuerza de Ventas | 644.6 | 688.5 | 4.2% | 693.7 | 1,452.1 |
| 88 | — — — Comisiones+Gratif (variable) | 152.1 | 176.3 | 1.1% | 184.3 | 372.4 |
| 89 | — — — Planeación y Productividad | 69.1 | 66.9 | 0.4% | 74.9 | 151.2 |
| 90 | — — — Servicios Integrales | 150.5 | 173.8 | 1.1% | 168.3 | 269.7 |
| 91 | — — Gasto General Comercial | 677.1 | 679.1 | 4.1% | 632.6 | 1,307.5 |
| 92 | — — — Gastos Generales | 179.2 | 149.9 | 0.9% | 137.4 | 340.6 |
| 93 | — — — Honorarios y asesorías | 24.9 | 49.9 | 0.3% | 38.5 | 74.1 |
| 94 | — — — Gastos de viaje | 53.1 | 34.3 | 0.2% | 55.8 | 110.3 |
| 95 | — — — Mtto equipos médicos | 73.8 | 69.8 | 0.4% | 68.9 | 167.9 |
| 96 | — — — Desperdicios PT | 133.7 | 136.3 | 0.8% | 110.3 | 184.5 |
| 97 | — — D&A | 212.3 | 238.9 | 1.4% | 221.7 | 430.0 |
| 100 | — Marketing | 181.9 | 234.1 | 1.4% | 304.4 | 0.0 |
| 101 | — — Medios (mercadotecnia) | 63.4 | 72.1 | 0.4% | 136.6 | 0.0 |
| 102 | — — Inversión en canales | 47.8 | 37.1 | 0.2% | 58.2 | 0.0 |
| 103 | — — Muestras y promocionales | 70.7 | 124.8 | 0.8% | 109.5 | 0.0 |
| 104 | — Soporte y Administrativos | 626.0 | 684.3 | 4.1% | 687.8 | 1,030.6 |
| 105 | — — Nómina (fijo+social+herr.) | 388.7 | 410.0 | 2.5% | 453.1 | 730.4 |
| 106 | — — — Ejecutivos y Regulatorio | 195.1 | 206.9 | 1.3% | 255.8 | 159.3 |
| 107 | — — — Operaciones | 193.6 | 203.1 | 1.2% | 197.3 | 489.6 |
| 109 | — — Gasto General de Soporte | 237.3 | 274.3 | 1.7% | 234.7 | 300.2 |
| 116 | — Investigación y Desarrollo | 259.2 | 255.4 | 1.5% | 301.9 | 595.7 |
| 117 | — — Nómina (fijo+social+herr.) | 157.3 | 174.2 | 1.1% | 175.9 | 356.4 |
| 118 | — — Gasto General de I&D | 101.9 | 81.1 | 0.5% | 126.0 | 239.3 |
| 120 | — — D&A | 28.4 | 28.5 | 0.2% | 30.7 | 61.4 |
| **124** | **UAFIR UN** | **2,494.4** | **2,972.2** | **18.0%** | **3,248.1** | **8,548.5** |
| 125 | — % margen | 15.3% | 18.0% | — | 18.4% | 23.7% |
| 127 | (+) D&A total (add-back) | 906.9 | 969.8 | 5.9% | 968.7 | 1,903.2 |
| 128 | — D&A (Costo) | 555.9 | 572.4 | 3.5% | 590.4 | 1,169.4 |
| 129 | — D&A (Gasto) | 299.7 | 341.0 | 2.1% | 322.6 | 625.9 |
| 130 | — Arrendamientos Terceros | 51.3 | 56.3 | 0.3% | 55.8 | 107.8 |
| **131** | **EBITDA UN** | **3,401.3** | **3,941.9** | **23.9%** | **4,216.9** | **10,451.7** |
| 132 | — % margen EBITDA UN | 20.9% | 23.9% | — | 23.9% | 29.0% |
| 134-153 | Corporativo (todas las sublíneas) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 155 | UAFIR UN después de Corpo | 2,494.4 | 2,972.2 | 18.0% | 3,248.1 | 8,548.5 |
| 157 | Nuevos Productos | (vacío) | (vacío) | — | (vacío) | (vacío) |
| 158/160 | — Gastos por Proyectos / por capitalizar | 192.4 | 62.3 | 0.4% | 213.4 | 389.2 |
| **162** | **UAFIR** | **2,302.1** | **2,909.8** | **17.6%** | **3,034.7** | **8,159.4** |
| 163 | — % margen UAFIR | 14.1% | 17.6% | — | 17.2% | 22.6% |
| 165 | (+) D&A total (add-back) | 906.9 | 969.8 | 5.9% | 968.7 | 1,903.2 |
| **170** | **EBITDA** | **3,209.0** | **3,879.6** | **23.5%** | **4,003.5** | **10,062.5** |
| 171 | — % margen EBITDA | 19.7% | 23.5% | — | 22.6% | 27.9% |

**Puente sintético (1S-2026, $M):** Venta Bruta 17,994.7 − Devoluciones 849.4 − Descuentos 625.4 = **Venta Neta 16,519.8** − Costo de Ventas 8,507.0 = **Utilidad Bruta 8,012.8 (48.5%)** − Logística y almacenaje 2,082.3 − Soporte Logística 120.3 = **Utilidad Marginal 5,930.5 (35.9%)** − SG&A 2,958.3 = **UAFIR UN 2,972.2 (18.0%)** + D&A add-back 969.8 = **EBITDA UN 3,941.9 (23.9%)** − Nuevos Productos/Proyectos 62.3 → **UAFIR 2,909.8**, y **EBITDA final 3,879.6 (23.5%)**.

> **Definición de columnas de referencia (declaración con incertidumbre):**
> - **PPTO 2026** = presupuesto/meta del 1S (para Venta Neta total = 17,678.3, que coincide exacto con la "meta" del sell-in). Base de comparación válida como "% de plan".
> - **PIN 2026** = cifra de rango anual: los valores son ~2x el semestre (Venta Neta PIN 36,076.6 vs 1S 16,519.8), por lo que **se interpreta como proyección/estimado de cierre de año completo (Real + pendiente)**. La definición exacta del acrónimo "PIN" no está documentada en el archivo y se declara como vacío (§Vacíos). NO usar como comparativo del semestre sin confirmar.

---

## 4. EBITDA y márgenes por segmento (1S-2026, detalle completo)

### 4.1 EBITDA final (fila 170) por bloque — $M MXN

| Bloque | 2025 | **2026** | %Vtas 2026 | PPTO 2026 | PIN 2026 |
|---|---:|---:|---:|---:|---:|
| GOBIERNO | 550.1 | **804.8** | 12.9% | 892.6 | 2,024.5 |
| IMPULSO | 758.7 | **954.5** | 34.3% | 912.8 | 2,080.2 |
| HOSP PRIVADOS | 1,071.8 | **1,196.8** | 39.2% | 1,258.0 | 2,705.0 |
| FARMACIAS | 914.3 | **962.7** | 32.5% | 1,053.3 | 3,173.5 |
| EXPANSIÓN | 519.9 | **561.9** | 38.3% | 626.3 | 1,319.5 |
| SOPORTE | -605.9 | **-601.1** | n/a | -739.6 | -1,240.2 |
| **TOTAL** | **3,209.0** | **3,879.6** | 23.5% | **4,003.5** | **10,062.5** |

### 4.2 EBITDA UN (fila 131, antes de Nuevos Productos) por bloque — $M MXN

| Bloque | 2025 | 2026 | %Vtas 2026 | PPTO 2026 |
|---|---:|---:|---:|---:|
| GOBIERNO | 624.0 | 808.4 | 12.9% | 934.4 |
| IMPULSO | 771.6 | 956.0 | 34.3% | 927.5 |
| HOSP PRIVADOS | 1,092.7 | 1,198.1 | 39.2% | 1,281.6 |
| FARMACIAS | 939.3 | 964.0 | 32.6% | 1,078.1 |
| EXPANSIÓN | 525.8 | 562.5 | 38.4% | 649.3 |
| SOPORTE | -552.1 | -547.1 | n/a | -654.1 |
| **TOTAL** | **3,401.3** | **3,941.9** | 23.9% | **4,216.9** |

### 4.3 Líneas clave del P&L por segmento (1S-2026 REAL, $M MXN)

| Línea | GOB | IM | HP | F | EXP | SOP | TOTAL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Venta Bruta | 6,901.7 | 2,885.7 | 3,153.8 | 3,558.6 | 1,494.8 | — | 17,994.7 |
| Devoluciones y rechazos | -535.2 | -40.4 | -73.4 | -188.5 | -11.8 | — | -849.4 |
| Descuentos | -112.8 | -59.5 | -24.5 | -412.0 | -16.5 | — | -625.4 |
| **Venta Neta** | **6,253.7** | **2,785.8** | **3,055.9** | **2,958.0** | **1,466.4** | **0.0** | **16,519.8** |
| Costo de Ventas | 4,114.4 | 1,621.4 | 1,192.2 | 1,123.4 | 455.7 | 0.0 | 8,507.0 |
| **Utilidad Bruta** | **2,139.3** | **1,164.5** | **1,863.7** | **1,834.6** | **1,010.7** | **0.0** | **8,012.8** |
| — % margen bruto | 34.2% | 41.8% | 61.0% | 62.0% | 68.9% | — | 48.5% |
| Logística y almacenaje | 837.2 | 202.3 | 453.5 | 369.0 | 148.0 | 72.3 | 2,082.3 |
| Soporte Logística | 31.9 | 3.2 | 4.1 | 5.3 | 9.1 | 66.8 | 120.3 |
| **Utilidad Marginal** | **1,302.1** | **962.2** | **1,410.2** | **1,465.6** | **862.7** | **-72.3** | **5,930.5** |
| — % margen marginal | 20.8% | 34.5% | 46.2% | 49.6% | 58.8% | — | 35.9% |
| Gastos SG&A | 846.1 | 134.4 | 417.4 | 645.7 | 411.0 | 503.7 | 2,958.3 |
| **UAFIR UN** | **456.0** | **827.8** | **992.8** | **819.9** | **451.7** | **-576.1** | **2,972.2** |
| — % margen UAFIR UN | 7.3% | 29.7% | 32.5% | 27.7% | 30.8% | — | 18.0% |
| **UAFIR (final)** | **452.4** | **826.3** | **991.5** | **818.6** | **451.1** | **-630.1** | **2,909.8** |
| — % margen UAFIR | 7.2% | 29.7% | 32.5% | 27.7% | 30.8% | — | 17.6% |
| **EBITDA UN** | **808.4** | **956.0** | **1,198.1** | **964.0** | **562.5** | **-547.1** | **3,941.9** |
| — % margen EBITDA UN | 12.9% | 34.3% | 39.2% | 32.6% | 38.4% | — | 23.9% |
| **EBITDA (final)** | **804.8** | **954.5** | **1,196.8** | **962.7** | **561.9** | **-601.1** | **3,879.6** |
| — % margen EBITDA | 12.9% | 34.3% | 39.2% | 32.5% | 38.3% | — | 23.5% |

### 4.4 Indicadores financieros por segmento (filas 179-204, $M MXN salvo %)

| Indicador | GOB | IM | HP | F | EXP | SOP | TOTAL |
|---|---:|---:|---:|---:|---:|---:|---:|
| UAFIR anualizado (a may/a dic, ambos iguales) | 788.8 | 1,468.4 | 1,922.6 | 1,712.1 | 811.6 | -1,281.6 | 5,421.8 |
| NOPAT (utilidad después de impuestos) | 552.2 | 1,027.9 | 1,345.8 | 1,198.5 | 568.1 | -897.1 | 3,795.3 |
| Utilidad Neta | 394.4 | 734.2 | 961.3 | 856.0 | 405.8 | -640.8 | 2,710.9 |
| ROA | 2.4% | 11.1% | 23.0% | 15.2% | 39.0% | -76.9% | 7.9% |
| ROIC | 3.5% | 16.3% | 32.8% | 21.9% | 57.4% | -107.6% | 11.4% |
| Capital invertido | 15,580.3 | 6,300.3 | 4,103.3 | 5,481.1 | 990.3 | 833.7 | 33,289.1 |
| Inventarios | 4,265.4 | 2,691.0 | 2,032.6 | 1,929.4 | 334.1 | 833.7 | 12,086.2 |
| — Inventario MP | 1,929.8 | 1,528.6 | 833.2 | 844.3 | 68.9 | 649.1 | 5,853.9 |
| — Inventario PT | 2,335.6 | 1,162.4 | 1,199.3 | 1,085.1 | 265.1 | 184.6 | 6,232.3 |
| Cuentas por cobrar (cartera) | 4,736.8 | 1,184.7 | 1,478.0 | 2,408.8 | 163.4 | 0.0 | 9,971.7 |
| PP&E | 7,261.8 | 2,726.9 | 668.9 | 1,289.9 | 543.9 | (vacío) | 12,491.4 |
| Intangibles (Software/Marcas) | (vacío) | (vacío) | (vacío) | (vacío) | (vacío) | (vacío) | (vacío) |
| Proveedores | 683.7 | 302.3 | 76.1 | 147.0 | 51.1 | (vacío) | 1,260.2 |

> "UAFIR anualizado a may" = "a dic" (mismo valor 5,421.8) — o ambas celdas apuntan a la misma fórmula, o el anualizado se calcula igual; se reporta el dato tal cual sin resolver (ver Inconsistencias).

---

## 5. Mapeo Finanzas ↔ segmentación del deck (4 segmentos)

**Segmentación de Finanzas (esta fuente):** GOBIERNO · IMPULSO · HOSPITALES PRIVADOS · FARMACIAS · EXPANSIÓN · SOPORTE (centro de costo).

**Segmentación del deck v5:** Retail (43.6%) · Gobierno Frasco Cerrado (24.4%) · Hospitales (18.5%) · Servicios (13.4%).

### Mapeo posible (verificado por aritmética de Venta Neta 1S-2026)

| Segmento deck | = Bloques Finanzas | Venta Neta Finanzas | Venta deck (ref sell-in) | ¿Cuadra? |
|---|---|---:|---:|---|
| **Retail** | Farmacias + Impulso + Expansión | 2,958.0 + 2,785.8 + 1,466.4 = **7,210.2** | 7,210.2 | **Exacto** |
| **Hospitales** | Hospitales Privados | **3,055.9** | 3,054.5 | ~ (Δ +1.4) |
| **Gobierno FC + Servicios** | GOBIERNO (un solo bloque) | **6,253.7** | 4,034.3 + 2,219.4 = 6,253.7 | **Exacto en el combinado** |

- **Retail del deck** = suma limpia de 3 bloques de Finanzas. EBITDA Retail (fila 170) = 962.7 + 954.5 + 561.9 = **2,479.1 $M** (margen 34.4% sobre 7,210.2; 63.9% del EBITDA total). También disponible por línea.
- **Hospitales del deck** = bloque HP de Finanzas directo. EBITDA **1,196.8 $M** (39.2%).
- **HUECO CRÍTICO PARA LA TABLITA L6:** El deck separa **Gobierno FC (4,034.3)** de **Servicios (2,219.4)**, pero **Finanzas NO los separa**: ambos viven dentro del bloque único GOBIERNO (Venta Neta 6,253.7, EBITDA 804.8, margen 12.9%). **No hay en este archivo EBITDA ni márgenes desglosados de "Gobierno Frasco Cerrado" vs "Servicios" por separado.** Solo se dispone del combinado. El split de venta (4,034.3 / 2,219.4) es exógeno (viene del sell-in comercial, no del P&L de Finanzas).
- **SOPORTE (-601.1 EBITDA, sin venta)** no tiene equivalente en la vista de 4 segmentos del deck. Es un bucket de costo compartido no distribuido a mercados. En una tablita L6 de 4 segmentos con venta, este -601.1 $M **queda sin hogar** salvo que se prorratee o se muestre como línea de "no asignado / soporte". Debe decidirse cómo tratarlo para que los EBITDA de segmento sumen el total 3,879.6.

### Reconciliación de EBITDA para la tablita (dos escenarios)

- **Vista Finanzas nativa (6 bloques):** GOB 804.8 · IM 954.5 · HP 1,196.8 · F 962.7 · EXP 561.9 · SOP -601.1 = **3,879.6**. Suma cuadra al 100%.
- **Vista deck (4 segmentos), lo máximo derivable de este archivo:** Retail 2,479.1 · Hospitales 1,196.8 · **Gobierno (FC+Servicios juntos) 804.8** · SOPORTE no asignado -601.1 = 3,879.6. **Servicios NO se puede aislar.**

---

## 6. Diccionario de líneas (hoja "Dicc datos") — clasificación Fijo/Variable

Clasificación de cada línea del P&L para propósitos de gasto operativo SG&A y costo (CF = Costo/Gasto Fijo; CV = Costo/Gasto Variable), con justificación en prosa dentro del archivo. Extracto de las clasificaciones:

- **Costo de Ventas Manufacturados:** Materiales (CD) = **CV**; Mano de Obra (CD) = **CV** (bajo esquema estándar); Maquinaria y energía = **CV**.
- **Costo Indirecto:** Nómina = **CF**; Laboratorio = **CV**; Refacc. y H. Mant. = **CF**; Materiales = **CV**; Lotes Pruebas = **CF**; Proyectos = **CF**; Recuperación de inversión = **CF**; Desperdicios PT = **CV**; D&A (Costo) = **CF**; Resto = **CF**.
- **Variaciones:** Var. Línea Compras = **CV**; Var. Línea Manufactura = **CV**; Desperdicios MP = **CV**; Variaciones (TC) = **CV**.
- **Logística — Fletes** (Interno/Primario/Secundario/CABL/Otras soc/Países) = **CV**.
- **Almacenaje:** Nómina = **CF**; Herramientas de personal = **CF**; Renta y mtto = **CF**; Muestras/salidas = **CV**; Empaque = **CV**; Administrativos = **CF**; Desperdicios PT = **CV**; D&A = **CF**.
- Las columnas C (clase CV/CF/VN) y D (tipo CT/GT/VN) de la hoja FarmaMX replican esta clasificación línea por línea.

---

## Inconsistencias internas

1. **"UAFIR anualizado a mayo" = "UAFIR anualizado a diciembre"** (fila 179 = fila 180 = 5,421.8 total, e idénticas en cada segmento). Dos etiquetas distintas con el mismo valor: o ambas referencian la misma fórmula, o el anualizado no distingue el corte. No resuelto; dato reportado tal cual.
2. **Rótulos con `#REF!`** en columna C de FarmaMX (filas 85 "Comercial", 90 "Servicios Integrales", 105, 108 "Administrativo Fin+RH+Transf") y en la hoja OP (EBITDA Meta, Venta Electrolit, Venta Resto). Son referencias rotas en **etiquetas/celdas de encabezado**, no en las cifras del P&L de Farma MX, que sí traen valor. La línea 108 "Administrativo (Fin+RH+Transf)" está en 0.0 en Real/PPTO pero tiene 81.5 en PIN, lo que sugiere que la nómina administrativa se refleja en otra línea en el acumulado.
3. **Hojas "Dashboard" y varias de otras unidades (Elec, Elec LATAM) traen `#VALUE!` / `#REF!`** en celdas que dependen de recálculo (no cacheadas). No afectan a FarmaMX pero implican que el libro no está totalmente recalculado en disco.
4. **Bloque de verificación EZ..FG (col 156+) de FarmaMX** con valores ~1e-5 a ~-4.7e-5: son residuales de cuadre (deberían ser 0). Confirman que el modelo cuadra a nivel de redondeo, pero el ~-4.7e-5 en "2026Meta" indica un descuadre mínimo esperado, no material.
5. **Corporativo dentro de FarmaMX en cero** (filas 134-153): consistente con que el corporativo del Grupo se lleva en la hoja "Corporativo" aparte; dentro de Farma MX el único costo compartido es SOPORTE. No es error, pero implica que el EBITDA de Farma MX (3,879.6) **no** carga corporativo de Grupo.
6. **Marketing PIN en 0.0** (filas 100-103): las columnas PIN de Marketing están en cero mientras Real/PPTO traen cifras. Posible que el rubro de mercadotecnia no se proyecte en PIN o se reclasifique. Declarado, no resuelto.

## Posibles choques con la referencia sell-in (solo se flagea con ambos números; no se resuelve)

1. **Segmentación distinta (choque estructural, el más importante):** el deck y el sell-in tratan **"Servicios" (2,219.4 $M, 13.4%)** y **"Gobierno Frasco Cerrado" (4,034.3 $M, 24.4%)** como dos segmentos; **Finanzas los tiene fusionados en un solo bloque GOBIERNO (6,253.7 $M)**. Aritmética coincide (4,034.3 + 2,219.4 = 6,253.7), pero el EBITDA/margen de Servicios por separado **no existe** en esta fuente.
2. **Venta total 1S:** sell-in "PISA 5 mercados" = **16,518.5**; Finanzas "Venta Neta" = **16,519.8**. Δ = +1.3 $M (redondeo/definición). Nota conceptual: la referencia lo llama "Venta" y aquí es "Venta Neta" (bruta − devoluciones − descuentos); la Venta **Bruta** de Finanzas es 17,994.7, muy por encima del número del deck — confirmar que el deck usa Venta Neta y no Bruta.
3. **Meta/plan total:** sell-in meta = **17,678.3** = PPTO Venta Neta de Finanzas **17,678.3** (idéntico). % de plan sell-in 93.4% = Finanzas 16,519.8/17,678.3 = 93.4%. Sin choque.
4. **Hospitales:** sell-in **3,054.5** (95.2% de plan, +5.1%) vs Finanzas HP **3,055.9** (95.3% de plan 3,207.1, +5.14% vs 2,906.6). Δ venta +1.4 $M. Sin choque material.
5. **Retail:** sell-in **7,210.2** (92.3%, +0.4%) vs Finanzas F+IM+EXP **7,210.2** (92.3% de plan 7,813.0, +0.44% vs 7,178.5). Coincide.
6. **Gobierno FC vs Servicios metas y crecimientos (no verificables por separado):** el deck da Gobierno FC 90.0% de plan / -0.6%, y Servicios 102.1% / +4.0%. Finanzas solo permite ver el **combinado**: GOBIERNO 6,253.7 / plan 6,658.1 = **93.9%**, +0.96% vs 6,194.1. Los splits 90.0%/-0.6% y 102.1%/+4.0% **no se pueden confirmar ni refutar** con este archivo.
7. **Impulso y Farmacias internos:** Finanzas Impulso +1.79% (2,785.8 vs 2,736.8) y Farmacias **-2.16%** (2,958.0 vs 3,023.3), Expansión +3.38% (1,466.4 vs 1,418.4). El deck reporta Retail agregado +0.4%; el detalle intra-Retail (Farmacias cayendo) es consistente pero no aparece explícito en la referencia dada.
8. **PVM 2 vías (volumen -830.7 / precio+mezcla +1,070.0):** ese puente proviene del sell-in comercial; **este archivo de Finanzas no trae piezas/volumen** (filas VOLUMEN vacías), por lo que el PVM **no es reproducible desde esta fuente**. No hay choque, pero tampoco corroboración.

## Vacíos declarados

1. **Split EBITDA/margen "Gobierno Frasco Cerrado" vs "Servicios":** NO existe en el archivo. Solo GOBIERNO combinado (EBITDA 804.8, margen 12.9%). Es el vacío que más impacta la tablita L6 de 4 segmentos.
2. **Piezas / volumen / unidades:** filas 6-10 "VOLUMEN" (Saldo inicial, Producción, Venta, Saldo final) sin valores numéricos cacheados en FarmaMX (solo marcas de texto "dic-23"/"dic-24" o celdas vacías). No hay base para reconstruir el PVM ni precio/pieza desde esta fuente.
3. **Definición exacta del acrónimo "PIN":** no documentada en el archivo. Por la magnitud (~2x el semestre) se interpreta como proyección de cierre de año completo, pero se declara como no confirmado. No usar PIN como comparativo del semestre sin validar con Finanzas.
4. **Intangibles (Software/Marcas), fila 199:** vacío en todos los segmentos y total.
5. **PP&E y Proveedores de SOPORTE (filas 198, 202):** vacíos (SOP no carga estos rubros).
6. **Pasivos acumulados (fila 203) y Otros Pasivos sin costo (fila 204):** vacíos en todos los segmentos.
7. **Vista mensual (MTD junio) por segmento:** no está en la hoja FarmaMX (es Acumulado YTD). La vista MTD agregada por unidad existe en "Dashboard" pero con celdas `#VALUE!` no cacheadas.
8. **Nombre/código explícito del bloque SOPORTE (¿06?):** inferido; fila 1 no rotula ese bloque con número (sí rotula 01-05 para los demás).
9. **Data sources DS, DS Gasto (8,544 filas), Gasto Fijo:** no extraídos celda por celda por volumen; se mapeó su estructura (§1). Si se requiere el desglose de una línea SG&A/costo por N1..N5 o el detalle de venta por mes, la fuente está en esas hojas y exigiría una segunda pasada dirigida.
10. **Corporativo de Grupo aplicable a Farma MX:** cero en este archivo (§Inconsistencias #5); si el deck necesita EBITDA "después de corporativo de Grupo", ese número no está aquí (vive en la hoja "Corporativo" / consolidado de Grupo, fuera de FarmaMX).
