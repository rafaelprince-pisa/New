# EXTRACT — Verificación de puentes de venta: Hospitales y Gob Frasco Cerrado

**Fecha:** 2026-07-16
**Fuente:** `PVM_Reconstruido_scripts/v2/Downtrading_Hospitales_FINAL_2026-07-16.xlsx` y `Downtrading_GobFC_FINAL_2026-07-16.xlsx`
**Alcance:** Ene–Jun 2025 vs Ene–Jun 2026, sell-in neto (down-trading / PVM por molécula, capa C7 de terceros aplicada).
**Método de recálculo:** los originales se entregan FORMULADOS (fórmulas vivas). Se copiaron a scratchpad y se recalcularon con LibreOffice headless (`soffice --headless --calc --convert-to xlsx`) usando un `UserInstallation` aislado con `OOXMLRecalcMode=0` (full recalc on load). **Los originales NO se tocaron.** Todos los valores de abajo son los que devuelve LibreOffice tras recalcular; se comparan contra los INSIGHTS canónicos.

---

## 1. Veredicto

**TODO CUADRA.** Las 8 líneas del puente, los 3 niveles de conciliación, la doble cobertura (core y G5b), el control de 8 bloques (= 0) y el detalle C7 (58 / 29 materiales, continuas/altas/bajas) reconcilian al último decimal en ambos segmentos. **Cero desviaciones.** El `terceros_overrides.csv` es byte-idéntico al PROPUESTA (SHA-256 `31959f…637a7`); Privado y Gob Servicios quedaron intocados.

Único punto de atención (no es error de dato): la coincidencia de que **dos materiales distintos** —KEYTRUDA (pembrolizumab, reclasificado C7) y SUTIVIN (vincristina, VARIOS nativo)— aportan cada uno **≈ +28.58 M** a Hospitales Terceros. Son materiales separados; no hay doble conteo (verificado en Datos Maestro).

---

## 2. Verificación celda por celda — HOSPITALES

| Bloque / vista | Recálculo (MXN M) | Esperado INSIGHTS | Estatus |
|---|---:|---:|:--:|
| 1 Precio — core PiSA | −5.716877 | −5.717 | **OK** |
| 2 Volumen — core PiSA | +26.262579 | +26.263 | **OK** |
| 3 Mix — core PiSA | −14.467861 | −14.468 | **OK** |
| 4 Gestión de portafolio core | +8.270338 | +8.270 | **OK** |
| — Bajas / discontinuaciones | −2.075529 | (info) | **OK** |
| — Altas de distribución/equipo | +10.345867 | (info) | **OK** |
| — Sustituciones cosidas | 0.000000 | 0 | **OK** |
| 5 Lanzamientos 2026 | +23.147183 | +23.147 | **OK** |
| 6 Terceros / VARIOS | +112.068773 | +112.069 | **OK** |
| 7 Serie 9 contable / servicios | +7.846772 | +7.847 | **OK** |
| 8 PiSA sin unidad comparable | −3.626026 | −3.626 | **OK** |
| **Δ Venta reclasificada (Σ 8)** | **+153.784883** | **+153.785** | **OK** |
| Control 8 bloques (Σ − Δ directa) | 0.0 (0.00e+00) | 0 | **OK** |
| Conciliación N1 → Δ reclasificada | +153.784883 | +153.785 | **OK** |
| (−) reclasif. nov-dic'25 lanzamientos | −4.412750 | — | **OK** |
| Conciliación N2 → Δ sell-in con MATNR | +149.372134 | +149.372 | **OK** |
| (+) Δ filas sin MATNR | −1.456512 | — | **OK** |
| Conciliación N3 → Δ cubo completo | +147.915622 | +147.916 | **OK** |
| Cobertura core (65.0% bruto elegible) | 0.650249 | 0.650 | **OK** |
| Cobertura técnica G5b (fila 25) | 0.728773 | 0.7288 | **OK** |
| Base bruta-positiva elegible | 5,909.12 | — | (info) |
| **Core neto (Σ bloques 1–4)** | **+14.348180** | **+14.348** | **OK** |

Detalle C7 (hoja *Detalle Terceros C7*):

| Movimiento core → Terceros | Materiales | Recálculo M | Esperado | Estatus |
|---|---:|---:|---:|:--:|
| Continuas | 36 | +36.489753 | +36.490 | **OK** |
| Altas | 6 | +4.751913 | +4.752 | **OK** |
| Bajas | 6 | −2.604636 | −2.605 | **OK** |
| Sin movimiento H1 | 10 | 0.000000 | — | **OK** |
| **Total movido** | **58** | **+38.637030** | **+38.637** | **OK** |

Cadena de core: **+52.985 (antes C7) − 38.637 (movido) = +14.348 (post-C7)**. Cuadra al centavo.

---

## 3. Verificación celda por celda — GOB FRASCO CERRADO

| Bloque / vista | Recálculo (MXN M) | Esperado INSIGHTS | Estatus |
|---|---:|---:|:--:|
| 1 Precio — core PiSA | −320.321268 | −320.321 | **OK** |
| 2 Volumen — core PiSA | +425.214485 | +425.214 | **OK** |
| 3 Mix — core PiSA | −84.600557 | −84.601 | **OK** |
| 4 Gestión de portafolio core | +19.530399 | +19.530 | **OK** |
| — Bajas / discontinuaciones | −64.578787 | −64.579 | **OK** |
| — Altas de licitación/contrato | +84.109186 | +84.109 | **OK** |
| — Sustituciones cosidas | 0.000000 | 0 | **OK** |
| 5 Lanzamientos 2026 | +0.154499 | +0.154 | **OK** |
| 6 Terceros / VARIOS | −53.309437 | −53.309 | **OK** |
| 7 Serie 9 contable / servicios | −10.385412 | −10.385 | **OK** |
| 8 PiSA sin unidad comparable | −1.178957 | −1.179 | **OK** |
| **Δ Venta reclasificada (Σ 8)** | **−24.896248** | **−24.896** | **OK** |
| Control 8 bloques | 0.0 (0.00e+00) | 0 | **OK** |
| Conciliación N1 = N2 = N3 | −24.896248 (los tres) | −24.896 | **OK** |
| Cobertura core (78.9% bruto elegible) | 0.789079 | 0.7891 | **OK** |
| Cobertura técnica G5b (fila 25) | 0.817110 | 0.8171 | **OK** |
| Base bruta-positiva elegible | 8,323.74 | — | (info) |
| **Core neto (Σ bloques 1–4)** | **+39.823059** | **+39.823** | **OK** |

En Gob FC los tres niveles de conciliación son idénticos (−24.896248): no hay reclasificación nov-dic de lanzamientos ni gap de filas sin MATNR.

Detalle C7 (hoja *Detalle Terceros C7*):

| Movimiento core → Terceros | Materiales | Recálculo M | Estatus |
|---|---:|---:|:--:|
| Continuas | 11 | +39.983212 | **OK** |
| Altas | 9 | +32.367829 | **OK** |
| Bajas | 7 | −35.494134 | **OK** |
| Sin movimiento H1 | 2 | 0.000000 | **OK** |
| **Total movido** | **29** | **+36.856907** | **OK** |

- **KETOSTERIL 4026185 — alta de tercero: +30.050460 M** (0 → 30.05). **OK**
- **BIOYETIN (4005429 + 4006851) — bajas de tercero: −33.236211 M** (−26.175581 + −7.060631). **OK**

Cadena de core: **+76.680 (antes C7) − 36.857 (movido) = +39.823 (post-C7)**. Cuadra.

---

## 4. Estructura de hojas (idéntica en ambos workbooks)

| # | Hoja | Contenido | Filas de datos |
|---|---|---|---|
| 1 | Resumen Ejecutivo | 8 bloques del puente + doble cobertura + top-5 down-traders + conciliación 3 niveles. Todas las celdas B son **fórmulas vivas** que apuntan a las hojas de datos. | 42 |
| 2 | Detalle Terceros C7 | Lista adjudicada de terceros: continuas/altas/bajas, MATNR, descripción, clasificación, pool C7, V25/V26 H1, Δ movida, evidencia. | Hosp 58+ / Gob 29+ |
| 3 | Datos Hechos | Hechos por material: V25/V26, flag lanzamiento, etc. Feed de bloque 5. | Hosp 1,579 / Gob 3,731 |
| 4 | Datos Lanzamientos | 13 materiales lanzamiento con reclasificación nov-dic'25. | 33 |
| 5 | Datos Maestro | Diccionario material→molécula (matnr, desc, molecula, molecula_nativa, clase, factor_conteo, contenido, flags g6, etc., 27 cols). | Hosp 1,579 / Gob 3,731 |
| 6 | Datos Familias | Insumo intermedio de familias. | ídem |
| 7 | **Familias** | **Núcleo del cálculo PVM.** Por familia (molécula\|unidad\|matnr): Q25/Q26, V25/V26, p0/p1, s0/s1, y las columnas **P=Precio, Q=Volumen, R=Mix, S=Altas, T=Bajas** (efecto en pesos). Bloques 1–3 = `SUM(P/Q/R)/1e6`; block 6/7/8 = `SUMIFS(BS, BT="TERCEROS_VARIOS" / "SERIE_9" / "PISA_SIN_UNIDAD")`. 77 cols. | Hosp 1,579 / Gob 3,731 |
| 8 | Ranking Franquicias | Precio/Volumen/Mix **por molécula**, ordenado por down-trading. Columna **Mix $M** reconcilia exacto al bloque 3; sus columnas Precio/Volumen son una descomposición alterna (NO reconcilian a los bloques 1–2, ver §7). | Hosp 282 / Gob 350 |
| 9 | Detalle Top Franquicias | Desglose de las franquicias top. | ídem |

Rangos de suma de bloques 1–4 (core normalizable): **Familias filas 5:894 (Hosp)**, **5:1631 (Gob FC)**. Bloques 6–8 barren todo el rango 5:3729.

---

## 5. Qué es la "reclasificación C7" y el `terceros_overrides.csv` (método)

**Problema que resuelve:** el puente PVM normaliza por molécula/unidad, pero PiSA **distribuye** muchos productos que **no manufactura** (marcas originadoras oncológicas/inmunológicas, biosimilares de terceros, algunos equipos/consumibles). Si esos productos se dejan en el core, contaminan Precio/Volumen/Mix con negocio que no es fabricación PiSA. C7 los **saca del core** y los enruta a un bloque separado (**Terceros / VARIOS**), **sin mover la Δ total** del segmento (invarianza: el control de 8 bloques queda en 0).

**Cómo opera (código `ext_segmentos/apply_c7_terceros.py`):**
1. Lee `terceros_overrides.csv` — lista adjudicada a mano: **87 materiales TERCERO** (58 Hospitales + 29 Gob FC). Columnas: `matnr, desc, segmentos_afectados, clasificacion, evidencia, v25h1_m, v26h1_m, delta_m, molecula, pool_actual`. `pool_actual` marca cada material como `P/V/M (comparable)` (→ continua), `Gestion-Alta` o `Gestion-Baja`.
2. En Familias, saca esos materiales de las columnas de core (BP/BQ/BR) y los re-enruta por BS/BT al bucket **"TERCEROS_VARIOS"**. Conserva la elegibilidad técnica en BB para que la cobertura **G5b no cambie** (72.88% / 81.71%); solo cambia la cobertura **comercial** del core.
3. La **enmienda final** (que gobierna sobre el cuerpo original): el movimiento es **COMPLETO** — KETOSTERIL y BIOYETIN salen del core junto con las continuas. Los **20 materiales AMBIGUOS no se consumen**: permanecen en core (no están en el CSV).
4. Construye la hoja *Detalle Terceros C7* con continuas / altas / bajas / sin-movimiento y fórmulas vivas.

**"Δ movida" vs bloque 6:** la Δ movida (+38.637 Hosp / +36.857 Gob) es lo que se **resta del core** (blocks 1–4). El bloque 6 Terceros/VARIOS es mayor (+112.069 Hosp) porque además contiene el VARIOS **nativo** que nunca estuvo en el core (≈ +73.4 M en Hosp). En Gob FC el bloque 6 es negativo (−53.309) porque el VARIOS nativo cae más de lo que suben las altas C7.

**Conciliación CSV vs cubo:** el CSV guarda 6 decimales de MXN M ≈ redondeo al peso por fila; residuo total −$0.54 (Hosp) y −$1.05 (Gob), sin material faltante ni doble conteo. Cinco gates PASS (invarianza, movimiento, regresión Privado bit-idéntica, SHA-256 de intocables 76/76, cero claims nuevos G1–G6).

---

## 6. Top del Mix (down-trading) por molécula

Fuente: hoja *Ranking Franquicias*, columna **Mix $M** (reconcilia exacto al bloque 3). Mix negativo = down-trading (la mezcla migró a presentaciones/moléculas de menor valor).

**HOSPITALES — Mix total −14.468 M**

| # | Molécula | Mix $M | (Volumen $M) | (Precio $M) |
|---|---|---:|---:|---:|
| 1 | FLEBOTEK | −6.936 | −20.305 | +3.186 |
| 2 | CEFTRIAXONA | −3.475 | −6.375 | +0.453 |
| 3 | ONDANSETRON | −2.855 | +8.489 | −4.618 |
| 4 | PARACETAMOL | −2.733 | +0.233 | −3.980 |
| 5 | MEROPENEM | −2.512 | +2.172 | −2.378 |
| 6 | ACICLOVIR | −1.975 | +2.075 | −0.264 |
| 7 | OMEPRAZOL | −1.227 | +0.479 | −2.881 |
| 8 | MIDAZOLAM | −1.147 | +1.713 | −0.884 |
| 9 | FLUOROURACILO | −1.105 | −1.117 | −1.570 |
| 10 | BENDAMUSTINA | −0.900 | +0.630 | +0.148 |

**GOB FRASCO CERRADO — Mix total −84.601 M**

| # | Molécula | Mix $M | (Volumen $M) | (Precio $M) |
|---|---|---:|---:|---:|
| 1 | FLEBOTEK | −46.914 | +105.010 | −3.338 |
| 2 | AMPICILINA | −18.505 | +34.365 | −1.234 |
| 3 | BUDESONIDA | −8.378 | +9.444 | −0.444 |
| 4 | PANTOPRAZOL | −7.897 | −8.027 | −9.540 |
| 5 | ALFA CETOANALOGOS | −6.394 | +13.353 | +3.794 |
| 6 | CLINDAMICINA | −5.839 | +10.992 | −2.349 |
| 7 | ENOXAPARINA DE SODIO | −4.882 | +4.802 | −5.460 |
| 8 | ERITROPOYETINA HUMANA RECOMB | −4.000 | +71.721 | −126.249 |
| 9 | CIPROFLOXACINO | −3.817 | −1.916 | −0.154 |
| 10 | NOREPINEFRINA | −2.831 | +16.265 | −2.858 |

**FLEBOTEK es el down-trader #1 en ambos segmentos** (solución/electrolitos de gran volumen que migra a presentación menor). En Gob FC concentra 55% del Mix negativo (−46.9 de −84.6).

---

## 7. Volumen Gob FC +425.2 — ¿cuáles claves ganaron piezas?

Fuente correcta: **`Familias!Q` agregado por molécula** (reconcilia exacto a +425.214 M). El "Volumen $M" de *Ranking Franquicias* usa otra descomposición y NO reconcilia (suma +443.3 M en Gob, +3.0 M en Hosp) — **no usar esa columna para volumen**; sí para Mix.

**GOB FC — Volumen total +425.214 M — top moléculas que ganaron piezas:**

| # | Molécula | Volumen $M | (Mix $M) | (Precio $M) |
|---|---|---:|---:|---:|
| 1 | FLEBOTEK | +105.010 | −46.914 | −3.338 |
| 2 | ERITROPOYETINA HUMANA RECOMB | +71.721 | −4.000 | −126.249 |
| 3 | HEPARINA | +71.175 | +1.858 | −16.693 |
| 4 | INSULINA GLARGINA | +41.681 | +0.067 | −29.100 |
| 5 | INSULINA HUMANA | +40.578 | +4.119 | −3.061 |
| 6 | AMPICILINA | +34.365 | −18.505 | −1.234 |
| 7 | MEROPENEM | +22.197 | −2.061 | −12.428 |
| 8 | EPINASTINA | +21.818 | 0.000 | +0.050 |
| 9 | ACIDO MICOFENOLICO | +20.840 | +0.042 | −0.156 |
| 10 | CEFTRIAXONA | +20.340 | +2.094 | −15.290 |
| 11 | OMEPRAZOL | +17.228 | −0.773 | −17.510 |
| 12 | NOREPINEFRINA | +16.265 | −2.831 | −2.858 |
| 13 | SOLUCION HARTMANN | +15.563 | +1.414 | −2.385 |
| 14 | PREGABALINA | +14.367 | −0.533 | −4.841 |
| 15 | ALFA CETOANALOGOS | +13.353 | −6.394 | +3.794 |

Lectura: el +425.2 de volumen viene de **ganancia de piezas en licitación** (soluciones/electrolitos, insulinas, antibióticos, eritropoyetina), pero **el precio se desploma en paralelo** (−320.3) — típico de adjudicaciones de gobierno a bajo precio. ERITROPOYETINA es el caso extremo: +71.7 de volumen contra −126.2 de precio.

Mayores **caídas** de volumen (contrapeso): INSULINA HUMANA ACCION INTERM −63.3, HIDROCLOROTIAZIDA+TELMISARTAN −27.0, PENTOXIFILINA −22.5, GABAPENTINA −18.5, PROPOFOL −16.1.

### Altas de licitación +84.1 (Gob FC) — detalle

Fuente: `Familias!S` donde `es_lanzamiento_familia = 0` (reconcilia exacto a +84.109; 243 familias). Son familias que aparecen en H1'26 sin base H1'25 (nuevas adjudicaciones/contratos, no lanzamientos):

| # | Molécula (alta) | +$M |
|---|---|---:|
| 1 | PROPOFOL | +12.587 |
| 2 | PALMITATO DE VIT. A + COLECALCIFEROL | +9.287 |
| 3 | CLORHIDRATO DE SITAGLIPTINA | +8.713 |
| 4 | TELMISARTAN | +5.783 |
| 5 | CARBOPLATINO | +5.184 |
| 6 | MULTIVITAMINICO | +4.125 |
| 7 | ACIDO CLAVULANICO + AMOXICILINA | +3.480 |
| 8 | SULFATO DE MORFINA | +3.148 |
| 9 | NAPROXENO | +2.706 |
| 10 | GLUCOSA | +2.460 |

Contraparte — **Bajas −64.6** (top): SERTRALINA −13.5, PARACETAMOL −7.2, SOMATROPINA −4.6, OLANZAPINA −4.3, ENOXAPARINA −3.7, ALFA CETOANALOGOS −3.0, SITAGLIPTINA −2.7. Gestión neta = 84.109 − 64.579 = **+19.530**.

---

## 8. Hospitales — Terceros / VARIOS +112.1 — ¿qué materiales/equipos?

Bloque 6 = **negocio distribuido, no manufactura PiSA**. Descompone en:
- **+38.637 M** = los **58 materiales reclasificados C7** (salen del core). Detalle nominal en la hoja *Detalle Terceros C7*.
- **+73.43 M** = **VARIOS nativo** (nunca estuvo en core; muchas filas con `molecula = None` en Familias, por eso el detalle nominal vive en Datos Maestro/hoja C7, no en el agregado por molécula).

**Movedores nombrados (hoja Detalle Terceros C7, continuas — marcas originadoras / biológicos de tercero):**

| MATNR | Material | Δ movida $M | V25→V26 H1 |
|---|---|---:|---|
| 4043923 | **KEYTRUDA** 100MG/4ML (pembrolizumab) | **+28.579** | 47.01 → 75.59 |
| 4059977 | ENHERTU (trastuzumab deruxtecan) 100MG | +6.094 | 4.11 → 10.20 |
| 4050157 | TECENTRIQ 1200MG/20ML | +5.158 | 1.04 → 6.20 |
| 4024350 | PERJETA 420MG/14ML | +4.241 | 11.63 → 15.88 |
| 4032867 | KADCYLA 160MG/8ML | +3.412 | 3.14 → 6.56 |
| 4036074 | GAZYVA 1000MG/40ML | +1.832 | 4.44 → 6.27 |
| 4041813 | OPDIVO 100MG/10ML | +1.811 | 12.64 → 14.45 |
| 4050053 | OCREVUS 300MG/10ML | +1.323 | 9.55 → 10.88 |
| 4005991 | HERCEPTIN 440MG/20ML | +1.043 | 9.60 → 10.65 |

Bajan (continuas): DARZALEX 400MG −6.415, ADCETRIS −3.626, MABTHERA 500MG −1.776, POLIVY −1.605.
**Altas C7** (+4.752): TRODELVY +3.026, SOLIRIS +1.210, PERJETA-GOB, ROACTEMRA, REMSIMA, MVASI.
**Bajas C7** (−2.605): RYBREVANT −0.845, LEMTRADA −0.815, JEVTANA −0.498, STELARA −0.329.

**Equipos/consumibles de tercero** presentes en el pool: INFUSOMAT SPACE NEUTRAPUR SAFESET (set de infusión B.Braun, −1.211), solución para diálisis peritoneal (+2.163), detergente polienzimático (+0.053).

**VARIOS nativo grande no listado en C7:** SUTIVIN 1MG/10ML (VINCRISTINA, matnr 4045766) **+28.579** — coincide en magnitud con KEYTRUDA pero es un material distinto (verificado en Datos Maestro; sin doble conteo).

Naturaleza dominante del +112.1: **portafolio oncológico/inmunológico de marcas originadoras y biosimilares que PiSA distribuye**, encabezado por KEYTRUDA (+28.6) y un bloque de anticuerpos monoclonales.

---

## 9. Vacíos / caveats

- **G1–G6 siguen pendientes de descubrimiento** — los propios INSIGHTS lo dicen ("esta ronda no los cierra"). Solo G5b se reporta como cobertura técnica sin cambio. La cobertura del core es 65.0% (Hosp) / 78.9% (Gob) del bruto elegible: **35% / 21% del bruto no está en el puente normalizable** y vive en bloques por valor (Terceros, Serie 9, Sin unidad).
- **Detalle nominal del VARIOS nativo (+73.4 Hosp) es parcial** en el agregado por molécula: muchas filas cargan `molecula = None` (marcas de tercero sin mapeo en el diccionario). El material-por-material completo está en Datos Maestro y en la hoja Detalle Terceros C7, no en el resumen.
- **La columna Volumen de *Ranking Franquicias* NO reconcilia al bloque 2** (usa otra descomposición; suma +443.3 vs +425.2 en Gob, +3.0 vs +26.3 en Hosp). Para volumen por molécula usar `Familias!Q`. Su columna **Mix sí reconcilia**.
- **Redondeo sub-peso CSV vs cubo:** −$0.54 (Hosp) / −$1.05 (Gob) en el movimiento C7; documentado, sin material faltante.
- Estos dos segmentos son parte del consolidado; falta cruzarlos contra Privado (Δ +58.65) y Gob Servicios para el número PiSA total. No están en el alcance de esta verificación.

---

*Verificado por recálculo LibreOffice sobre copia; originales intactos. Cifras a máxima precisión almacenada. Fuente: workbooks FINAL 2026-07-16; `apply_c7_terceros.py`; `terceros_overrides.csv` (SHA-256 31959f…637a7); INSIGHTS canónicos MD/DOCX.*
