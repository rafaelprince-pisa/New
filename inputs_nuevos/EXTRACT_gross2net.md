# EXTRACT — Gross2Net.xlsx (palancas Bruto→Neto por segmento, 1S25 vs 1S26)

**Fuente:** `/Users/rafaelprince/Downloads/Gross2Net.xlsx` (12.7 KB, recibido 16-jul-2026 17:18)
**Alcance:** Farma MX, periodo Ene–Jun (1S), comparativo 2025 vs 2026.
**Método de extracción:** openpyxl `read_only`+`data_only` (valores cacheados presentes) y openpyxl formulas view. No requirió recálculo con LibreOffice: todas las fórmulas traían caché válido. Original intacto.
**Verificación de cuadre:** los tres anclajes de la v18 de Finanzas cierran al centavo (ver §Cuadre). Cruce independiente contra `EXTRACT_edo_resultados_jun26_v18.md` líneas 234–235: coincidencia exacta por segmento.

---

## 1. Estructura del archivo

Una sola hoja: **"Gross 2 Net"**. 31 filas, 6 columnas. Sin celdas combinadas. Tres bloques apilados verticalmente:

| Bloque | Filas | Contenido | Cortes |
|---|---|---|---|
| **1. EBITDA** | 2–8 | EBITDA $ y % por segmento | 4 segmentos del deck · 2025 vs 2026 |
| **2. Gross-to-Net por segmento** | 11–21 | NC comerciales y sanciones + Devoluciones | 4 segmentos + subsegmentos de Retail · 2025 vs 2026 |
| **3. Farmacias por negocio** | 25–31 | NC comerciales y sanciones + Devoluciones | Consumo / Friso / RX / MP · 2025 vs 2026 |

**Conceptos disponibles:** solo dos líneas de deducción — (a) **"NC comerciales y sanciones"** y (b) **"Devoluciones"**. NO hay línea separada de "NC logísticas", ni desglose de sanciones aparte de NC comerciales, ni piezas/volumen. El corte es semestral (1S completo), NO mensual.

**Layout de columnas** (nota de trampa): en el bloque 1 las columnas van 2025-$, 2025-%, 2026-$, 2026-%. En los bloques 2 y 3 el orden es distinto: **col C = 2025, col D = 2026** (NC), **col E = 2025, col F = 2026** (Devoluciones). Los años NO están apareados igual entre bloques.

---

## 2. Bloque 1 — EBITDA por segmento (1S, $ y %)

| Segmento | EBITDA $ 1S25 | EBITDA % 1S25 | EBITDA $ 1S26 | EBITDA % 1S26 | Base implícita 1S26 ($/%) |
|---|---:|---:|---:|---:|---:|
| Retail (Expansión, Impulso, Farmacias) | 2,236.8 | 31.16% | 2,482.5 | 34.43% | 7,210.3 |
| Gobierno (FC) | 379.3 | 9.34% | 482.9 | 11.97% | 4,034.3 |
| Hospitales | 1,092.7 | 37.59% | 1,198.1 | 39.20% | 3,055.9 |
| Servicios | 184.8 | 8.66% | 321.8 | 14.50% | 2,219.4 |
| **Suma bases implícitas 1S26** | | | | | **16,519.8** |

Cifras exactas EBITDA $ 1S26: Retail 2,482,549,289 · Gobierno 482,916,345 · Hospitales 1,198,055,257 · Servicios 321,756,558.

**Lectura:** la "base implícita" (EBITDA $ ÷ EBITDA %) = Venta Neta por segmento. Suma = **16,519.8 $M = ancla Venta Neta 1S26** exacto. Confirma que el denominador del margen es la Venta Neta y da el split de venta por segmento:

| Segmento | Share Venta Neta 1S26 | (deck 44/24/18/13) |
|---|---:|---:|
| Retail | 43.6% | 44 |
| Gobierno FC | 24.4% | 24 |
| Hospitales | 18.5% | 18 |
| Servicios | 13.4% | 13 |

Coincide con los bloques del storyline v5/v6. Además, **este archivo separa Gobierno FC (4,034.3) de Servicios (2,219.4)** — el HUECO CRÍTICO que la v18 de Finanzas no podía resolver (ahí ambos vivían dentro de un único bloque GOBIERNO). Aquí sí están partidos, tanto en EBITDA como en las dos líneas de deducción.

**Salto de margen 1S25→1S26 (pp):** Retail +3.3 · Gobierno FC +2.6 · Hospitales +1.6 · Servicios +5.8. Servicios es el que más expande margen; Gobierno FC casi lo triplica en nivel absoluto de EBITDA % (9.34%→11.97%).

---

## 3. Bloque 2 — Gross-to-Net por segmento ($M, 1S)

Etiqueta literal de columnas en el archivo: **"NC comerciales y sanciones"** y **"Devoluciones"**. Signo negativo = deducción.

| Segmento | NC com. y sanciones 1S25 | 1S26 | Δ | Devoluciones 1S25 | 1S26 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| **Retail** | −426.6 | −488.1 | −61.4 (+14.4%) | −232.6 | −240.8 | −8.2 (+3.5%) |
| &nbsp;&nbsp;Farmacias | −373.7 | −412.0 | −38.3 (+10.3%) | −197.7 | −188.5 | +9.2 (−4.6%) |
| &nbsp;&nbsp;&nbsp;&nbsp;Contractual* | −160.7 | −177.2 | −16.5 (+10.3%) | — | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Discrecional* | −213.0 | −234.9 | −21.8 (+10.3%) | — | — | — |
| &nbsp;&nbsp;Impulso | −42.1 | −59.5 | −17.4 (+41.3%) | −20.7 | −40.4 | −19.8 (+95.6%) |
| &nbsp;&nbsp;Expansión | −10.8 | −16.5 | −5.7 (+53.0%) | −14.2 | −11.8 | +2.4 (−16.8%) |
| **Gobierno (FC)** | −103.0 | −111.7 | −8.7 (+8.5%) | −729.7 | −531.5 | +198.2 (−27.2%) |
| **Hospitales** | −24.3 | −24.5 | −0.3 (+1.2%) | −59.7 | −73.4 | −13.7 (+22.9%) |
| **Servicios** | −0.0006 | −1.1 | −1.1 | −2.6 | −3.7 | −1.1 (+43.6%) |
| **TOTAL** | **−553.8** | **−625.4** | **−71.6 (+12.9%)** | **−1,024.6** | **−849.4** | **+175.2 (−17.1%)** |

\* **Contractual / Discrecional es un supuesto modelado, NO dato observado.** Las celdas son fórmulas: Contractual = Farmacias NC × 43%, Discrecional = Farmacias NC × 57% (hardcoded, mismo ratio 2025 y 2026). Por eso ambos crecen exactamente +10.3%, idéntico a Farmacias total. El split 43/57 es una asignación fija, no una medición. Solo aplica a la línea NC; en Devoluciones no hay split Contractual/Discrecional.

Cifras Retail (fila 13), Farmacias (fila 14), Impulso (fila 17), Expansión (fila 18) son fórmulas de suma verificadas (Retail = Farmacias + Impulso + Expansión, cuadra exacto en las 4 columnas).

**Lecturas de negocio:**
- **La palanca que se movió de verdad es Devoluciones de Gobierno FC:** −729.7 → −531.5, una mejora de +198.2 $M (−27.2%). Explica por sí sola casi todo el −175.2 $M de mejora del total de devoluciones. Concentra la narrativa de "menos devoluciones" del segmento gobierno.
- **NC comerciales sube +12.9% (−71.6 $M),** empujado por Retail (+61.4) — dentro de Retail, Impulso (+41.3%) y Expansión (+53.0%) crecen mucho más rápido que Farmacias (+10.3%).
- **Impulso deteriora en las dos líneas:** NC +41.3% y Devoluciones +95.6% (casi se duplican). Bandera de calidad de venta en Impulso.
- **Hospitales:** NC casi plano (+1.2%) pero Devoluciones +22.9%. Servicios es material solo en devoluciones (−3.7) y trivial en NC.

---

## 4. Bloque 3 — Farmacias por negocio ($M, 1S)

Farmacias (fila 27) = referencia directa a Farmacias del bloque 2 (fórmula =C14). Cuadra exacto; los 4 negocios suman a Farmacias en las 4 columnas.

| Negocio | NC com. y sanciones 1S25 | 1S26 | Δ | Devoluciones 1S25 | 1S26 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Consumo | −43.6 | −41.0 | +2.6 (−5.9%) | −21.4 | −22.2 | −0.8 (+3.7%) |
| Friso | −45.1 | −41.1 | +4.0 (−8.9%) | −25.5 | −23.3 | +2.2 (−8.8%) |
| RX | −190.4 | −161.3 | +29.1 (−15.3%) | −88.3 | −96.5 | −8.3 (+9.4%) |
| MP | −94.6 | −168.6 | −74.0 (+78.3%) | −62.5 | −46.5 | +16.0 (−25.6%) |
| **Farmacias** | **−373.7** | **−412.0** | **−38.3 (+10.3%)** | **−197.7** | **−188.5** | **+9.2 (−4.6%)** |

**Lecturas:**
- **MP (Marca Propia) es el driver del alza de NC en Farmacias:** +78.3% (−74.0 $M). Sin MP, la NC comercial de Farmacias habría BAJADO (Consumo/Friso/RX todos mejoran). MP explica y supera el deterioro del segmento.
- **RX baja NC −15.3%** pero sube Devoluciones +9.4%.
- El alivio de Devoluciones de Farmacias (+9.2 $M, −4.6%) viene de MP (+16.0) parcialmente compensado por RX (−8.3).

---

## 5. Mapeo a Estado de Resultados v18 (terminología)

Las dos líneas de este archivo mapean 1:1 a las líneas del ER de Finanzas. **Verificado por totales Y por segmento** (cruce con `EXTRACT_edo_resultados_jun26_v18.md` líneas 234–235):

| Etiqueta en Gross2Net | Línea en ER v18 (Finanzas) | Total 1S26 | Cuadre |
|---|---|---:|---|
| "NC comerciales y sanciones" | **Descuentos** (línea 16) | −625.4 | Exacto (Δ −0.01 $M redondeo) |
| "Devoluciones" | **Devoluciones y rechazos** (línea 15) | −849.4 | Exacto (Δ −0.04 $M redondeo) |

Cruce por segmento (ER v18 vista nativa 6 bloques, 1S26). La única diferencia es que **Finanzas pliega Servicios dentro de Gobierno**; Gross2Net lo separa:

| | Gross2Net | ER v18 |
|---|---|---|
| Descuentos GOB+Serv | −111.7 + −1.1 = **−112.8** | GOB **−112.8** ✓ |
| Descuentos Impulso / Hosp / Farm / Exp | −59.5 / −24.5 / −412.0 / −16.5 | −59.5 / −24.5 / −412.0 / −16.5 ✓ |
| Devoluciones GOB+Serv | −531.5 + −3.7 = **−535.2** | GOB **−535.2** ✓ |
| Devoluciones Impulso / Hosp / Farm / Exp | −40.4 / −73.4 / −188.5 / −11.8 | −40.4 / −73.4 / −188.5 / −11.8 ✓ |

**Conclusión de terminología:** lo que el deck llama "NC comerciales" = línea Descuentos del P&L (bundle comercial + sanciones). Lo que aquí se llama "Devoluciones" = línea Devoluciones y rechazos del P&L. **El archivo aporta sobre la v18:** el corte 2025 por segmento y el desglose Servicios-vs-Gobierno FC, más el subdetalle de Retail y de Farmacias por negocio.

---

## 6. TABLA OBJETIVO para la columna 3 del deck (comparativo de palancas comerciales)

Existe, con matiz de etiqueta. El corte pedido era "NC comerciales y NC logísticas por segmento 1S25 vs 1S26". El archivo entrega **NC comerciales (y sanciones)** y **Devoluciones** — NO entrega "NC logísticas" como línea propia (ver §8). Con los cuatro segmentos del deck ya separados (Gobierno FC ≠ Servicios), la tabla deck-ready es:

| Segmento | NC comerciales 1S25 | NC comerciales 1S26 | Δ NC | Devoluciones 1S25 | Devoluciones 1S26 | Δ Dev |
|---|---:|---:|---:|---:|---:|---:|
| Retail (Farm+Imp+Exp) | −426.6 | −488.1 | +14.4% | −232.6 | −240.8 | +3.5% |
| Gobierno FC | −103.0 | −111.7 | +8.5% | −729.7 | −531.5 | −27.2% |
| Hospitales | −24.3 | −24.5 | +1.2% | −59.7 | −73.4 | +22.9% |
| Servicios | −0.0 | −1.1 | — | −2.6 | −3.7 | +43.6% |
| **Total Farma MX** | **−553.8** | **−625.4** | **+12.9%** | **−1,024.6** | **−849.4** | **−17.1%** |

Nota para el deck: la columna "NC comerciales" incluye sanciones (no separables) y en Gobierno es casi toda sanción (ver §7). Si el deck quiere tres columnas (NC comercial pura / sanciones / logísticas), **este archivo NO lo soporta**; solo dos buckets.

---

## 7. Sanciones de gobierno ($108M): MEZCLADAS, no separables

La columna se llama literalmente **"NC comerciales y SANCIONES"** — las sanciones están **bundleadas** dentro de la línea de NC comercial, no aisladas. Para Gobierno FC:
- NC comerciales y sanciones 1S26 = **−111.7 $M**. Si la sanción ronda −108 $M (transcript), casi todo este bucket sería sanción y quedaría muy poco de descuento comercial puro — coherente con la lógica de gobierno (no hay descuento comercial, hay penalización). **Pero no es descomponible desde este archivo.**
- 1S25 = −103.0 $M.

Las **330 devoluciones + 108 sanciones / 428 total (357 aplicadas + 71 pendientes)** del transcript son casi con certeza **conteos de notas de crédito (número), no pesos** — este archivo está en pesos y NO reconcilian con sus $M (ver §8 Choques). Declarado: la separación devoluciones-vs-sanciones-vs-comercial de gobierno NO existe en este archivo.

---

## 8. Inconsistencias / Choques / Vacíos

**VACÍOS (lo que el archivo NO trae):**
1. **NC logísticas como línea propia: NO existe.** No hay ninguna columna, fila ni total llamado "logísticas". Solo "NC comerciales y sanciones" y "Devoluciones".
2. **El −$100M de NC logísticas de Rafael: NO es visible en ningún corte.** No aparece aislado. Podría ser un subconjunto dentro de "Devoluciones" (devoluciones/rechazos por causa logística), pero el archivo no lo etiqueta ni lo separa. El total Devoluciones 1S26 es −849.4 $M, muy lejos de −100; no hay forma de derivar los −100 desde aquí. **Universo del −$100M sigue sin validar con esta fuente.**
3. **Sanciones de gobierno separadas: NO.** Bundleadas en "NC comerciales y sanciones" (§7).
4. **Sin corte mensual** — solo 1S agregado. Sin piezas/volumen (no reproduce PVM).
5. **Sin desglose de "NC comerciales" en comercial-puro vs sanción** para ningún segmento.

**CHOQUES / a reconciliar:**
6. **Transcript "NC gobierno 428 (−53% vs 25); 330 dev + 108 sanciones" NO reconcilia con los $M del archivo.** En pesos: Gobierno Devoluciones −729.7→−531.5 = −27.2% (no −53%); NC comerciales y sanciones −103.0→−111.7 = +8.5%. Ni 428, ni 330, ni 108 mapean a estas cifras. Interpretación más probable: los números del transcript son **conteos de NC (unidades)**, distinta métrica. Marcar para reconciliar con el equipo de gobierno (David Silva) antes de mezclar ambas fuentes en una misma lámina.
7. **Contractual/Discrecional (Farmacias) es supuesto 43/57 hardcoded, no observado** (§3). Ambos crecen +10.3% idéntico porque es un prorrateo fijo. Si el deck muestra "contractual vs discrecional" como hallazgo, hay que declarar que es una asignación, no una medición — o el partner lo va a marcar.

**CONSISTENCIAS (lo que SÍ cuadra):**
8. Sumas internas: Retail = Farm+Imp+Exp (4/4 columnas) ✓; Farmacias = Consumo+Friso+RX+MP (4/4) ✓; Farmacias = Contractual+Discrecional en NC (2/2) ✓.
9. Totales vs ER v18: Descuentos −625.4 ✓, Devoluciones −849.4 ✓, Venta Neta implícita 16,519.8 ✓ (los tres al centavo).
10. Cruce por segmento vs ER v18 líneas 234–235: exacto (con Servicios plegado en Gobierno del lado Finanzas) ✓.
11. Share de venta por segmento (base implícita EBITDA): 43.6/24.4/18.5/13.4 = 44/24/18/13 del deck ✓.

---

## 9. Verificación de cuadre contra anclas (OK / DESVIACIÓN)

| Ancla (ER v18, 1S26 Farma MX) | Valor ancla | Valor Gross2Net | Δ | Veredicto |
|---|---:|---:|---:|---|
| Descuentos = "NC comerciales y sanciones" | −625.4 | −625.41 | −0.01 | **OK** (redondeo) |
| Devoluciones = "Devoluciones" | −849.4 | −849.44 | −0.04 | **OK** (redondeo) |
| Venta Neta (suma bases EBITDA) | 16,519.8 | 16,519.8 | 0.0 | **OK** |
| Split segmento (44/24/18/13) | 44/24/18/13 | 43.6/24.4/18.5/13.4 | ~0 | **OK** |
| NC logísticas −100 (cifra Rafael) | −100 | no visible | n/a | **VACÍO — no isolable aquí** |
| Sanciones gobierno 108 | 108 (¿$? ¿conteo?) | dentro de −111.7 | n/a | **MEZCLADO — no separable** |
| Transcript gob 428/330/108 | conteos(?) | no mapea a $M | n/a | **CHOQUE — reconciliar unidad** |

**Nota:** Venta Bruta 17,994.7 − Devoluciones 849.4 − Descuentos 625.4 = 16,519.9 ≈ Venta Neta 16,519.8 (Δ +0.1 por redondeo del bruto). El puente bruto→neto cierra.

---

## 10. Notas de método (trampas para el siguiente que lo use)

- **Los años NO están apareados igual entre bloques.** Bloque 1: $2025/%2025/$2026/%2026. Bloques 2–3: NC-2025 / NC-2026 / Dev-2025 / Dev-2026. No copiar columnas ciegamente entre bloques.
- **Fórmulas presentes (12):** Retail (C13:F13) suma de subsegmentos; Contractual/Discrecional (C15:D16) = Farmacias×43%/57%; Farmacias bloque 3 (C27:F27) = referencia a Farmacias bloque 2. Todas con caché válido; no hubo que recalcular.
- **Servicios NC 2025 = −589 pesos** (−0.0006 $M), efectivamente cero. El +186,824% de crecimiento es artefacto de dividir entre casi-cero; reportar en absoluto (−0.0 → −1.1), no en %.
- **Signos:** todo negativo = deducción. En el deck, mostrar como magnitud positiva de "resta" o mantener el signo según la convención de la lámina de puente.
