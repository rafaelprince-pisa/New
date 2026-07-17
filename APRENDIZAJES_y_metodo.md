# APRENDIZAJES y MÉTODO · Consejo 27-jul
> Archivo append-only por proyecto. Captura lo que el handoff de ESTADO no captura: por qué se construyó así, la lógica no obvia, las trampas y los caminos descartados. Un Claude de cero contexto debe poder reconstruir el razonamiento, no solo el siguiente paso.

---

## Sesión 10-jul → 16-jul-2026 (storyline v4→v5 + research externo)

### 1. Por qué el storyline tiene esta arquitectura (y no otra)

- **Bloques por segmento (entorno→1S→2S), no momentos temáticos.** Decisión de Felipe en la llamada del 6-jul, aceptada por Rafael: el entorno global como sección abría el reflejo de "¿me estás justificando?" y el "cómo" (plan) quedaba demasiado tarde en la agenda. Cada segmento se cuenta completo y autocontenido. El compromiso del número se declara al minuto uno (Edmundo: quita la ansiedad del Consejo y "compra el permiso" de profundizar) y el 1S global va ANTES de cualquier entorno.
- **El year-to-go se "suministra"** (Rodrigo): el hueco se declara en el resumen ejecutivo y cada bloque aporta su parte; la ruta consolidada solo consolida, no estrena información.
- **Dos audiencias, un deck:** consejeros (4 modelos) + Santiago (detalle brutal). La válvula es: cuerpo simple + anexos profundos. Nació del debrief con Michelle (9-jul): el problema percibido es de comunicación/transparencia, no de desempeño.
- **Sin autofelicitación:** meta contra real sin aplauso; junio SIEMPRE con su asterisco (~$104M pull-forward + 5 lunes de Hospitales). El "pin" (meta 99 → real 92 → aplauso en 95) destruye credibilidad con Santiago. Ligado: "que no parezca justificación" es el principio contra el que se prueba cada lámina, y los contrafactuales ("si el fill rate hubiera sido 90...") están PROHIBIDOS como defensa del 1S — viven solo implícitos en la base del year-to-go (resolución fina de la llamada: Rodrigo+Felipe+Víctor).
- **Los 4 villanos mapean 1:1 a los 4 segmentos** (hallazgo de diseño que hace clic con el pedido de Madero de competitividad): Retail=migración valor→volumen · Gobierno=cliente sin recursos · Hospitales=tres frentes (Mindray/Baxter/Kener) · Servicios=FESA/COI en Onco. Cada villano lleva respuesta (problema→solución); donde no la hay: "identificado, esto estamos haciendo".

### 2. La mecánica de las cascadas (lo más fácil de romper si no se entiende)

Referencia madre: `HANDOFF_storyline_consejo_27jul_2026-07-10_0725.md` §7 (cuatro universos de datos que NO se mezclan, doble conteo, convención de signo). Lo que esta sesión añadió encima:

- **Dos llaves visuales** agrupan los escalones: EFECTO VOLUMEN (mercado + venta perdida + NC logísticas + NADAL + nuevos + residual-vol) y EFECTO PRECIO+MEZCLA (precio + mezcla + NC comerciales + elasticidad). Las llaves reportan el total ROBUSTO del PVM 2-vías; los escalones son desglose narrativo, NO sumas encima. Así se cumplió el pedido de Rafael de "menú completo en cada cascada" sin doble conteo: volumen no es barra, es la llave que agrupa a sus explicadores.
- **PIN no solicitado va en panel de oportunidad, no como escalón del bridge**: solo existe el nivel 2026 (privado $635M; mejora $95M may-jun vs run-rate), no hay comparador 2025 → no puede puentear 2025→2026 sin inflar el residual. Además es palanca del 2S (Víctor). Rafael pidió el PIN "en la cascada": la solución es que APARECE en la lámina (panel lateral), no en la aritmética del bridge.
- **3-vías (precio/mezcla/volumen separados) es frágil**: el driver dominante cambia de signo con la granularidad (SKU vs molécula); Servicios a nivel SKU da "volumen +1,004" cuando las piezas cayeron −31.5% (artefacto de churn: 628 claves nuevas / 836 perdidas). Regla: 2-vías en deck; si exigen 3, molécula, direccional, y NUNCA desglosar Gobierno.
- **Residual que cuadra siempre** (contrato #5 del 6-jul): es cascada narrativa, no descomposición algebraica. Nunca forzar un escalón para que cierre; el residual absorbe y se declara.
- **Alerta viva:** la venta perdida de Gobierno NO reconcilia (DP $443.9M ene-may vs sell-in FC −$24.9M total). Es un problema de definición/universo, no de captura. NO graficar antes de alinear con DS/FM. Mientras, en la cascada de Gobierno va como "−XX [ALERTA]".

### 3. Cómo leer las revisiones de Rafael (crítico para no perder instrucciones)

- Rafael marca sus cambios **con highlights de color en el Word** y los complementa con un dictado de voz. **SIEMPRE abrir su archivo con detección de formato** (python-docx: `run.font.highlight_color`, `run.font.color.rgb`, `run.font.underline`) — el dictado solo trae ~70% de los cambios; el resto vive en las marcas. Patrón observado: **rojo** = dato por poner/verificar o elemento a QUITAR (ej. "ahorros $350M", la columna "Qué haremos"); **amarillo** = cambio estructural o texto nuevo aceptado (ej. "Desempeño por Canal", "Mindray, Baxter").
- Su dictado de voz trae **nombres corruptos por el ASR**: "Min Ray"=Mindray, "kibbe"/"aiki uvia"=IQVIA, "B Brown"=B.Braun, "cofe pris"=Cofepris, "levita/evita"=EBITDA. Interpretar por contexto y confirmar contra sus marcas escritas.
- Sus placeholders "XX" en rojo significan "pon el dato": rellenarlos cuando el dato existe en la fuente-de-verdad (venta perdida Retail +15.5, Hosp +73.7) y conservarlos con ALERTA cuando el dato NO reconcilia (venta perdida Gobierno). En la L10 dejó XX/YY/ZZ deliberados (negados, WMAPE, valor del servicio): se conservaron con el candidato en corchetes porque la unidad de "negados 640→78" está sin validar.
- Al editar, Rafael a veces PIERDE contenido sin querer (su v4 marcado perdió el escalón de mercado de la cascada PISA y la tabla sell-in de L9): reconstruir lo perdido por consistencia y FLAGEARLO explícitamente para que confirme.

### 4. Método del research externo (workflow de agentes)

- **Regla de modelos de Rafael aplicada:** Fable decide QUÉ se investiga y consolida; Opus investiga. Fable no gasta tokens investigando.
- **Lanzamiento escalonado obligatorio:** oleadas de 3 agentes, secuenciales (instrucción explícita de Rafael: lanzar todos a la vez "se traba"). Implementación: `for` sobre oleadas con `parallel()` de 3 adentro; NO un `parallel(9)`.
- **Schema estructurado por agente** con: hallazgos (título asertivo + detalle + fuente con URL + fecha + confiabilidad alta/media/baja + uso_sugerido→lámina), numeros_clave (listos para nota al pie) y **vacios** (lo no encontrado). La regla de oro impresa en cada prompt: "un vacío declarado vale más que un número fabricado" — y funcionó: los agentes declararon 40+ vacíos en lugar de inventar (ej. ventas de Kener, el −5% hospitalario, comodatos de Mindray).
- **Confidencialidad:** prohibido mencionar a PiSA o datos internos en las búsquedas; el contexto interno se da en el prompt (local) pero las queries van "desde afuera".
- **La consolidación distingue tres destinos** para cada hallazgo: (a) cifra citable con fuente pública → nota al pie de lámina; (b) corrección al storyline → acción; (c) intel interna NO citable públicamente (Nadro 5→3%, Ultra 0%, markup 300-400%, ventas Kener) → se presenta como "lo que nos dice el mercado/nuestras conversaciones", nunca con fuente inventada. Esta triple clasificación es el valor del consolidado; no perderla al bajar a láminas.
- Costo/tiempo de referencia: 9 agentes Opus effort high = ~750k tokens, ~19 min, 207 consultas, 0 errores.

### 5. Trampas técnicas conocidas (Word/python-docx en esta Mac)

- **Tablas Word necesitan DUAL WIDTHS**: `table.columns[i].width` (tblGrid) ADEMÁS de `cell.width` por celda. Si solo pones cell widths, LibreOffice iguala las columnas (Word a veces lo perdona). Bug encontrado y corregido en v4.
- **El gate del design system marca "→" como emoji prohibido** en entregables: usar comas o "·" en texto de .docx.
- `extract-text`/`pandoc` NO están instalados: leer .docx con python-docx. LibreOffice existe pero `soffice` no está en PATH: usar `/Applications/LibreOffice.app/Contents/MacOS/soffice` directo. `pdftoppm` no existe: rasterizar PDF con PyMuPDF (`fitz`, instalado).
- QA estándar de un entregable Word aquí: (1) regenerar desde script; (2) gate `python3 ../design-system-pisa/generators/quality_gates.py <docx> --strict --warn` (0/0); (3) checks de números clave por extracción de texto; (4) render PDF→PNG y revisión visual de tablas.
- Ortografía: escribir SIEMPRE con acentos en el script (un despiste generó una v4 completa sin acentos que hubo que rehacer).

### 6. Caminos descartados (no re-proponer)

- **Bien/faltó/haremos a 3 columnas** → Rafael lo partió: la tabla queda a 2 columnas (bien/faltó) y el "haremos" se muda a la lámina de plan 2S de cada bloque, que es lámina por sí sola.
- **$350M de ahorros en la ruta consolidada** → fuera ("no es el lugar"). Solo se registra su exclusión.
- **Kener como EL villano de Hospitales** → re-dimensionado; el bloque es "amenaza en tres frentes" con Mindray (infusión) y Baxter/Vantive (soluciones) como los grandes.
- **Margen/utilidad fuera del cuerpo (contrato #4 del 6-jul)** → enmendado DOS veces por Rafael: 1ª margen en anexos (10-jul AM), 2ª EBITDA $ y % + % del total EN la tablita del cuerpo (10-jul PM). No "corregir" de vuelta.
- **"Mercado −3% en valor sin GLP-1"** → no se sostiene con Knobloch (da ~plano); usar mercado foco PISA/AMSA −3.4% YTD o conseguir el corte IQVIA.
- **Semáforo/boleta de calificaciones bueno-regular-malo** → sustituido por la vista por segmento/canal (decisión del 6-jul).
- **Macrotendencias de largo plazo como sección** → solo "deslizadas" en una línea de conclusiones (Edmundo: la junta es táctica, ya tiene número).
- **Cascadas como párrafo corrido** → siempre en bullets (formato de Rafael, para poderse leer).
- **Vendors públicos (Grand View/Mordor) como contraste del GLP-1 de Knobloch** → universos incomparables; no mezclar.

### 7. Lecciones de esta sesión

- **El gate de índice-antes-de-storyline funcionó**: Rafael pidió acordar índice primero; el v4 salió alineado y su revisión fue quirúrgica, no estructural. Repetir el patrón para el storyboard/deck: esqueleto → OK → construcción.
- **Verificar el dato en la fuente cuando el dueño duda** ("¿2 y 5 o 3 y 6?"): recalcular el ranking desde 04_Meses tomó minutos y cerró la discusión con un dato fino extra (#2 por $1.6M) que además blinda la lámina.
- **El research externo cambia láminas, no solo las decora**: la corrección Baxter→Vantive reescribe un frente completo del bloque Hospitales. Investigar ANTES de imprimir evita que un consejero corrija en vivo.
- **Fechas del sistema vs fechas del trabajo**: la sesión abarcó 10→16 de julio; los nombres de archivo quedaron con fecha 10-jul (convención del día en que se abrió el frente). El handoff debe auditar `ls` (fechas reales de disco), no la memoria de la conversación.

---

## Sesión 16-jul-2026, día completo (v6 + storyboard v2/v3 + 2 consejos + puentes canónicos + rediseño v7)

### 1. La maquinaria de puentes canónica (lo más fácil de romper)

- **Una sola fuente para toda cascada:** la matriz 8 componentes × 4 segmentos de `Downtrading_PiSA_Consolidado_FINAL_2026-07-16.xlsx` (verificada al peso por 2 agentes con recálculo LibreOffice sobre COPIAS; control 0.0000). Los INSIGHTS_*.md de la carpeta v2 de PVM son la lectura curada de Rafael.
- **Doble vista y conciliación de 3 niveles, SIEMPRE:** reclasificada (+272.1) − reclasif nov-dic de lanzamientos (−31.7) = con MATNR (+240.3) − filas sin MATNR (−1.0) = **cubo/sell-in oficial (+239.3)**. Regla de cita: solo +239.3 es "sell-in"; cualquier vista reclasificada viaja CON su conciliación visible. Por segmento: Privado 58.7→31.3→31.8; Hosp 153.8→149.4→147.9; GobFC −24.9 plano; GobServ +84.5 plano.
- **Mix = "core PiSA" con cobertura declarada** (96.0/65.0/78.9%; GobServ no admite P/V/M: 45.6% sin unidad → puente POR VALOR con anexo DP por bolsa). C7 = reclasificación de distribuidos-no-manufacturados a Terceros vía terceros_overrides.csv, no mueve la Δ.
- **Rango del down-trading:** central −197.9; piso vigente −144.4 ("mínimo entre variantes", sensibilidad composicional POST-arista FRISO). El −107.3 que circuló es PRE-arista (spec §7.4): no citarlo sin esa etiqueta.
- **Trampa de taxonomías paralelas:** el 2-vías clásico (vol −830.7 / precio+mezcla +1,070) y la matriz (Volumen +281.8 intra-molécula) NO son comparables término a término — "volumen" significa cosas distintas. En láminas nunca juntos; el 2-vías queda como validación en anexo de método.
- **NC:** la taxonomía real del Gross2Net es "NC comerciales y sanciones" + "Devoluciones"; NO existe línea "NC logísticas" (el −$100M de Rafael no es aislable ahí). Los 428/330/108 del transcript de gobierno son CONTEOS/piezas, no $M.
- **EBITDA:** bloque = v18 final + split Gross2Net (cuadra al peso, ±3.6M de Nuevos Productos declarado); sub-líneas SOLO en EBITDA UN. El margen es historia de REBOTE (compañía: 30.9% en 2023 → 19.9% en 2025 → 23.5% 1S26; Gobierno UN: 1,474 en 2024 → 624 → 808): tener la línea de manejo antes de mostrar series largas. PnL Diciembre trae 1S-26 en 25.2% (≠23.5%): versión/definición por reconciliar [VJ], no mezclar.

### 2. Cómo se corrió el día (método de orquestación que funcionó)

- **Ciclo:** extracción exhaustiva por agentes (un archivo = un agente Opus, EXTRACT_*.md durable) → síntesis/decisión del orquestador → build → consejo adversarial → aplicar → redibujar. Nunca construir sin extraer primero; nunca entregar sin consejo.
- **Carriles de Codex:** disjuntos por archivos, task file por carril (CODEX_TASK_*.md) con: una-por-una DENTRO del carril, PROGRESS_<carril>.md escrito inmediatamente tras cada lámina, regla skip-si-existe (tanda nueva) u OVERWRITE explícito (redibujo), "DONE <carril>: n de N" al final. El rescue-forwarder NO devuelve el resultado: se vigila el disco con watcher en background (conteo de PNGs o mtime > marcador). Paralelizar carriles es seguro porque los archivos no colisionan; lo que NO se hace es re-delegar el mismo archivo.
- **Prompts de imagen que funcionan (ChatGPT Images 2 vía Codex):** un bloque autocontenido por lámina con TODO el texto verbatim entre comillas y acentos, layout con proporciones, hex exactos, proporciones RELATIVAS de barras ("baja el doble que"), corchetes placeholder literales en gris, prohibiciones explícitas (carácter →, emojis, rótulos de caja, border-left, verde celebratorio). Falla conocida: typos de diacríticos en render ("deścisión") → QA visual siempre; texto denso (tablas 8 filas) sale legible pero no tipográficamente exacto: suficiente para storyboard, no para deck final.
- **529 de Fable:** reintentos con espera creciente (3-8 min); si persiste, fallback a Opus DECLARADO a Rafael (nunca downgrade silencioso). SendMessage a un agente caído lo resume con su lectura intacta.
- **Verificar los replaces:** un replace case-sensitive "exitoso" dejó vivo un "PIXIVA" en mayúsculas y una nota sin aplicar; desde entonces todo batch de ediciones imprime misses y se re-verifica con grep. Nunca declarar "resuelto" sin releer.
- **Dos agentes jamás editan el mismo archivo**; el orquestador particiona por archivos y hace él mismo los archivos compartidos (v6, README).

### 3. Los dos consejos y el rediseño (método de decisión)

- **Regla de oro: la convergencia entre revisores independientes de cero contexto es la señal más fuerte.** Consejo 2 (5 lentes sobre los DIBUJOS, no las specs) encontró lo que ningún review de specs vio: aritmética entre láminas (hueco con 2 definiciones; VP que no cruza 901.9 vs 463; $429M sin universo), cocina impresa y densidad. Revisar el artefacto RENDERIZADO, no solo la fuente.
- **Rediseño sin recency bias:** 3 arquitectos sesgados (IR banker / operador que presenta / consejero que diseña desde las preguntas de la mesa), corpus completo, cero contexto entre sí → los tres convergieron en cuerpo de 22 y los mismos movimientos → esa convergencia ES la propuesta; el orquestador solo adjudicó divergencias (posición de la lámina de mercado, col-3 consolidada en cuerpo, tablita sin columna de mercado) y escribió su auto-reto ANTES de presentar. Rafael aprobó completo a la primera.
- **Redacción humana (mandato):** "rival" no "villano"; cero "no es X, es Y" en serie; cero em-dash; títulos sin punto final; el múltiplo entre universos ("6 veces menos") se imprime como par y se dice a voz; datos memorables donde cargan la historia, no en cada lámina (calibración explícita de Rafael contra el "número héroe" como tic).
- **Brunswick rules (kill-list):** las stage directions impresas ("sin aplauso", "no son excusa") convierten disciplina en coaching visible; "información privilegiada" es término legal; las exclusiones ($350M) se ejecutan con SILENCIO, no con disclaimer; el andamiaje de negociación (nombres, fechas internas) jamás llega a la audiencia final.

### 4. Caminos descartados hoy (no re-proponer)

- Vista Consejo 5 líneas por canal (superseded por matriz v4) · "+9.2% INEFAM 2025" como comparador del puente (ventana/universo) · "mercado −3% sin GLP-1" (muerto dos veces) · % PIB salud (vetado: trillado; macro = BBVA/ANTAD) · columna "Crec. mercado" en la tablita con el −5% sin fuente · rotular el −5% hospitalario como IQVIA (IQVIA abril NO cubre hospital) · hero-por-lámina como formato fijo · L33 habilitadores como lámina (2/3 vacía) · bien/faltó como láminas de cuerpo (v7: anexos en familia) · dato ganador de junio como lámina propia (neto de adelanto cae a ~#5-6) · convención 15/50/35 como layout de cuerpo (v7: col-2 protagonista, col-3 consolidada una vez) · forzar puente de 5 conceptos en GobServicios (churn/unidades: va por valor).

### 5. Lecciones

- **El dato llega cuando llega: diseñar para placeholders honestos** (corchete con responsable, siluetas grises, "forma comprometida") permitió entregar 3 storyboards el mismo día sin fingir números — y el consejo lo premió como transparencia diseñada.
- **La cifra curada del dueño supersede a la fuente intermedia** (tablas PIN/VP de Rafael vs niveles DP), pero los deltas se flagean, no se esconden.
- **Auditar la aritmética CRUZADA entre láminas** (no solo dentro de cada una) es lo que salva frente a una familia que recalcula: hueco, VP total vs partes, 429×meses vs sell-in.
- **El PPT de revisión se organiza como el dueño piensa** (por momentos, índice primero) — la estructura de revisión es parte del producto.
