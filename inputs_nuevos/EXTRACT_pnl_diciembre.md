# EXTRACT — `PnL Diciembre.xlsx`

**Archivo fuente:** `/Users/rafaelprince/Downloads/PnL Diciembre.xlsx` (575 KB)
**Extraído:** 2026-07-16 · openpyxl `data_only` (caché de valores presente y completo; no requirió recalc LibreOffice)
**Universo:** FARMA MX (consolidado nacional PiSA) · **Moneda:** MXN · **Notación:** millones ($XM), márgenes en %
**Integridad:** la suma de los 6 segmentos reconcilia exacto con el consolidado FARMA MX en cada línea y escenario (diff = 0.0). Fórmulas vivas con caché correcto.

---

## 0. Resumen ejecutivo

- Es una **P&L multi-año "Acumulado a Diciembre" de FARMA MX**, con histórico anual completo 2020–2025 (REAL) y **tres escenarios 2026: REAL, PPTO (presupuesto) y PIN (plan)**. Desagregada en 6 segmentos comerciales.
- **Ancla dura full-year 2025 REAL:** Venta Neta **$33,353.6M** · EBITDA **$6,639.4M (19.9%)** · Utilidad Bruta $15,326.6M (46.0%).
- **2026 REAL = acumulado del año en curso (parcial, ≈1S / a junio).** Venta Neta $16,973.9M · EBITDA $4,272.9M (25.2%). Ver bandera de periodo en §6 y §10.
- **DESVIACIÓN a reconciliar:** el EBITDA 2026 REAL de este archivo ($4,272.9M / 25.2%) queda **+$393.3M y +1.7 pp por encima** del EBITDA 1S-26 "final" que trae el deck ($3,879.6M / 23.5%). No forzar; investigar antes de usar.
- **Los compromisos FY-2026 de la llamada 16-jul (compromiso $34,458M / PIN $34,242M) NO aparecen en este archivo.** El PPTO y el PIN de este P&L traen Venta Neta $36,076.6M (bruta $38,977.2M / $37,711.2M). Distinto nivel/definición (probable sell-in vs. venta neta P&L).

---

## 1. Qué ES exactamente

| Atributo | Valor |
|---|---|
| Tipo de documento | Estado de Resultados (P&L) gerencial multi-año, formato interno PiSA |
| Marco temporal | "Acumulado" / "Diciembre" (rótulos en F1:F2) = vista full-year |
| Universo | **FARMA MX** (consolidado) = suma de 6 segmentos |
| Años REAL completos | 2020, 2021, 2022, 2023, 2024, 2025 |
| Escenarios 2026 | **REAL** (acumulado en curso) · **PPTO** (presupuesto full-year) · **PIN** (plan full-year) |
| Segmentos | 01 GOBIERNO · 02 IMPULSO · 03 HOSPITALES PRIVADOS · 04 FARMACIAS · 05 EXPANSIÓN · 06 SOPORTE |
| Profundidad | Detalle línea por línea: Venta Bruta → deducciones → COGS (Manufactura/Indirecto/Variaciones/Comercializados) → Fletes → Almacenaje → SG&A (Comercial/Soporte/I&D) → Corporativo → EBITDA → UAFIR → NOPAT → Utilidad Neta → Balance/ROIC |
| Emisor / dueño | No hay firma/logo en celdas; es el modelo P&L de Finanzas/Controlería PiSA (estructura idéntica a los cortes de Edo. de Resultados del proyecto) |

**Nota sobre "SOPORTE" (06):** es un centro de costo sin ingreso (Venta Neta = $0 en todos los años); absorbe overhead/corporativo. Su EBITDA es siempre negativo (2025: −$1,228.3M). Por eso las líneas "Corporativo" del bloque consolidado salen en $0 — ese costo vive dentro de SOPORTE.

---

## 2. Estructura del archivo

- **2 hojas.** Hoja `'2025'` (todo el contenido, A1:IX229 = 229 filas × 258 columnas) y `'Hoja2'` (vacía, A1).
- **Eje vertical (filas):** columna A = línea de detalle; columna F = rótulo de subtotal/sección; columna C = clasificación de costo (`VN` Venta Neta, `CV` Costo Variable, `CF` Costo Fijo).
- **Eje horizontal (columnas):** 7 bloques de 21 columnas cada uno.
  - Bloque 1 = **FARMA MX consolidado** (col H–AA).
  - Bloques 2–7 = los 6 segmentos (GOB desde AC, IM desde AX, HP desde BS, FARM desde CN, EXP desde DI, SOP desde ED).
- **Dentro de cada bloque** (offset desde la 1ª columna del bloque): REAL 2020(+0), 2021(+1), 2022(+2), 2023(+3), 2024(+4), %Vtas(+5), **REAL 2025(+6)**, %Vtas(+7), **REAL 2026(+8)**, %Vtas(+9), VAR(+10), %(+11), **PPTO 2026(+12)**, %Vtas(+13), VAR(+14), %(+15), **PIN 2026(+16)**, %Vtas(+17), VAR(+18), %(+19).
  - Consolidado FARMA MX: 2025R = **N**, 2026R = **P**, PPTO = **T**, PIN = **X**.
- Zona derecha (EZ–FG) = celdas de cuadre/validación (residuos ~1e-5, ruido de redondeo). "FF" rotulada `2026Meta`.

---

## 3. Anclas full-year 2025 REAL (lo prioritario para el deck)

| Concepto | FY-2025 REAL | % s/ Venta Neta |
|---|---:|---:|
| Venta Bruta | $36,619.5M | — |
| (−) Devoluciones y rechazos | −$1,904.9M | −5.7% |
| (−) Descuentos | −$1,361.0M | −4.1% |
| **Venta Neta** | **$33,353.6M** | 100.0% |
| (−) Costo de Ventas | −$18,027.0M | 54.0% |
| **Utilidad Bruta** | **$15,326.6M** | **46.0%** |
| Utilidad Marginal (post logística/almacén) | $10,993.6M | 33.0% |
| EBITDA UN (antes de proyectos) | $6,968.3M | 20.9% |
| **EBITDA** | **$6,639.4M** | **19.9%** |
| UAFIR | $4,806.6M | 14.4% |
| NOPAT (× 0.7) | $3,364.6M | — |
| Utilidad Neta (× 0.5) | $2,403.3M | — |
| D&A total | $1,832.8M | — |

**Deducciones gross-to-net 2025 = $3,265.9M = 8.92% de la venta bruta.**

### Arco histórico de margen EBITDA (la historia de compresión)
| Año | Venta Neta | EBITDA $ | Margen EBITDA |
|---|---:|---:|---:|
| 2020 | $23,830.1M | $5,077.2M | 21.3% |
| 2021 | $25,010.1M | $6,714.5M | 26.8% |
| 2022 | $26,601.9M | $7,080.4M | 26.6% |
| **2023** | $30,320.0M | **$9,378.1M** | **30.9%** ← pico |
| 2024 | $31,967.8M | $7,946.8M | 24.9% |
| **2025** | $33,353.6M | **$6,639.4M** | **19.9%** ← valle |

La venta neta creció sin parar (CAGR 2020–25 = **+6.96%**), pero el EBITDA en $ cayó **−$2,738.7M (−29.2%)** del pico 2023 al valle 2025, y el margen se comprimió **11.0 pp** (30.9% → 19.9%). Ese es el punto de partida que el 2026 busca revertir.

---

## 4. P&L consolidado FARMA MX — 4 escenarios (detalle completo)

Cifras en MXN millones. Escenarios: **2025R** (real full-year) · **2026R** (real acumulado en curso, ≈1S) · **PPTO** (presupuesto full-year) · **PIN** (plan full-year).

| Línea (fila) | 2025R | 2026R | PPTO26 | PIN26 |
|---|---:|---:|---:|---:|
| Venta Bruta (12) | 36,619.5 | 18,522.1 | 38,977.2 | 37,711.2 |
| · Manufacturados (13) | 30,755.1 | 15,419.9 | 33,170.6 | 31,903.0 |
| · Comercializados (14) | 5,864.5 | 3,102.3 | 5,806.6 | 5,808.2 |
| (−) Devoluciones y rechazos (15) | −1,904.9 | −906.6 | −1,266.0 | **0.0** |
| (−) Descuentos (16) | −1,361.0 | −641.6 | −1,634.6 | −1,634.6 |
| **Venta Neta (18)** | **33,353.6** | **16,973.9** | **36,076.6** | **36,076.6** |
| Costo de Ventas (20) | 18,027.0 | 8,610.5 | 18,848.3 | 18,313.2 |
| · COGS Manufacturados (21) | 14,870.1 | 7,009.6 | 15,895.6 | 15,316.1 |
| · COGS Costo Indirecto (25) | 5,690.3 | 2,845.0 | 5,909.8 | 5,866.5 |
| · COGS Variaciones (36) | 624.0 | 80.0 | 857.6 | 287.0 |
| · COGS Comercializados (42) | 3,156.9 | 1,600.9 | 2,952.7 | 2,997.1 |
| **Utilidad Bruta (47)** | **15,326.6** | **8,363.4** | **17,228.3** | **17,763.4** |
| **% margen bruto (48)** | **46.0%** | 49.3% | 47.8% | 49.2% |
| Logística y almacenaje (50) | 4,333.0 | 2,099.4 | 4,040.4 | 4,035.6 |
| · Fletes (51) | 2,034.5 | 962.0 | 1,701.4 | 1,703.9 |
| · Almacenaje (59) | 2,096.6 | 1,021.1 | 2,095.5 | 2,095.2 |
| · Soporte Logística (71) | 201.9 | 116.3 | 243.5 | 236.5 |
| **Utilidad Marginal (81)** | **10,993.6** | **6,264.0** | **13,187.9** | **13,727.8** |
| **% margen marginal (82)** | **33.0%** | 36.9% | 36.6% | 38.1% |
| Gastos SG&A (84) | 5,858.0 | 2,900.8 | 6,021.0 | 5,179.2 |
| · SG&A Comercial (85) | 3,533.7 | 1,739.2 | 3,488.1 | 3,552.9 |
| · · Marketing (100) | 484.2 | 242.4 | 601.6 | **0.0** |
| · SG&A Soporte/Admin (104) | 1,307.9 | 670.9 | 1,338.5 | 1,030.6 |
| · SG&A I+D (116) | 532.2 | 248.2 | 592.9 | 595.7 |
| UAFIR UN (124) | 5,135.5 | 3,363.2 | 7,166.9 | 8,548.5 |
| **EBITDA UN (131)** | **6,968.3** | **4,335.2** | **9,068.1** | **10,451.7** |
| **% margen EBITDA UN (132)** | 20.9% | 25.5% | 25.1% | 29.0% |
| Corporativo (134) | 0.0¹ | 0.0¹ | 0.0¹ | 0.0¹ |
| UAFIR UN post-Corpo (155) | 5,135.5 | 3,363.2 | 7,166.9 | 8,548.5 |
| Gastos por Proyectos (158) | 328.9 | 62.3 | 398.2 | 389.2 |
| UAFIR (162) | 4,806.6 | 3,300.9 | 6,768.7 | 8,159.4 |
| **% margen UAFIR (163)** | 14.4% | 19.4% | 18.8% | 22.6% |
| **EBITDA (170)** | **6,639.4** | **4,272.9** | **8,669.8** | **10,062.5** |
| **% margen EBITDA (171)** | **19.9%** | **25.2%** | **24.0%** | **27.9%** |
| NOPAT (184) | 3,364.6 | 3,795.3² | 4,738.1 | s/d |
| Utilidad Neta (185) | 2,403.3 | 2,710.9² | 3,384.3 | s/d |

¹ Las líneas Corporativo salen en $0 en el consolidado porque ese costo está capturado dentro del segmento **06 SOPORTE**.
² NOPAT y Utilidad Neta del 2026R se calculan sobre **UAFIR anualizado** (fila 179/180 = $5,421.8M), no sobre el UAFIR real acumulado. Factores: NOPAT = UAFIR anualizado × 0.7; Utilidad Neta × 0.5.

---

## 5. Corte por 6 segmentos comerciales

### Venta Neta (MXN millones) y mix
| Segmento | 2025R | mix25 | 2026R | 2026PPTO | 2026PIN |
|---|---:|---:|---:|---:|---:|
| 01 Gobierno | 12,795.7 | 38.4% | 6,548.9 | 13,402.9 | 13,402.9 |
| 02 Impulso | 5,506.8 | 16.5% | 2,789.4 | 5,829.7 | 5,829.7 |
| 03 Hospitales Privados | 5,938.5 | 17.8% | 3,158.5 | 6,537.7 | 6,537.7 |
| 04 Farmacias | 6,309.5 | 18.9% | 2,967.2 | 7,166.9 | 7,166.9 |
| 05 Expansión | 2,803.1 | 8.4% | 1,509.9 | 3,139.5 | 3,139.5 |
| 06 Soporte | 0.0 | 0.0% | 0.0 | 0.0 | 0.0 |
| **FARMA MX** | **33,353.6** | 100% | **16,973.9** | **36,076.6** | **36,076.6** |

### EBITDA por segmento (MXN millones) y margen
| Segmento | 2025R $ | 2025R % | 2026R $ | 2026R % | PPTO $ | PPTO % | PIN $ | PIN % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 Gobierno | 1,223.6 | 9.6% | 1,031.6 | 15.8% | 1,753.4 | 13.1% | 2,024.5 | 15.1% |
| 02 Impulso | 1,514.4 | 27.5% | 962.3 | 34.5% | 1,854.3 | 31.8% | 2,080.2 | 35.7% |
| 03 Hospitales Priv. | 2,193.0 | 36.9% | 1,288.0 | 40.8% | 2,630.2 | 40.2% | 2,705.0 | 41.4% |
| 04 Farmacias | 1,946.4 | 30.8% | 980.9 | 33.1% | 2,574.2 | 35.9% | 3,173.5 | 44.3% |
| 05 Expansión | 990.2 | 35.3% | 608.3 | 40.3% | 1,277.2 | 40.7% | 1,319.5 | 42.0% |
| 06 Soporte | −1,228.3 | — | −598.3 | — | −1,419.5 | — | −1,240.2 | — |
| **FARMA MX** | **6,639.4** | **19.9%** | **4,272.9** | **25.2%** | **8,669.8** | **24.0%** | **10,062.5** | **27.9%** |

**Lecturas de mezcla (2025 REAL):**
- **Gobierno** es el mayor por volumen (38.4% de venta) pero el de **menor margen EBITDA (9.6%)** — dilutivo.
- **Hospitales Privados (36.9%)** y **Expansión (35.3%)** son los de mayor margen; **Impulso 27.5%**, **Farmacias 30.8%**.
- El drag de **Soporte (−$1,228.3M)** consume ~15.6% del EBITDA bruto de los segmentos.
- En el PIN, el salto de margen más agresivo es **Farmacias (30.8% → 44.3%)** — ojo, es el más difícil de sostener (ver §6, caveat marketing).

---

## 6. Escenarios 2026: REAL / PPTO / PIN — qué es cada uno

### 2026 REAL — acumulado del año en curso (parcial, ≈1S / a junio)
- Venta Neta $16,973.9M · EBITDA $4,272.9M (25.2%).
- **Evidencia de que es 1S (a junio), no full-year ni a mayo:** la Venta Neta 2026R es **47.0% del PPTO full-year** = **94.1% del PPTO semestral proporcional**, casi idéntico al **93.4%** de cumplimiento de sell-in 1S-26 que trae el deck. El EBITDA 2026R está a **98.6%** del PPTO semestral (el margen aguanta mejor que el ingreso). Además, si 1S-25 fue $16,279.2M = 48.8% del FY25, un acumulado a mayo daría ~40% del año — inconsistente con el 47.0% observado.
- **Bandera:** la fila auxiliar 179 se rotula **"UAFIR (Anualizado a May)"**. Hay tensión entre ese rótulo y la aritmética (que apunta a junio). Lo más probable: rótulo heredado de una corrida de mayo del template. **Confirmar el mes de corte exacto con el dueño del modelo antes de citar el 2026R como "1S-26".**

### 2026 PPTO — presupuesto full-year
- Venta Neta $36,076.6M · Venta Bruta $38,977.2M · EBITDA $8,669.8M (24.0%).

### 2026 PIN — plan full-year
- Venta Neta $36,076.6M (idéntica al PPTO) · Venta Bruta $37,711.2M · EBITDA $10,062.5M (27.9%).
- **El PIN mantiene el ingreso neto igual al PPTO pero sube el EBITDA +$1,392.7M.** ¿Cómo? Mecánicamente, por dos supuestos agresivos:
  1. **Devoluciones y rechazos = $0** (vs −$1,266.0M en PPTO). Las deducciones gross-to-net del PIN caen a **4.33%** de la venta bruta vs **8.92%** real en 2025 y 7.44% en PPTO.
  2. **Marketing = $0** (Medios, Inversión en canales, Muestras y promocionales todos en $0; vs $601.6M en PPTO).
- **Caveat para el deck:** el EBITDA PIN de 27.9% **no es comparable one-to-one** con el real; descansa en cero devoluciones y cero inversión comercial, supuestos poco realistas. Tratar el PIN como techo aspiracional, no como forecast base.

### Puente EBITDA 2026
`2025R $6,639.4M (19.9%) → PPTO $8,669.8M (24.0%, +$2,030.4M) → PIN $10,062.5M (27.9%, +$1,392.7M)`

---

## 7. Balance / capital / ROIC (consolidado FARMA MX)

| Concepto | 2025R | 2026R | PPTO26 |
|---|---:|---:|---:|
| ROA | 6.9% | 7.9% | 9.7% |
| ROIC | 10.0% | 11.5% | 14.1% |
| Capital invertido | $33,630.6M | $32,908.4M | $33,590.5M |
| Activo operativo | $34,768.7M | $34,209.3M | $34,856.0M |
| · Inventarios (MP + PT) | $12,222.5M | $11,753.7M | $12,135.8M |
| · · Inventario MP | $6,061.5M | $5,606.7M | $5,966.1M |
| · · Inventario PT | $6,161.0M | $6,147.1M | $6,169.7M |
| · Cuentas por cobrar (cartera) | $9,834.9M | $10,037.4M | $9,834.9M |
| · PP&E | $12,711.3M | $12,418.1M | $12,885.3M |
| Pasivo operativo (Proveedores) | $1,138.0M | $1,300.9M | $1,265.5M |

- ROA/ROIC del 2026R se calculan sobre utilidad **anualizada**, por eso el 11.5% es comparable con años completos.
- El PIN no trae valores de balance/ROIC (columna en blanco en esta sección).

---

## 8. Cruces contra lo conocido

| Referencia conocida (deck / llamada) | Este archivo | Veredicto |
|---|---|---|
| EBITDA 1S-25 = 19.7% | EBITDA FY-2025 = **19.9%** (no hay columna 1S-25) | **OK** — consistente (full-year ligeramente arriba del 1S). No se puede verificar el 1S-25 exacto aquí. |
| 1S-25 Venta Neta = $16,279.2M | FY-2025 VN = $33,353.6M → implica 2S-25 = $17,074.4M | **OK / plausible** (1S = 48.8% del año). |
| 1S-26 sell-in $16,518.5M / 93.4% del plan / +1.5% | 2026R Venta Neta P&L = $16,973.9M = 94.1% del PPTO semestral | **OK** — métricas distintas (sell-in vs venta neta P&L) pero el % de cumplimiento (94.1% vs 93.4%) casa muy bien. |
| **EBITDA 1S-26 Farma MX = $3,879.6M "final" / 23.5%** | 2026R EBITDA = **$4,272.9M / 25.2%** | **DESVIACIÓN — +$393.3M / +1.7 pp.** El archivo trae más EBITDA que el deck. Reconciliar antes de usar (posible: corte de mes distinto, versión/cierre previo a ajustes/provisiones, o definición). No forzar. |
| Compromiso FY-2026 = $34,458M · PIN FY-2026 = $34,242M (llamada 16-jul) | PPTO VN $36,076.6M / PIN VN $36,076.6M; brutas $38,977.2M / $37,711.2M | **NO MATCHEA** — ninguna cifra del archivo iguala $34,458M ni $34,242M. Los compromisos de la llamada están a otro nivel/definición (probable **sell-in**, no venta neta P&L). Confirmar la base antes de cruzar. |

---

## 9. Corte "FC vs Servicios" — NO disponible en este archivo

Este P&L **no** desagrega Gobierno en FC vs Servicios. Gobierno viene **consolidado como un único segmento** (VN 2025 = $12,795.7M, EBITDA 9.6%). Los 6 cortes son GOB / IM / HP / FARM / EXP / SOP. Si el deck necesita el split FC vs Servicios dentro de Gobierno, esa apertura hay que sacarla de otra fuente (ver `EXTRACT_pl_gob_vs_servicios.md` y `EXTRACT_puentes_hosp_gobfc.md` ya en `inputs_nuevos`).

---

## 10. Vacíos y banderas (lo que NO se puede afirmar desde este archivo)

1. **Periodo exacto del 2026 REAL:** la aritmética dice ≈junio (1S-26); el rótulo de la fila de anualización dice "a May". Confirmar mes de corte. (§6)
2. **DESVIACIÓN de EBITDA 1S-26** de +$393.3M / +1.7 pp vs el número "final" del deck. Sin reconciliar. (§8)
3. **Compromiso $34,458M / PIN $34,242M no están en el archivo.** No usar el PPTO/PIN de este P&L ($36,076.6M) como si fueran esos compromisos. (§8)
4. **PIN infla EBITDA con supuestos de cero devoluciones y cero marketing.** No es forecast base; es techo. (§6)
5. **No hay monthly breakdown** — solo columnas anuales/acumuladas. Cualquier estacionalidad hay que sacarla de otra fuente.
6. **No hay corte FC vs Servicios ni sub-canal dentro de segmento.** (§9)
7. NOPAT/Utilidad Neta usan factores fijos (0.7 / 0.5) sobre UAFIR anualizado, no tasa fiscal real por año.
8. Emisor no consta en celdas; se asume Finanzas/Controlería PiSA por estructura.

---

## Apéndice — Mapeo de columnas (para reproducir)

| Bloque | Col inicio | 2025R | 2026R | PPTO26 | PIN26 |
|---|---|---|---|---|---|
| FARMA MX | H (8) | N | P | T | X |
| 01 GOB | AC (29) | AI | AK | AO | AS |
| 02 IM | AX (50) | BD | BF | BJ | BN |
| 03 HP | BS (71) | BY | CA | CE | CI |
| 04 FARM | CN (92) | CT | CV | CZ | DD |
| 05 EXP | DI (113) | DO | DQ | DU | DY |
| 06 SOP | ED (134) | EJ | EL | EP | ET |

Offset dentro de cada bloque: 2025R = +6, 2026R = +8, PPTO = +12, PIN = +16. Filas clave: Venta Bruta 12 · Venta Neta 18 · Utilidad Bruta 47 · Utilidad Marginal 81 · EBITDA UN 131 · EBITDA 170 · % margen EBITDA 171 · UAFIR 162 · NOPAT 184 · Utilidad Neta 185.
