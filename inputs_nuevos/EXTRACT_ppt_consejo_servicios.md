# EXTRACT — "CONSEJO 27 DE JULIO_Servicios.pptx" (segmento Servicios / Gobierno)

> Extracción exhaustiva lámina por lámina. Archivo fuente: `/Users/rafaelprince/Downloads/CONSEJO 27 DE JULIO_Servicios.pptx`.
> Preparado por el equipo de David Silva (Gobierno). Primera vez que Servicios se presenta a Consejo.
> Método: `python-pptx` (texto de shapes/tablas/notas + datos nativos de gráficas think-cell), conversión a PDF con LibreOffice y rasterizado a PNG 150 dpi con PyMuPDF, leído lámina por lámina.
> Moneda MXN. "M" = millones de pesos salvo cuando se indica "pacientes" o "bolsas". Periodo base recurrente: Ene–Jun 2026 (1S 2026) vs 1S 2025. Corte de datos declarado en varias láminas: **02 de julio 2026**.

## Nota estructural crítica (conteo de láminas)
- El .pptx tiene **36 láminas**; el PDF renderizó **35 páginas**. **La lámina 8 está OCULTA** (no renderiza): es una segunda variante de "Cartera Gobierno" con desglose "Proceso Cliente" (ver §Lámina 8).
- Muchas láminas son gráficas think-cell embebidas como objeto OLE: su texto NO sale por python-pptx y vive solo en el PNG. Los valores nativos de las gráficas sí se extrajeron (`chart.series/values`) y se cruzan con las etiquetas del PNG.
- **Las láminas 31–36 son cuadros de animación (build progresivo) de la MISMA cascada** "¿Qué está pasando en gobierno? – Frasco Cerrado" que aparece completa en la lámina 3. El estado final (lámina 36) es idéntico a la lámina 3.
- **Las láminas 4, 5 y 6 son visualmente idénticas** (mismo gráfico "Notas de Crédito"; cuadros de animación/duplicados).

## Mapa de secciones (bloques del deck)
1. **Situación del mercado gobierno** (L1)
2. **Nivel de Servicio – Gobierno** (portada L2; cascada Frasco Cerrado L3; Notas de Crédito L4–6; Cartera Gobierno L7 + L8 oculta)
3. **Servicios – Mezclas** (L9 resultados 2022–26; L10 histórico 2018–25 Priv/Gob; L11 precio SAFE IMSS)
4. **Servicios – Diálisis (mezclas de diálisis)** (L12 resultados)
5. **Diálisis Peritoneal (DP) — sizing de mercado y competencia vs Baxter** (L13–L26: total México, IMSS, IMSS Bienestar, ISSSTE, OTROS, resumen)
6. **Servicios – Hemodiálisis** (L27 resultados; L28 mapa 12 clínicas SANEFRO; L29 venta anual SANEFRO)
7. **Servicios – Anestesia** (L30 resultados)
8. **Cascada Frasco Cerrado repetida en build** (L31–L36)

---

## LÁMINA 1 (PDF p1) — "Situación del mercado"
Título/etiqueta: **"Situación del mercado"**.

**Gráfica de barras (izq)** — "Presupuesto salud gobierno" (barras 2024, 2025, 2026; think-cell COLUMN_STACKED, valores nativos indexados 100 / 90.65 / 96.0):
- 2024 → 2025: **−9%**
- 2025 → 2026: **+6%**
- Etiqueta del bloque: "% ENTREGAS"

**Doughnut (centro)** — "% del presupuesto total" (valores nativos 50/20/12/10/8):
- IMSS **50%**
- IMSS BIENESTAR **20%**
- ESTADOS **12%**
- ISSSTE **10%**
- CCINSHAE´S **8%**
(suma 100%)

**Tabla (der)** — "Crec. Esperado compras 2026 vs 2025":
| Cliente | Crec. esperado |
|---|---|
| IMSS | +11% |
| IMSS BIENESTAR | +3% |
| ESTADOS | +2% |
| ISSSTE | +6% |
| CCINSHAE´S | +11% |

**Cuatro cajas inferiores (amenazas/tendencias):** "Más competidores internacionales" · "Más competidores por clave" · "Mayor presión de precios" · "Menos compras directas".

**Caja de insight (banner inferior):** "El mercado mantiene volumen, pero **no es más grande**; el crecimiento dependerá de **ganar participación** y **ejecutar mejor** que la competencia."

**Fuente al pie:** "Información obtenida de INEFAM 2026."

---

## LÁMINA 2 (PDF p2) — Portada "Nivel de Servicio GOBIERNO"
Texto: **"Nivel de Servicio / GOBIERNO"**. Logos PiSA Farmacéutica + FARMA MX 25.
**Speaker notes:** "Acumulado FARMA Total 85%".

---

## LÁMINA 3 (PDF p3) — Cascada "¿Qué está pasando en gobierno?" — Frasco Cerrado
Título banner: **"Alcance a Meta Enero – Junio 2026 / Frasco Cerrado"**. Título der: **"¿Qué está pasando en gobierno?"**. (Gráfica think-cell; texto vive en PNG.)

Cascada (izquierda a derecha), etiquetas literales:
- **Meta Ene-Jun 2026 = 6,658M** (compuesta: **Servicios 2,757M** [porción rayada] + **FC 3,901M** [porción negra])
- **PIN Ene-Jun 2026 = 4,266M**
- **Pedidos Ene-Jun 2026 = 3,993M (102%)**
- **Sin Atender (Fill Rate) = 704M (18%)** [barra roja, resta] — marcador ②. Desglose: **$544 Negado · $90 Sin inv. Pedido Vigente · $70 Inv Conf. (Fact Julio)** (544+90+70 = 704)
- **Fact. (Ped. 2025) = 54M (1%)** [verde, suma]
- Subtotal intermedio rotulado **3,343M**
- **Venta Ene-Jun 2026 = 3,235M (83%)** [barra verde]
- **Notas de Crédito = 108M (3%)** [naranja] — marcador ③ / 330M (8%)
- **Vta Perdida = 121M (3%)** [marcador ②] / 342M (9%) [rayado]
- **PIN NO SOL = 859M (22%)** [marcador ①]

Reconciliación aritmética de la cascada: 3,993 (pedidos) − 704 (sin atender) + 54 (fact ped 2025) = **3,343** subtotal; 3,343 − 108 (notas crédito) = **3,235 (83%)** venta neta. Cuadra.
Los % (18%, 83%, 22%, etc.) son sobre la meta FC 3,901M (3,235/3,901 = 82.9% ≈ 83%).

---

## LÁMINAS 4, 5, 6 (PDF p4, p5, p6) — "Notas de Crédito, aplicadas y en proceso (Envíos rechazados / No enviados)"
**Las tres láminas son visualmente idénticas** (cuadros de animación). Título: "Notas de Crédito, aplicadas y en proceso (Envíos rechazados / No enviados)".

**Tabla superior izq (Origen × año, $M):**
| Origen | 2024 | 2025 | 2026 | Proceso |
|---|---:|---:|---:|---:|
| 20-23 | $40 | $10 | $0 | $0 |
| 2024 | $603 | $210 | $15 | $2 |
| 2025 | – | $695 | $131 | $25 |
| 2026 | – | – | $211 | $44 |
| **Total** | **$643** | **$915** | **$357** | **$71** |

**Resumen (centro):** "Notas de Crédito 2026 — **$357M Aplicados · $71M Pendientes · $428M Total (−53% vs 2025)**".
**Tabla semana (der):** SEM ANT. **$420** · SEM ACT. **$428** (Δ **$8**).

**Gráfica de columnas 2025 vs 2026 por mes ($M):**
| Mes | 2025 (gris) | 2026 (navy) |
|---|---:|---:|
| Ene | $20 | $46 |
| Feb | $29 | $47 |
| Mzo | $137 | $80 |
| Abr | $97 | $28 |
| May | $153 | $68 |
| Jun | $118 | $61 |
| Jul | $95 | $27 |
| Ago | $56 | – |
| Sep | $58 | – |
| Oct | $51 | – |
| Nov | $51 | – |
| Dic | $50 | – |
Líneas de referencia: **$76 – 2025** y **$54 – 2024** (promedios).

**Barra "Devoluciones en proceso 2026" (der):** total **$71** = **$3 Contabilizado + $68 En Proceso**.
**Fuente al pie:** "*Actualizado al 02 Julio 2026*".

---

## LÁMINA 7 (PDF p7) — "Cartera Gobierno | Jun 2025 – Jun 2026"
Título: **"Cartera Gobierno | Jun 2025 – Jun 2026"**. Logo GRUPO PiSA.

**Cascada de cartera izq (Millones de pesos), "Cartera del 30 de junio 2025 y Cierre 2025 al 30 de junio 2026" (etiqueta "FC Y SERV", "Jun-jun"):**
- 30 Jun 2025 = **$5,120**
- 31 Dic 2025 = **$3,966**
- Facturado 2026 = **$6,256**
- Pagado 2026 = **$5,388**
- 30 Jun 2026 = **$4,834** (Δ **$868 / +22%**), desglosado en **Ingresado $2,295 + No Ingresado $2,539**
**Tabla al pie izq:**
| | 30 Jun 2025 | 31 Dic 2025 | | 30 Jun 2026 |
|---|---:|---:|---:|---:|
| Vta. Ult. 12 Meses | $1,032 | $1,100 | | $1,042 |
| Meses Cart. | 5.0 | 3.6 | | 4.6 |

**Tabla "Facturación y Pagos Ene - Jun 2026" (der, Millones de pesos):**
| Cliente | Saldo 31 Dic 25 | Facturado 2026 | Pagado 2026 | Saldo 30 Jun 26 | Diferencia |
|---|---:|---:|---:|---:|---:|
| Bienestar | $1,276 | $389 | $299 | $1,366 | $90 |
| IMSS | $1,214 | $3,443 | $3,013 | $1,644 | $430 |
| Distribuidores | $460 | $749 | $758 | $451 | −$9 |
| Estatal | $398 | $1,291 | $912 | $777 | $379 |
| CCINSHAE'S | $309 | $125 | $186 | $248 | −$61 |
| ISSSTE | $240 | $224 | $195 | $270 | $29 |
| Pemex | $69 | $33 | $24 | $78 | $9 |
| **Total** | **$3,966** | **$6,256** | **$5,388** | **$4,834** | **$868** |

**Barras stacked Ingresado/No Ingresado (der inf):**
- **FC:** Ingresado $1,939 + No Ingresado $1,622 = $3,561 · **5.3 M.C.** (meses cartera)
- **Servicios:** Ingresado $356 + No Ingresado $917 = $1,273 · **3.4 M.C.**

---

## LÁMINA 8 (OCULTA — no renderiza en PDF) — segunda variante "Cartera Gobierno"
> Detectada solo por python-pptx; está marcada oculta y no aparece en el PDF/PNG. Casi idéntica a L7 con estas diferencias:
- Misma cascada 30 Jun 2025 $5,120 → 31 Dic 2025 $3,966 → Facturado $6,256 → Pagado $5,388 → 30 Jun 2026 $4,834.
- Tabla al pie izq usa etiqueta **"Vta. Mensual"** (en L7 es "Vta. Ult. 12 Meses") con los mismos valores $1,032 / $1,100 / $1,042; Meses Cart. 5.0 / 3.6 / 4.6. **(Inconsistencia de rótulo entre L7 y L8.)**
- Misma tabla "Facturación y Pagos Ene-Jun 2026" (idéntica a L7).
- En lugar de las dos barras FC/Servicios, tiene: barra "Cartera Total" **$3,114 (Proceso Cliente) + $1,720 (Proceso Empresa) = $4,834**; y caja de texto **"Proceso Cliente: $2,295 Ingresado / $0,793 Trámites con Dependencia / $0,026 Formalización de Contratos"**.

---

## LÁMINA 9 (PDF p8) — "Resultados mezclas" (2022–2026, YTD/YTG)
Etiqueta: **"Resultados mezclas"**. Barras apiladas YTD (sólido) + YTG (rayado), $M. Leyenda: YTG / YTD.
| Año | YTD | YTG | Total |
|---|---:|---:|---:|
| 2022 | $523 | $632 | $1,155 |
| 2023 | $668 | $860 | $1,528 |
| 2024 | $917 | $1,083 | $2,000 |
| 2025 | $925 | $985 | $1,910 |
| 2026 | $886 | (n/d) | (solo YTD) |
Delta 2026 vs 2025 YTD: **−$39 (−4%)** (886 − 925 = −39).

**Cuadro de texto (der):**
- "En 2026 hay afectación de **−$50 M YTD** vs 2025 por salidas derivadas de capacidad."
- "La salida en **SEMAR** a causa del alto precio representa **−$142 M** hasta el mes de junio."
- "**IMSS** ha crecido **+$108 M** gracias al sistema híbrido (medicamento + mezclas)."
- "Se ha capitalizado venta de oportunidad con **ISAPEG +70 M**."

---

## LÁMINA 10 (PDF p9) — "Resultados mezclas" histórico 2018–2025 (Priv/Gob)
Etiqueta: **"Resultados mezclas"**. Barras apiladas Gob (navy) + Priv (gris), con % y valores $M. Flecha "+14%".
| Año | Gob % | Priv % | Total $M |
|---|---:|---:|---:|
| 2018 | 85% | 15% | $2,918 |
| 2019 | 82% | 18% | $2,891 |
| 2020 | 75% | 25% | $2,019 |
| 2021 | 71% | 29% | $1,523 |
| 2022 | 68% | 32% | $1,716 |
| 2023 | 69% | 31% | $2,214 |
| 2024 | 73% | 27% | $2,749 |
| 2025 Proy | 73% ($1,835) Gob / 27% ($695) Priv | | $2,530 |
Anotación "+14%" (tendencia).

**Tablas al pie (por año 2018→2025):**
| Métrica | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CM (clientes/claves) | 19 | 18 | 16 | 9 | 7 | 7 | 7 | 6 |
| MEZCLAS | 7.2M | 5.1M | 3.1M | 3.4M | 2.9M | 3.2M | 3.2M | 2.8M |
| Mg Bruto | 42% | 42% | 41% | 56% | 55% | 56% | 61% | 63% |
| Mg Op | TBD | 21% | 2% | 7% | 10% | 21% | 27% | 22% |
(Mg Op 2018 = **"TBD"**, placeholder sin dato.)

---

## LÁMINA 11 (PDF p10) — "Comportamiento Precio SAFE IMSS | 2020-2026"
Título: **"COMPORTAMIENTO PRECIO SAFE IMSS | 2020-2026"**. Gráfica de líneas (XY scatter, 3 series: ONCO rosa, NPT azul claro, ATB navy). Eje Y $ (0–800).
Series nativas (valores por año 2020→2026):
- **ONCO:** 256 / 349 / 444 (rosa: 256/321/444...)  — etiquetas PNG: $256, $349→(varias), $676, $730, $774, $821. Incrementos anotados: +25% (2021), +38%(2022), +52%(2023), +66%..., 8%(2024), 6%(2025), 6%(2026).
- **NPT:** 256 / 321 / 373 / 620 / 670 / 710 / 752 → etiquetas $256, $321, $373, $620, $670, $710, $752. Incrementos: +36%, +7%, +66%, +8%, +6%, +6%.
- **ATB:** 81 / 99 / 106 / 145.59 / 157 / 167 / 176.66 → etiquetas $81, $99, $106, $146, $157, $167, $177. Incrementos: +22%, +7%, +37%, +8%, 6%, 6%.
Anotación der: **$662 – Pharmatycsa · $570 – Serbitec** (competidores).
**Caja de insight (pie):** "En 2026 se implementó un incremento del **6%**. Precios SAFE Onco están **24% arriba** del principal competidor Pharmatycsa."

---

## LÁMINA 12 (PDF p11) — "Resultados diálisis" (mezclas de diálisis, 2022–2026)
Etiqueta: **"Resultados diálisis"**. Barras YTD/YTG $M.
| Año | YTD | YTG | Total |
|---|---:|---:|---:|
| 2022 | $444 | $462 | $906 |
| 2023 | $537 | $499 | $1,036 |
| 2024 | $520 | $537 | $1,057 |
| 2025 | $667 | $685 | $1,352 |
| 2026 | $735 | 0 | (solo YTD) |
Delta 2026 vs 2025 YTD: **+$68 (+10%)**.
**Cuadro de texto:** "El crecimiento YTD 26 vs 25 se debe **totalmente al incremento precio**."
**⚠ Caja placeholder sin resolver (banner azul):** "**Meter numero de mezclas y precios**" (tarea pendiente dejada en la lámina).

---

## LÁMINA 13 (PDF p12) — "DIALISIS PERITONEAL" — sizing mercado México
Título: **"DIALISIS PERITONEAL"**. Subtítulo: "Pacientes anuales (DPA + DPCA)". Barra apilada "2026 MEXICO" = **53,400 pacientes**:
- IMSS **38,000 (71%)**
- IMSS BTAR (Bienestar) **7,800 (15%)**
- ISSSTE **6,100 (11%)**
- OTROS **1,500 (3%)**

**Texto (der):** "En México detectamos licitaciones para aproximadamente **53,400 pacientes** al año en diálisis Peritoneal en el sector público, el **71% se concentra en el IMSS**."
"Del IMSS Bienestar se tiene información de **17 estados** de la última IM (2025) que representan **54% de la población** de México, por lo que se estima que puedan llegar a ser hasta **5,755 pacientes más**. Estados con información:"
**Speaker notes:** "Acumulado FARMA Total 79%".

---

## LÁMINA 14 (PDF p13) — DP: participación por proveedor
Título: **"DIALISIS PERITONEAL"**. Añade 2ª barra "Proveedor" (53,400): **PiSA 16,550 (31%) · Baxter 36,850 (69%)**.
**Tabla $ ANUAL MDP:** TOTAL **$5,631** · BAXTER **$4,182 (74%)** · PiSA **$1,448 (26%)**.
**Texto:** "El **31%** de estos pacientes son atendidos por PiSA."

---

## LÁMINA 15 (PDF p14) — DP: foco IMSS (caja roja punteada)
Título: **"DIALISIS PERITONEAL"**. Añade 3ª barra "IMSS" (38,000): **PiSA 16,000 (42%) · Baxter 22,000 (58%)**.
**Tabla $ ANUAL MDP (col IMSS):** TOTAL **$4,200** · BAXTER **$2,800 (67%)** · PiSA **$1,400 (33%)**.
**Texto (der):**
- "En IMSS PiSA atiende el **42%** de los pacientes."
- "Nuestra estrategia comercial es buscar el **100% de los pacientes** en los estados donde somos dominantes."
- "Incremento de precios entre el **15% y 20% anual** en pacientes prevalente."

---

## LÁMINA 16 (PDF p15) — DP IMSS: tabla comparativa PiSA vs Baxter (TOTAL / DPCA / DPA)
Título: **"DIALISIS PERITONEAL IMSS"**. Tres bloques. Columnas: IMSS (mercado) | PiSA (Valores / % del IMSS) | Baxter (Valores / % del IMSS).

**TOTAL:**
| | IMSS | PiSA | %IMSS | Baxter | %IMSS |
|---|---:|---:|---:|---:|---:|
| Pacientes | 38,000 | 16,000 | 42% | 22,000 | 58% |
| Bolsas Anuales | 45 Millones | 20 Millones | 44% | 25 Millones | 56% |
| Contrato anual | $4,200 Millones | $1,400 Millones | 33% | $2,800 Millones | 67% |

**DPCA (Diálisis Peritoneal Continua Ambulatoria – MANUAL; Bolsa 2L, 120 bolsas/mes/paciente):**
| | IMSS | PiSA | %IMSS | Baxter | %IMSS |
|---|---:|---:|---:|---:|---:|
| Pacientes | 22,000 | 11,000 | 50% | 11,000 | 50% |
| Bolsas Anuales | 32 Millones | 16 Millones | 50% | 16 Millones | 50% |
| Contrato anual | $2,200 Millones | $900 Millones | 41% | $1,300 Millones | 59% |
| Precio Nuevos | $57 | $47 | | $70 | (+49% Baxter vs PiSA) |
| Precio Prevalentes | $71 | $63 | | $80 | (+27% Baxter vs PiSA) |

**DPA (Diálisis Peritoneal Automatizada; Bolsa 6L, 60 bolsas/mes/paciente, 1 máquina cicladora/paciente):**
| | IMSS | PiSA | %IMSS | Baxter | %IMSS |
|---|---:|---:|---:|---:|---:|
| Pacientes | 16,000 | 5,000 | 31% | 11,000 | 69% |
| Bolsas Anuales | 13 Millones | 4 Millones | 31% | 9 Millones | 69% |
| Contrato anual | $2,000 Millones | $500 Millones | 25% | $1,500 Millones | 75% |
| Precio Nuevos | $162 | $129 | | $189 | (+47% Baxter vs PiSA) |
| Precio Prevalentes | $217 | $180 | | $234 | (+30% Baxter vs PiSA) |

**Panel der "Top 15 delegaciones - 65% de los pacientes" (Pacientes IMSS DP):**
| Delegación | PiSA | Baxter | Pacientes totales |
|---|---:|---:|---:|
| Jalisco | 88% | 12% | 2,610 |
| CDMX Sur | 56% | 44% | 2,482 |
| Edo. Mex. Oriente | 94% | 6% | 2,471 |
| Guanajuato | 80% | 20% | 2,333 |
| Puebla | 29% | 71% | 2,035 |
| Edo. Mex Poniente | 76% | 24% | 1,970 |
| Nuevo León | 76% | 24% | 1,641 |
| Coahuila | 1% | 99% | 1,316 |
| Hidalgo | 36% | 64% | 1,227 |
| CDMX Norte | 5% | 95% | 1,223 |
| Baja California Norte | 87% | 13% | 1,162 |
| Querétaro | 81% | 19% | 1,158 |
| Oaxaca | 0% | 100% | 1,115 |
| Chiapas | 0% | 100% | 1,058 |
| Tamaulipas | 0% | 100% | 1,031 |
| OTROS | 22% | 78% | 13,169 |
| **TOTAL** | **44%** | **56%** | **38,000** |

---

## LÁMINA 17 (PDF p16) — igual a L16 + panel Top 15 (misma tabla)
Título: **"DIALISIS PERITONEAL IMSS"**. Repite tabla PiSA/Baxter y Top 15 delegaciones (idéntica a L16). Cuadro de animación.

## LÁMINA 18 (PDF p17) — L16/17 + caja "HIGHLIGHTS"
Igual a L17, añade **caja "HIGHLIGHTS" (morada):**
1. "En IMSS se atienden **38,000 pacientes** de DP por año, el **42%** son atendidos por PiSA."
2. "En todos los casos **Baxter tiene un precio más alto que PiSA (Entre 27% y 49% más)**."
3. "El principal reto no solo radica en la **manufactura estéril** de las bolsas, sino también en la **complejidad logística** que permita llegar a todos los hogares mensualmente, garantizando la cobertura incluso en zonas de difícil acceso."

## LÁMINA 19 (PDF p18) — DP IMSS: "17 delegaciones donde PiSA es dominante"
Título: **"DIALISIS PERITONEAL IMSS"**. Misma tabla PiSA/Baxter izq. Panel der cambia a **"17 delegaciones donde PiSA es dominante"** (col extra "Baxter" = # pacientes Baxter):
| Delegación | PiSA | Baxter | Pac. totales | Baxter (pac.) |
|---|---:|---:|---:|---:|
| CDMX Sur | 56% | 44% | 2,482 | 1,080 |
| Edo. de Méx. Pte. | 74% | 26% | 1,834 | 478 |
| Guanajuato | 80% | 20% | 2,333 | 471 |
| Michoacán | 59% | 41% | 1,024 | 417 |
| Nuevo León | 72% | 28% | 1,435 | 398 |
| Jalisco | 88% | 12% | 2,610 | 322 |
| Tlaxcala | 58% | 42% | 641 | 269 |
| Querétaro | 81% | 19% | 1,158 | 219 |
| Zacatecas | 63% | 37% | 454 | 169 |
| Edo. de Méx. Ote. | 94% | 6% | 2,607 | 148 |
| Morelos | 81% | 19% | 717 | 138 |
| San Luis Potosí | 81% | 19% | 687 | 133 |
| Aguascalientes | 58% | 42% | 305 | 128 |
| Sinaloa | 61% | 39% | 292 | 114 |
| California | 71% | 29% | 310 | 89 |
| Baja California | 93% | 7% | 852 | 59 |
| Nuevo Leòn | 100% | 0% | 206 | 0 |
| **(subtotal)** | | | **19,947** | **4,632** |
**Texto:** "En **17/47 delegaciones** PiSA es dominante." · "En esas 17 delegaciones Baxter tiene **4,632 pacientes: 2,672 DPA y 1,960 DPCA**."

---

## LÁMINA 20 (PDF p19) — DP: IMSS Bienestar (barra IMSS BTAR, caja roja)
Título: **"DIALISIS PERITONEAL"**. Añade barra "IMSS BTAR" = **7,800** (todo Baxter).
**Tabla $ ANUAL MDP (col IMSS BTAR):** TOTAL **$655** · BAXTER **$655 (100%)** · PiSA **–**.
**Texto (der) "IMSS BIENESTAR":**
- "Hasta hoy solo han emitido **5 investigaciones de mercado desde 2024**."
- "**14 estados para DPA, 9 estados para DPCA**."
- "En el periodo donde atendimos este cliente tuvimos constantes **retrasos en los pagos** afectando la **cartera** y el flujo de la empresa."
**Speaker notes:** "Acumulado FARMA Total 79%".

---

## LÁMINA 21 (PDF p20) — DP IMSS Bienestar: tabla + estados
Título: **"DIALISIS PERITONEAL IMSS BIENESTAR"**. Tabla PiSA/Baxter (% del BTAR) — PiSA en todo "–", Baxter 100%.
**TOTAL:** Pacientes 7,800 (Baxter 7,800/100%) · Bolsas 9.8 Millones (100%) · Contrato $655 Millones (100%).
**DPCA:** Pacientes 5,800 (100% Baxter) · Bolsas 8.4 Millones · Contrato $443 Millones · Precio Estimado **$53**.
**DPA:** Pacientes 2,000 (100% Baxter) · Bolsas 1.4 Millones · Contrato $212 Millones · Precio Estimado **$149**.
(Contrato total 443+212 = $655M; pacientes 5,800+2,000 = 7,800.)

**Tabla "Estado / DPA / DPCA / Total" (der):**
| Estado | DPA | DPCA | Total |
|---|---:|---:|---:|
| VERACRUZ | 0 | 2,384 | 2,384 |
| ESTADO DE MEXICO | 476 | 1,140 | 1,616 |
| MORELOS | 184 | 708 | 892 |
| PUEBLA | 715 | 0 | 715 |
| TLAXCALA | 170 | 432 | 603 |
| TABASCO | 0 | 556 | 556 |
| TAMAULIPAS | 0 | 304 | 304 |
| BAJA CALIFORNIA SUR | 78 | 117 | 195 |
| BAJA CALIFORNIA | 168 | 0 | 168 |
| NAYARIT | 27 | 106 | 132 |
| COLIMA | 47 | 54 | 102 |
| SONORA | 50 | 0 | 50 |
| CHIAPAS | 28 | 0 | 28 |
| GUERRERO | 28 | 0 | 28 |
| ZACATECAS | 22 | 0 | 22 |
| HIDALGO | 3 | 0 | 3 |
| OAXACA | 3 | 0 | 3 |
| **Total** | **2,000** | **5,800** | **7,800** |
**Speaker notes (misma sección):** "Acumulado FARMA Total 79%".

---

## LÁMINA 22 (PDF p21) — DP: ISSSTE (barra, caja roja)
Título: **"DIALISIS PERITONEAL"**. Añade barra "ISSSTE" = **6,100** (todo Baxter).
**Tabla $ ANUAL MDP (col ISSSTE):** TOTAL **$595** · BAXTER **$595 (100%)** · PiSA **–**.
**Texto (der) "ISSSTE":** "El **11 de marzo** emitió investigación de mercado solicitando **Icodextrina y CRRT** (Terapia de reemplazo renal continua) **como restricción**."
**Speaker notes:** "Acumulado FARMA Total 79%".

---

## LÁMINA 23 (PDF p22) — DP ISSSTE: tabla detalle
Título: **"DIALISIS PERITONEAL ISSSTE"**. Tabla PiSA/Baxter (% del ISSSTE) — PiSA "–", Baxter 100%.
**TOTAL:** Pacientes 6,100 · Bolsas 5.7 Millones · Contrato $595 Millones (Baxter 100%).
**DPCA:** Pacientes 1,800 · Bolsas 2.6 Millones · Contrato $139 Millones · Precio Estimado **$53**.
**DPA:** Pacientes 4,300 · Bolsas 3.1 Millones · Contrato $456 Millones · Precio Estimado **$149**.
(139+456 = $595M; 1,800+4,300 = 6,100.)
**Texto:** repite "El 11 de marzo emitió investigación de mercado solicitando Icodextrina y CRRT como restricción."

---

## LÁMINA 24 (PDF p23) — DP: OTROS (barra + barra pacientes por institución)
Título: **"DIALISIS PERITONEAL"**. Añade barra "OTROS" = **1,500** (PiSA 550 / Baxter 950).
**Tabla $ ANUAL MDP (col OTROS):** TOTAL **$180** · BAXTER **$132 (73%)** · PiSA **$48 (27%)**.
**Barra horizontal "OTROS – Pacientes" (der):**
| Institución | Pacientes | Proveedor |
|---|---:|---|
| ISSSEMYM | 950 | BAXTER |
| PEMEX | 220 | PiSA |
| H. CIVIL GDL | 128 | PiSA |
| SESEQ | 123 | PiSA |
| SEMAR | 74 | PiSA |
| IMIEM | 5 | PiSA |
**Texto:** "Restricciones **ISSSEMYM**: Icodextrina · Cicladora con sistema de comunicación remoto."
**Speaker notes:** "Acumulado FARMA Total 79%".

---

## LÁMINA 25 (PDF p24) — DP OTROS: tabla detalle
**⚠ Título literal: "DIALISIS PERITONEAL ISSSTE"** (título erróneo; el contenido es OTROS — columnas "% de/del OTROS"). Tabla PiSA vs Baxter (% del OTROS):
**TOTAL:** Pacientes 1,500 · PiSA 550 (37%) · Baxter 950 (63%). Bolsas 1.6 Millones (PiSA 0.8M/47%, Baxter 0.8M/53%). Contrato $180 Millones (PiSA $48M/27%, Baxter $132M/73%).
**DPCA:** Pacientes 732 (PiSA 510/70%, Baxter 222/30%). Bolsas 1 Millón (PiSA 0.7M/69%, Baxter 0.3M/31%). Contrato $67 Millones (PiSA $43M/65%, Baxter $24M/35%). Precio: OTROS $64 · PiSA $60 · Baxter $74.
**DPA:** Pacientes 768 (PiSA 40/5%, Baxter 728/95%). Bolsas 0.6 Millones (PiSA 0.1M/5%, Baxter 0.5M/95%). Contrato $113 Millones (PiSA $5M/4%, Baxter $109M/96%). Precio: OTROS $206 · PiSA $169 · Baxter $208.
**Panel der:** misma barra ISSSEMYM 950 (Baxter)/PEMEX 220/H.CIVIL GDL 128/SESEQ 123/SEMAR 74/IMIEM 5 (PiSA); "Restricciones ISSSEMYM: Icodextrina · Cicladora con sistema de comunicación remoto".

---

## LÁMINA 26 (PDF p25) — DP: "En resumen" (cascada completa + anotaciones)
Título: **"DIALISIS PERITONEAL"**. Muestra las 6 barras (2026 MEXICO 53,400 / Proveedor / IMSS / IMSS BTAR / ISSSTE / OTROS) con la tabla $ ANUAL MDP completa:
| | TOTAL | IMSS | IMSS BTAR | ISSSTE | OTROS |
|---|---:|---:|---:|---:|---:|
| TOTAL | $5,631 | $4,200 | $655 | $595 | $180 |
| BAXTER | $4,182 (74%) | $2,800 (67%) | $655 (100%) | $595 (100%) | $132 (73%) |
| PiSA | $1,448 (26%) | $1,400 (33%) | – | – | $48 (27%) |
Anotaciones sobre las barras: **"Cobranza"** (rojo, sobre IMSS BTAR) y **"Restricciones"** (rojo, sobre ISSSTE+OTROS).
**Texto "En resumen" (der):**
- "Nuestro **potencial principal** se centra en el **incremento de precios** y la búsqueda del **100% de pacientes IMSS** en estados donde somos dominantes."
- "En **17/47 delegaciones** PiSA es dominante."
- "En esas 17 delegaciones Baxter tiene **4,632 pacientes: 2,672 DPA y 1,960 DPCA**."
**Speaker notes:** "Acumulado FARMA Total 79%".

---

## LÁMINA 27 (PDF p26) — "Resultados Hemodiálisis" (2022–2026, YTD/YTG)
Etiqueta: **"Resultados Hemodiálisis"**. Barras YTD/YTG $M.
| Año | YTD | YTG | Total |
|---|---:|---:|---:|
| 2022 | $325 | $339 | $664 |
| 2023 | $383 | $428 | $810 |
| 2024 | $452 | $471 | $923 |
| 2025 | $482 | $550 | $1,032 |
| 2026 | $545 | (n/d) | (solo YTD) |
Delta 2026 vs 2025 YTD: **+$64 (+13%)** (545 − 482 = +63 ≈ +64).
**Texto:** "En 2026 las **sesiones han incrementado 6%** vs YTD 2025."

---

## LÁMINA 28 (PDF p27) — Mapa "Actualmente tenemos 12 clínicas en 6 estados" (SANEFRO)
Título: **"Actualmente tenemos 12 clínicas en 6 estados"**. Mapa con pins:
- **Baja California:** Tijuana
- **Nuevo León:** Monterrey
- **Guanajuato:** Irapuato, León
- **Jalisco:** Venezuela, Moctezuma, Palomar, La Paz, Cd Guzmán
- **Colima:** Colima, Manzanillo
- **Michoacán:** Zamora
(12 clínicas: Tijuana, Monterrey, Irapuato, León, Venezuela, Moctezuma, Palomar, La Paz, Cd Guzmán, Colima, Manzanillo, Zamora.)

---

## LÁMINA 29 (PDF p28) — "Venta anual SANEFRO" (waterfall por clínica)
Título: **"Venta anual SANEFRO"**. Cascada $M (leyenda: Riesgo / Sin riesgo). Fila "Pacientes totales".
| Nodo | Venta $M | Pacientes totales |
|---|---:|---:|
| Total | $1,005 | 4,110 |
| ZMG | $413 | 1,643 |
| Irapuato | $127 | 571 |
| Colima | $114 | 458 |
| León | $114 | 570 |
| Tijuana | $94 | 320 |
| Monterrey | $53 | 210 |
| Otras (3) | $90 | 338 |
**Desglose ZMG ($413):** Venezuela $207 (50%) · Moctezuma $85 (21%) · Palomar $75 (18%) · La Paz $46 (11%).
**Desglose Otras (3) ($90):** Zamora $35 (3%) · Manzanillo $34 (3%) · CD. Guzmán $21 (2%).
(Suma ZMG 207+85+75+46 = 413. Suma Otras 35+34+21 = 90.)

---

## LÁMINA 30 (PDF p29) — "Resultados Anestesia" (2022–2026, YTD/YTG)
Etiqueta: **"Resultados Anestesia"**. Barras YTD/YTG $M.
| Año | YTD | YTG | Total |
|---|---:|---:|---:|
| 2022 | $25 | $37 | $62 |
| 2023 | $36 | $41 | $76 |
| 2024 | $33 | $32 | $65 |
| 2025 | $61 | $57 | $118 |
| 2026 | $53 | (n/d) | (solo YTD) |
Delta 2026 vs 2025 YTD: **−$8 (−13%)** (53 − 61 = −8).

---

## LÁMINAS 31–36 (PDF p30–p35) — Cascada "Frasco Cerrado" en build (animación)
Las 6 láminas son **cuadros de animación progresiva** de la cascada de la Lámina 3 ("¿Qué está pasando en gobierno? / Frasco Cerrado – Alcance a Meta Ene-Jun 2026"). El estado final (L36) reproduce completa la L3:
- Meta 6,658M (Servicios 2,757M + FC 3,901M) → PIN 4,266M → Pedidos 3,993M (102%) → Sin Atender 704M (18%; $544 Negado + $90 Sin inv + $70 Inv Conf Fact Julio) → Fact Ped 2025 54M (1%) → subtotal 3,343M → Venta Ene-Jun 2026 3,235M (83%) → Notas de Crédito 108M (3%) → Vta Perdida 121M (3%) / 342M (9%) → PIN NO SOL 859M (22%).
Progresión de reveal por lámina: L31 hasta "Venta"; L32 hasta "Notas de Crédito"; L33 hasta "Vta Perdida" (108M/3% visible); L34 hasta ~342M(9%); L35 y L36 cascada completa con "PIN NO SOL 859M (22%)".

---

# Inconsistencias internas
1. **Mezclas L9 — delta contradictorio:** la gráfica etiqueta el cambio YTD 2026 vs 2025 como **−$39 (−4%)** (886 − 925), pero el cuadro de texto dice "afectación de **−$50 M** YTD vs 2025". No cuadran (−39 vs −50).
2. **Diálisis L12 — placeholder sin resolver:** caja azul con instrucción interna **"Meter numero de mezclas y precios"** (tarea pendiente dejada en la lámina de Consejo).
3. **Mezclas L10 — placeholder:** Mg Op 2018 = **"TBD"** (sin dato).
4. **Hemodiálisis L27 — dos métricas de crecimiento mezcladas:** la gráfica marca **+$64 / +13%** (valor $ YTD 26 vs 25), pero el texto afirma "**sesiones han incrementado 6%**". El +13% es valor y el 6% es sesiones (posible reconciliación por precio), pero tal como está redactado puede leerse como cifras en conflicto.
5. **L25 — título erróneo:** el título dice **"DIALISIS PERITONEAL ISSSTE"** cuando el contenido es **OTROS** (columnas "% de/del OTROS", instituciones ISSSEMYM/PEMEX/etc.). Copia-pega no corregido de la L23.
6. **L7 vs L8 (oculta) — rótulo inconsistente:** L7 rotula la fila "**Vta. Ult. 12 Meses**" y L8 "**Vta. Mensual**" con los MISMOS valores ($1,032 / $1,100 / $1,042). Uno de los dos rótulos es incorrecto (un valor de $1,032–$1,100 no puede ser a la vez venta mensual y venta de 12 meses).
7. **L8 oculta:** existe una segunda versión de "Cartera Gobierno" con desglose "Proceso Cliente" (Ingresado $2,295 / Trámites con Dependencia $0,793 / Formalización de Contratos $0,026) que quedó **oculta**; el Consejo verá la L7 (versión FC/Servicios) en su lugar.
8. **DP — rótulos de PiSA en delegaciones L16 vs L19:** L16 (Top 15) reporta p.ej. Nuevo León 76%/24% y Edo. Mex. Oriente 94%/6% con 2,471 pacientes; L19 (17 dominantes) reporta Nuevo León 72%/28% (1,435 pac.) y Edo. de Méx. Ote. 94%/6% con **2,607** pacientes (vs 2,471 en L16), además de un renglón adicional "Nuevo Leòn 100%/0% 206 pac.". Las bases de pacientes por delegación difieren entre ambas tablas.
9. **Láminas 4–6 triplicadas** (idénticas) y **31–36** como frames de animación: inflan el conteo; no aportan datos nuevos frente a L4 y L3 respectivamente.

# Posibles choques con la referencia sell-in (solo se flaguean; no se resuelven)
> Referencia (sell-in 1S 2026, cierre junio, $M MXN): PISA 5 mercados 16,518.5 / meta 17,678.3 = 93.4%, +1.5% vs 1S25. Gobierno Frasco Cerrado 4,034.3 / 90.0% / −0.6%. Servicios 2,219.4 / 102.1% / +4.0%. PVM PISA: volumen −830.7 / precio+mezcla +1,070.0 (piezas −5.1%).

1. **Frasco Cerrado — venta y meta no coinciden con la referencia.** La cascada L3/L36 muestra **FC meta 3,901M** y **FC Venta Ene-Jun 2026 = 3,235M (83%)**. La referencia da **Gobierno FC = 4,034.3M / 90.0%** (venta). Choque: 3,235M(83%) [deck] vs 4,034.3M(90%) [ref] en venta FC; y meta 3,901M [deck] vs ~4,483M implícita [ref, 4,034.3/0.90]. Posible diferencia de alcance (el "FC" de la cascada excluye Servicios; la referencia "Gobierno FC" puede tener perímetro distinto).
2. **Servicios — la referencia CUADRA con la suma de líneas de servicio del deck (consistencia, no choque).** YTD 2026: Mezclas $886M + Diálisis $735M + Hemodiálisis $545M + Anestesia $53M = **$2,219M**, que iguala **Servicios 2,219.4M** de la referencia. Fuerte alineación. **SANEFRO ($1,005M anual, hemodiálisis privada) queda FUERA de esa suma** — verificar si Servicios (ref) lo excluye o si es venta anual vs YTD.
3. **"Servicios 2,757M" en la cascada L3 vs 2,219.4M (ref).** El 2,757M es una **componente de META** del nivel de servicio gobierno (meta total 6,658M = FC 3,901 + Servicios 2,757), mientras 2,219.4M es **venta** real. No comparables directamente, pero conviene confirmar por qué la meta de Servicios (2,757M) supera la venta (2,219M ≈ 80% de esa meta) cuando la referencia da Servicios al **102.1%** de SU meta.
4. **PVM (dirección consistente cualitativamente).** El deck atribuye el crecimiento de Servicios/Diálisis "totalmente al incremento de precio" (L12), precios SAFE +6% y +24% sobre competidor (L11), DP +15–20% anual en prevalentes (L15). Coherente con la referencia PVM (precio+mezcla +1,070.0, volumen −830.7, piezas −5.1%). No hay cifra PVM en el deck para cuadre numérico.
5. **Meses de cartera y cifras de gobierno (L7):** cartera 30 Jun 2026 $4,834M, FC 5.3 M.C. / Servicios 3.4 M.C. — no hay contraparte en la referencia sell-in; se reporta como dato nuevo del deck (posible insumo, no choque).

# Vacíos declarados
1. **L10 — Mg Op 2018 = "TBD"** (dato faltante).
2. **L12 — "Meter numero de mezclas y precios"**: cuadro/tabla de número de mezclas y precios de diálisis **pendiente de insertar**.
3. **L13 — "Estados con información:"** la lista de estados del IMSS Bienestar (17 estados / 54% población / hasta +5,755 pacientes) queda **enunciada sin desplegar** en esa lámina (el detalle por estado sí aparece luego en L21, pero L13 corta la frase).
4. **Años 2026 sin YTG en todas las series de "Resultados" (L9 mezclas, L12 diálisis, L27 hemodiálisis, L30 anestesia):** solo se muestra YTD 2026; el YTG (Year-To-Go) 2026 no está graficado (por definición aún no ocurre), por lo que el total anual 2026 proyectado no está en el deck.
5. **L1 — presupuesto salud gobierno sin valores absolutos:** solo índices/porcentajes (−9%, +6%); no hay el monto base del presupuesto.
6. **Precios SAFE (L11) — series ONCO/NPT/ATB con etiquetas parcialmente encimadas en el render;** valores nativos capturados, pero algunos labels de años intermedios se solapan (p.ej. ONCO 2020–2021). No hay nota de fuente del precio (a diferencia de L1 que sí cita INEFAM).
7. **Notas de Crédito (L4–6) — corte "Actualizado al 02 Julio 2026"**; el resto del deck (gobierno FC, servicios) no declara corte homogéneo salvo esa mención, por lo que el as-of de cada lámina no está uniformado explícitamente.
8. **Márgenes/EBITDA de Servicios:** el deck reporta Mg Bruto y Mg Op solo para mezclas (L10); no hay márgenes para diálisis, hemodiálisis, anestesia ni SANEFRO.

---
*Ruta de este extracto:* `/Users/rafaelprince/Claude Code/consejo-27jul/inputs_nuevos/EXTRACT_ppt_consejo_servicios.md`
*PNGs de trabajo (scratchpad, no del proyecto):* `/private/tmp/claude-501/-Users-rafaelprince-Claude-Code/557bd416-2b4f-41c7-bd5f-689b38a35a10/scratchpad/serv_p01.png` … `serv_p35.png`
