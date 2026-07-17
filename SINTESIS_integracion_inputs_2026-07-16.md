# SÍNTESIS DE INTEGRACIÓN · Insumos nuevos 16-jul → Storyline v6
**Proyecto:** Consejo Pharma MX 27-jul-2026 · **Fecha:** 16-jul-2026
**Qué es:** el veredicto de integración sobre los 10 insumos nuevos (extracciones exhaustivas en `inputs_nuevos/EXTRACT_*.md`): qué entra al storyline v6, qué no, qué choca y qué sigue faltando. Rafael valida este documento junto con el v6.

---

## 1. Qué llegó y qué es cada cosa

| Insumo | Qué es | Veredicto de uso |
|---|---|---|
| `Consejo Farmacias.pptx` (29 lám.) | Tablero del canal Farmacias/FARMA MX: mercado Knobloch + sell-in + NADAL por UDN + lanzamientos | ENTRA fuerte: L2, L11, L12 (burbujas TACC5 vs LY ya existen), L14, L16, L34 |
| `Presentacion RP HP_Consejo_Hospitales.pptx` (16 lám.) | Deck del canal Hospitales: tres frentes con datos duros, cascadas propias, plan 2S 7 palancas | ENTRA fuerte: L21, L22, L24, L25; sus cascadas solo como insumo (taxonomía propia, bugs internos) |
| `20260529 PPT Hospitales DG.pptx` (20 lám.) | Deck Hospitales a DG (ventana ene-abr) | Banco de láminas para ANEXOS (Muguerza, PxV, GASS vs SAFE, distribuidores); no al cuerpo (datos a abril) |
| `CONSEJO 27 DE JULIO_Servicios.pptx` (35 lám.) | Deck Servicios/Gobierno de David Silva: nivel de servicio FC (universo pedidos), NC, cartera, mezclas, DP vs Baxter, SANEFRO | ENTRA fuerte: L17-L20 (candidatos), L26-L30 (sizing DP es oro); cuadre Servicios exacto con sell-in |
| Transcript 07-01 (sesión IQVIA) | IQVIA presenta la caída de abril + forecast a PiSA | ENTRA: L11 (tesis "abril no es outlier"), L2 (forecast), efecto gobierno |
| PDF IQVIA abril (31 pp) | El material de esa sesión | Extracción relanzada (falló por error de API, no de contenido); cifras del transcript por cotejar contra el PDF |
| `Estado de Resultados Jun26 v18` | P&L Farma MX de Finanzas, 6 bloques | ENTRA: EBITDA de la tablita L6 por fin existe — con dos problemas estructurales (ver §4.1) |
| Paquete `Downtrading_Privado_v4_FINAL` | La nueva clasificación del puente (5 conceptos), Privado terminado y auditado | ENTRA como NUEVA CONVENCIÓN de cascadas (decisión Rafael 16-jul); define la col-2 de la lámina 15/50/35 |
| `Puente_PVM_VistaConsejo_5lineas` + 2 cubos downtrading | Puente por 10 canales (+$232.5M) + diagnósticos de down-trading por segmento/molécula | PARCIAL: los cubos son diagnóstico (cobertura parcial, no reconcilian); la Vista Consejo choca de estructura (ver §4.2) |
| Transcript 07-15 (gobierno/servicios) | Revisión de láminas con David/Dani | ENTRA como CANDIDATOS (VP 463, PIN 859/869, NC 330) — confirmado por Rafael: aún no canónicos |

## 2. La nueva lámina de puente por segmento (decisión Rafael 16-jul, RIGE)

Sustituye la convención v5 de llaves volumen/precio+mezcla. Una lámina por segmento (y la rectora PISA), tres columnas:

- **Col 1 (15%):** barra crecimiento del MERCADO vs crecimiento PISA del segmento.
- **Col 2 (50%):** puente de ventas con la clasificación nueva (maquinaria Downtrading v4): **Precio · Volumen · Mix (down-trading) · Lanzamientos · Gestión de Portafolio**, control = 0.
- **Col 3 (35%):** comparativo **1S-2025 vs 1S-2026** de cuatro métricas: venta perdida · PIN no solicitado · NC comerciales · NC logísticas. (Rafael dictó "S1/2025 vs S2/2025"; se lee 1S25 vs 1S26 — confirmar.)

**Estado por segmento:**

| Segmento | Col 1 (mercado vs PISA) | Col 2 (puente 5 conceptos) | Col 3 (comparativo 1S25 vs 1S26) |
|---|---|---|---|
| Retail | Entry Market −4.2% vs PISA −0.1%/+0.4% [unificar corte, §4.6] | **LISTO** (v4 FINAL, auditado) | VP lista (359.0→343.5); PIN sin comparador 25; NC por llegar |
| Gobierno FC | INEFAM −3.8% vs −0.6% | En construcción (misma maquinaria) | Candidatos transcript 07-15; definición VP en cierre |
| Hospitales | [−5% validar IQVIA] vs +5.1% | En construcción | VP lista (188.2→114.5); PIN nivel 71 sin comparador; NC por llegar |
| Servicios | n/a modelos propios (col-1 se declara) | En construcción | VP ~0; PIN n/d; NC [DS] |
| PISA (rectora) | Mercado total vs +1.5% | En construcción (consolida los 4) | VP lista (−143.1 efecto); resto parcial |

**El puente Retail, números finales (v4, MXN M, 1S26 vs 1S25):** Precio **+392.9** · Volumen **−169.7** · Mix/down-trading **−197.9** · Lanzamientos **+43.8** flujo genuino (**+71.1** si se reclasifican los $27.3M de adelanto nov-dic-25) · Gestión de Portafolio **−37.8** → Δ **+31.3M bruto** (= el +0.4% oficial) / **+58.7M reclasificada** (analítica).

**Recomendación de lámina (decisión pendiente de Rafael):** mostrar la vista BRUTA (+31.3, cuadra con la tablita y el cubo) con nota al pie de la reclasificación; la advertencia del propio handoff v4 es que +58.7M NO es el crecimiento sell-in oficial.

**Qué gana el deck con la nueva vista:** el "+0.4% plano" de Retail se abre en su física real — el precio de lista sube fuerte (+$392.9M), pero el down-trading (−$197.9M: la marca cede al genérico propio a 1/12 del precio por mg, caso Ceftriaxona/Cefaxona) y el volumen (−$169.7M) se lo comen; el neto lo sostienen los lanzamientos. Top-5 down-traders = Amox/Clav −45.6 · Levofloxacino −32.9 · Ceftriaxona −24.7 · Enoxaparina −21.3 · Fexofenadina −15.9 (71% del Mix). FRISO migra hacia ARRIBA (+16.4M). Esto blinda la narrativa "valor sobre volumen" con mecanismo y culpables.

## 3. Qué entra al storyline v6, por momento

- **L2 (resumen):** comparativa mercado vs PISA con datos frescos y comparables (mismo universo Knobloch): Entry Market −4.2% valor / −7.9% unidades vs PiSA −0.1% / −9.4%; mercado privado sin GLP-1 +1.4% valor / −4.8% unidades (MAT may-26) — mata definitivamente el "−3% sin GLP-1". BBVA −4.9% jun-26 (research). Forecast IQVIA para encuadre 2S: mercado ~3.5-4.5% valores / ~1% volumen; sin GLP-1 ~2.7-3%.
- **L6 (tablita):** EBITDA real de Finanzas v18: Retail $2,479.1M (34.4%) · Hospitales $1,196.8M (39.2%) · Gobierno+Servicios COMBINADO $804.8M (12.9%) · Soporte −$601.1M · total $3,879.6M (23.5% vs 19.7% en 2025). Split FC/Servicios NO existe en la fuente (§4.1).
- **L7 (boleta):** DP público PiSA 31% vs Baxter 69% (en IMSS 42%); Biossmann re-matizado (85% de su venta es gobierno); India vía reliance (292 autorizaciones) como amenaza citable.
- **L11 (entorno retail):** tesis IQVIA "abril no es outlier, es tendencia" (respiratorio estructural, W.A.I.T./FAN); abril: mercado +3.1% valores / −13.8% unidades, sin GLP-1 −2.4% valores; efecto gobierno (compra pública contamina retail); VM el subsegmento más golpeado (−6.7% valor / −13.8% unidades); cadenas +13% vs independiente plano; Marzam/OMNi.
- **L12 (burbujas):** YA EXISTEN en el deck Farmacias (L14-L17: TACC5 vs LY por línea terapéutica, mercado total/ético/genérico/OTC). El "TAC 1 año" pendiente = el eje LY de esas láminas. Falta rotular valores [CC].
- **L13/18/23/28 + L8:** la nueva lámina 15/50/35 (§2).
- **L14 (doble clic):** UDN reales (VM +2%, MP −10% corrigiendo, Consumo +24%, Friso −2%); conflicto OTC/Consumo documentado con ambos lados (§4.7).
- **L16 (plan 2S retail):** NADAL junio por UDN honesto (MP 98% · Consumo 87% · Impulso 66% · EXP 186% · RX 0%); GAP lanzamientos (total 63% ene-jun, 83% proyección anual; Votripax 57% / Pisalak 68% / Pixiba 73%).
- **L17-L20 (gobierno):** research (2.6% PIB vs 6% OPS; adeudos 14k vs 5k; consolidada anulada; bianual fallo 28-ago-26) + candidatos del universo PEDIDOS (pedidos 3,901 vs meta 3,993; no atendido 704 = 544 negado + 90 sin inv + 70 conf; sanciones 108 aparte; "la acabó la factura 463 / la acabó comercial 859") + cartera junio-junio 4,834M +22% (FC 5.3 meses / Serv 3.4).
- **L21-L22 (hospitales):** ocupación 59%, siniestralidad ~131k, primas +6-10%/+40%, inflación médica 14.8%, IVA 16% no acreditable, aseguradoras cubren 80-85%; tres frentes CON números: Mindray bombas $110-121 vs $227 (200 clientes compran >$200), Baxter $17 = −40% en cuentas puntuales, TI $1,473M (Soluciones+EqBomba $930M = 63% de la línea), Kener catálogo cruzado ~$850M (~$300M corporativos) y ~$43M ya desplazados en Ángeles 2025; corrección research: frente 2 = "Baxter/Vantive".
- **L24-L25:** asterisco de junio con detalle del canal (5 lunes + ~$10M one-off ABC/OCA); plan 2S: gap $57M/mes cubierto con $47M/mes en 7 palancas nombradas.
- **L26-L30 (servicios):** sizing DP vs Baxter completo (53,400 pacientes públicos; $5,631M; Bienestar+ISSSTE hoy 100% Baxter = espacio; Baxter +27-49% más caro; complejidad logística de entrega domiciliaria como foso); SANEFRO 12 clínicas / 4,110 pacientes / ~$1,005M anual; líneas YTD que CUADRAN exacto con sell-in (886−4% + 735+10% + 545+13% + 53−13% = 2,219.4 ✓); frame de David/Dani: dos caras (SAFE chico y riesgoso vs HD/diálisis/anestesia a invertir) + historia de precios; riesgo tecnológico de diálisis (equipos chinos, espejo Mindray).
- **L34 (portafolio):** lanzamientos con lista autoritativa v4 (11 con material, 7 abiertos sin match); semaglutida/reformas abril (research).
- **Anexos:** banco DG may-29 (Muguerza 274 claves/$220M, PxV 32 hospitales/$9.4M mes, GASS vs SAFE onco, distribuidores −21/−59%), cartera gobierno, DP sizing detalle.

## 4. Conflictos y decisiones abiertas (lo que NO se imprime sin resolver)

1. **EBITDA FC vs Servicios NO separable:** Finanzas funde GOBIERNO ($6,253.7M venta, EBITDA $804.8M, 12.9%). Opciones: (a) tablita muestra Gobierno+Servicios combinado con nota; (b) pedir split a [VJ/Finanzas]. v6 va con (a) declarado + pendiente (b). Además: SOPORTE −$601.1M sin hogar (los 4 segmentos no suman el total sin él) y hay dos EBITDA (UN $3,941.9 vs final $3,879.6) — v6 usa el FINAL y lo declara. OJO transcript: el 0% de diálisis y el recorte de SAFE (500→100) vienen de reclasificaciones de Finanzas en disputa — el EBITDA de Servicios, cuando llegue, llega contaminado de esa pelea.
2. **Dos "puentes de 5 líneas" conviven:** la maquinaria v4 (Precio/Volumen/Mix/Lanzamientos/Gestión; Privado listo) y la `Puente_PVM_VistaConsejo_5lineas` del 14-jul (Precio/Volumen/Mix/Nuevos Productos/Resto + Devoluciones, por 10 CANALES, Δ +$232.5M). La Vista Consejo no cierra contra la referencia (+232.5 vs +239.3) ni se reparte a los 4 segmentos (no hay tabla canal-segmento). Lectura: es el borrador previo al v4. **Confirmar con Rafael que la canónica es la maquinaria v4 y la Vista Consejo queda superseded.**
3. **Venta perdida gobierno, 4 números en juego:** 342 (restricto) / 443.9 (DP ene-may) / 463 (elegido en llamada, candidato) / 595-600 (Fer Mendoza). Definición única antes de lámina [DS/FM/Rafael].
4. **PIN no solicitado gobierno:** 859 vs 869 (ASR) vs 790 (versión previa); a planchar con Hugo y Daniel Torres. Y no existe PIN 1S25 (la col-3 lo declara, no lo inventa).
5. **NC gobierno:** deck Servicios dice 428 total (−53% vs 25; 357 aplicadas + 71 pendientes); transcript dice 330 devoluciones (~55/mes, Dani revisa si excluye sanciones 108; a Rafael le sonaba ~70/mes; 2025 ≈ 357). Cerrar una sola cifra con universo [Dani/DS].
6. **"Nuestro mercado" retail, dos cortes Knobloch:** mercado foco PISA/AMSA −3.4% YTD (v5) vs Entry Market −4.2% LY MAT may-26 (deck canal, sin electrolitos/FI/GLP-1). v6 adopta Entry Market (mismo universo que la comparativa PiSA del canal, más defendible) y retira el foco −3.4% — confirmar [CC/Rafael].
7. **OTC vs Consumo:** sublínea OTC sell-in $91.0M (102.6%, +46.1%) vs UDN Consumo del canal $147M (81%, +23.7%). Son cortes distintos (OTC ⊂ Consumo). Elegir cuál cuenta la historia en L14 [Rafael+IC].
8. **Universo PEDIDOS ≠ sell-in en gobierno:** pedidos 3,901 vs meta 3,993 (transcript) pero el deck Servicios rotula meta FC 3,901 y venta 3,235 (83%); y la meta sell-in FC es 4,484.9 (90.0% de alcance). Tres cifras de "meta" en el aire; el puente pedidos→facturación→venta neta debe declararse antes de imprimir la lámina de nivel de servicio [DS/Dani].
9. **Cascadas propias del canal Hospitales:** taxonomía distinta (Precio −8 / Volumen +93 / Descuentos 0 / Altas y Bajas +25 / Servicios +41 = +149) con bugs internos (desglose regional copy-paste entre L11/L12, rótulos invertidos en L12). Se usan como insumo del puente v4 de Hospitales, NO se heredan al deck.
10. **Frente Baxter:** el deck del canal declara la respuesta "Por definir" mientras el v5 ya narra defensa de base instalada — alinear con Martín qué se dice el 27 [Martín/CC]. Y el research obliga "Baxter/Vantive" (Vantive-Carlyle es además el rival renal de DP con USD 70M en Cuernavaca).
11. **"PiSA creció 9% en junio" (Felipe, sesión IQVIA)** sin universo declarado, y su frase "llegamos a meta con volumen, no valores" contradice el PVM (piezas −5.1%, todo precio/mezcla). Aclarar antes de que suba a cualquier lámina [Felipe/Rafael].
12. **Mercado gobierno:** AlphaDog/INEFAM da +30-35% pedidos genéricos (rechazado por Rafael; Chery re-pide con definiciones); el borrador trae −5%/−3.9%. Los bullets de la lámina (competidores por clave, erosión, % compras directas) siguen sin datos duros [Chery/DS].

## 5. Qué NO entra (y por qué)

- **La Δ reclasificada +58.7M como "crecimiento de Retail"** — advertencia explícita del handoff v4; el oficial es +31.3M/+0.4%.
- **Ingresado/no ingresado de cartera (~3,500M) y Bienestar $205M por ingresar** — instrucción de Rafael 07-15: no es frase de Consejo (vive como soporte interno).
- **El pleito de reclasificaciones con Finanzas (diálisis 0%, SAFE 500→100)** — off-record; al Consejo solo llega el EBITDA conciliado o el hueco declarado.
- **Detalle de contención/inventario del PIN** — simplificado por Rafael al idioma consejero (factura vs comercial).
- **Costos de fuentes (Knobloch ~$1M/mes, AlphaDog ~$60K/mes)** — anécdota interna.
- **Cascadas del canal Hospitales tal cual** (bugs y taxonomía propia) y **deck DG may-29 al cuerpo** (ventana a abril, superseded por el 1S).
- **Vendors públicos de GLP-1 como contraste** y todo lo ya descartado en v5/research (sin cambio).

## 6. Qué sigue faltando (el pedido a Rafael y responsables)

1. **Número del 2S** [Heriberto, antes del 20] — sigue exógeno, nada se construye aguas abajo.
2. **Puentes v4 de Gobierno FC / Hospitales / Servicios** [equipo PVM — en construcción, confirmado por Rafael].
3. **Venta perdida / PIN / NC formales** (por segmento, 1S25 vs 1S26, definición y universo declarados) [Rafael los manda] — la col-3 de las 5 láminas de puente vive de esto.
4. **EBITDA split FC/Servicios** o bendición del combinado [VJ/Finanzas].
5. **Vista IQVIA del mercado hospitalario / validar −5%** [CC] — la L3 del deck del canal venía VACÍA (EMF sin datos); sigue abierto.
6. **TAC 1 año rotulado para burbujas** [CC] — el concepto ya está en el deck del canal; faltan valores impresos.
7. **Efecto mercado monetizado** [CC/DS] y **nuevos productos 1S por segmento fuera de Retail** [VW].
8. **Confirmaciones de Rafael:** col-3 = 1S25 vs 1S26 (¿o 1S25 vs 2S25?); vista bruta vs reclasificada en la lámina Retail; Entry Market como corte de mercado; Vista Consejo 5líneas superseded; ¿el v5 llegó a Felipe/Edmundo?

---
*Extracciones completas: `inputs_nuevos/EXTRACT_*.md` (9 en disco; IQVIA en curso). Este documento decide; las extracciones prueban.*
