# HANDOFF · Consejo 27-jul · Rediseño v7 APROBADO, ejecutar pasos 6-8
**Proyecto:** Presentación al Consejo de Pharma MX, lunes 27-jul-2026 · **Fecha del handoff:** 16-jul-2026, noche
**Estado en una línea:** Rafael aprobó COMPLETO el rediseño v7 ("de acuerdo con todo", incluidos los 4 retos); la sesión que retome ejecuta los pasos 6-8: escribir ~38 specs nuevas según `PROPUESTA_rediseno_v7_2026-07-16.md`, dibujarlas en 9 carriles de Codex y reensamblar el storyboard en PPT por momentos.

**OJO ARQUITECTURA DE EJECUCIÓN (decisión Rafael 16-jul noche):** el paso 6 (escribir las 38 specs) lo hace una **SESIÓN DE NUBE**; los pasos 7-8 (Codex dibuja, PPT se ensambla) se hacen DESPUÉS en una sesión LOCAL en la Mac de Rafael (Codex CLI, renders, LibreOffice). El corpus completo ya está subido a la nube (ver §0).

## 0. UBICACIÓN DE LOS ARCHIVOS (mapa nube/local — leer antes que nada)

**EN LA NUBE (OneDrive corporativo PiSA, carpeta `Consejo27jul_nube/`; ruta local sincronizada: `~/Library/CloudStorage/OneDrive-LABORATORIOSPISAS.A.DEC.V/Consejo27jul_nube/`):** el corpus COMPLETO del paso 6 — 64 archivos, 2.3MB, todo texto:
- Raíz: este handoff · `PROPUESTA_rediseno_v7_2026-07-16.md` (la biblia) · `APRENDIZAJES_y_metodo.md` · `README_dibujante.md` (reglas/caveats/calibraciones) · los 2 veredictos de consejo · `SINTESIS_integracion_inputs_2026-07-16.md` · `Storyboard_v2_consolidado_2026-07-16.md` · `Research_Consejo_27jul_2026-07-10.md` · `MEGADOC_Consejo_27jul_Fuentes_2026-07-10.md` · `build_storyline_v6.py` (léelo como documento).
- Raíz (complementos): `HANDOFF_storyline_consejo_27jul_2026-07-10_0725.md` (VIGENTE solo en §3 números sell-in y §7 trampas de los cuatro universos; su §5 estructura está STALE) · las 3 minutas de revisiones del 8-jul + `Consejo27jul_Sintesis_Revisiones_Jun26_2026-07-09.md` (narrativas por segmento) · `CONTEXTO_CLAUDE_global.md` (las reglas de trabajo y calibración de Rafael: síguelas como si fueran el CLAUDE.md de la sesión).
- `storyboard_v2_specs/` — las 35 specs individuales (el banco de material del campo "absorbe").
- `inputs_nuevos/` — los EXTRACT (18) y el `INPUT_pin_vp_privado_2026-07-16.md`.
- `puentes_insights/` — los 5 INSIGHTS curados de los puentes canónicos (la matriz 8×4 con conciliación vive en `INSIGHTS_PiSA_Consolidado_FINAL.md`) + los 2 HANDOFF de método del downtrading (reclasificación y lanzamientos).
- `design_system/` — `ppt.md` (perfil PPT del sistema visual PiSA) y `tokens.json` (paleta canónica): OBLIGATORIOS para las secciones de gráficas y los prompts de imagen de cada spec.
- **`storyboard_v3_specs_AQUI_ESCRIBE_LA_NUBE/` — VACÍA a propósito: la sesión de nube escribe AQUÍ sus 38 specs nuevas** (`SB_L01.md` a `SB_L38.md` según la numeración de la PROPUESTA), cada una con su sección final "## Instrucciones ChatGPT Images 2". Nada más se escribe fuera de esa carpeta.

**SOLO LOCAL (Mac de Rafael; la nube NO los necesita):** `consejo-27jul/storyboard_v2/renders/` (35 PNG, 47MB) y los PPT de revisión · los .docx regenerables · los xlsx fuente (`~/Downloads/PVM_Reconstruido_scripts/v2/Downtrading_*_FINAL*.xlsx`, `Gross2Net.xlsx`, `PL Gobierno vs Servicios.xlsx`, `PnL Diciembre.xlsx`, Estado de Resultados v18; sus contenidos ya viven en los EXTRACT de la nube) · el Codex CLI y `build_storyboard_ppt.py`.

**FLUJO DE REGRESO:** la sesión de nube termina el paso 6 → OneDrive sincroniza solo → una sesión LOCAL copia `storyboard_v3_specs_AQUI_ESCRIBE_LA_NUBE/` a `consejo-27jul/storyboard_v3/`, hace la verificación de primera mano (auditoría mecánica + cuadres) y ejecuta pasos 7-8 (9 carriles Codex + PPT por momentos).

**Calendario (al 16-jul noche):** número del 2S con Heriberto antes del 20 · kill-list de corchetes el 21 · PPT con datos financieros finales a Presidencia el miércoles 22 · junta lunes 27. Nada se construye aguas abajo del [96].

---

## 1. Qué se hizo el 16-jul (la sesión más larga del proyecto)

- **AM:** 10 insumos nuevos extraídos exhaustivamente (agentes Opus, `inputs_nuevos/EXTRACT_*.md`) → síntesis de integración → **storyline v6** construido (gate 0/0) → **consejo adversarial 1** (McKinsey + patrimonial) → 12 fixes aplicados al v6.
- **PM:** storyboard v2 completo: 35 specs con prompts de ChatGPT Images 2 integrados → Codex dibujó las 35 en carriles paralelos → PPT de revisión → **consejo adversarial 2** (IQVIA/McKinsey/BCG/ArtDirector/Brunswick sobre los DIBUJOS) → veredicto consolidado.
- **Tarde-noche:** llegó el **paquete canónico de Rafael** (5 puentes Downtrading FINAL verificados al peso por 2 agentes; tablas PIN/VP 1S25vs26; Gross2Net con NC/devoluciones y split EBITDA FC/Servicios; P&L split verificado; PnL Diciembre FY25) → **ola de integración única**: 35 specs actualizadas con puentes reales + capa A del consejo 2 + kill-list → redibujo total (7 carriles) → **PPT por momentos** (índice + máx 4 fotos/hoja sin mezclar momentos) entregado.
- **Noche:** Rafael ordenó el rediseño (8 pasos) → **3 arquitectos independientes** (IR/operador/consejero) desde cero → **síntesis + auto-reto → `PROPUESTA_rediseno_v7_2026-07-16.md` → APROBADA COMPLETA por Rafael.**

## 2. Estado canónico (archivos y roles)

Home: `/Users/rafaelprince/Claude Code/consejo-27jul/` · Sin git · Nada se edita a mano; todo entregable se regenera desde script.

| Archivo | Rol | Estado |
|---|---|---|
| `PROPUESTA_rediseno_v7_2026-07-16.md` | **LA BIBLIA del siguiente paso**: arquitectura aprobada de 38 láminas (22 cuerpo + 16 anexos), títulos redactados, gráficas por lámina, mapa viejo→nuevo, lista de salto, retos aprobados | Canónico, APROBADO |
| `storyboard_v2/SB_L01.md … SB_L35.md` | Las 35 specs v3 con datos canónicos integrados: **BANCO DE MATERIAL** para las 38 nuevas (títulos, cifras, layouts, prompts). El mapa "absorbe" de la PROPUESTA dice qué spec vieja alimenta cada lámina nueva | Vigentes como fuente; serán superseded por v7 |
| `storyboard_v2/README_dibujante.md` | **Reglas transversales + caveats de citación + calibraciones de Rafael** (incluida "no abusar del número héroe") | Canónico, se hereda a v7 |
| `storyboard_v2/renders/*.png` (35) + `Storyboard_visual_35laminas_2026-07-16.pptx` | El storyboard v3 dibujado y su PPT por momentos | Entregado; STALE para v7 (referencia visual) |
| `storyboard_v2/build_storyboard_ppt.py` | Ensamblador PPT por momentos (índice + 4/hoja) | Se adapta a las secciones v7 |
| `CONSEJO_veredicto_2026-07-16.md` y `CONSEJO2_storyboard_veredicto_2026-07-16.md` | Los dos consejos adversariales; el 2 trae el plan de adelgazamiento y la kill-list | Vigentes: NO reintroducir lo matado |
| `SINTESIS_integracion_inputs_2026-07-16.md` + `inputs_nuevos/EXTRACT_*.md` (14) + `INPUT_pin_vp_privado_2026-07-16.md` | Qué es canónico/candidato + extracciones exhaustivas de todos los insumos | Vigentes |
| `build_storyline_v6.py` (+docx, gate 0/0) | El storyline Word con consejo 1 aplicado | **UN PASO ATRÁS de las specs** (los puentes canónicos y capa A viven en specs, no en el Word). Actualizarlo NO bloquea los pasos 6-8; es deuda para antes del 22 |
| `HANDOFF_consejo27jul_2026-07-16_storyline_v5_y_research.md` | Handoff de la mañana | STALE en estado; útil como historia |
| Puentes fuente: `~/Downloads/PVM_Reconstruido_scripts/v2/Downtrading_*_FINAL_2026-07-16.xlsx` + INSIGHTS; `~/Downloads/Gross2Net.xlsx`, `PL Gobierno vs Servicios.xlsx`, `PnL Diciembre.xlsx` | Los canónicos de datos (verificados al peso por agentes; extractos en inputs_nuevos) | Congelados C7 |

## 3. Números clave (auditados hoy contra workbooks recalculados; $M MXN, 1S26 vs 1S25)

- **Matriz de puentes (única fuente de cascadas):** TOTAL PiSA: Precio +66.9 / Volumen +281.8 / Mix core −297.0 / Gestión +28.0 / Lanzamientos +94.4 / Terceros +95.5 / Servicios +51.8 / Sin unidad −49.4 = **+272.1 reclasificada → −31.7 → +240.3 → −1.0 → +239.3 SELL-IN OFICIAL** (16,279.2 → 16,518.5; control 0). Por segmento: Privado +58.7→+31.3→+31.8 · Hospitales +153.8→+149.4→+147.9 (core +14.3; Terceros +112.1, KEYTRUDA +28.6; cobertura 65.0%) · GobFC −24.9 (3 niveles idénticos; Precio −320.3/Volumen +425.2 con FLEBOTEK +105/EPO +71.7/Heparina +71.2; cobertura 78.9%) · GobServicios +84.5 POR VALOR (HD 9000915 +61.5 = 73%; DP: Precio +96.2/Vol −8.6/Mix formato −18.1, +15% por bolsa; Pembrolizumab −60.4 fin contrato).
- **Caveats de citación (NO negociables):** +239.3 único citable como sell-in; +272.1 solo con conciliación; Mix de Hosp/GobFC como "core PiSA" con cobertura; down-trading central −197.9, piso −144.4 ("mínimo entre variantes", NUNCA −107.3 sin etiqueta pre-arista FRISO).
- **PIN no solicitado (canónico Rafael):** Farm 245→251 · Hosp 174→**71 (−59%)** · Imp 146→151 · Exp 80→**162 (+102%)** · Privado+Hosp 645→635. Retail 471→564 (+20%, EMPEORA). **Gobierno PENDIENTE** (859/869 por planchar + comparador 25).
- **Venta perdida (canónico Rafael, supersede DP):** Farm 139→171 (+24%) · Hosp 188→118 (−37%) · Imp 146→137 · Exp 75→44 · Privado+Hosp 548→470 (−14%). **Gobierno: definición única PENDIENTE** (342/443.9/463/595-600) — jamás como headline.
- **NC (Gross2Net; taxonomía real "NC comerciales y sanciones" + "Devoluciones"; NO existe "NC logísticas"):** Total NC −553.8→−625.4 (driver MP +78%) · Dev −1,024.6→−849.4 (−17.1%). GobFC Dev −729.7→−531.5 (**+$198M, la palanca real**). Conteos del transcript (428/330/108) son PIEZAS, no $M.
- **EBITDA (v18 final + split Gross2Net, cuadra a 3,879.6 = 23.5% vs 19.7%):** Retail 2,479.1 (34.4% vs 31.2%) · GobFC 482.9 (12.0% vs 9.3%) · Hosp 1,196.8 (39.2% vs 37.6%) · Servicios 321.8 (14.5% vs 8.7%, +5.8pp) · Soporte −601.1. Sub-líneas SOLO en EBITDA UN (DP 17.4 / SANEFRO 19.9 / SAFE 8.4 / SIA 23.9). Contexto: margen compañía pico 2023 30.9%, valle 2025 19.9% (el 23.5% es recuperación parcial); Gobierno UN pico 2024 1,474→624→808 (rebote). DESVIACIÓN abierta: PnL Diciembre da 1S-26 25.2% vs 23.5% [VJ].
- **Sell-in base:** PISA 16,518.5 / 93.4% / +1.5%; Retail 7,210.2 / 92.3% / +0.4% (Farm 2,958.0-88.9% / Imp 2,785.8 / Exp 1,466.4); GobFC 4,034.3 / 90.0% / −0.6%; Hosp 3,054.5 / 95.2% / +5.1%; Serv 2,219.4 / 102.1% / +4.0% (líneas 886/735/545/53 cuadran exacto). Ranking 36m verificado: oct-25 3,048.6 #1 · jun-26 2,986.9 #2 · sep-25 2,985.3 · abr-25 2,932.0 · oct-24 2,886.0 · may-26 2,843.9 #6. Pull-forward jun ~$104M [CC]. Hueco v7 (única definición): repetir venta → **+$1,596.6M** al [96] ($18,115.1M jul-dic = 98.5% del plan 2S).

## 4. Decisiones que RIGEN (todas de Rafael salvo marcadas)

1. **Rediseño v7 aprobado COMPLETO** ("de acuerdo con todo"): 22 cuerpo + 16 anexos; los 4 retos van: 15/50/35 desarmado (contenido intacto, layout no), bien/faltó a anexos como familia, junio sin lámina propia (asterisco en lámina 2, ranking en A1), puente de Servicios a anexo (titulares al cuerpo).
2. **Estilo:** IR roadshow; 1-3 gráficas/lámina; poco texto; **no abusar del número héroe** (dato memorable donde carga, láminas que respiran); redacción humana ("rival", nunca "villano"; cero plantillas IA, cero em-dash, títulos sin punto final).
3. **Hueco único = repetir venta (+$1,596.6M)**; la definición "ritmo sobre plan (~$931M)" desaparece del imprimible.
4. **PPT de revisión:** índice de momentos primero; máx 4 fotos/hoja; jamás mezclar momentos.
5. **Paso 7 = 9 carriles de Codex** (orden explícita de Rafael).
6. Kill-list Brunswick (cero corchetes con iniciales/estados internos el 27; cero "información privilegiada"; cero stage directions; $350M = silencio total); caveats de citación; % PIB salud vetado (macro = BBVA/ANTAD); Pixiba con b; FESA/COI = rival de Onco en Servicios (deck madre mantiene 3 frentes en Hospitales; el 4º reto vive solo en el anexo del canal).
7. **PENDIENTE de Rafael/Felipe:** el ASK de la lámina 22 (aprobó la arquitectura, no definió el ask). También pendientes de dato: ver §7.

## 5. Siguiente paso (lo primero que hace la próxima sesión)

1. Leer el orden de lectura (abajo). 2. Crear `storyboard_v3/` y escribir las **38 specs nuevas** (formato heredado de v2: encabezado/layout/zona por zona/mensaje/fuente/estado del dato/notas + sección final "## Instrucciones ChatGPT Images 2") siguiendo la PROPUESTA lámina por lámina y jalando cifras/redacción del banco v2 según el campo "absorbe". Sugerencia operativa: 7-8 agentes de escritura en paralelo (archivos disjuntos), Fable xhigh (si 529, Opus high declarándolo). 3. Verificación de primera mano (auditoría mecánica + cuadres + lectura de las 3-4 specs más cargadas). 4. **Paso 7:** 9 carriles Codex (~4-5 láminas c/u), task files por carril en `storyboard_v3/renders/` (patrón CODEX_TASK_*: una por una dentro del carril, PROGRESS por carril, overwrite, corchetes literales, siluetas grises); watcher por conteo/marcador mtime. 5. **Paso 8:** adaptar `build_storyboard_ppt.py` a las secciones v7 (Apertura y semestre / Retail / Gobierno FC / Hospitales / Servicios / Ruta y cierre / Anexos), ensamblar, QA visual, entregar a Rafael. 6. Deuda paralela no bloqueante: actualizar `build_storyline_v6.py`→v7 Word al canónico antes del 22.

## LEE PRIMERO, EN ESTE ORDEN (no actúes antes)

1. **Este handoff** completo.
2. `PROPUESTA_rediseno_v7_2026-07-16.md` — la biblia: qué es cada una de las 38 láminas.
3. `storyboard_v2/README_dibujante.md` — reglas transversales, caveats de citación, calibraciones.
4. `APRENDIZAJES_y_metodo.md` — método y trampas (sección 16-jul: maquinaria de puentes, carriles Codex, prompts de imagen, redacción).
5. `CONSEJO2_storyboard_veredicto_2026-07-16.md` — lo que los 5 asesores mataron: no reintroducirlo.
6. `storyboard_v2/Storyboard_v2_consolidado_2026-07-16.md` — el banco de las 35 specs con datos canónicos (consultar por lámina según "absorbe"; NO leerlo completo de entrada).
7. Según lámina: `SINTESIS_integracion_inputs_2026-07-16.md`, `inputs_nuevos/INPUT_pin_vp_privado_2026-07-16.md` y los EXTRACT correspondientes.

## 7. Riesgos / pendientes / lo que NO está hecho

- **NO está hecho:** las 38 specs v7 (paso 6) · dibujos v7 (paso 7) · PPT v7 (paso 8) · Word v7 (deuda antes del 22) · pre-read 3pp · deck real a Presidencia.
- **Pendientes de dato con dueño:** VP/PIN gobierno definición única + comparador 25 [DS/FM/Hugo/DT] · aportes al hueco por escalón y segmento [RC, antes del 22, con gate de que sumen +$1,596.6M] · mercado hospitalario sin fuente (jamás rotular IQVIA) [CC] · TAC 1 año burbujas [CC] · shares boleta con unidad/base [CC/DS] · universo del $429M/mes [Martín/CC] · comparador del −40% Baxter y nombre "AZURA" [Martín] · respuesta frente Baxter [Martín] · pull-forward ~$104M [CC] · bendición Finanzas al split y a 25.2% vs 23.5% [VJ] · KPIs e-commerce/transformación o se corta A-habilitadores [Felipe/RC] · corte OTC vs Consumo [Rafael+IC] · base "17 de 47" delegaciones (IMSS ~35 OOAD) [DS] · unificar corte Knobloch (llamada 16-jul: +4.1%/−4.5%, sin GLP-1 +2.2%) [CC] · ASK lámina 22 [Rafael/Felipe] · kill-list con árbitro el 21-jul.
- **Trampas activas:** ninguna cifra candidata como headline; universos jamás mezclados; los redondeos declarados (272.0655→"272.1"; EBITDA suma 3,879.5 visible vs 3,879.6) NO se "corrigen".

## 8. Pendiente exógeno (NO construir aguas abajo)

- **Número del 2S** [Heriberto, antes del 20]: TODO lo condicionado ($18,115.1M, 98.5%, +$1,596.6M, 53¢) se re-deriva al cerrar; el deck del 27 no puede conservar andamiaje de negociación.
- Datos de responsables listados en §7; la revisión lámina-por-lámina con el equipo ocurre tras entregar el storyboard v7 (compromiso verbal de Rafael de la llamada del 16: versión final en la noche y revisión después).

---
*Gemelo de método: `APRENDIZAJES_y_metodo.md` (sección 16-jul). Memoria persistente actualizada en `project_consejo_27jul.md`.*
