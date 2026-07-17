# EXTRACT — P&L Gobierno (archivo maestro grande)

**Archivo fuente:** `/Users/rafaelprince/Downloads/Copy of P&L Gobierno .xlsx` (13.3 MB; OJO al espacio antes de `.xlsx`).
**Extraído:** 2026-07-16 · openpyxl 3.1.5 (read_only, data_only) · valores cacheados en el libro (no requirió recálculo en LibreOffice — ver nota de método).
**Autor del libro:** Felipe Medeles (firma en `Indicadores!C1`).
**Naturaleza:** NO es el split chico. Es el **modelo maestro de P&L de PiSA a nivel Grupo**, 23 hojas, vivo (pivotes GETPIVOTDATA + SUMIFS). El split chico (`PL Gobierno vs Servicios.xlsx`) es una **rebanada congelada** de la hoja `FarmaMX` de este libro.
**Periodo del snapshot:** Congelado en **Acumulado / Junio** (YTD-1S), parametrizable (`FarmaMX!F1="Acumulado"`, `F2="Junio"`). Toda cifra de P&L de este documento es **1S = YTD a junio, MXN nominales**, salvo PIN (que es plan **anual**).
**Unidades:** tablas en **$M** (millones de pesos) salvo indicación. Márgenes en % sobre Venta Neta de la propia columna.

> **Nota de método (LibreOffice):** el libro trae los valores cacheados de las fórmulas; se leyeron directo con `data_only=True`. La única columna con errores es **FARMA MX total (col P/N/T/X)**, que muestra `#REF!`/`#VALUE!` en las líneas de P&L. `#REF!` es una **referencia rota** (rango borrado), NO se arregla recalculando — por eso no se corrió LibreOffice sobre una copia (no habría cambiado nada). Se declara la columna FARMA MX como inservible para el P&L (ver §Vacíos). El original nunca se tocó.

---

## 1. Estructura completa — 23 hojas

| # | Hoja | Estado | Contenido | ¿Nuevo vs split chico? |
|---|---|---|---|---|
| 0 | `BC` | oculta | Base de comparación: **pesos de cada segmento dentro de Farma MX** (venta y costo) 2022–2026 | **SÍ** (§8) |
| 1 | `DS Gasto` | oculta | **Fuente de gasto SG&A** — pivote "P&L x Mercado" N1–N5, **mensual**, por mercado | **SÍ — data source** (§12) |
| 2 | `Hoja1` | oculta | Vacía | — |
| 3 | `Gasto Fijo` | oculta | Costo indirecto/fijo por sociedad (GETPIVOTDATA) | apoyo |
| 4 | `DS` | oculta | **Fuente de venta y devoluciones** — pivote División/ID RUN, **mensual** | **SÍ — data source** (§12) |
| 5 | `Dicc datos` | oculta | **Diccionario metodológico**: cada línea de P&L clasificada CF/CV con notas | **SÍ — método** (§12) |
| 6 | `FyV Resumen` | oculta | Resumen fuerza de ventas (link a `FyV Grupo`) | apoyo |
| 7 | `Indicadores` | oculta | **Capital de trabajo mensual por segmento** (cartera, inventarios, proveedores, activos) 2021–**ago-2025** | **SÍ** pero vintage viejo (§6.2) |
| 8 | `OP` | oculta | Tablero corto (links a `Grupo`) | apoyo |
| 9 | `Dashboard` / 10 `% Dashboard` | ocultas | Tableros de KPIs (WC, DPO, DSO) | apoyo |
| 11 | `Tablas` | oculta | Motor de tablas dinámicas (2,268 fórmulas) | apoyo |
| 12 | `Comp elec anual` / 13 `Comp anual` | ocultas | Comparativos anuales por línea | apoyo |
| 14 | `FyV Grupo` | oculta | Fuerza de ventas a nivel Grupo (SUMIFS) | apoyo |
| 15–17 | `Grupo`, `Elec`, `Elec LATAM` | ocultas | P&L consolidado Grupo / Electrolit / Electrolit LATAM | otros negocios |
| 18 | **`FarmaMX`** | **visible** | **P&L maestro Farma México por segmento — AQUÍ vive Gobierno + el split + todo lo nuevo** | **★ núcleo** |
| 19–22 | `FarmaINT`, `FarmaINT LATAM`, `S.Animal`, `Corporativo` | ocultas | P&L de las otras divisiones (misma plantilla) | otros negocios |

**Conclusión estructural:** el dato de Gobierno vive **íntegro en `FarmaMX`**. Es la única hoja visible y la fuente del split chico. Las demás hojas son (a) fuentes de datos [`DS`, `DS Gasto`, `Dicc datos`], (b) P&L de otras divisiones, o (c) motores de tablero. Para el Consejo, el 95% del valor nuevo está en `FarmaMX`.

---

## 2. `FarmaMX` — mapa de la hoja (mucho más rica que el split)

**Bloques de columnas (P&L en filas 6–204):**

| Cols | Bloque | Escenarios que trae |
|---|---|---|
| H–AA | **FARMA MX total** | REAL 2020–2026 + %VTAS + VAR + **PPTO 2026** + **PIN 2026** — *(pero roto, ver §Vacíos)* |
| AC–AV | **GOBIERNO combinado** | REAL 2020, 2021, 2022, 2023, 2024, 2025, 2026 + %VTAS + VAR + **PPTO 2026** + **PIN 2026** |
| AX–BA | IMPULSO | REAL 2020–2023 (parcial, truncado) |
| BB–BH | **Split 2026**: DP · SAFE · SANEFRO · SIA · FC · servicio | solo REAL 2026 |
| BI–BO | **Split 2025**: DP · SAFE · SANEFRO · SIA · FC · servicio | solo REAL 2025 |

Columnas clave: **AK=GOB REAL 2026 · AI=GOB REAL 2025 · AO=GOB PPTO 2026 · AS=GOB PIN 2026 (anual)** · BG=FC 2026 · BH=Servicios 2026 · BN=FC 2025 · BO=Servicios 2025.

**Filas (la diferencia grande con el split chico):** el split chico terminaba en **fila 131 = EBITDA UN**. Esta hoja **continúa 73 filas más**:

- **134–146 Corporativo** (Dirección, RRHH, Contraloría, Transformación, Finanzas, Auditoría, Seg. Industrial, PIN, Abastecimientos)
- **148–153 Otros Gastos** (Alta Dirección / Presidencia)
- **155 UAFIR UN después de Corpo** · **157 Nuevos Productos / 158 Gastos por Proyectos / 160 Proyectos por capitalizar**
- **162 UAFIR** · **165–168 D&A** · **170 EBITDA (final)** · **171 % margen**
- **179–180 UAFIR anualizado (May / Dic)**
- **183–204 INDICADORES FINANCIEROS**: NOPAT, Utilidad Neta, ROA, ROIC, Capital invertido, Activo operativo (Inventarios MP/PT, Cartera, PP&E, Intangibles), Pasivo operativo (Proveedores)

> Traducción para el Consejo: este archivo **sí baja hasta EBITDA final (804.8) y hasta ROIC / capital invertido**. El split chico se quedaba en EBITDA UN (808.4) sin corporativo ni retornos. **Aquí está lo que faltaba.**

---

## 3. VERIFICACIÓN del split contra este maestro — OK / desviaciones

Se reprodujo el split (FC/Servicios y las 4 sub-líneas) leyendo directo `FarmaMX`. **Resultado: cuadre exacto al peso en EBITDA UN.**

| Prueba (1S-2026, $M) | Split chico | Este maestro | Veredicto |
|---|---:|---:|---|
| GOB Venta Neta | 6,253.7 | 6,253.7 | ✅ exacto |
| GOB EBITDA UN | 808.4 | 808.4 | ✅ exacto |
| **FC EBITDA UN** | **484.8** | **484.8** | ✅ exacto |
| **Servicios EBITDA UN** | **323.6** | **323.6** | ✅ exacto |
| DP / SAFE / SANEFRO / SIA EBITDA UN | 127.9 / 74.4 / 108.6 / 12.7 | 127.9 / 74.4 / 108.6 / 12.7 | ✅ exacto |
| FC + Servicios = GOB (peso) | — | `484,779,834.37 + 323,620,047.09 = 808,399,881.46` = GOB | ✅ exacto |
| DP+SAFE+SANEFRO+SIA = Servicios | — | delta 0.00 | ✅ exacto |
| Fuerza de Ventas: sub-líneas = Servicios (180.2) | 180.2 | 180.2 | ✅ exacto |

**Veredicto de verificación: el split chico es fiel al maestro sin una sola desviación en EBITDA UN.** Todos los números que ya usábamos (484.8 / 323.6 y las 4 sub-líneas) están confirmados contra la fuente. La única zona donde la aditividad **se rompe** es **debajo de EBITDA UN** (línea "Gastos por Proyectos"), tema nuevo que el split chico no alcanzaba a ver — ver §10.

---

## 4. LO NUEVO #1 — P&L completo hasta EBITDA final, Corporativo y UAFIR

P&L 1S-2026, $M. GOB combinado + FC + Servicios + las 4 sub-líneas, **bajando hasta EBITDA final** (lo que el split chico no tenía).

| Línea (fila) | GOB26 | FC26 | Serv26 | DP | SAFE | SANEFRO | SIA |
|---|---:|---:|---:|---:|---:|---:|---:|
| EBITDA UN (131) | **808.4** | **484.8** | **323.6** | 127.9 | 74.4 | 108.6 | 12.7 |
| — % margen | 12.93% | 12.02% | 14.58% | 17.40% | 8.40% | 19.92% | 23.91% |
| Corporativo (134) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| UAFIR UN desp. Corpo (155) | 456.0 | 174.7 | 281.4 | 91.8 | 69.7 | 107.3 | 12.6 |
| Gastos por Proyectos (158/160) | 3.6 | 1.9 | 1.9 | 1.9 | 1.9 | 1.9 | 2.5 |
| UAFIR (162) | 452.4 | 172.8 | 279.5 | 89.9 | 67.8 | 105.5 | 10.0 |
| (+) D&A total (165) | 352.4 | 310.1 | 42.3 | 36.2 | 4.7 | 1.3 | 0.1 |
| **EBITDA final (170)** | **804.8** | **482.9** | **321.8** | 126.1 | 72.5 | 106.8 | 10.2 |
| — % margen | 12.87% | 11.97% | 14.50% | 17.14% | 8.19% | 19.58% | 19.13% |

**Dos lecturas clave:**
1. **Corporativo = 0 en `FarmaMX`.** Confirma que el EBITDA de Gobierno es **antes de corporativo de Grupo** (el corporativo vive en la hoja `Corporativo`, no se prorratea a segmentos aquí). No hay carga corporativa escondida en Gobierno.
2. **A nivel de BLOQUE (FC/Servicios), EBITDA final SÍ cuadra** (482.9 + 321.8 = 804.7 ≈ GOB 804.8, delta −0.16 $M por redondeo de la línea de proyectos). Es decir: **ya se puede bajar el split de bloque a EBITDA final** — FC 482.9 / Servicios 321.8. Lo que **NO cuadra** es la suma de sub-líneas a EBITDA final (ver §10).

**GOB combinado — cascada completa 1S-2026 ($M):** Vta Bruta 6,901.7 → (−dev 535.2 − desc 112.8) → **Vta Neta 6,253.7** → (−Costo 4,114.4) → U. Bruta 2,139.3 (34.21%) → (−Logística 837.2 − Soporte 31.9) → U. Marginal 1,302.1 → (−SG&A 846.1) → **UAFIR UN 456.0** (+D&A 352.4) → **EBITDA UN 808.4** → (Corpo 0) → (−Proyectos 3.6) → UAFIR 452.4 (+D&A 352.4) → **EBITDA final 804.8** (12.87%).

---

## 5. LO NUEVO #2 — PPTO 2026 y PIN 2026: cumplimiento de plan (nivel GOB)

El split chico **no traía plan** y por eso no podía verificar cumplimiento. Este maestro **sí trae PPTO y PIN para GOB combinado** (columnas AO y AS). No los trae partidos por FC/Servicios.

| Concepto GOB ($M) | REAL 1S-26 | PPTO 1S-26 | **Cumpl. vs PPTO** | PIN (anual) |
|---|---:|---:|---:|---:|
| Venta Neta | 6,253.7 | 6,658.1 | **93.9%** | 13,402.9 |
| Utilidad Bruta | 2,139.3 | 2,125.5 | 100.6% | 4,482.3 |
| UAFIR UN | 456.0 | 579.7 | 78.7% | 1,385.3 |
| **EBITDA UN** | **808.4** | **934.4** | **86.5%** | 2,087.4 |
| **EBITDA final** | **804.8** | **892.6** | **90.2%** | 2,024.5 |

**Lectura:** Gobierno cierra el 1S en **93.9% de la venta presupuestada** y **90.2% del EBITDA final presupuestado**. El faltante de EBITDA vs plan (≈88 $M en EBITDA final) es mayor en proporción que el de venta — es decir, **el gap es más de margen/mezcla que de volumen**. El PIN anual implica que el 1S representó ~46.7% del EBITDA final del año (804.8 / 2,024.5), consistente con estacionalidad de Gobierno cargada al 2S.

> **Cuidado:** los cumplimientos del deck **"FC 90.0% / Servicios 102.1%"** siguen **sin poder verificarse** con este archivo — el PPTO/PIN existe a nivel GOB combinado, no partido FC/Servicios. Es coincidencia que 90.2% (EBITDA GOB) se parezca al 90.0% de FC; no es la misma métrica. (Vacío #2.)

---

## 6. LO NUEVO #3 — Indicadores financieros: ROIC, capital invertido, capital de trabajo

Dimensión **completamente ausente** del split chico. Solo a nivel **GOB combinado** (no hay ROIC por FC/Servicios/sub-línea). $M salvo %.

### 6.1 Retornos y capital (filas 184–204)

| Indicador GOB | REAL 1S-26 | REAL 1S-25 | PPTO 1S-26 |
|---|---:|---:|---:|
| NOPAT (util. desp. impuestos, factor 0.7) | 552.2 | 373.6 | 735.8 |
| Utilidad Neta (factor 0.5) | 394.4 | 266.8 | 525.6 |
| **ROA** | **2.43%** | 1.61% | 3.17% |
| **ROIC** | **3.54%** | 2.34% | 4.61% |
| Capital invertido | 15,580.3 | 15,978.7 | 15,978.7 |
| Activo operativo | 16,264.0 | 16,593.7 | — |
| — Inventarios (MP 1,929.8 + PT 2,335.6) | 4,265.4 | 4,418.9 | — |
| — Cuentas por cobrar (cartera) | 4,736.8 | 4,812.1 | — |
| — PP&E | 7,261.8 | 7,362.6 | — |
| Pasivo operativo (Proveedores) | 683.7 | 615.0 | — |

**Lectura de negocio (fuerte):** Gobierno **inmoviliza ~$15.6 mil M de capital** para generar EBITDA final de 804.8 $M en el semestre. El **ROIC de 3.54%** (vs 4.61% presupuestado, y apenas 2.34% en 2025) es **bajísimo**: el segmento gana poco sobre el capital que consume. El capital de trabajo es el villano — **inventarios 4,265 + cartera 4,737 = 9,002 $M contra proveedores de apenas 684 $M**. Gobierno financia inventario y cartera casi sin apalancamiento de proveedores. Aunque el EBITDA se recupera (§7), **la creación de valor sigue débil** — dato incómodo pero board-relevante si el Consejo pregunta por retorno de capital, no solo por margen.

### 6.2 Capital de trabajo mensual por segmento (hoja `Indicadores`)

Pivote mensual 2021 → **ago-2025** (vintage viejo, no llega a jun-2026) de cartera, inventarios (ALMACEN MP / PT), proveedores y activos, **por segmento** (Farma Mx, Gobierno, Impulso, Hospitales Privados, Farmacias, Expansión). Es el andamiaje histórico detrás de los saldos de §6.1. Existe además una etiqueta **"UN GOBIERNO CENTRAL" vs "UN GOBIERNO DESCENTRALIZADO"** (`Indicadores!C13/C14`) — indicio de un corte Central/Descentralizado dentro de Gobierno, pero en esta hoja solo aparece como rótulo de capital de trabajo, **sin P&L Central/Descentralizado desarrollado**. (Vacío #4.)

---

## 7. LO NUEVO #4 — Serie histórica GOB 2020–2026 (el pico 2024 y el colapso 2025)

`FarmaMX` trae la serie completa de GOB combinado. **El split chico solo mostraba 2025→2026; aquí está el contexto multianual, que cambia la narrativa.**

| GOB combinado ($M) | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **2026** |
|---|---:|---:|---:|---:|---:|---:|---:|
| Venta Neta | 5,079.4 | 4,030.5 | 4,606.9 | 5,739.8 | 6,202.6 | 6,194.1 | **6,253.7** |
| EBITDA UN | −152.0 | 235.1 | 628.9 | 1,435.6 | **1,474.1** | 624.0 | **808.4** |
| — % margen EBITDA UN | −3.0% | 5.8% | 13.7% | 25.0% | **23.8%** | 10.1% | **12.9%** |
| EBITDA final | −165.5 | 226.5 | 623.5 | 1,423.9 | **1,441.5** | 550.1 | **804.8** |

**Lectura (importante para el Consejo):** la venta de Gobierno lleva 3 años planos (~6,200 $M desde 2024). Pero el EBITDA cuenta otra historia:
- **2024 fue un pico anómalo** (EBITDA UN 1,474.1 $M, margen **23.8%**; 2023 fue 25.0%).
- **2025 se desplomó** a 624.0 $M (margen 10.1%) — una caída de **−58%** en EBITDA con venta plana.
- **2026 recupera** a 808.4 $M (+29.6% vs 2025), pero **sigue en apenas ~55% del pico 2024**.

Es decir, el "+18.5% de FC / +50.7% de Servicios" que celebra el split chico es un **rebote desde un 2025 colapsado, no un nuevo máximo**. Si el Consejo ve 2020–2026, la pregunta natural es "¿qué pasó en 2024 (margen 24%) que ya no volvió?". Conviene tener lista esa respuesta (probablemente mezcla/precio de licitaciones 2023-24) antes de exponer la serie larga.

---

## 8. LO NUEVO #5 — Pesos de segmento: Gobierno dentro de Farma MX (hoja `BC`)

`BC` guarda las participaciones de cada segmento en Farma MX, para venta y para costo, 2024–2026.

| Segmento (% de Farma MX) | Venta 2024 | Venta 2025 | Venta 2026 | Costo 2026 |
|---|---:|---:|---:|---:|
| **GOBIERNO** | 30.66% | 32.59% | **31.42%** | **47.96%** |
| IMPULSO | 15.01% | 13.20% | 13.50% | 20.66% |
| HOSPITALES PRIV | 21.49% | 21.86% | 21.74% | 12.45% |
| FARMACIAS | 26.41% | 26.17% | 22.80% | 13.42% |
| EXPANSION | 6.43% | 6.17% | 10.53% | 5.50% |

**Lectura:** Gobierno pesa **~31% de la venta de Farma MX pero ~48% del costo** — la firma de un segmento de bajo margen (mucha solución/volumen, poco valor por peso). Contrasta con Farmacias (23% venta / 13% costo) y Hospitales (22% venta / 12% costo), que son ligeros en costo. Estas participaciones permiten reconstruir el tamaño de Farma MX (Venta Neta Farma MX ≈ GOB 6,253.7 / 0.3142 ≈ **19,900 $M** en el 1S), útil porque la columna FARMA MX total del propio archivo está rota.

---

## 9. Item 4 — Detalle de la reasignación de fuerza de ventas (FC negativo → Servicios)

**Sí, este archivo muestra la mecánica completa.** La fuerza de ventas negativa de FC (−72.0 $M) no es un error: es un **contra-cargo** — se acredita a FC y se carga a Servicios, concentrado en SANEFRO. SG&A comercial 1S-2026, $M:

| Línea comercial (fila) | GOB | FC | Serv | DP | SAFE | **SANEFRO** | SIA |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fuerza de Ventas (87) | 108.2 | **−72.0** | 180.2 | 23.0 | 17.7 | **139.5** | 0.0 |
| Comisiones + Gratif (88) | 7.9 | 7.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Servicios Integrales (90) | 154.1 | 154.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Gastos Generales com. (92) | 75.3 | **−34.1** | 109.4 | 5.7 | 6.4 | **91.6** | 5.8 |
| Mtto equipos médicos (95) | 42.6 | 42.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

**Mecánica:** hay **dos contra-cargos** de FC hacia Servicios, no uno solo:
1. **Fuerza de Ventas:** FC −72.0, y los 180.2 $M reales aterrizan casi todo en **SANEFRO (139.5 $M)**, con DP 23.0 y SAFE 17.7. SIA no recibe fuerza de ventas.
2. **Gastos Generales comerciales:** FC −34.1, y los 109.4 $M aterrizan otra vez en **SANEFRO (91.6 $M)**.

Combinados, **FC queda acreditado con −106.1 $M** (−72.0 −34.1) que se trasladan a Servicios/SANEFRO. Operativamente tiene lógica: la "fuerza de ventas" de la diálisis es personal clínico/de campo de las clínicas SANEFRO (hemodiálisis), por eso el modelo lo saca de FC-producto y lo carga al servicio. Pero contablemente es una **reclasificación, no un costo natural** — infla el margen de FC-producto y castiga el de Servicios. Aun absorbiendo estos 180+ $M, **Servicios termina con mayor margen EBITDA (14.58% vs FC 12.02%)**: la conclusión direccional (Servicios = motor de rentabilidad) es robusta al artefacto.

**Recomendación:** exponer FC/Servicios a nivel de bloque sin problema. **No mostrar SG&A comercial por sub-línea** (fuerza de ventas de FC en negativo) sin una nota de reclasificación — es la costura por donde asoma el "pleito".

---

## 10. Item 5 — Reparto de "Nuevos Productos / Proyectos": ¿lo reparte este archivo?

**Respuesta: lo INTENTA, pero el reparto NO es aditivo debajo de EBITDA UN. Es un artefacto de prorrateo.**

La línea es **"Gastos por Proyectos / Proyectos por capitalizar"** (filas 158/160), que baja de UAFIR UN a UAFIR y por tanto de EBITDA UN a EBITDA final. Valores 1S-2026 ($M):

| Nivel | GOB | FC | Serv | FC+Serv | DP | SAFE | SANE | SIA | Σ sub-líneas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gastos por Proyectos (158) | **3.57** | 1.86 | 1.86 | **3.73** | 1.86 | 1.86 | 1.86 | 2.53 | **8.11** |

- **A nivel bloque:** FC 1.86 + Serv 1.86 = 3.73 vs GOB 3.57 → **delta +0.16 $M** (casi cuadra; por eso EBITDA final de bloque cuadra dentro de redondeo).
- **A nivel sub-línea:** las 4 sub-líneas suman **8.11 $M**, muy por encima del 1.86 asignado a Servicios y del 3.57 de todo Gobierno → **delta +6.26 $M**. Cada sub-línea recibió un ~1.86 casi constante (SIA 2.53), como un **spread plano**, no un prorrateo real.

**Consecuencia aritmética exacta (al peso):**
- **EBITDA UN (131): cuadra perfecto** — FC 484,779,834 + Serv 323,620,047 = GOB 808,399,881 (delta 0). Sub-líneas = Servicios (delta 0).
- **EBITDA final (170):** FC 482.9 + Serv 321.8 = 804.7 vs GOB 804.8 (**delta −0.16 $M**, aceptable). Sub-líneas suman 315.5 vs Servicios 321.8 (**delta −6.26 $M**, NO cuadra).

**Veredicto operativo:**
- Si necesitas el split **a nivel bloque (FC/Servicios)**, puedes usar EBITDA final: **FC 482.9 / Servicios 321.8** (cuadra con GOB 804.8 dentro de $0.2 M).
- Si necesitas **sub-líneas**, quédate en **EBITDA UN** (127.9 / 74.4 / 108.6 / 12.7) — es el único nivel donde las sub-líneas suman Servicios. **No bajes las sub-líneas a EBITDA final**; el prorrateo de proyectos las descuadra en 6.3 $M.
- El split chico **acertó** al detenerse en EBITDA UN: debajo, la línea de proyectos contamina la aditividad.

(2025: mismo patrón — Gastos por Proyectos GOB 73.85 vs FC 29.94 + Serv 29.94 = 59.88, delta 13.97 $M; tampoco cuadra debajo de EBITDA UN.)

---

## 11. Item 6 — Margen bruto por sub-línea y señal de "diálisis 0%"

Confirmado contra la fuente (fila 48, % margen bruto 1S-2026):

| Sub-línea | Margen bruto | EBITDA UN | % EBITDA UN | Perfil |
|---|---:|---:|---:|---|
| **SANEFRO** | **66.61%** | 108.6 | 19.92% | Servicio (clínica HD): bruto alto, **cero logística**, SG&A comercial pesado |
| **SIA** | **66.61%** | 12.7 | 23.91% | Servicio (mismo perfil que SANEFRO) |
| DP | 34.21% | 127.9 | 17.40% | Producto (bolsas/soluciones diálisis peritoneal) |
| SAFE | 28.38% | 74.4 | 8.40% | Producto (mezclas/nutrición): eslabón débil, EBITDA bajó 87.2→74.4 YoY |

**Señal del pleito de reclasificaciones: este es el corte HONESTO — la diálisis NO está en 0% de EBITDA.**
- SANEFRO (la línea de ~70% de margen bruto) muestra **EBITDA 108.6 $M = 19.92%**, no cero.
- DP (diálisis peritoneal) muestra **EBITDA 127.9 $M = 17.40%**.
- Corporativo = 0 (no hay carga corporativa que aplaste artificialmente a diálisis).

La reclasificación en disputa dejaba "diálisis al 0% de EBITDA con margen bruto 70%". **En este archivo eso NO ocurre**: cada sub-línea conserva su economía natural y positiva. Este split es la fotografía **sin** el recorte de diálisis-a-cero — el número "bueno" para defender que la diálisis sí genera EBITDA. La única marca del pleito que sí persiste son los **contra-cargos de fuerza de ventas** (§9), no un zeroing de márgenes.

---

## 12. Fuentes de datos (lo que alimenta el modelo)

| Hoja | Rol | Estructura |
|---|---|---|
| `DS` | **Venta y devoluciones** | Pivote: División · ID RUN N1–N4 · Año · **meses 01–12**. Granularidad mensual por dimensión de negocio. |
| `DS Gasto` | **Gastos SG&A** | Pivote "P&L x Mercado": N1–N5 (p.ej. CORPORATIVO/AUDITORIA/...) · Año · **∑ Gto y ∑ Gto YTD por mes**. El gasto **sí está etiquetado por mercado** (Gobierno, etc.). |
| `Dicc datos` | **Diccionario metodológico** | Cada línea de P&L clasificada **CF/CV** (costo fijo/variable) con notas ("BAJO ESQUEMA ESTANDAR", trato de materiales directos, variaciones por TC, etc.). Es el manual del modelo. |

**Sobre lo MENSUAL:** el **dato mensual existe a nivel fuente** (`DS` y `DS Gasto` tienen columnas 01–12), pero el **P&L consolidado por segmento (`FarmaMX`) está congelado en YTD-junio** — no hay una vista de P&L mensual de Gobierno ya construida. Sería **reconstruible** desde `DS`/`DS Gasto`, pero no está pre-armada en este libro. (Vacío #3.)

---

## 13. CIERRE

### Inconsistencias internas
1. **Columna FARMA MX total rota:** las líneas de P&L de Farma MX (col P/N/T/X) devuelven **`#REF!`/`#VALUE!`** (referencia a rango borrado). No se puede leer Farma MX total del propio archivo ni recalcular (es error estructural, no de caché). Se reconstruye vía pesos de `BC` (§8). **No usar la columna FARMA MX de este libro.**
2. **"Gastos por Proyectos" no aditivo bajo EBITDA UN:** prorrateo casi plano (~1.86 por columna) que descuadra sub-líneas por +6.26 $M a EBITDA final (§10). Bloque FC/Serv cuadra dentro de $0.16 M; sub-líneas no.
3. **Fuerza de Ventas y Gastos Generales de FC negativos** (−72.0 y −34.1 $M): contra-cargos de reclasificación FC→SANEFRO. Cuadran en total, no a nivel de línea (§9).
4. **IMPULSO truncado:** el bloque IMPULSO (cols AX–BA) solo trae REAL 2020–2023 parcial; no es un P&L Impulso completo.
5. **Celda de encabezado 38.22%** (`FarmaMX!BC1`, misma que el AE1 del split chico): sin base reconciliable (Serv/GOB VN = 35.49%). Artefacto de encabezado, no afecta el P&L.

### Choques con referencias
1. **vs split chico:** cuadre **exacto al peso** en EBITDA UN (484.8 / 323.6 y 4 sub-líneas). El split es fiel. ✅
2. **vs v18 (Estado de Resultados):** este archivo **sí baja a EBITDA final** — GOB **804.8** (= v18 exacto) y GOB 2025 **550.1** (= v18 exacto). Resuelve el choque UN-vs-final que el split chico dejó abierto: **los 3.6 $M (2026) / 73.9 $M (2025) de proyectos ya están aquí**, y a nivel bloque FC 482.9 / Serv 321.8 cuadra. ✅
3. **Cumplimiento del deck "FC 90.0% / Serv 102.1%": aún no verificable** — PPTO/PIN solo a nivel GOB combinado, no FC/Serv. A nivel GOB sí: **93.9% venta, 90.2% EBITDA final** vs presupuesto.
4. **Serie histórica:** 2026 EBITDA UN 808.4 es **~55% del pico 2024** (1,474.1). El "crecimiento" YoY es rebote desde el colapso 2025, no un máximo (§7).

### Vacíos declarados
1. **FARMA MX total:** ilegible en este archivo (referencias rotas). Solo reconstruible por pesos `BC`.
2. **PPTO/PIN por FC-Servicios:** NO existe. Solo GOB combinado y Farma MX. No se reproducen los cumplimientos por bloque del deck.
3. **P&L mensual por segmento:** NO pre-armado. El dato mensual vive en `DS`/`DS Gasto` (reconstruible, no extraído aquí).
4. **P&L Gobierno Central vs Descentralizado:** solo aparece como rótulo de capital de trabajo en `Indicadores` (`C13/C14`), sin P&L desarrollado.
5. **Sub-líneas históricas <2025:** el split DP/SAFE/SANEFRO/SIA solo existe para 2025 y 2026. El 2024 solo está a nivel GOB combinado (`BC` da la participación 30.66%).
6. **Rótulos definitivos de SAFE/SANEFRO/SIA:** no rotulados en la fuente; correspondencia (SANEFRO=HD, SAFE=mezclas, SIA=servicio) inferida por estructura de costos, no confirmada.
7. **ROIC/capital por FC-Servicios-sub-línea:** NO existe. Los indicadores financieros (ROA/ROIC/capital) solo a nivel GOB combinado.

### Veredicto de board-readiness
Este maestro **confirma el split chico al peso** y **cierra sus dos grandes vacíos**: (a) baja hasta **EBITDA final 804.8** con reparto de bloque limpio (FC 482.9 / Serv 321.8), y (b) agrega la dimensión de **retorno de capital (ROIC 3.54%, capital invertido 15.6 mil M)** y el **contexto histórico 2020–2026** que cambia el tono de la narrativa (recuperación parcial desde el colapso 2025, no nuevo máximo). Advertencias antes de exponer: **no usar la columna FARMA MX** (rota), **no bajar sub-líneas a EBITDA final** (descuadran 6.3 $M — usar EBITDA UN para sub-líneas), y **no mostrar SG&A comercial por sub-línea** sin nota de reclasificación (fuerza de ventas de FC negativa). A nivel bloque y en EBITDA UN, el número es sólido y la historia — Servicios como motor de margen — es robusta.
