# EXTRACT — Verificación puentes de venta: Consolidado PiSA + Gob Servicios

**Fuente verificada:** `/Users/rafaelprince/Downloads/PVM_Reconstruido_scripts/v2/`
- `Downtrading_PiSA_Consolidado_FINAL_2026-07-16.xlsx` (md5 `87e3fc28…c39`)
- `Downtrading_GobServicios_FINAL_2026-07-16.xlsx` (md5 `1139a969…4f2`)

**Método de verificación.** Los originales se entregan FORMULADOS (fórmulas vivas; `openpyxl data_only` → None). Se copió cada archivo a scratchpad (md5 idéntico al original, originales intactos) y se recalculó con LibreOffice headless (`soffice --convert-to xlsx`) forzando *Recalculation on File Load = Always* vía perfil temporal (`OOXMLRecalcMode=0`). Los valores mostrados son los recalculados de las fórmulas vivas. Verificación de integridad hecha en Python sobre el recalculo.

**Veredicto global: TODO CUADRA.** 0 desviaciones contra las cifras esperadas de los INSIGHTS canónicos. Todos los controles internos (`CONTROL`, `Σ bloques − Δ`) cierran en 0.0000. Fecha corrida 2026-07-16.

---

## 1. Estructura de hojas

### Consolidado (`Downtrading_PiSA_Consolidado_FINAL`)
| Hoja | Dims | Rol |
|---|---|---|
| `Datos Consolidado` | A1:J42 | Trazabilidad por celda: 41 líneas, cada componente×segmento con archivo fuente + hoja + celda origen + método + nota |
| `Resumen Consolidado` | A1:G29 | Matriz 8 componentes × 4 segmentos + conciliación de 3 niveles + cobertura + método |

El Consolidado **transcribe** los 4 puentes de segmento (no re-calcula), salvo la Δ FULL del cubo que **sí recomputa de primera mano** (celda G23/G38).

### GobServicios (`Downtrading_GobServicios_FINAL`)
| Hoja | Dims | Rol |
|---|---|---|
| `Resumen Ejecutivo` | A1:C31 | Puente por VALOR, 4 bloques MECE + Lanzamientos=0 + conciliación |
| `Datos Hechos` | A1:M2861 | Universo material-nivel (2,856 materiales, partición MECE) — motor de fórmulas |
| `Bloque A Servicios` | A1:F27 | Serie 9 sin unidad física (Hemodiálisis, Anestesia, Quirófano, Contable) + top SKU |
| `Bloque B Canastas` | A1:F27 | Canastas VARIOS (ONCOLOGICOS, ANTIMICROBIANOS, NPT…) + top SKU |
| `Bloque C Dialisis` | A1:G13 | Pool diálisis peritoneal (6 SKU) por valor + piezas |
| `Anexo Dialisis PVM` | A1:M27 | P/V/M real por PIEZA (bolsa) del pool de diálisis |
| `Bloque D Molecula` | A1:F165 | Resto molécula-específica agregado por molécula nativa (continuas/altas/bajas) |
| `Aristas Sucesion` | A1:G24 | 5 aristas de cosido SKU no-GOB→GOB (evidencia del cosido E6) |
| `Lanzamientos` | A1:E18 | Los 13 lanzamientos autoritativos, todos 0 en el canal |
| `Consignacion (info)` | A1:B8 | Línea informativa piezas a valor cero (no toca el puente) |

---

## 2. Consolidado — matriz 8 × 4 (hoja Resumen Consolidado)

Fila TOTAL PiSA = suma de los 4 segmentos. **Verificación de integridad: cada línea Σ(4 seg) = columna TOTAL, exacto.**

| # | Componente | Privado | Hospitales | Gob FC | Gob Serv | **TOTAL** | Esperado | ✓ |
|---:|---|---:|---:|---:|---:|---:|---:|:--:|
| 1 | Precio (core) | 392.9498 | −5.7169 | −320.3213 | — | **66.9116** | 66.9 | OK |
| 2 | Volumen (core) | −169.7100 | 26.2626 | 425.2145 | — | **281.7671** | 281.8 | OK |
| 3 | Mix / down-trading | −197.8992 | −14.4679 | −84.6006 | — | **−296.9676** | −297.0 | OK |
| 4 | Gestión portafolio | 0.2255 | 8.2703 | 19.5304 | — | **28.0263** | 28.0 | OK |
| 5 | Lanzamientos 2026 | 71.1360 | 23.1472 | 0.1545 | 0.0000 | **94.4377** | 94.4 | OK |
| 6 | Terceros / VARIOS | — | 112.0688 | −53.3094 | 36.7266 | **95.4860** | 95.5 | OK |
| 7 | Servicios / serie 9 | — | 7.8468 | −10.3854 | 54.3203 | **51.7816** | 51.8 | OK |
| 8 | PiSA por valor / sin unidad | −38.0478 | −3.6260 | −1.1790 | −6.5244 | **−49.3772** | −49.4 | OK |
| | **Δ reclasificada (Σ)** | **58.6543** | **153.7849** | **−24.8962** | **84.5225** | **272.0654** | 272.1 | OK |

- Δ por segmento esperada **58.7 / 153.8 / −24.9 / 84.5 = 272.1** → 58.6543 / 153.7849 / −24.8962 / 84.5225 = **272.0654** → **OK** (redondeo 1-dec exacto).
- Verificación cruzada: cada **columna** de segmento suma sus 8 líneas = su Δ (los 4 en True).
- Core PiSA PVM (L1+L2+L3 TOTAL) = 66.9116 + 281.7671 − 296.9676 = **+51.71 M** → confirma el claim del INSIGHT "el core PVM aporta solo +51.7 M". **OK**
- Privado core PVM = 392.9498 − 169.71 − 197.8992 = **+25.34 M** (INSIGHT +25.3) **OK**.
- Hospitales core (P+V+M+Gestión) = −5.7169 + 26.2626 − 14.4679 + 8.2703 = **+14.35 M** (INSIGHT +14.3) **OK**.

**Nota de guiones:** líneas 1–4 en Gob Servicios muestran "—" (no admite P/V/M por unidades). Líneas 6–7 en Privado muestran "—" (sin capa de terceros por diseño). Consistente con INSIGHT.

---

## 3. Consolidado — conciliación de 3 niveles (columna TOTAL)

| Paso | Privado | Hospitales | Gob FC | Gob Serv | **TOTAL** | Esperado | ✓ |
|---|---:|---:|---:|---:|---:|---:|:--:|
| N1 — Δ reclasificada | 58.6543 | 153.7849 | −24.8962 | 84.5225 | **272.0654** | 272.1 | OK |
| (−) Reclas. nov-dic 2025 | −27.3073 | −4.4127 | 0 | 0 | **−31.7200** | −31.7 | OK |
| N2 — Δ con MATNR | 31.3470 | 149.3721 | −24.8962 | 84.5225 | **240.3454** | 240.3 | OK |
| (±) Filas sin MATNR | 0.4131 | −1.4565 | 0 | 0 | **−1.0434** | −1.0 | OK |
| N3 — Δ sell-in completo cubo | 31.7601 | 147.9156 | −24.8962 | 84.5225 | **239.3020** | 239.3 | OK |
| Check independiente cubo | | | | | **239.3020** | 239.3 | OK |
| **CONTROL (N3 − cubo)** | | | | | **0.0000** | 0 | OK |

- Cadena esperada **272.1 − 31.7 = 240.3 → ± (−1.0) = 239.3 sell-in oficial** reproducida al peso: 272.0654 − 31.7200 = 240.3454 − 1.0434 = **239.3020**. **OK**
- Δ FULL recomputado de primera mano sobre el cubo: **H1-25 $16,279,197,392.13 → H1-26 $16,518,499,352.29 = +$239,301,960.16** (celda Datos Consolidado R38). CONTROL = 0.0000. **OK**

---

## 4. Consolidado — cobertura / sensibilidad impresa (R26)

Texto literal de la hoja Resumen Consolidado, celda A26:
- **Privado: 96.0%** del bruto (sin capa de terceros, por diseño). → esperado 96.0% **OK**
- **Hospitales: 65.0%** del bruto elegible (G5b técnico **72.88%**). → esperado 65% **OK**
- **Gob FC: 78.9%** del bruto elegible (G5b técnico **81.71%**). → esperado 78.9% **OK**
- **Gob Servicios:** excluido del P/V/M por unidades por diseño (45.6% del bruto sin molécula ni unidad; techo G5b elegible **73.66% < 85%**); puente 100% por valor.

Las tres cifras esperadas 65% / 78.9% / 96.0% están impresas y correctas; además trae los techos técnicos G5b (72.88 / 81.71 / 73.66) como capa de sensibilidad. **OK**

---

## 5. Consolidado — hoja Datos Consolidado (trazabilidad por celda)

Mapa de 41 líneas `id | línea | componente | segmento | valor | archivo fuente | hoja | celda | método | nota`. Cada valor de la matriz apunta a su celda origen en el workbook de segmento. Hallazgos de traza:

- **Precio/Volumen/Mix/Gestión** de Privado → `Downtrading_Privado_v4_FINAL_2026-07-15.xlsx` hoja `Resumen Ejecutivo` (B5/B6/B7); Hosp y Gob FC → `…Hospitales_v4_FORMULADO` / `…GobFC_v4_FORMULADO` `Resumen Ejecutivo` B5/B6/B7/B8.
- **Gestión Privado se descompone en 2 filas** (id 10/11): *bajas* B14 = **−106.6374** + *sustituciones/altas no lanzamiento* B15 = **+106.8630** → neto **+0.2255** (= L4 Privado de la matriz). Relevante para §7 (el −106.6 es distinto del piso −107.3).
- **Terceros Gob FC** (id 19) nota: incluye **KETOSTERIL +30.05 / BIOYETIN −33.24** (INSIGHT los cita +30.1 / −33.2; redondeo, **OK**).
- **Gob Servicios línea 8** se compone de id 27 *Diálisis peritoneal* **+69.4245** + id 28 *Resto molécula* **−75.9490** = **−6.5244** (= L8 Gob Serv de la matriz). **OK**
- **Anexo diálisis** (id 38/39/40): P **+96.1587** / V **−8.6191** / Mix formato **−18.1151**; sub-familia Hemodiálisis (id 41) **+64.4618** (9000915 aporta +61.47).
- Fuentes de segmento: Privado `v4_FINAL`; Hospitales / Gob FC `v4_FORMULADO` (en `ext_segmentos/build/…`); Gob Servicios `Downtrading_GobServicios_valor_v1.xlsx`.
- Nota de traza id 33: el valor "filas sin MATNR" Privado (+0.4131) quedó *frozen* en el FORMULADO (el FINAL fue recortado a B38); no afecta números.

---

## 6. GobServicios — verificación por bloque

Δ del segmento esperada **+84.5225** → Resumen Ejecutivo B21/B22 = **84.5225**, CONTROL (B23) = **0.0000**. **OK**

| Bloque | Celda | Valor | Esperado | ✓ |
|---|---|---:|---:|:--:|
| 1. Servicios (serie 9) | B5 | **54.3203** | +54.32 | OK |
| — Hemodiálisis | B6 | **64.4618** | HD +64.46 | OK |
| — 9000915 SERVICIOS DE HEMODIALISIS | Bloque A R13 Δ | **61.4740** | material +61.47 | OK |
| 2. Canastas VARIOS | B10 | **36.7266** | VARIOS +36.73 | OK |
| — ONCOLOGICOS / ANTIMICROB. / NPT / otros | B11-B14 | 52.9608 / −7.6640 / −3.5623 / −5.0078 | Σ=36.73 | OK |
| 3. Diálisis peritoneal (pool) | B15 | **69.4245** | DP +69.42 | OK |
| 4. Resto molécula-específica | B16 | **−75.9490** | −75.95 | OK |
| — Continuas / Altas / Bajas | B17-B19 | −97.3235 / 26.8794 / −5.5049 | Σ=−75.95 | OK |
| 5. Lanzamientos (13 autoritativos) | B20 | **0.0000** | 0 | OK |

**Anexo Diálisis PVM (cierra contra Δ bloque 3):**
| Efecto | Celda | Valor | Esperado | ✓ |
|---|---|---:|---:|:--:|
| (P) Precio | B20 | **96.1587** | +96.16 | OK |
| (V) Volumen (piezas) | B21 | **−8.6191** | −8.62 | OK |
| (M) Mix de formato | B22 | **−18.1151** | −18.12 | OK |
| Σ P+V+M | B23 | **69.4245** | =Δ bloque C | OK |
| CONTROL anexo | B25 | **0.0000** | 0 | OK |

Piezas (bolsas): 9,879,454 → 9,751,697 = **−1.29%** (INSIGHT "bolsas −1.3%"; valor +10.4% ⇒ historia de precio). **OK**

**Detalle molécula (Bloque D):**
- Pembrolizumab (continua, molécula nativa) = 131.4824 − ... net **−60.4117** (KEYTRUDA no-GOB 4043923 −77.5695 + GOB 4064238 +17.1577). Esperado Pembrolizumab −60.41. **OK**
- Altas de licitación/contrato = **+26.8794** (12 moléculas). Esperado +26.88. **OK**
- **OCRELIZUMAB = +18.8844** (mayor alta, biosimilar OCREVUS a gobierno). Esperado Ocrelizumab +18.88. **OK**. Sigue DOXORUBICINA/ZODOX +3.7366.

**Aristas de sucesión (cosido E6):** MAMITRA 4065590 +17.9499 (sucede a Trazimera en Trastuzumab), Opdivo GOB 4063930 +5.6624 / 4063931 +0.5110 (Nivolumab), ENHERTU 4060230 +22.6605. Sin cosido serían altas espurias; neteadas por molécula nativa (Trastuzumab, Nivolumab) no distorsionan el puente. Consistente con INSIGHT.

**Consignación (info):** 1,812 materiales, 6,404 filas, **5,835,918 piezas a valor 0** — no toca el puente de valor. Consistente con INSIGHT (5.84 M piezas a $0).

---

## 7. Dónde vive y cómo se define el "piso citable −$107.3 M" del down-trading de Privado

**NO vive en los dos workbooks verificados** (Consolidado y GobServicios sólo cargan el Mix central de Privado −197.9 M). Es una cifra de **documentación/spec**, no una celda de estos entregables.

**Definición (SPEC_PVM_UNIDADES_v2.md §7.4 — gate G4):** el Mix de Privado se calcula en tres variantes de la banda de sensibilidad:
- (i) **Todo el maestro** = −197.90 M
- (ii) **Sin confianza baja** = −197.90 M
- (iii) **Solo confianza alta** = variante sensible

La **regla de cita ejecutiva** (SPEC línea 513): *"el piso citable = MÍNIMO ENTRE VARIANTES del cálculo, NUNCA el endpoint sensible en sí (cifra final: piso −$107.3 M)"*. El piso es la variante (iii) solo-confianza-alta calculada **pre-arista de sucesión FRISO** = **−107.26 M ≈ −107.3 M**. Banda del verificador = **[−201.27, −107.28]**, central −197.9 M.

**Caveat crítico:** el −107.3 es una **SENSIBILIDAD COMPOSICIONAL, NO un piso de intervalo de confianza**. El endpoint (iii) es estructuralmente sensible a la definición de familia: una sola arista documental (sucesión FRISO §5.5) lo mueve **−37.1 M (34.6% de su valor pre-arista)** por mecánica Shapley legítima (redistribución de shares al entrar la familia tarima barata a un pool que se contrae; no es pérdida económica incremental).

**Dónde vive exactamente:**
- **Canónico:** `SPEC_PVM_UNIDADES_v2.md` §7.4 (líneas 3, 513, 568, 666): *"Mix central −$197.9 M · piso mínimo entre variantes −$107.3 M"*.
- **Tabla de variantes:** `REPORTE_downtrading_privado_v2.md` L307 (`Mix total (iii) solo alta | −107.26M (sin arista) | −144.38M (con arista) | −37.12M`) y banda [−201.27, −107.28] (L309).
- **Handoff:** `HANDOFF_downtrading_lanzamientos_2026-07-15.md` L64: *"Piso citable del Mix = −107.3 (solo-alta; es sensibilidad composicional, NO piso de intervalo)"*.
- **En el workbook Privado v4 FINAL** (`Resumen Ejecutivo` bloque "Sensibilidad del Mix", A18:B21): la celda viva **(iii) Solo confianza alta = B21 = −144.3799** (POST-arista, modelo final). El −107.3 es el mismo endpoint **pre-arista**; NO figura como celda en el workbook. Ojo: no confundir con B14 = **−106.6374** (bajas de gestión, cifra distinta y sin relación con el piso).

**Lectura para el Consejo:** citar Mix central **−197.9 M**; si se quiere piso conservador, **−107.3 M** con la etiqueta "mínimo entre variantes / sensibilidad composicional", nunca como cota inferior estadística.

---

## 8. Hallazgos y vacíos

1. **Cero desviaciones numéricas.** Las 8 líneas × 4 segmentos, la Δ por segmento (272.1), la conciliación de 3 niveles (272.1 → 240.3 → 239.3), el check independiente del cubo (239.3020, CONTROL 0), y todos los bloques de GobServicios coinciden al 4.º decimal con los INSIGHTS. Todos los controles cierran en 0.0000.
2. **Consolidado = transcripción, no motor.** Las 32 líneas de matriz se copian de los 4 workbooks de segmento (Privado v4_FINAL; Hospitales/Gob FC v4_FORMULADO; Gob Servicios valor_v1). Lo único recomputado in-situ es la Δ FULL del cubo (239.3020). Implicación: la integridad del Consolidado depende de que esos 4 workbooks fuente sigan congelados; la hoja Datos Consolidado da la traza celda-a-celda para auditarlo.
3. **El −107.3 M no está en estos entregables.** Vive en SPEC/REPORTE/HANDOFF de Privado. En el workbook Privado la variante viva análoga es −144.38 (post-arista). Si el deck del Consejo cita −107.3, la fuente es la spec, no el Excel Consolidado.
4. **Etiqueta de versión rezagada (cosmética, no numérica):** el workbook Privado v4_FINAL rotula internamente "Down-trading Privado v3" (Resumen Ejecutivo A1) y la hoja Datos Consolidado nota "Down-trading Privado v3" en algún encabezado del linaje; los números son los v4. No afecta cifras.
5. **Gob Servicios 100% por valor por diseño** (45.6% del bruto sin molécula/unidad; techo G5b 73.66% < 85%): no hay P/V/M por unidades salvo el pool de diálisis peritoneal (único pool limpio, 6 SKU). El crecimiento del segmento (+84.5) lo carga un servicio sin unidades (hemodiálisis 9000915 +61.47 = 72.7% de la Δ), no una molécula.
6. **Sin vacíos de datos detectados** en el alcance pedido. Único punto de atención metodológico: el piso −107.3 debe citarse siempre con su caveat composicional para no leerse como intervalo de confianza.
