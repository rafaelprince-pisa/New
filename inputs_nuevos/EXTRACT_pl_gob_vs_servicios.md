# EXTRACT — P&L Gobierno FC vs Servicios (split del bloque GOBIERNO)

**Archivo fuente:** `/Users/rafaelprince/Downloads/PL Gobierno vs Servicios.xlsx`
**Extraído:** 2026-07-16 · openpyxl 3.1.5 (read_only, data_only) · pandas 2.3.3
**Hoja única:** `Sheet1` (rango A1:AQ132, 3,890 celdas con valor, **0 fórmulas** — todo son valores duros; no requirió recálculo en LibreOffice).
**Periodo:** Acumulado a **Junio** (1S) — encabezado F1="Acumulado", F2="Junio". Columnas históricas = YTD-junio de cada año.
**Segmento:** GOBIERNO (I1="01 GOB", I3="GOBIERNO"). Es el P&L del bloque único GOBIERNO de Finanzas, ahora **partido en dos columnas — FC y Servicios — más 4 sub-líneas de Servicios**.
**Unidades:** MXN nominales (celdas al peso). En este documento las tablas van en **$M** (millones) salvo que se indique al peso. Márgenes en % sobre Venta Neta del propio bloque.
**Corte de EBITDA de este archivo:** llega hasta **"EBITDA UN" (fila 131)** — es decir, **antes de "Nuevos Productos / Proyectos"**. No incluye la fila 170 "EBITDA final" del Estado de Resultados v18. Este punto es determinante para el cuadre (ver §5 y §7).

---

## 1. Estructura de la hoja y mapa de columnas

Una sola hoja. Bloque izquierdo (I:AB) = P&L combinado de GOBIERNO en serie de tiempo + PPTO + PIN. Bloque derecho (AD:AQ) = **el split nuevo**: FC/Servicios y las 4 sub-líneas de Servicios, solo REAL, 2026 vs 2025.

### 1.1 Bloque combinado (serie histórica + presupuesto + plan)

| Col | Contenido | Año / escenario |
|---|---|---|
| I, J, K, L, M | REAL | 2020, 2021, 2022, 2023, 2024 (YTD-jun) |
| N | % s/Vtas | 2024 |
| **O** | **REAL** | **2025 (YTD-jun) — comparativo del split** |
| P | % s/Vtas | 2025 |
| **Q** | **REAL** | **2026 (YTD-jun) = GOBIERNO combinado, el dato vivo** |
| R | % s/Vtas | 2026 |
| S / T | VAR / % | Q − O (real 2026 vs real 2025) |
| U | PPTO | 2026 (1S) |
| V | % s/Vtas | PPTO |
| W / X | VAR / % | Q − U (real vs presupuesto) |
| Y | PIN | 2026 (plan anual; ≈2.1× el semestre) |
| Z | % s/Vtas | PIN |
| AA / AB | VAR / % | vs PIN |

### 1.2 Bloque split (lo nuevo) — REAL, solo 2026 y 2025

| Col | Bloque / sub-línea | Año |
|---|---|---|
| **AD** | Servicios — **DP** (Diálisis Peritoneal) | 2026 |
| **AF** | Servicios — **SAFE** | 2026 |
| **AG** | Servicios — **SANEFRO** | 2026 |
| **AH** | Servicios — **SIA** | 2026 |
| **AI** | **Gobierno FC** (Frasco Cerrado) | 2026 |
| **AJ** | **Servicios** (= DP+SAFE+SANEFRO+SIA) | 2026 |
| AK | DP | 2025 |
| AM | SAFE | 2025 |
| AN | SANEFRO | 2025 |
| AO | SIA | 2025 |
| **AP** | **Gobierno FC** | 2025 |
| **AQ** | **Servicios** | 2025 |

> Nota: las columnas AE y AL están vacías de datos de P&L (separadores). En la banda de encabezado, la fila 2 guarda participaciones (AD2=11.76%, AF2=14.16%, AG2=8.72%, AH2=0.85% — cada sub-línea como % de la Venta Neta total de GOBIERNO; suman 35.49% = Servicios/GOBIERNO). La celda **AE1=38.22%** no reconcilia con ninguna base corriente probada (Serv/GOB VN=35.49%, Serv/GOB EBITDA=40.03%, Serv/GOB UB=42.14%); se declara **artefacto de encabezado sin fuente confirmada** (ver §Vacíos).

### 1.3 Correspondencia probable de nombres (NO verificada en el archivo)

El archivo solo trae los rótulos literales **DP, SAFE, SANEFRO, SIA**. Contra el lenguaje del proyecto ("HD/DP/mezclas/SIA"), la lectura más plausible es:
- **DP** = Diálisis Peritoneal (negocio de producto: bolsas/soluciones DP).
- **SANEFRO** = servicio de hemodiálisis / clínicas de nefrología (el "HD"). Margen bruto 66.6%, sin logística, SG&A comercial pesado → perfil de servicio en clínica.
- **SAFE** = probable línea de mezclas / nutrición / producto (tiene COGS y logística altos).
- **SIA** = Servicio (perfil idéntico a SANEFRO: 66.6% bruto, sin logística).

Esta correspondencia es inferencia por estructura de costos, **no** está rotulada en la fuente. Reportar los nombres literales al Consejo.

---

## 2. P&L resumen — combinado, FC y Servicios (1S-2026 vs 1S-2025), $M

| Línea | GOB 2026 | GOB 2025 | **FC 2026** | FC 2025 | **Serv 2026** | Serv 2025 |
|---|---:|---:|---:|---:|---:|---:|
| Venta/Ingresos Bruta | 6,901.7 | 7,029.3 | 4,682.4 | 4,894.5 | 2,219.4 | 2,134.9 |
| — Manufacturados | 5,917.7 | 6,084.5 | 5,917.7 | 6,084.5 | 0.0 | 0.0 |
| — Comercializados | 984.1 | 944.8 | 984.1 | 944.8 | 0.0 | 0.0 |
| — Devoluciones y rechazos | −535.2 | −732.3 | −535.2 | −732.3 | 0.0 | 0.0 |
| — Descuentos | −112.8 | −103.0 | −112.8 | −103.0 | 0.0 | 0.0 |
| **VENTA NETA** | **6,253.7** | **6,194.1** | **4,034.3** | **4,059.2** | **2,219.4** | **2,134.9** |
| Costo de Ventas | 4,114.4 | 4,189.9 | 2,796.5 | 2,853.0 | 1,317.9 | 1,337.0 |
| **UTILIDAD BRUTA** | **2,139.3** | **2,004.1** | **1,237.8** | **1,206.3** | **901.5** | **797.9** |
| — **% margen bruto** | **34.21%** | 32.36% | **30.68%** | 29.72% | **40.62%** | 37.37% |
| Logística y almacenaje | 837.2 | 986.4 | 620.2 | 737.0 | 217.0 | 249.3 |
| Soporte Logística | 31.9 | 27.5 | 23.6 | 20.3 | 8.3 | 7.1 |
| **UTILIDAD MARGINAL** | **1,302.1** | **1,017.8** | **617.6** | **469.3** | **684.5** | **548.5** |
| — % margen marginal | 20.82% | 16.43% | 15.31% | 11.56% | 30.84% | 25.69% |
| Gastos SG&A | 846.1 | 740.8 | 443.0 | 364.4 | 403.1 | 376.3 |
| — Comercial | 549.9 | 492.1 | 245.6 | 204.4 | 304.3 | 287.7 |
| — Soporte y Administrativos | 259.7 | 233.2 | 167.5 | 150.4 | 92.2 | 82.8 |
| — Investigación y Desarrollo | 16.3 | 10.4 | 10.5 | 6.7 | 5.8 | 3.7 |
| **UAFIR UN** | **456.0** | **277.0** | **174.7** | **104.8** | **281.4** | **172.2** |
| — % margen UAFIR | 7.29% | 4.47% | 4.33% | 2.58% | 12.68% | 8.07% |
| (+) D&A add-back | 352.4 | 346.9 | 310.1 | 304.4 | 42.3 | 42.5 |
| **EBITDA UN** | **808.4** | **624.0** | **484.8** | **409.2** | **323.6** | **214.7** |
| — **% margen EBITDA** | **12.93%** | 10.07% | **12.02%** | 10.08% | **14.58%** | 10.06% |

**Cifras exactas al peso (líneas críticas):**
- EBITDA UN 2026 — GOB `808,399,881.46` = FC `484,779,834.37` + Servicios `323,620,047.09` (cuadre exacto).
- EBITDA UN 2025 — GOB `623,956,295.98` = FC `409,240,320.78` + Servicios `214,715,975.20` (cuadre exacto).
- Venta Neta 2026 — GOB `6,253,705,988.41` = FC `4,034,326,413.30` + Servicios `2,219,379,575.11`.
- Venta Neta 2025 — GOB `6,194,081,889.86` = FC `4,059,222,660.84` + Servicios `2,134,859,229.02`.

### 2.1 Crecimiento YoY (1S-2026 vs 1S-2025)

| Línea | FC | Servicios |
|---|---|---|
| Venta Neta | −0.6% (4,059.2 → 4,034.3) | **+4.0%** (2,134.9 → 2,219.4) |
| Utilidad Bruta | +2.6% | +13.0% |
| **EBITDA UN** | **+18.5%** (409.2 → 484.8) | **+50.7%** (214.7 → 323.6) |
| Margen bruto | +96 pb (29.72% → 30.68%) | +325 pb (37.37% → 40.62%) |
| Margen EBITDA | +194 pb (10.08% → 12.02%) | **+452 pb** (10.06% → 14.58%) |

**Lectura:** Servicios crece la venta (+4.0%) y expande margen con fuerza (EBITDA 10.06% → 14.58%). FC cae en venta (−0.6%) pero mejora margen (10.08% → 12.02%), en parte por reasignación de costos comerciales hacia Servicios (ver §7). El motor de rentabilidad del bloque GOBIERNO en 1S-2026 es **Servicios**.

---

## 3. Servicios — desglose por sub-línea (1S-2026), $M

| Línea | Servicios | DP | SAFE | SANEFRO | SIA |
|---|---:|---:|---:|---:|---:|
| Venta Neta 2026 | 2,219.4 | 735.4 | 885.6 | 545.3 | 53.1 |
| — % de GOBIERNO VN | 35.49% | 11.76% | 14.16% | 8.72% | 0.85% |
| Costo de Ventas | 1,317.9 | 483.8 | 634.2 | 182.1 | 17.7 |
| **Utilidad Bruta** | **901.5** | **251.6** | **251.4** | **363.2** | **35.4** |
| — % margen bruto | 40.62% | 34.21% | 28.38% | **66.61%** | **66.61%** |
| Logística y almacenaje | 217.0 | 98.5 | 118.6 | **0.0** | **0.0** |
| SG&A total | 403.1 | 61.4 | 63.1 | 255.9 | 22.8 |
| — de la cual, SG&A Comercial | 304.3 | 28.7 | 24.0 | 231.1 | 20.4 |
| **EBITDA UN** | **323.6** | **127.9** | **74.4** | **108.6** | **12.7** |
| — **% margen EBITDA** | **14.58%** | **17.40%** | **8.40%** | **19.92%** | **23.91%** |

**Sub-líneas 2025 (EBITDA UN, $M / margen):** DP 36.7 (5.50%) · SAFE 87.2 (9.42%) · SANEFRO 68.1 (14.15%) · SIA 22.7 (37.28%). Suma = 214.7.

**Dos modelos de negocio dentro de Servicios:**
- **DP y SAFE = producto** (bolsas/soluciones): tienen COGS de materiales/mano de obra + logística (fletes, almacenaje). Margen bruto 34% / 28%; EBITDA 17.4% / 8.4%. SAFE es el eslabón débil — su EBITDA **cayó** 87.2 → 74.4 $M YoY (−14.7%) pese a ser la sub-línea de mayor venta (885.6 $M).
- **SANEFRO y SIA = servicio** (clínica/aplicación): margen bruto ~66.6%, **cero logística**, pero SG&A comercial altísimo (SANEFRO gasta 231.1 $M comercial sobre 545.3 $M de venta = 42.4%). EBITDA 19.9% / 23.9%.

---

## 4. Verificación de cuadre INTERNO (aritmética del split)

Se verificó fila por fila (rows 12–132) en las líneas en pesos. **Resultado: cuadre exacto (delta 0.00) en TODAS las líneas de importe.**

| Prueba | Resultado |
|---|---|
| FC (AI) + Servicios (AJ) = GOBIERNO 2026 (Q) | ✅ Exacto en todas las líneas (Venta Bruta, Neta, Costo, U. Bruta, U. Marginal, SG&A, UAFIR, EBITDA UN) |
| FC (AP) + Servicios (AQ) = GOBIERNO 2025 (O) | ✅ Exacto en todas las líneas |
| DP+SAFE+SANEFRO+SIA (AD+AF+AG+AH) = Servicios (AJ) | ✅ Exacto en todas las líneas (delta 0.00) |
| Sub-líneas 2025 = Servicios 2025 | ✅ Exacto |

Los únicos "deltas" aparecen en las filas de **% margen** (48, 82, 125, 132), y son esperados: los porcentajes no son aditivos (cada columna muestra su propio margen sobre su propia venta, no se suman). **No es un error.**

**Conclusión:** El split es internamente consistente al 100%. Las cifras de FC y Servicios reconstruyen exactamente el bloque GOBIERNO que ya conocíamos.

---

## 5. Cuadre CONTRA referencias externas

### 5.1 Contra el Estado de Resultados v18 (`EXTRACT_edo_resultados_jun26_v18.md`)

El v18 tiene **dos líneas de EBITDA** para GOBIERNO:

| Concepto v18 | GOB 2026 | GOB 2025 |
|---|---:|---:|
| **EBITDA UN** (fila 131) | **808.4** | **624.0** |
| **EBITDA final** (fila 170, tras "Nuevos Productos/Proyectos") | **804.8** | **550.1** |

| Prueba | Este archivo | v18 | Veredicto |
|---|---:|---:|---|
| Venta Neta GOB 2026 | 6,253.7 | 6,253.7 | ✅ **OK exacto** |
| **EBITDA UN** GOB 2026 | **808.4** | **808.4** | ✅ **OK exacto** (delta 0.0) |
| EBITDA UN GOB 2025 | 624.0 | 624.0 | ✅ OK exacto |
| **EBITDA final** GOB 2026 | **808.4** (solo hay UN) | **804.8** | ⚠️ **DESVIACIÓN +3.6 $M** |
| EBITDA final GOB 2025 | 624.0 (solo hay UN) | 550.1 | ⚠️ **DESVIACIÓN +73.9 $M** |

**El hallazgo clave:** este split **llega solo hasta EBITDA UN (808.4)**. La tablita L6 del deck y el v18 usan **EBITDA final (804.8)**, que resta la línea "Nuevos Productos / Proyectos". Esa resta vale **3.6 $M en 2026 y 73.9 $M en 2025** para GOBIERNO, y **el archivo NO la reparte** entre FC y Servicios. Por lo tanto:

> **FC 484.8 + Servicios 323.6 = 808.4 (EBITDA UN), NO 804.8 (EBITDA final).** Si la tablita mezcla este split (nivel UN) con los demás segmentos a nivel final, el total sube a ~3,883.2 en vez de 3,879.6. Hay que decidir dónde cargar los 3.6 $M (ver §7 y Vacíos).

### 5.2 Contra el sell-in comercial (referencia del deck)

| Bloque | Este archivo (Venta Neta 2026) | Sell-in referencia | Veredicto |
|---|---:|---:|---|
| Gobierno FC | 4,034.3 | 4,034.3 | ✅ **OK exacto** |
| Servicios | 2,219.4 | 2,219.4 | ✅ **OK exacto** |
| — YoY FC | −0.6% | −0.6% | ✅ coincide |
| — YoY Servicios | +4.0% | +4.0% | ✅ coincide |

**La frontera de este P&L es la Venta NETA, y coincide al peso con el sell-in (4,034.3 / 2,219.4).** No es "otra frontera": el split usa exactamente la misma partición que el sell-in comercial. La famosa diferencia **~$835M del universo neto NO aparece aquí** — este archivo vive en el universo Venta Neta = sell-in, no expone el puente hacia el otro universo. (El único puente visible es Bruta→Neta: 6,901.7 − 535.2 devol − 112.8 desc = 6,253.7, que es 648.0 $M, no 835 $M; concepto distinto.)

Los % de cumplimiento de plan del deck (FC 90.0%, Servicios 102.1%) **no se pueden verificar** con este archivo: el split no trae PPTO/PIN por bloque, solo REAL 2026 y 2025.

---

## 6. Sub-líneas — detalle P&L completo (apéndice fiel, $M)

Todas las líneas etiquetadas (filas 12–132), columnas GOB/FC/Servicios 2026 + las 4 sub-líneas 2026 + GOB/FC/Servicios 2025. Reproducción fiel de la fuente.

| Row | Línea | GOB26 | FC26 | Serv26 | DP26 | SAFE26 | SANE26 | SIA26 | GOB25 | FC25 | Serv25 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | Venta/Ingresos Bruta | 6,901.7 | 4,682.4 | 2,219.4 | 735.4 | 885.6 | 545.3 | 53.1 | 7,029.3 | 4,894.5 | 2,134.9 |
| 13 | Manufacturados | 5,917.7 | 5,917.7 | 0.0 | — | — | — | — | 6,084.5 | 6,084.5 | 0.0 |
| 14 | Comercializados | 984.1 | 984.1 | 0.0 | — | — | — | — | 944.8 | 944.8 | 0.0 |
| 15 | Devoluciones y rechazos | −535.2 | −535.2 | 0.0 | — | — | — | — | −732.3 | −732.3 | 0.0 |
| 16 | Descuentos | −112.8 | −112.8 | 0.0 | — | — | — | — | −103.0 | −103.0 | 0.0 |
| 18 | **VENTA NETA** | 6,253.7 | 4,034.3 | 2,219.4 | 735.4 | 885.6 | 545.3 | 53.1 | 6,194.1 | 4,059.2 | 2,134.9 |
| 20 | Costo de Ventas | 4,114.4 | 2,796.5 | 1,317.9 | 483.8 | 634.2 | 182.1 | 17.7 | 4,189.9 | 2,853.0 | 1,337.0 |
| 21 | — Manufacturados | 3,506.6 | 2,598.7 | 907.9 | 412.4 | 295.7 | 182.1 | 17.7 | 3,632.2 | 2,898.4 | 733.8 |
| 22 | — — Materiales | 1,552.7 | 1,001.7 | 551.0 | 182.6 | 219.9 | 135.4 | 13.2 | 1,599.1 | 1,031.6 | 567.5 |
| 23 | — — Mano de Obra | 342.8 | 221.1 | 121.6 | 40.3 | 48.5 | 29.9 | 2.9 | 291.3 | 187.9 | 103.4 |
| 24 | — — Maquinaria y energía | 192.8 | 124.4 | 68.4 | 22.7 | 27.3 | 16.8 | 1.6 | 177.4 | 114.5 | 63.0 |
| 25 | — Costo Indirecto | 1,379.9 | 879.1 | 500.8 | 162.3 | 338.5 | 0.0 | 0.0 | 1,379.8 | 863.9 | 515.8 |
| 26 | — — Nómina | 725.0 | 301.3 | 423.8 | 85.3 | 338.5 | 0.0 | 0.0 | 691.8 | 256.9 | 434.9 |
| 27 | — — Laboratorio | 74.4 | 65.7 | 8.8 | 8.8 | 0.0 | 0.0 | 0.0 | 76.4 | 67.4 | 9.0 |
| 28 | — — Refacc. y H. Mant. | 35.8 | 31.6 | 4.2 | 4.2 | 0.0 | 0.0 | 0.0 | 55.9 | 49.3 | 6.6 |
| 29 | — — Materiales | 87.9 | 77.6 | 10.3 | 10.3 | 0.0 | 0.0 | 0.0 | 91.7 | 80.9 | 10.8 |
| 30 | — — Lotes Pruebas | 3.0 | 2.7 | 0.4 | 0.4 | 0.0 | 0.0 | 0.0 | 5.9 | 5.2 | 0.7 |
| 31 | — — Proyectos | 30.9 | 27.3 | 3.6 | 3.6 | 0.0 | 0.0 | 0.0 | 15.5 | 13.6 | 1.8 |
| 32 | — — Recuperación de la inversión | 37.8 | 33.3 | 4.4 | 4.4 | 0.0 | 0.0 | 0.0 | 38.1 | 33.6 | 4.5 |
| 33 | — — Desperdicios PT | 10.2 | 9.0 | 1.2 | 1.2 | 0.0 | 0.0 | 0.0 | 13.1 | 11.5 | 1.5 |
| 34 | — — D&A (Costo) | 274.5 | 242.2 | 32.3 | 32.3 | 0.0 | 0.0 | 0.0 | 272.9 | 240.8 | 32.1 |
| 35 | — — Resto | 100.3 | 88.5 | 11.8 | 11.8 | 0.0 | 0.0 | 0.0 | 118.7 | 104.7 | 14.0 |
| 36 | — Variaciones | 38.4 | 33.9 | 4.5 | 4.5 | 0.0 | 0.0 | 0.0 | 184.7 | 162.9 | 21.7 |
| 42 | — Comercializados (costo) | 607.8 | 536.3 | 71.5 | 71.5 | 0.0 | 0.0 | 0.0 | 557.7 | 492.2 | 65.6 |
| 47 | **UTILIDAD BRUTA** | 2,139.3 | 1,237.8 | 901.5 | 251.6 | 251.4 | 363.2 | 35.4 | 2,004.1 | 1,206.3 | 797.9 |
| 48 | — % margen bruto | 34.21% | 30.68% | 40.62% | 34.21% | 28.38% | 66.61% | 66.61% | 32.36% | 29.72% | 37.37% |
| 50 | Logística y almacenaje | 837.2 | 620.2 | 217.0 | 98.5 | 118.6 | 0.0 | 0.0 | 986.4 | 737.0 | 249.3 |
| 51 | — Fletes | 484.2 | 358.7 | 125.5 | 56.9 | 68.6 | 0.0 | 0.0 | 593.1 | 439.4 | 153.7 |
| 59 | — Almacenaje | 321.1 | 237.9 | 83.2 | 37.8 | 45.5 | 0.0 | 0.0 | 365.8 | 277.3 | 88.5 |
| 71 | Soporte Logística | 31.9 | 23.6 | 8.3 | 3.8 | 4.5 | 0.0 | 0.0 | 27.5 | 20.3 | 7.1 |
| 81 | **UTILIDAD MARGINAL** | 1,302.1 | 617.6 | 684.5 | 153.1 | 132.8 | 363.2 | 35.4 | 1,017.8 | 469.3 | 548.5 |
| 82 | — % margen marginal | 20.82% | 15.31% | 30.84% | 20.82% | 15.00% | 66.61% | 66.61% | 16.43% | 11.56% | 25.69% |
| 84 | Gastos SG&A | 846.1 | 443.0 | 403.1 | 61.4 | 63.1 | 255.9 | 22.8 | 740.8 | 364.4 | 376.3 |
| 85 | — Comercial | 549.9 | 245.6 | 304.3 | 28.7 | 24.0 | 231.1 | 20.4 | 492.1 | 204.4 | 287.7 |
| 87 | — — Fuerza de Ventas | 108.2 | **−72.0** | 180.2 | 23.0 | 17.7 | 139.5 | 0.0 | 103.1 | **−58.4** | 161.5 |
| 90 | — — Servicios Integrales | 154.1 | 154.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 133.9 | 133.9 | 0.0 |
| 91 | — — Gasto General Comercial | 279.7 | 170.3 | 109.4 | 5.7 | 6.4 | 91.6 | 5.8 | 247.9 | 133.7 | 114.1 |
| 92 | — — — Gastos Generales | 75.3 | **−34.1** | 109.4 | 5.7 | 6.4 | 91.6 | 5.8 | 106.1 | **−7.3** | 113.4 |
| 95 | — — Mtto equipos médicos | 42.6 | 42.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 43.0 | 43.0 | 0.0 |
| 100 | — Marketing | 20.2 | 19.3 | 0.9 | 0.2 | 0.0 | 0.7 | 0.0 | 5.1 | 2.9 | 2.2 |
| 104 | — Soporte y Administrativos | 259.7 | 167.5 | 92.2 | 30.5 | 36.8 | 22.6 | 2.2 | 233.2 | 150.4 | 82.8 |
| 116 | — Investigación y Desarrollo | 16.3 | 10.5 | 5.8 | 1.9 | 2.3 | 1.4 | 0.1 | 10.4 | 6.7 | 3.7 |
| 124 | **UAFIR UN** | 456.0 | 174.7 | 281.4 | 91.8 | 69.7 | 107.3 | 12.6 | 277.0 | 104.8 | 172.2 |
| 125 | — % margen UAFIR | 7.29% | 4.33% | 12.68% | 12.48% | 7.87% | 19.68% | 23.67% | 4.47% | 2.58% | 8.07% |
| 127 | (+) D&A total add-back | 352.4 | 310.1 | 42.3 | 36.2 | 4.7 | 1.3 | 0.1 | 346.9 | 304.4 | 42.5 |
| 131 | **EBITDA UN** | **808.4** | **484.8** | **323.6** | **127.9** | **74.4** | **108.6** | **12.7** | **624.0** | **409.2** | **214.7** |
| 132 | — **% margen EBITDA** | **12.93%** | **12.02%** | **14.58%** | **17.40%** | **8.40%** | **19.92%** | **23.91%** | 10.07% | 10.08% | 10.06% |

---

## 7. Señales del "pleito de reclasificaciones"

**¿Este split ya viene conciliado, o trae las marcas del pleito adentro? Respuesta: es la versión LIMPIA en cuanto a la diálisis, pero SÍ trae marcas de asignación de costos comerciales.**

### 7.1 Diálisis NO está en 0% de EBITDA — este es el corte honesto

La reclasificación en disputa dejaba "diálisis al 0% de EBITDA con margen bruto ~70%". **En este archivo eso NO ocurre:**
- **SANEFRO** (la línea de ~70% de margen bruto: 66.61%) muestra **EBITDA 108.6 $M = 19.92%**, no cero.
- **SIA** (también 66.61% bruto) muestra **EBITDA 12.7 $M = 23.91%**.
- **DP** (diálisis peritoneal) muestra **EBITDA 127.9 $M = 17.40%**.

Cada sub-línea de diálisis conserva su economía natural. **El split que llegó es la fotografía sin el recorte de diálisis-a-cero.** Es el número "bueno" para defender que Servicios/diálisis sí genera EBITDA.

### 7.2 SAFE no está "cortado a cero", pero sí es el eslabón débil

SAFE muestra EBITDA 74.4 $M (8.40%), positivo pero **bajó** desde 87.2 $M (9.42%) en 2025. No está zeroed; es simplemente la sub-línea de menor margen (carga casi toda la "Nómina de Costo Indirecto" de Servicios: 338.5 $M).

### 7.3 SÍ hay marcas de asignación de costos (revisar antes de exponer a nivel sub-línea)

Dos líneas de SG&A de FC salen **negativas** (contra-gasto), lo que delata que el split empujó costo comercial de FC hacia Servicios:

| Línea | FC 2026 | Servicios 2026 | Combinado |
|---|---:|---:|---:|
| Fuerza de Ventas (fila 87) | **−72.0** | +180.2 | 108.2 |
| Gastos Generales comercial (fila 92) | **−34.1** | +109.4 | 75.3 |

A Servicios se le asignó **más** fuerza de ventas (180.2 $M) que el total del bloque (108.2 $M), acreditando a FC con −72.0 $M. El mismo patrón existía en 2025 (FC −58.4). **Aritméticamente cuadra** (los totales reconstruyen el combinado), pero a nivel de línea es un **artefacto de asignación**: infla el EBITDA de FC y castiga el de Servicios. Aun así, Servicios termina con **mayor** margen EBITDA (14.58% vs 12.02%) — la conclusión direccional (Servicios más rentable) es **robusta** incluso absorbiendo 180 $M de fuerza de ventas.

**Implicación:** los **totales de bloque (FC 484.8 / Servicios 323.6) son defendibles** porque suman el combinado auditado. Pero si alguien en el Consejo aterriza en "¿por qué FC tiene fuerza de ventas negativa?", ahí asoma el pleito. No mostrar el detalle de SG&A por sub-línea sin una nota de asignación.

### 7.4 El corte en EBITDA UN, no final — la marca más importante para la tablita

Como el archivo se detiene en EBITDA UN (808.4) y no baja a EBITDA final (804.8), **los 3.6 $M de "Nuevos Productos/Proyectos" 2026 (y 73.9 $M en 2025) no están repartidos** entre FC y Servicios. Ese reparto es una decisión pendiente (típicamente el cargo de Nuevos Productos es de FC/producto, no de servicios, pero el dato no lo dice).

---

## 8. Cierre

### Inconsistencias internas
1. **Fuerza de Ventas y Gastos Generales de FC negativos** (−72.0 y −34.1 $M en 2026; −58.4 y −7.3 en 2025). Artefacto de asignación: costo comercial reasignado de FC a Servicios. Cuadra en total, no a nivel de línea. (§7.3)
2. **Servicios sin desglose Bruta→Neta.** Toda la venta de Servicios (2,219.4 $M) entra directo en las filas 12/18; sus componentes Manufacturados/Comercializados/Devoluciones/Descuentos (filas 13–16) están en 0. Por eso Servicios Bruta = Neta. FC carga el 100% de devoluciones (−535.2) y descuentos (−112.8). Es coherente (los servicios no "se manufacturan/devuelven"), pero es una asimetría estructural.
3. **Celda AE1 = 38.22%** en la banda de encabezado, sin base reconciliable (probadas: Serv/GOB VN 35.49%, EBITDA 40.03%, UB 42.14%). Artefacto de encabezado. No afecta el P&L.
4. **% margen no aditivos** (filas 48/82/125/132): FC%+Serv% ≠ GOB% por construcción. No es error; no sumar porcentajes.

### Choques con referencias
1. **EBITDA UN vs EBITDA final (el choque que importa):** este split da **EBITDA UN 808.4** (FC 484.8 + Serv 323.6). La tablita L6 y el v18 usan **EBITDA final 804.8**. Diferencia **+3.6 $M (2026)** y **+73.9 $M (2025)** = línea "Nuevos Productos/Proyectos", **no repartida** por bloque. Hay que decidir el reparto o declarar que la tablita de GOBIERNO va a nivel UN.
2. **Venta Neta y sell-in: cuadre exacto** (FC 4,034.3 / Serv 2,219.4, YoY −0.6% / +4.0%). La frontera del P&L es Venta Neta = universo sell-in. La diferencia ~$835M del "universo neto" no vive en este archivo.
3. **Cumplimiento de plan (FC 90.0% / Serv 102.1%): no verificable.** El split no trae PPTO/PIN por bloque.

### Vacíos declarados
1. **Reparto de "Nuevos Productos/Proyectos" (3.6 $M 2026 / 73.9 $M 2025) entre FC y Servicios: NO existe** en el archivo. Es lo único que impide bajar el split de EBITDA UN (808.4) a EBITDA final (804.8) de forma limpia.
2. **PPTO / PIN por bloque FC-Servicios: NO existe.** Solo REAL 2026 y 2025. No se pueden reconstruir los % de cumplimiento del deck.
3. **Rótulos definitivos de SAFE, SANEFRO, SIA: NO están en la fuente.** Correspondencia con HD/mezclas inferida por estructura de costos (§1.3), no confirmada.
4. **Base de la celda AE1 (38.22%): NO reconciliada.**
5. **Corporativo de Grupo:** igual que en v18, este bloque no carga corporativo de Grupo; el EBITDA es "antes de corporativo".

### Veredicto de board-readiness
El split es **board-ready para Venta y para EBITDA UN** (cuadra al peso contra v18 y sell-in, y la diálisis viene sin el recorte a cero). **Trae dos advertencias antes de exponerlo:** (a) los totales están a nivel **EBITDA UN 808.4**, no al **final 804.8** que usa la tablita — decidir el reparto de 3.6 $M; (b) **no mostrar SG&A por sub-línea** sin nota, por los contra-gastos de FC (fuerza de ventas negativa). A nivel de bloque (FC 484.8 / Servicios 323.6) el número es sólido y la historia — Servicios como motor de margen (14.6%, +452 pb) — es robusta.
