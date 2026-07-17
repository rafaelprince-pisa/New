# Storyboard v2 · Consejo 27-jul · Las 35 láminas (rev. integración 16-jul noche)
**Puentes canónicos integrados + tablas PIN/VP/NC + split EBITDA + capa A del consejo 2 + kill-list. Fuente canónica: los SB_L##.md.**

---

# README para el dibujante (Codex Images) · Storyboard Consejo 27-jul
**Qué es esta carpeta:** una spec autocontenida por lámina (`SB_L##.md`). Cada spec es ejecutable tal cual: encabezado, layout por zonas con proporciones, contenido completo de cada zona, mensaje, fuente al pie, estado del dato y notas. **La spec manda.** Si algo de la spec parece contradictorio o infactible, se detiene y se flagea al orquestador; el dibujante NO resuelve conflictos de contenido por su cuenta.

## Reglas transversales (aplican a las 20 láminas, además de lo que diga cada spec)

1. **Formato:** PowerPoint 16:9 (13.333 x 7.5 in), márgenes 0.5 in. Tipografía Calibri Light (bold puntual = Calibri). Tabular figures en TODA cifra (Format, Font, OpenType, Tabular figures). Paleta = tokens del sistema PiSA (`design-system-pisa/tokens.json`): navy #0F2845 / #0F4C81, grises #1A2332-#FAFBFC, semáforo solo en deltas, gold #C5A55A.
2. **El carácter "→" JAMÁS se imprime** en ningún cuadro de texto (el gate del design system lo rechaza). Transiciones se escriben "de X a Y" o con "·". Flechas solo como shapes dibujados (conectores de línea con punta).
3. **Cero emojis**, incluidos semáforos heredados de decks fuente (🔴🟢 y equivalentes NO viajan).
4. **Gold: máximo 1 elemento por lámina.** Cada spec nombra cuál es (o declara que no hay). No agregar golds.
5. **Placeholders y chips se dibujan LITERALES y visibles:** todo texto entre corchetes con responsable — "[dato: CC]", "[respuesta por cerrar: Martín]", "[96]" — se imprime tal cual, en gris neutro, sin ámbar/rojo ni iconos. Prohibido rellenarlos, estimarlos o borrarlos.
6. **Los universos de datos no se mezclan en una misma gráfica** (sell-in / sell-out Knobloch / IQVIA retail / pedidos gobierno / P&L Finanzas / intel de canal). Cada panel lleva su eyebrow de universo si la spec lo pide; prohibido unificar paneles o conectarlos con flechas.
7. **Deck de Consejo sobrio:** títulos asertivos sin punto final; sin caja de insight; prohibido rotular bloques con "INSIGHT", "SO WHAT", "RESPUESTA" u otra etiqueta de caja; sin border-left; sin gradientes; sin sombras infladas; sin logos de competidores ni imágenes de stock.
8. **Sin aplauso:** nada de verde celebratorio en cifras de desempeño propias; el semáforo solo aparece donde la spec lo pide explícitamente en deltas cuantitativos.
9. **Gráficas:** barras arrancan en cero (si un eje se trunca, la spec lo pide y se marca el corte); espacio entre barras >= 50% del ancho; máximo 4 líneas por gráfica; data labels directos antes que leyendas; sin gridlines o en #E5E9EE.
10. **Pie de lámina:** siempre la línea de fuente que trae la spec (9 pt, #8A95A8/gray-500, itálica) + "PiSA Confidencial | {número de lámina}".
11. **Numeración:** el número de lámina del deck es el del nombre del archivo (SB_L22 = lámina 22 del storyline v6). Los huecos (láminas 2, 4, 6-8, 10, 12-14, 17-19, 23, 28, 31) llegan en la segunda tanda; no renumerar.

## Estado
- 20 specs listas (láminas estables). Pendientes de la segunda tanda: puentes (L8/13/18/23/28), tablita (L6), boleta (L7), L2, L4, L10, L12, L14, L17, L19, L31.
- Formato de salida acordado con Rafael: cada lámina dibujada se pega 4-por-hoja en un PPT de storyboard para revisión.

## Caveats de citación de los puentes (Rafael 16-jul, NO negociables en Consejo)
- El sell-in oficial es **+$239.3M**; la Δ reclasificada (+$272.1M) solo se muestra CON su conciliación de tres niveles (272.1 − 31.7 reclasif − 1.0 sin MATNR = 239.3).
- El Mix de Hospitales y Gob FC se cita como **"core PiSA"** con su cobertura (65.0% / 78.9%), nunca como el segmento entero.
- Down-trading de Privado: cifra central **−$197.9M**; si piden rango, el piso del workbook vigente es **−$144.4M** ("mínimo entre variantes", sensibilidad composicional, no intervalo de confianza). El −$107.3M es pre-arista FRISO (spec §7.4): no citarlo sin esa etiqueta.
- Los conteos de NC del transcript de gobierno (428/330/108) son PIEZAS/conteos, no $M: no mezclarlos con el Gross2Net.
- La taxonomía real de NC (Gross2Net) es "NC comerciales y sanciones" + "Devoluciones"; la línea "NC logísticas" no existe como corte.

## Decisiones provisionales del orquestador (16-jul; Rafael puede revertirlas)
1. Títulos asertivos propuestos en las bien/faltó (L15/L24/L29): QUEDAN (assertion-evidence).
2. L11 se mantiene como UNA lámina; el panel D solo se muda a una 11-bis si el render no respira.
3. L22: "el cliente también cambia" va como franja de una línea encima del pie (ya en la spec).
4. L25: el descubierto de ~$10M/mes SÍ se muestra explícito (transparencia ante Santiago).
5. L30: barras de reducción sin rojo semáforo (achicarse es decisión propia, no alarma).
6. L33: e-commerce y transformación cualitativas con chip "[KPI por asignar: Felipe/RC]".
7. Pixiba (con b) en todo el deck — decisión de Rafael 16-jul, no provisional.
8. L3: ranking de meses completo y verificado contra la hoja 04_Meses (ya sin [IC]).
9. El % del PIB en salud NO se usa en ninguna lámina (trillado, decisión Rafael 16-jul); los hechos de gobierno son consolidada anulada + adeudos, y el mensaje macro de consumo lo cargan BBVA y ANTAD.


---

# Lamina 1 · El compromiso del año es [96]: vamos a llegar
- **Momento:** M0 · Apertura y resumen ejecutivo
- **Encabezado:** El compromiso del año es [96]: vamos a llegar
- **So-what subtitle:** Esta sesión explica el primer semestre, el entorno segmento por segmento y las iniciativas para lograrlo
- **Layout:** Lámina tipográfica, sin gráficas ni tablas. Cuatro bandas horizontales: banda de título 15% + compromiso central (KPI hero) 45% + dos bloques de objetivos 30% (2 columnas 50/50 con gutter 0.15in) + footer 10%. Márgenes 0.5in; todo el contenido centrado en el eje vertical de la lámina.

## Zona por zona

### Zona A — Banda de título (15% superior)
- Tipo: título + subtítulo estándar.
- Título: "El compromiso del año es [96]: vamos a llegar" — Calibri Light 32 pt, `#0F2845` (primary-900). El "[96]" dentro del título va en Calibri bold (énfasis puntual permitido), corchetes incluidos.
- Subtítulo so-what: "Esta sesión explica el primer semestre, el entorno segmento por segmento y las iniciativas para lograrlo" — Calibri Light 14 pt italic, `#44546A`.
- Separador opcional: línea 0.5 pt `#E5E9EE` bajo el subtítulo.

### Zona B — Compromiso central, KPI hero (45%)
- Tipo: KPI hero único, centrado horizontalmente.
- KPI label (arriba del valor): "COMPROMISO DEL AÑO" — Calibri Light 10.5 pt UPPERCASE con tracking, `#5A6679`.
- Valor: "[96]" — Calibri bold 54 pt, `#0F2845`, tabular figures. LOS CORCHETES SE DIBUJAN: son la marca visible de que el número está pendiente. NO sustituir por ningún número.
- Línea de unidad bajo el valor: "% de cumplimiento del plan anual" — Calibri Light 12 pt, `#5A6679`. Esta es la ÚNICA lámina del deck que declara la unidad del [96]; las demás usan "[96]" a secas.
- SIN nota de negociación en el imprimible: la nota "[número del 2S en negociación: Heriberto / Dirección, cierre antes del 20-jul]" NO se dibuja (vive como nota interna en "Notas para el dibujante"). "Vamos a llegar" aparece UNA sola vez en la lámina (en el título); no repetirlo bajo el hero.

### Zona C — Los dos objetivos (30%; 2 columnas 50/50)
- Tipo: dos bloques tipográficos gemelos.
- Eyebrow común centrado arriba de los bloques: "Doble objetivo fijado por la Dirección General" — Calibri Light 10.5 pt UPPERCASE, `#5A6679`.
- Bloque izquierdo: fondo `#FAFBFC` (gray-050), top border 1.5 pt `#0F4C81` (primary-700), border-radius 4-8 px, padding 0.20in. Numeral "1" Calibri bold 20 pt `#0F4C81` + texto "Explicar el desempeño comercial del primer semestre" Calibri Light 14 pt `#3D4A5F`.
- Bloque derecho: mismo estilo. Numeral "2" + texto "Presentar cómo vamos a llegar al número del segundo semestre".
- PROHIBIDO rotular los bloques con etiquetas tipo "OBJETIVO" como header; el numeral y la frase bastan.

### Zona D — Footer (10%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie (ver abajo) + "PiSA Confidencial | 1" a la derecha, Calibri Light 9 pt `#8A95A8`.

- **Mensaje que manda la lamina:** Al minuto uno nadie está adivinando cuándo llegamos: el compromiso del año se pone sobre la mesa antes que cualquier explicación, y la sesión entera existe para sostenerlo.
- **Fuente (pie de lamina):** Fuente: objetivo anual fijado por Dirección General; número del 2S en negociación con Dirección (cierre previsto antes del 20-jul-26)
- **Estado del dato:**
  - Zona B ([96]): placeholder [Heriberto / Dirección — número del 2S, exógeno; NO construir nada aguas abajo de él]
  - Zonas A, C: en mano (texto del storyline v6)
  - KILL-LIST 16-jul aplicada: hero rotulado "COMPROMISO DEL AÑO" (fuera "OBJETIVO ANUAL COMPROMETIDO"); la nota de negociación (Heriberto / cierre antes del 20) sale del imprimible a nota interna; unidad del [96] declarada bajo el hero SOLO en esta lámina; "vamos a llegar" una sola vez.
- **Notas para el dibujante:**
  - NOTA INTERNA (no imprimible): el número del 2S está en negociación (Heriberto / Dirección, cierre antes del 20-jul). Esta información NO se dibuja en la lámina; el pie de fuente ya la carga sin nombres.
  - Todo texto entre corchetes con responsable es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris en el borrador y se elimina antes de la sesión; ninguno llega a la lámina final.
  - NO sustituir "[96]" por 96, 96% ni ningún otro número: es placeholder declarado de un dato exógeno que llega después. Los corchetes se imprimen tal cual en el borrador.
  - Cero gold en esta lámina. Cuando el número real sustituya al placeholder, se dibuja en navy `#0F2845`, no en gold: apertura sobria, sin festejo.
  - Sin caja de insight, sin bullets, sin iconos, sin imágenes. El poder de la lámina es el espacio en blanco: no rellenar.
  - Universo: n/a (lámina de compromiso, sin datos de mercado).
  - No usar punto final en el título. Sin emojis. No gradientes, no border-left.

- AJUSTE POST-CONSEJO (16-jul): [96] se rotula como compromiso ANUAL; la exigencia del 2S (98.5% de su plan) vive en L4. No rotular [96] como "objetivo del 2S" en ninguna zona.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin ilustraciones. Tipografía sans-serif limpia y ligera (tipo Calibri Light); usa negrita solo donde lo indique. Es una lámina puramente tipográfica, sin gráficas ni tablas. El poder de la lámina es el espacio en blanco: no rellenar. Todo el contenido centrado en el eje vertical de la diapositiva. Cuatro bandas horizontales apiladas.

BANDA 1 (15% superior, título): en dos partes. Título grande en color navy oscuro #0F2845: "El compromiso del año es [96]: vamos a llegar" — el fragmento "[96]" (con corchetes) en negrita, el resto en peso ligero. Debajo, subtítulo en itálica gris azulado #44546A, más chico: "Esta sesión explica el primer semestre, el entorno segmento por segmento y las iniciativas para lograrlo". Una línea divisoria delgada gris #E5E9EE debajo del subtítulo.

BANDA 2 (45%, KPI hero centrado): arriba, una etiqueta pequeña en MAYÚSCULAS con espaciado de letras, gris #5A6679: "COMPROMISO DEL AÑO". Debajo, un número enorme en negrita navy #0F2845: "[96]" — dibuja los corchetes literalmente, NO los reemplaces por ningún número. Debajo del valor, una línea de unidad en gris #5A6679 tamaño medio-chico: "% de cumplimiento del plan anual". Nada más en esta banda: sin notas de negociación, sin nombres, sin repetir "vamos a llegar".

BANDA 3 (30%, dos objetivos en 2 columnas iguales lado a lado): arriba, centrada, una etiqueta en MAYÚSCULAS gris #5A6679: "Doble objetivo fijado por la Dirección General". Debajo, dos tarjetas gemelas con fondo gris muy claro #FAFBFC, esquinas redondeadas y una línea superior delgada azul #0F4C81 (borde solo arriba, nunca a la izquierda). Tarjeta izquierda: un numeral grande en negrita azul #0F4C81 "1" junto al texto en gris #3D4A5F "Explicar el desempeño comercial del primer semestre". Tarjeta derecha: numeral "2" junto al texto "Presentar cómo vamos a llegar al número del segundo semestre". No pongas encabezados tipo "OBJETIVO" en las tarjetas.

BANDA 4 (10% inferior, pie): línea divisoria gris #E5E9EE y debajo, en gris claro #8A95A8 tamaño chico, a la izquierda: "Fuente: objetivo anual fijado por Dirección General; número del 2S en negociación con Dirección (cierre previsto antes del 20-jul-26)"; alineado a la derecha: "PiSA Confidencial | 1".

Reglas estrictas: ningún carácter de flecha en el texto; sin emojis; sin rótulos de caja tipo INSIGHT o SO WHAT; sin borde izquierdo en ningún bloque; nada en dorado ni en verde; todo el texto en español con acentos correctos; el título sin punto final; números con figuras tabulares.
```


---

# Lámina 2 · PiSA defiende el valor: cae seis veces menos donde el mercado se hunde y crece en Hospitales y Servicios
- **Momento:** M0 · Apertura y resumen ejecutivo
- **Encabezado:** PiSA defiende el valor: cae seis veces menos donde el mercado se hunde y crece en Hospitales y Servicios
  (El "seis veces" va SOLO como texto plano dentro del título; PROHIBIDO imprimirlo como múltiplo aritmético destacado — sin "6x", sin número grande. El par que lo sustenta, −0.6% vs −3.8%, se imprime en la tabla, fila Gobierno FC.)
- **So-what subtitle:** Cerramos el 1S en 93.4% del plan (+$239.3M, +1.5%) con las piezas cayendo −5.1%; el crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core (mix −$297.0M)
- **Layout:** Banda de título 17% + cuerpo 67% (tabla comparativa izquierda ~62% · riel de dos notas derecha ~36%, gutter 0.15in) + franja de una línea + línea de leyenda de placeholders + footer 12%. Márgenes 0.5in; 13.333 × 7.5 in.

## Zona por zona

### Zona A — Banda de título (17%)
- Título: Calibri Light 28-32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.
- Separador 0.5 pt `#E5E9EE` de margen a margen.

### Zona B — Tabla comparativa mercado vs PiSA (izquierda, ~7.4 in de ancho)
- Micro-título de zona: "Dónde crece el mercado y dónde crece PiSA: una fila comparable, tres proxys" — Calibri bold 12 pt `#0F2845` (texto plano, no etiqueta de caja).
- Tabla en DOS bloques visualmente separados: bloque "COMPARABLE · MISMO UNIVERSO" (solo la fila Retail) y bloque "PROXY · UNIVERSOS DISTINTOS" (Gobierno FC, Hospitales, Servicios). Cada bloque abre con una fila-rótulo de grupo en Calibri Light 8.5 pt UPPERCASE `#5A6679`, fondo `#F0F3F7`; entre bloques, border 1.5 pt `#0F4C81` (separación horizontal, nunca border-left).
- Header: fondo `#0F2845`, texto blanco Calibri bold 11 pt. Body: Calibri Light 11 pt `#3D4A5F`, filas alternas blanco / `#F0F3F7`, border inferior por fila 1 px `#E5E9EE`, sin líneas verticales, border externo 0.5 pt `#C5CDD9`. Tabular figures en toda celda numérica; signo menos tipográfico "−", "+" explícito.
- Columnas (4): "Segmento" (izquierda) | "Mercado · valor" (derecha) | "PiSA · valor" (derecha) | "Base de comparación" (izquierda).

| Segmento | Mercado · valor | PiSA · valor | Base de comparación |
|---|---:|---:|---|
| *COMPARABLE · MISMO UNIVERSO* | | | |
| Retail (mercado foco) | −4.2% | −0.1% | Mismo universo: KB Entry Market MAT may-26 (mercado y PiSA/AMSA en el mismo corte) |
| *PROXY · UNIVERSOS DISTINTOS* | | | |
| Gobierno FC | −3.8% | −0.6% | Proxy: INEFAM genéricos ene-may vs sell-in PiSA |
| Hospitales | [−5% validar: CC] | +5.1% | Proxy: IQVIA (por validar) vs sell-in PiSA |
| Servicios | n/a | +4.0% | Proxy: modelos propios vs sell-in PiSA |

- Nota pegada al −0.1% (dentro de la celda, segunda línea, Calibri Light 8.5 pt `#5A6679`): "en sell-in Retail: +0.4%".
- Nota bajo la fila Retail (una línea, Calibri Light 8.5 pt `#5A6679`, indentada bajo el bloque comparable): "Unidades del mismo universo: mercado −7.9% · PiSA −9.4%." (Las columnas de unidades salieron de la tabla: estaban semivacías.)
- Nota al pie de la tabla (Calibri Light 8.5 pt `#8A95A8`): "Corte Knobloch por unificar [CC]: la llamada del 16-jul reporta mercado +4.1% en dinero / −4.5% en unidades y +2.2% sin GLP-1, corte distinto al Entry Market impreso; no sustituir sin unificación de CC."
- Semáforo (solo en deltas cuantitativos):
  - "Mercado · valor": −4.2% y −3.8% en `#C00000`. La celda "[−5% validar: CC]" completa en gris placeholder `#8A95A8` (no se colorea). "n/a" en `#8A95A8`.
  - "PiSA · valor": −0.6% en `#C00000`; +5.1% y +4.0% en NEUTRO `#1A2332` (sin verde: nada de verde celebratorio en cifras propias); el −0.1% de Retail es la cifra pivotal (ver gold).
- Cifra pivotal en GOLD: el "−0.1%" de la fila Retail, columna "PiSA · valor", Calibri bold `#C5A55A`. Es la prueba de mismo universo de que defendemos valor donde el mercado cae −4.2%. ÚNICO elemento gold de la lámina.

### Zona C — Riel de dos notas (derecha, ~4.4 in de ancho). Dos bloques apilados.
Cada bloque: micro-título Calibri bold 11.5 pt `#0F2845` (texto plano) + cuerpo Calibri Light 10.5 pt `#3D4A5F`. Separación entre bloques con top border 1 pt `#0F4C81` (permitido; prohibido border-left).
1. **El mercado sólo crece por GLP-1 y precio** — "Privado sin GLP-1: +1.4% en valor y −4.8% en unidades (KB MAT may-26). La demanda física cae."
2. **Consumo débil, confirmado por terceros** — "BBVA −4.9% anual a jun-26 (quinta caída consecutiva); ANTAD +0.8% nominal, es decir, caída real."
- (La nota 1 anterior, "El +1.5% es todo precio y mezcla", SALE: duplicaba el subtítulo y su claim choca con el puente canónico; ver Estado del dato.)

### Zona D — Franja de una línea (sobre la leyenda)
- Calibri Light 11 pt `#1A2332`: "La cadena de suministro se estabilizó; el reto se movió a acelerar la venta."

### Zona D2 — Línea de leyenda de placeholders (sobre el footer)
- Calibri Light 8 pt `#8A95A8`: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

### Zona E — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 2".

## Mensaje que manda la lámina
El 1S cerró en 93.4% del plan (+$239.3M, +1.5% sell-in). En la única comparación de mismo universo, PiSA defiende el valor: −0.1% vs −4.2% del mercado foco (Knobloch Entry Market). En los proxys, cae seis veces menos que el mercado de gobierno (−0.6% vs −3.8% INEFAM) y crece contra corriente en Hospitales (+5.1%) y Servicios (+4.0%). Ese crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core (mix −$297.0M, core prácticamente plano); el consumo débil lo confirman BBVA y ANTAD.

## Fuente (pie de lámina)
Fuente: Sell-In PiSA cierre jun-26 (1S, cubo; +$239.3M = 16,279.2 a 16,518.5); matriz consolidada Downtrading FINAL 16-jul (mix, core); Knobloch Entry Market MAT may-26 (mercado foco PiSA/AMSA, sin electrolitos, fórmulas infantiles ni GLP-1); INEFAM ene-may-26; IQVIA (Hospitales, por validar); BBVA Research y ANTAD jun-26

## Estado del dato
- +$239.3M / +1.5% sell-in oficial (16,279.2 a 16,518.5): **en mano** (matriz consolidada Downtrading FINAL 16-jul). CAVEAT de citación: +239.3 es lo ÚNICO citable como sell-in; la Δ reclasificada +272.1 solo con su conciliación de tres niveles y NO se usa en esta lámina.
- Mix −$297.0M y core prácticamente plano (PVM core PiSA neto +$51.7M): **en mano** (matriz 16-jul).
- **SUPERSEDIDO por el canónico:** el claim v6 "el crecimiento es enteramente precio y mezcla" y el "Volumen −$831M" chocan con la matriz canónica (Volumen reclasificado +$281.8M, Precio +$66.9M, Mix −$297.0M): gana el canónico. El −$831M ya NO se cita en ninguna zona. El −5.1% de piezas (unidades físicas totales) sigue vigente: no lo contradice la matriz (el efecto Volumen en $ es positivo por composición Gob FC).
- Retail (Entry Market −4.2% / −7.9%; PiSA −0.1% / −9.4%): **en mano** (deck canal Farmacias L1/L9, KB MAT may-26; verificado en el extract).
- Nota "en sell-in Retail: +0.4%": **en mano** (conciliación FLP del cubo, matriz 16-jul). Cortes distintos: no sustituye al −0.1% del Entry Market ni al revés.
- Corte Knobloch 16-jul (mercado +4.1% dinero / −4.5% unidades, sin GLP-1 +2.2%): **FLAG por unificar [CC]** — universo distinto al Entry Market impreso; se imprime solo como nota al pie, jamás sustituye las celdas sin el OK de CC.
- Gobierno mercado −3.8% (INEFAM) vs PiSA −0.6%: **en mano** (v6; INEFAM ene-may).
- Hospitales mercado **[−5% validar: CC]**: **placeholder declarado** (la vista IQVIA del mercado hospitalario venía vacía; sigue abierta). PiSA +5.1% en mano.
- Servicios: mercado **n/a** (modelos propios, se declara); PiSA +4.0% en mano.
- +1.4% sin GLP-1, BBVA −4.9%, ANTAD +0.8%: **en mano** (v6).

## Notas para el dibujante
- Universos NO se mezclan en una gráfica: por eso esta comparativa va como TABLA con columna "Base de comparación" por fila, no como barras apiladas de un solo eje.
- La fila Retail es la ÚNICA apples-to-apples (mercado y PiSA en el mismo corte Knobloch): por eso vive en su propio bloque "COMPARABLE" separado de los tres proxys. La separación es visual (fila-rótulo de grupo + border 1.5 pt entre bloques), no otra tabla.
- El "seis veces menos" del título mapea al par Gobierno FC (−0.6% vs −3.8%), NO al par Retail (−0.1% vs −4.2%). No imprimir el múltiplo como cifra ni destacarlo gráficamente: vive solo como palabras del título.
- El "−0.1%" de PiSA en Retail (Entry Market) NO es el +0.4% de sell-in de Retail: son cortes distintos. La celda imprime el −0.1% con su nota pegada "en sell-in Retail: +0.4%". No sustituir uno por otro.
- Sin verde en ninguna celda: +5.1% y +4.0% van en neutro `#1A2332` (nada de verde celebratorio en cifras propias). El rojo solo en deltas negativos cuantitativos.
- Placeholder "[−5% validar: CC]" se dibuja literal, gris neutro `#8A95A8`, sin ámbar ni rojo ni icono. No rellenar. Todos los corchetes de esta lámina son PLACEHOLDER INTERNO (kill antes del 27): la línea de leyenda de la Zona D2 lo declara una sola vez.
- El símbolo $ no se repite en las notas del riel salvo la primera mención por cifra; los porcentajes llevan su signo.
- Sin caja de insight; los micro-títulos del riel son texto plano navy, sin fondo ni marco; sin border-left (la separación entre notas es top border).
- Cero círculos de semáforo o iconos de estatus; el color vive solo en los deltas de la tabla y el gold solo en el −0.1%. Cero em-dash y cero carácter de flecha en texto imprimible.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares alineados a la derecha; usa el signo menos tipográfico "−", no un guion, y el signo "+" explícito en positivos.

BANDA DE TÍTULO (arriba, ~17%, ancho completo): título grande navy #0F2845 en peso ligero, hasta dos líneas: "PiSA defiende el valor: cae seis veces menos donde el mercado se hunde y crece en Hospitales y Servicios". El "seis veces" es SOLO texto del título: no dibujar ningún "6x" ni múltiplo como número destacado. Debajo, en itálica gris azulado #44546A: "Cerramos el 1S en 93.4% del plan (+$239.3M, +1.5%) con las piezas cayendo −5.1%; el crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core (mix −$297.0M)". Línea horizontal fina gris #E5E9EE de margen a margen.

CUERPO en dos columnas. COLUMNA IZQUIERDA (~62% del ancho) — arriba, texto plano navy #0F2845 negrita: "Dónde crece el mercado y dónde crece PiSA: una fila comparable, tres proxys". Debajo, una tabla de 4 columnas dividida en DOS bloques. Encabezado con fondo navy #0F2845 y texto blanco negrita: "Segmento" (izquierda) | "Mercado · valor" (derecha) | "PiSA · valor" (derecha) | "Base de comparación" (izquierda). Cuerpo gris #3D4A5F, filas alternando blanco y gris muy claro #F0F3F7, línea inferior fina gris #E5E9EE por fila, SIN líneas verticales.
Primer bloque: una fila-rótulo de grupo en mayúsculas chicas gris #5A6679 sobre fondo gris muy claro #F0F3F7 que dice "COMPARABLE · MISMO UNIVERSO", y debajo la fila:
Retail (mercado foco) | −4.2% | −0.1% (y debajo del −0.1%, dentro de la misma celda, en chico gris #5A6679: "en sell-in Retail: +0.4%") | Mismo universo: KB Entry Market MAT may-26 (mercado y PiSA/AMSA en el mismo corte)
Bajo esa fila, una línea indentada en gris chico #5A6679: "Unidades del mismo universo: mercado −7.9% · PiSA −9.4%."
Después, una línea divisoria más gruesa azul #0F4C81 (horizontal) y el segundo bloque: fila-rótulo "PROXY · UNIVERSOS DISTINTOS" (mismo formato de rótulo) y tres filas:
Gobierno FC | −3.8% | −0.6% | Proxy: INEFAM genéricos ene-may vs sell-in PiSA
Hospitales | [−5% validar: CC] | +5.1% | Proxy: IQVIA (por validar) vs sell-in PiSA
Servicios | n/a | +4.0% | Proxy: modelos propios vs sell-in PiSA
Color de las celdas: "−4.2%" y "−3.8%" en rojo #C00000; "−0.6%" en rojo #C00000; "+5.1%" y "+4.0%" en gris muy oscuro NEUTRO #1A2332 (NUNCA en verde); la celda "[−5% validar: CC]" completa en gris #8A95A8 (sin color de alerta); "n/a" en gris #8A95A8. La celda "−0.1%" (fila Retail, columna PiSA · valor) va en negrita color dorado #C5A55A: es el ÚNICO elemento dorado de toda la lámina.
Bajo la tabla, una nota en gris chico #8A95A8: "Corte Knobloch por unificar [CC]: la llamada del 16-jul reporta mercado +4.1% en dinero / −4.5% en unidades y +2.2% sin GLP-1, corte distinto al Entry Market impreso; no sustituir sin unificación de CC."

COLUMNA DERECHA (~36% del ancho) — DOS bloques apilados, cada uno con una línea superior fina azul #0F4C81 (sin bordes laterales). Cada bloque: un micro-título navy #0F2845 negrita pequeño y debajo un texto gris #3D4A5F pequeño:
Bloque 1 — "El mercado sólo crece por GLP-1 y precio" / "Privado sin GLP-1: +1.4% en valor y −4.8% en unidades (KB MAT may-26). La demanda física cae."
Bloque 2 — "Consumo débil, confirmado por terceros" / "BBVA −4.9% anual a jun-26 (quinta caída consecutiva); ANTAD +0.8% nominal, es decir, caída real."

FRANJA DE UNA LÍNEA (ancho completo, encima de la leyenda), gris muy oscuro #1A2332: "La cadena de suministro se estabilizó; el reto se movió a acelerar la venta."

LÍNEA DE LEYENDA (ancho completo, encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE (abajo, ~12%): línea fina gris #E5E9EE; debajo, en gris #8A95A8 pequeño, a la izquierda en itálica: "Fuente: Sell-In PiSA cierre jun-26 (1S, cubo; +$239.3M = 16,279.2 a 16,518.5); matriz consolidada Downtrading FINAL 16-jul (mix, core); Knobloch Entry Market MAT may-26 (mercado foco PiSA/AMSA, sin electrolitos, fórmulas infantiles ni GLP-1); INEFAM ene-may-26; IQVIA (Hospitales, por validar); BBVA Research y ANTAD jun-26"; a la derecha: "PiSA Confidencial | 2".

Reglas estrictas: la comparación va como tabla en dos bloques (comparable vs proxy; los universos no se mezclan en una sola gráfica); el color vive solo en los deltas negativos y el dorado solo en la celda "−0.1%"; los positivos de PiSA (+5.1%, +4.0%) van en neutro, JAMÁS en verde; el placeholder "[−5% validar: CC]" se dibuja literal en gris, sin rellenar. Ningún carácter de flecha en el texto; ningún em-dash; sin emojis; sin rótulos de caja tipo INSIGHT o SO WHAT; sin borde izquierdo; sin gradientes; español con acentos; título sin punto final.
```


---

# Lamina 3 · Q2 facturó $8,495.7M, +5.9% contra Q1; junio es el segundo mejor mes de los últimos 36
- **Momento:** M0 · Apertura y resumen ejecutivo
- **Encabezado:** Q2 facturó $8,495.7M, +5.9% contra Q1; junio es el segundo mejor mes de los últimos 36
- **So-what subtitle:** El asterisco lo ponemos nosotros: ~$104M de compra adelantada y calendario favorable en junio
- **Layout:** Banda de título 18% + cuerpo 2 columnas 45/55 (izquierda: stack de KPIs; derecha: mini ranking de meses) 54% + banda de asterisco 18% + footer 10%. Gutter entre columnas 0.15in; márgenes 0.5in.

## Zona por zona

### Zona A — Banda de título (18%)
- Título: Calibri Light 32 pt `#0F2845`; "$8,495.7M" y "+5.9%" en Calibri bold (énfasis puntual).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Stack de KPIs (columna izquierda, 45%)
- Tipo: 1 KPI hero + 2 KPI cards secundarias lado a lado.
- KPI hero (arriba, ancho completo de la columna):
  - Label: "VENTA Q2 2026 · SELL-IN" — Calibri Light 10.5 pt UPPERCASE `#5A6679`.
  - Valor: "$8,495.7M" — Calibri bold 40 pt `#0F2845`, tabular figures.
  - Delta: "+$473.0M (+5.9%) vs Q1-26" — Calibri Light 14 pt bold, `#0F2845` (navy; FUERA el verde: cifra propia sin aplauso). El triángulo indicador de subida se dibuja como SHAPE (triángulo pequeño relleno navy junto al delta), NUNCA como carácter "▲" dentro del cuadro de texto.
- Dos KPI cards secundarias (fila de 2, 50/50; separación con border 0.5 pt `#E5E9EE`, sin fondo — una sola técnica de separación):
  - Card 1 — Label: "JUNIO 2026 *" (el asterisco SIEMPRE visible junto al mes). Valor: "$2,986.9M" Calibri bold 24 pt `#0F2845`. Context: "#2 de los últimos 36 meses" Calibri Light 10 pt `#5A6679`.
  - Card 2 — Label: "MAYO 2026". Valor: "$2,843.9M" Calibri bold 24 pt `#0F2845`. Context: "#6 de los últimos 36 meses" Calibri Light 10 pt `#5A6679`.
- No imprimir el nivel de Q1 (evitar dos derivaciones que difieran por redondeo); el delta +$473.0M / +5.9% carga la comparación.

### Zona C — Mini ranking de meses (columna derecha, 55%)
- Tipo: tabla compacta 6 filas × 3 columnas.
- Kicker sobre la tabla: "Ranking de meses de venta · ventana jul-23 a jun-26 (36 meses, sell-in)" — Calibri bold 11 pt `#0F2845`.
- Header de tabla: fondo `#0F2845`, texto blanco Calibri bold 11 pt. Columnas: "#" (centro) | "Mes" (izquierda) | "Venta ($M)" (derecha, tabular figures).
- Filas (alternas blanco / `#F0F3F7`):
  1. | oct-25 | 3,048.6
  2. | jun-26 * | 2,986.9  ← fila destacada: fondo `#E8F1F8`, texto Calibri bold
  3. | sep-25 | 2,985.3
  4. | abr-25 | 2,932.0
  5. | oct-24 | 2,886.0
  6. | may-26 | 2,843.9  ← texto Calibri bold, sin fondo especial
- Anotación bajo la tabla (Calibri Light 10 pt `#5A6679`): "El #2 le gana al #3 (sep-25) por $1.6M: 'segundo mejor mes' se dice con esa conciencia".
- Ranking completo VERIFICADO por el orquestador contra la fuente (resumen_sell_in_consejo_27jul.xlsx, hoja 04_Meses, 16-jul): #1 oct-25 $3,048.6M · #2 jun-26 $2,986.9M · #3 sep-25 $2,985.3M · #4 abr-25 $2,932.0M · #5 oct-24 $2,886.0M · #6 may-26 $2,843.9M. La diferencia #2 contra #3 ($1.6M) cuadra.

### Zona D — Banda de asterisco (18%)
- Tipo: prosa directa, SIN caja, SIN rótulo. Arranca con el símbolo "*" que liga con junio.
- Texto final (Calibri Light 11 pt `#3D4A5F`; solo "~$104M" en Calibri bold): "* Junio trae ~$104M de compra adelantada identificable, Simi $30M, Nadro $30M, Fanasa $27M, JMP $17M [cerrar cifra: CC], y un calendario favorable en Hospitales: 5 lunes y ~$10M one-off de mezclas por los paros de ABC/OCA."
- La frase "Meta contra real, sin aplauso" NO se imprime (es instrucción de speaker; vive en Notas). Cero em-dash en la prosa: la enumeración va con comas.

### Zona E — Footer (10%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 3".

- **Mensaje que manda la lamina:** Q2 aceleró de verdad (+5.9% contra Q1) y junio quedó a nada del mejor mes en tres años, pero el asterisco lo declaramos nosotros: parte del mes es compra adelantada y calendario, no demanda pura.
- **Fuente (pie de lamina):** Fuente: Sell-In PiSA, cierre jun-26; ranking sobre ventana jul-23 a jun-26 (36 meses); compra adelantada: estimación Comercial [cerrar cifra: CC]
- **Estado del dato:**
  - Zona B (Q2 $8,495.7M, +$473.0M, +5.9%; jun $2,986.9M #2; may $2,843.9M #6): en mano (verificado contra sell-in, storyline v6)
  - Zona C: ranking completo en mano, VERIFICADO contra hoja 04_Meses del sell-in (16-jul); ya no hay placeholders [IC]
  - Zona D (~$104M y desglose): por completar [CC — cerrar cifra]; 5 lunes y ~$10M one-off: en mano (aprox. declarado en v6)
- **Notas para el dibujante:**
  - CERO gold en esta lámina: el dato ganador no se festeja ("meta contra real, sin aplauso" es la instrucción del SPEAKER, no texto imprimible). El destaque de jun-26 es tipográfico (bold + fondo `#E8F1F8`), nunca dorado ni verde. El delta del Q2 va en navy, sin verde (KILL-LIST 16-jul: verde celebratorio fuera de cifras propias).
  - Rank ex-adelanto (nota, NO imprimible): si a junio se le descuentan los ~$104M de compra adelantada, el mes queda en ~$2,883M y caería del #2 a aproximadamente el #5 de la ventana (verificar contra hoja 04_Meses antes de imprimir cualquier versión). Decisión de Rafael PENDIENTE sobre si encabezar la lámina con el subyacente en vez del reportado.
  - Todo texto entre corchetes con responsable ("[cerrar cifra: CC]") es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris en el borrador y se elimina antes de la sesión.
  - El asterisco de junio aparece DOS veces: en la KPI card y en la fila #2 del ranking; ambos remiten a la banda D. No omitirlo en ninguna instancia.
  - La banda D es prosa con "*" inicial: PROHIBIDO rotularla ("NOTA", "INSIGHT", "SO WHAT" o similar) y prohibido darle caja con fondo.
  - No graficar el ranking como barras: con valores entre 2,843 y 2,987 y eje obligado en cero, las barras serían indistinguibles. La tabla es la forma correcta.
  - Números con coma de miles y un decimal; alineados a la derecha con tabular figures. El signo $ solo en el KPI hero y en el header de la columna.
  - Universo: sell-in PiSA exclusivamente; no meter aquí ningún dato de mercado (Knobloch/IQVIA).

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; números con figuras tabulares alineados a la derecha en la tabla. Cuatro bandas horizontales apiladas.

BANDA 1 (18% superior, título): título grande navy #0F2845 en peso ligero, con "$8,495.7M" y "+5.9%" en negrita: "Q2 facturó $8,495.7M, +5.9% contra Q1; junio es el segundo mejor mes de los últimos 36". Debajo, subtítulo en itálica gris #44546A: "El asterisco lo ponemos nosotros: ~$104M de compra adelantada y calendario favorable en junio".

BANDA 2 (54%, cuerpo en dos columnas, izquierda 45% / derecha 55%, con separación).
COLUMNA IZQUIERDA (stack de KPIs): arriba un KPI hero de ancho completo — etiqueta chica MAYÚSCULAS gris #5A6679 "VENTA Q2 2026 · SELL-IN"; valor enorme en negrita navy #0F2845 "$8,495.7M"; debajo el delta en NAVY #0F2845 (no verde): "+$473.0M (+5.9%) vs Q1-26", precedido por un triángulo pequeño de subida dibujado como FORMA rellena navy (no un carácter de texto). Debajo del hero, dos tarjetas KPI lado a lado separadas solo por una línea fina gris #E5E9EE, sin fondo. Tarjeta 1: etiqueta "JUNIO 2026 *" (con asterisco visible), valor en negrita navy "$2,986.9M", contexto en gris "#2 de los últimos 36 meses". Tarjeta 2: etiqueta "MAYO 2026", valor en negrita navy "$2,843.9M", contexto "#6 de los últimos 36 meses".
COLUMNA DERECHA (mini ranking de meses): un kicker en negrita navy #0F2845 "Ranking de meses de venta · ventana jul-23 a jun-26 (36 meses, sell-in)". Debajo una tabla compacta de 6 filas y 3 columnas. Encabezado con fondo navy #0F2845 y texto blanco en negrita, columnas: "#" (centrado) | "Mes" (izquierda) | "Venta ($M)" (derecha). Filas alternando blanco y gris muy claro #F0F3F7, sin líneas verticales, números a la derecha:
1 | oct-25 | 3,048.6
2 | jun-26 * | 2,986.9  (esta fila destacada con fondo azul claro #E8F1F8 y texto en negrita)
3 | sep-25 | 2,985.3
4 | abr-25 | 2,932.0
5 | oct-24 | 2,886.0
6 | may-26 | 2,843.9  (texto en negrita, sin fondo especial)
Debajo de la tabla, una anotación chica gris #5A6679: "El #2 le gana al #3 (sep-25) por $1.6M: 'segundo mejor mes' se dice con esa conciencia".

BANDA 3 (18%, prosa de asterisco): un solo párrafo, SIN caja y SIN rótulo, que arranca con el símbolo "*", texto en gris #3D4A5F con solo "~$104M" en negrita: "* Junio trae ~$104M de compra adelantada identificable, Simi $30M, Nadro $30M, Fanasa $27M, JMP $17M [cerrar cifra: CC], y un calendario favorable en Hospitales: 5 lunes y ~$10M one-off de mezclas por los paros de ABC/OCA." Dibuja "[cerrar cifra: CC]" literal con sus corchetes. No uses rayas largas (em-dash) en este párrafo: solo comas.

BANDA 4 (10% inferior, pie): línea divisoria gris #E5E9EE; debajo, en gris claro #8A95A8 chico, a la izquierda: "Fuente: Sell-In PiSA, cierre jun-26; ranking sobre ventana jul-23 a jun-26 (36 meses); compra adelantada: estimación Comercial [cerrar cifra: CC]"; a la derecha: "PiSA Confidencial | 3".

Reglas estrictas: NADA en dorado ni en verde en esta lámina; el destaque de jun-26 es solo tipográfico (negrita + fondo azul claro); el delta del Q2 va en navy #0F2845. Ningún carácter de flecha ni de triángulo en texto (el indicador de subida del delta es una pequeña forma triangular dibujada, no un carácter); sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin rayas largas (em-dash) en la prosa; español con acentos; título sin punto final; el signo $ aparece solo en el KPI hero y en el encabezado de columna "Venta ($M)".
```


---

# Lámina 4 · Vamos a llegar al [96]: el 2S debe correr a 98.5% de su plan, +5.1 puntos de intensidad sobre el ritmo del 1S
- **Momento:** M0 · Apertura y resumen ejecutivo
- **Encabezado:** Vamos a llegar al [96]: el 2S debe correr a 98.5% de su plan, +5.1 puntos de intensidad sobre el ritmo del 1S
- **So-what subtitle:** El [96] anual exige $18,115.1M en jul-dic; el hueco contra el ritmo del 1S se cierra con palancas propias por segmento
- **Layout:** Banda de título 16% + cuerpo 66% (gráfica de intensidad izquierda ~52% · lógica del número derecha ~44%, gutter 0.15in) + banda de dependencia 8% + footer 10%. Márgenes 0.5in; 13.333 × 7.5 in.
- **Naturaleza:** lámina CONCEPTUAL. Todas las cifras del 2S ($18,115.1M, 98.5%, +5.1 pts) están calculadas SUPONIENDO el [96] anual; el [96] es placeholder que se cierra con Heriberto antes del 20-jul. Si [96] cambia, se recalcula toda la lámina. Esa condicionalidad se rotula, no se esconde.

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 28-32 pt `#0F2845` (2 líneas). El chip "[96]" se imprime literal dentro del título, mismo color del título (no en gris, es parte de la frase; su condición se explica en la banda de dependencia).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.
- Separador 0.5 pt `#E5E9EE`.

### Zona B — Gráfica de intensidad: ritmo 1S vs ritmo exigido 2S (izquierda, ~6.1 in). Dos columnas.
- Micro-título de zona: "El ritmo tiene que subir" — Calibri bold 12 pt `#0F2845` (texto plano).
- Dos columnas verticales, escala "% del plan del semestre", eje Y arranca en 0 (marcar el eje hasta 100% con una línea guía punteada `#E5E9EE` en 100%), sin gridlines adicionales, sin leyenda:
  - Columna 1: **Ritmo 1S = 93.4%** — relleno `#0F2845`; data label "93.4%"; debajo, en `#5A6679` 10 pt: "$16,518.5M de $17,678.3M".
  - Columna 2: **Ritmo exigido 2S = 98.5%** — relleno `#0F4C81`, más alta; data label "98.5%" (ver gold); debajo, en `#5A6679` 10 pt: "$18,115.1M requeridos de $18,398.7M".
- Corchete/conector entre los topes de ambas columnas, rotulado "+5.1 puntos de intensidad" — Calibri bold 16 pt `#0F2845` (AGRANDADA por instrucción 16-jul: es la anotación protagonista de la gráfica; debe leerse antes que los data labels).
- Nota bajo la gráfica, Calibri Light 9.5 pt `#5A6679`: "Cifras calculadas al [96] anual; condicionales a ese cierre."

### Zona C — La lógica del número (derecha, ~5.2 in). Cuatro pasos + una nota de utilidad.
- Micro-título de zona: "Cómo se arma el número" — Calibri bold 12 pt `#0F2845`.
- Cuatro renglones cortos, Calibri Light 11 pt `#3D4A5F`, cada uno con un top border 1 pt `#0F4C81` sutil (sin border-left); el chip "[96]" en gris placeholder `#8A95A8` donde aparece como dato pendiente:
  1. "El compromiso del año es [96]."
  2. "Ese [96] exige $18,115.1M de venta en jul-dic."
  3. "Equivale a correr el 2S a 98.5% de su plan ($18,398.7M)."
  4. "El hueco contra el ritmo del 1S se cierra con palancas propias, segmento por segmento."
- Nota de utilidad al pie de la zona, Calibri Light 10 pt `#3D4A5F`, con su placeholder declarado: "Con contribución de ~53 centavos por peso, ese [96] alcanza la meta de utilidad del año [soporte del puente ingreso a utilidad: VJ/Finanzas]."
- Placeholder declarado adicional, Calibri Light 10 pt `#8A95A8`: "[Cifra fina del hueco por segmento: RC, con los puentes de segmento]."

### Zona D — Banda de dependencia (8%, sobre el footer, ancho completo)
- Fondo `#F0F3F7` sin border-left, top border 2 pt `#0F4C81`. Una línea, Calibri Light 11 pt `#1A2332`: "Toda esta lámina depende del [96] final: se cierra con Dirección General antes del 20-jul. Si [96] cambia, las cifras del 2S se recalculan." (KILL-LIST: sin nombres de staff en texto imprimible; "Heriberto" solo en notas internas.)

### Zona E — Footer (10%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 4".

## Mensaje que manda la lámina
No es fe: es aritmética condicional. El compromiso anual [96] fija el número de jul-dic ($18,115.1M) y obliga a correr el 2S a 98.5% de su plan, +5.1 puntos de intensidad sobre el 93.4% del 1S. Ese hueco se cierra con palancas propias que se muestran segmento por segmento; el número fino por segmento y el puente a utilidad están declarados como pendientes, no inventados.

## Fuente (pie de lámina)
Fuente: Sell-In PiSA cierre jun-26 (1S = $16,518.5M de $17,678.3M); meta anual y del 2S = plan comercial 2026; el compromiso [96] se cierra con Dirección General antes del 20-jul. Cifras del 2S condicionales a ese cierre

## Estado del dato
- $16,518.5M / $17,678.3M / 93.4% (1S): **en mano** (sell-in cierre jun-26, verificado).
- $18,115.1M jul-dic y 98.5% del plan del 2S: **en mano pero condicional** — calculados al [96] anual (96% de la meta anual $36,076.6M = $34,634M; menos 1S $16,518.5M = $18,115.5M ≈ $18,115.1M; el plan del 2S = $36,076.6M − $17,678.3M = $18,398.3M; 18,115.1/18,398.7 = 98.5%). Se recalculan si [96] cambia.
- +5.1 puntos: derivado (98.5% − 93.4%).
- [96] anual: **placeholder** (Heriberto, antes del 20-jul; en el imprimible se dice "Dirección General", nunca el nombre).
- Hueco fino por segmento: **placeholder [RC]** (con los puentes).
- 53¢ por peso y puente a utilidad: **placeholder de soporte [VJ/Finanzas]** (el consejo lo marcó sin soporte; sube declarado, no como cifra dura).
- [definición del hueco pendiente: Rafael — esta lámina usa ritmo sobre plan (~$931M implícito); L31 usa repetir venta ($1,596.6M); UNA sola definición antes del 22]. Mientras no se decida, NO imprimir ninguna cifra de "hueco" en esta lámina.

## Notas para el dibujante
- Es una lámina conceptual: la columna 2 y sus cifras son condicionales al [96]. NO borrar la banda de dependencia ni la nota "calculadas al [96]" bajo la gráfica: son el corazón de la honestidad de la lámina.
- Todo texto entre corchetes con responsable ([RC], [VJ/Finanzas]) es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris en el borrador y se elimina antes de la sesión.
- El chip "[96]" se dibuja literal en TODAS sus apariciones. En el título va en el color del título (es parte de la frase). En los renglones de la Zona C y en la banda de dependencia va como dato pendiente en gris `#8A95A8`. No sustituir por un número.
- Los placeholders "[Cifra fina del hueco por segmento: RC…]" y "[soporte del puente ingreso a utilidad: VJ/Finanzas]" se dibujan literales, gris neutro, sin ámbar ni rojo.
- Barras arrancan en cero; la columna 2 (98.5%) supera a la columna 1 (93.4%) por aproximadamente 5 puntos de altura sobre una escala 0-100%. Ambas navy (no verde: no es un resultado celebrado, es una meta exigida).
- Sin caja de insight; los micro-títulos de zona son texto plano navy; sin border-left; la banda de dependencia usa top border, no borde lateral.
- Tabular figures en todo número; unidades "% del plan del semestre" y "$M" declaradas.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; números en figuras tabulares; usa el signo menos tipográfico "−" y el "+" explícito. Es una lámina conceptual: incluye literalmente los textos entre corchetes.

BANDA DE TÍTULO (arriba, ~16%, ancho completo): título grande navy #0F2845 en peso ligero, hasta dos líneas, con el corchete impreso tal cual: "Vamos a llegar al [96]: el 2S debe correr a 98.5% de su plan, +5.1 puntos de intensidad sobre el ritmo del 1S". Debajo, itálica gris azulado #44546A: "El [96] anual exige $18,115.1M en jul-dic; el hueco contra el ritmo del 1S se cierra con palancas propias por segmento". Línea fina gris #E5E9EE de margen a margen.

CUERPO en dos columnas. COLUMNA IZQUIERDA (~52%) — arriba, texto plano navy #0F2845 negrita: "El ritmo tiene que subir". Debajo, una gráfica de DOS columnas verticales, eje Y desde 0 en escala "% del plan del semestre", con una línea guía punteada gris #E5E9EE a la altura de 100%, sin otras gridlines, sin leyenda. Columna 1 rellena navy oscuro #0F2845, etiqueta "93.4%", y debajo en gris #5A6679 pequeño "$16,518.5M de $17,678.3M" (rótulo: Ritmo 1S). Columna 2 rellena navy medio #0F4C81, MÁS ALTA que la columna 1 por unos 5 puntos de altura, etiqueta "98.5%" en negrita color dorado #C5A55A (único elemento dorado de la lámina), y debajo en gris #5A6679 pequeño "$18,115.1M requeridos de $18,398.7M" (rótulo: Ritmo exigido 2S). Entre los topes de ambas columnas, un corchete/conector rotulado en navy oscuro negrita GRANDE (más grande que los data labels de las columnas; es la anotación protagonista): "+5.1 puntos de intensidad". Bajo la gráfica, texto pequeño gris #5A6679: "Cifras calculadas al [96] anual; condicionales a ese cierre."

COLUMNA DERECHA (~44%) — arriba, texto plano navy #0F2845 negrita: "Cómo se arma el número". Debajo, cuatro renglones cortos en gris #3D4A5F, cada uno con una línea superior fina azul #0F4C81 (sin bordes laterales); el corchete "[96]" impreso en gris #8A95A8:
1. "El compromiso del año es [96]."
2. "Ese [96] exige $18,115.1M de venta en jul-dic."
3. "Equivale a correr el 2S a 98.5% de su plan ($18,398.7M)."
4. "El hueco contra el ritmo del 1S se cierra con palancas propias, segmento por segmento."
Debajo de los cuatro renglones, en gris #3D4A5F pequeño: "Con contribución de ~53 centavos por peso, ese [96] alcanza la meta de utilidad del año [soporte del puente ingreso a utilidad: VJ/Finanzas]." Y en gris #8A95A8 pequeño: "[Cifra fina del hueco por segmento: RC, con los puentes de segmento]." Estos corchetes se dibujan literales, sin rellenar.

BANDA DE DEPENDENCIA (ancho completo, encima del pie): rectángulo de fondo gris muy claro #F0F3F7 con una línea superior gruesa azul #0F4C81 (sin borde izquierdo). Una línea gris muy oscuro #1A2332: "Toda esta lámina depende del [96] final: se cierra con Dirección General antes del 20-jul. Si [96] cambia, las cifras del 2S se recalculan."

PIE (abajo, ~10%): línea fina gris #E5E9EE; debajo, gris #8A95A8 pequeño, izquierda en itálica: "Fuente: Sell-In PiSA cierre jun-26 (1S = $16,518.5M de $17,678.3M); meta anual y del 2S = plan comercial 2026; el compromiso [96] se cierra con Dirección General antes del 20-jul. Cifras del 2S condicionales a ese cierre"; derecha: "PiSA Confidencial | 4".

Reglas estrictas: ambas columnas en tonos navy (no verde: es una meta exigida, no un resultado celebrado); el dorado solo en la etiqueta "98.5%"; todos los corchetes se dibujan literales sin rellenar. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT o SO WHAT; sin borde izquierdo; sin gradientes ni sombras infladas; español con acentos; título sin punto final.
```


---

# Lamina 5 · Cuatro modelos de negocio, cuatro conversaciones: la sesión avanza por peso de venta
- **Momento:** M0 · Apertura y resumen ejecutivo
- **Encabezado:** Cuatro modelos de negocio, cuatro conversaciones: la sesión avanza por peso de venta
- **So-what subtitle:** Presupuesto de tiempo protegido por bloque; Servicios se presenta por primera vez
- **Layout:** Banda de título 16% + cuerpo de bloques por segmento 50% (4 bloques en una fila, ancho PROPORCIONAL al peso de venta 43.6 : 24.4 : 18.5 : 13.4, gutter 0.15in) + leyenda única de contenido de bloque 6% + banda de ruta de la sesión 18% + footer 10%. Márgenes 0.5in.

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 32 pt `#0F2845`.
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Bloques por segmento (50%; anchos proporcionales al peso)
- Tipo: 4 bloques-tarjeta en fila. El ancho de cada bloque codifica su peso de venta (Retail el más ancho, Servicios el más angosto): esa proporción ES el mensaje visual, respetarla.
- Estilo común: fondo `#FAFBFC` (gray-050), top border 2 pt `#0F4C81` (primary-700), border-radius 4-8 px, padding 0.20in. EXCEPCIÓN: bloque Servicios con top border 2 pt gold `#C5A55A` (único elemento gold de la lámina).
- Estructura interna de cada bloque (SIN los tres renglones repetidos; van UNA sola vez en la leyenda de Zona B-bis):
  - Nombre del segmento: Calibri bold 14 pt `#0F2845`.
  - Peso: Calibri bold 20 pt `#0F4C81`, tabular figures, con label "de la venta 1S" Calibri Light 9 pt `#5A6679`.
  - Número de láminas del bloque: Calibri Light 10 pt `#5A6679`.
- Bloque 1 — Retail: peso "43.6%" · "6 láminas".
- Bloque 2 — Gobierno (frasco cerrado): peso "24.4%" · "4 láminas".
- Bloque 3 — Hospitales: peso "18.5%" · "5 láminas".
- Bloque 4 — Servicios: peso "13.4%" · "5 láminas" · renglón extra bajo el nombre: "Primera vez en junta de Consejo" — Calibri Light 10 pt italic `#44546A`.

### Zona B-bis — Leyenda única de contenido de bloque (6%, bajo los 4 bloques)
- UNA sola línea centrada, Calibri Light 11 pt `#3D4A5F`, que sustituye los 3 renglones que antes se repetían dentro de cada bloque: "Cada bloque recorre lo mismo: entorno y competencia · el 1S (puente y radiografía) · plan 2S y aporte al hueco".
- Sin caja, sin fondo; separada de los bloques por 0.1in de aire.

### Zona C — Ruta completa de la sesión (18%)
- Tipo: secuencia horizontal de chips conectados por flechas DIBUJADAS como shape de línea con punta (color `#5A6679`, 1.5 pt outline; NUNCA el carácter "→" en un cuadro de texto, el gate lo rechaza; los chips: texto Calibri Light 10 pt `#3D4A5F` sobre fondo blanco con border 0.5 pt `#C5CDD9`).
- Secuencia exacta (los cuatro segmentos ya viven en Zona B; aquí se dibujan como un solo chip agrupador):
  "Apertura y resumen" | "Mapa del negocio y boleta competitiva" | "PiSA total: el 1S" | "Los cuatro segmentos (entorno · 1S · 2S)" | "La ruta consolidada al número" | "Proyectos críticos y conclusiones" | "Anexos"
- El chip "Los cuatro segmentos (entorno · 1S · 2S)" se dibuja más ancho y con border 1 pt `#0F4C81`, alineado visualmente bajo/sobre la Zona B para que se lea que es el corazón de la sesión.

### Zona D — Footer (10%)
- Línea 0.5 pt `#E5E9EE` + nota de redondeo + fuente + "PiSA Confidencial | 5".
- Nota impresa antes de la fuente (Calibri Light 9 pt `#8A95A8`): "Pesos sobre los 5 mercados sell-in ($16,518.5M, 1S-2026); no suman 100.0 por redondeo."

- **Mensaje que manda la lamina:** La sesión no es un promedio de PiSA: son cuatro modelos de negocio con mercados y competidores distintos, se recorren en orden de peso de venta, y el tiempo está presupuestado para que Servicios, que nunca ha subido al Consejo, tenga su espacio.
- **Fuente (pie de lamina):** Fuente: Sell-In PiSA, cierre jun-26; pesos por segmento sobre los 5 mercados ($16,518.5M, 1S-2026)
- **Estado del dato:** En mano (pesos 43.6 / 24.4 / 18.5 / 13.4 y conteos de láminas del storyline v6). Riesgo menor: el conteo de láminas por bloque puede moverse al ensamblar el deck; verificar contra el índice final antes de imprimir. KILL-LIST 16-jul aplicada: los 3 renglones repetidos por bloque se comprimen a UNA leyenda (Zona B-bis); "esta vez sí llegamos a Servicios" sale del imprimible.
- **Notas para el dibujante:**
  - LÍNEA DE SPEAKER (no imprimible): "esta vez sí llegamos a Servicios" la dice Rafael en voz; en la lámina solo queda "Primera vez en junta de Consejo" en el bloque Servicios y el subtítulo neutro.
  - El ÚNICO gold de la lámina es el top border del bloque Servicios. Nada más en dorado.
  - Los anchos de los bloques deben ser genuinamente proporcionales (43.6 : 24.4 : 18.5 : 13.4 del ancho útil menos gutters); no igualarlos por comodidad estética.
  - Es una lámina de mapa: los bloques solo llevan nombre, peso y conteo de láminas; el contenido común vive UNA vez en la leyenda de Zona B-bis. No inventar contenido distinto por bloque.
  - Sin iconos decorativos; las flechas de la Zona C son el único elemento gráfico permitido (outline gris).
  - PROHIBIDO convertir los pesos en pie/dona. La proporción vive en el ancho de los bloques.
  - Sin caja de insight. Sin emojis. Título sin punto final.
  - Universo: sell-in (solo para los pesos); no mezclar datos de mercado aquí.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; figuras tabulares en los números. Cuatro bandas horizontales apiladas.

BANDA 1 (16% superior, título): título grande navy #0F2845 en peso ligero: "Cuatro modelos de negocio, cuatro conversaciones: la sesión avanza por peso de venta". Debajo, subtítulo en itálica gris #44546A: "Presupuesto de tiempo protegido por bloque; Servicios se presenta por primera vez".

BANDA 2 (50%, cuatro bloques-tarjeta en una sola fila). IMPORTANTE: el ancho de cada bloque es proporcional a su peso de venta, en proporción 43.6 : 24.4 : 18.5 : 13.4 (el primero es el más ancho, el último el más angosto); esa proporción de anchos ES el mensaje, respétala. Todos los bloques con fondo gris muy claro #FAFBFC, esquinas redondeadas y una línea superior de 2 pt azul #0F4C81 (borde solo arriba, nunca a la izquierda), EXCEPTO el cuarto bloque (Servicios) cuya línea superior es dorada #C5A55A. Dentro de cada bloque, de arriba a abajo SOLO tres cosas: nombre del segmento en negrita navy #0F2845; el peso como número grande en negrita azul #0F4C81 con una etiqueta chica gris #5A6679 "de la venta 1S"; y el conteo de láminas en gris #5A6679. NO repitas renglones de contenido dentro de los bloques.
Bloque 1 Retail: peso "43.6%", "6 láminas".
Bloque 2 Gobierno (frasco cerrado): peso "24.4%", "4 láminas".
Bloque 3 Hospitales: peso "18.5%", "5 láminas".
Bloque 4 Servicios: peso "13.4%", "5 láminas", con un renglón extra en itálica gris #44546A bajo el nombre: "Primera vez en junta de Consejo".
Debajo de los cuatro bloques, UNA sola línea de leyenda centrada en gris #3D4A5F (sin caja, sin fondo): "Cada bloque recorre lo mismo: entorno y competencia · el 1S (puente y radiografía) · plan 2S y aporte al hueco".

BANDA 3 (18%, ruta de la sesión): una secuencia horizontal de chips (cajitas de fondo blanco con borde fino gris #C5CDD9, texto gris #3D4A5F) conectados entre sí por conectores dibujados como líneas grises #5A6679 con una punta de flecha al final (NO uses el carácter flecha en el texto de los chips; la punta es una forma gráfica). Los chips en este orden exacto: "Apertura y resumen", "Mapa del negocio y boleta competitiva", "PiSA total: el 1S", "Los cuatro segmentos (entorno · 1S · 2S)", "La ruta consolidada al número", "Proyectos críticos y conclusiones", "Anexos". El chip "Los cuatro segmentos (entorno · 1S · 2S)" se dibuja más ancho y con borde azul #0F4C81 de 1 pt, y queda visualmente alineado bajo los cuatro bloques de la banda 2 (es el corazón de la sesión).

BANDA 4 (10% inferior, pie): línea divisoria gris #E5E9EE; debajo, en gris claro #8A95A8 chico, a la izquierda una nota de redondeo seguida de la fuente: "Pesos sobre los 5 mercados sell-in ($16,518.5M, 1S-2026); no suman 100.0 por redondeo." y "Fuente: Sell-In PiSA, cierre jun-26; pesos por segmento sobre los 5 mercados ($16,518.5M, 1S-2026)"; alineado a la derecha: "PiSA Confidencial | 5".

Reglas estrictas: el ÚNICO elemento dorado es la línea superior del bloque Servicios; nada más en dorado. No conviertas los pesos en gráfica de pastel ni de dona: la proporción vive en el ancho de los bloques. Sin iconos decorativos. Ningún carácter de flecha dentro de texto; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; español con acentos; título sin punto final.
```


---

# Lámina 6 · Cuatro modelos de negocio con márgenes muy distintos: Hospitales rinde 39.2% de EBITDA y Gobierno FC solo 12.0%
- **Momento:** M1 · Mapa del negocio y boleta competitiva
- **Encabezado:** Cuatro modelos de negocio con márgenes muy distintos: Hospitales rinde 39.2% de EBITDA y Gobierno FC solo 12.0%
- **So-what subtitle:** La venta se reparte 43.6 / 24.4 / 18.5 / 13.4; Farma MX cerró el 1S con 23.5% de EBITDA ($3,879.6M) contra 19.7% en 1S-2025
- **Layout:** Banda de título 18% + tabla full-width 60% + caveats 10% + footer 12%. Tabla centrada, ancho útil completo (~12.3in). Márgenes 0.5in; 13.333 × 7.5 in.

## Zona por zona

### Zona A — Banda de título (18%)
- Título: Calibri Light 28-32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.
- Separador 0.5 pt `#E5E9EE`.

### Zona B — Tabla de los cuatro segmentos (la tablita) (60%)
- Tabla 6 filas de datos × 8 columnas. Header: fondo `#0F2845`, texto blanco Calibri bold 11 pt. Body: Calibri Light 11 pt `#3D4A5F`, filas alternas blanco / `#F0F3F7`, border inferior por fila 1 px `#E5E9EE`, sin líneas verticales, border externo 0.5 pt `#C5CDD9`. Tabular figures en toda celda numérica; "−" tipográfico, "+" explícito.
- Columnas: "Segmento" (izquierda) | "% venta 1S" (derecha) | "Cumpl. 1S" (derecha) | "Crec. PiSA" (derecha) | "Crec. mercado" (derecha) | "EBITDA 1S26 ($M · %)" (derecha) | "Margen 1S25" (derecha) | "% del EBITDA total" (derecha).

| Segmento | % venta 1S | Cumpl. 1S | Crec. PiSA | Crec. mercado | EBITDA 1S26 ($M · %) | Margen 1S25 | % del EBITDA total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Retail | 43.6% | 92.3% | +0.4% | −4.2% (EM·KB) | 2,479.1 · 34.4% | 31.2% | 63.9% |
| Gobierno (FC) | 24.4% | 90.0% | −0.6% | −3.8% (INEFAM) | 482.9 · 12.0% | 9.3% | 12.4% |
| Hospitales | 18.5% | 95.2% | +5.1% | −5% [validar IQVIA] | 1,196.8 · 39.2% | 37.6% | 30.9% |
| Servicios | 13.4% | 102.1% | +4.0% | n/a (modelos propios) | 321.8 · 14.5% | 8.7% | 8.3% |
| Gastos corporativos no distribuidos | · | · | · | · | −601.1 · n/a | · | −15.5% |
| **Total Farma MX (5 mercados)** | **100.0%** | **93.4%** | **+1.5%** | **·** | **3,879.6 · 23.5%** | **19.7%** | **100.0%** |

- Tratamiento de la fila total: "Total Farma MX (5 mercados)", Calibri bold, fondo `#F0F3F7`, border-top 2 pt `#0F2845`.
- Semáforo (solo en las columnas de delta, magnitud cuantitativa, SIN verde en cifras propias):
  - "Crec. PiSA": −0.6% en `#C00000`; +5.1% y +4.0% en navy `#0F4C81` (positivo sobrio, sin verde celebratorio); +0.4% de Retail en `#5A6679` neutro (plano, es la historia del +0.4% chato); el +1.5% de la fila total en `#0F2845` bold neutro (headline, no semáforo).
  - "Crec. mercado": −4.2% y −3.8% en `#C00000` (validados); la celda "−5% [validar IQVIA]" completa en gris placeholder `#8A95A8`; "n/a (modelos propios)" y "·" en `#8A95A8`.
- Placeholder declarado en la tabla (gris `#8A95A8`, literal): "−5% [validar IQVIA]". Ya NO hay placeholder en la celda EBITDA de Servicios: el split canónico del bloque Gobierno está en mano (Gob FC 482.9 · 12.0% / Servicios 321.8 · 14.5%).
- Gold: NINGUNO. Lámina de mapa sobria; el peso de la fila total se da con bold + border-top, no con gold. (Declarado: sin elemento gold.)

### Zona C — Caveats (10%)
- Tres bullets de UNA línea cada uno, Calibri Light 9-9.5 pt `#8A95A8`:
  - Bullet 1: "Pesos y cumplimiento sobre los 5 mercados sell-in ($16,518.5M); el consolidado (~$2.0B adicionales) queda fuera de esta vista [alcance y denominador del [96]: RC/CC/Rafael]."
  - Bullet 2: "EBITDA del Estado de Resultados v18 (Finanzas, ene-jun-26); split del bloque Gobierno por Gross2Net, cuadra con v18 al peso (±3.6M de Nuevos Productos sin repartir, declarado) [bendición Finanzas: VJ]."
  - Bullet 3: "Crecimiento de mercado por segmento en su propia fuente: Retail = Entry Market Knobloch MAT may-26; Gobierno = INEFAM genéricos ene-may; Hospitales por validar con IQVIA [CC]."

### Zona D — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 6".

## Mensaje que manda la lámina
PiSA no es un ente único: son cuatro modelos con márgenes que van de 39.2% (Hospitales) a 12.0% (Gobierno FC). El Consejo descubre aquí que Servicios existe, pesa 13.4% y es el margen que más expande: de 8.7% a 14.5% (+5.8 pp). El contraste de rentabilidad por modelo explica por qué defender cada segmento exige armas distintas; Farma MX cerró el 1S con 23.5% de EBITDA, arriba del 19.7% del año pasado.

## Fuente (pie de lámina)
Fuente: pesos, cumplimiento y crecimiento PiSA = Sell-In PiSA cierre jun-26 (5 mercados); EBITDA y % del EBITDA total = Estado de Resultados Farma MX v18 (Finanzas, acumulado ene-jun-26) con split del bloque Gobierno por Gross2Net; crecimiento de mercado por segmento en su propia fuente (Knobloch / INEFAM / IQVIA)

## Estado del dato
- Pesos, cumplimiento, crecimiento PiSA (43.6/24.4/18.5/13.4; 92.3/90.0/95.2/102.1; +0.4/−0.6/+5.1/+4.0; total 100/93.4/+1.5): **en mano** (sell-in cierre jun-26).
- EBITDA por segmento con SPLIT CANÓNICO (Retail 2,479.1·34.4% / Gob FC 482.9·12.0% / Hospitales 1,196.8·39.2% / Servicios 321.8·14.5% / Gastos corporativos no distribuidos −601.1 / total 3,879.6·23.5%): **en mano** (v18 + split del bloque Gobierno por Gross2Net, cuadra con v18 al peso; ±3.6M de Nuevos Productos sin repartir declarado; bendición Finanzas VJ). SUPERSEDE al bloque combinado "comb. 804.8 · 12.9%" y al placeholder "[en comb. Gobierno: VJ/Finanzas]" de la versión anterior.
- Margen 1S25 por segmento (Gross2Net): Retail 31.2% / Gob FC 9.3% / Hospitales 37.6% / Servicios 8.7% (Servicios +5.8 pp, el que más expande); total 19.7%: **en mano**.
- % del EBITDA total recalculado con el split: 63.9 / 12.4 / 30.9 / 8.3 / −15.5 = 100.0 exacto.
- Redondeo declarado: la suma visible de la columna EBITDA a 1 decimal da 3,879.5 vs total 3,879.6 ($0.1M de redondeo); la fuente cuadra al peso. No forzar la tabla a cuadrar visualmente.
- Título anterior ("Gobierno combinado sólo 12.9%") superado por el split canónico: ahora Gob FC 12.0% y Servicios 14.5% por separado.
- Crec. mercado Hospitales **[−5% validar IQVIA]**: placeholder declarado.
- Alcance del consolidado (~$2.0B) y denominador del [96]: **placeholder [RC/CC/Rafael]**.

## Notas para el dibujante
- FLAG DE CONCILIACIÓN (no se dibuja, contexto): la Venta Neta de Finanzas para Hospitales es 3,055.9 y el sell-in es 3,054.5 (Δ +1.4M por redondeo/definición); la tabla usa el peso de sell-in (18.5%) y el EBITDA de Finanzas (1,196.8·39.2%). No es choque material; no "corregir" en la lámina.
- Esta lámina SÍ footea a la vista: la fila "Gastos corporativos no distribuidos −601.1" es la que hace que los EBITDA de segmento sumen el total 3,879.6 y que la columna "% del EBITDA total" cierre a 100%. No omitirla (fue el hallazgo del consejo: sin ella la tabla sumaba de más). La suma visible a 1 decimal trae $0.1M de redondeo declarado; no ajustar celdas.
- La columna "% del EBITDA total" es porcentaje del EBITDA total, NO % de la venta.
- La columna "Margen 1S25" es el margen EBITDA del mismo segmento un año antes (Gross2Net): es la que deja leer la expansión (Servicios 8.7% a 14.5%).
- Placeholder literal, gris neutro `#8A95A8`, sin ámbar ni rojo: "−5% [validar IQVIA]". No rellenar ni estimar.
- Todos los corchetes con responsable ([RC/CC/Rafael], [VJ], [CC]) son PLACEHOLDER INTERNO — kill antes del 27: se dibujan literales en el storyboard de revisión, pero se retiran o resuelven antes de la versión que ve el Consejo.
- SIN verde en ninguna celda: los positivos de "Crec. PiSA" (+5.1%, +4.0%) van en navy `#0F4C81` sobrio, no en verde (regla: sin verde celebratorio en cifras propias). El +0.4% de Retail va en gris neutro (plano). El +1.5% total va en navy bold, no semáforo.
- Sin caja de insight; sin gold (declarado); sin border-left; sin círculos de semáforo ni iconos de estatus. El símbolo $ no se repite por celda: lo declara el header "EBITDA 1S26 ($M · %)".

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares alineados a la derecha; signo menos tipográfico "−", "+" explícito. El centro lo domina una tabla de ancho completo.

BANDA DE TÍTULO (arriba, ~18%): título grande navy #0F2845 en peso ligero, hasta dos líneas: "Cuatro modelos de negocio con márgenes muy distintos: Hospitales rinde 39.2% de EBITDA y Gobierno FC solo 12.0%". Debajo, itálica gris azulado #44546A: "La venta se reparte 43.6 / 24.4 / 18.5 / 13.4; Farma MX cerró el 1S con 23.5% de EBITDA ($3,879.6M) contra 19.7% en 1S-2025". Línea fina gris #E5E9EE de margen a margen.

TABLA (centro, ancho completo, ~60%). Encabezado con fondo navy #0F2845 y texto blanco negrita; 8 columnas: "Segmento" (izquierda) | "% venta 1S" (derecha) | "Cumpl. 1S" (derecha) | "Crec. PiSA" (derecha) | "Crec. mercado" (derecha) | "EBITDA 1S26 ($M · %)" (derecha) | "Margen 1S25" (derecha) | "% del EBITDA total" (derecha). Cuerpo gris #3D4A5F, filas alternando blanco y gris muy claro #F0F3F7, línea inferior fina gris #E5E9EE por fila, SIN líneas verticales. Filas en este orden:
Retail | 43.6% | 92.3% | +0.4% | −4.2% (EM·KB) | 2,479.1 · 34.4% | 31.2% | 63.9%
Gobierno (FC) | 24.4% | 90.0% | −0.6% | −3.8% (INEFAM) | 482.9 · 12.0% | 9.3% | 12.4%
Hospitales | 18.5% | 95.2% | +5.1% | −5% [validar IQVIA] | 1,196.8 · 39.2% | 37.6% | 30.9%
Servicios | 13.4% | 102.1% | +4.0% | n/a (modelos propios) | 321.8 · 14.5% | 8.7% | 8.3%
Gastos corporativos no distribuidos | · | · | · | · | −601.1 · n/a | · | −15.5%
Total Farma MX (5 mercados) | 100.0% | 93.4% | +1.5% | · | 3,879.6 · 23.5% | 19.7% | 100.0%   (esta fila total en negrita, fondo gris #F0F3F7, con línea superior gruesa navy #0F2845)
Color de celdas: en "Crec. PiSA", "−0.6%" en rojo #C00000; "+5.1%" y "+4.0%" en azul navy #0F4C81 (NO verde); "+0.4%" en gris neutro #5A6679; el "+1.5%" de la fila total en navy #0F2845 negrita (sin semáforo). En "Crec. mercado", "−4.2% (EM·KB)" y "−3.8% (INEFAM)" en rojo #C00000; "−5% [validar IQVIA]" completo en gris #8A95A8; "n/a (modelos propios)" y "·" en gris #8A95A8. NO hay ningún elemento dorado en esta lámina y NO se usa verde en ninguna celda.

CAVEATS (tres bullets de una línea, ~10%, gris #8A95A8 pequeño):
Bullet 1: "Pesos y cumplimiento sobre los 5 mercados sell-in ($16,518.5M); el consolidado (~$2.0B adicionales) queda fuera de esta vista [alcance y denominador del [96]: RC/CC/Rafael]."
Bullet 2: "EBITDA del Estado de Resultados v18 (Finanzas, ene-jun-26); split del bloque Gobierno por Gross2Net, cuadra con v18 al peso (±3.6M de Nuevos Productos sin repartir, declarado) [bendición Finanzas: VJ]."
Bullet 3: "Crecimiento de mercado por segmento en su propia fuente: Retail = Entry Market Knobloch MAT may-26; Gobierno = INEFAM genéricos ene-may; Hospitales por validar con IQVIA [CC]."

PIE (~12%): línea fina gris #E5E9EE; debajo, gris #8A95A8 pequeño, izquierda en itálica: "Fuente: pesos, cumplimiento y crecimiento PiSA = Sell-In PiSA cierre jun-26 (5 mercados); EBITDA y % del EBITDA total = Estado de Resultados Farma MX v18 (Finanzas, acumulado ene-jun-26) con split del bloque Gobierno por Gross2Net; crecimiento de mercado por segmento en su propia fuente (Knobloch / INEFAM / IQVIA)"; derecha: "PiSA Confidencial | 6".

Reglas estrictas: NO agregues columna de semáforo ni círculos de estatus; el color vive solo en las columnas de crecimiento; los placeholders entre corchetes se dibujan literales en gris, sin rellenar. La columna "% del EBITDA total" es porcentaje del EBITDA, no de la venta; la columna "Margen 1S25" es el margen EBITDA del año anterior. El símbolo $ no se repite por celda (lo declara el encabezado). Ningún elemento dorado; ningún verde. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT o SO WHAT; sin borde izquierdo; sin gradientes ni sombras infladas; español con acentos; título sin punto final.
```


---

# Lámina 7 · Somos #1 en los cuatro modelos, pero cada uno tiene un villano distinto que exige armas distintas
- **Momento:** M1 · Mapa del negocio y boleta competitiva
- **Encabezado:** Somos #1 en los cuatro modelos, pero cada uno tiene un villano distinto que exige armas distintas
- **So-what subtitle:** Dónde ganamos, dónde se erosiona el valor y quién es el rival por segmento; el down-trading ya nos costó −$197.9M en Retail
- **Layout:** Banda de título 16% + boleta de cuatro columnas 76% (una columna por segmento, gutter 0.15in) + footer 8%. Márgenes 0.5in; 13.333 × 7.5 in. Cada columna con top border 2 pt `#0F4C81` (permitido; prohibido border-left).

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 28-32 pt `#0F2845` (2 líneas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.
- Separador 0.5 pt `#E5E9EE`.

### Zona B — Boleta de cuatro columnas (76%)
Cuatro columnas de igual ancho (~2.95 in cada una). Cada columna arranca con top border 2 pt `#0F4C81` y adentro tres bloques verticales:
1. **Nombre del segmento** — Calibri bold 14 pt `#0F2845`.
2. **Dónde ganamos** (micro-título texto plano Calibri bold 10.5 pt `#0F2845`) + cuerpo Calibri Light 10 pt `#3D4A5F`.
3. **Villano** (micro-título texto plano Calibri bold 10.5 pt `#0F2845`) + cuerpo Calibri Light 10 pt `#3D4A5F`.

**Columna 1 — Retail**
- Dónde ganamos: "#1 en RX: 16.3% de share en unidades y 14.5% en valores (el #2 trae 12.3%). Marca propia ~50% de share en cadenas nacionales y ~41% del mercado direccionable (#2 con 9%). [shares por validar contra Knobloch, con unidad y base rotuladas: CC/DS]"
- Villano: "La migración de valor a volumen, ahora medida: el down-trading nos costó −$197.9M en el semestre (puente v4). Ganamos share, pierde el pastel."

**Columna 2 — Gobierno**
- Dónde ganamos: "#1 en volumen del sector público (82.5M de piezas, INEFAM). En nuestra canasta de 105 claves el mercado cae −31.7% y PiSA sube a 42.7% de participación (+17.7 pts). Defendimos el valor comprando volumen: −$320.3M de deflación de licitación compensados con +$425.2M de piezas (puente en L18)."
- Villano: "Un cliente subfinanciado que ejecuta mal y paga tarde. Amenaza estructural nueva: India entra a inyectables vía reliance regulatorio (292 autorizaciones Cofepris oct-nov-25)."

**Columna 3 — Hospitales**
- Dónde ganamos: "Proveedor #1 del hospital privado (~45% de los inyectables [validar, con unidad y base rotuladas: CC/DS]); share estable hace años."
- Villano: "Tres frentes: Mindray en terapia de infusión (la carta de entrada al hospital, $1,473M de línea), Baxter/Vantive en soluciones (el negocio base) y Kener en inyectables (~$1,000M hoy, meta ~$5,000M al 2030, estimación propia de la industria)."

**Columna 4 — Servicios**
- Dónde ganamos: "Líder en hemodiálisis y mezclas; únicos en nutrición. En diálisis peritoneal pública tenemos 31% de los pacientes contra 69% de Baxter/Vantive (en IMSS 42/58)."
- Villano: "En SIA el líder es Biossmann, ~4 veces nuestro tamaño, pero concentrado en gobierno (85% de su venta): en el privado la brecha es menor. Villano de fondo: los centros de mezclas (COI y similares) en Onco."

- Cifra pivotal en GOLD: el "−$197.9M" del down-trading (columna Retail, bloque Villano), Calibri bold `#C5A55A`. Es el único villano ya medido en pesos y el hallazgo nuevo del semestre. ÚNICO elemento gold de la lámina.

### Zona C — Footer (8%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 7".

## Mensaje que manda la lámina
PiSA es #1 en los cuatro modelos, pero cada uno se defiende contra un rival distinto: en Retail el enemigo es interno (el down-trading, ya medido en −$197.9M); en Gobierno es un cliente que ejecuta mal y no paga, más la entrada de India, y ahí defendimos el valor comprando volumen (−$320.3M de deflación vs +$425.2M de piezas); en Hospitales son tres frentes (Mindray, Baxter/Vantive, Kener); en Servicios es Baxter/Vantive en diálisis y los centros de mezclas en Onco. Un liderazgo, cuatro batallas distintas.

## Fuente (pie de lámina)
Fuente: Sell-In PiSA cierre jun-26; Knobloch MAT may-26 (shares retail, por confirmar CC); INEFAM (volumen y canasta sector público); IQVIA y estimación propia de la industria (Hospitales); deck del canal Servicios (diálisis peritoneal vs Baxter/Vantive, SIA); down-trading y puente Gobierno FC = matriz consolidada Downtrading FINAL 16-jul; India = 292 autorizaciones Cofepris oct-nov-25

## Estado del dato
- Down-trading −$197.9M: **en mano** (matriz consolidada Downtrading FINAL 16-jul; cifra central del rango, se mantiene por instrucción de Rafael 16-jul).
- Gobierno FC, matiz de volumen comprado (Precio −$320.3M / Volumen +$425.2M): **en mano** (matriz consolidada FINAL 16-jul, idéntico en 3 niveles); el detalle del puente vive en L18 y aquí solo se referencia.
- Diálisis peritoneal pública 31% vs 69% (IMSS 42/58): **en mano** (deck canal Servicios).
- India reliance (292 autorizaciones Cofepris oct-nov-25): **en mano** (research citable).
- Gobierno canasta 105 claves (mercado −31.7%, PiSA 42.7%, +17.7 pts) y 82.5M piezas INEFAM: **en mano** (v6).
- Kener (~$1,000M hoy, meta ~$5,000M 2030): **estimación propia declarada** (sin cifras públicas).
- Terapia de infusión $1,473M (línea Mindray): **en mano** (deck canal Hospitales).
- Shares retail (16.3% uds / 14.5% val; MP ~50% / ~41%) y ~45% inyectables hospital: **por validar [CC/DS]** — se citaron en revisión interna; validar antes de imprimir Y rotular unidad y base de cada share (uds vs valores; universo Knobloch vs direccionable). Sin unidad y base rotuladas, el share no se imprime.

## Notas para el dibujante
- Es una boleta comparativa: cuatro columnas paralelas, misma estructura ("Dónde ganamos" / "Villano"). Los micro-títulos "Dónde ganamos" y "Villano" son texto plano navy (contenido del deck), NO etiquetas de caja tipo INSIGHT/SO WHAT; no llevan fondo ni marco.
- "Villano" es vocabulario del deck ("quién es el villano"): se imprime como micro-título de contenido, no como badge de color.
- Placeholders literales, gris neutro `#8A95A8`: "[shares por validar contra Knobloch, con unidad y base rotuladas: CC/DS]" y "[validar, con unidad y base rotuladas: CC/DS]" del ~45% hospitalario. No rellenar. Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27]: se elimina antes de la sesión.
- Kener se presenta explícitamente como "estimación propia de la industria": esa frase viaja con el número, no se borra.
- El único gold es "−$197.9M" (down-trading, Retail). Ninguna otra cifra en gold; los demás villanos en gris/navy neutro.
- Separación entre columnas: top border 2 pt `#0F4C81` sobre cada columna, sin bordes laterales. Sin sombras infladas, sin gradientes.
- Sin logos de competidores (Mindray, Baxter/Vantive, Kener, Biossmann van como texto). Tabular figures en cifras.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; números en figuras tabulares; signo menos tipográfico "−", "+" explícito.

BANDA DE TÍTULO (arriba, ~16%): título grande navy #0F2845 en peso ligero, hasta dos líneas: "Somos #1 en los cuatro modelos, pero cada uno tiene un villano distinto que exige armas distintas". Debajo, itálica gris azulado #44546A: "Dónde ganamos, dónde se erosiona el valor y quién es el rival por segmento; el down-trading ya nos costó −$197.9M en Retail". Línea fina gris #E5E9EE de margen a margen.

CUERPO en CUATRO columnas de igual ancho (una por segmento), separadas por espacio en blanco. Cada columna tiene una línea superior gruesa azul #0F4C81 (sin bordes laterales) y adentro, de arriba a abajo: el nombre del segmento en navy #0F2845 negrita mediano; un micro-título "Dónde ganamos" en navy #0F2845 negrita pequeño y debajo un párrafo gris #3D4A5F pequeño; un micro-título "Villano" en navy #0F2845 negrita pequeño y debajo otro párrafo gris #3D4A5F pequeño.

COLUMNA 1 — "Retail".
Dónde ganamos: "#1 en RX: 16.3% de share en unidades y 14.5% en valores (el #2 trae 12.3%). Marca propia ~50% de share en cadenas nacionales y ~41% del mercado direccionable (#2 con 9%). [shares por validar contra Knobloch, con unidad y base rotuladas: CC/DS]"
Villano: "La migración de valor a volumen, ahora medida: el down-trading nos costó −$197.9M en el semestre (puente v4). Ganamos share, pierde el pastel." (El monto "−$197.9M" va en negrita color dorado #C5A55A; es el ÚNICO elemento dorado de la lámina.)

COLUMNA 2 — "Gobierno".
Dónde ganamos: "#1 en volumen del sector público (82.5M de piezas, INEFAM). En nuestra canasta de 105 claves el mercado cae −31.7% y PiSA sube a 42.7% de participación (+17.7 pts). Defendimos el valor comprando volumen: −$320.3M de deflación de licitación compensados con +$425.2M de piezas (puente en L18)."
Villano: "Un cliente subfinanciado que ejecuta mal y paga tarde. Amenaza estructural nueva: India entra a inyectables vía reliance regulatorio (292 autorizaciones Cofepris oct-nov-25)."

COLUMNA 3 — "Hospitales".
Dónde ganamos: "Proveedor #1 del hospital privado (~45% de los inyectables [validar, con unidad y base rotuladas: CC/DS]); share estable hace años."
Villano: "Tres frentes: Mindray en terapia de infusión (la carta de entrada al hospital, $1,473M de línea), Baxter/Vantive en soluciones (el negocio base) y Kener en inyectables (~$1,000M hoy, meta ~$5,000M al 2030, estimación propia de la industria)."

COLUMNA 4 — "Servicios".
Dónde ganamos: "Líder en hemodiálisis y mezclas; únicos en nutrición. En diálisis peritoneal pública tenemos 31% de los pacientes contra 69% de Baxter/Vantive (en IMSS 42/58)."
Villano: "En SIA el líder es Biossmann, ~4 veces nuestro tamaño, pero concentrado en gobierno (85% de su venta): en el privado la brecha es menor. Villano de fondo: los centros de mezclas (COI y similares) en Onco."

PIE (~8%): línea fina gris #E5E9EE; debajo, gris #8A95A8 pequeño, izquierda en itálica: "Fuente: Sell-In PiSA cierre jun-26; Knobloch MAT may-26 (shares retail, por confirmar CC); INEFAM (volumen y canasta sector público); IQVIA y estimación propia de la industria (Hospitales); deck del canal Servicios (diálisis peritoneal vs Baxter/Vantive, SIA); down-trading y puente Gobierno FC = matriz consolidada Downtrading FINAL 16-jul; India = 292 autorizaciones Cofepris oct-nov-25"; derecha: "PiSA Confidencial | 7".

Reglas estrictas: los micro-títulos "Dónde ganamos" y "Villano" son texto plano navy de contenido, NO etiquetas de caja ni badges de color; los corchetes "[shares por validar contra Knobloch, con unidad y base rotuladas: CC/DS]" y "[validar, con unidad y base rotuladas: CC/DS]" se dibujan literales en gris (son placeholders internos del borrador; se eliminarán antes de la versión final); la única cifra dorada es "−$197.9M". Sin logos de competidores (van como texto). Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT o SO WHAT; sin borde izquierdo; sin gradientes ni sombras infladas; sin rayas largas (em-dash) en la prosa; español con acentos; título sin punto final.
```


---

# Lámina 8 · PiSA creció +$239.3M (+1.5%) en H1-2026, pero el mix erosionó −$297.0M: el crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core
- **Momento:** M2 · PiSA total: qué pasó en el 1S
- **Encabezado:** PiSA creció +$239.3M (+1.5%) en H1-2026, pero el mix erosionó −$297.0M: el crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core
- **So-what subtitle:** Puente 1S-2025 a 1S-2026: Δ reclasificada +$272.1M concilia a +$239.3M de sell-in oficial (de $16,279.2M a $16,518.5M); el PVM del core aporta +$51.7M, prácticamente plano
- **Layout:** Banda de título 14% + cuerpo 78% en tres columnas 15 / 50 / 35 (A: dos tiles numéricos mercado / PiSA · B: puente TOTAL de 8 componentes con conciliación de 3 niveles · C: palancas comerciales 1S25 vs 1S26) + footer 8%. Márgenes 0.5in; 13.333 × 7.5 in. Gutter 0.15in entre columnas.
- **Naturaleza:** el puente de la columna B ya es REAL (matriz consolidada Downtrading FINAL 16-jul, verificada al peso; CONTROL 0.0000). Se acabaron las siluetas placeholder: los 8 componentes se dibujan con su valor y la cascada cierra en la conciliación de 3 niveles.

## Zona por zona

### Zona A — Banda de título (14%)
- Título: Calibri Light 26-30 pt `#0F2845` (2 líneas).
- Subtítulo so-what: Calibri Light 13-14 pt italic `#44546A`.
- Separador 0.5 pt `#E5E9EE`.

### Zona B — Columna 1 (15%) · Dos tiles numéricos (sin barras comparadas)
- Micro-título de zona: "Mercado vs PiSA" — Calibri bold 12 pt `#0F2845` (texto plano).
- DOS tiles apilados, cada uno un rectángulo tenue fondo `#FAFBFC` contorno 0.5 pt `#E5E9EE` (sin border-left), con su propio eyebrow de universo. NO se dibujan barras comparadas: los universos y periodos no son homologables todavía.
  - Tile 1 "Mercado": eyebrow Calibri Light 9 pt `#5A6679` "INEFAM". Valor central: el chip literal "[comparador por elegir: CC]" en gris `#8A95A8`, Calibri Light 12 pt. Nota al pie del tile, 9 pt `#5A6679`: "Referencia año completo 2025: mercado +9.2% valor · −2.4% volumen (INEFAM); no comparable 1S contra 1S sin el corte."
  - Tile 2 "PiSA": eyebrow "Sell-in 1S26 vs 1S25". Valor central: "+1.5%" Calibri bold 24 pt `#0F2845`, con "+$239.3M" debajo en Calibri Light 11 pt `#3D4A5F`.

### Zona C — Columna 2 (50%) · Puente TOTAL PiSA 1S-2025 a 1S-2026, ocho componentes (REAL)
- Micro-título de zona: "El puente en ocho componentes" — Calibri bold 12 pt `#0F2845`.
- Eyebrow de universo, Calibri Light 9 pt `#5A6679`: "Sell-in PiSA · matriz consolidada Downtrading FINAL 16-jul · control = 0".
- Waterfall REAL, escala "$M", eje Y desde 0, connectors punteados 0.5 pt `#C5CDD9`, data label con signo sobre cada barra. Barras de izquierda a derecha:
  - Barra ancla inicial: **1S-2025 = $16,279.2M** — navy `#0F2845`.
  - Ocho barras de componente:
    1. "Precio" — **+66.9** — navy `#0F4C81` (hacia arriba).
    2. "Volumen" — **+281.8** — navy `#0F4C81` (hacia arriba, la mayor positiva).
    3. "Mix / down-trading (core PiSA)" — **−297.0** — rojo `#C00000` (hacia abajo, la barra villana, la mayor del puente).
    4. "Gestión de portafolio" — **+28.0** — navy `#0F4C81`.
    5. "Lanzamientos" — **+94.4** — navy `#0F4C81`.
    6. "Terceros / VARIOS" — **+95.5** — navy `#0F4C81`.
    7. "Servicios / serie 9" — **+51.8** — navy `#0F4C81`.
    8. "Sin unidad (por valor)" — **−49.4** — rojo `#C00000`.
  - Llave/corchete horizontal sobre las 8 barras, Calibri Light 10 pt `#3D4A5F`: "Δ reclasificada +$272.1M".
  - Dos barras de conciliación en GRIS `#C5CDD9` (contorno `#8A95A8`, etiqueta gris; conciliación contable, no desempeño): "Reclas. nov-dic-25" **−31.7** (con tick intermedio "Δ con MATNR +$240.3M" en 9 pt `#8A95A8`) y "Sin MATNR" **−1.0**.
  - Barra ancla final: **1S-2026 = $16,518.5M** — navy `#0F2845`.
- Etiqueta del delta oficial, Calibri bold 13 pt `#C5A55A` (gold): "+$239.3M (+1.5%) sell-in oficial" — junto a la barra ancla final. ÚNICO elemento gold de la lámina.
- Anotación PVM core (una línea), Calibri Light 10 pt `#3D4A5F`: "Precio + volumen + mix del core = +$51.7M, prácticamente plano: el crecimiento vive en lanzamientos (+$94.4M), terceros (+$95.5M) y servicios (+$51.8M)."
- Nota técnica de cobertura (una línea), Calibri Light 9 pt `#8A95A8`: "P/V/M sobre el core medible: Privado 96.0% del bruto, Hospitales 65.0% y Gob FC 78.9% del bruto elegible; Gob Servicios entra por valor."

### Zona D — Columna 3 (35%) · Palancas comerciales 1S-2025 vs 1S-2026 (niveles, no escalones)
- Micro-título de zona: "Palancas comerciales, niveles lado a lado" — Calibri bold 12 pt `#0F2845`.
- Cuatro renglones, cada uno con barras horizontales pares 1S25 (`#8A95A8`) vs 1S26 (`#0F4C81`), rótulos Calibri Light 10 pt `#3D4A5F`, valores tabulares. Los renglones 1-2 llevan eyebrow "DP / pedidos"; los renglones 3-4 llevan eyebrow "Gross2Net Finanzas" (universos distintos, declarados, sin mezclarse en una misma gráfica):
  1. **Venta perdida (Privado + Hospitales):** $548M a $470M — mejora −14%. Chip: "[gobierno: definición única pendiente]".
  2. **PIN no solicitado (Privado + Hospitales):** $645M a $635M — −2%. Chip: "[gobierno: pendiente]".
  3. **NC comerciales y sanciones (total PiSA):** −$553.8M a −$625.4M — empeora $71.6M (delta en rojo `#C00000`).
  4. **Devoluciones (total PiSA):** −$1,024.6M a −$849.4M — mejora −17.1% (delta en navy bold `#0F4C81`, sin verde).

### Zona E — Footer (8%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 8".

## Mensaje que manda la lámina
El +$239.3M (+1.5%) de PiSA en el 1S no vino del portafolio core: precio, volumen y mix del core netean +$51.7M, prácticamente plano, porque el mix erosionó −$297.0M todo lo que el volumen (+$281.8M) y el precio (+$66.9M) construyeron. El crecimiento real lo pusieron los lanzamientos (+$94.4M), la distribución de terceros (+$95.5M) y los servicios (+$51.8M). Las palancas comerciales de la derecha muestran, a nivel, dónde se ganó y perdió ejecución: mejoran venta perdida y devoluciones, empeoran las NC comerciales.

## Fuente (pie de lámina)
Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In PiSA cierre jun-26 (Δ reclasificada +$272.1M; conciliación a +$239.3M sell-in oficial); NC y devoluciones: Gross2Net Finanzas 1S26 vs 1S25; venta perdida y PIN: DP y áreas comerciales (gobierno pendiente de definición única); mercado: INEFAM 2025 [comparador del 1S por elegir: CC]

## Estado del dato
- Total +$239.3M; anclas 1S-2025 $16,279.2M y 1S-2026 $16,518.5M: **en mano** (sell-in; 16,518.5 − 16,279.2 = 239.3, recomputado de primera mano en el EXTRACT, CONTROL 0.0000).
- Los 8 componentes del puente (Precio +66.9 / Volumen +281.8 / Mix −297.0 / Gestión +28.0 / Lanzamientos +94.4 / Terceros +95.5 / Servicios +51.8 / Sin unidad −49.4 = +272.1): **en mano y verificados al peso** (matriz consolidada Downtrading FINAL 16-jul; EXTRACT_puentes_consolidado_gobserv.md, 0 desviaciones). SUPERSEDE las 5 siluetas placeholder "[dato: equipo PVM]" de la versión anterior.
- Conciliación de 3 niveles: +272.1 − 31.7 (reclas. nov-dic-25) = +240.3 con MATNR − 1.0 (sin MATNR) = +239.3 sell-in oficial: **en mano** (verificada al 4º decimal: 272.0654 − 31.7200 = 240.3454 − 1.0434 = 239.3020).
- Redondeo declarado: las sumas visibles a 1 decimal pueden diferir ±$0.1M entre pasos (p. ej. 272.1 − 31.7 = 240.4 visible vs 240.3 canónico; los 8 componentes a 1 decimal suman 272.0 vs 272.1 canónico; 16,279.2 + 272.1 − 31.7 − 1.0 = 16,518.6 visible vs ancla 16,518.5); el workbook cierra al 4º decimal con CONTROL 0.0000. Se imprimen los niveles canónicos (272.1 / 240.3 / 239.3), no las restas visibles.
- PVM core +$51.7M (66.9 + 281.8 − 297.0): **en mano** (EXTRACT lo confirma como +51.71).
- Venta perdida $548M a $470M (Privado + Hospitales, −14%) y PIN $645M a $635M (−2%): **en mano** (tabla canónica Rafael 16-jul); gobierno **pendiente de definición única** (chip declarado). SUPERSEDE el par $758.8M a $901.9M de la versión anterior (incluía gobierno con definición no única) y el "PIN $635M sin comparador" (el comparador 2025 ya existe: $645M).
- NC comerciales y sanciones −$553.8M a −$625.4M y Devoluciones −$1,024.6M a −$849.4M (−17.1%): **en mano** (Gross2Net). La línea "NC logísticas" NO existe en la taxonomía real: el renglón "[−$100M candidato: RC]" de la versión anterior se elimina.
- Validación 2-vías (volumen −$830.7M / precio+mezcla +$1,070.0M / piezas −5.1%): sigue siendo cierta pero se difiere a anexo (ver Contenido diferido): su "volumen" a precio constante total no es el mismo concepto que el "Volumen +281.8" intra-molécula de la matriz y en la misma lámina confunde.
- Mercado 2025 +9.2% valor / −2.4% volumen (INEFAM): **en mano**; comparador del 1S por elegir **[CC]**.

## Notas para el dibujante
- El waterfall es REAL: ocho barras con valor + dos barras grises de conciliación. Proporciones relativas de las barras de componente (magnitud): Mix −297.0 es la barra más grande del puente; Volumen +281.8 casi igual de grande hacia arriba; Lanzamientos +94.4 y Terceros +95.5 medianas y prácticamente iguales; Precio +66.9 y Servicios +51.8 algo menores; Sin unidad −49.4 pequeña; Gestión +28.0 la más chica. Las conciliaciones −31.7 y −1.0 son mínimas (la de −1.0 casi un filo).
- SIN verde en ninguna barra: positivos en navy `#0F4C81`, negativos en rojo `#C00000`, anclas en navy `#0F2845`, conciliaciones en gris `#C5CDD9` (son contabilidad, no desempeño; no pintarlas de rojo).
- El único gold es "+$239.3M (+1.5%) sell-in oficial". La Δ reclasificada +$272.1M NUNCA va en gold ni se cita sola: siempre con su conciliación visible (caveat de citación del README).
- La columna 1 son DOS TILES numéricos, no barras: prohibido dibujar una gráfica comparando mercado vs PiSA (el comparador del 1S no está elegido).
- La col 3 son NIVELES lado a lado, NO escalones del waterfall. Renglones 1-2 y 3-4 viven en universos distintos (DP/pedidos vs Gross2Net): cada par con su eyebrow, sin conectar entre sí ni con el puente.
- En el renglón de devoluciones, 1S26 (−849.4) se dibuja MÁS CORTA que 1S25 (−1,024.6): es una mejora. En NC, 1S26 (−625.4) MÁS LARGA que 1S25 (−553.8): empeora.
- Todos los corchetes se dibujan literales, gris neutro `#8A95A8`: "[comparador por elegir: CC]", "[gobierno: definición única pendiente]", "[gobierno: pendiente]". Los corchetes con responsable son PLACEHOLDER INTERNO — kill antes del 27: viven en el storyboard de revisión, no en la versión del Consejo.
- El título es de Rafael (16-jul) y usa "H1-2026"; se respeta verbatim aunque el resto del deck diga "1S-2026" (flageado al orquestador).
- Sin caja de insight; micro-títulos de zona en texto plano navy; sin border-left; sin verde celebratorio; ningún carácter de flecha. Tabular figures en todo número; unidades "$M" declaradas en el eje.

### Contenido diferido a anexo
- A ANEXO: validación 2-vías del total — "Validación 2-vías: volumen −$830.7M · precio y mezcla +$1,070.0M (piezas −5.1%); descomposición gruesa a precio constante, consistente con el cierre +$239.3M. La matriz de 8 componentes es el desglose fino; su línea 'Volumen +281.8' es volumen intra-molécula del core, no el mismo concepto." Se difiere porque en la misma lámina los dos "volumen" con signo opuesto confunden al Consejo.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; números en figuras tabulares; signo menos tipográfico "−", "+" explícito.

BANDA DE TÍTULO (arriba, ~14%): título grande navy #0F2845 en peso ligero, hasta dos líneas: "PiSA creció +$239.3M (+1.5%) en H1-2026, pero el mix erosionó −$297.0M: el crecimiento viene de lanzamientos, servicios y distribución, no del portafolio core". Debajo, itálica gris azulado #44546A: "Puente 1S-2025 a 1S-2026: Δ reclasificada +$272.1M concilia a +$239.3M de sell-in oficial (de $16,279.2M a $16,518.5M); el PVM del core aporta +$51.7M, prácticamente plano". Línea fina gris #E5E9EE de margen a margen.

CUERPO en TRES columnas de anchos 15% / 50% / 35%.

COLUMNA IZQUIERDA (15%) — arriba, texto plano navy #0F2845 negrita: "Mercado vs PiSA". Debajo, DOS recuadros apilados con fondo gris muy claro #FAFBFC y contorno fino gris #E5E9EE (sin barra lateral de color), SIN gráficas de barras:
Recuadro 1: arriba en gris #5A6679 muy pequeño "INEFAM"; al centro el chip literal en gris #8A95A8: "[comparador por elegir: CC]"; abajo en gris #5A6679 muy pequeño: "Referencia año completo 2025: mercado +9.2% valor · −2.4% volumen (INEFAM); no comparable 1S contra 1S sin el corte."
Recuadro 2: arriba en gris #5A6679 muy pequeño "Sell-in 1S26 vs 1S25"; al centro, grande y en negrita navy #0F2845: "+1.5%"; debajo en gris #3D4A5F: "+$239.3M".

COLUMNA CENTRAL (50%) — arriba, texto plano navy #0F2845 negrita: "El puente en ocho componentes". Debajo, en gris #5A6679 muy pequeño: "Sell-in PiSA · matriz consolidada Downtrading FINAL 16-jul · control = 0". Debajo, una gráfica de cascada (waterfall) REAL con eje Y desde 0, escala "$M", conectores punteados finos gris #C5CDD9 y etiqueta de valor con signo sobre cada barra. De izquierda a derecha:
1. Barra ancla "1S-2025" = "16,279.2" — alta, navy oscuro #0F2845.
2. "Precio" = "+66.9" — positiva, azul #0F4C81, mediana-chica.
3. "Volumen" = "+281.8" — positiva, azul #0F4C81, la positiva MÁS GRANDE.
4. "Mix / down-trading (core PiSA)" = "−297.0" — negativa, roja #C00000, la barra MÁS GRANDE de todo el puente.
5. "Gestión de portafolio" = "+28.0" — positiva, azul #0F4C81, la más chica.
6. "Lanzamientos" = "+94.4" — positiva, azul #0F4C81, mediana.
7. "Terceros / VARIOS" = "+95.5" — positiva, azul #0F4C81, mediana (casi igual a la anterior).
8. "Servicios / serie 9" = "+51.8" — positiva, azul #0F4C81, mediana-chica.
9. "Sin unidad (por valor)" = "−49.4" — negativa, roja #C00000, chica.
Sobre estas ocho barras de componente, una llave horizontal rotulada en gris #3D4A5F: "Δ reclasificada +$272.1M".
10. "Reclas. nov-dic-25" = "−31.7" — barra GRIS claro #C5CDD9 con contorno gris #8A95A8 (conciliación contable, no roja), con un tick pequeño en gris #8A95A8: "Δ con MATNR +$240.3M".
11. "Sin MATNR" = "−1.0" — barra gris #C5CDD9 casi un filo.
12. Barra ancla "1S-2026" = "16,518.5" — alta, navy oscuro #0F2845. Junto a ella, en negrita color DORADO #C5A55A: "+$239.3M (+1.5%) sell-in oficial" (ÚNICO elemento dorado de la lámina).
Bajo el chart, dos líneas: en gris #3D4A5F "Precio + volumen + mix del core = +$51.7M, prácticamente plano: el crecimiento vive en lanzamientos (+$94.4M), terceros (+$95.5M) y servicios (+$51.8M)."; y en gris #8A95A8 más pequeño "P/V/M sobre el core medible: Privado 96.0% del bruto, Hospitales 65.0% y Gob FC 78.9% del bruto elegible; Gob Servicios entra por valor."

COLUMNA DERECHA (35%) — arriba, texto plano navy #0F2845 negrita: "Palancas comerciales, niveles lado a lado". Debajo, cuatro renglones, cada uno con dos barras horizontales pares (1S25 en gris #8A95A8, 1S26 en azul #0F4C81) y su etiqueta:
1. Eyebrow gris muy pequeño "DP / pedidos". "Venta perdida (Privado + Hospitales)": 1S25 "$548M", 1S26 "$470M" (la de 2026 MÁS CORTA: mejora −14%); chip literal gris #8A95A8 "[gobierno: definición única pendiente]".
2. "PIN no solicitado (Privado + Hospitales)": 1S25 "$645M", 1S26 "$635M" (apenas más corta, −2%); chip gris "[gobierno: pendiente]".
3. Eyebrow gris muy pequeño "Gross2Net Finanzas". "NC comerciales y sanciones (total PiSA)": 1S25 "−$553.8M", 1S26 "−$625.4M" (la de 2026 MÁS LARGA); etiqueta de delta en rojo #C00000: "empeora $71.6M".
4. "Devoluciones (total PiSA)": 1S25 "−$1,024.6M", 1S26 "−$849.4M" (la de 2026 claramente MÁS CORTA); etiqueta de delta en azul navy #0F4C81 negrita: "mejora −17.1%" (NO verde).

PIE (~8%): línea fina gris #E5E9EE; debajo, gris #8A95A8 pequeño, izquierda en itálica: "Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In PiSA cierre jun-26 (Δ reclasificada +$272.1M; conciliación a +$239.3M sell-in oficial); NC y devoluciones: Gross2Net Finanzas 1S26 vs 1S25; venta perdida y PIN: DP y áreas comerciales (gobierno pendiente de definición única); mercado: INEFAM 2025 [comparador del 1S por elegir: CC]"; derecha: "PiSA Confidencial | 8".

Reglas estrictas: el único elemento dorado es "+$239.3M (+1.5%) sell-in oficial"; la Δ reclasificada +$272.1M va en gris, nunca en dorado. NO usar verde en ninguna barra ni etiqueta: positivos en azul, negativos en rojo, conciliaciones en gris. La columna izquierda son tiles de texto, sin barras. La columna derecha son niveles lado a lado, no escalones del waterfall, y sus dos pares de renglones llevan universos distintos declarados. Todos los corchetes se dibujan literales en gris. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT o SO WHAT; sin borde izquierdo; sin gradientes ni sombras infladas; español con acentos; título sin punto final.
```


---

# Lamina 9 · El gap del 1S vive en Farmacias y Gobierno FC; Hospitales y Servicios crecen sin compensarlo
- **Momento:** M2 · PiSA total: qué pasó en el 1S
- **Encabezado:** El gap del 1S vive en Farmacias y Gobierno FC; Hospitales y Servicios crecen sin compensarlo
- **So-what subtitle:** Sell-in 1S-2026 contra meta por canal: $16,518.5M de $17,678.3M (93.4%, +1.5% vs 1S-2025)
- **Layout:** Banda de título 18% + tabla full-width 62% + caveat de universo 8% + footer 12%. Márgenes 0.5in. Tabla centrada, ancho útil completo (~12.3in).

## Zona por zona

### Zona A — Banda de título (18%)
- Título: Calibri Light 32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Tabla de desempeño por canal (62%)
- Tipo: tabla 8 filas de datos × 5 columnas (dentro del máximo 8×6). Header: fondo `#0F2845`, texto blanco Calibri bold 11 pt. Body: Calibri Light 11-12 pt `#3D4A5F`, filas alternas blanco / `#F0F3F7`, border inferior por fila 1 px `#E5E9EE`, sin líneas verticales, border externo 0.5 pt `#C5CDD9`. Tabular figures en TODA celda numérica.
- Columnas: "Canal (por segmento)" (izquierda) | "Venta ($M)" (derecha) | "Meta ($M)" (derecha) | "Cumplimiento" (derecha) | "Crec. vs 1S-2025" (derecha).
- Filas, con TODOS los valores (un decimal, coma de miles; deltas con signo explícito):

| Canal (por segmento) | Venta ($M) | Meta ($M) | Cumplimiento | Crec. vs 1S-2025 |
|---|---:|---:|---:|---:|
| Retail · Farmacias | 2,958.0 | 3,327.8 | 88.9% | −2.2% |
| Retail · Impulso | 2,785.8 | 2,921.1 | 95.4% | +1.8% |
| Retail · Expansión | 1,466.4 | 1,564.1 | 93.8% | +3.4% |
| **Retail (subtotal)** | **7,210.2** | **7,813.0** | **92.3%** | **+0.4%** |
| Gobierno · Frasco Cerrado | 4,034.3 | 4,484.9 | 90.0% | −0.6% |
| Hospitales | 3,054.5 | 3,207.1 | 95.2% | +5.1% |
| Servicios (Gob Servicios) | 2,219.4 | 2,173.3 | 102.1% | +4.0% |
| **PiSA (5 mercados)** | **16,518.5** | **17,678.3** | **93.4%** | **+1.5%** |

- Tratamiento de filas especiales:
  - "Retail (subtotal)": Calibri bold, fondo `#F0F3F7`, border-top 1 pt `#0F4C81`.
  - "PiSA (5 mercados)" (total): Calibri bold, fondo `#F0F3F7`, border-top 2 pt `#0F2845`.
- Colores de la columna "Crec. vs 1S-2025" (semáforo solo en deltas): negativos (−2.2%, −0.6%) en `#C00000` (danger_ppt); positivos (+1.8%, +3.4%, +0.4%, +5.1%, +4.0%, +1.5%) en `#2E7D4F` (success-500).
- Cifra pivotal en GOLD: el "88.9%" de Retail · Farmacias, Calibri bold `#C5A55A` — es la celda que concentra la historia del gap. ÚNICO elemento gold de la lámina.
- Columna "Cumplimiento": resto de valores en `#1A2332` neutro (NO semáforo: esta lámina sustituye al semáforo viejo, no lo replica).

### Zona C — Caveat de universo (8%)
- Tipo: texto de una línea, Calibri Light 9 pt `#8A95A8`: "La frontera FC/Servicios difiere ~$835M contra el universo neto; esta lámina usa siempre la frontera Sell-In. Diferencias de $0.1M por redondeo."

### Zona D — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 9".

- **Mensaje que manda la lamina:** El 93.4% no es una historia sino cuatro: Farmacias (88.9%, −2.2%) y Gobierno FC (90.0%, −0.6%) concentran el faltante, mientras Hospitales (+5.1%) y Servicios (+4.0%, único canal arriba de meta) crecen pero no alcanzan a compensar.
- **Fuente (pie de lamina):** Fuente: Sell-In PiSA, cierre jun-26 (1S-2026), 5 mercados; apertura por canal según los segmentos de la lámina 6
- **Estado del dato:** En mano (las 8 filas cuadran: Retail 2,958.0+2,785.8+1,466.4 = 7,210.2; total 7,210.2+4,034.3+3,054.5+2,219.4 = 16,518.4 vs 16,518.5 impreso, $0.1M de redondeo declarado en Zona C; metas suman 17,678.3 exacto). Consistente con el paquete canónico 16-jul: sell-in oficial 1S = $16,518.5M (+1.5%, de $16,279.2M). Caveat de Zona C verificado y se conserva: la frontera FC/Servicios de esta lámina es SIEMPRE la del Sell-In (~$835M contra el universo neto); no mezclar con la frontera Gross2Net del EBITDA.
- **Notas para el dibujante:**
  - NO agregar columna de semáforo (círculos rojo/verde) ni iconos de estatus: esta lámina sustituye deliberadamente al semáforo. El color vive solo en la columna de crecimiento y el gold en 88.9%. Verificación 16-jul: el ÚNICO gold de la lámina es la celda 88.9%; si algún render agrega otro gold, se rechaza.
  - Todo corchete con responsable (el pendiente [RC/CC] del consolidado, si Rafael decide declararlo) es [PLACEHOLDER INTERNO - kill antes del 27].
  - No agregar el 2-vías (volumen −$830.7M / precio+mezcla +$1,070.0M): esa física vive en la lámina 8 (puente rectora), no aquí. Una idea por lámina.
  - El símbolo $ no se repite por celda: el header "($M)" lo declara.
  - Signo menos tipográfico "−" (no guion) en los negativos; signo "+" explícito en positivos.
  - Sin caja de insight. Universo: sell-in exclusivamente; prohibido meter cualquier dato de mercado (Knobloch/INEFAM/IQVIA) en esta tabla.
  - Pendiente NO imprimible que existe alrededor de esta lámina: el alcance del consolidado (~$2.0B de segmentos no desglosados fuera de los 5 mercados) está por cerrar [RC/CC]; si Rafael decide declararlo, iría como segunda línea del caveat de Zona C, nunca como fila de la tabla.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares alineados a la derecha. Cuatro bandas horizontales apiladas; el centro lo domina una tabla de ancho completo.

BANDA 1 (18% superior, título): título grande navy #0F2845 en peso ligero (puede ocupar dos líneas): "El gap del 1S vive en Farmacias y Gobierno FC; Hospitales y Servicios crecen sin compensarlo". Debajo, subtítulo en itálica gris #44546A: "Sell-in 1S-2026 contra meta por canal: $16,518.5M de $17,678.3M (93.4%, +1.5% vs 1S-2025)".

BANDA 2 (62%, tabla de desempeño por canal, ancho completo). Encabezado con fondo navy #0F2845 y texto blanco en negrita; 5 columnas: "Canal (por segmento)" (alineada a la izquierda) | "Venta ($M)" (derecha) | "Meta ($M)" (derecha) | "Cumplimiento" (derecha) | "Crec. vs 1S-2025" (derecha). Cuerpo en gris #3D4A5F, filas alternando blanco y gris muy claro #F0F3F7, con línea inferior fina gris #E5E9EE por fila, SIN líneas verticales. Filas en este orden:
Retail · Farmacias | 2,958.0 | 3,327.8 | 88.9% | −2.2%
Retail · Impulso | 2,785.8 | 2,921.1 | 95.4% | +1.8%
Retail · Expansión | 1,466.4 | 1,564.1 | 93.8% | +3.4%
Retail (subtotal) | 7,210.2 | 7,813.0 | 92.3% | +0.4%   (esta fila en negrita, fondo gris #F0F3F7, con línea superior azul #0F4C81)
Gobierno · Frasco Cerrado | 4,034.3 | 4,484.9 | 90.0% | −0.6%
Hospitales | 3,054.5 | 3,207.1 | 95.2% | +5.1%
Servicios (Gob Servicios) | 2,219.4 | 2,173.3 | 102.1% | +4.0%
PiSA (5 mercados) | 16,518.5 | 17,678.3 | 93.4% | +1.5%   (fila total en negrita, fondo gris #F0F3F7, con línea superior gruesa navy #0F2845)
Color de la columna "Crec. vs 1S-2025" (semáforo solo aquí): los valores negativos "−2.2%" y "−0.6%" en rojo #C00000; todos los positivos "+1.8%, +3.4%, +0.4%, +5.1%, +4.0%, +1.5%" en verde #2E7D4F. Usa el signo menos tipográfico "−", no un guion. La columna "Cumplimiento" va toda en gris neutro #1A2332 SIN color de semáforo, EXCEPTO una única celda pivotal: el "88.9%" de la fila "Retail · Farmacias" va en negrita color dorado #C5A55A (es el único elemento dorado de la lámina).

BANDA 3 (8%, caveat de universo): una sola línea chica en gris claro #8A95A8: "La frontera FC/Servicios difiere ~$835M contra el universo neto; esta lámina usa siempre la frontera Sell-In. Diferencias de $0.1M por redondeo."

BANDA 4 (12% inferior, pie): línea divisoria gris #E5E9EE; debajo, en gris claro #8A95A8 chico, a la izquierda: "Fuente: Sell-In PiSA, cierre jun-26 (1S-2026), 5 mercados; apertura por canal según los segmentos de la lámina 6"; a la derecha: "PiSA Confidencial | 9".

Reglas estrictas: NO agregues columna de semáforo ni círculos rojo/verde ni iconos de estatus; el color solo vive en la columna de crecimiento y el dorado solo en la celda 88.9%. El signo $ no se repite por celda (lo declara el encabezado "($M)"). Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; español con acentos; título sin punto final.
```


---

# Lamina 10 · Dos segmentos restan y dos suman; los que suman no compensan, y la cadena de suministro ya entregó su parte
- **Momento:** M2 · PiSA total: qué pasó en el 1S
- **Encabezado:** Dos segmentos restan y dos suman; los que suman no compensan, y la cadena de suministro ya entregó su parte
- **So-what subtitle:** El 93.4% son cuatro historias, no una; el cuello de botella del semestre se movió del abasto a la demanda
- **Layout:** Banda de título 16% + línea de síntesis (UNA línea; comprime la vieja franja de 4 tiles que repetía la L9) 8% + fila de reconocimiento a cadena (4 tiles KPI) 44% + banda de transición al 2S 10% + caveat 8% + footer 14%. Márgenes 0.5in.

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Línea de síntesis: cuatro historias en UNA línea (8%)
- UNA sola línea de texto (puede correr a 2 renglones visuales), Calibri Light 13 pt `#1A2332`, cumplimientos en Calibri bold navy `#0F2845`, sin tiles, sin tabla: "El 93.4% son cuatro historias: restan Retail (92.3%, vía Farmacias) y Gobierno FC (90.0%); suman Hospitales (95.2%) y Servicios (102.1%), sin alcanzar a compensar."
- Regla de color: los cuatro cumplimientos en navy neutro, SIN semáforo, SIN verde. Esta línea NO repite la tabla de la L9 (comprimida por instrucción 16-jul); el detalle vive en la L9.

### Zona C — Reconocimiento a la cadena de suministro (44%)
- Kicker de zona: "La cadena de suministro entregó su parte en el 1S" — Calibri bold 12 pt `#0F2845`. (La lectura "se dice como logro, no como excusa" es instrucción de SPEAKER: vive en Notas, NO se imprime.)
- Cuatro tiles KPI en fila (separación border 0.5 pt `#E5E9EE`, sin fondo). Valor grande arriba, etiqueta/definición debajo (Calibri Light 10 pt `#5A6679`), y estado del dato al pie del tile (Calibri Light 9 pt `#8A95A8`).
- Jerarquía tipográfica 16-jul: el valor en mano (fill rate) va Calibri bold 24 pt; los tres candidatos van UN NIVEL ABAJO, Calibri bold 18 pt gris `#8A95A8` (siguen siendo placeholders, no compiten con la métrica en mano).
  - Tile 1 — "Producto negado": valor "[candidato: de 640 a 78]" (Calibri bold 18 pt `#8A95A8`, gris de placeholder) · etiqueta "de abril a junio" · pie "[validar unidad, claves vs miles de piezas: FM]".
  - Tile 2 — "Fill rate": valor "95-96%" (Calibri bold 24 pt GOLD `#C5A55A` — ÚNICO elemento gold de la lámina; es la única métrica en mano y el ancla del reconocimiento) · etiqueta "sostenido seis semanas" · pie "En mano".
  - Tile 3 — "WMAPE": valor "[candidato: de 51 a 33]" (Calibri bold 18 pt `#8A95A8`) · etiqueta "precisión de pronóstico de la demanda" · pie "[candidato: DP]".
  - Tile 4 — "Servicio recuperado": valor "[candidato: $9-12M/mes]" (Calibri bold 18 pt `#8A95A8`) · etiqueta "en facturación" · pie "[revisar doble conteo vs NADAL: RC]".

### Zona D — Transición al 2S (10%)
- Una línea, Calibri Light 13 pt `#1A2332`, sin caja: "En el 2S el juego cambia de abasto a demanda: cuatro realidades exigen cuatro conversaciones; vamos segmento por segmento."

### Zona E — Caveat (8%)
- Una línea, Calibri Light 9.5 pt `#8A95A8`: "Tres de las cuatro métricas de reconocimiento están por cerrar; se imprimen como candidatos hasta validarse. El '$9-12M/mes de servicio recuperado' debe revisarse contra el NADAL para evitar doble conteo."

### Zona F — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 10".

- **Mensaje que manda la lamina:** El 93.4% no es una historia sino cuatro (Retail y Gobierno restan, Hospitales y Servicios suman sin compensar), y el semestre deja un logro operativo real: la cadena de suministro estabilizó el servicio (fill rate 95-96% seis semanas) y ahora el reto se movió a acelerar la demanda.
- **Fuente (pie de lamina):** Fuente: Sell-In PiSA cierre jun-26 (cumplimiento por segmento); métricas de servicio y pronóstico: Demand Planning / cadena de suministro, 1S-2026 (candidatos por validar)
- **Estado del dato:**
  - Zona B (cumplimientos 92.3 / 90.0 / 95.2 / 102.1): en mano (lámina 9); comprimidos a UNA línea por instrucción 16-jul.
  - Zona C, Tile 2 (fill rate 95-96%, seis semanas): en mano.
  - Zona C, Tiles 1, 3, 4 (640 a 78 / 51 a 33 / $9-12M/mes): CANDIDATOS, se imprimen entre corchetes; ninguno se rellena.
  - REGLA FILL-OR-KILL (16-jul): si [FM] (producto negado), [DP] (WMAPE) o [RC] (servicio recuperado) no validan su cifra el 21-jul, ese tile SE CORTA de la lámina (no viaja como candidato al Consejo). La lámina puede quedar con 2-3 tiles.
- **Notas para el dibujante:**
  - LÍNEA DE SPEAKER (no imprimible): el reconocimiento a la cadena "se dice como logro, no como excusa"; esa instrucción es para quien presenta, no texto de lámina.
  - El ÚNICO gold es el "95-96%" del Tile 2 (fill rate). Nada más en dorado. Es deliberado: la única métrica en mano lleva el peso del reconocimiento; los tres candidatos van en gris de placeholder `#8A95A8` y un nivel tipográfico abajo (18 pt vs 24 pt).
  - Los valores candidatos se dibujan con su corchete literal completo ("[candidato: de 640 a 78]") en gris; prohibido estimarlos, redondearlos o borrar el corchete. Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27].
  - Zona B NO es la tabla de la lámina 9 ni una franja de tiles: es UNA línea de prosa. Una idea por lámina.
  - Sin verde celebratorio en ningún cumplimiento ni en el 102.1% de Servicios; todo navy neutro.
  - Usar "de X a Y" para las transiciones (de 640 a 78, de 51 a 33); ningún carácter de flecha en texto.
  - Sin caja de insight, sin rótulos "INSIGHT"/"RECONOCIMIENTO" como etiqueta de bloque; los kickers de zona son texto plano navy.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares. Estructura en bandas horizontales apiladas.

BANDA 1 (título, ~16%): título grande navy #0F2845 en peso ligero, dos líneas: "Dos segmentos restan y dos suman; los que suman no compensan, y la cadena de suministro ya entregó su parte". Debajo, subtítulo en itálica gris #44546A: "El 93.4% son cuatro historias, no una; el cuello de botella del semestre se movió del abasto a la demanda".

BANDA 2 (síntesis, ~8%): UNA sola línea de texto (puede correr a dos renglones), en gris oscuro #1A2332 con los cuatro porcentajes en negrita navy #0F2845 (figuras tabulares), sin tiles ni tabla: "El 93.4% son cuatro historias: restan Retail (92.3%, vía Farmacias) y Gobierno FC (90.0%); suman Hospitales (95.2%) y Servicios (102.1%), sin alcanzar a compensar." SIN color de semáforo, SIN verde.

BANDA 3 (reconocimiento a la cadena de suministro, ~44%): arriba, en negrita navy #0F2845 pequeño: "La cadena de suministro entregó su parte en el 1S". Debajo, cuatro tiles KPI en una fila, separados por líneas finas gris #E5E9EE, sin fondo. Cada tile lleva un valor grande arriba, una etiqueta descriptiva en gris #5A6679 en medio, y el estado del dato en gris claro #8A95A8 al pie. IMPORTANTE: el valor del Tile 2 (fill rate) es el más grande; los tres valores candidatos van visiblemente MÁS CHICOS (un nivel tipográfico abajo) y en gris:
- Tile 1: valor "[candidato: de 640 a 78]" en negrita GRIS #8A95A8, más chico que el del Tile 2; etiqueta "Producto negado · de abril a junio"; pie "[validar unidad, claves vs miles de piezas: FM]".
- Tile 2: valor "95-96%" en negrita color DORADO #C5A55A, el más grande de la fila (ÚNICO elemento dorado de toda la lámina); etiqueta "Fill rate · sostenido seis semanas"; pie "En mano".
- Tile 3: valor "[candidato: de 51 a 33]" en negrita gris #8A95A8, más chico; etiqueta "WMAPE · precisión de pronóstico de la demanda"; pie "[candidato: DP]".
- Tile 4: valor "[candidato: $9-12M/mes]" en negrita gris #8A95A8, más chico; etiqueta "Servicio recuperado · en facturación"; pie "[revisar doble conteo vs NADAL: RC]".

BANDA 4 (transición, ~10%): una sola línea en gris oscuro #1A2332, sin caja: "En el 2S el juego cambia de abasto a demanda: cuatro realidades exigen cuatro conversaciones; vamos segmento por segmento."

BANDA 5 (caveat, ~8%): una línea chica en gris claro #8A95A8: "Tres de las cuatro métricas de reconocimiento están por cerrar; se imprimen como candidatos hasta validarse. El '$9-12M/mes de servicio recuperado' debe revisarse contra el NADAL para evitar doble conteo."

BANDA 6 (pie, ~14%): línea divisoria gris #E5E9EE; debajo, a la izquierda en itálica gris #8A95A8 chico: "Fuente: Sell-In PiSA cierre jun-26 (cumplimiento por segmento); métricas de servicio y pronóstico: Demand Planning / cadena de suministro, 1S-2026 (candidatos por validar)"; a la derecha: "PiSA Confidencial | 10".

Reglas estrictas: el ÚNICO elemento dorado es el "95-96%" del fill rate; los otros tres valores KPI van en gris de placeholder, más chicos que el fill rate, con su corchete "[candidato: ...]" dibujado literal y completo, sin rellenar ni estimar (son placeholders internos del borrador; se eliminarán o resolverán antes de la versión final). Ningún cumplimiento en verde. La banda 2 es UNA línea de prosa, no una tabla ni tiles. Usa "de X a Y" en las transiciones; ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT/SO WHAT/RECONOCIMIENTO; sin borde izquierdo; sin rayas largas (em-dash) en la prosa; español con acentos; título sin punto final.
```


---

# Lamina 11 · PiSA defiende el valor en un retail que entra en recesión de volumen: abril no es un mal mes, es la tendencia
- **Momento:** M3 · Retail: entorno, 1S, 2S
- **Encabezado:** PiSA defiende el valor en un retail que entra en recesión de volumen: abril no es un mal mes, es la tendencia
- **So-what subtitle:** El volumen cae en todos los cortes; el valor lo sostienen GLP-1 y precio, y los exógenos están medidos
- **Layout (RECORTE MAYOR 16-jul):** Banda de título 14% + cuerpo con DOS paneles lado a lado 56% (Panel A 55% / Panel C 45%, gutter 0.15in) + línea de exógenos 7% + banda de intel de canal (kicker) 9% + línea de leyenda de placeholders + footer 12%. CADA PANEL DECLARA SU UNIVERSO en un eyebrow propio; los universos NUNCA se combinan en una misma gráfica. Los Paneles B y D salieron de la lámina: A ANEXO (ver "Contenido diferido a anexo").

## Zona por zona

### Zona A — Banda de título (14%)
- Título: Calibri Light 32 pt `#0F2845` (2 líneas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Panel A (izquierda, 55%): la caída de abril es tendencia
- Eyebrow de universo: "IQVIA · RETAIL SELL-OUT RX+OTC (MERCADO TOTAL) · ENE-ABR-26" — Calibri Light 9 pt UPPERCASE `#5A6679`.
- Kicker: "El mercado pierde volumen mes tras mes; el valor ya no cubre la inflación" — Calibri bold 11 pt `#0F2845`.
- Gráfica de barras verticales: YoY de unidades por mes, 2026 vs 2025.
  - Eje Y: "% var. anual, unidades" (arranca en 0, barras hacia abajo); sin gridlines o `#E5E9EE` 0.5 pt.
  - Barras en orden: ene-26 −3.7% · feb-26 −3.9% · mar-26 −9.4% · abr-26 −13.6% · YTD ene-abr −7.7% (quinta barra separada por gap mayor).
  - Colores: ene-mar y YTD en `#0F2845` (primary-900); abr-26 en GOLD `#C5A55A` (único gold de la lámina). Data labels sí, Calibri Light 10 pt `#1A2332`. Espacio entre barras ≥ 50% del ancho de barra.
- Anotaciones al costado de la gráfica (DOS, no tres; Calibri Light 10 pt `#3D4A5F`):
  - "Valor de abril: +3.1%, debajo del INPC (4.45%)"
  - "El +7.8% de valor YTD es 72% GLP-1 (+176% anual)"
  - (La anotación "Sin GLP-1, el valor de abril CAE: entre −1.2% y −2.4%" con su chip [fijar cifra con IQVIA: CC] SALE de la lámina: A ANEXO.)
- Sub-strip de prescripciones (misma fuente IQVIA, panel PBS), una línea al pie del panel: "Las recetas confirman lo estructural: antiinfecciosos −19.7% y respiratorio −30.6% anual (volumen prescriptivo)".

### Zona C — Panel C (derecha, 45%): nuestro mercado foco ya se contrae
- Eyebrow de universo: "KNOBLOCH · SELL-OUT · ENTRY MARKET (SIN ELECTROLITOS, FI Y GLP-1) · MAT MAY-26".
- Kicker: "El mercado foco cae −4.2%; PiSA defiende el valor, no las piezas".
- Gráfica de barras agrupadas: 2 grupos (Valor, Unidades) × 2 series.
  - Serie "Entry Market": Valor −4.2% · Unidades −7.9% — color `#8A95A8` (gray-400).
  - Serie "PiSA/AMSA": Valor −0.1% · Unidades −9.4% — color `#0F4C81` (primary-700).
  - Eje Y "% var. anual"; barras hacia abajo desde 0; data labels sí; etiquetar las series directamente (sin leyenda flotante).
- Anotaciones (Calibri Light 10 pt `#3D4A5F`):
  - "Visita médica, el subsegmento más golpeado: −6.7% valor / −13.8% unidades"
  - "El crecimiento del mercado total es GLP-1 ($19.8B, +162.6%), que no jugamos [validar cifra vs corte del deck Farmacias: CC]"
  - "Antibióticos: −7.7% MAT en valor"

### Zona D — Línea de exógenos (una línea, ancho completo)
- Calibri Light 11 pt `#3D4A5F`, sin caja: "Exógenos: vacunación +77%, el invierno más cálido de la serie, gripe −19.1%: medidos, detalle en anexo."

### Zona E — Banda de intel de canal (kicker, 9%)
- Tipo: una línea de prosa italic, Calibri Light 10 pt `#5A6679`, sin caja ni rótulo: "Lo que nos dice el mercado: Nadro ajustó su meta de crecimiento de 5% a 3%; Ultra crece 0%; y el capital de trabajo del canal se está yendo a GLP-1: los mayoristas financian Mounjaro y no financian el resto."

### Zona E2 — Línea de leyenda de placeholders (sobre el footer)
- Calibri Light 8 pt `#8A95A8`: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

### Zona F — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie (dos líneas permitidas a 9 pt) + "PiSA Confidencial | 11".

- **Mensaje que manda la lamina:** El retail farmacéutico está entrando en recesión de volumen: la caída de abril es la aceleración de una tendencia (IQVIA) y nuestro mercado foco ya se contrae (Knobloch). Los exógenos que la explican están medidos (detalle en anexo) y el canal lo confirma desde adentro: el capital de trabajo de los mayoristas se está yendo a GLP-1.
- **Fuente (pie de lamina):** Fuente: IQVIA retail sell-out Rx+OTC ene-abr-26 (universo mercado total; NO cubre canal hospitalario ni licitación) y panel IQVIA PBS (prescripciones); Knobloch MAT may-26 (Entry Market = mercado foco PiSA/AMSA sin electrolitos, FI y GLP-1); exógenos: IQVIA sector público / FAN / Conagua (detalle en anexo); intel de canal PiSA
- **Estado del dato:**
  - Panel A: en mano (IQVIA p42/p3/p16). La anotación del abril sin GLP-1 (rango −1.2% a −2.4%, inconsistencia interna del reporte IQVIA p43 vs p6, [fijar con IQVIA: CC]) se difirió a anexo con todo y chip.
  - Panel C: en mano (Knobloch MAT may-26), EXCEPTO GLP-1 $19.8B / +162.6%: por validar [CC] (ver riesgos).
  - Línea de exógenos (+77% vacunación, invierno más cálido, gripe −19.1%): en mano (IQVIA sector público, FAN, Conagua); el detalle numérico completo vive en el anexo.
  - Banda E: intel de canal, se dice como tal (nunca con fuente inventada).
  - Contenido diferido a anexo (Paneles B y D): estados de dato intactos, ver la subsección al final.
- **Notas para el dibujante:**
  - RECORTE MAYOR (orden Rafael 16-jul): la lámina queda en DOS paneles (A IQVIA mensual + C Knobloch) lado a lado. El Panel B (exógenos) se comprime a UNA línea de texto y su detalle va a anexo; el Panel D (consumo y tablero de distribución) va COMPLETO a anexo; la banda de intel (mayoristas/Mounjaro) se queda como kicker. Esto supersede la decisión provisional del README ("Panel D a una 11-bis solo si no respira").
  - El ÚNICO gold es la barra de abr-26 en el Panel A. Nada más en dorado.
  - Los universos NO se mezclan en una misma gráfica. Los periodos difieren entre paneles a propósito (IQVIA ene-abr · Knobloch MAT may-26): cada eyebrow declara el suyo; prohibido compararlos entre sí con flechas o conectores.
  - Vocabulario matizado obligatorio: "se está gestando una recesión", nunca "el mercado está en recesión" ni statements absolutos.
  - La banda de intel es intel: va en italic y arranca con "Lo que nos dice el mercado"; prohibido atribuirle fuente formal o convertirla en bullets con datos duros.
  - Cero em-dash y cero carácter de flecha en texto imprimible. Cero stage directions impresas: la instrucción de speaker "los exógenos no son excusa" vive aquí abajo (Guía de speaker), no en ningún cuadro de texto.
  - Chips ([validar cifra vs corte del deck Farmacias: CC] y los del anexo) se dibujan literales en gris neutro; todos son PLACEHOLDER INTERNO (kill antes del 27), declarado una sola vez en la línea de leyenda.
  - Sin caja de insight, sin emojis, sin border-left, sin gradientes.
- **Guía de speaker (NO se dibuja):** Los exógenos se presentan como medidos, no como excusa: ese matiz se dice a voz, no se imprime. El detalle de exógenos y el tablero de distribución (Panel D) viven en anexo por si el Consejo pregunta.

### Contenido diferido a anexo

**A ANEXO — Panel B (exógenos, detalle):**
- Eyebrow de universo: "IQVIA SECTOR PÚBLICO · FAN · CONAGUA (PANELES SEPARADOS)".
- Kicker: "Los exógenos, medidos".
- 4 tiles KPI compactos (2×2; separación border 0.5 pt `#E5E9EE`):
  - Tile 1 — "+77%" (Calibri bold 20 pt `#0F2845`) · label: "vacunación institucional, unidades atendidas MAT abr-26 (respiratorias +121%)".
  - Tile 2 — "18.9 °C" · label: "invierno 25-26, el más cálido de la serie (promedio nov-feb, Conagua)".
  - Tile 3 — "−19.1%" · label: "población afectada por gripe, acumulado de temporada (FAN, a semana 37)".
  - Tile 4 — "24% a 32% · 62% a 68%" (Calibri bold 16 pt) · label: "peso del gobierno en unidades de respiratorio (ATC R) y antiinfecciosos (ATC J), 2022 a 2026".
- Remate del panel (Calibri Light 10 pt italic `#44546A`): "Lo que el sector público surte ya no pasa por el mostrador".
- Estado: en mano (IQVIA sector público, FAN, Conagua).

**A ANEXO — Panel D (consumo y tablero de distribución):**
- Eyebrow de universo: "UNIVERSOS MÚLTIPLES · DECLARADOS POR RENGLÓN. SIN GRÁFICA COMBINADA".
- Kicker: "El consumo cae y el tablero de distribución se reordena".
- Lista de 5 renglones (delta inicial en Calibri bold con semáforo `#C00000`/`#2E7D4F`; fuente por renglón al final en 8.5 pt `#8A95A8`):
  1. "−4.9% el consumo privado anual a jun-26, quinta caída mensual consecutiva" — (BBVA Research, 15-jul-26)
  2. "~90 días de inventario en el canal contra 60 de estándar; mayoristas RX entre 113 y 146" — (intel de canal / DDI PiSA)
  3. "+13% cadenas grandes en valor sostienen el mercado; el independiente ya cae: −4% en valor y −7% en unidades" — (IQVIA retail, YTD abr-26)
  4. "Drogueros modernos desplazan al tradicional: Nadro +25%, Fanasa +34%, Difarmer −25% [rotular fuente: CC]; Marzam rescatada por Grupo OMNi (ago-25); Fanasa migra de cliente a competidor"
  5. "−29% Tramadol en Simi por regulación de controlados" — (intel de canal)
- Estado: BBVA e IQVIA en mano; renglón drogueros (Nadro +25% / Fanasa +34% / Difarmer −25%) por completar [CC — rotular fuente]; inventarios: intel de canal declarado.

**A ANEXO — Anotación del Panel A (abril sin GLP-1):**
- "Sin GLP-1, el valor de abril CAE: entre −1.2% y −2.4% [fijar cifra con IQVIA: CC]" — se imprime COMO RANGO con su corchete de pendiente (inconsistencia interna del reporte IQVIA p43 vs p6); no elegir una de las dos cifras por cuenta propia.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; figuras tabulares en los números. Estructura: banda de título arriba (14%), un cuerpo con DOS paneles lado a lado (56%), una línea de exógenos de ancho completo (7%), una banda de intel de una línea (9%), una línea de leyenda chica y el pie (12%). Cada panel lleva su propio eyebrow (etiqueta chica MAYÚSCULAS) que declara su universo de datos; los universos NUNCA se combinan en una misma gráfica.

BANDA DE TÍTULO: título grande navy #0F2845 en peso ligero (dos líneas): "PiSA defiende el valor en un retail que entra en recesión de volumen: abril no es un mal mes, es la tendencia". Debajo, subtítulo en itálica gris #44546A: "El volumen cae en todos los cortes; el valor lo sostienen GLP-1 y precio, y los exógenos están medidos".

PANEL A (izquierda, ~55% del ancho): eyebrow gris #5A6679 "IQVIA · RETAIL SELL-OUT RX+OTC (MERCADO TOTAL) · ENE-ABR-26". Kicker en negrita navy #0F2845 "El mercado pierde volumen mes tras mes; el valor ya no cubre la inflación". Gráfica de barras verticales que crecen hacia abajo desde una línea cero (son variaciones negativas), eje Y "% var. anual, unidades", con data labels. Cinco barras en este orden con estas proporciones aproximadas de profundidad: ene-26 −3.7% (corta) · feb-26 −3.9% (corta, casi igual) · mar-26 −9.4% (más del doble de profunda que febrero) · abr-26 −13.6% (la más profunda, ~1.4x la de marzo) · y separada por un espacio mayor, YTD ene-abr −7.7% (profundidad intermedia). Barras en navy #0F2845 excepto la de abr-26 que va en dorado #C5A55A (único elemento dorado de toda la lámina). Al costado de la gráfica, DOS anotaciones chicas en gris #3D4A5F: "Valor de abril: +3.1%, debajo del INPC (4.45%)" y "El +7.8% de valor YTD es 72% GLP-1 (+176% anual)". Al pie del panel una línea: "Las recetas confirman lo estructural: antiinfecciosos −19.7% y respiratorio −30.6% anual (volumen prescriptivo)".

PANEL C (derecha, ~45% del ancho): eyebrow "KNOBLOCH · SELL-OUT · ENTRY MARKET (SIN ELECTROLITOS, FI Y GLP-1) · MAT MAY-26". Kicker en negrita navy "El mercado foco cae −4.2%; PiSA defiende el valor, no las piezas". Gráfica de barras agrupadas: dos grupos ("Valor" y "Unidades"), cada uno con dos barras que caen hacia abajo desde cero, etiquetadas directamente sin leyenda flotante. Serie "Entry Market" en gris #8A95A8: Valor −4.2%, Unidades −7.9%. Serie "PiSA/AMSA" en azul #0F4C81: Valor −0.1% (casi nula, apenas asoma bajo cero), Unidades −9.4% (la más profunda del panel). Eje Y "% var. anual", data labels visibles. Anotaciones chicas en gris #3D4A5F: "Visita médica, el subsegmento más golpeado: −6.7% valor / −13.8% unidades"; "El crecimiento del mercado total es GLP-1 ($19.8B, +162.6%), que no jugamos [validar cifra vs corte del deck Farmacias: CC]"; "Antibióticos: −7.7% MAT en valor".

LÍNEA DE EXÓGENOS (ancho completo, una sola línea, texto gris #3D4A5F, sin caja): "Exógenos: vacunación +77%, el invierno más cálido de la serie, gripe −19.1%: medidos, detalle en anexo."

BANDA DE INTEL (una línea, italic, gris #5A6679, sin caja ni rótulo): "Lo que nos dice el mercado: Nadro ajustó su meta de crecimiento de 5% a 3%; Ultra crece 0%; y el capital de trabajo del canal se está yendo a GLP-1: los mayoristas financian Mounjaro y no financian el resto."

LÍNEA DE LEYENDA (encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE: línea divisoria gris #E5E9EE; debajo, en gris claro #8A95A8 chico (puede ir en dos líneas), a la izquierda: "Fuente: IQVIA retail sell-out Rx+OTC ene-abr-26 (universo mercado total; NO cubre canal hospitalario ni licitación) y panel IQVIA PBS (prescripciones); Knobloch MAT may-26 (Entry Market = mercado foco PiSA/AMSA sin electrolitos, FI y GLP-1); exógenos: IQVIA sector público / FAN / Conagua (detalle en anexo); intel de canal PiSA"; a la derecha: "PiSA Confidencial | 11".

Reglas estrictas: el ÚNICO elemento dorado es la barra de abr-26 del Panel A; nada más en dorado. Solo DOS paneles: no dibujar tiles de exógenos ni listas de distribución (viven en anexo). Nunca unifiques los paneles en una sola gráfica. Dibuja literal el corchete "[validar cifra vs corte del deck Farmacias: CC]" en gris neutro. Signo menos tipográfico "−", no guion. Ningún carácter de flecha ni em-dash en texto; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin gradientes; español con acentos; título sin punto final.
```


---

# Lamina 12 · El corto plazo castiga a un mercado que de fondo sigue sano; Diabetes/Obesidad y marca propia crecen con fuerza
- **Momento:** M3 · Retail: entorno, 1S, 2S
- **Encabezado:** El corto plazo castiga a un mercado que de fondo sigue sano; Diabetes/Obesidad y marca propia crecen con fuerza
  (SIN "solo": la exclusividad no se afirma hasta que el rotulado de valores [CC] la respalde; si al validar los valores resulta que son los únicos crecimientos fuertes, Rafael puede restaurar el "solo".)
- **So-what subtitle:** Donde el castigo es de corto plazo, se aguanta; donde el deterioro es estructural, se re-asigna
- **Layout:** Banda de título 16% + gráfica de burbujas (cuadrante) a ancho casi completo 60% + banda de lectura 12% + footer 12%. Es una lámina CONCEPTUAL: los ejes van rotulados, las burbujas son siluetas placeholder SIN valores numéricos, y la leyenda declara el pendiente de rotulado.

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Gráfica de burbujas por línea terapéutica, CONCEPTUAL (60%)
- Eyebrow de universo (arriba-izquierda del panel): "KNOBLOCH · SELL-OUT · MERCADO TOTAL RETAIL · TACC 5 AÑOS vs ÚLTIMO AÑO" — Calibri Light 9 pt UPPERCASE `#5A6679`.
- Ejes rotulados (SIN escala numérica impresa; solo el cruce de cuadrantes):
  - Eje X: "TACC 3-5 años · crecimiento estructural (largo plazo)" — Calibri Light 10 pt `#5A6679`, de izquierda (bajo) a derecha (alto).
  - Eje Y: "Crecimiento último año · corto plazo" — Calibri Light 10 pt `#5A6679`, de abajo (bajo) a arriba (alto).
  - Líneas de cuadrante: dos ejes de referencia grises `#C5CDD9` 0.5 pt que cruzan el plano en el centro (origen conceptual, no cero rotulado).
- Rótulos de cuadrante (Calibri Light 9.5 pt italic `#8A95A8`, en la esquina de cada cuadrante, texto plano; sin em-dash):
  - Arriba-derecha: "Sano en ambos plazos: sostener"
  - Abajo-derecha: "Sano de fondo, castigado a corto: aguantar"
  - Arriba-izquierda: "Rebote de corto sobre base débil"
  - Abajo-izquierda: "Deterioro estructural: re-asignar"
- Burbujas: SILUETAS placeholder en gris `#E5E9EE` con borde 0.75 pt `#C5CDD9`, tamaño variable (representa tamaño de mercado), SIN valores numéricos dentro ni etiquetas de dato. Distribución conceptual sugerida (posiciones cualitativas, no medidas):
  - Una burbuja GRANDE en el cuadrante arriba-derecha rotulada "Diabetes / Obesidad (GLP-1)" — ÚNICA burbuja con contorno GOLD `#C5A55A` 1.5 pt (único elemento gold de la lámina): es el crecimiento fuerte del mercado que PiSA no juega.
  - Una burbuja mediana en el cuadrante arriba-derecha rotulada "Marca propia" (el otro crecimiento genuino; silueta gris con borde `#C5CDD9`).
  - Varias siluetas grises SIN rótulo repartidas en los cuadrantes de abajo (dos-tres en "aguantar" abajo-derecha y dos-tres en "re-asignar" abajo-izquierda), representando el resto de líneas terapéuticas; una de las de abajo-izquierda algo mayor (antibióticos/antiinfecciosos, línea estructuralmente débil), sin rótulo de dato.
- Chip de pendiente, dibujado literal dentro del panel (Calibri Light 10 pt `#8A95A8`, fondo `#F0F3F7`, borde 0.5 pt `#C5CDD9`): "[valores por rotular por burbuja: CC]".

### Zona C — Banda de lectura (12%)
- Una línea, Calibri Light 11 pt `#1A2332`, sin caja: "La fuente trae cuatro vistas (mercado total, ético, genérico, OTC); la lámina muestra el mercado total. La lectura: donde el corto plazo castiga a un mercado de fondo sano se aguanta; donde el deterioro es de largo plazo, se re-asigna el esfuerzo."

### Zona D — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 12".

- **Mensaje que manda la lamina:** El mercado retail se lee en dos ejes de tiempo: la mayoría de las líneas terapéuticas están de fondo sanas pero castigadas a corto plazo (ahí se aguanta), mientras unas pocas se deterioran estructuralmente (ahí se re-asigna); los crecimientos fuertes y sostenidos son Diabetes/Obesidad (GLP-1), que PiSA no juega, y la marca propia.
- **Fuente (pie de lamina):** Fuente: deck del canal Farmacias (Knobloch sell-out, mercado total retail; TACC 5 años vs último año por línea terapéutica); valores por burbuja pendientes de rotular [CC]. El eje de crecimiento a un año proviene del corte IQVIA/Knobloch interno del canal
- **Estado del dato:**
  - La FUENTE existe (deck del canal Farmacias L14-L17: cuatro vistas con TACC 5 años vs último año). Falta rotular los valores por burbuja [CC].
  - Lámina CONCEPTUAL por instrucción de Rafael: ejes rotulados, burbujas como siluetas placeholder SIN valores, leyenda "[valores por rotular: CC]". Ninguna cifra se inventa.
  - Las posiciones de "Diabetes/Obesidad (GLP-1)" y "Marca propia" en el cuadrante de alto crecimiento son cualitativas y provienen del propio storyline v6 ("solo crecen con fuerza Diabetes/Obesidad y marcas propias"); no llevan valores.
- **Notas para el dibujante:**
  - Es una lámina CONCEPTUAL: NO inventar números de crecimiento, tamaño ni ejes; las burbujas son siluetas grises `#E5E9EE` sin dato. El chip "[valores por rotular por burbuja: CC]" se dibuja visible; es [PLACEHOLDER INTERNO - kill antes del 27].
  - PETICIÓN DE RAFAEL (llamada 16-jul), referencia de coherencia con el ANEXO: en la versión del anexo las burbujas se reducen a la MITAD de tamaño y se colorean por dependencia del portafolio PiSA. Esta lámina de cuerpo se queda con siluetas grises; al dibujar el anexo, respetar esa relación (mitad de tamaño + color por dependencia) para que ambas vistas se lean como la misma familia.
  - El ÚNICO gold es el contorno de la burbuja "Diabetes / Obesidad (GLP-1)". Ninguna otra burbuja lleva color; el resto son siluetas gris `#E5E9EE` con borde `#C5CDD9`.
  - NO poner escala numérica en los ejes; solo el cruce de cuadrantes y los rótulos de cada eje. El origen es conceptual, no un cero medido.
  - Los cuatro rótulos de cuadrante son texto gris italic plano, sin fondo ni marco. No convertirlos en badges de color.
  - No dibujar una leyenda con valores de tamaño de burbuja (no existen aún); el tamaño relativo es solo ilustrativo del concepto "tamaño de mercado".
  - Sin caja de insight, sin emojis, ningún carácter de flecha, sin border-left, sin gradientes; título sin punto final.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique. Es una gráfica CONCEPTUAL: los ejes van rotulados pero SIN escala numérica, y las burbujas son siluetas grises sin ningún valor numérico.

BANDA DE TÍTULO (arriba, ~16%): título grande navy #0F2845 en peso ligero, dos líneas: "El corto plazo castiga a un mercado que de fondo sigue sano; Diabetes/Obesidad y marca propia crecen con fuerza". Debajo, subtítulo en itálica gris #44546A: "Donde el castigo es de corto plazo, se aguanta; donde el deterioro es estructural, se re-asigna".

PANEL CENTRAL (~60%): una gráfica de dispersión de burbujas dentro de un plano con dos ejes de referencia grises finos #C5CDD9 que se cruzan en el centro formando cuatro cuadrantes (el cruce es un origen conceptual, NO un cero numérico; no imprimas números en los ejes). Arriba a la izquierda del panel, una etiqueta pequeña en mayúsculas gris #5A6679: "KNOBLOCH · SELL-OUT · MERCADO TOTAL RETAIL · TACC 5 AÑOS vs ÚLTIMO AÑO". Rótulo del eje horizontal (abajo) en gris #5A6679: "TACC 3-5 años · crecimiento estructural (largo plazo)", creciendo de izquierda a derecha. Rótulo del eje vertical (izquierda, girado) en gris #5A6679: "Crecimiento último año · corto plazo", creciendo de abajo hacia arriba.

En cada esquina de cuadrante, un rótulo pequeño en itálica gris #8A95A8, texto plano sin recuadro (sin rayas largas): arriba-derecha "Sano en ambos plazos: sostener"; abajo-derecha "Sano de fondo, castigado a corto: aguantar"; arriba-izquierda "Rebote de corto sobre base débil"; abajo-izquierda "Deterioro estructural: re-asignar".

BURBUJAS (todas son siluetas grises rellenas en gris muy claro #E5E9EE con borde fino gris #C5CDD9, de distintos tamaños, SIN ningún número dentro ni etiqueta de dato):
- Una burbuja GRANDE en el cuadrante de arriba a la derecha, rotulada junto a ella "Diabetes / Obesidad (GLP-1)"; ESTA burbuja es la única con el borde en color DORADO #C5A55A (más grueso) — es el único elemento dorado de toda la lámina.
- Una burbuja mediana también arriba a la derecha, rotulada "Marca propia", con borde gris normal.
- Tres o cuatro siluetas grises SIN rótulo en el cuadrante de abajo a la derecha ("aguantar"), de tamaños medianos.
- Dos o tres siluetas grises SIN rótulo en el cuadrante de abajo a la izquierda ("re-asignar"), una de ellas algo más grande, sin ningún texto.

Dentro del panel, abajo, un chip rectangular pequeño con fondo gris muy claro #F0F3F7 y borde fino gris #C5CDD9, con el texto gris #8A95A8 dibujado literal: "[valores por rotular por burbuja: CC]".

BANDA DE LECTURA (~12%): una sola línea en gris oscuro #1A2332, sin caja: "La fuente trae cuatro vistas (mercado total, ético, genérico, OTC); la lámina muestra el mercado total. La lectura: donde el corto plazo castiga a un mercado de fondo sano se aguanta; donde el deterioro es de largo plazo, se re-asigna el esfuerzo."

PIE (~12%): línea divisoria gris #E5E9EE; debajo, a la izquierda en itálica gris #8A95A8 chico: "Fuente: deck del canal Farmacias (Knobloch sell-out, mercado total retail; TACC 5 años vs último año por línea terapéutica); valores por burbuja pendientes de rotular [CC]. El eje de crecimiento a un año proviene del corte IQVIA/Knobloch interno del canal"; a la derecha: "PiSA Confidencial | 12".

Reglas estrictas: NO inventes números; los ejes NO llevan escala numérica; las burbujas son siluetas grises sin ningún valor. El único elemento dorado es el borde de la burbuja "Diabetes / Obesidad (GLP-1)"; ninguna otra burbuja lleva color. El chip "[valores por rotular por burbuja: CC]" se dibuja visible y literal. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin gradientes; español con acentos; título sin punto final.
```


---

# Lámina 13 · El down-trading está dimensionado y localizado: −$197.9M en Privado, 71% concentrado en 5 moléculas, y la lista de precios aguanta (+$392.9M intra-SKU)
- **Momento:** M3 · Retail: entorno, 1S, 2S (43.6% de la venta)
- **Encabezado:** El down-trading está dimensionado y localizado: −$197.9M en Privado, 71% concentrado en 5 moléculas, y la lista de precios aguanta (+$392.9M intra-SKU)
- **So-what subtitle:** Puente Privado 1S-2025 a 1S-2026: de $7,178.5M a $7,209.8M en el universo del modelo, +$31.3M (+0.4%), 92.3% de meta; +$0.4M de FLP = $7,210.2M cubo
- **Layout:** Banda de título 15% + cuerpo 3 columnas 15/50/35 (Col 1: mercado vs PiSA · Col 2: puente de 6 componentes + conciliación, LISTO · Col 3: palancas comerciales 1S25 vs 1S26) 68% + footer 12%. Gutter 0.15in. Geometría 13.333 × 7.5 in, márgenes 0.5 in. Con la matriz consolidada del 16-jul, TODAS las láminas de puente (L8/13/18/23/28) van con columna 2 real; ésta conserva el mayor detalle de mix.

## Zona por zona

### Zona A — Banda de título (15%)
- Título: Calibri Light 26-30 pt `#0F2845` (2 líneas).
- Subtítulo so-what: Calibri Light 13-14 pt italic `#44546A`.

### Zona B — Columna 1: Mercado vs PiSA (15%, ~1.85 in de ancho)
- Micro-título de zona: "Mercado vs PiSA" — Calibri bold 12 pt `#0F2845`.
- Dos barras verticales, % var. anual, eje Y con cero al centro (variaciones negativas y positivas), sin gridlines:
  - Barra 1 "Entry Market" — valor "−4.2%" (cae bajo cero), color `#8A95A8` (gray-400), data label directo.
  - Barra 2 "PiSA Retail" — valor "+0.4%" (apenas sobre cero), color `#0F4C81` (primary-700), data label directo.
- Nota bajo la gráfica, Calibri Light 9 pt `#5A6679`: "Entry Market: valor, Knobloch MAT may-26. PiSA Retail: sell-in 1S. [unificar periodo del corte de mercado: CC]".

### Zona C — Columna 2: Puente Privado 1S25 a 1S26 (50%, ~6.15 in de ancho). Waterfall LISTO.
- Micro-título de zona: "Puente de ventas, seis componentes (matriz Downtrading FINAL 16-jul, control = 0)" — Calibri bold 12 pt `#0F2845`.
- Eyebrow de universo, Calibri Light 9 pt `#5A6679`: "Sell-in Privado = Farmacias + Impulso + Expansión · cobertura 96.0% del bruto".
- Waterfall, $M, eje Y arranca en 0, connectors punteados 0.5 pt `#C5CDD9`, data label sobre cada barra (con signo). Barras en orden de izquierda a derecha:
  1. "1S-2025" — **7,178.5** — barra ancla, navy `#0F2845` (mayor peso).
  2. "Precio" — **+392.9** — positivo, navy `#0F4C81` (la barra positiva grande: intra-SKU, la lista aguanta).
  3. "Volumen" — **−169.7** — negativo, rojo `#C00000`.
  4. "Mix / down-trading" — **−197.9** — negativo, rojo `#C00000` (la barra villana, la mayor negativa).
  5. "Gestión de portafolio" — **+0.2** — positivo, navy `#0F4C81` (casi un filo; se dibuja como línea con etiqueta).
  6. "Lanzamientos" — **+71.1** — positivo, navy `#0F4C81`.
  7. "Sin unidad (por valor)" — **−38.0** — negativo, rojo `#C00000`.
  8. Llave/corchete sobre las seis barras de componente, Calibri Light 10 pt `#3D4A5F`: "Δ reclasificada +$58.7M".
  9. "Reclas. nov-dic-25" — **−27.3** — barra GRIS `#C5CDD9` (contorno `#8A95A8`; conciliación contable, no desempeño).
  10. "1S-2026 (universo del modelo)" — **7,209.8** — barra ancla final, navy `#0F2845`, con data label "+$31.3M (+0.4%) oficial".
- Stub de cubo junto a la barra final, Calibri Light 9 pt `#8A95A8`: "+0.4 FLP = 7,210.2 cubo".
- Anotación de erosión vs precio (Calibri Light 11 pt), a la altura entre Precio y Mix, con línea guía tenue: "Down-trading (−$197.9M) más volumen (−$169.7M) = −$367.6M: se comen casi todo el precio de lista (+$392.9M). Poder de precio neto ≈ **+$195M**." La cifra "+$195M" en Calibri bold GOLD `#C5A55A` — ÚNICO elemento gold de la lámina.
- Línea de conciliación (una línea), Calibri Light 9.5 pt `#5A6679`: "Conciliación: Δ reclasificada +$58.7M · −$27.3M de cierre nov-dic-25 reclasificado = +$31.3M oficial (+0.4%) · +$0.4M FLP = $7,210.2M cubo."
- Sub-banda "Down-trading: dimensionado y localizado" (Calibri Light 10 pt `#3D4A5F`, una línea): "Top-5 moléculas = −$140.4M, 71% del efecto mix (detalle en L16)."

### Zona D — Columna 3: Comparativo 1S25 vs 1S26 (35%, ~4.3 in de ancho). Niveles lado a lado, NO waterfall.
- Micro-título de zona: "Palancas comerciales, 1S-2025 vs 1S-2026 (niveles, no escalones)" — Calibri bold 12 pt `#0F2845`.
- Cuatro bloques verticales; los bloques 1-2 con eyebrow "DP / pedidos · Retail = F+I+E", los bloques 3-4 con eyebrow "Gross2Net Finanzas · Retail":
  - Bloque 1 "Venta perdida" — dos barras lado a lado: "1S-2025 = $360M" (`#8A95A8`) y "1S-2026 = $352M" (`#0F4C81`); etiqueta "mejora −2%" Calibri Light 9.5 pt `#5A6679`.
  - Bloque 2 "PIN no solicitado" — dos barras lado a lado: "1S-2025 = $471M" (`#8A95A8`) y "1S-2026 = $564M" (`#0F4C81`, MÁS LARGA); etiqueta de delta en rojo `#C00000`: "empeora +20%". Bullet nuevo bajo las barras, Calibri Light 9.5 pt `#3D4A5F`: "Lo carga Expansión: de $80M a $162M (+102%); Farmacias 245 a 251 · Impulso 146 a 151."
  - Bloque 3 "NC comerciales y sanciones" — dos barras: "1S-2025 = −$426.6M" (`#8A95A8`) y "1S-2026 = −$488.1M" (`#0F4C81`, más larga); etiqueta en rojo `#C00000` "empeora +14.4%"; nota 9 pt `#5A6679`: "driver: marca propia +78% e Impulso +41%".
  - Bloque 4 "Devoluciones" — dos barras: "1S-2025 = −$232.6M" (`#8A95A8`) y "1S-2026 = −$240.8M" (`#0F4C81`); etiqueta neutra `#5A6679` "empeora $8.2M".
- Nota de universo (Calibri Light 9 pt `#8A95A8`): "El PIN no solicitado es demanda no cubierta (universo pedidos/planeación), no venta neta; no se cuadra contra el sell-in."

### Zona E — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 13".

- **Mensaje que manda la lámina:** El down-trading de Privado ya tiene tamaño y dirección: −$197.9M, con 71% concentrado en 5 moléculas (detalle en L16). La lista de precios aguanta (+$392.9M intra-SKU), pero el down-trading y el volumen (−$367.6M juntos) se comen casi todo; el poder de precio efectivo se lee neto (~+$195M) y el neto positivo del semestre lo sostienen los lanzamientos (+$71.1M). En las palancas, la venta perdida mejora pero el PIN no solicitado empeora +20%, cargado por Expansión.
- **Fuente (pie de lámina):** Fuente: matriz consolidada Downtrading FINAL 16-jul / Downtrading Privado v4 FINAL (Sell-In cierre jun-26, universo Privado = Farmacias+Impulso+Expansión, 1S-2026 vs 1S-2025, sell-in neto; método Mix = Shapley exacto sobre familias continuas); Entry Market: Knobloch MAT may-26; venta perdida y PIN: tabla canónica 16-jul (universo DP/pedidos); NC y devoluciones: Gross2Net Finanzas
- **Estado del dato:**
  - Columna 1 (Entry Market −4.2% vs PiSA +0.4%): en mano; el periodo del corte de mercado por unificar [CC].
  - Columna 2 (puente completo Precio +392.9 / Volumen −169.7 / Mix −197.9 / Gestión +0.2 / Lanzamientos +71.1 / Sin unidad −38.0 = +58.7 reclasificada; −27.3 reclasif = +31.3 con MATNR; +0.4 FLP = +31.8 cubo): EN MANO Y AUDITADO (matriz consolidada FINAL 16-jul, verificada al peso, CONTROL 0.0000). SUPERSEDE los valores viejos "Lanzamientos +43.8" y "Gestión −37.8" de la vista bruta anterior: en la vista reclasificada canónica Lanzamientos = +71.1 y Gestión = +0.2, y aparece la línea "Sin unidad −38.0".
  - Redondeo declarado: las sumas visibles a 1 decimal pueden diferir ±$0.1M (los 6 componentes a 1 decimal suman 58.6 vs 58.7 canónico; 7,178.5 + 58.7 − 27.3 = 7,209.9 visible vs ancla 7,209.8; 7,210.2 − 7,178.5 = 31.7 visible vs +31.8 cubo canónico); el workbook cierra al 4º decimal. Se imprimen los valores canónicos, no las restas visibles.
  - Columna 3: venta perdida $360M a $352M y PIN $471M a $564M con desglose (Farmacias 245/251 · Impulso 146/151 · Expansión 80/162): **en mano** (tabla canónica Rafael 16-jul; SUPERSEDE la venta perdida 359.0 a 343.5 de DP y el "PIN sin comparador 2025"). NC −426.6 a −488.1 y Dev −232.6 a −240.8: **en mano** (Gross2Net). La línea "NC logísticas" NO existe en la taxonomía real; los placeholders "[por llegar: VJ/RC]" quedan superados.
  - Rango citable del down-trading (no se imprime, vive en reserva del speaker): central −$197.9M; piso −$144.4M "mínimo entre variantes" (sensibilidad composicional, no intervalo de confianza); el −$107.3M es pre-arista FRISO y NO se cita sin esa etiqueta.
- **Notas para el dibujante:**
  - El ÚNICO gold es la cifra "+$195M" (poder de precio neto) en la anotación de la columna 2. Nada más en dorado.
  - Waterfall SIN verde: los positivos (Precio, Gestión, Lanzamientos) van en navy `#0F4C81`; los negativos (Volumen, Mix, Sin unidad) en rojo `#C00000`; las barras ancla (1S-25, 1S-26) en navy `#0F2845` con mayor peso; la barra de conciliación "Reclas. nov-dic-25 −27.3" en GRIS `#C5CDD9` (contabilidad, no desempeño: no pintarla de rojo). El rojo es semáforo cuantitativo sobre deltas (la erosión ES la historia), no decoración.
  - Proporciones relativas: Precio +392.9 es la barra flotante más grande; Mix −197.9 y Volumen −169.7 le siguen hacia abajo; Lanzamientos +71.1 mediana; Sin unidad −38.0 y Reclasif −27.3 chicas; Gestión +0.2 es un filo con etiqueta.
  - La barra "Mix / down-trading −197.9" es visualmente el villano, pero NO se pinta en gold; el gold vive solo en la anotación de neto "+$195M".
  - La columna 3 son NIVELES lado a lado, NO escalones de waterfall; los bloques 1-2 (DP/pedidos) y 3-4 (Gross2Net) llevan su eyebrow de universo y no se mezclan ni conectan.
  - Los chips "[unificar periodo del corte de mercado: CC]" se dibujan literales, en gris neutro, sin ámbar ni rojo. Todos los corchetes con responsable son PLACEHOLDER INTERNO — kill antes del 27: viven en el storyboard de revisión, no en la versión del Consejo.
  - Signo menos tipográfico "−", no guion; signo "+" explícito en positivos. Tabular figures en todo número. Usar "de X a Y" o "1S-2025 a 1S-2026", ningún carácter de flecha.
  - Números que NO se "corrigen" en la lámina: la Δ reclasificada es +$58.7M; el oficial del universo del modelo es +$31.3M (= +0.4% del sell-in); el cubo es +$31.8M ($7,210.2M). Se imprimen con su línea de conciliación, no se homologan.
  - Sin caja de insight, sin emojis, sin border-left, sin gradientes; título sin punto final.

### Contenido diferido a anexo
- A ANEXO: detalle nominal del top-5 down-traders (vive en L16 y en anexo): Amox/Clav −45.6 · Levofloxacino −32.9 · Ceftriaxona −24.7 · Enoxaparina −21.3 · Fexofenadina −15.9 (suman −$140.4M, 71% del efecto mix). Friso migra al revés: +$16.4M de mezcla positiva. En L13 solo viaja el total −$140.4M (71%) con la referencia "detalle en L16".

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares. Estructura: banda de título arriba (~15%), cuerpo dividido en TRES columnas de anchos 15% / 50% / 35% (~68%), y un pie delgado abajo (~12%).

BANDA DE TÍTULO (ancho completo): título grande navy #0F2845 en peso ligero, dos líneas: "El down-trading está dimensionado y localizado: −$197.9M en Privado, 71% concentrado en 5 moléculas, y la lista de precios aguanta (+$392.9M intra-SKU)". Debajo, subtítulo en itálica gris #44546A: "Puente Privado 1S-2025 a 1S-2026: de $7,178.5M a $7,209.8M en el universo del modelo, +$31.3M (+0.4%), 92.3% de meta; +$0.4M de FLP = $7,210.2M cubo". Línea horizontal fina gris #E5E9EE.

COLUMNA IZQUIERDA (15%): arriba, texto plano en negrita navy #0F2845 pequeño: "Mercado vs PiSA". Debajo, dos barras verticales con eje de cero al centro (una cae bajo cero, otra apenas sube), unidad "% var. anual", sin gridlines, con etiqueta de dato directa: barra 1 "Entry Market" en gris #8A95A8 con "−4.2%" (bajo cero); barra 2 "PiSA Retail" en azul #0F4C81 con "+0.4%" (apenas sobre cero). Bajo la gráfica, texto chico gris #5A6679: "Entry Market: valor, Knobloch MAT may-26. PiSA Retail: sell-in 1S. [unificar periodo del corte de mercado: CC]".

COLUMNA CENTRAL (50%): arriba, texto plano en negrita navy #0F2845 pequeño: "Puente de ventas, seis componentes (matriz Downtrading FINAL 16-jul, control = 0)". Debajo, en gris #5A6679 muy pequeño: "Sell-in Privado = Farmacias + Impulso + Expansión · cobertura 96.0% del bruto". Debajo, una gráfica de cascada (waterfall) con eje Y desde 0, unidad "$M", conectores punteados finos gris #C5CDD9. Barras de izquierda a derecha con su etiqueta de valor encima (con signo) y su nombre debajo:
1. "1S-2025" = "7,178.5" — barra ancla alta, navy oscuro #0F2845.
2. "Precio" = "+392.9" — positiva, azul #0F4C81, la barra flotante MÁS GRANDE del puente.
3. "Volumen" = "−169.7" — negativa, roja #C00000.
4. "Mix / down-trading" = "−197.9" — negativa, roja #C00000, la mayor de las negativas.
5. "Gestión de portafolio" = "+0.2" — positiva, azul #0F4C81, casi un filo (dibujar como línea delgada con etiqueta).
6. "Lanzamientos" = "+71.1" — positiva, azul #0F4C81, mediana.
7. "Sin unidad (por valor)" = "−38.0" — negativa, roja #C00000, chica.
Sobre estas seis barras flotantes, una llave horizontal rotulada en gris #3D4A5F: "Δ reclasificada +$58.7M".
8. "Reclas. nov-dic-25" = "−27.3" — barra GRIS claro #C5CDD9 con contorno gris #8A95A8 (conciliación contable: NO roja).
9. "1S-2026 (universo del modelo)" = "7,209.8" — barra ancla final alta, navy oscuro #0F2845, con la etiqueta "+$31.3M (+0.4%) oficial". Junto a ella, en gris #8A95A8 pequeño: "+0.4 FLP = 7,210.2 cubo".
NO uses verde en ninguna barra. Junto a la cascada, una anotación en gris #3D4A5F: "Down-trading (−$197.9M) más volumen (−$169.7M) = −$367.6M: se comen casi todo el precio de lista (+$392.9M). Poder de precio neto ≈ +$195M." La cifra "+$195M" va en negrita color DORADO #C5A55A — ÚNICO elemento dorado de toda la lámina. Debajo del waterfall, una línea chica en gris #5A6679: "Conciliación: Δ reclasificada +$58.7M · −$27.3M de cierre nov-dic-25 reclasificado = +$31.3M oficial (+0.4%) · +$0.4M FLP = $7,210.2M cubo." Y una línea final en gris #3D4A5F: "Top-5 moléculas = −$140.4M, 71% del efecto mix (detalle en L16)."

COLUMNA DERECHA (35%): arriba, texto plano en negrita navy #0F2845 pequeño: "Palancas comerciales, 1S-2025 vs 1S-2026 (niveles, no escalones)". Debajo, cuatro bloques apilados, cada uno con su título en negrita chica; los bloques 1-2 llevan arriba un eyebrow gris muy pequeño "DP / pedidos · Retail = F+I+E" y los bloques 3-4 un eyebrow "Gross2Net Finanzas · Retail":
- "Venta perdida": dos barras lado a lado, "1S-2025 = $360M" en gris #8A95A8 y "1S-2026 = $352M" en azul #0F4C81 (apenas más corta); etiqueta chica gris #5A6679 "mejora −2%".
- "PIN no solicitado": dos barras lado a lado, "1S-2025 = $471M" en gris #8A95A8 y "1S-2026 = $564M" en azul #0F4C81 claramente MÁS LARGA; etiqueta en rojo #C00000 "empeora +20%"; debajo, texto chico gris #3D4A5F: "Lo carga Expansión: de $80M a $162M (+102%); Farmacias 245 a 251 · Impulso 146 a 151."
- "NC comerciales y sanciones": dos barras, "1S-2025 = −$426.6M" gris y "1S-2026 = −$488.1M" azul más larga; etiqueta en rojo #C00000 "empeora +14.4%"; nota chica gris #5A6679 "driver: marca propia +78% e Impulso +41%".
- "Devoluciones": dos barras, "1S-2025 = −$232.6M" gris y "1S-2026 = −$240.8M" azul apenas más larga; etiqueta chica gris #5A6679 "empeora $8.2M".
Al pie de la columna, texto chico gris #8A95A8: "El PIN no solicitado es demanda no cubierta (universo pedidos/planeación), no venta neta; no se cuadra contra el sell-in."

PIE (ancho completo): línea fina gris #E5E9EE; a la izquierda, itálica gris #8A95A8 chica: "Fuente: matriz consolidada Downtrading FINAL 16-jul / Downtrading Privado v4 FINAL (Sell-In cierre jun-26, universo Privado = Farmacias+Impulso+Expansión, 1S-2026 vs 1S-2025, sell-in neto; método Mix = Shapley exacto sobre familias continuas); Entry Market: Knobloch MAT may-26; venta perdida y PIN: tabla canónica 16-jul; NC y devoluciones: Gross2Net Finanzas". A la derecha: "PiSA Confidencial | 13".

Reglas estrictas: el ÚNICO elemento dorado es la cifra "+$195M" del poder de precio neto. El waterfall NO usa verde: positivos en azul #0F4C81, negativos en rojo #C00000, anclas en navy #0F2845, la conciliación en gris #C5CDD9. La columna 3 son niveles lado a lado, no una cascada, con universos declarados por eyebrow. Los chips entre corchetes se dibujan literales, en gris neutro, sin ámbar ni rojo. Signo menos tipográfico "−", no guion; "+" explícito. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin gradientes; español con acentos; título sin punto final.
```


---

# Lamina 14 · Farmacias concentra el deterioro del 1S; Impulso y Expansión defienden valor con elasticidad y mezcla
- **Momento:** M3 · Retail: entorno, 1S, 2S (43.6% de la venta)
- **Encabezado:** Farmacias concentra el deterioro del 1S; Impulso y Expansión defienden valor con elasticidad y mezcla
- **So-what subtitle:** El gap de Farmacias fue capacidad y liberación, no demanda, y ya se corrige desde mayo
- **Layout:** Banda de título 15% + cuerpo 3 paneles BALANCEADOS (misma anchura ~1/3 cada uno: Farmacias · Impulso · Expansión) 47% + franja horizontal de Consumo (ancho completo) 14% + footer 12%. Gutter 0.15in. (Rediseño 16-jul: tarjetas balanceadas; el sub-bloque de Consumo sale del panel de Farmacias y baja a franja horizontal propia.)

## Zona por zona

### Zona A — Banda de título (15%)
- Título: Calibri Light 32 pt `#0F2845` (2 líneas permitidas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Panel Farmacias (columna izquierda, ~1/3 del ancho)
- Header del panel: "Farmacias · 88.9% de meta · −2.2%" (Calibri bold 12 pt blanco sobre banda `#0F2845`; el delta "−2.2%" en BLANCO, no rojo: rojo sobre navy no lee y el semáforo sale de los headers). Cuerpo fondo blanco, border 0.5 pt `#C5CDD9`, radius 4-8 px.
- Cifra pivote: "Concentra el gap del bloque: **−$369M** (56% es marca propia)". La cifra "−$369M" en Calibri bold 20 pt GOLD `#C5A55A` — ÚNICO elemento gold de la lámina.
- Bullets (Calibri Light 11 pt `#3D4A5F`):
  1. Marca propia −10.5% (81.2% de meta): fue capacidad y liberación, no demanda.
  2. Ya se corrige: MP crece desde mayo, +$21M el bimestre.
  3. Venta perdida empeoró: de $139M a $171M (+24% vs 1S25).

### Zona C — Panel Impulso (columna central, ~1/3 del ancho)
- Header del panel: "Impulso · 95.4% de meta · +1.8%" (Calibri bold 12 pt blanco sobre banda `#0F4C81`; el delta "+1.8%" en BLANCO, sin verde: verde celebratorio fuera de cifras propias).
- Cifra: "Elasticidad que funcionó: **+$51M** de beneficio de precio vs **$32M** de plan" (valores Calibri bold 18 pt `#0F2845`).
- Bullet (Calibri Light 11 pt `#3D4A5F`): "Valor sobre volumen deliberado: se subió precio sin perder el volumen esperado."

### Zona D — Panel Expansión (columna derecha, ~1/3 del ancho)
- Header del panel: "Expansión · 93.8% de meta · +3.4%" (Calibri bold 12 pt blanco sobre banda `#0F4C81`; el delta "+3.4%" en BLANCO, sin verde).
- Cifra: "Friso gana share y migra hacia arriba: mezcla **+$16.4M**" (valor Calibri bold 18 pt `#0F2845`).
- Bullet (Calibri Light 11 pt `#3D4A5F`): "En un mercado premium que se hunde: Friso −5.1% contra −8.5% del mercado."

### Zona D-bis — Franja horizontal de Consumo (ancho completo, ~14%)
- Micro-título de franja (texto plano): "Consumo crece fuerte: dos cortes en la mesa" — Calibri bold 10.5 pt `#0F2845`.
- Los DOS cortes impresos lado a lado (ninguno se elige aquí), Calibri Light 11 pt `#3D4A5F`:
  - Corte A: "Sublínea OTC (sell-in): **+46.1%** · 102.6% de meta"
  - Corte B: "UDN Consumo (canal): **+23.7%** · 81% de meta"
  - Chip literal entre/bajo los dos cortes, Calibri Light 10 pt `#8A95A8`, fondo `#F0F3F7`, borde 0.5 pt `#C5CDD9`: "[corte OTC vs Consumo por definir: Rafael+IC]".

### Zona E — Footer (12%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 14".

- **Mensaje que manda la lamina:** El deterioro de Retail está concentrado en Farmacias (88.9%, −2.2%, −$369M de gap, 56% marca propia), y ese gap fue capacidad y liberación de marca propia, no caída de demanda, que ya se corrige desde mayo aunque la venta perdida del canal empeoró (+24%); en paralelo, Impulso defendió valor con elasticidad (+$51M vs $32M plan) y Expansión con la mezcla de Friso (+$16.4M) en un mercado premium que cae.
- **Fuente (pie de lamina):** Fuente: Sell-In PiSA cierre jun-26 (Retail por canal); venta perdida: tabla consolidada Comercial 16-jul-26; UDN Consumo y sublínea OTC del deck del canal Farmacias; elasticidad Impulso y mezcla Friso: análisis del canal 1S-2026
- **Estado del dato:**
  - Farmacias 88.9% / −2.2% / gap −$369M / 56% MP / MP −10.5% (81.2%) / +$21M bimestre: en mano.
  - Venta perdida Farmacias de $139M a $171M (+24% vs 1S25): en mano, tabla CANÓNICA Rafael 16-jul (supersede cualquier corte previo de DP).
  - Los DOS cortes de Consumo (OTC +46.1% a 102.6% de meta vs UDN Consumo +23.7% a 81%): AMBOS en mano y AMBOS impresos; la definición del corte está pendiente [Rafael+IC]. No se elige en la lámina.
  - Impulso +$51M vs $32M plan; Expansión Friso +$16.4M, −5.1% vs −8.5% mercado: en mano.
- **Notas para el dibujante:**
  - El ÚNICO gold es "−$369M" en el panel de Farmacias (gap concentrado). Ni el 88.9% ni ningún otro número van en dorado.
  - Los DOS cortes de Consumo se dibujan LADO A LADO en la franja horizontal, ambos visibles, con el chip "[corte OTC vs Consumo por definir: Rafael+IC]" entre ellos; prohibido elegir uno, borrar el otro o marcar cuál "gana". (El chip es neutral: la palabra "honesto" NO se imprime.) Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27].
  - Los TRES paneles son del mismo ancho (tarjetas balanceadas, instrucción 16-jul); la historia de Farmacias domina por contenido (gold + 3 bullets), no por ancho.
  - Los deltas de encabezado de panel (−2.2%, +1.8%, +3.4%) van en BLANCO sobre la banda navy del header: el rojo sobre navy no lee (instrucción 16-jul) y el verde celebratorio sobre cifras propias está prohibido (KILL-LIST). El cumplimiento (88.9%, 95.4%, 93.8%) también en blanco neutro.
  - Signo menos tipográfico "−", no guion; "+" explícito. Tabular figures. Ningún carácter de flecha; "gana share y migra hacia arriba" (no símbolo).
  - Sin caja de insight, sin emojis, sin border-left, sin gradientes; título sin punto final.

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares. Estructura: banda de título arriba (~15%), cuerpo en TRES columnas del MISMO ancho (~1/3 cada una), debajo una franja horizontal de ancho completo (~14%), y un pie delgado abajo (~12%).

BANDA DE TÍTULO (ancho completo): título grande navy #0F2845 en peso ligero, dos líneas: "Farmacias concentra el deterioro del 1S; Impulso y Expansión defienden valor con elasticidad y mezcla". Debajo, subtítulo en itálica gris #44546A: "El gap de Farmacias fue capacidad y liberación, no demanda, y ya se corrige desde mayo".

PANEL IZQUIERDO (1/3), con banda de encabezado navy oscuro #0F2845 y TODO el texto en blanco negrita (incluido el delta; nada de rojo ni verde en los encabezados): "Farmacias · 88.9% de meta · −2.2%". Cuerpo blanco con borde fino gris #C5CDD9, esquinas suaves. Dentro: una línea con la cifra pivote "Concentra el gap del bloque: −$369M (56% es marca propia)", donde "−$369M" va en negrita grande color DORADO #C5A55A (ÚNICO elemento dorado de toda la lámina). Debajo, tres viñetas gris #3D4A5F: "Marca propia −10.5% (81.2% de meta): fue capacidad y liberación, no demanda."; "Ya se corrige: MP crece desde mayo, +$21M el bimestre."; "Venta perdida empeoró: de $139M a $171M (+24% vs 1S25)."

PANEL CENTRAL (1/3), con banda de encabezado azul #0F4C81 y TODO el texto en blanco negrita: "Impulso · 95.4% de meta · +1.8%". Cuerpo blanco con borde fino gris #C5CDD9. Dentro: una cifra en negrita navy #0F2845 "Elasticidad que funcionó: +$51M de beneficio de precio vs $32M de plan". Debajo, una viñeta gris #3D4A5F: "Valor sobre volumen deliberado: se subió precio sin perder el volumen esperado."

PANEL DERECHO (1/3), con banda de encabezado azul #0F4C81 y TODO el texto en blanco negrita: "Expansión · 93.8% de meta · +3.4%". Cuerpo blanco con borde fino gris #C5CDD9. Dentro: una cifra en negrita navy #0F2845 "Friso gana share y migra hacia arriba: mezcla +$16.4M". Debajo, una viñeta gris #3D4A5F: "En un mercado premium que se hunde: Friso −5.1% contra −8.5% del mercado."

FRANJA HORIZONTAL DE CONSUMO (ancho completo, bajo los tres paneles): título pequeño en negrita navy #0F2845: "Consumo crece fuerte: dos cortes en la mesa". Debajo, los DOS cortes dibujados lado a lado, ambos visibles, en gris #3D4A5F: "Sublínea OTC (sell-in): +46.1% · 102.6% de meta" y "UDN Consumo (canal): +23.7% · 81% de meta". Entre los dos cortes, un chip rectangular con fondo gris muy claro #F0F3F7 y borde fino gris #C5CDD9, texto gris #8A95A8 literal: "[corte OTC vs Consumo por definir: Rafael+IC]".

PIE (ancho completo): línea fina gris #E5E9EE; a la izquierda, itálica gris #8A95A8 chica: "Fuente: Sell-In PiSA cierre jun-26 (Retail por canal); venta perdida: tabla consolidada Comercial 16-jul-26; UDN Consumo y sublínea OTC del deck del canal Farmacias; elasticidad Impulso y mezcla Friso: análisis del canal 1S-2026". A la derecha: "PiSA Confidencial | 14".

Reglas estrictas: el ÚNICO elemento dorado es "−$369M" del panel de Farmacias. Los DOS cortes de Consumo (OTC +46.1% y UDN Consumo +23.7%) se dibujan lado a lado, ambos visibles, con el chip "[corte OTC vs Consumo por definir: Rafael+IC]" literal (placeholder interno del borrador; se eliminará antes de la versión final); no elijas uno ni marques cuál gana. Los TRES paneles tienen el mismo ancho. Los deltas de los encabezados van en BLANCO sobre la banda de color (sin rojo, sin verde). Signo menos tipográfico "−"; "+" explícito. Ningún carácter de flecha; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin gradientes; sin rayas largas (em-dash) en la prosa; español con acentos; título sin punto final.
```


---

# Lamina 15 · Elasticidad, servicio y Friso funcionaron; el gap se concentró en marca propia y down-trading

- **Momento:** M3 · Retail: entorno, 1S, 2S (43.6% de la venta)

- **Encabezado:** Elasticidad, servicio y Friso funcionaron; el gap se concentró en marca propia y down-trading
  (2 líneas: "Elasticidad, servicio y Friso funcionaron;" / "el gap se concentró en marca propia y down-trading". Calibri Light 32 pt, #0F2845, sentence case, sin punto final.)

- **So-what subtitle:** n/a (el título carga la implicación; deck de Consejo sobrio, sin caja de insight)

- **Layout:** banda de título 15% + cuerpo 75% (DOS tablas independientes lado a lado 50/50, ancho completo 12.53 in con márgenes 0.4 in; los conteos difieren: 5 renglones "bien" vs 7 "faltó") + pie 10% (fuente + confidencial + página). Formato 16:9 (13.333 × 7.5 in).

- **Zona por zona:**

  **Zona única · Tabla doble "bien / faltó" (dos tablas independientes lado a lado):**
  - Tipo: dos tablas independientes del mismo ancho (los conteos difieren: 5 vs 7). Sin líneas verticales; header con fondo #0F4C81 y texto blanco Calibri bold 12 pt; filas alternas blanco / #E8F1F8 (la alternancia ARRANCA igual en ambas columnas: zebra alineada); separadores horizontales 1 px #E5E9EE; texto de celdas Calibri Light 12 pt #3D4A5F, alineado a la izquierda, con guion inicial "– " por bullet.
  - Header columna izquierda: **Qué hicimos bien en el 1S**
  - Header columna derecha: **Qué nos faltó en el 1S**
  - Celdas columna izquierda (texto final, en este orden):
    1. Elasticidad en Impulso: +$51M de precio contra $32M plan, con el volumen esperado
    2. Corrección de raíz en marca propia: negados a la baja; MP crece desde mayo
    3. Servicio 95%+ seis semanas: RX cerró junio en 101% de meta
    4. Friso gana share y defiende valor vía mezcla (+$16.4M) en mercado que cae
    5. Lanzamientos aportan +$43.8M al puente (Sitagliptina, Votripax B+L, Pisagot)
  - Celdas columna derecha (texto final, en este orden):
    1. Farmacias 88.9%: el gap de MP del 1S ya estaba hecho cuando el servicio volvió
    2. Down-trading −$197.9M: la marca cede al genérico propio en 5 franquicias identificadas
    3. Faltantes largos cedieron share caro de recuperar (Bufigen, Pisartra)
    4. Venta perdida de Farmacias empeoró: de $139M a $171M (+24% vs 1S25)
    5. El PIN de Expansión se duplicó (+102%, de $80M a $162M): planeación de demanda equivocada que no logramos vender
    6. NC comerciales y sanciones de Retail +14.4% (de $426.6M a $488.1M), cargadas por marca propia (+78%) e Impulso (+41%)
    7. El canal quedó saturado: 90-120 días de inventario
  - Los montos en cada celda llevan tabular figures. Signos explícitos + / −. NO colorear los montos con semáforo dentro de esta tabla: es radiografía en prosa, no tablero de deltas (los colores verde/rojo aquí leerían como aplauso/castigo; el balance lo dan las dos columnas).

- **Mensaje que manda la lamina:** el 1S de Retail deja tres palancas probadas (elasticidad, servicio recuperado, mezcla de Friso) y heridas medidas al peso (arranque de MP, down-trading de −$197.9M, venta perdida de Farmacias +24%, PIN de Expansión duplicado, NC de Retail +14.4% y saturación del canal); nada de lo que faltó es misterio: cada renglón tiene mecanismo y dueño en el plan 2S (lámina siguiente).

- **Fuente (pie de lamina):** Fuente: Sell-In cierre jun-26, 1S26 vs 1S25; down-trading, mezcla Friso y lanzamientos: matriz consolidada Downtrading FINAL 16-jul; venta perdida y PIN: tabla consolidada Comercial 16-jul-26; NC: Gross2Net ene-jun-26; DDI: intel de canal. Universo sell-in salvo indicación.

- **Estado del dato:**
  - Columna "bien": en mano (storyline v6 tal cual; cifras trazables a puente FINAL 16-jul y sell-in cierre junio).
  - Faltó-4 (venta perdida): ACTUALIZADO a la tabla canónica Rafael 16-jul: de $139M a $171M (+24%). El "+$27M vs 1S25" anterior queda SUPERSEDED (era corte DP); gana el canónico.
  - Faltó-5 (PIN Expansión +102%, de $80M a $162M): NUEVO 16-jul, tabla canónica PIN.
  - Faltó-6 (NC Retail +14.4%, de $426.6M a $488.1M; marca propia +78%, Impulso +41%): NUEVO 16-jul, Gross2Net. Taxonomía REAL: "NC comerciales y sanciones" (la línea "NC logísticas" NO existe).
  - Con los renglones nuevos la columna derecha queda en 7 vs 5 de la izquierda: los conteos difieren y NO se disfrazan.

- **Notas para el dibujante:**
  - Es la lámina más simple del bloque: tablas y nada más. NO agregar gráficas, iconos ni KPI cards. NO agregar caja de insight ni rotular bloques con etiquetas tipo "INSIGHT".
  - Sin gold en esta lámina. Sin semáforos.
  - Paridad visual entre columnas por ANCHO y formato (mismo ancho, mismo header, mismo gris): la simetría de peso comunica honestidad. Los conteos ya NO son iguales (5 vs 7); no estirar filas para emparejar ni recortar faltantes para que cuadre.
  - No reordenar los bullets: el orden es deliberado; los renglones nuevos (VP actualizada, PIN Expansión, NC) van en las posiciones 4, 5 y 6 de la columna derecha, antes de la saturación del canal.
  - Respetar la ortografía de cifras: "−$197.9M" (down-trading, cifra central canónica), "88.9%" (alcance Farmacias), "de $139M a $171M (+24%)" (venta perdida Farmacias). No redondear distinto.
  - Contexto de VP Retail (NO imprimible, para el speaker): la venta perdida de Retail total MEJORA de $360M a $352M (−2%); el deterioro es específico de Farmacias.
  - "Gap" está permitido; jamás "boquete".
  - Trampa: no convertir el "95%+ seis semanas" en un porcentaje puntual; es un rango sostenido, dejarlo como está.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color, sin viñetas decorativas. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; todos los números alineados a la derecha en las celdas de la tabla, con acentos en español.

LAYOUT en tres bandas horizontales:
- Banda de título (arriba, ~15% de la altura).
- Cuerpo (~75%): DOS tablas independientes del mismo ancho, lado a lado (50/50), que ocupan casi todo el ancho, con márgenes laterales estrechos. La izquierda tiene 5 renglones de contenido; la derecha tiene 7 (los conteos difieren y así se dibujan).
- Pie (~10%): línea de fuente y confidencial.

BANDA DE TÍTULO: título en dos líneas, tamaño grande, color navy oscuro #0F2845, sentence case, SIN punto final. Texto exacto:
"Elasticidad, servicio y Friso funcionaron;"
"el gap se concentró en marca propia y down-trading"

CUERPO — DOS TABLAS del mismo ancho. Sin líneas verticales. Cada tabla arranca con una fila de encabezado con fondo azul #0F4C81 y texto blanco en negrita. Las filas de contenido alternan fondo blanco y fondo azul muy claro #E8F1F8, arrancando ambas columnas con blanco (zebra alineada). Separadores horizontales finos gris claro #E5E9EE. Texto de celdas en gris #3D4A5F, alineado a la izquierda, cada bullet inicia con un guion "– ". Mismo ancho y mismo formato en ambas columnas; el número de filas difiere (5 vs 7) y NO se empareja artificialmente.

Encabezado columna izquierda (negrita, blanco): "Qué hicimos bien en el 1S"
Encabezado columna derecha (negrita, blanco): "Qué nos faltó en el 1S"

Celdas columna izquierda, en este orden exacto:
– "Elasticidad en Impulso: +$51M de precio contra $32M plan, con el volumen esperado"
– "Corrección de raíz en marca propia: negados a la baja; MP crece desde mayo"
– "Servicio 95%+ seis semanas: RX cerró junio en 101% de meta"
– "Friso gana share y defiende valor vía mezcla (+$16.4M) en mercado que cae"
– "Lanzamientos aportan +$43.8M al puente (Sitagliptina, Votripax B+L, Pisagot)"

Celdas columna derecha, en este orden exacto:
– "Farmacias 88.9%: el gap de MP del 1S ya estaba hecho cuando el servicio volvió"
– "Down-trading −$197.9M: la marca cede al genérico propio en 5 franquicias identificadas"
– "Faltantes largos cedieron share caro de recuperar (Bufigen, Pisartra)"
– "Venta perdida de Farmacias empeoró: de $139M a $171M (+24% vs 1S25)"
– "El PIN de Expansión se duplicó (+102%, de $80M a $162M): planeación de demanda equivocada que no logramos vender"
– "NC comerciales y sanciones de Retail +14.4% (de $426.6M a $488.1M), cargadas por marca propia (+78%) e Impulso (+41%)"
– "El canal quedó saturado: 90-120 días de inventario"

Los montos van con dígitos de ancho uniforme y signos + / − explícitos. NO colorear ningún monto de verde ni rojo: toda la tabla usa el mismo gris de texto, sin semáforo.

PIE (gris #8A95A8, itálica, tamaño pequeño):
"Fuente: Sell-In cierre jun-26, 1S26 vs 1S25; down-trading, mezcla Friso y lanzamientos: matriz consolidada Downtrading FINAL 16-jul; venta perdida y PIN: tabla consolidada Comercial 16-jul-26; NC: Gross2Net ene-jun-26; DDI: intel de canal. Universo sell-in salvo indicación."
Y a la derecha del pie: "PiSA Confidencial | 15"

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; border-left (barras verticales de color a la izquierda de bloques); verde celebratorio en cifras propias; agregar gráficas, iconos o KPI cards; usar color gold. Esta lámina no lleva gold ni semáforos: es solo la tabla.
```


---

# Lamina 16 · Retail ataca el 2S con precio, defensa de mezcla y NADAL ya medido palanca por palanca

- **Momento:** M3 · Retail: entorno, 1S, 2S (43.6% de la venta)

- **Encabezado:** Retail ataca el 2S con precio, defensa de mezcla y NADAL ya medido palanca por palanca
  (2 líneas: "Retail ataca el 2S con precio, defensa de mezcla" / "y NADAL ya medido palanca por palanca". Calibri Light 32 pt, #0F2845, sin punto final.)

- **So-what subtitle:** Julio arranca hipotecado por la compra adelantada de junio; el drenaje del Q3 es secuencia planeada, no sorpresa de octubre (Calibri Light 14 pt itálica, #44546A)

- **Layout:** banda de título + subtitle 16% + cuerpo 72% en 2 columnas 45/55 con gutter 0.15 in — columna izquierda: numerales del plan (alto completo); columna derecha apilada: tabla NADAL junio por UDN (~60% del alto) sobre panel de 5 franquicias down-trader (~40% del alto) — + banda inferior de aporte al hueco ~5% + línea de leyenda de placeholders + pie 4%. Formato 16:9.

- **Zona por zona:**

  **Zona 1 (columna izquierda, 45%) · Numerales del plan 2S (4 numerales comprimidos + 1 numeral NUEVO = 5, texto final):**
  1. Segundo incremento de precios en julio, con gestión de elasticidad por canal
  2. Defensa de la mezcla como palanca nueva: las 5 franquicias down-trader (panel derecho) son la lista de trabajo inicial, con defensa de marca de visita médica, surtido y condiciones por canal y arquitectura de precios del genérico propio
  3. Portafolio que empuja: ventana de 90 días en marca propia ($21M YTG ya cotizados, proyecto de 20 moléculas top-to-top con Ahorro) y lanzamientos con foco: el GAP anual proyecta 83% (Votripax 57%, Pisalak 68%, Pixiba 73%)
  4. Q3 de drenaje por diseño: DDI top de 120 a 70 días, concursos, CEDIs de drogueros, fachadas 100 (caso a 1,000); el plan invernal se factura en septiembre (orden 25-sep)
  5. El PIN de Expansión se duplicó (+102%, de $80M a $162M): la planeación de demanda de Expansión se corrige con el NADAL del 2S
  - Tipografía: Calibri Light 12 pt #3D4A5F; negrita Calibri solo en "palanca nueva", "drenaje por diseño" y "83%" (máximo 3-4 palabras en bold por lámina, no más).

  **Zona 2 (columna derecha superior, 55% × ~60% alto) · Tabla "NADAL junio por UDN: el real declarado":**
  - Tipo: tabla 5 columnas × 7 filas. Header fondo #0F4C81, texto blanco Calibri bold 11 pt; filas alternas blanco / #E8F1F8; números a la derecha con tabular figures; texto a la izquierda; sin líneas verticales.
  - Encabezados: UDN | Deseada jun ($M) | Real jun ($M) | Alcance jun | Deseada YTG ($M)
  - Filas (orden Farmacias, Impulso, Expansión del canal; RX al final como la palanca que se corrige):

    | UDN | Deseada jun ($M) | Real jun ($M) | Alcance jun | Deseada YTG ($M) |
    |---|---:|---:|---:|---:|
    | Marcas Propias | 10.4 | 10.2 | 98% | 102.5 |
    | Consumo | 5.2 | 4.5 | 87% | 66.0 |
    | Impulso | 6.2 | 4.1 | 66% | 70.0 |
    | Expansión | 2.2 | 4.1 | 186% | 45.5 |
    | RX | 5.5 | 0.0 | 0% | 76.0 |
    | Total | 29.5 | 22.9 | 78% | 360.0 |

  - Semáforo SOLO en la columna "Alcance jun" (es delta cuantitativo de alcance vs plan, escala de monitoreo, no aplauso): 98% y 186% en #2E7D4F; 87% en #C97A2B; 66% y 0% en #C00000; el 78% del total en #C97A2B. Fila Total en bold con border-top 2 px #0F2845.
  - Nota al pie de la tabla (Calibri Light 9 pt #8A95A8): "RX: palanca de catalogación Aldrosa/distribuidores arrancó sin ejecución en junio; se corrige en julio. KPIs mensuales desde julio."

  **Zona 3 (columna derecha inferior, 55% × ~40% alto) · Panel "Las 5 franquicias down-trader: la lista de trabajo":**
  - Esta lámina es la DUEÑA del detalle de franquicias del down-trading; las láminas de puente (L13) solo lo referencian.
  - Tipo: lista de trabajo en 5 renglones (franquicia a la izquierda, Mix $M 1S26 vs 1S25 a la derecha, tabular figures), bloque con fondo #FAFBFC y top border 2 pt #0F4C81 (nunca border-left). Sin rótulo de caja tipo "INSIGHT"; el título del panel es funcional: "Las 5 franquicias down-trader (Mix 1S26 vs 1S25, $M)".
    1. Ácido clavulánico + amoxicilina · −45.6
    2. Levofloxacino · −32.9
    3. Ceftriaxona · −24.7
    4. Enoxaparina de sodio · −21.3
    5. Fexofenadina · −15.9
  - Renglón de cierre del panel (Calibri Light 10 pt #5A6679): "Suma −$140.4M = 71% del down-trading del semestre (−$197.9M). Acción por franquicia: defensa de marca de visita médica, surtido y condiciones por canal, arquitectura de precios del genérico propio."
  - Los cinco valores Mix en #C00000 (deltas negativos, semáforo legítimo).

  **Zona 4 (banda inferior, ancho completo) · Aporte al hueco (chip único):**
  - Texto en una línea, Calibri Light 12 pt #1A2332, sobre fondo #F0F3F7: "Aporte de Retail al hueco del [96]: [monto por segmento: RC]" — los corchetes se dibujan tal cual, como placeholder visible. Notación "[96]" sin unidad: la unidad se declara solo en L1.

  **Zona 5 (línea de leyenda, sobre el pie):**
  - Calibri Light 8 pt #8A95A8: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

- **Mensaje que manda la lamina:** el plan 2S de Retail no es una lista de deseos: NADAL ya se mide palanca por palanca con el real de junio declarado (incluido el 0% de RX, que se corrige en julio), la palanca nueva de mezcla ataca 5 franquicias con nombre y apellido (71% del down-trading de −$197.9M que el 1S dejó medido), y la planeación de demanda de Expansión, cuyo PIN se duplicó, se corrige con el NADAL del 2S.

- **Fuente (pie de lamina):** Fuente: Plan NADAL jun-26 por UDN (deck canal Farmacias, 16-jul-26); matriz consolidada Downtrading FINAL 16-jul, sell-in 1S26 vs 1S25 (franquicias); PIN no solicitado 1S25 vs 1S26 (tabla canónica 16-jul); GAP de lanzamientos: BD&Portafolio MX, PIN 6+6 jun-26. Universos NADAL y sell-in en paneles separados, no se mezclan en una misma gráfica.

- **Estado del dato:**
  - Zona 1 (numerales): en mano (storyline v6, comprimidos de 6 a 4 por orden Rafael 16-jul); detalle del segundo incremento de precios y elasticidad por canal lo cierra [VJ].
  - Numeral 5 NUEVO (PIN Expansión $80M a $162M, +102%): en mano (tabla canónica PIN de Rafael, 16-jul). Contexto canónico: Retail F+I+E empeora +20% ($471M a $564M), cargado por Expansión.
  - Zona 2 (tabla NADAL): en mano (deck canal Farmacias L22-L26). La fila Total es suma aritmética de los 5 UDN (29.5 / 22.9 / 78% / 360.0), verificada; el deck del canal no imprime ese total: confirmar con Rafael si se muestra.
  - Zona 3 (franquicias −45.6 / −32.9 / −24.7 / −21.3 / −15.9 = −140.4, 71% de −197.9): en mano (matriz consolidada Downtrading FINAL 16-jul; cifras verificadas al peso). CAVEAT de citación del rango: central −$197.9M; si piden rango, piso −$144.4M "mínimo entre variantes" (sensibilidad composicional, no intervalo de confianza); el −$107.3M SOLO con etiqueta pre-arista FRISO.
  - Zona 4: placeholder [RC] (aporte de Retail al hueco del [96]; el [96] sigue por negociar con Heriberto antes del 20).
  - RETIRADO del imprimible: el cite "~$244M Farmacias + $70M Impulso" del v6 (corte sin Expansión, distinto del total $360M de la tabla): la tabla manda; el corte v6 queda en este registro por si Rafael lo quiere de vuelta.

- **Notas para el dibujante:**
  - Sin gold en esta lámina: el semáforo de la tabla NADAL ya carga el énfasis; agregar gold saturaría.
  - Los numerales quedaron en 5: 4 comprimidos del plan original de 6 + 1 nuevo (PIN Expansión). No re-expandir ni renumerar.
  - El verde de la columna "Alcance jun" es escala de monitoreo (junto con ámbar y rojo), no verde celebratorio suelto; OJO: el 186% de Expansión en verde convive con el numeral 5 que declara la falla de planeación de Expansión — si Rafael prefiere neutralizarlo, se cambia esa celda, no la escala.
  - La tabla NADAL NO lleva columna "Real YTG": el deck fuente repite el real de junio como real YTG (artefacto de copiado, inconsistencia documentada). Solo Deseada jun / Real jun / Alcance jun / Deseada YTG.
  - El "0%" de RX se muestra sin suavizar; la nota al pie explica el mecanismo. NO omitir la fila RX.
  - "Top-to-top" y "YTG" se quedan (anglicismos permitidos); "fachadas 100 (caso a 1,000)" se transcribe tal cual del v6 — es el programa de fachadas a 100 tiendas con caso de negocio a 1,000.
  - Todos los corchetes son PLACEHOLDER INTERNO (kill antes del 27): la línea de leyenda de la Zona 5 lo declara una sola vez; los nombres/iniciales de responsables no viajan al texto del deck final.
  - Cero em-dash y cero carácter de flecha en texto imprimible ("de 120 a 70 días", nunca con flecha). No dibujar flechas ni iconos decorativos en los numerales.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; números alineados a la derecha en las tablas, con acentos en español.

LAYOUT en bandas:
- Banda de título + subtítulo arriba (~16% de la altura).
- Cuerpo (~72%) en DOS columnas: izquierda 45% del ancho, derecha 55%, con separación estrecha. La columna derecha se divide en dos zonas apiladas: una tabla (superior, ~60% del alto) y un panel de lista (inferior, ~40% del alto).
- Banda inferior de ancho completo (~5%) con un placeholder gris.
- Línea de leyenda muy chica y pie (~4%).

TÍTULO en dos líneas, grande, navy oscuro #0F2845, sin punto final:
"Retail ataca el 2S con precio, defensa de mezcla"
"y NADAL ya medido palanca por palanca"
SUBTÍTULO debajo, en itálica gris-azulado #44546A, tamaño mediano:
"Julio arranca hipotecado por la compra adelantada de junio; el drenaje del Q3 es secuencia planeada, no sorpresa de octubre"

COLUMNA IZQUIERDA (45%) — lista numerada de 5 puntos, texto gris #3D4A5F, tamaño mediano. Negrita SOLO en las palabras "palanca nueva", "drenaje por diseño" y "83%". Texto exacto:
1. "Segundo incremento de precios en julio, con gestión de elasticidad por canal"
2. "Defensa de la mezcla como palanca nueva: las 5 franquicias down-trader (panel derecho) son la lista de trabajo inicial, con defensa de marca de visita médica, surtido y condiciones por canal y arquitectura de precios del genérico propio"
3. "Portafolio que empuja: ventana de 90 días en marca propia ($21M YTG ya cotizados, proyecto de 20 moléculas top-to-top con Ahorro) y lanzamientos con foco: el GAP anual proyecta 83% (Votripax 57%, Pisalak 68%, Pixiba 73%)"
4. "Q3 de drenaje por diseño: DDI top de 120 a 70 días, concursos, CEDIs de drogueros, fachadas 100 (caso a 1,000); el plan invernal se factura en septiembre (orden 25-sep)"
5. "El PIN de Expansión se duplicó (+102%, de $80M a $162M): la planeación de demanda de Expansión se corrige con el NADAL del 2S"

COLUMNA DERECHA SUPERIOR — TABLA titulada "NADAL junio por UDN: el real declarado". 5 columnas, 7 filas (encabezado + 5 UDN + fila Total). Encabezado con fondo azul #0F4C81 y texto blanco en negrita. Filas alternas blanco / azul muy claro #E8F1F8. Números a la derecha con dígitos de ancho uniforme; texto a la izquierda; sin líneas verticales.
Encabezados: "UDN" | "Deseada jun ($M)" | "Real jun ($M)" | "Alcance jun" | "Deseada YTG ($M)"
Filas (en este orden):
"Marcas Propias" | 10.4 | 10.2 | 98% | 102.5
"Consumo" | 5.2 | 4.5 | 87% | 66.0
"Impulso" | 6.2 | 4.1 | 66% | 70.0
"Expansión" | 2.2 | 4.1 | 186% | 45.5
"RX" | 5.5 | 0.0 | 0% | 76.0
"Total" | 29.5 | 22.9 | 78% | 360.0
SEMÁFORO SOLO en la columna "Alcance jun": pinta el texto de "98%" y "186%" en verde #2E7D4F; "87%" en ámbar #C97A2B; "66%" y "0%" en rojo #C00000; "78%" (fila Total) en ámbar #C97A2B. Ninguna otra columna se colorea. La fila Total va en negrita, con una línea superior gruesa navy #0F2845.
Nota al pie de la tabla, gris #8A95A8 pequeño: "RX: palanca de catalogación Aldrosa/distribuidores arrancó sin ejecución en junio; se corrige en julio. KPIs mensuales desde julio."

COLUMNA DERECHA INFERIOR — PANEL "Las 5 franquicias down-trader (Mix 1S26 vs 1S25, $M)". Fondo gris muy claro #FAFBFC con una línea superior de 2 pt azul #0F4C81 (NUNCA barra vertical a la izquierda). Sin rótulo de caja. Lista de 5 renglones: nombre de franquicia a la izquierda, valor a la derecha (dígitos uniformes). Los cinco valores en rojo #C00000 (son deltas negativos legítimos):
"Ácido clavulánico + amoxicilina" · −45.6
"Levofloxacino" · −32.9
"Ceftriaxona" · −24.7
"Enoxaparina de sodio" · −21.3
"Fexofenadina" · −15.9
Renglón de cierre del panel, gris #5A6679 pequeño: "Suma −$140.4M = 71% del down-trading del semestre (−$197.9M). Acción por franquicia: defensa de marca de visita médica, surtido y condiciones por canal, arquitectura de precios del genérico propio."

BANDA INFERIOR (ancho completo), fondo gris claro #F0F3F7, texto navy #1A2332: "Aporte de Retail al hueco del [96]: [monto por segmento: RC]" — dibuja los corchetes literalmente, en gris neutro, como placeholder visible; no rellenar.

LÍNEA DE LEYENDA (encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE (gris #8A95A8, itálica, pequeño): "Fuente: Plan NADAL jun-26 por UDN (deck canal Farmacias, 16-jul-26); matriz consolidada Downtrading FINAL 16-jul, sell-in 1S26 vs 1S25 (franquicias); PIN no solicitado 1S25 vs 1S26 (tabla canónica 16-jul); GAP de lanzamientos: BD&Portafolio MX, PIN 6+6 jun-26. Universos NADAL y sell-in en paneles separados, no se mezclan en una misma gráfica." A la derecha: "PiSA Confidencial | 16"

PROHIBIDO: el carácter de flecha en cualquier texto ("de 120 a 70 días" se escribe así, con palabras); em-dash; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; border-left; verde fuera de la columna de alcance indicada; usar color gold (esta lámina NO lleva gold). El único color de énfasis permitido es el semáforo en la columna "Alcance jun" y el rojo de los 5 valores de mix. No dibujar flechas ni iconos en los numerales.
```


---

# Lamina 17 · Gobierno: compra anulada por ~13,000 mdp y adeudos por ~14,000 mdp; PiSA cae −0.6% en un mercado −3.8%
- **Momento:** M4 · Gobierno: entorno, 1S, 2S (24.4% de la venta)
- **Encabezado:** Gobierno: compra anulada por ~13,000 mdp y adeudos por ~14,000 mdp; PiSA cae −0.6% en un mercado −3.8%
  (2 líneas. Sin insulto al cliente y sin múltiplo aritmético: el par −0.6% vs −3.8% se imprime tal cual; el "seis veces menos" NO se usa aquí — vive en L2 como texto de título.)
- **So-what subtitle:** Dos hechos duros con fuente pública, tres tendencias con lectura propia del canal y un mercado que se descapitaliza
- **Layout (REESCRITURA 16-jul):** Banda de título 16% + fila de dos hechos duros 26% + bloque de tres tendencias de una línea 24% + banda de descapitalización (1 línea) 10% + línea de leyenda de placeholders + footer 14%. Abre con los dos hechos duros (no con el numerito macro), mientras Edmundo entrega el dato macro por elegir.

## Zona por zona

### Zona A — Banda de título (16%)
- Título: Calibri Light 30-32 pt `#0F2845` (2 líneas).
- Subtítulo so-what: Calibri Light 14 pt italic `#44546A`.

### Zona B — Dos hechos duros con fuente (26%)
- Kicker de zona: "Dos hechos duros, con fuente pública" — Calibri bold 12 pt `#0F2845` (texto plano, no etiqueta de caja).
- Dos bloques lado a lado (mitad y mitad), cada uno con su cifra grande arriba y su fuente al pie:
  - Bloque 1 "Ejecución fallida": cifra "~13,000 mdp" (Calibri bold 22 pt `#0F2845`) · texto "compra consolidada anulada por sobreprecio; la ronda cubrió solo **50.5%** de claves" (Calibri Light 11 pt `#3D4A5F`) · fuente "(La Silla Rota / Forbes / El Financiero)" 9 pt `#8A95A8`.
  - Bloque 2 "No pagan": cifra "~14,000 mdp" (Calibri bold 22 pt GOLD `#C5A55A` — ÚNICO elemento gold de la lámina) · texto "adeudos a proveedores según la industria, contra ~5,000 mdp reconocidos por el gobierno" (Calibri Light 11 pt `#3D4A5F`) · fuente "(Expansión / El Informador)" 9 pt `#8A95A8`.
- Chip literal a la derecha de la fila, Calibri Light 9.5 pt `#8A95A8`: "[numerito macro único por elegir: Edmundo/Rafa]".
- (La franja de matiz "+5.9% real / −4.7% vs 2024" SALE del imprimible: es argumento en reserva del speaker, ver Guía de speaker.)

### Zona C — Tres tendencias de una línea (24%)
- Kicker de zona: "Tres tendencias, con lectura propia del canal" — Calibri bold 12 pt `#0F2845`.
- Lista numerada (Calibri Light 11 pt `#3D4A5F`); el arranque de cada renglón en Calibri bold `#0F2845`; UNA línea por tendencia (dos si el render lo exige, nunca tres):
  1. **Consolidada retrasada**: el proceso se difirió y arrastra el abasto del semestre.
  2. **Subatención de contratos**: nos piden por debajo de la meta. Universo pedidos: piden $3,901M de una meta de $3,993M y facturamos $3,235M.
  3. **La PI se endurece pro-innovador**: protección de datos 5 años y extensión de patente hasta +5 años (DOF abr-2026), Priority Watch List y revisión del T-MEC; los genéricos se retrasan.

### Zona D — Mercado que se descapitaliza (1 línea, 10%)
- Una sola línea (Calibri Light 10.5 pt `#3D4A5F`), con encabezado en bold navy integrado al renglón: "**Un mercado opaco que se descapitaliza:** INEFAM genéricos **−3.8%** en valor y **−12.5%** en piezas (ene-may); el no pago quiebra a los débiles: consolida a nuestro favor en 2027, en 2026 presiona precios."
- Deltas −3.8% y −12.5% en `#C00000` (deltas cuantitativos).

### Zona D2 — Línea de leyenda de placeholders (sobre el footer)
- Calibri Light 8 pt `#8A95A8`: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

### Zona E — Footer (14%)
- Línea 0.5 pt `#E5E9EE` + fuente al pie + "PiSA Confidencial | 17".

- **Mensaje que manda la lamina:** El entorno de Gobierno se resume en dos hechos con fuente pública (compra consolidada anulada por ~13,000 mdp con solo 50.5% de claves cubiertas; adeudos por ~14,000 mdp contra ~5,000 reconocidos), tres tendencias con lectura propia del canal y un mercado de genéricos que se descapitaliza (−3.8% valor / −12.5% piezas). En ese mercado, PiSA cae −0.6% contra −3.8% del mercado: el título lo dice sin adjetivos.
- **Fuente (pie de lamina):** Fuente: research externo con fuente pública (consolidada anulada, adeudos, marco de PI), jul-26; INEFAM genéricos gobierno ene-may-26; universo pedidos gobierno frasco cerrado (transcript 15-jul; cifras rotuladas como pedidos, no sell-in). El % del PIB en salud no se usa en esta lámina (decisión Rafael 16-jul)
- **Estado del dato:**
  - Dos hechos duros (consolidada anulada ~13,000 mdp / 50.5% claves; adeudos ~14,000 vs ~5,000): en mano (research público).
  - PiSA −0.6% vs mercado −3.8% (título): en mano (INEFAM ene-may vs sell-in PiSA; el par también se imprime en L2).
  - Numerito macro único: placeholder [Edmundo/Rafa]; el % PIB descartado por trillado (decisión Rafael 16-jul). El matiz "+5.9% real / −4.7% vs 2024" está en mano (research) pero vive SOLO en la Guía de speaker.
  - Tendencia 2 (pedidos $3,901M / meta $3,993M / facturación $3,235M): universo pedidos, IMPRESO SOLO porque va rotulado como pedidos; el puente pedidos-facturación-venta neta sigue por declarar [DS/Dani] (pendiente en registro, ya no como chip impreso).
  - INEFAM genéricos −3.8% valor / −12.5% piezas: en mano (INEFAM ene-may).
  - VP/PIN de Gobierno: PENDIENTES canónicos (definición única de venta perdida por cerrar; nada de 463/443.9 como headline). No entran a esta lámina.
  - RETIRADOS del imprimible (viven en registro/speaker): AlphaDog +30-35% (RECHAZADO por Rafael, en re-validación [Chery]); bullets de competidores por clave/erosión/% compras directas [Chery/DS]; tendencias SS/Birmex/IMSS/ISSSTE [Felipe + Hugo Bobadilla]; cambios de cuadros en la Secretaría de Salud (a voz, sin nombres).
- **Notas para el dibujante:**
  - El ÚNICO gold es "~14,000 mdp" (adeudos). El "~13,000 mdp" de la consolidada va en navy.
  - La lámina ABRE con los dos hechos duros; el numerito macro es un chip placeholder, NUNCA el % del PIB en salud. No rellenarlo.
  - "Lectura propia del canal" es la fórmula obligada; PROHIBIDO el término "información privilegiada" en cualquier texto (término legal).
  - Las cifras del universo pedidos ($3,901 / $3,993 / $3,235) se imprimen SOLO rotuladas como "Universo pedidos"; ese universo NO se mezcla con el sell-in ni se conecta con flechas.
  - Los deltas negativos (−3.8%, −12.5%) en rojo `#C00000`; las cifras de contexto (~13,000, ~14,000, 50.5%) en neutro salvo el gold.
  - La buena nueva de Gobierno (devoluciones −27.2%, +$198M) NO va aquí: vive en L18/L19/L20. No adelantarla.
  - Cero stage directions impresas ("matiz en reserva", "para no revirar", "que no se pueden revirar" y equivalentes): la instrucción de speaker vive en la Guía de speaker.
  - Signo menos tipográfico "−", no guion; "+" explícito. Cero em-dash y cero carácter de flecha en texto imprimible.
  - Los corchetes son PLACEHOLDER INTERNO (kill antes del 27), declarado una sola vez en la línea de leyenda.
  - Sin caja de insight, sin emojis, sin border-left, sin gradientes; título sin punto final.
- **Guía de speaker (NO se dibuja):**
  - Matiz anti-revire, en reserva: el presupuesto 2026 creció +5.9% real y aun así queda −4.7% contra lo ejercido en 2024. Se usa solo si el Consejo revira con "el gobierno sí tiene dinero".
  - Cambios de cuadros: relevos en la Secretaría de Salud (la baja de la principal aliada del abasto) se comentan A VOZ, sin nombres impresos ni dichos con apellido en la lámina.
  - Regla de la sección: no abrir el debate "queremos venderle a quien no paga" (superado hace dos años). Si el Consejo lo saca, el racional está listo (margen ~25%, PiSA tiene capital para aguantar la cartera, ventaja de compras/volumen/costos; gobierno es ~60% del volumen de plantas, la nueva fábrica de oncológicos destina 95% ahí). Alinear postura con Juan Jaime [Dirección].
  - AlphaDog +30-35% para pedidos de genéricos: RECHAZADO y en re-validación [Chery]; no citarlo como dato ni a voz como vigente.
  - Pendientes de contenido (fuera del imprimible): tendencias SS / Birmex / IMSS / ISSSTE [Felipe + Hugo Bobadilla]; bullets de competidores por clave con dato [Chery/DS]; puente pedidos-facturación-venta neta [DS/Dani].

### Contenido diferido a anexo
- **Franja de matiz presupuestal** (antes impresa): "El presupuesto 2026 creció +5.9% real y aun así queda −4.7% contra lo ejercido en 2024." — pasa a Guía de speaker; si Rafael quiere un anexo de macro, esta línea es el candidato, con el numerito macro único que elija Edmundo.
- **Detalle de descapitalización** (antes 2 líneas + chips): mecanismo completo "el no pago quiebra a los jugadores débiles: a mediano plazo (2027) consolida el mercado a nuestro favor, en 2026 juega en contra (liquidan inventario vía impulso y presionan precios)" + bullets de competidores por clave, erosión y % de compras directas [con dato: Chery/DS].
- **Tendencias institucionales por cerrar**: SS / Birmex / IMSS / ISSSTE [Felipe + Hugo Bobadilla].

## Instrucciones ChatGPT Images 2

```
Diseña una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negrita solo donde se indique; TODOS los números en figuras tabulares. Estructura en bandas horizontales apiladas, con aire: esta lámina tiene poco texto a propósito.

BANDA 1 (título, ~16%): título grande navy #0F2845 en peso ligero, dos líneas: "Gobierno: compra anulada por ~13,000 mdp y adeudos por ~14,000 mdp; PiSA cae −0.6% en un mercado −3.8%". Debajo, subtítulo en itálica gris #44546A: "Dos hechos duros con fuente pública, tres tendencias con lectura propia del canal y un mercado que se descapitaliza".

BANDA 2 (dos hechos duros, ~26%): arriba, en negrita navy #0F2845 pequeño, texto plano: "Dos hechos duros, con fuente pública". Debajo, dos bloques lado a lado (mitad y mitad), cada uno con una cifra grande arriba y su fuente chica al pie:
- Bloque izquierdo "Ejecución fallida": cifra "~13,000 mdp" en negrita navy #0F2845; texto gris #3D4A5F "compra consolidada anulada por sobreprecio; la ronda cubrió solo 50.5% de claves" (el "50.5%" en negrita); fuente gris #8A95A8 "(La Silla Rota / Forbes / El Financiero)".
- Bloque derecho "No pagan": cifra "~14,000 mdp" en negrita color DORADO #C5A55A (ÚNICO elemento dorado de toda la lámina); texto gris #3D4A5F "adeudos a proveedores según la industria, contra ~5,000 mdp reconocidos por el gobierno"; fuente gris #8A95A8 "(Expansión / El Informador)".
A la derecha de la fila, un chip literal gris #8A95A8 chico: "[numerito macro único por elegir: Edmundo/Rafa]".

BANDA 3 (tres tendencias, ~24%): arriba, en negrita navy #0F2845 pequeño: "Tres tendencias, con lectura propia del canal". Debajo, una lista numerada en gris #3D4A5F, UNA línea por tendencia, con el arranque de cada renglón en negrita navy #0F2845:
1. "Consolidada retrasada: el proceso se difirió y arrastra el abasto del semestre."
2. "Subatención de contratos: nos piden por debajo de la meta. Universo pedidos: piden $3,901M de una meta de $3,993M y facturamos $3,235M."
3. "La PI se endurece pro-innovador: protección de datos 5 años y extensión de patente hasta +5 años (DOF abr-2026), Priority Watch List y revisión del T-MEC; los genéricos se retrasan."

BANDA 4 (descapitalización, ~10%): UNA sola línea, arranque en negrita navy #0F2845 y resto gris #3D4A5F: "Un mercado opaco que se descapitaliza: INEFAM genéricos −3.8% en valor y −12.5% en piezas (ene-may); el no pago quiebra a los débiles: consolida a nuestro favor en 2027, en 2026 presiona precios." Los deltas "−3.8%" y "−12.5%" en rojo #C00000.

LÍNEA DE LEYENDA (encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

BANDA 5 (pie, ~14%): línea divisoria gris #E5E9EE; debajo, a la izquierda en itálica gris #8A95A8 chico: "Fuente: research externo con fuente pública (consolidada anulada, adeudos, marco de PI), jul-26; INEFAM genéricos gobierno ene-may-26; universo pedidos gobierno frasco cerrado (transcript 15-jul; cifras rotuladas como pedidos, no sell-in). El % del PIB en salud no se usa en esta lámina (decisión Rafael 16-jul)"; a la derecha: "PiSA Confidencial | 17".

Reglas estrictas: el ÚNICO elemento dorado es "~14,000 mdp" (adeudos); el "~13,000 mdp" de la consolidada va en navy. El numerito macro es un chip placeholder literal, NUNCA un porcentaje del PIB. PROHIBIDO imprimir "información privilegiada", "matiz en reserva", "para no revirar" o cualquier instrucción de speaker. Las cifras de pedidos van SIEMPRE precedidas del rótulo "Universo pedidos" y nunca se conectan con el sell-in. Todos los corchetes se dibujan literales y completos, en gris neutro, sin ámbar ni rojo. Signo menos tipográfico "−", no guion; "+" explícito. Ningún carácter de flecha ni em-dash; sin emojis; sin rótulos de caja INSIGHT/SO WHAT; sin borde izquierdo; sin gradientes; español con acentos; título sin punto final.
```


---

# Lámina 18 · En Gobierno FC defendimos el valor comprando volumen: −$320.3M de deflación de licitación compensada con +$425.2M de piezas
- **Momento:** M4 · Gobierno: entorno, 1S, 2S (24.4% de la venta)
- **Encabezado:** En Gobierno FC defendimos el valor comprando volumen: −$320.3M de deflación de licitación compensada con +$425.2M de piezas
- **So-what subtitle:** Sell-in FC de $4,059.2M a $4,034.3M (−$24.9M, 90.0% de meta), idéntico en los tres niveles de conciliación; la pregunta del 2S es cuánto volumen más aguanta la red
- **Layout:** banda de título 15% + cuerpo 66% en tres columnas 15/50/35 (col 1 mercado vs PiSA · col 2 puente de ventas REAL de 8 componentes · col 3 palancas comerciales) + caveat de universo 9% + footer 10%. Geometría 13.333 × 7.5 in, márgenes 0.5 in, área útil 12.333 in. Título y 0.5–1.55 in; cuerpo y 1.65–6.3 in; caveat y 6.35–6.75 in; footer y 6.85–7.1 in. Anchos de columna dentro del área útil: col 1 ≈ 1.8 in, col 2 ≈ 6.0 in, col 3 ≈ 4.2 in, gutter 0.15 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 1.0 in).**
Título asertivo Calibri Light 28-30 pt `#0F2845` (2 líneas), sin punto final; so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Cuerpo, tres columnas (convención de puente 15/50/35).**

*Columna 1 (15%, ≈1.8 in) — Mercado vs PiSA. Gráfica de dos barras.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845` (texto plano, sin marco): "Mercado vs PiSA".
- Dos barras verticales, eje Y en % de crecimiento (arranca en 0 hacia abajo, ambas negativas), sin gridlines, sin leyenda:
  - Barra 1: **INEFAM genéricos −3.8%** (valor, ene-may) — relleno `#8A95A8` (gris, es el mercado), data label "−3.8%".
  - Barra 2: **Gobierno FC −0.6%** (sell-in 1S) — relleno `#0F4C81` (navy, es PiSA), data label "−0.6%".
- Corchete/llave vertical entre los topes de ambas barras con el callout **"6 veces menos"** en Calibri bold 12 pt `#C5A55A` (gold). ÚNICO elemento gold de la lámina.
- Nota bajo la gráfica, Calibri Light 9 pt `#5A6679`: "INEFAM = genéricos de gobierno, valor, ene-may; PiSA = sell-in FC, 1S. Universos distintos, mismo signo."

*Columna 2 (50%, ≈6.0 in) — Puente de ventas 1S25 a 1S26 (REAL). Waterfall de 8 componentes.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Puente de ventas, ocho componentes (−$24.9M, idéntico en los 3 niveles)".
- Eyebrow de universo, Calibri Light 9 pt `#5A6679`: "Sell-in FC · matriz Downtrading FINAL 16-jul · cobertura core PiSA 78.9% del bruto elegible".
- Waterfall de 10 barras, $M, eje Y desde 0, connectors punteados 0.5 pt `#C5CDD9`, data label con signo sobre cada barra:
  - Barra inicial (navy `#0F2845`): **$4,059.2M** — data label "1S25 · $4,059.2M".
  - Ocho barras de componente:
    1. "Precio" — **−320.3** — rojo `#C00000` (la mayor negativa: deflación de licitación).
    2. "Volumen" — **+425.2** — navy `#0F4C81` (la mayor barra del puente, hacia arriba).
    3. "Mix (core PiSA)" — **−84.6** — rojo `#C00000`.
    4. "Gestión de portafolio" — **+19.5** — navy `#0F4C81`.
    5. "Lanzamientos" — **+0.2** — navy `#0F4C81` (un filo con etiqueta).
    6. "Terceros" — **−53.3** — rojo `#C00000`.
    7. "Servicios / serie 9" — **−10.4** — rojo `#C00000` (chica).
    8. "Sin unidad (por valor)" — **−1.2** — rojo `#C00000` (un filo).
  - Barra final (navy `#0F2845`): **$4,034.3M** — data label "1S26 · $4,034.3M (90.0% de meta)".
- Nota de conciliación (una línea), Calibri Light 9 pt `#8A95A8`: "Sin reclasificaciones: la Δ de −$24.9M es idéntica en los tres niveles (reclasificada = con MATNR = cubo)."
- Anotaciones bajo el chart, Calibri Light 9.5 pt `#3D4A5F`, dos renglones de una línea:
  - "Volumen top: FLEBOTEK +$105.0M · Eritropoyetina +$71.7M · Heparina +$71.2M; en el mix core, FLEBOTEK pone −$46.9M (55% del efecto)."
  - "Gestión +$19.5M = bajas −$64.6M y altas de licitación +$84.1M; en terceros, KETOSTERIL +$30.1M (alta) y BIOYETIN −$33.2M (baja). Neto core PiSA (P+V+M+gestión) +$39.8M."

*Columna 3 (35%, ≈4.2 in) — Palancas comerciales 1S25 vs 1S26. Cuatro renglones.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Palancas comerciales, 1S25 vs 1S26".
- Renglones 1-2 con eyebrow "universo PEDIDOS / DP", renglones 3-4 con eyebrow "Gross2Net Finanzas":
  1. Venta perdida — silueta placeholder gris `#E5E9EE` con chip literal: "[definición única pendiente: DS/FM]". SIN cifra: ni $463M ni $443.9M se imprimen como headline.
  2. PIN no solicitado — silueta placeholder gris `#E5E9EE` con chip literal: "[pendiente + comparador 25]".
  3. NC comerciales y sanciones — dos barras: "1S-2025 = −$103.0M" (`#8A95A8`) y "1S-2026 = −$111.7M" (`#0F4C81`, más larga); etiqueta en rojo `#C00000` "empeora $8.7M".
  4. Devoluciones — dos barras: "1S-2025 = −$729.7M" (`#8A95A8`) y "1S-2026 = −$531.5M" (`#0F4C81`, claramente MÁS CORTA); etiqueta en navy bold `#0F4C81` (sin verde): "mejora +$198M (−27.2%), la palanca real del segmento".

**Zona C — Caveat de universo (12.333 × 0.4 in).**
Texto Calibri Light 9.5 pt `#8A95A8`, dos renglones: "Venta perdida y PIN de gobierno viven en el universo PEDIDOS y están pendientes de definición única; NC y devoluciones vienen del Gross2Net de Finanzas (taxonomía: NC comerciales y sanciones + devoluciones). El puente pedidos-facturación-venta neta ($3,901M / $3,235M / $4,034.3M) está pendiente [DS] y vive en anexo."

**Zona D — Footer (12.333 × 0.25 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 18" derecha.

## Mensaje que manda la lámina
Gobierno FC defendió el valor comprando volumen: la deflación de licitación le quitó −$320.3M y el segmento la compensó con +$425.2M de piezas (FLEBOTEK, Eritropoyetina, Heparina, insulinas), para cerrar casi plano (−$24.9M). El neto del core PiSA es +$39.8M. La pregunta que la lámina deja armada para el 2S es de sostenibilidad: cuánto volumen adicional aguanta la red para seguir compensando la deflación. La palanca real del segmento en ejecución son las devoluciones: mejoran +$198M.

## Fuente (pie de lámina)
Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In cierre jun-26, Gobierno FC 1S26 vs 1S25 (cobertura core 78.9% del bruto elegible); mercado: INEFAM genéricos gobierno ene-may-26; NC y devoluciones: Gross2Net Finanzas; venta perdida y PIN: universo PEDIDOS, definición única pendiente (DS/FM).

## Estado del dato
- Col 1 (INEFAM −3.8% vs FC −0.6%): **en mano** (storyline v6; universos declarados en nota).
- Col 2 (puente completo Precio −320.3 / Volumen +425.2 / Mix −84.6 / Gestión +19.5 / Lanzamientos +0.2 / Terceros −53.3 / Serie 9 −10.4 / Sin unidad −1.2 = −24.9): **en mano y verificado al peso** (matriz consolidada FINAL 16-jul; suma exacta a un decimal; Δ idéntica en los 3 niveles de conciliación). SUPERSEDE las 5 siluetas "[equipo PVM]" y la referencia 2-vías (−8.1 / −16.8) de la versión anterior.
- Detalle de anotaciones (FLEBOTEK +105.0 / EPO +71.7 / Heparina +71.2; mix FLEBOTEK −46.9 = 55%; gestión = bajas −64.6 + altas licitación +84.1; KETOSTERIL +30.1 / BIOYETIN −33.2; core neto +39.8): **en mano** (matriz + trazabilidad del EXTRACT).
- CHOQUE RESUELTO: el "diagnóstico parcial de mix +$112.8M, FC sube de gama (cobertura 55%)" de la versión anterior queda SUPERSEDED por el Mix core canónico −$84.6M con cobertura 78.9%; no viaja ni a anexo como cifra válida.
- Col 3: NC −103.0 a −111.7 y devoluciones −729.7 a −531.5 (+$198M, −27.2%): **en mano** (Gross2Net). Venta perdida y PIN de gobierno: **pendientes** — la definición única de VP sigue abierta (candidatos en anexo, NUNCA como headline) y el PIN de gobierno espera cifra + comparador 2025.
- Los conteos 428/330/108 del transcript de gobierno son PIEZAS/conteos, no $M: quedan fuera de la lámina (los $330M/$357M/$108M de la versión anterior estaban mal etiquetados como $M).
- Choque con EXTRACT declarado en Notas: el deck de David Silva rotula meta FC $3,901M y venta $3,235M (universo pedidos, 83%); el v6 usa sell-in $4,034.3M / 90.0%. Manda el v6; el pedidos vive en anexo con su puente.

## Notas para el dibujante
- El ÚNICO gold de la lámina es el callout "6 veces menos" de la columna 1. Nada más en gold; la mejora de devoluciones (+$198M) va en navy bold `#0F4C81`, no en gold ni en verde.
- Proporciones relativas del waterfall: Volumen +425.2 es la barra flotante más grande (hacia arriba); Precio −320.3 la mayor negativa; Mix −84.6 mediana; Terceros −53.3 chica-mediana; Gestión +19.5 y Serie 9 −10.4 chicas; Lanzamientos +0.2 y Sin unidad −1.2 son filos con etiqueta.
- SIN verde en ninguna barra ni etiqueta: positivos navy `#0F4C81`, negativos rojo `#C00000`, anclas navy `#0F2845`. El rojo es semáforo cuantitativo sobre deltas, no decoración.
- Las siluetas placeholder de VP y PIN (col 3) van en gris `#E5E9EE` SIN cifra; sus chips se dibujan literales en gris `#8A95A8`, sin ámbar/rojo ni iconos. Prohibido imprimir $463M o $443.9M como headline de venta perdida.
- Todos los corchetes con responsable ([DS/FM], [DS]) son PLACEHOLDER INTERNO — kill antes del 27: viven en el storyboard de revisión, no en la versión del Consejo.
- Signo menos tipográfico "−" en los negativos; no usar el carácter de flecha en ningún texto (el puente se lee "1S25 a 1S26").
- NO mezclar universos: col 1 y col 2 son sell-in; en col 3, los renglones 1-2 son PEDIDOS/DP y los 3-4 Gross2Net, cada par con su eyebrow. El caveat de Zona C es obligatorio y no se abrevia.
- NO desplegar el universo PEDIDOS completo (pedidos $3,901M, no atendido $704M y su desglose $544/$90/$70): sin el puente pedidos-facturación-venta neta esa cascada NO se muestra; vive en anexo.
- Tabular figures en toda cifra. Sin líneas verticales. Sin border-left. Sin caja de insight ni rótulos de bloque.

### Contenido diferido a anexo
- A ANEXO: inventario de candidatos de venta perdida de gobierno, pendiente de definición única [DS/FM]: $342M (restricto) · $443.9M (DP) · $463M · $595-600M. Ninguno se imprime como headline en L18 hasta que la definición cierre.
- A ANEXO: PIN no solicitado de gobierno: por planchar las dos cifras del canal (859 vs 869) y construir el comparador 2025 [responsables del canal gobierno].
- A ANEXO: conteos del transcript de gobierno 428 / 330 / 108 — son PIEZAS/conteos de NC, no $M; no se mezclan con el Gross2Net.
- A ANEXO: puente pedidos-facturación-venta neta ($3,901M / $3,235M / $4,034.3M) [DS], prerrequisito para desplegar el universo PEDIDOS completo.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; TODAS las cifras en figuras tabulares; acentos en español.

ESTRUCTURA EN BANDAS: banda de título arriba (~15%); cuerpo al centro (~66%) dividido en TRES columnas de anchos 15% / 50% / 35% de izquierda a derecha; una banda de caveat de dos renglones (~9%); y un pie delgado abajo (~10%).

BANDA DE TÍTULO (ancho completo): título grande navy oscuro #0F2845, sans-serif ligera, sin punto final, hasta dos líneas: "En Gobierno FC defendimos el valor comprando volumen: −$320.3M de deflación de licitación compensada con +$425.2M de piezas". Debajo, en gris azulado #44546A pequeño e itálica: "Sell-in FC de $4,059.2M a $4,034.3M (−$24.9M, 90.0% de meta), idéntico en los tres niveles de conciliación; la pregunta del 2S es cuánto volumen más aguanta la red". Línea horizontal fina gris #E5E9EE de margen a margen.

COLUMNA IZQUIERDA (15%) — arriba, texto plano navy #0F2845 negrita, pequeño: "Mercado vs PiSA". Debajo, una gráfica de DOS barras verticales, eje en % (ambas negativas, hacia abajo desde cero), sin gridlines, sin leyenda. Barra 1 rellena en gris #8A95A8 con etiqueta "−3.8%" (INEFAM genéricos, el mercado). Barra 2 rellena en navy #0F4C81 con etiqueta "−0.6%" (PiSA Gobierno FC), visiblemente MENOS profunda que la barra 1 (cae seis veces menos). Entre los topes de ambas barras, un corchete vertical rotulado en DORADO #C5A55A negrita: "6 veces menos" (este es el ÚNICO elemento dorado de toda la lámina). Bajo la gráfica, texto pequeño gris #5A6679: "INEFAM = genéricos de gobierno, valor, ene-may; PiSA = sell-in FC, 1S. Universos distintos, mismo signo."

COLUMNA CENTRAL (50%) — arriba, texto plano navy #0F2845 negrita: "Puente de ventas, ocho componentes (−$24.9M, idéntico en los 3 niveles)". Debajo, en gris #5A6679 muy pequeño: "Sell-in FC · matriz Downtrading FINAL 16-jul · cobertura core PiSA 78.9% del bruto elegible". Debajo, una gráfica de cascada (waterfall) de DIEZ barras con conectores punteados finos gris #C5CDD9, eje Y en millones desde 0, etiqueta de valor con signo sobre cada barra. De izquierda a derecha:
1. Barra ancla "1S25 · $4,059.2M" — sólida navy oscuro #0F2845, alta.
2. "Precio" = "−320.3" — negativa, roja #C00000, la negativa MÁS GRANDE (deflación de licitación).
3. "Volumen" = "+425.2" — positiva, azul #0F4C81, la barra flotante MÁS GRANDE de todo el puente.
4. "Mix (core PiSA)" = "−84.6" — negativa, roja #C00000, mediana.
5. "Gestión de portafolio" = "+19.5" — positiva, azul #0F4C81, chica.
6. "Lanzamientos" = "+0.2" — positiva, azul #0F4C81, un filo con etiqueta.
7. "Terceros" = "−53.3" — negativa, roja #C00000, chica-mediana.
8. "Servicios / serie 9" = "−10.4" — negativa, roja #C00000, chica.
9. "Sin unidad (por valor)" = "−1.2" — negativa, roja #C00000, un filo.
10. Barra ancla "1S26 · $4,034.3M (90.0% de meta)" — sólida navy oscuro #0F2845, alta (apenas más baja que la inicial).
Bajo la gráfica, en gris #8A95A8 pequeño: "Sin reclasificaciones: la Δ de −$24.9M es idéntica en los tres niveles (reclasificada = con MATNR = cubo)." Y en gris #3D4A5F, dos renglones: "Volumen top: FLEBOTEK +$105.0M · Eritropoyetina +$71.7M · Heparina +$71.2M; en el mix core, FLEBOTEK pone −$46.9M (55% del efecto)." y "Gestión +$19.5M = bajas −$64.6M y altas de licitación +$84.1M; en terceros, KETOSTERIL +$30.1M (alta) y BIOYETIN −$33.2M (baja). Neto core PiSA (P+V+M+gestión) +$39.8M."

COLUMNA DERECHA (35%) — arriba, texto plano navy #0F2845 negrita: "Palancas comerciales, 1S25 vs 1S26". Debajo, cuatro renglones; los renglones 1-2 llevan arriba un eyebrow gris muy pequeño "universo PEDIDOS / DP" y los renglones 3-4 un eyebrow "Gross2Net Finanzas":
1. "Venta perdida" — una silueta rectangular gris muy claro #E5E9EE SIN cifra, con el chip literal en gris #8A95A8: "[definición única pendiente: DS/FM]".
2. "PIN no solicitado" — una silueta gris muy claro #E5E9EE SIN cifra, con el chip literal en gris #8A95A8: "[pendiente + comparador 25]".
3. "NC comerciales y sanciones" — dos barras horizontales pares: "1S-2025 = −$103.0M" en gris #8A95A8 y "1S-2026 = −$111.7M" en azul #0F4C81 apenas más larga; etiqueta en rojo #C00000: "empeora $8.7M".
4. "Devoluciones" — dos barras horizontales pares: "1S-2025 = −$729.7M" en gris #8A95A8 y "1S-2026 = −$531.5M" en azul #0F4C81 claramente MÁS CORTA; etiqueta en azul navy #0F4C81 negrita (NO verde): "mejora +$198M (−27.2%), la palanca real del segmento".

BANDA DE CAVEAT (ancho completo, dos renglones, gris #8A95A8 pequeño): "Venta perdida y PIN de gobierno viven en el universo PEDIDOS y están pendientes de definición única; NC y devoluciones vienen del Gross2Net de Finanzas (taxonomía: NC comerciales y sanciones + devoluciones). El puente pedidos-facturación-venta neta ($3,901M / $3,235M / $4,034.3M) está pendiente [DS] y vive en anexo."

PIE (ancho completo): línea fina gris #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In cierre jun-26, Gobierno FC 1S26 vs 1S25 (cobertura core 78.9% del bruto elegible); mercado: INEFAM genéricos gobierno ene-may-26; NC y devoluciones: Gross2Net Finanzas; venta perdida y PIN: universo PEDIDOS, definición única pendiente (DS/FM)." A la derecha: "PiSA Confidencial | 18".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde en cualquier barra o etiqueta (la mejora de devoluciones va en azul navy); más de un elemento en dorado (solo el callout "6 veces menos"); imprimir cifra alguna en las siluetas de venta perdida y PIN o rellenar cualquier corchete. El signo menos es "−" tipográfico, no un guion; español con acentos; título sin punto final.
```


---

# Lámina 19 · Gobierno cerró en 90.0% de meta y la cartera subió +22%, pero en la contracción ganamos +17.7 pts de share
- **Momento:** M4 · Gobierno: entorno, 1S, 2S (24.4% de la venta)
- **Encabezado:** Gobierno cerró en 90.0% de meta y la cartera subió +22%, pero en la contracción ganamos +17.7 pts de share
  (Título REORDENADO 16-jul para cerrar en lo controlado: abre con el faltante, cierra con el share ganado, que es lo que hicimos nosotros.)
- **So-what subtitle:** Radiografía del 1S de Gobierno FC: cinco aciertos, cinco faltantes; las palancas comerciales viajan como candidatos
- **Layout:** banda de título 15% + cuerpo 80% (dos tablas independientes lado a lado, ~6.0 in de ancho cada una, gutter 0.3 in; zebra ALINEADA: ambas arrancan la alternancia en blanco y las alturas de fila se emparejan renglón a renglón) + footer 5%. Geometría 13.333 × 7.5 in; márgenes 0.5 in; área útil 12.333 × 6.5 in. Título y 0.5–1.55 in; cuerpo y 1.65–6.6 in; footer y 6.7–7.0 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 1.0 in, arriba).**
Título asertivo Calibri Light 28 pt `#0F2845` (2 líneas), sin punto final; so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Tabla doble "bien / faltó" (cuerpo completo, dos tablas independientes lado a lado).**
Los conteos difieren (4 vs 5 renglones); ambas columnas pesan visualmente igual (mismo ancho, mismo formato, mismo gris de texto).

*Columna izquierda — header:* fondo `#0F2845`, texto blanco Calibri bold 13 pt, alineado izquierda: **"Qué hicimos bien en el 1S"**. Renglones alternos blanco / `#F0F3F7`, texto Calibri Light 11.5 pt `#3D4A5F`, viñeta guion corto gris, border inferior 1 px `#E5E9EE`, sin líneas verticales. Contenido final (verbatim):
1. PiSA #1 en volumen del sector público (82.5M pzs INEFAM)
2. En nuestra canasta de 105 claves el mercado cae 31.7% y subimos a 42.7% de share (+17.7 pts) [unidad y base por rotular: DS]: ganamos share en la contracción
3. Q2 de FC al 99% en junio; IMSS +12.1%
4. NC (conteo de notas) -53% vs 2025 [candidato: 428 notas vs base 25 por cerrar; universo conteos, NO $M]
5. Devoluciones de gobierno mejoraron -27.2% (+$198M vs 1S25): la palanca operativa real del segmento

*Columna derecha — header:* mismo formato: **"Qué nos faltó en el 1S"**. Contenido final (verbatim):
1. FC quedó en 90.0% y -0.6% (Q1 ~88%)
2. No nos piden lo suficiente: subatención de contratos [candidato, universo pedidos]
3. Venta perdida de gobierno se deterioró [definición única en cierre: DS/FM]
4. PIN no solicitado ~$859M: planeación de demanda equivocada que no logramos vender [candidato]
5. Cartera: +22% vs cierre 2025 ($4,834M al 30-jun; FC 5.3 meses de venta, Servicios 3.4); IMSS Bienestar -43.1%

**Zona C — Footer (12.333 × 0.3 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 19" derecha.

## Mensaje que manda la lámina
Gobierno FC es una historia de dos caras: quedó a 10 pts de meta con cartera creciendo y fallas de ejecución comercial (venta perdida, PIN no solicitado), pero ganó participación de forma agresiva en un mercado que se contrae (share +17.7 pts sobre una canasta que cae 31.7%) y las devoluciones mejoraron -27.2% (+$198M), la palanca operativa que sí controlamos; los faltantes se dicen sin adjetivar y los números aún no canónicos viajan como candidatos.

## Fuente (pie de lámina)
Fuente: Sell-In cierre jun-26, Gobierno FC 1S26 vs 1S25; share INEFAM canasta de 105 claves; cartera Finanzas al 30-jun-26; devoluciones: Gross2Net ene-jun-26; NC (conteos), venta perdida y PIN: universo PEDIDOS / DP, candidatos [por conciliar: DS/FM/Dani].

## Estado del dato
- Columna "bien": renglones 1-3 **en mano** (storyline v6); renglón 2 con chip nuevo "[unidad y base por rotular: DS]" para el 42.7%. Renglón 4 (NC -53%) **candidato** (428 vs base 2025 por cerrar), impreso con su corchete y RE-ETIQUETADO como conteo de notas: los 428/330/108 del transcript son PIEZAS/conteos, NO $M (caveat README); no mezclar con Gross2Net. OJO: en Gross2Net las NC comerciales de Gob FC EMPEORAN (de $103.0M a $111.7M, +8.4%); si el candidato de conteos no se concilia el 21, el renglón 4 se corta.
- Renglón "bien" 5 (devoluciones -27.2%, de $729.7M a $531.5M = +$198M): **en mano, CANÓNICO** (Gross2Net 16-jul). NUEVO por instrucción de Rafael.
- Columna "faltó": renglón 1 y 5 **en mano** (90.0% / -0.6%; cartera $4,834M / +22% / 5.3 y 3.4 meses / Bienestar -43.1% del deck de David Silva y cartera Finanzas). Renglones 2, 3 y 4 **candidatos** (subatención universo pedidos; venta perdida sin definición única, NADA de 463/443.9 como headline; PIN de gobierno PENDIENTE como cifra canónica), impresos con sus corchetes.

## Notas para el dibujante
- Deck de Consejo sobrio: SIN caja de insight, sin rotular bloques con "INSIGHT"/"SO WHAT" ni equivalentes. Los headers llevan exactamente "Qué hicimos bien en el 1S" / "Qué nos faltó en el 1S", nada más.
- Las dos columnas pesan IGUAL: mismo ancho, mismo formato, mismo gris. Nada de verde en "bien" ni rojo en "faltó" — es radiografía, no boleta. Deltas y signos menos en el mismo `#3D4A5F` del texto; sin semáforos en prosa.
- ZEBRA ALINEADA (16-jul): la alternancia blanco/`#F0F3F7` arranca igual en ambas columnas y las alturas de fila se emparejan renglón a renglón (renglón 1 izquierdo a la misma altura que renglón 1 derecho, y así); con 5 vs 5 renglones la retícula debe verse como UNA tabla partida en dos.
- Negritas: máximo 3-4 palabras en toda la lámina (sugerido: "+17.7 pts" en bien-2 y "90.0%" en faltó-1). No más.
- Los corchetes de candidato y de responsable se dibujan literales, en gris `#8A95A8` dentro del renglón, sin ámbar/rojo ni iconos. Prohibido rellenarlos o estimarlos. Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27].
- La frase "Servicios compensó el semestre de Gobierno" fue ELIMINADA por el consejo adversarial (contradecía la tesis "los alegres no compensan"): NO reintroducirla en ningún renglón.
- SIN gold en esta lámina (no hay cifra pivotal única; el equilibrio de las dos caras es el mensaje).
- Signo menos tipográfico "−"; no usar el carácter de flecha en ningún texto.
- Tabular figures en toda cifra. Sin líneas verticales. Sin border-left. No agregar KPIs ni gráficas: la venta y el puente ya se mostraron en la L18.
- Nivel de venta del segmento NO se imprime aquí (vive en L18, $4,034.3M sell-in); esta lámina no repite cifras de venta base.

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha en tablas. Márgenes amplios y homogéneos.

ESTRUCTURA VERTICAL: banda de título arriba (~15% de la altura), cuerpo al centro con DOS columnas iguales lado a lado 50/50 (~80%), y un pie delgado abajo (~5%).

BANDA DE TÍTULO (arriba, ancho completo): título en dos líneas, sans-serif ligera, color navy oscuro #0F2845, sin punto final: "Gobierno cerró en 90.0% de meta y la cartera subió +22%, pero en la contracción ganamos +17.7 pts de share". Debajo, en gris azulado #44546A, pequeño e itálica: "Radiografía del 1S de Gobierno FC: cinco aciertos, cinco faltantes; las palancas comerciales viajan como candidatos". Una línea horizontal fina gris claro #E5E9EE separa el título del cuerpo, de margen a margen.

CUERPO: dos tablas independientes del mismo ancho, una a la izquierda y otra a la derecha, con un espacio entre ellas. Ambas pesan visualmente IGUAL (mismo ancho, mismo formato, mismo gris de texto). La alternancia de fondos ARRANCA igual en ambas (zebra alineada) y las alturas de fila se emparejan renglón a renglón, de modo que la retícula se lea como una sola tabla partida en dos. No usar verde en la izquierda ni rojo en la derecha; todo el texto de los renglones en gris #3D4A5F. Sin líneas verticales. Sin bordes laterales de color.

COLUMNA IZQUIERDA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué hicimos bien en el 1S". Debajo, 5 renglones con fondo alternado blanco / gris muy claro #F0F3F7, cada renglón con una viñeta de guion corto gris y una línea inferior fina gris claro #E5E9EE. Texto de los renglones (verbatim):
1. "PiSA #1 en volumen del sector público (82.5M pzs INEFAM)"
2. "En nuestra canasta de 105 claves el mercado cae 31.7% y subimos a 42.7% de share (+17.7 pts) [unidad y base por rotular: DS]: ganamos share en la contracción"
3. "Q2 de FC al 99% en junio; IMSS +12.1%"
4. "NC (conteo de notas) -53% vs 2025 [candidato: 428 notas vs base 25 por cerrar; universo conteos, NO $M]"
5. "Devoluciones de gobierno mejoraron -27.2% (+$198M vs 1S25): la palanca operativa real del segmento"
Dentro de esta columna, solo "+17.7 pts" del renglón 2 va en negrita. Los corchetes se dibujan literales, en gris, sin color de alerta (son placeholders internos del borrador).

COLUMNA DERECHA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué nos faltó en el 1S". Debajo, 5 renglones con el mismo formato alternado blanco / gris muy claro #F0F3F7, misma viñeta de guion. Texto de los renglones (verbatim):
1. "FC quedó en 90.0% y -0.6% (Q1 ~88%)"
2. "No nos piden lo suficiente: subatención de contratos [candidato, universo pedidos]"
3. "Venta perdida de gobierno se deterioró [definición única en cierre: DS/FM]"
4. "PIN no solicitado ~$859M: planeación de demanda equivocada que no logramos vender [candidato]"
5. "Cartera: +22% vs cierre 2025 ($4,834M al 30-jun; FC 5.3 meses de venta, Servicios 3.4); IMSS Bienestar -43.1%"
Dentro de esta columna, solo "90.0%" del renglón 1 va en negrita. Los corchetes "[candidato, universo pedidos]", "[definición única en cierre: DS/FM]" y "[candidato]" se dibujan literales, en gris, sin color de alerta.

PIE (abajo, ancho completo): una línea fina gris claro #E5E9EE arriba del pie. A la izquierda, texto pequeño en itálica gris #8A95A8: "Fuente: Sell-In cierre jun-26, Gobierno FC 1S26 vs 1S25; share INEFAM canasta de 105 claves; cartera Finanzas al 30-jun-26; devoluciones: Gross2Net ene-jun-26; NC (conteos), venta perdida y PIN: universo PEDIDOS / DP, candidatos [por conciliar: DS/FM/Dani]." A la derecha, mismo estilo: "PiSA Confidencial | 19".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde celebratorio en las cifras propias; cualquier semáforo de color en los renglones; cualquier elemento en dorado (esta lámina no lleva gold). El signo menos en los deltas ("-0.6%", "-53%", "-43.1%") va en el mismo gris del texto, no en rojo, y es "−" tipográfico, no un guion.
```


---

# Lamina 20 · El plan 2S de Gobierno depende de surtir y cobrar, no de que el gobierno pague pronto

- **Momento:** M4 · Gobierno: entorno, 1S, 2S (24.4% de la venta)

- **Encabezado:** El plan 2S de Gobierno depende de surtir y cobrar, no de que el gobierno pague pronto
  (2 líneas: "El plan 2S de Gobierno depende de surtir y cobrar," / "no de que el gobierno pague pronto". Calibri Light 32 pt, #0F2845, sin punto final.)

- **So-what subtitle:** La bianual no es viento a favor en 2026: fallo diferido al 28-ago-26 y primeros pedidos hasta enero 2027 (Calibri Light 14 pt itálica, #44546A)

- **Layout:** banda de título + subtitle 16% + cuerpo 70% en 2 columnas 55/45 con gutter 0.15 in — columna izquierda: bullets del plan; columna derecha: calendario duro de la bianual (timeline horizontal) — + banda inferior de riesgo y aporte al hueco ~10% + pie 4%. Formato 16:9.

- **Zona por zona:**

  **Zona 1 (columna izquierda, 55%) · Bullets del plan 2S (5 bullets, texto final):**
  1. NADAL Gobierno FC: claves, PIN y Bienestar ($110.4M en may-jun a 60% de efectividad, total del plan asignado a FC); YTG con KPIs mensuales
  2. Cumplimiento de contratos y cobranza como foco del semestre, con meta en pesos y fecha [cifra cobrada al 30-sep: DS]: cartera medida junio contra junio, cartera entre venta de los últimos doce meses
  3. Separar sanciones de las notas de crédito para leer el síntoma correcto
  4. Sostener la mejora de devoluciones: +$198M ya capturados en el 1S (-27.2% vs 1S25, Gross2Net); es la palanca operativa que ya probó
  5. Bianual consolidada, dicho por nosotros: no es viento a favor en 2026 (calendario a la derecha; detalle de contratos en anexo)
  - Tipografía: Calibri Light 12 pt #3D4A5F; negrita Calibri solo en "surtir y cobrar" si se usa en algún bullet — preferible sin negritas aquí (máx. 3-4 palabras bold por lámina y el título ya carga el mensaje).

  **Zona 2 (columna derecha, 45%) · Calendario duro de la bianual 2027-28 (mapa-esquema / timeline):**
  - Tipo: línea de tiempo horizontal con 3 hitos sobre una regla de jul-26 a ene-27. Línea base 1.5 pt #C5CDD9; marcadores circulares 10 px.
  - Hito 1 (izquierda): "27-jul-26 · Hoy, esta junta" (marcador #8A95A8, texto Calibri Light 11 pt #5A6679)
  - Hito 2 (centro): "28-ago-26 · Fallo de la bianual (3,831 claves)" (marcador en #C5A55A gold — el ÚNICO elemento gold de la lámina; texto Calibri bold 12 pt #0F2845)
  - Hito 3 (derecha): "ene-27 · Primeros pedidos" (marcador #0F4C81, texto Calibri Light 12 pt #1A2332)
  - Corchete o llave horizontal bajo el tramo ago-26 a dic-26 con la leyenda: "2026 cierra sin un peso de la bianual: el 2S se gana con los contratos vigentes" (Calibri Light 11 pt #5A6679).
  - Título funcional de la zona (Calibri bold 12 pt #0F2845): "Bianual 2027-28: calendario duro"

  **Zona 3 (banda inferior, ancho completo) · Riesgo declarado + aporte al hueco:**
  - Bloque de fondo #F0F3F7 (sin border-left; sin rótulo de caja). Dos líneas de texto, Calibri Light 12 pt #1A2332:
    - Línea 1: "Riesgo, dicho por nosotros: el gobierno sigue sin pagar; el plan del 2S no depende de que pague pronto, depende de surtir bien lo contratado y cobrar con disciplina."
    - Línea 2: "Aporte de Gobierno al hueco del [96]: [dato: RC]" (placeholder dibujado tal cual; notación única "[96]", sin unidad: la unidad solo se declara en L1).

- **Mensaje que manda la lamina:** el 2S de Gobierno se gana con lo que ya está contratado (surtir bien, cobrar con disciplina, NADAL con KPIs); la bianual la decimos nosotros antes de que la pregunten: fallo el 28-ago-26 y pedidos hasta enero 2027, cero viento a favor este año.

- **Fuente (pie de lamina):** Fuente: Plan NADAL Gobierno FC jun-26; cartera Finanzas al 30-jun-26; bianual 2027-28: fallo diferido al 28-ago-26, 3,831 claves (prensa especializada, jul-26). Universos NADAL y cartera; el calendario de la bianual es fuente pública.

- **Estado del dato:**
  - Zona 1: bullets en mano (storyline v6). Bullet 1 RESUELTO por el orquestador contra la fuente (HANDOFF 0725 §3.4/§7.7): $110.4M = NADAL Gobierno may-jun ×60% plano, TODO asignado a Frasco Cerrado (las iniciativas del plan en gobierno son claves, PIN y Bienestar). Se imprime $110.4M; confirmación de cortesía con DS.
  - Bullet 4 (devoluciones +$198M, -27.2%): NUEVO 16-jul, en mano, CANÓNICO (Gross2Net: de $729.7M a $531.5M); continuidad de la palanca que la L19 reporta como "bien".
  - Zona 2: en mano (research consolidado 10-jul, cifra citable #9: fallo diferido 28-ago-26, 3,831 claves; pedidos ene-27).
  - Zona 3: riesgo en mano (v6); aporte al hueco = placeholder [RC]; el [96] sigue por negociar con Heriberto antes del 20 (en imprimible siempre "[96]" a secas).
  - Lámina soporte de contratos y cartera vive en Anexo B [DS]; esta lámina no la duplica.

- **Notas para el dibujante:**
  - El ÚNICO gold de la lámina es el marcador del hito 28-ago-26. Nada más en gold.
  - Todo corchete con responsable ([cifra cobrada al 30-sep: DS], [dato: RC]) es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris y se elimina antes de la sesión.
  - Cero em-dash en el texto imprimible (la línea 1 de la banda inferior ya va con coma); notación "[96]" sin unidad.
  - NO dibujar semáforos: no hay deltas cuantitativos en esta lámina.
  - NO meter aquí los números de cartera ($4,834M, +22%, 5.3 meses): viven en la lámina 19 (bien/faltó) y en el Anexo B. El bullet 2 se queda en el "cómo se mide", sin cifras.
  - NO abrir el universo PEDIDOS en esta lámina (pedidos $3,901M, no atendido $704M, etc. son [candidato] y viven en las láminas 17-18); aquí solo palancas y calendario.
  - Regla de la sección (no se imprime, se cuida): NO abrir el debate "queremos venderle a quien no paga"; la lámina no debe insinuarlo ni con iconografía.
  - El timeline lee de izquierda a derecha con el tiempo; no invertir. Sin flechas decorativas: la línea con marcadores basta.
  - "Dicho por nosotros" es tono deliberado (anticipar el riesgo antes de que lo digan ellos): conservar la frase en la banda inferior.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; acentos en español.

LAYOUT en bandas:
- Banda de título + subtítulo arriba (~16% de la altura).
- Cuerpo (~70%) en DOS columnas: izquierda 55% del ancho (bullets), derecha 45% (una línea de tiempo horizontal).
- Banda inferior de ancho completo (~10%) con dos líneas de texto sobre fondo gris claro.
- Pie (~4%).

TÍTULO en dos líneas, grande, navy oscuro #0F2845, sin punto final:
"El plan 2S de Gobierno depende de surtir y cobrar,"
"no de que el gobierno pague pronto"
SUBTÍTULO debajo, itálica gris-azulado #44546A, mediano:
"La bianual no es viento a favor en 2026: fallo diferido al 28-ago-26 y primeros pedidos hasta enero 2027"

COLUMNA IZQUIERDA (55%) — lista de 5 bullets, texto gris #3D4A5F, tamaño mediano, sin negritas. Texto exacto:
1. "NADAL Gobierno FC: claves, PIN y Bienestar ($110.4M en may-jun a 60% de efectividad, total del plan asignado a FC); YTG con KPIs mensuales"
2. "Cumplimiento de contratos y cobranza como foco del semestre, con meta en pesos y fecha [cifra cobrada al 30-sep: DS]: cartera medida junio contra junio, cartera entre venta de los últimos doce meses"
3. "Separar sanciones de las notas de crédito para leer el síntoma correcto"
4. "Sostener la mejora de devoluciones: +$198M ya capturados en el 1S (-27.2% vs 1S25, Gross2Net); es la palanca operativa que ya probó"
5. "Bianual consolidada, dicho por nosotros: no es viento a favor en 2026 (calendario a la derecha; detalle de contratos en anexo)"
El corchete "[cifra cobrada al 30-sep: DS]" se dibuja literal, en gris neutro, como placeholder visible (placeholder interno del borrador); no rellenar.

COLUMNA DERECHA (45%) — LÍNEA DE TIEMPO horizontal. Título funcional arriba, navy #0F2845 en negrita: "Bianual 2027-28: calendario duro". Una regla/base horizontal fina gris #C5CDD9 que corre de izquierda (jul-26) a derecha (ene-27), con 3 marcadores circulares. El tiempo corre de izquierda a derecha; no invertir. Sin flechas decorativas.
- Marcador izquierdo, círculo gris #8A95A8, texto gris #5A6679: "27-jul-26 · Hoy, esta junta"
- Marcador central, círculo COLOR GOLD #C5A55A (este es el ÚNICO elemento gold de toda la lámina), texto navy #0F2845 en negrita: "28-ago-26 · Fallo de la bianual (3,831 claves)"
- Marcador derecho, círculo azul #0F4C81, texto navy #1A2332: "ene-27 · Primeros pedidos"
Debajo del tramo que va de ago-26 a dic-26, una llave/corchete horizontal con la leyenda en gris #5A6679: "2026 cierra sin un peso de la bianual: el 2S se gana con los contratos vigentes"

BANDA INFERIOR (ancho completo), fondo gris claro #F0F3F7, sin barra vertical de color, texto navy #1A2332 en dos líneas (sin rayas largas):
Línea 1: "Riesgo, dicho por nosotros: el gobierno sigue sin pagar; el plan del 2S no depende de que pague pronto, depende de surtir bien lo contratado y cobrar con disciplina."
Línea 2: "Aporte de Gobierno al hueco del [96]: [dato: RC]" — corchetes dibujados literalmente como placeholder gris; no rellenar.

PIE (gris #8A95A8, itálica, pequeño): "Fuente: Plan NADAL Gobierno FC jun-26; cartera Finanzas al 30-jun-26; bianual 2027-28: fallo diferido al 28-ago-26, 3,831 claves (prensa especializada, jul-26). Universos NADAL y cartera; el calendario de la bianual es fuente pública." A la derecha: "PiSA Confidencial | 20"

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; semáforos (verde/ámbar/rojo) — esta lámina NO tiene deltas cuantitativos, todo el texto va en los grises y navy indicados; usar gold en cualquier elemento que no sea el marcador del 28-ago-26; rótulos de caja tipo "INSIGHT" o "RIESGO"; border-left. No meter cifras de cartera aquí.
```


---

# Lamina 21 · Crecemos +5.1% mientras el pagador cambia el juego: aseguradoras al límite y ocupación de 59%

- **Momento:** M5 · Hospitales: entorno, 1S, 2S (18.5% de la venta)

- **Encabezado:** Crecemos +5.1% mientras el pagador cambia el juego: aseguradoras al límite y ocupación de 59%
  (1 línea de 87 caracteres, cabe en el límite de 110; si el master exige 2 líneas: "El pagador cambia el juego: aseguradoras al límite" / "y hospital con 59% de ocupación". Calibri Light 32 pt, #0F2845, sin punto final.)

- **So-what subtitle:** El efecto duro llega en Q4-2026, al vencer las últimas pólizas contratadas antes del cambio de IVA (Calibri Light 14 pt itálica, #44546A)

- **Layout:** banda de título + subtitle 15% + cuerpo 71% en 2 filas — fila superior ~35% del cuerpo: KPI row de 4 tarjetas (aseguradoras) + línea de lectura; fila inferior ~65% del cuerpo en 3 columnas 32/36/32: (a) bullets "el hospital pierde tráfico", (b) proxy de tráfico con 2 mini-gráficas de línea apiladas, (c) placeholder vista IQVIA — + franja "el pagador también cambia de dueños" 6% + pie 8%. Formato 16:9.

- **Zona por zona:**

  **Zona 1 (fila superior, ancho completo) · KPI row "la crisis del pagador, con datos duros" (4 tarjetas):**
  - Tipo: 4 KPI cards iguales, separación por border 0.5 pt #E5E9EE (una sola técnica, sin fondo adicional). Label Calibri Light 10.5 pt #5A6679 UPPERCASE; valor Calibri bold 40 pt #0F2845 tabular; contexto Calibri Light 10 pt #5A6679.
    1. SINIESTRALIDAD GMM · **~$131,000M** · cierre 2025, +14.7% vs 2024
    2. PRIMAS GMM 2026 · **+6-10%** · general; hasta +40% en adultos mayores
    3. INFLACIÓN MÉDICA · **14.8%** · cuatro veces la inflación general
    4. IVA NO ACREDITABLE · **16%** · pagos directos, Ley 2026: encarece pólizas
  - Línea de lectura bajo las tarjetas (Calibri Light 12 pt #3D4A5F, 1 línea): "Las aseguradoras cubren 80-85% del costo e intervienen el flujo: compra directa a quirófano y redirección del gasto."

  **Zona 2 (fila inferior, columna a, 32%) · Bullets "el hospital pierde tráfico" (texto final, sin em-dash):**
  1. Ocupación hospitalaria privada 59%, 21 pts bajo el estándar de 80%; quirófanos ~50%
  2. El pagador redirige el flujo oncológico: el hospital marca 300-400% la quimio (según nuestras conversaciones con pagadores) y el flujo migra a centros de infusión (Alivia ~15 clínicas, COI/FESA 12 sedes)
  3. Las mezclas se commoditizan
  - Título funcional de la zona (Calibri bold 12 pt #0F2845): "El hospital pierde tráfico"

  **Zona 3 (fila inferior, columna b, 36%) · Proxy propio de tráfico: 2 mini-gráficas de línea apiladas:**
  - Título funcional: "Tráfico hospitalario, proxy propio: venta en piezas vs promedio 2025"
  - **Mini-gráfica 1 — "Equipo para bomba (miles de piezas)":**
    - Eje X: Ene · Feb · Mar · Abr · May · Jun (2026). Eje Y truncado 80-110 (anotar el corte de eje con doble raya; permitido en líneas si se declara).
    - Serie 2026 (línea 2 pt #0F4C81): 96.3 / 94.6 / 100.6 / 94.2 / 92.4 / 105.1
    - Línea base punteada 1.5 pt #8A95A8, constante: 104.5 ("promedio 2025"), rotulada directo sobre la línea, sin leyenda flotante.
    - Data labels: solo Jun (105.1) y la base (104.5), Calibri Light 10 pt #1A2332.
    - Anotación (Calibri Light 10 pt #5A6679): "junio recupera: 105.1 vs base 104.5; abr-may fueron el valle"
  - **Mini-gráfica 2 — "Soluciones (millones de piezas)":**
    - Eje X: Ene-Jun 2026. Eje Y truncado 1.6-2.6 (anotado).
    - Serie 2026 (línea 2 pt #0F4C81): 2.16 / 2.09 / 2.32 / 1.99 / 1.95 / 2.32
    - Línea base punteada 1.5 pt #8A95A8, constante: 2.14 ("promedio 2025"), rotulada directo.
    - Data labels: solo Jun (2.32) y la base (2.14).
  - Sin gridlines (o #E5E9EE 0.5 pt máximo); ejes #5A6679, labels Calibri Light 10 pt.
  - Chip bajo las dos mini-gráficas, Calibri Light 9.5 pt #8A95A8, fondo #F0F3F7, borde 0.5 pt #C5CDD9, dibujado literal: "[series mismas tiendas vs totales: por confirmar, equipo canal]".

  **Zona 4 (fila inferior, columna c, 32%) · Vista IQVIA del mercado hospitalario — PLACEHOLDER declarado:**
  - Tipo: recuadro de borde punteado 1 pt #C5CDD9, fondo blanco, texto centrado.
  - Texto del placeholder (Calibri Light 12 pt #8A95A8): "[dato: CC · vista IQVIA del mercado hospitalario: tamaño y crecimiento]"
  - Microcopy bajo el placeholder (Calibri Light 9 pt #8A95A8): "El reporte IQVIA de abril NO cubre el canal hospitalario; corte específico en gestión. Esta vista valida además el −5% de la tablita."
  - NO dibujar ninguna gráfica provisional ni cifra tentativa dentro del recuadro.

  **Zona 5 (franja de una línea, ancho completo, encima del pie) · El pagador también cambia de dueños (recibida desde L22, 16-jul):**
  - UNA línea, Calibri Light 11 pt #3D4A5F, sin caja o con fondo #FAFBFC y top border 1 pt #C5CDD9 (nunca border-left): "El pagador también cambia de dueños: fondos y grupos entran al hospital y la clínica privada (PC Capital, General Atlantic, Hospiten)."
  - Nada más en la franja: ni cifras, ni logos, ni segunda oración.

- **Mensaje que manda la lamina:** el entorno de Hospitales no es una anécdota de un trimestre: el pagador (aseguradoras con siniestralidad récord, primas al alza e IVA no acreditable) está redirigiendo el flujo, el hospital opera al 59% de ocupación, y nuestro proxy propio de piezas confirma el valle de abril-mayo con recuperación en junio. El golpe fuerte llega en Q4-2026.

- **Fuente (pie de lamina):** Fuente: siniestralidad GMM: CNSF/AMIS, cierre 2025; primas 2026: AMIS/EKA/WTW vía El Universal; ocupación: IntelLat vía Milenio, nov-25; inflación médica e IVA: El Economista, 10-may-26; centros de infusión, markup quimio y propiedad hospitalaria (PC Capital/General Atlantic/Hospiten): lectura propia del canal y research jul-26. Proxy de tráfico: sell-in piezas PiSA Eq/Bomba y Soluciones, ene-jun-26 vs promedio 2025. Vista de mercado hospitalario IQVIA: por integrar [CC].

- **Estado del dato:**
  - Zona 1 (KPIs aseguradoras): en mano (research consolidado 10-jul, cifras citables #5-#7, con fuente pública).
  - Zona 2 (bullets): en mano; el 300-400% se imprime SOLO con la muletilla "según nuestras conversaciones con pagadores" (es dato de campo, no público). COI/FESA se menciona aquí como parte del FLUJO del pagador (instrucción 16-jul; coherente con el 4o reto del anexo del canal).
  - Zona 3 (proxy): en mano (deck canal Hospitales L4, datos nativos); el chip "[series mismas tiendas vs totales: por confirmar, equipo canal]" se imprime bajo las gráficas hasta que el canal confirme.
  - Zona 4: placeholder [CC] — el reporte IQVIA de abril no cubre hospital; el corte es otro y hay que conseguirlo.
  - Zona 5 (franja de dueños del pagador): en mano (research jul-26); recibida desde L22 por instrucción 16-jul, una sola línea.

- **Notas para el dibujante:**
  - Sin gold en esta lámina: los cuatro KPI en navy #0F2845 pesan solos; la lámina es entorno, no celebración ni alarma decorada.
  - Sin semáforos: ninguna cifra de esta lámina es un delta nuestro contra meta; son datos de entorno (colorear el +14.7% de siniestralidad de rojo sería usar semáforo para "tema serio", prohibido).
  - Inflación médica: imprimir **14.8%** (cifra del storyline v6 y del deck del canal); el research externo trae 14.9% (AMIS/EKA/WTW) — NO cambiar sin decisión de Rafael; el choque queda flageado.
  - Los ejes truncados de las dos mini-gráficas DEBEN llevar la marca de corte; sin ella parecería manipulación.
  - No mezclar universos: las tarjetas (fuentes públicas), el proxy (sell-in piezas PiSA) y la futura vista IQVIA son tres universos distintos en tres zonas separadas; jamás en una misma gráfica.
  - El placeholder se dibuja como recuadro vacío declarado, con estética limpia: es honestidad de proceso, no un error de diseño. Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27].
  - Cero em-dash en texto imprimible: los bullets de Zona 2 ya van con coma/paréntesis; no reintroducir rayas largas.
  - El −5% del mercado hospitalario NO se imprime en esta lámina (vive en la tablita y el puente como [validar IQVIA]); aquí solo la nota del placeholder lo menciona como pendiente de validación.
  - Título del v6 nombra "el pagador y el paciente"; este storyboard prioriza "el pagador" por instrucción del orquestador — el tráfico perdido (zona 2-3) cubre la parte del paciente.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; números alineados con dígitos de ancho uniforme; acentos en español.

LAYOUT en bandas:
- Banda de título + subtítulo arriba (~15% de la altura).
- Cuerpo (~71%) en DOS filas: fila superior (~35% del cuerpo) = fila de 4 tarjetas KPI del ancho completo + una línea de lectura; fila inferior (~65% del cuerpo) en TRES columnas (32% / 36% / 32%): (a) bullets, (b) dos mini-gráficas de línea apiladas, (c) un recuadro placeholder.
- Franja de UNA línea de ancho completo encima del pie (~6%).
- Pie (~8%).

TÍTULO, grande, navy oscuro #0F2845, sin punto final (dos líneas):
"El pagador cambia el juego: aseguradoras al límite"
"y hospital con 59% de ocupación"
SUBTÍTULO, itálica gris-azulado #44546A, mediano:
"El efecto duro llega en Q4-2026, al vencer las últimas pólizas contratadas antes del cambio de IVA"

FILA SUPERIOR — 4 tarjetas KPI iguales, separadas solo por un borde fino gris #E5E9EE (sin fondo de color). En cada tarjeta: etiqueta arriba en MAYÚSCULAS gris #5A6679 pequeña; valor grande en negrita navy #0F2845; contexto abajo gris #5A6679 pequeño. Contenido exacto:
1. Etiqueta "SINIESTRALIDAD GMM" · valor "~$131,000M" · contexto "cierre 2025, +14.7% vs 2024"
2. Etiqueta "PRIMAS GMM 2026" · valor "+6-10%" · contexto "general; hasta +40% en adultos mayores"
3. Etiqueta "INFLACIÓN MÉDICA" · valor "14.8%" · contexto "cuatro veces la inflación general"
4. Etiqueta "IVA NO ACREDITABLE" · valor "16%" · contexto "pagos directos, Ley 2026: encarece pólizas"
Los cuatro valores en navy #0F2845 (NINGUNO en rojo ni verde). Línea de lectura bajo las tarjetas, gris #3D4A5F, una línea: "Las aseguradoras cubren 80-85% del costo e intervienen el flujo: compra directa a quirófano y redirección del gasto."

FILA INFERIOR, COLUMNA A (32%) — título funcional navy #0F2845 negrita: "El hospital pierde tráfico". Debajo 3 bullets, gris #3D4A5F (sin rayas largas):
1. "Ocupación hospitalaria privada 59%, 21 pts bajo el estándar de 80%; quirófanos ~50%"
2. "El pagador redirige el flujo oncológico: el hospital marca 300-400% la quimio (según nuestras conversaciones con pagadores) y el flujo migra a centros de infusión (Alivia ~15 clínicas, COI/FESA 12 sedes)"
3. "Las mezclas se commoditizan"

FILA INFERIOR, COLUMNA B (36%) — título funcional navy #0F2845 negrita: "Tráfico hospitalario, proxy propio: venta en piezas vs promedio 2025". Debajo DOS mini-gráficas de línea apiladas (una encima de la otra), cada una con eje X = Ene Feb Mar Abr May Jun (2026), sin gridlines (o gris muy tenue #E5E9EE), ejes gris #5A6679. En cada gráfica hay UNA línea azul sólida #0F4C81 (serie 2026) y UNA línea base punteada gris #8A95A8 constante y horizontal (promedio 2025), rotulada directo sobre la línea, sin leyenda flotante. IMPORTANTE: los ejes Y están truncados (no arrancan en cero); dibuja una marca de corte de eje (doble raya) en la base del eje Y de cada mini-gráfica.
  - Mini-gráfica 1, título "Equipo para bomba (miles de piezas)": la línea 2026 arranca a media altura (Ene), baja un poco (Feb), sube a un pico en Mar, cae al VALLE más bajo en Abr y aún más bajo en May, y remonta a su punto MÁS ALTO en Jun, quedando ligeramente por encima de la línea base punteada. La base punteada horizontal se rotula "104.5 · promedio 2025". Data labels solo en el punto de Jun ("105.1") y en la base ("104.5"), gris #1A2332 pequeño. Anotación debajo, gris #5A6679: "junio recupera: 105.1 vs base 104.5; abr-may fueron el valle".
  - Mini-gráfica 2, título "Soluciones (millones de piezas)": misma forma general — Ene a media altura, leve baja en Feb, pico en Mar, VALLE en Abr y May (los dos puntos más bajos), y repunte en Jun que iguala el pico de Mar y queda por encima de la base. La base punteada se rotula "2.14 · promedio 2025". Data labels solo en Jun ("2.32") y en la base ("2.14").
  Bajo las dos mini-gráficas, un chip rectangular pequeño con fondo gris muy claro #F0F3F7 y borde fino gris #C5CDD9, texto gris #8A95A8 dibujado literal: "[series mismas tiendas vs totales: por confirmar, equipo canal]".

FILA INFERIOR, COLUMNA C (32%) — RECUADRO PLACEHOLDER: borde punteado fino gris #C5CDD9, fondo blanco, texto centrado gris #8A95A8. Texto: "[dato: CC · vista IQVIA del mercado hospitalario: tamaño y crecimiento]" (dibujar los corchetes literales; no rellenar). Microcopy debajo, gris #8A95A8 más pequeño: "El reporte IQVIA de abril NO cubre el canal hospitalario; corte específico en gestión. Esta vista valida además el −5% de la tablita." NO dibujar ninguna gráfica ni cifra dentro del recuadro.

FRANJA DE UNA LÍNEA (ancho completo, encima del pie): fondo gris muy claro #FAFBFC con una línea superior fina gris #C5CDD9 (arriba, nunca lateral), texto gris #3D4A5F en UNA sola línea: "El pagador también cambia de dueños: fondos y grupos entran al hospital y la clínica privada (PC Capital, General Atlantic, Hospiten)." Nada más en la franja.

PIE (gris #8A95A8, itálica, pequeño): "Fuente: siniestralidad GMM: CNSF/AMIS, cierre 2025; primas 2026: AMIS/EKA/WTW vía El Universal; ocupación: IntelLat vía Milenio, nov-25; inflación médica e IVA: El Economista, 10-may-26; centros de infusión, markup quimio y propiedad hospitalaria (PC Capital/General Atlantic/Hospiten): lectura propia del canal y research jul-26. Proxy de tráfico: sell-in piezas PiSA Eq/Bomba y Soluciones, ene-jun-26 vs promedio 2025. Vista de mercado hospitalario IQVIA: por integrar [CC]." A la derecha: "PiSA Confidencial | 21"

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; usar color gold (esta lámina NO lleva gold); semáforos (verde/ámbar/rojo) en cualquier cifra — todo el entorno va en navy y grises, no colorear el +14.7% ni ninguna cifra de rojo; rótulos de caja tipo "INSIGHT"; border-left. Las dos mini-gráficas DEBEN mostrar la marca de corte de eje. No mezclar los tres universos (tarjetas públicas, proxy de piezas, placeholder IQVIA) en una misma gráfica.
```


---

# Lamina 22 · Tres frentes atacan la infusión, las soluciones y los inyectables; la defensa ya opera en dos

- **Momento:** M5 · Hospitales: entorno, 1S, 2S (18.5% de la venta)

- **Encabezado:** Tres frentes atacan la infusión, las soluciones y los inyectables; la defensa ya opera en dos
  (1 línea de 96 caracteres, cabe en el límite de 110; si el master exige 2 líneas: "Tres frentes atacan la infusión, las soluciones y los inyectables;" / "la defensa ya opera en dos". Calibri Light 32 pt, #0F2845, sin punto final.)

- **So-what subtitle:** Mindray va por la carta de entrada, Baxter/Vantive por el negocio base, Kener por los inyectables con precio de lista muy por debajo del mercado (Calibri Light 14 pt itálica, #44546A)

- **Layout:** banda de título + subtitle 14% + franja de contexto 8% (la línea que está en juego) + cuerpo 3 columnas iguales ~33% cada una con gutter 0.15 in, alto ~50% (paneles de frente, máximo 3 bullets cada uno) + banda de respuesta ~16% en 3 celdas alineadas a las columnas + banda única al pie (una-dos líneas) + chip de decisión + línea de leyenda + pie 8%. Formato 16:9.

- **Zona por zona:**

  **Zona 0 (franja de contexto, ancho completo) · Lo que está en juego:**
  - Una línea de texto con la cifra pivote: "La terapia de infusión vale **$1,473M** de línea y es nuestra carta de entrada al hospital; soluciones + equipo de bomba = $930M, 63% de la línea."
  - "**$1,473M**" en Calibri bold con color gold #C5A55A — el ÚNICO elemento gold de la lámina. Resto Calibri Light 13 pt #1A2332.

  **Zona 1 (columna izquierda) · Panel Frente 1: Mindray, en terapia de infusión (3 bullets máximo):**
  - Header del panel: "Frente 1 · Mindray · terapia de infusión" (Calibri bold 12 pt blanco sobre banda #0F2845). Cuerpo del panel fondo blanco con border 0.5 pt #C5CDD9, radius 4-8 px.
  - Mini-KPI comparativo (tabular figures): "**$110-121** por equipo Mindray vs **$227** PiSA/ZMIN" (valores Calibri bold 20 pt #0F2845; nada de rojo).
  - Bullets (texto final, Calibri Light 11 pt #3D4A5F):
    1. Consumible propio (InfusoSafe) para capturar el flujo recurrente
    2. Ya presente en: Muguerza, Ángeles, AZURA [nombre por verificar: Martín], Hospitaria, Ginequito
    3. Amenaza estructural, no oportunista: su negocio internacional necesita mercados como México

  **Zona 2 (columna central) · Panel Frente 2: Baxter/Vantive, en soluciones (3 bullets máximo):**
  - Header del panel: "Frente 2 · Baxter/Vantive · soluciones" (mismo formato).
  - Mini-KPI comparativo: "**$17** por pieza ya ejecutado: −19% a −32% contra nuestros **$21-25**"
  - Bullets (texto final):
    1. Amenaza directa al negocio base: si nos sustituye en soluciones, el daño es mayor que el de cualquier otro competidor
    2. Matiz del research: las plantas de sueros de Cuernavaca y Atlacomulco son de Vantive (Carlyle) desde ene-25; Baxter México queda a la mitad de tamaño y declara pivote al hospital privado

  **Zona 3 (columna derecha) · Panel Frente 3: Kener, en inyectables, dimensionado (3 bullets máximo):**
  - Header del panel: "Frente 3 · Kener · inyectables" (mismo formato).
  - Mini-KPI: "catálogo cruzado **~$850M** (~$300M en corporativos)"
  - Bullets (texto final):
    1. Meropenem a $75 de lista contra $600-800 del mercado, con Grupo Ángeles como vehículo; 35,000 médicos credencializados
    2. En Ángeles ya nos desplazó ~$43M en 2025
    3. En proporción: vende ~$1,000M con meta ~$5,000M al 2030 (estimación propia de la industria)

  **Zona 4 (banda de respuesta, 3 celdas alineadas a las columnas) · La respuesta, frente por frente:**
  - Banda con fondo #FAFBFC y top border 2 pt #0F4C81 (sin border-left; sin rótulo tipo "RESPUESTA" como etiqueta de caja — el contenido abre con verbo). Texto Calibri Light 11 pt #1A2332.
  - Celda 1 (bajo Mindray): "Defendemos la base instalada: comodatos de infusión y soluciones, servicio y costo total de propiedad vs Mindray"
  - Celda 2 (bajo Baxter/Vantive): UN solo marcador — chip rectangular fondo #F0F3F7, borde 0.5 pt #C5CDD9, texto Calibri Light 10 pt #3D4A5F: "Respuesta en construcción [por cerrar: Martín]" — el chip se dibuja tal cual, visible. (El doble marcador anterior, texto "Identificado; la respuesta está en construcción" MÁS chip aparte, queda corregido a este único chip.)
  - Celda 3 (bajo Kener): "Plan Kener: defensa selectiva con gobierno central de precios de pelea (láser, no barra libre); ~40 convenios multi-hospital por ~$25M/mes con business reviews"

  **Zona 5 (banda única al pie, ancho completo, una-dos líneas):**
  - Calibri Light 10 pt #5A6679, sin caja: "Fidelidad estructural en paralelo: tecnología de infusión, consigna, quirófano inteligente. El cliente también cambia: fondos comprando hospitales (Polar con PC Capital, MAC con General Atlantic, Amerimed a Hospiten) y compradores-auditores que exigen rebates (Star Médica)."
  - (Antes eran dos franjas separadas, línea de cierre + franja de cliente; quedan fusionadas en esta banda única.)

  **Zona 6 (chip de decisión + línea de leyenda, sobre el pie):**
  - Chip de decisión, Calibri Light 9 pt #8A95A8: "[Rafael: el canal agrega 4o reto FESA/COI en su anexo; decidir si el deck madre adopta 4 frentes o FESA/COI queda como tema del pagador en L21]".
  - Línea de leyenda, Calibri Light 8 pt #8A95A8: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

- **Mensaje que manda la lamina:** la amenaza competitiva de Hospitales no es difusa: son tres frentes con números (Mindray a $110-121 contra nuestros $227 en la carta de entrada; Baxter/Vantive a $17, −19% a −32% contra nuestros $21-25, en el negocio base; Kener con ~$850M de nuestro catálogo cruzado y meropenem a $75 contra $600-800) y dos de los tres ya tienen defensa operando; el tercero está identificado y se cierra antes del 27. El veredicto sobre Kener se dice a voz, no se imprime (ver Guía de speaker).

- **Fuente (pie de lamina):** Fuente: sell-in canal Hospitales 1S26 y precios ejecutados por cuenta (canal HP, jul-26); Vantive/Carlyle y GEA-Kener: research externo con fuente pública, jul-26. Ventas y meta 2030 de Kener: estimación propia de la industria (sin cifra pública).

- **Estado del dato:**
  - Zonas 0-3: en mano (storyline v6 + deck canal Hospitales L5-L9 + research 10-jul).
  - Mini-KPI Baxter: el "(−40%)" anterior queda SUSTITUIDO por el rango real −19% a −32% (aritmética verificada: $17 vs $21 = −19%, $17 vs $25 = −32%); la alternativa chip "[comparador del descuento por declarar: Martín]" se descartó porque el rango real existe.
  - Zona 1, bullet 2: nombre "AZURA" por verificar con [Martín] (así viene rotulado en el deck del canal; no existe públicamente con ese nombre).
  - Zona 4, celda 2: por completar [Martín] — el deck del canal declara la respuesta al frente Baxter "por definir"; cerrar antes del 27 (pendiente #13 del v6, con el dimensionamiento de Mindray y Baxter [Martín/CC]).
  - Chip de decisión FESA/COI: NUEVO 16-jul, decisión de Rafael pendiente (4 frentes en el deck madre o tema del pagador en L21).
  - A ANEXO: precios Baxter por cuenta, detalle GEA de Kener y el bullet "200 clientes nos compran arriba de $200" (ver Contenido diferido a anexo).

- **Notas para el dibujante:**
  - El ÚNICO gold es "$1,473M" en la franja de contexto. Los mini-KPI de los paneles van en navy; NO pintar los precios de la competencia en rojo (sería semáforo decorativo: no son deltas nuestros).
  - Máximo 3 bullets por panel; los tres paneles con el MISMO ancho y la misma altura: ningún frente se dibuja "más grande" que otro; la jerarquía la da el orden (Mindray primero, por instrucción del storyline).
  - PROHIBIDO imprimir "compra mercado a pérdida" o cualquier veredicto equivalente: los números (meropenem $75 vs $600-800) lo dicen solos; el veredicto va en voz (Guía de speaker).
  - OJO numeración: el deck del canal numera Kener=frente 1, Baxter=frente 2, Mindray=frente 3; el storyline v6 manda Mindray=1, Baxter/Vantive=2, Kener=3. RIGE EL STORYLINE. No copiar los rótulos del deck del canal.
  - Escribir siempre "Baxter/Vantive", nunca "Baxter" solo (corrección obligada del research). Casing único "PiSA" (también en "PiSA/ZMIN").
  - El chip "Respuesta en construcción [por cerrar: Martín]" es un placeholder honesto, no un badge de alerta: gris neutro, sin ámbar ni rojo, sin icono. Es el ÚNICO marcador de esa celda (doble marcador corregido).
  - Problema-solución alineado por columna: la celda de respuesta de cada frente queda EXACTAMENTE debajo de su panel; el consejero debe poder leer en vertical amenaza y respuesta.
  - "Láser, no barra libre" se imprime sin comillas internas dobles si el master ya usa comillas; mantener el sentido: defensa selectiva, no guerra de descuentos.
  - Cero em-dash y cero carácter de flecha en texto imprimible (headers de panel con "·", no con raya).
  - Todos los corchetes son PLACEHOLDER INTERNO (kill antes del 27), declarado una sola vez en la línea de leyenda.
  - No usar mapa de México ni logos de competidores (el deck del canal los trae; el deck de Consejo no los hereda).

- **Guía de speaker (NO se dibuja):**
  - Veredicto de Kener, a voz: compra mercado a pérdida; los números impresos (meropenem $75 de lista contra $600-800) lo dicen solos, el adjetivo lo pone el speaker.
  - Kener no es el foco de la sesión de hospitales: se dice si el Consejo se clava; ya no se imprime como bullet.
  - Detalle GEA y precios por cuenta viven en anexo por si piden profundidad.

### Contenido diferido a anexo
- **Precios Baxter/Vantive ejecutados por cuenta:** "ABC $25 · Star Médica $25 · Christus $23 · G. Ángeles $21 · Español $24" (universo: precios ejecutados por cuenta, canal HP jul-26).
- **Detalle GEA-Kener (research público):** "GEA lo compró en ~200 mdd e invierte ~5,200 mdp; mezclas oncológicas en 1T-2027."
- **Bullet Mindray retirado por el tope de 3:** "200 clientes nos compran arriba de $200" (deck canal Hospitales; revisar redacción de unidades antes de reusarlo: el umbral "$200" viene sin unidad clara en el deck fuente).

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin mapas, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; números con dígitos de ancho uniforme; acentos en español.

LAYOUT en bandas horizontales:
- Banda de título + subtítulo arriba (~14% de la altura).
- Franja de contexto de ancho completo (~8%): una sola línea con la cifra pivote.
- Cuerpo (~50%): TRES columnas de igual ancho (~33% cada una), con separación estrecha; cada columna es un panel de "frente" con MÁXIMO 3 bullets. Los tres paneles tienen EXACTAMENTE el mismo ancho y la misma altura (ninguno más grande).
- Banda de respuesta (~16%): 3 celdas alineadas exactamente bajo las 3 columnas.
- Banda única al pie (una-dos líneas) + un chip de decisión chico + una línea de leyenda.
- Pie (~8%).

TÍTULO, grande, navy oscuro #0F2845, sin punto final (dos líneas):
"Tres frentes atacan la infusión, las soluciones y los inyectables;"
"la defensa ya opera en dos"
SUBTÍTULO, itálica gris-azulado #44546A, mediano:
"Mindray va por la carta de entrada, Baxter/Vantive por el negocio base, Kener por los inyectables con precio de lista muy por debajo del mercado"

FRANJA DE CONTEXTO (ancho completo), texto #1A2332: "La terapia de infusión vale $1,473M de línea y es nuestra carta de entrada al hospital; soluciones + equipo de bomba = $930M, 63% de la línea." La cifra "$1,473M" va en NEGRITA y color GOLD #C5A55A — este es el ÚNICO elemento gold de toda la lámina. Ningún otro texto en gold.

CUERPO — TRES PANELES iguales, cada uno con una banda de encabezado navy y cuerpo blanco con borde fino gris #C5CDD9, esquinas redondeadas suaves.

PANEL 1 (izquierda), encabezado con banda navy #0F2845, texto blanco negrita: "Frente 1 · Mindray · terapia de infusión". Dentro: un mini-KPI comparativo en negrita navy #0F2845: "$110-121 por equipo Mindray vs $227 PiSA/ZMIN" (nada en rojo). Tres bullets gris #3D4A5F:
1. "Consumible propio (InfusoSafe) para capturar el flujo recurrente"
2. "Ya presente en: Muguerza, Ángeles, AZURA [nombre por verificar: Martín], Hospitaria, Ginequito"
3. "Amenaza estructural, no oportunista: su negocio internacional necesita mercados como México"
El corchete "[nombre por verificar: Martín]" se dibuja literal, en gris neutro.

PANEL 2 (centro), encabezado banda navy #0F2845, texto blanco negrita: "Frente 2 · Baxter/Vantive · soluciones". Mini-KPI negrita navy: "$17 por pieza ya ejecutado: −19% a −32% contra nuestros $21-25". Dos bullets gris #3D4A5F:
1. "Amenaza directa al negocio base: si nos sustituye en soluciones, el daño es mayor que el de cualquier otro competidor"
2. "Matiz del research: las plantas de sueros de Cuernavaca y Atlacomulco son de Vantive (Carlyle) desde ene-25; Baxter México queda a la mitad de tamaño y declara pivote al hospital privado"

PANEL 3 (derecha), encabezado banda navy #0F2845, texto blanco negrita: "Frente 3 · Kener · inyectables". Mini-KPI negrita navy: "catálogo cruzado ~$850M (~$300M en corporativos)". Tres bullets gris #3D4A5F:
1. "Meropenem a $75 de lista contra $600-800 del mercado, con Grupo Ángeles como vehículo; 35,000 médicos credencializados"
2. "En Ángeles ya nos desplazó ~$43M en 2025"
3. "En proporción: vende ~$1,000M con meta ~$5,000M al 2030 (estimación propia de la industria)"

BANDA DE RESPUESTA — fondo gris muy claro #FAFBFC con una línea superior de 2 pt azul #0F4C81 (NUNCA barra vertical a la izquierda; sin rótulo de caja). 3 celdas, cada una alineada exactamente bajo su panel, texto #1A2332:
Celda 1 (bajo Mindray): "Defendemos la base instalada: comodatos de infusión y soluciones, servicio y costo total de propiedad vs Mindray"
Celda 2 (bajo Baxter/Vantive): SOLO un chip rectangular pequeño, fondo gris claro #F0F3F7, borde fino gris #C5CDD9, texto gris #3D4A5F: "Respuesta en construcción [por cerrar: Martín]" (dibujar el chip literal, gris neutro, sin ámbar ni rojo, sin icono; es el único contenido de esa celda).
Celda 3 (bajo Kener): "Plan Kener: defensa selectiva con gobierno central de precios de pelea (láser, no barra libre); ~40 convenios multi-hospital por ~$25M/mes con business reviews"

BANDA ÚNICA AL PIE (ancho completo, una-dos líneas), gris #5A6679 pequeña, sin caja: "Fidelidad estructural en paralelo: tecnología de infusión, consigna, quirófano inteligente. El cliente también cambia: fondos comprando hospitales (Polar con PC Capital, MAC con General Atlantic, Amerimed a Hospiten) y compradores-auditores que exigen rebates (Star Médica)."

CHIP DE DECISIÓN (debajo de la banda única), gris #8A95A8 chico, entre corchetes literales: "[Rafael: el canal agrega 4o reto FESA/COI en su anexo; decidir si el deck madre adopta 4 frentes o FESA/COI queda como tema del pagador en L21]".
LÍNEA DE LEYENDA, gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE (gris #8A95A8, itálica, pequeño): "Fuente: sell-in canal Hospitales 1S26 y precios ejecutados por cuenta (canal HP, jul-26); Vantive/Carlyle y GEA-Kener: research externo con fuente pública, jul-26. Ventas y meta 2030 de Kener: estimación propia de la industria (sin cifra pública)." A la derecha: "PiSA Confidencial | 22"

PROHIBIDO: el carácter de flecha o em-dash en cualquier texto; emojis; la frase "compra mercado a pérdida" o cualquier veredicto impreso sobre Kener; usar gold en cualquier elemento que no sea la cifra "$1,473M"; pintar los precios de la competencia en rojo (no son deltas nuestros); rótulos de caja tipo "RESPUESTA" o "INSIGHT"; border-left; mapas o logos; más de 3 bullets por panel. Los tres paneles del mismo tamaño exacto; las celdas de respuesta perfectamente alineadas bajo su panel para leer amenaza y respuesta en vertical.
```


---

# Lámina 23 · Hospitales crece +$153.8M, pero solo +$14.3M es portafolio PiSA: +$112.1M es distribución de terceros
- **Momento:** M5 · Hospitales: entorno, 1S, 2S (18.5% de la venta)
- **Encabezado:** Hospitales crece +$153.8M, pero solo +$14.3M es portafolio PiSA: +$112.1M es distribución de terceros
- **So-what subtitle:** Sell-in Hospitales de $2,906.6M a $3,054.5M (+$147.9M, 95.2% de meta); Δ reclasificada +$153.8M concilia a +$147.9M; mercado [-5% por validar IQVIA]
- **Layout:** banda de título 15% + cuerpo 66% en tres columnas 15/50/35 (col 1 mercado vs PiSA · col 2 puente de ventas REAL de 8 componentes + conciliación · col 3 palancas comerciales) + caveat 9% + footer 10%. Geometría 13.333 × 7.5 in, márgenes 0.5 in, área útil 12.333 in. Título y 0.5–1.55 in; cuerpo y 1.65–6.3 in; caveat y 6.35–6.75 in; footer y 6.85–7.1 in. Anchos: col 1 ≈ 1.8 in, col 2 ≈ 6.0 in, col 3 ≈ 4.2 in, gutter 0.15 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 1.0 in).**
Título asertivo Calibri Light 28-30 pt `#0F2845` (2 líneas), sin punto final; so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Cuerpo, tres columnas (convención de puente 15/50/35).**

*Columna 1 (15%, ≈1.8 in) — Mercado vs PiSA. Gráfica de dos barras.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Mercado vs PiSA".
- Dos barras verticales, eje Y en % de crecimiento (cero al centro), sin gridlines, sin leyenda:
  - Barra 1: **Mercado hospitalario [-5%]** — relleno `#8A95A8` (gris), hacia abajo (negativa), data label literal "[-5% por validar IQVIA]" en `#8A95A8`.
  - Barra 2: **PiSA Hospitales +5.1%** — relleno `#0F4C81` (navy), hacia arriba (positiva), data label "+5.1%".
- Callout entre ambas barras, Calibri Light 11 pt `#3D4A5F`: "crecemos contra corriente".
- Nota bajo la gráfica, Calibri Light 9 pt `#5A6679`: "Mercado por validar con IQVIA (el reporte de abril no cubre el canal hospitalario); PiSA = sell-in Hospitales, 1S."

*Columna 2 (50%, ≈6.0 in) — Puente de ventas 1S25 a 1S26 (REAL). Waterfall de 8 componentes + conciliación.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Puente de ventas, ocho componentes".
- Eyebrow de universo, Calibri Light 9 pt `#5A6679`: "Sell-in Hospitales · matriz Downtrading FINAL 16-jul · cobertura core PiSA 65.0% del bruto elegible".
- Waterfall, $M, eje Y desde 0, connectors punteados 0.5 pt `#C5CDD9`, data label con signo sobre cada barra:
  - Barra inicial (navy `#0F2845`): **$2,906.6M** — data label "1S25 · $2,906.6M".
  - Ocho barras de componente:
    1. "Precio" — **−5.7** — rojo `#C00000` (un filo con etiqueta).
    2. "Volumen" — **+26.3** — navy `#0F4C81`.
    3. "Mix (core PiSA)" — **−14.5** — rojo `#C00000`.
    4. "Gestión de portafolio" — **+8.3** — navy `#0F4C81`.
    5. "Lanzamientos" — **+23.1** — navy `#0F4C81`.
    6. "Terceros" — **+112.1** — navy `#0F4C81` (la barra dominante del puente), con anotación "lo encabeza KEYTRUDA +$28.6M" en 9 pt `#5A6679`.
    7. "Servicios / serie 9" — **+7.8** — navy `#0F4C81`.
    8. "Sin unidad (por valor)" — **−3.6** — rojo `#C00000` (un filo).
  - Llave/corchete sobre las ocho barras, Calibri Light 10 pt `#3D4A5F`: "Δ reclasificada +$153.8M".
  - Dos barras de conciliación en GRIS `#C5CDD9` (contorno `#8A95A8`; contabilidad, no desempeño): "Reclas. nov-dic-25" **−4.4** (tick intermedio "Δ con MATNR +$149.4M" en 9 pt `#8A95A8`) y "Sin MATNR" **−1.5**.
  - Barra final (navy `#0F2845`): **$3,054.5M** — data label "1S26 · $3,054.5M (95.2% de meta)". El cierre CUADRA con el sell-in impreso en L9 (+$147.9M).
- Anotaciones bajo el chart, Calibri Light 9.5 pt `#3D4A5F`, dos renglones de una línea:
  - "Portafolio core PiSA (precio, volumen, mix y gestión) neto +$14.3M: el crecimiento del segmento lo carga la distribución de terceros (+$112.1M)."
  - "La distribución de terceros no rinde el margen del portafolio propio: leer contra el EBITDA del segmento de 39.2% (L6)."

*Columna 3 (35%, ≈4.2 in) — Palancas comerciales 1S25 vs 1S26. Cuatro renglones.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Palancas comerciales, 1S25 vs 1S26".
- Renglones 1-2 con eyebrow "seguimiento del canal / DP", renglones 3-4 con eyebrow "Gross2Net Finanzas":
  1. Venta perdida: dos barras — "1S-2025 = $188M" (`#8A95A8`) y "1S-2026 = $118M" (`#0F4C81`, MÁS CORTA); etiqueta "mejora −37%" Calibri Light 9.5 pt `#5A6679`.
  2. PIN no solicitado: dos barras — "1S-2025 = $174M" (`#8A95A8`) y "1S-2026 = $71M" (`#0F4C81`, mucho MÁS CORTA); etiqueta **"−59%, la mejora estrella del deck"** en Calibri bold 12 pt `#C5A55A` (gold). ÚNICO elemento gold de la lámina. Sub-nota 9 pt `#5A6679`: "bolsa real ~$42M; $30M comprometidos al 2S".
  3. NC comerciales y sanciones: dos barras — "1S-2025 = −$24.3M" y "1S-2026 = −$24.5M"; etiqueta neutra `#5A6679` "estable".
  4. Devoluciones: dos barras — "1S-2025 = −$59.7M" y "1S-2026 = −$73.4M" (más larga); etiqueta en rojo `#C00000` "empeora +22.9%" (el flag del segmento).

**Zona C — Caveat de universo (12.333 × 0.4 in).**
Texto Calibri Light 9.5 pt `#8A95A8`, dos renglones: "Col 1 y col 2 en universo sell-in; el mercado de la col 1 está por validar con IQVIA (el reporte de abril no cubre el canal hospitalario). El mix y el precio del puente se citan como core PiSA (cobertura 65.0% del bruto elegible), no como el segmento entero; venta perdida y PIN del seguimiento del canal, NC y devoluciones del Gross2Net de Finanzas."

**Zona D — Footer (12.333 × 0.25 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 23" derecha.

## Mensaje que manda la lámina
Hospitales es el segmento de mayor crecimiento (+$153.8M en la Δ reclasificada, +$147.9M de sell-in), pero el puente enseña de qué está hecho: solo +$14.3M es portafolio core PiSA; +$112.1M es distribución de terceros, encabezada por KEYTRUDA (+$28.6M), que no rinde el margen del portafolio propio. En ejecución, el canal trae la mejora estrella del deck: el PIN no solicitado cae −59% (de $174M a $71M) y la venta perdida mejora −37%; el flag es devoluciones, que empeora +22.9%.

## Fuente (pie de lámina)
Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In cierre jun-26, Hospitales 1S26 vs 1S25 (cobertura core 65.0% del bruto elegible); mercado por validar (IQVIA no cubre canal hospitalario en el reporte de abril); venta perdida y PIN: tabla canónica 16-jul (seguimiento del canal); NC y devoluciones: Gross2Net Finanzas.

## Estado del dato
- Col 1: **en mano** en el lado PiSA (+5.1% sell-in); el mercado es **placeholder** "[-5% por validar IQVIA]".
- Col 2 (puente completo Precio −5.7 / Volumen +26.3 / Mix −14.5 / Gestión +8.3 / Lanzamientos +23.1 / Terceros +112.1 / Serie 9 +7.8 / Sin unidad −3.6 = +153.8; conciliación −4.4 reclasif = +149.4 con MATNR; −1.5 sin MATNR = +147.9 cubo): **en mano y verificado al peso** (matriz consolidada FINAL 16-jul; 2,906.6 + 153.8 − 4.4 − 1.5 = 3,054.5 exacto). Core PiSA neto +14.3; terceros encabezado por KEYTRUDA +28.6. SUPERSEDE las 5 siluetas "[equipo PVM]", la referencia 2-vías (+14.8 / +133.2) y la cascada propia del canal de la versión anterior (ver Contenido diferido).
- Col 3: venta perdida $188M a $118M (−37%) y PIN $174M a $71M (−59%; bolsa ~$42M, $30M al 2S): **en mano** (tabla canónica Rafael 16-jul; SUPERSEDE el par 188.2 a 114.5 con "mejora $73.7M" de la versión anterior — la cifra canónica de 1S26 es $118M y la mejora se cita como −37%). NC −24.3 a −24.5 y Dev −59.7 a −73.4 (+22.9%): **en mano** (Gross2Net; SUPERSEDE el placeholder "[por llegar: VJ/RC]").
- Cambio de gold declarado: el gold pasa de "mejora $73.7M" (VP, superseded) a la mejora estrella del PIN "−59%".

## Notas para el dibujante
- El ÚNICO gold de la lámina es la etiqueta "−59%, la mejora estrella del deck" del PIN no solicitado (col 3). Nada más en gold; ni el +$112.1M de terceros ni el +$14.3M del core van en dorado (viven en el título).
- Proporciones relativas del waterfall: Terceros +112.1 domina; Volumen +26.3 y Lanzamientos +23.1 medianas-chicas; Mix −14.5, Gestión +8.3 y Serie 9 +7.8 chicas; Precio −5.7 y Sin unidad −3.6 filos con etiqueta; conciliaciones −4.4 y −1.5 mínimas y en gris.
- SIN verde en ninguna barra ni etiqueta: positivos navy `#0F4C81`, negativos rojo `#C00000`, anclas navy `#0F2845`, conciliaciones gris `#C5CDD9` (no rojas: son contabilidad).
- El mercado de la col 1 se dibuja como barra placeholder gris con la etiqueta literal "[-5% por validar IQVIA]": no fijar un −5% como si fuera dato duro. El lado PiSA +5.1% sí es sólido en navy.
- El rojo del "empeora +22.9%" de devoluciones es semáforo cuantitativo sobre un delta (el flag del segmento), no decoración.
- Todos los corchetes con responsable son PLACEHOLDER INTERNO — kill antes del 27: viven en el storyboard de revisión, no en la versión del Consejo.
- Signo menos tipográfico "−"; signo "+" explícito en positivos; no usar el carácter de flecha (el puente se lee "1S25 a 1S26", la venta perdida "de $188M a $118M").
- NO mezclar universos: col 2 es sell-in; en col 3 los renglones 1-2 son seguimiento del canal/DP y los 3-4 Gross2Net, cada par con su eyebrow. Caveat de Zona C obligatorio.
- Tabular figures en toda cifra. Sin líneas verticales. Sin border-left. Sin caja de insight ni rótulos de bloque.

### Contenido diferido a anexo
- A ANEXO: referencia 2-vías del segmento (volumen +$14.8M · precio y mezcla +$133.2M = +$147.9M, piezas +0.5%): descomposición gruesa superseded por la matriz de 8 componentes; se conserva solo como validación de anexo.
- A ANEXO: cascada propia del canal Hospitales (precio −8, volumen +93, altas y bajas +25, servicios +41): taxonomía distinta y bugs internos; se usó como insumo del puente, no se hereda al deck.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; TODAS las cifras en figuras tabulares; acentos en español.

ESTRUCTURA EN BANDAS: banda de título arriba (~15%); cuerpo al centro (~66%) dividido en TRES columnas de anchos 15% / 50% / 35% de izquierda a derecha; una banda de caveat de dos renglones (~9%); y un pie delgado abajo (~10%).

BANDA DE TÍTULO (ancho completo): título grande navy oscuro #0F2845, sans-serif ligera, sin punto final, hasta dos líneas: "Hospitales crece +$153.8M, pero solo +$14.3M es portafolio PiSA: +$112.1M es distribución de terceros". Debajo, en gris azulado #44546A pequeño e itálica: "Sell-in Hospitales de $2,906.6M a $3,054.5M (+$147.9M, 95.2% de meta); Δ reclasificada +$153.8M concilia a +$147.9M; mercado [-5% por validar IQVIA]". Línea horizontal fina gris #E5E9EE de margen a margen.

COLUMNA IZQUIERDA (15%) — arriba, texto plano navy #0F2845 negrita, pequeño: "Mercado vs PiSA". Debajo, una gráfica de DOS barras verticales, eje en % con cero al centro, sin gridlines, sin leyenda. Barra 1 rellena en gris #8A95A8, apuntando hacia ABAJO (negativa), con etiqueta literal "[-5% por validar IQVIA]" en gris #8A95A8 (es un placeholder, no un dato duro). Barra 2 rellena en navy #0F4C81, apuntando hacia ARRIBA (positiva), con etiqueta "+5.1%" (PiSA Hospitales). Entre ambas barras, un texto pequeño gris #3D4A5F: "crecemos contra corriente". Bajo la gráfica, texto pequeño gris #5A6679: "Mercado por validar con IQVIA (el reporte de abril no cubre el canal hospitalario); PiSA = sell-in Hospitales, 1S."

COLUMNA CENTRAL (50%) — arriba, texto plano navy #0F2845 negrita: "Puente de ventas, ocho componentes". Debajo, en gris #5A6679 muy pequeño: "Sell-in Hospitales · matriz Downtrading FINAL 16-jul · cobertura core PiSA 65.0% del bruto elegible". Debajo, una gráfica de cascada (waterfall) con conectores punteados finos gris #C5CDD9, eje Y en millones desde 0, etiqueta de valor con signo sobre cada barra. De izquierda a derecha:
1. Barra ancla "1S25 · $2,906.6M" — sólida navy oscuro #0F2845, alta.
2. "Precio" = "−5.7" — negativa, roja #C00000, un filo con etiqueta.
3. "Volumen" = "+26.3" — positiva, azul #0F4C81, chica-mediana.
4. "Mix (core PiSA)" = "−14.5" — negativa, roja #C00000, chica.
5. "Gestión de portafolio" = "+8.3" — positiva, azul #0F4C81, chica.
6. "Lanzamientos" = "+23.1" — positiva, azul #0F4C81, chica-mediana.
7. "Terceros" = "+112.1" — positiva, azul #0F4C81, la barra flotante DOMINANTE del puente; junto a ella, en gris #5A6679 pequeño: "lo encabeza KEYTRUDA +$28.6M".
8. "Servicios / serie 9" = "+7.8" — positiva, azul #0F4C81, chica.
9. "Sin unidad (por valor)" = "−3.6" — negativa, roja #C00000, un filo.
Sobre estas ocho barras, una llave horizontal rotulada en gris #3D4A5F: "Δ reclasificada +$153.8M".
10. "Reclas. nov-dic-25" = "−4.4" — barra GRIS claro #C5CDD9 con contorno gris #8A95A8 (conciliación, no roja), con un tick pequeño en gris #8A95A8: "Δ con MATNR +$149.4M".
11. "Sin MATNR" = "−1.5" — barra gris #C5CDD9 mínima.
12. Barra ancla "1S26 · $3,054.5M (95.2% de meta)" — sólida navy oscuro #0F2845, alta.
Bajo la gráfica, en gris #3D4A5F, dos renglones: "Portafolio core PiSA (precio, volumen, mix y gestión) neto +$14.3M: el crecimiento del segmento lo carga la distribución de terceros (+$112.1M)." y "La distribución de terceros no rinde el margen del portafolio propio: leer contra el EBITDA del segmento de 39.2% (L6)."

COLUMNA DERECHA (35%) — arriba, texto plano navy #0F2845 negrita: "Palancas comerciales, 1S25 vs 1S26". Debajo, cuatro renglones; los renglones 1-2 llevan arriba un eyebrow gris muy pequeño "seguimiento del canal / DP" y los renglones 3-4 un eyebrow "Gross2Net Finanzas":
1. "Venta perdida": dos barras horizontales pares, "1S-2025 = $188M" en gris #8A95A8 y "1S-2026 = $118M" en azul #0F4C81 claramente MÁS CORTA; etiqueta chica gris #5A6679 "mejora −37%".
2. "PIN no solicitado": dos barras pares, "1S-2025 = $174M" en gris #8A95A8 y "1S-2026 = $71M" en azul #0F4C81 mucho MÁS CORTA; etiqueta en DORADO #C5A55A negrita: "−59%, la mejora estrella del deck" (este es el ÚNICO elemento dorado de toda la lámina); debajo, texto chico gris #5A6679: "bolsa real ~$42M; $30M comprometidos al 2S".
3. "NC comerciales y sanciones": dos barras casi iguales, "1S-2025 = −$24.3M" y "1S-2026 = −$24.5M"; etiqueta chica gris #5A6679 "estable".
4. "Devoluciones": dos barras, "1S-2025 = −$59.7M" en gris y "1S-2026 = −$73.4M" en azul #0F4C81 visiblemente más larga; etiqueta en rojo #C00000: "empeora +22.9%".

BANDA DE CAVEAT (ancho completo, dos renglones, gris #8A95A8 pequeño): "Col 1 y col 2 en universo sell-in; el mercado de la col 1 está por validar con IQVIA (el reporte de abril no cubre el canal hospitalario). El mix y el precio del puente se citan como core PiSA (cobertura 65.0% del bruto elegible), no como el segmento entero; venta perdida y PIN del seguimiento del canal, NC y devoluciones del Gross2Net de Finanzas."

PIE (ancho completo): línea fina gris #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: matriz consolidada Downtrading FINAL 16-jul sobre Sell-In cierre jun-26, Hospitales 1S26 vs 1S25 (cobertura core 65.0% del bruto elegible); mercado por validar (IQVIA no cubre canal hospitalario en el reporte de abril); venta perdida y PIN: tabla canónica 16-jul; NC y devoluciones: Gross2Net Finanzas." A la derecha: "PiSA Confidencial | 23".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde en cualquier barra o etiqueta; más de un elemento en dorado (solo la etiqueta del PIN "−59%, la mejora estrella del deck"); fijar el −5% del mercado como dato duro; rellenar cualquier corchete. El signo menos es "−" tipográfico y el "+" explícito; español con acentos; título sin punto final.
```


---

# Lámina 24 · El mayor crecimiento (+5.1%) convive con 95.2% de meta: abril-mayo y Ángeles concentran el faltante
- **Momento:** M5 · Hospitales: entorno, 1S, 2S (18.5% de la venta)
- **Encabezado:** El mayor crecimiento (+5.1%) convive con 95.2% de meta: abril-mayo y Ángeles concentran el faltante
  ("concentran", NO "explican": instrucción 16-jul; el verbo mide dónde vive el faltante sin sobre-atribuir causalidad.)
- **So-what subtitle:** Radiografía del 1S de Hospitales: seis aciertos, cuatro faltantes; junio se lee con su asterisco
- **Layout:** banda de título 13% + cuerpo 82% (dos columnas iguales 50/50 con gutter 0.3 in) + footer 5%. Geometría: lámina 13.333 × 7.5 in; márgenes 0.5 in; área útil 12.333 × 6.5 in. Título en y 0.5–1.35 in; cuerpo en y 1.5–6.6 in; footer en y 6.7–7.0 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 0.85 in, arriba).**
Título asertivo Calibri Light 32 pt `#0F2845` (si no cabe en 1 línea, 28 pt en 2 líneas); debajo el so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Tabla doble "bien / faltó" (cuerpo completo, dos tablas independientes lado a lado, 6.0 in de ancho cada una, gutter 0.3 in).**
Cada columna es una tabla propia (los conteos difieren: 5 vs 4 renglones).

*Columna izquierda — header:* fondo `#0F2845`, texto blanco Calibri bold 13 pt, alineado izquierda: **"Qué hicimos bien en el 1S"**. Renglones alternos blanco / `#F0F3F7`, texto Calibri Light 11.5 pt `#3D4A5F`, viñeta guion corto gris, border inferior 1 px `#E5E9EE`, sin líneas verticales. Contenido final (texto listo para lámina):
1. +5.1%: el mayor crecimiento, en el entorno más agresivo (1S26 vs 1S25, sell-in)
2. Anestesia/SIA privado +18.1% (102.3% de meta); mezclas/SAFE privado +9.5% (103.7%)
3. Venta perdida mejoró -37% contra 1S25 (de $188M a $118M)
4. El PIN no solicitado bajó -59% (de $174M a $71M): pedimos mejor
5. Convenios multi-hospital: ~$25M/mes desde marzo
6. Cartera respondiendo: la liberación al 90% capturó 40% de lo proyectado en 2 semanas; Dalinde paga $4M/semana

*Columna derecha — header:* mismo formato: **"Qué nos faltó en el 1S"**. Contenido final:
1. Abril-mayo costó la mitad del crecimiento (de +9/10% a +5%): ocupación (exógena), crédito (autoinfligida, ya respondiendo) y presión de precios (estructural); 89% de meta en esos dos meses
2. Pérdida de Grupo Ángeles CDMX en mezclas: −$10M/mes; −22% en el semestre
3. El PIN usado como meta y no como señal de demanda: bolsa mal ajustada
4. Junio 99% de meta (+12% vs jun-25) lleva asterisco: 5 lunes y ~$10M one-off de mezclas (paros ABC/OCA)

**Zona C — Footer (12.333 × 0.3 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` a la izquierda; "PiSA Confidencial | 24" a la derecha.

## Mensaje que manda la lámina
Hospitales entregó el mayor crecimiento del portafolio en el entorno competitivo más agresivo, con la venta perdida y el PIN mejorando fuerte, pero quedó a 4.8 pts de su meta; el faltante tiene tres causas nombradas (abril-mayo, Ángeles, PIN mal usado) y junio se lee con su asterisco, dicho por nosotros.

## Fuente (pie de lámina)
Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Hospitales; venta perdida y PIN: tabla consolidada Comercial 16-jul-26; convenios y cartera: seguimiento del canal Hospitales, corte jun-26.

## Estado del dato
- Columna "bien": **en mano**. Bien-3 ACTUALIZADO a la tabla canónica Rafael 16-jul: venta perdida de $188M a $118M (-37%). La cifra previa "de $188.2M a $114.5M / mejoró $74M" (corte DP) queda SUPERSEDED; gana el canónico. Bien-4 NUEVO 16-jul: PIN no solicitado de $174M a $71M (-59%), tabla canónica PIN.
- Columna "faltó": **en mano** (cruzado con deck del canal: abr-may 89% de meta y gap −$122.5M; Ángeles −22% / gap −$32.7M; junio 99% +12%).

## Notas para el dibujante
- Deck de Consejo sobrio: SIN caja de insight, sin rotular bloques con "INSIGHT"/"SO WHAT" ni equivalentes. Los headers de tabla llevan exactamente "Qué hicimos bien en el 1S" / "Qué nos faltó en el 1S", nada más.
- Las dos columnas pesan visualmente IGUAL: mismo ancho, mismo formato, mismo gris de texto. Nada de verde en la columna "bien" ni rojo en la "faltó" — es radiografía, no boleta de calificaciones. Deltas en el mismo `#3D4A5F` del texto; sin semáforos en prosa.
- Negritas: máximo 3-4 palabras en toda la lámina (sugerido: "+5.1%" en bien-1 y "89% de meta" en faltó-1). No más.
- El bullet del asterisco de junio (faltó-4) va en la columna "faltó" a propósito: el asterisco lo ponemos nosotros; no moverlo a "bien" ni suavizarlo.
- Tensión declarada (no imprimible): bien-4 dice que el PIN bajó -59% (pedimos mejor) y faltó-3 critica el PIN usado como meta; conviven a propósito — la mejora es del monto, la crítica es del uso. Si Rafael prefiere fusionarlos, es su decisión.
- SIN gold en esta lámina (no hay cifra pivotal única; el equilibrio es el mensaje).
- Tabular figures en toda cifra. Sin líneas verticales en tablas. Sin border-left en ningún bloque.
- No agregar KPIs ni gráficas de contexto: la venta y el puente ya se mostraron en la L23; repetirlos rompe "una idea por lámina".
- Cifras del deck del canal (FC $3,050 acumulado) NO se imprimen: la referencia de venta del segmento es sell-in ($3,054.5M, vive en L23). Esta lámina no imprime nivel de venta.
- Trampa conocida: el deck del canal muestra SAFE/SIA combinado (+10%, 104% de alcance) mientras el v6 separa anestesia/SIA +18.1% y mezclas/SAFE +9.5%. Manda el storyline (bien-2 tal cual); no sustituir por las cifras del canal.

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha en tablas. Márgenes amplios y homogéneos.

ESTRUCTURA VERTICAL: banda de título arriba (~13% de la altura), cuerpo al centro con DOS columnas iguales lado a lado 50/50 (~82%), y un pie delgado abajo (~5%).

BANDA DE TÍTULO (arriba, ancho completo): título en dos líneas, sans-serif ligera, color navy oscuro #0F2845, tamaño grande: "El mayor crecimiento (+5.1%) convive con 95.2% de meta: abril-mayo y Ángeles concentran el faltante". Debajo, en gris azulado #44546A, tamaño pequeño en itálica: "Radiografía del 1S de Hospitales: seis aciertos, cuatro faltantes; junio se lee con su asterisco". Una línea horizontal fina gris claro #E5E9EE separa el título del cuerpo, de margen a margen.

CUERPO: dos tablas independientes del mismo ancho, una a la izquierda y otra a la derecha, con un espacio entre ellas. Ambas pesan visualmente IGUAL (mismo ancho, mismo formato, mismo gris de texto). No usar verde en la izquierda ni rojo en la derecha; todo el texto de los renglones en gris #3D4A5F. Sin líneas verticales. Sin bordes laterales de color.

COLUMNA IZQUIERDA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué hicimos bien en el 1S". Debajo, 6 renglones con fondo alternado blanco / gris muy claro #F0F3F7, cada renglón con una viñeta de guion corto gris y una línea inferior fina gris claro #E5E9EE. Texto de los renglones (verbatim):
1. "+5.1%: el mayor crecimiento, en el entorno más agresivo (1S26 vs 1S25, sell-in)"
2. "Anestesia/SIA privado +18.1% (102.3% de meta); mezclas/SAFE privado +9.5% (103.7%)"
3. "Venta perdida mejoró -37% contra 1S25 (de $188M a $118M)"
4. "El PIN no solicitado bajó -59% (de $174M a $71M): pedimos mejor"
5. "Convenios multi-hospital: ~$25M/mes desde marzo"
6. "Cartera respondiendo: la liberación al 90% capturó 40% de lo proyectado en 2 semanas; Dalinde paga $4M/semana"
Dentro de esta columna, solo "+5.1%" del renglón 1 va en negrita.

COLUMNA DERECHA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué nos faltó en el 1S". Debajo, 4 renglones con el mismo formato alternado blanco / gris muy claro #F0F3F7, misma viñeta de guion. Texto de los renglones (verbatim):
1. "Abril-mayo costó la mitad del crecimiento (de +9/10% a +5%): ocupación (exógena), crédito (autoinfligida, ya respondiendo) y presión de precios (estructural); 89% de meta en esos dos meses"
2. "Pérdida de Grupo Ángeles CDMX en mezclas: −$10M/mes; −22% en el semestre"
3. "El PIN usado como meta y no como señal de demanda: bolsa mal ajustada"
4. "Junio 99% de meta (+12% vs jun-25) lleva asterisco: 5 lunes y ~$10M one-off de mezclas (paros ABC/OCA)"
Dentro de esta columna, solo "89% de meta" del renglón 1 va en negrita.

PIE (abajo, ancho completo): una línea fina gris claro #E5E9EE arriba del pie. A la izquierda, texto pequeño en itálica gris #8A95A8: "Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Hospitales; venta perdida y PIN: tabla consolidada Comercial 16-jul-26; convenios y cartera: seguimiento del canal Hospitales, corte jun-26." A la derecha, mismo estilo: "PiSA Confidencial | 24".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde celebratorio en las cifras propias; cualquier semáforo de color en los renglones. El signo menos en los deltas ("−$10M", "−22%") va en el mismo gris del texto, no en rojo.
```


---

# Lámina 25 · El gap del 2S es $57M/mes; las siete palancas identificadas cubren $47M/mes y julio es la prueba
- **Momento:** M5 · Hospitales: entorno, 1S, 2S (18.5% de la venta)
- **Encabezado:** El gap del 2S es $57M/mes; las siete palancas identificadas cubren $47M/mes y julio es la prueba
- **So-what subtitle:** Medición formal desde julio; el piloto de junio capturó $11M, 23% del run-rate objetivo
- **Layout (RECORTE 16-jul):** banda de título 13% + cuerpo 78% en DOS columnas 58/42 (B: waterfall de palancas con base y meta como referencias · C: plan de acción con aire) + banda inferior de anotación + línea de leyenda + footer 5%. El panel izquierdo anterior (gráfica de dos columnas $429/$485) SALIÓ: el waterfall ya carga base y meta como referencias; su contenido está en "Contenido diferido a anexo". Geometría: 13.333 × 7.5 in, márgenes 0.5 in, área útil 12.333 × 6.5 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 0.85 in).**
Título Calibri Light 32 pt `#0F2845` (28 pt si requiere 2 líneas); so-what 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE`.

**Zona B — Waterfall de palancas contra la línea del gap (columna izquierda, ~7.1 in de ancho).**
- Micro-título de zona: "Siete palancas, $47M/mes" — Calibri bold 12 pt `#0F2845` (texto plano, no etiqueta de caja).
- Waterfall acumulativo de 0 a $47M/mes, $M/mes, eje Y desde 0. Orden de barras (mayor a menor, izquierda a derecha), todas positivas en navy `#0F4C81`, connectors punteados 0.5 pt `#C5CDD9`, data label sobre cada barra (valor) y nombre de palanca bajo el eje X en 9.5 pt:
  1. Recuperación de cuentas — **$14M**
  2. Plan Kener — **$9M**
  3. Liberación de cartera — **$7M**
  4. Nuevos productos — **$6M**
  5. PIN no solicitado — **$5M**
  6. Convenios — **$4M**
  7. Cambio de tecnología — **$2M**
  8. Barra total: **$47M/mes** — navy `#0F2845` con mayor peso, data label bold.
- **Línea horizontal punteada en $57M** cruzando todo el chart, color gold `#C5A55A` 1.5 pt, rotulada a la derecha "Gap $57M/mes: de $429M/mes de venta promedio ene-may a $485M/mes de meta jul-dic" (Calibri bold 11 pt `#C5A55A` la cifra "Gap $57M/mes"; el resto del rótulo Calibri Light 9.5 pt `#5A6679`). Línea + rótulo cuentan como el ÚNICO elemento gold de la lámina. Así el waterfall carga base y meta como referencias sin panel aparte.
- Anotación entre la barra total y la línea, Calibri Light 10 pt `#3D4A5F`: "~$10M/mes aún sin palanca asignada".
- Notas al pie del chart (Calibri Light 9.5 pt `#5A6679`, dos líneas):
  - "Piloto junio: $11M capturados (23% del run-rate objetivo); medición formal desde julio. Base ene-may: excluye junio (mes con asterisco)."
  - Chip literal: "[universo del $429M/mes por rotular: Martín/CC; no reconcilia contra sell-in L9]".

**Zona C — Plan de acción (columna derecha, ~4.9 in de ancho, con aire). Bullets.**
Micro-título de zona: "Cómo se ejecuta" — Calibri bold 12 pt `#0F2845`. Bullets Calibri Light 11 pt `#3D4A5F` (subió de 10.5 a 11 pt: esta columna ganó ancho y aire con el recorte), texto final:
- Defensa de la base instalada: comodatos de infusión y soluciones frente a Mindray y Baxter/Vantive (servicio, costo total, contratos). [plan frente Baxter por cerrar: Martín]
- Plan Kener: defensa selectiva con precio gobernado, no guerra de descuentos.
- Apriete de cumplimiento de convenios: +$3-4M/mes identificados; 32 hospitales en precio por volumen, $9.4M/mes de beneficio negociado.
- Híbrido con centros de infusión: PiSA mezcla con cumplimiento regulatorio; ellos ponen pagadores (primer gate 14-jul).
- Riesgo declarado: las últimas pólizas con IVA deducible vencen en Q4.

**Zona D — Banda inferior de anotación (12.333 × 0.25 in, sobre la leyenda).**
Una línea, Calibri Light 11 pt `#1A2332`: "Julio es el mes de la prueba: sin quinto lunes, el run-rate de palancas debe compensar el calendario." A su derecha, placeholder declarado: "[Aporte de Hospitales al hueco consolidado: RC]" en Calibri Light 10 pt `#8A95A8`.

**Zona D2 — Línea de leyenda de placeholders (sobre el footer).**
Calibri Light 8 pt `#8A95A8`: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

**Zona E — Footer.**
Línea 0.5 pt `#E5E9EE`; fuente 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 25" derecha.

## Mensaje que manda la lámina
La brecha del 2S de Hospitales está dimensionada ($57M/mes, de $429M/mes de venta base a $485M/mes de meta) y tiene siete palancas nombradas que cubren $47M/mes; el descubierto de ~$10M/mes se declara, el piloto de junio ya capturó $11M y julio, sin quinto lunes, es la primera lectura real del run-rate.

## Fuente (pie de lámina)
Fuente: Sell-In cierre jun-26 (venta promedio ene-may) y metas jul-dic 2026; palancas y piloto: plan del canal Hospitales, jul-26. Universo del $429M/mes por rotular (no reconcilia contra sell-in L9).

## Estado del dato
- Gap $429/$485/$57: **en mano** (storyline v6 + deck del canal L16), PERO el universo del $429M/mes está **por rotular [Martín/CC]**: no reconcilia contra el sell-in de L9; el chip lo declara en la lámina. Nada de cuadrar la diferencia en silencio: si CC/Martín rotulan el universo, se actualiza la fuente, no la cifra.
- Zona B (7 palancas y piloto $11M/23%): **en mano** (storyline v6 + deck del canal L16).
- Zona C (plan): **en mano**, salvo respuesta al frente Baxter/Vantive: **por completar [Martín, antes del 27]**.
- Zona D (aporte al hueco consolidado): **placeholder [RC]**.
- A ANEXO: la gráfica de dos columnas de dimensión del gap (ver Contenido diferido a anexo).

## Notas para el dibujante
- SIN caja de insight; sin etiquetas tipo "PLAN"/"INSIGHT" como rótulos de caja — los micro-títulos de zona son texto plano en navy, sin fondo ni marco.
- El ÚNICO gold de la lámina es la línea del gap $57M/mes (línea + su rótulo cuentan como un elemento). Nada más en gold.
- El panel izquierdo de dos columnas ($429 vs $485) YA NO SE DIBUJA: base y meta viven como texto en el rótulo de la línea gold. No reintroducirlo.
- Waterfall según sistema: positivos navy, total navy oscuro con mayor peso, connectors grises punteados. NO usar verde en las palancas (no son deltas realizados, son plan).
- La anotación "~$10M/mes aún sin palanca asignada" es deliberada y se queda explícita: honestidad contra "que no parezca justificación". No omitirla ni disfrazarla (decisión provisional #4 del README, transparencia ante Santiago).
- No convertir el waterfall en barra apilada con 7 colores: máximo contraste con un solo tono navy y labels claros.
- Aritmética conocida (no "corregir" en la lámina): $429 + $57 = $486 vs meta rotulada $485 (redondeo del canal; las series nativas son 88.35%/11.65%); las palancas nativas suman $47.28M vs $47M rotulado. Se imprimen los valores canónicos del storyline: 429 / 57 / 485 / 47 y los 7 valores enteros.
- La base ene-may excluye junio a propósito (mes con asterisco): mantener la nota, no cambiar la base a ene-jun.
- Los placeholders "[universo del $429M/mes por rotular: Martín/CC; no reconcilia contra sell-in L9]" y "[Aporte de Hospitales al hueco consolidado: RC]" se dibujan como texto gris visible, no se rellenan. Todos los corchetes son PLACEHOLDER INTERNO (kill antes del 27), declarado una sola vez en la línea de leyenda.
- Tabular figures en todo número; unidad "$M/mes" declarada en el eje del waterfall. Cero em-dash y cero carácter de flecha en texto imprimible.

### Contenido diferido a anexo
**A ANEXO — Dimensión del gap (panel retirado):**
- Micro-título: "La brecha, dimensionada". Gráfica de dos columnas verticales, $M/mes, eje Y desde 0, sin gridlines, sin leyenda:
  - Columna 1: Venta promedio ene-may 26 = $429M/mes — relleno `#0F2845`, data label $429.
  - Columna 2: Meta promedio jul-dic 26 = $485M/mes — relleno `#0F4C81`, data label $485 (~13% más alta que la columna 1).
  - Corchete entre el tope de ambas rotulado "Gap $57M/mes".
  - Nota: "Base ene-may: excluye junio (mes con asterisco)."
- Estado: en mano (mismas cifras que la línea de referencia del waterfall); hereda el chip del universo del $429M/mes.

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha. Márgenes amplios.

ESTRUCTURA VERTICAL: banda de título arriba (~13%), cuerpo al centro dividido en DOS columnas de anchos 58% / 42% (~78%), una banda de anotación de una línea encima de una línea de leyenda muy chica, y un pie delgado abajo (~5%).

BANDA DE TÍTULO (arriba, ancho completo): título en navy oscuro #0F2845, sans-serif ligera, grande, hasta dos líneas: "El gap del 2S es $57M/mes; las siete palancas identificadas cubren $47M/mes y julio es la prueba". Debajo, en gris azulado #44546A pequeño e itálica: "Medición formal desde julio; el piloto de junio capturó $11M, 23% del run-rate objetivo". Línea horizontal fina gris claro #E5E9EE de margen a margen.

COLUMNA IZQUIERDA (58%) — arriba, texto plano navy oscuro #0F2845 negrita: "Siete palancas, $47M/mes". Debajo, una gráfica de cascada (waterfall) acumulativa que sube de 0 a 47, unidad "$M/mes", eje Y desde 0. Ocho barras de izquierda a derecha, todas positivas en navy medio #0F4C81 salvo la última; conectores punteados finos gris #C5CDD9 entre barras; cada barra con su etiqueta de valor encima y el nombre de la palanca debajo del eje X en texto pequeño. Las barras están ordenadas de mayor a menor aporte; visualmente la primera barra ("$14M") es la más alta y van decreciendo hasta la penúltima ("$2M", la más baja, aproximadamente una séptima parte de la primera). Barras y valores en orden:
1. "Recuperación de cuentas" — "$14M"
2. "Plan Kener" — "$9M"
3. "Liberación de cartera" — "$7M"
4. "Nuevos productos" — "$6M"
5. "PIN no solicitado" — "$5M"
6. "Convenios" — "$4M"
7. "Cambio de tecnología" — "$2M"
8. Barra total "$47M/mes" en navy oscuro #0F2845 con mayor peso visual y su etiqueta en negrita.
Cruzando todo el ancho de esta gráfica, una LÍNEA HORIZONTAL PUNTEADA en color gold #C5A55A, situada más arriba que la barra total (a la altura de 57 en el eje, ~21% por encima del tope de la barra total de 47), rotulada a la derecha: "Gap $57M/mes" en gold negrita, y debajo de ese rótulo, en gris #5A6679 chico: "de $429M/mes de venta promedio ene-may a $485M/mes de meta jul-dic". Línea y rótulo son el ÚNICO elemento en color gold de toda la lámina. Entre el tope de la barra total y la línea gold, una anotación pequeña gris #3D4A5F: "~$10M/mes aún sin palanca asignada". Al pie de la gráfica, dos líneas de texto pequeño gris #5A6679: "Piloto junio: $11M capturados (23% del run-rate objetivo); medición formal desde julio. Base ene-may: excluye junio (mes con asterisco)." y, debajo, el chip literal en gris #8A95A8: "[universo del $429M/mes por rotular: Martín/CC; no reconcilia contra sell-in L9]".

COLUMNA DERECHA (42%) — arriba, texto plano navy oscuro #0F2845 negrita: "Cómo se ejecuta". Debajo, una lista de viñetas en gris #3D4A5F con aire generoso entre viñetas (verbatim):
- "Defensa de la base instalada: comodatos de infusión y soluciones frente a Mindray y Baxter/Vantive (servicio, costo total, contratos). [plan frente Baxter por cerrar: Martín]"
- "Plan Kener: defensa selectiva con precio gobernado, no guerra de descuentos."
- "Apriete de cumplimiento de convenios: +$3-4M/mes identificados; 32 hospitales en precio por volumen, $9.4M/mes de beneficio negociado."
- "Híbrido con centros de infusión: PiSA mezcla con cumplimiento regulatorio; ellos ponen pagadores (primer gate 14-jul)."
- "Riesgo declarado: las últimas pólizas con IVA deducible vencen en Q4."
El texto "[plan frente Baxter por cerrar: Martín]" se dibuja literal, en gris neutro, sin color de alerta ni icono.

BANDA DE ANOTACIÓN (una línea, ancho completo): a la izquierda, en gris muy oscuro #1A2332: "Julio es el mes de la prueba: sin quinto lunes, el run-rate de palancas debe compensar el calendario." A la derecha, en gris claro #8A95A8, se dibuja literal el placeholder: "[Aporte de Hospitales al hueco consolidado: RC]".

LÍNEA DE LEYENDA (encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE (abajo, ancho completo): línea fina gris claro #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: Sell-In cierre jun-26 (venta promedio ene-may) y metas jul-dic 2026; palancas y piloto: plan del canal Hospitales, jul-26. Universo del $429M/mes por rotular (no reconcilia contra sell-in L9)." A la derecha: "PiSA Confidencial | 25".

PROHIBIDO: el carácter de flecha o em-dash en cualquier texto; emojis; rótulos de caja tipo "INSIGHT", "SO WHAT" o "PLAN"; bordes laterales de color; verde en las barras del waterfall (son plan, no resultados); más de un elemento en gold; dibujar una gráfica aparte de dos columnas para la base y la meta (base y meta viven SOLO como texto del rótulo de la línea gold); rellenar o estimar los placeholders entre corchetes. Los micro-títulos de columna son texto plano navy, sin fondo ni marco.
```


---

# Lámina 26 · Servicios pesa 13.4% de la venta y es el único segmento arriba de meta: 102.1% y +4.0%
- **Momento:** M6 · Servicios: entorno, 1S, 2S (13.4% de la venta)
- **Encabezado:** Servicios pesa 13.4% de la venta y es el único segmento arriba de meta: 102.1% y +4.0%
- **So-what subtitle:** Primera vez que el segmento se presenta en una junta de Consejo: nefrología, mezclas y anestesia
- **Layout:** banda de título 13% + banda de KPIs 15% + cuerpo 67% en dos columnas 35/65 (izquierda: qué es el segmento · derecha: las cuatro líneas con venta y crecimiento) + footer 5%. Geometría: 13.333 × 7.5 in, márgenes 0.5 in; título y 0.5–1.35; KPIs y 1.5–2.45; cuerpo y 2.6–6.6; footer y 6.7–7.0.

## Zona por zona

**Zona A — Banda de título (12.333 × 0.85 in).**
Título Calibri Light 32 pt `#0F2845`; so-what 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE`.

**Zona B — KPI row (5 tarjetas iguales de ~2.3 in, y 1.5–2.45 in).**
Tarjetas con fondo `#F0F3F7` (sin borde adicional), padding 0.2 in. Label Calibri Light 10.5 pt `#5A6679` MAYÚSCULAS; valor Calibri bold 36-40 pt `#0F2845` tabular:
1. **% DE LA VENTA PiSA 1S26**: `13.4%` (contexto 10 pt: "sobre $16,518.5M, 5 mercados sell-in")
2. **VENTA 1S26**: `$2,219.4M` (contexto: "ene-jun 2026, sell-in")
3. **CUMPLIMIENTO DE META**: `102.1%` — este valor en gold `#C5A55A` (ÚNICO gold de la lámina; contexto: "único segmento arriba de meta")
4. **CRECIMIENTO**: `+4.0%` (contexto: "vs ene-jun 2025")
5. **EBITDA 1S26**: `14.5%` (contexto: "+5.8pp vs 1S25 (8.7%): el margen que más expande")
Nota bajo la KPI row, Calibri Light 9 pt `#8A95A8`, una línea: "EBITDA: split del bloque Gobierno por Gross2Net; cuadra con Estado de Resultados v18 al peso, ±$3.6M de Nuevos Productos sin repartir [bendición Finanzas pendiente: VJ]".

**Zona C — Qué es Servicios (columna izquierda, ~4.1 in de ancho). Tres bloques de definición + una línea de demanda.**
Tres bloques apilados, cada uno con top border 1 pt `#0F4C81` (nunca border-left), título Calibri bold 12 pt `#0F2845` y descripción Calibri Light 10.5 pt `#3D4A5F`:
1. **Nefrología** — Hemodiálisis y diálisis peritoneal.
2. **Mezclas** — Oncología y nutrición.
3. **Servicios integrales de anestesia** — SIA.
Cierre de columna (una línea, Calibri Light 11 pt `#1A2332`): "Demanda estructural creciente: las enfermedades crónicas y la diabetes sostienen hemodiálisis y mezclas."

**Zona D — Las cuatro líneas del segmento (columna derecha, ~7.6 in de ancho). Barras horizontales.**
- Micro-título de zona: "Venta 1S26 por línea, $M" — Calibri bold 12 pt `#0F2845`.
- Barras horizontales navy `#0F2845`, ordenadas por valor (mayor arriba), espacio entre barras ≥ 50% del ancho de barra, sin gridlines, sin leyenda, data label al final de cada barra (valor $M en `#1A2332` 10 pt) + delta vs 1S25 junto al label, con semáforo:
  1. Mezclas — **$886M** · `−4%` (delta en `#C00000`)
  2. Diálisis — **$735M** · `+10%` (delta en `#2E7D4F`)
  3. Hemodiálisis — **$545M** · `+13%` (delta en `#2E7D4F`)
  4. Anestesia — **$53M** · `−13%` (delta en `#C00000`)
- Línea de cuadre bajo el chart, Calibri Light 10 pt `#5A6679`: "Suma de líneas = $2,219.4M: cuadre exacto con el sell-in del segmento."

**Zona E — Footer.**
Línea 0.5 pt `#E5E9EE`; fuente 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 26" derecha.

## Mensaje que manda la lámina
Servicios existe, pesa 13.4% de la venta, es el único segmento arriba de meta (102.1%, +4.0%) y su margen ya es citable: EBITDA 14.5%, el que más expande (+5.8pp); son tres modelos de negocio, nefrología, mezclas y anestesia, cuyas cuatro líneas cuadran exacto contra el sell-in, con demanda estructural que crece.

## Fuente (pie de lámina)
Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Servicios (4 líneas); EBITDA: Estado de Resultados v18 + split del bloque Gobierno por Gross2Net, ene-jun-26 [bendición Finanzas pendiente: VJ].

## Estado del dato
- Zonas A/C/D: **en mano** (storyline v6; líneas verificadas contra deck del canal Servicios y cuadre exacto con sell-in $2,219.4M).
- KPI 5 (EBITDA 14.5%, +5.8pp vs 8.7% de 1S25): **en mano, NUEVO 16-jul** — tablita v18 + split Gross2Net del bloque Gobierno (Servicios $321.8M / 14.5%); cuadra a $3,879.6M total al peso; ±$3.6M de Nuevos Productos sin repartir declarado. Bendición Finanzas pendiente [VJ]: si VJ no bendice antes del 22, el KPI baja a chip.
- ACTUALIZACIÓN 16-jul: "buen margen" ya ES imprimible con dato (deroga la instrucción previa de no imprimir cifra de margen en esta lámina).

## Notas para el dibujante
- Es la lámina que hace descubrir el segmento al Consejo: densidad baja, mucho aire. NO meter competencia ni P&L completo aquí — la dinámica competitiva vive en la L27; del margen SOLO el KPI 5 con su nota de fuente (el detalle por sub-línea vive en L30).
- La nota de EBITDA bajo la KPI row es OBLIGADA mientras la bendición de Finanzas esté pendiente; no borrarla ni resumirla. El corchete [VJ] es [PLACEHOLDER INTERNO - kill antes del 27].
- ÚNICO gold: el valor `102.1%` del KPI 3. Nada más en gold (el 14.5% va en navy).
- Semáforo SOLO en los cuatro deltas de la Zona D (+10/+13 verde, −4/−13 rojo). Los KPIs de la Zona B van en navy, incluido el +4.0% (es el hero del segmento, no un semáforo).
- Prohibido escribir "no hay competencia" o "sin competencia" en cualquier parte de esta lámina (regla de tono del storyline); la ventaja competitiva se cuenta en la L27.
- "Diálisis" se rotula así, a secas (es la línea de diálisis del sell-in); no abrirla en DP/mezclas de diálisis ni mezclar con el sizing de pacientes de la L27.
- Las etiquetas $886/$735/$545/$53 son redondeadas y suman $2,219M; el cuadre exacto ($2,219.4M) es con decimales de fuente — por eso la línea de cuadre cita $2,219.4M y las barras van redondeadas. No "ajustar" barras para que sumen exacto.
- Tabular figures en KPIs y data labels. Sin caja de insight, sin etiquetas de bloque, sin emojis, sin border-left (los bloques de la Zona C llevan top border).

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha. Densidad baja, mucho aire.

ESTRUCTURA VERTICAL: banda de título arriba (~13%), fila de 5 tarjetas KPI debajo (~15%) con una nota de una línea al pie de la fila, cuerpo con DOS columnas de anchos 35% / 65% (~65%), y pie delgado abajo (~5%).

BANDA DE TÍTULO (arriba, ancho completo): título en navy oscuro #0F2845, sans-serif ligera, grande: "Servicios pesa 13.4% de la venta y es el único segmento arriba de meta: 102.1% y +4.0%". Debajo, en gris azulado #44546A pequeño e itálica: "Primera vez que el segmento se presenta en una junta de Consejo: nefrología, mezclas y anestesia". Línea horizontal fina gris claro #E5E9EE de margen a margen.

FILA DE KPIs: CINCO tarjetas del mismo tamaño, lado a lado, con fondo gris muy claro #F0F3F7 (sin borde). Cada tarjeta con una etiqueta pequeña en MAYÚSCULAS gris #5A6679 arriba, un valor grande en negrita, y una línea de contexto pequeña gris abajo. Contenido (verbatim):
1. Etiqueta "% DE LA VENTA PiSA 1S26"; valor grande navy oscuro #0F2845 "13.4%"; contexto "sobre $16,518.5M, 5 mercados sell-in".
2. Etiqueta "VENTA 1S26"; valor grande navy oscuro #0F2845 "$2,219.4M"; contexto "ene-jun 2026, sell-in".
3. Etiqueta "CUMPLIMIENTO DE META"; valor grande en color gold #C5A55A "102.1%" (este es el ÚNICO elemento en gold de toda la lámina); contexto "único segmento arriba de meta".
4. Etiqueta "CRECIMIENTO"; valor grande navy oscuro #0F2845 "+4.0%"; contexto "vs ene-jun 2025".
5. Etiqueta "EBITDA 1S26"; valor grande navy oscuro #0F2845 "14.5%"; contexto "+5.8pp vs 1S25 (8.7%): el margen que más expande".
Bajo la fila de tarjetas, una nota de UNA línea en gris claro #8A95A8, dibujada literal con su corchete: "EBITDA: split del bloque Gobierno por Gross2Net; cuadra con Estado de Resultados v18 al peso, ±$3.6M de Nuevos Productos sin repartir [bendición Finanzas pendiente: VJ]".

COLUMNA IZQUIERDA (35%) — tres bloques de definición apilados, cada uno con un top border fino (1 pt) navy medio #0F4C81 arriba (nunca borde lateral), un título en navy oscuro #0F2845 negrita pequeño y una descripción en gris #3D4A5F:
1. Título "Nefrología" — descripción "Hemodiálisis y diálisis peritoneal."
2. Título "Mezclas" — descripción "Oncología y nutrición."
3. Título "Servicios integrales de anestesia" — descripción "SIA."
Bajo los tres bloques, una línea en gris muy oscuro #1A2332: "Demanda estructural creciente: las enfermedades crónicas y la diabetes sostienen hemodiálisis y mezclas."

COLUMNA DERECHA (65%) — arriba, texto plano navy oscuro #0F2845 negrita: "Venta 1S26 por línea, $M". Debajo, una gráfica de BARRAS HORIZONTALES en navy oscuro #0F2845, ordenadas por valor de mayor a menor (mayor arriba), con espacio generoso entre barras, sin gridlines, sin leyenda. Al final de cada barra, la etiqueta de valor en $M en gris muy oscuro #1A2332 y, junto a ella, el delta vs 1S25 con color de semáforo. Barras de arriba hacia abajo (la primera es la más larga; la cuarta es minúscula, aproximadamente un dieciseisavo de la primera):
1. "Mezclas" — "$886M" · delta "−4%" en rojo #C00000
2. "Diálisis" — "$735M" · delta "+10%" en verde #2E7D4F
3. "Hemodiálisis" — "$545M" · delta "+13%" en verde #2E7D4F
4. "Anestesia" — "$53M" · delta "−13%" en rojo #C00000
La barra 2 (Diálisis) mide aproximadamente el 83% de la barra 1; la barra 3 (Hemodiálisis) aproximadamente el 62%; la barra 4 (Anestesia) es muy corta. Bajo la gráfica, texto pequeño gris #5A6679: "Suma de líneas = $2,219.4M: cuadre exacto con el sell-in del segmento."

PIE (abajo, ancho completo): línea fina gris claro #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Servicios (4 líneas); EBITDA: Estado de Resultados v18 + split del bloque Gobierno por Gross2Net, ene-jun-26 [bendición Finanzas pendiente: VJ]." A la derecha: "PiSA Confidencial | 26".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (los bloques de la izquierda llevan top border, no border-left); más de un elemento en gold (el "14.5%" de EBITDA va en navy, NO en gold); usar semáforo de color fuera de los cuatro deltas de la gráfica de barras (los KPIs, incluidos "+4.0%" y "+5.8pp", van en navy, no en verde). No escribir "no hay competencia" ni "sin competencia". Los corchetes se dibujan literales en gris (placeholders internos del borrador).
```


---

# Lámina 27 · No es un mercado clásico: cada modelo compite en su propia cancha, con fosos y riesgos distintos
- **Momento:** M6 · Servicios: entorno, 1S, 2S (13.4% de la venta)
- **Encabezado:** No es un mercado clásico: cada modelo compite en su propia cancha, con fosos y riesgos distintos
- **So-what subtitle:** El rival renal es Vantive-Carlyle con capital fresco; el foso real de DP es la logística domiciliaria
- **Layout:** banda de título 13% + cuerpo 82% en dos filas: fila superior 55% = panel Diálisis peritoneal (interno 60/40: gráfica de pacientes / bullets), fila inferior 45% = dos paneles 50/50 (Hemodiálisis | Mezclas y SIA) + footer 5%. Geometría: 13.333 × 7.5 in, márgenes 0.5 in; título y 0.5–1.35; fila DP y 1.5–4.25; fila inferior y 4.4–6.6; footer y 6.7–7.0.

## Zona por zona

**Zona A — Banda de título (12.333 × 0.85 in).**
Título Calibri Light 32 pt `#0F2845` (28 pt si pide 2 líneas); so-what 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE`.

**Zona B — Panel Diálisis peritoneal pública (fila superior completa, 12.333 × 2.75 in).**
Encabezado de panel: "Diálisis peritoneal (sector público)" — Calibri bold 13 pt `#0F2845`, texto plano.

*B1 — Gráfica (izquierda, ~7.2 in): barras horizontales apiladas, pacientes/año.* Universo único: pacientes (licitaciones detectadas 2025-26). Dos series: PiSA navy `#0F2845`, Baxter/Vantive gris `#8A95A8`; leyenda directa (rótulo de serie sobre la primera barra, sin caja de leyenda); data labels con pacientes y % (10 pt). REGLA 16-jul: las etiquetas van DENTRO del tramo solo si el tramo es ancho; en segmentos CHICOS (PiSA 550 en Otros, y cualquier tramo angosto) la etiqueta va FUERA de la barra, a la derecha, con línea guía fina `#C5CDD9`; nunca encimar texto sobre un tramo angosto:
1. **Total público 53,400** — PiSA 16,550 (31%) · Baxter/Vantive 36,850 (69%) — barra con mayor peso (más alta), separada 0.15 in del resto
2. **IMSS 38,000** — PiSA 16,000 (42%) · Baxter/Vantive 22,000 (58%)
3. **IMSS Bienestar 7,800** — Baxter/Vantive 7,800 (100%) — anotación gris 9.5 pt a la derecha: "cobranza: retrasos de pago"
4. **ISSSTE 6,100** — Baxter/Vantive 6,100 (100%) — anotación gris 9.5 pt: "restricciones técnicas (icodextrina, CRRT)"
5. **Otros 1,500** — PiSA 550 (37%) · Baxter/Vantive 950 (63%) — etiquetas de ambos tramos FUERA de la barra (segmentos chicos)
Línea de valor bajo la gráfica, Calibri Light 10 pt `#5A6679`: "Valor anual del mercado $5,631M: PiSA $1,448M (26%) vs Baxter/Vantive $4,182M (74%)."

*B2 — Bullets DP (derecha, ~4.6 in), Calibri Light 10.5 pt `#3D4A5F` (sin em-dash):*
- Baxter es 27-49% más caro por bolsa; el precio no es el foso.
- **El foso real es la logística: entrega mensual a domicilio en todo el país** — esta línea en gold `#C5A55A` bold (ÚNICO gold de la lámina).
- IMSS Bienestar e ISSSTE, hoy 100% Baxter: espacio de entrada, limitado por restricciones técnicas y cobranza.
- En IMSS dominamos 17 de 47 delegaciones [base por validar: DS; IMSS opera ~35 OOAD].
- El rival renal ya no es Baxter: es Vantive-Carlyle, con capital fresco (USD 70M en Cuernavaca).

**Zona C — Panel Hemodiálisis (fila inferior izquierda, ~6.0 in).**
Encabezado de panel: "Hemodiálisis" — Calibri bold 13 pt `#0F2845`. Bullets Calibri Light 10.5 pt `#3D4A5F`:
- SANEFRO: 12 clínicas en 6 estados, 4,110 pacientes, ~$1,005M anuales.
- Crece +13% en el 1S (6% sesiones, 7% precio); relativamente blindada por infraestructura y costo.
- Riesgo tecnológico a declarar: adelantar la inversión antes de que llegue el jugador chino; que no nos pase lo de bombas de infusión.

**Zona D — Panel Mezclas y SIA (fila inferior derecha, ~6.0 in).**
Encabezado de panel: "Mezclas y SIA" — Calibri bold 13 pt `#0F2845`. TRES bullets (instrucción 16-jul: el bloque se queda en 3, sin sub-bullets ni segunda oración suelta), Calibri Light 10.5 pt `#3D4A5F`:
- Nutrición: somos únicos. En Onco la competencia seria ya está adentro: centros de mezclas (COI, 12 sedes), consorcios y oncólogos con clínicas propias.
- Precio de mezclado onco muy por arriba de la competencia (~$831 vs ~$600 por mezcla): sostiene margen hoy, es fragilidad mañana; riesgo gestionado.
- SIA: un solo competidor, pero es el líder y ~4 veces nuestro tamaño (Biossmann), concentrado en gobierno (85% de su venta); en el privado la brecha es menor.

**Zona E — Footer.**
Línea 0.5 pt `#E5E9EE`; fuente 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 27" derecha.

## Mensaje que manda la lámina
Servicios no compite en un mercado clásico: en diálisis peritoneal el 69% de los pacientes públicos está con Baxter/Vantive (espacio y amenaza a la vez) y el foso es logístico; hemodiálisis está blindada pero pide inversión tecnológica anticipada; en mezclas onco el precio alto es margen hoy y fragilidad mañana; en SIA el líder es 4 veces mayor pero concentrado en gobierno.

## Fuente (pie de lámina)
Fuente: dimensionamiento del canal Servicios sobre licitaciones del sector público 2025-2026 (pacientes/año DP; no es mercado auditado); SANEFRO corte jun-26; sell-in cierre jun-26 (crecimientos por línea); investigación externa jul-26 (Vantive-Carlyle).

## Estado del dato
- Zona B (sizing DP, pacientes y $): **en mano** (deck del canal Servicios, cuadres internos verificados: 38,000+7,800+6,100+1,500 = 53,400; 16,000+550 = 16,550).
- Zona B2 (Vantive USD 70M): **en mano** (research jul-26, confiabilidad alta).
- Zona C (SANEFRO): **en mano**.
- Zona D: **en mano**, con el precio onco por conciliar (ver notas). Atribución del COI: aquí se imprime "COI" a secas (la razón social queda por confirmar con DS; el texto previo decía "COI de Fanasa"). OJO consistencia: la L21 imprime "COI/FESA" como flujo del pagador por instrucción de Rafael 16-jul; conciliar la atribución única (Fanasa vs FESA) con DS antes del 22.
- Bullet "17 de 47 delegaciones": chip NUEVO 16-jul "[base por validar: DS; IMSS opera ~35 OOAD]" — la base de 47 no cuadra con las ~35 OOAD con que opera IMSS; no citar sin validar la base.

## Notas para el dibujante
- Lámina densa por diseño (una lámina para los tres modelos, instrucción Rafael 15-jul): compensar con jerarquía clara — el panel DP domina, los dos inferiores son secundarios. No reducir tipografía por debajo de 9.5 pt.
- ÚNICO gold: la línea del foso logístico en B2. El resto de énfasis en navy bold puntual.
- La gráfica B1 es SOLO pacientes; el valor en $ vive en la línea de texto bajo la gráfica. No mezclar pacientes y pesos en una misma barra ni en un mismo eje (universos no se mezclan).
- Rojo/verde: NO usar. Las anotaciones "cobranza" y "restricciones técnicas" van en gris `#5A6679`, no en rojo — no son deltas.
- "Baxter/Vantive" siempre con esa grafía en serie y bullets (corrección del research: las plantas renales son de Vantive-Carlyle desde ene-25).
- Kener NO aparece en esta lámina (vive en el bloque Hospitales). No importar los tres frentes aquí.
- Prohibido "no hay competencia"; el registro correcto es el del storyline: "un solo competidor, pero es el líder", "somos únicos" (nutrición). No agregar superlativos.
- Trampa de cifra: el v6 dice precio onco "~$831 vs ~$600"; el deck del canal (L11) muestra ONCO 2026 = $821 y competidores Pharmatycsa $662 / Serbitec $570 ("24% arriba del principal competidor"). Manda el storyline (~$831 vs ~$600) pero la cifra queda por conciliar [DS/Rafael] antes del 22 — dibujar con los valores del storyline y marcar en la nota interna de build.
- SANEFRO ~$1,005M es venta ANUAL y los crecimientos por línea son YTD sell-in: no ponerlos en una misma gráfica ni sumarlos; en bullets separados como está especificado.
- "17 de 47 delegaciones" se imprime como frase CON su chip "[base por validar: DS; IMSS opera ~35 OOAD]"; NO imprimir las tablas de delegaciones del deck del canal (traen bases inconsistentes entre sí; el detalle vive en anexo). Todo corchete con responsable es [PLACEHOLDER INTERNO - kill antes del 27].
- Etiquetas del stacked bar: fuera de los segmentos chicos (con línea guía); dentro solo cuando el tramo respira. Cero em-dash en texto imprimible.
- Sin caja de insight, sin rótulos de bloque tipo "HIGHLIGHTS" (así viene en el deck del canal: no heredarlo), sin emojis, sin border-left; encabezados de panel como texto plano navy.

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha. Lámina densa: jerarquía clara, el panel superior domina, los dos inferiores son secundarios; no reducir el texto por debajo de un tamaño legible.

ESTRUCTURA VERTICAL: banda de título arriba (~13%), cuerpo (~82%) en DOS filas: fila superior (~55% del cuerpo) es un solo panel ancho; fila inferior (~45%) son dos paneles 50/50 lado a lado; pie delgado abajo (~5%).

BANDA DE TÍTULO (arriba, ancho completo): título en navy oscuro #0F2845, sans-serif ligera, grande, hasta dos líneas: "No es un mercado clásico: cada modelo compite en su propia cancha, con fosos y riesgos distintos". Debajo, en gris azulado #44546A pequeño e itálica: "El rival renal es Vantive-Carlyle con capital fresco; el foso real de DP es la logística domiciliaria". Línea horizontal fina gris claro #E5E9EE de margen a margen.

FILA SUPERIOR — un panel ancho. Encabezado en texto plano navy oscuro #0F2845 negrita: "Diálisis peritoneal (sector público)". Dentro, dos zonas: a la izquierda (~60%) una gráfica, a la derecha (~40%) viñetas.
  Gráfica izquierda: BARRAS HORIZONTALES APILADAS, universo "pacientes/año". Dos series por barra: PiSA en navy oscuro #0F2845 y "Baxter/Vantive" en gris #8A95A8; rotular el nombre de cada serie directamente sobre la primera barra (sin caja de leyenda). Cada tramo lleva su número de pacientes y su porcentaje; IMPORTANTE: si un tramo es angosto, su etiqueta va FUERA de la barra (a la derecha, con una línea guía fina gris #C5CDD9), nunca encimada sobre el tramo. Cinco barras de arriba hacia abajo:
  1. "Total público 53,400" — tramo PiSA "16,550 (31%)" + tramo Baxter/Vantive "36,850 (69%)"; esta barra es la de mayor peso (la más larga/gruesa) y va separada del resto por un espacio.
  2. "IMSS 38,000" — tramo PiSA "16,000 (42%)" + tramo Baxter/Vantive "22,000 (58%)".
  3. "IMSS Bienestar 7,800" — barra 100% Baxter/Vantive (gris completa); anotación gris pequeña a la derecha: "cobranza: retrasos de pago".
  4. "ISSSTE 6,100" — barra 100% Baxter/Vantive (gris completa); anotación gris pequeña a la derecha: "restricciones técnicas (icodextrina, CRRT)".
  5. "Otros 1,500" — tramo PiSA "550 (37%)" + tramo Baxter/Vantive "950 (63%)"; las etiquetas de esta barra van FUERA (los dos tramos son chicos).
  Proporciones: la barra 1 (53,400) es la más larga; la 2 (38,000) mide aproximadamente el 71% de la 1; las barras 3 y 4 son cortas (aprox. una séptima parte de la 1) y la 5 es la más corta. Bajo la gráfica, texto pequeño gris #5A6679: "Valor anual del mercado $5,631M: PiSA $1,448M (26%) vs Baxter/Vantive $4,182M (74%)."
  Viñetas derecha, en gris #3D4A5F (verbatim):
  - "Baxter es 27-49% más caro por bolsa; el precio no es el foso."
  - "El foso real es la logística: entrega mensual a domicilio en todo el país" — esta línea entera en color gold #C5A55A negrita (ÚNICO elemento en gold de toda la lámina).
  - "IMSS Bienestar e ISSSTE, hoy 100% Baxter: espacio de entrada, limitado por restricciones técnicas y cobranza."
  - "En IMSS dominamos 17 de 47 delegaciones [base por validar: DS; IMSS opera ~35 OOAD]." (el corchete se dibuja literal, en gris)
  - "El rival renal ya no es Baxter: es Vantive-Carlyle, con capital fresco (USD 70M en Cuernavaca)."

FILA INFERIOR IZQUIERDA — panel. Encabezado texto plano navy oscuro #0F2845 negrita: "Hemodiálisis". Viñetas en gris #3D4A5F (verbatim):
  - "SANEFRO: 12 clínicas en 6 estados, 4,110 pacientes, ~$1,005M anuales."
  - "Crece +13% en el 1S (6% sesiones, 7% precio); relativamente blindada por infraestructura y costo."
  - "Riesgo tecnológico a declarar: adelantar la inversión antes de que llegue el jugador chino; que no nos pase lo de bombas de infusión."

FILA INFERIOR DERECHA — panel. Encabezado texto plano navy oscuro #0F2845 negrita: "Mezclas y SIA". EXACTAMENTE tres viñetas en gris #3D4A5F (verbatim):
  - "Nutrición: somos únicos. En Onco la competencia seria ya está adentro: centros de mezclas (COI, 12 sedes), consorcios y oncólogos con clínicas propias."
  - "Precio de mezclado onco muy por arriba de la competencia (~$831 vs ~$600 por mezcla): sostiene margen hoy, es fragilidad mañana; riesgo gestionado."
  - "SIA: un solo competidor, pero es el líder y ~4 veces nuestro tamaño (Biossmann), concentrado en gobierno (85% de su venta); en el privado la brecha es menor."

PIE (abajo, ancho completo): línea fina gris claro #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: dimensionamiento del canal Servicios sobre licitaciones del sector público 2025-2026 (pacientes/año DP; no es mercado auditado); SANEFRO corte jun-26; sell-in cierre jun-26 (crecimientos por línea); investigación externa jul-26 (Vantive-Carlyle)." A la derecha: "PiSA Confidencial | 27".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT", "SO WHAT" o "HIGHLIGHTS"; bordes laterales de color; más de un elemento en gold; usar rojo o verde en ninguna parte (las anotaciones "cobranza" y "restricciones técnicas" van en gris, no en rojo); rayas largas (em-dash) dentro de la prosa de las viñetas. Encabezados de panel como texto plano navy. La gráfica es SOLO de pacientes; no mezclar pesos ($) dentro de las barras. Los corchetes se dibujan literales en gris (placeholders internos del borrador; se eliminan antes de la versión final).
```


---

# Lámina 28 · Servicios crece +$84.5M: hemodiálisis pone el 73% y la diálisis sube 15% el precio por bolsa con volumen plano
- **Momento:** M6 · Servicios: entorno, 1S, 2S (13.4% de la venta)
- **Encabezado:** Servicios crece +$84.5M: hemodiálisis pone el 73% y la diálisis sube 15% el precio por bolsa con volumen plano
- **So-what subtitle:** Sell-in Servicios de $2,134.9M a $2,219.4M (+$84.5M, 102.1% de meta); puente 100% por valor (45.6% del bruto sin unidad), idéntico en los tres niveles de conciliación
- **Layout:** banda de título 15% + cuerpo 66% en tres columnas 15/50/35 (col 1 mercado n/a · col 2 puente por VALOR resuelto + panel anexo de diálisis peritoneal · col 3 palancas + validación por modelo) + caveat 9% + footer 10%. Geometría 13.333 × 7.5 in, márgenes 0.5 in, área útil 12.333 in. Título y 0.5–1.55 in; cuerpo y 1.65–6.3 in; caveat y 6.35–6.75 in; footer y 6.85–7.1 in. Anchos: col 1 ≈ 1.8 in, col 2 ≈ 6.0 in, col 3 ≈ 4.2 in, gutter 0.15 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 1.0 in).**
Título asertivo Calibri Light 28 pt `#0F2845` (2 líneas), sin punto final; so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Cuerpo, tres columnas (convención de puente 15/50/35).**

*Columna 1 (15%, ≈1.8 in) — Mercado vs PiSA: declaración n/a.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Mercado vs PiSA".
- Bloque de texto centrado, Calibri Light 12 pt `#5A6679`: "n/a". Debajo, Calibri Light 10 pt `#8A95A8`: "modelos propios sin mercado auditado comparable (se declara)".
- Sin barra: la columna 1 aquí es una declaración, no una gráfica. Un rectángulo tenue de fondo `#FAFBFC` con contorno 0.5 pt `#E5E9EE`, sin border-left, encierra la declaración.

*Columna 2 (50%, ≈6.0 in) — Puente por VALOR (RESUELTO) + panel anexo de diálisis peritoneal.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Puente por valor, cuatro bloques".
- Eyebrow de universo, Calibri Light 9 pt `#5A6679`: "Sell-in Gob Servicios · workbook Downtrading GobServicios FINAL 16-jul · 100% por valor".
- BLOQUE SUPERIOR (~60% de la columna) — Waterfall por VALOR, $M, eje Y desde 0, connectors punteados 0.5 pt `#C5CDD9`, data label con signo sobre cada barra:
  - Barra inicial (navy `#0F2845`): **$2,134.9M** — data label "1S25 · $2,134.9M".
  - Cuatro bloques de valor:
    1. "Servicios (serie 9)" — **+54.3** — navy `#0F4C81`, con anotación 9 pt `#5A6679`: "hemodiálisis, material 9000915: +$61.5M = 73% de la Δ del segmento".
    2. "Canastas VARIOS" — **+36.7** — navy `#0F4C81`.
    3. "Diálisis peritoneal" — **+69.4** — navy `#0F4C81`, con anotación 9 pt `#5A6679`: "ver panel P/V/M abajo".
    4. "Resto molécula" — **−75.9** — rojo `#C00000`, con anotación 9 pt `#5A6679`: "Pembrolizumab −$60.4M, fin de contrato".
  - Barra final (navy `#0F2845`): **$2,219.4M** — data label "1S26 · $2,219.4M (102.1% de meta)".
- Línea de lanzamientos (una línea), Calibri Light 9.5 pt `#3D4A5F`: "Lanzamientos = $0 por diseño: las altas de licitación (+$26.9M; Ocrelizumab +$18.9M) son biosimilares ganando licitación y viven dentro de resto molécula, nunca en la línea Lanzamientos."
- BLOQUE INFERIOR (~30% de la columna) — Panel anexo "Diálisis peritoneal: P/V/M por bolsa" (micro-rótulo Calibri Light 10 pt `#5A6679`): mini-puente horizontal de tres efectos + total, barras chicas con data label:
  - "Precio" **+96.2** (navy `#0F4C81`) · "Volumen" **−8.6** (rojo `#C00000`; nota "bolsas −1.3%") · "Mix de formato" **−18.1** (rojo `#C00000`; nota "bolsa 2L") = **+$69.4M**.
  - Línea de lectura, Calibri Light 9.5 pt `#3D4A5F`: "Precio por bolsa +15% con volumen plano: la diálisis es historia de precio, no de piezas."
- Nota de conciliación y mapeo (una línea), Calibri Light 9 pt `#8A95A8`: "Δ +$84.5M idéntica en los tres niveles (sin reclasificaciones). En la matriz consolidada del total (L8), diálisis (+$69.4M) y resto molécula (−$75.9M) viajan neteados como 'sin unidad' −$6.5M."

*Columna 3 (35%, ≈4.2 in) — Palancas comerciales + validación por modelo.*
- Micro-título de zona, Calibri bold 12 pt `#0F2845`: "Palancas y validación".
- Bloque 1 — palancas 1S25 vs 1S26, tres renglones Calibri Light 11 pt `#3D4A5F`:
  1. Venta perdida: ~**0** (no es palanca de este segmento).
  2. PIN no solicitado: **n/d** — "[vacío declarado, no se inventa]".
  3. NC comerciales y sanciones: de ~0 a **−$1.1M**; devoluciones: de **−$2.6M** a **−$3.7M**, con la marca "inmateriales (Gross2Net)".
- Línea 0.5 pt `#E5E9EE` de separación.
- Bloque 2 — validación por modelo (YTD, cuadra exacto con el sell-in), Calibri Light 11 pt `#3D4A5F`, cuatro renglones + total:
  - Mezclas: **$886M** (−4%)
  - Diálisis: **$735M** (+10%)
  - Hemodiálisis: **$545M** (+13%)
  - Anestesia: **$53M** (−13%)
  - Total: **$2,219.4M** en Calibri bold 13 pt `#C5A55A` (gold), con la marca "= sell-in Servicios, cuadra exacto". ÚNICO elemento gold de la lámina.

**Zona C — Caveat de universo (12.333 × 0.4 in).**
Texto Calibri Light 9.5 pt `#8A95A8`, dos renglones: "Servicios no tiene mercado auditado comparable: la col 1 se declara n/a. El puente es 100% por valor porque 45.6% del bruto no trae molécula ni unidad; el único pool con P/V/M real por pieza es la diálisis peritoneal (panel). Las cuatro líneas por modelo (venta real YTD) suman exacto $2,219.4M, el mismo sell-in del segmento."

**Zona D — Footer (12.333 × 0.25 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 28" derecha.

## Mensaje que manda la lámina
Servicios es el único segmento arriba de meta (+4.0%, 102.1%) y su crecimiento ya tiene nombre: la hemodiálisis (material 9000915, +$61.5M) pone el 73% de la Δ, y la diálisis peritoneal aporta +$69.4M que son casi puro precio (+15% por bolsa con bolsas −1.3%). El lastre es el fin del contrato de Pembrolizumab (−$60.4M dentro de resto molécula). La credibilidad de la lámina la ancla la validación por modelo: las cuatro líneas YTD suman exacto el sell-in ($2,219.4M).

## Fuente (pie de lámina)
Fuente: workbook Downtrading GobServicios FINAL 16-jul sobre Sell-In cierre jun-26, Servicios 1S26 vs 1S25 (puente 100% por valor; anexo diálisis P/V/M por bolsa); líneas por modelo: venta real YTD (deck Servicios); NC y devoluciones: Gross2Net Finanzas.

## Estado del dato
- Col 1 (n/a): **declaración** (modelos propios sin mercado comparable).
- Col 2 — RESUELTA: el puente por valor está **en mano y verificado al peso** (EXTRACT_puentes_consolidado_gobserv §6, CONTROL 0.0000): Servicios +54.3 (HD 9000915 +61.5 = 73% de la Δ) / Canastas VARIOS +36.7 / Diálisis peritoneal +69.4 / Resto molécula −75.9 (Pembrolizumab −60.4; altas de licitación +26.9 con Ocrelizumab +18.9) / Lanzamientos 0.0 por diseño = +84.5 EXACTO (2,134.9 + 84.5 = 2,219.4). Anexo DP: Precio +96.2 / Volumen −8.6 (bolsas −1.29%) / Mix formato −18.1 = +69.4; precio por bolsa +15%. Redondeo declarado: los 3 efectos del panel DP a 1 decimal suman 69.5 vs 69.4 canónico (exacto al 4º decimal: 96.1587 − 8.6191 − 18.1151 = 69.4245); se imprime el 69.4 canónico. Δ idéntica en los tres niveles de conciliación (sin reclasificaciones ni filas sin MATNR).
- DISCREPANCIA DE LA ORDEN, RESUELTA CONTRA FUENTE: la orden del 16-jul enunciaba los 4 bloques como "+54.3 / +36.7 / −75.9 / −6.5 = +84.5", lista que NO suma (+8.6). El workbook verificado define los bloques que sí suman: +54.3 +36.7 +69.4 −75.9 = +84.5; el "−6.5 sin unidad" de la matriz consolidada es la agregación de diálisis (+69.4) y resto molécula (−75.9), y así se declara en la nota de mapeo para que cuadre contra L8. La lámina usa los bloques del workbook.
- SUPERSEDED: las dos opciones conceptuales (A: puente de 5 conceptos con siluetas; B: mezcla de contratos), la nota "[decisión pendiente de Rafael…]", la advertencia roja de churn (628 nuevas / 836 perdidas, ±32%) y la referencia 2-vías (−671.6 / +756.1) — la decisión se tomó por VALOR y el puente fino por moléculas se descartó (ver Contenido diferido).
- Col 3: VP ~0 y PIN n/d **declarados**; NC ~0 a −1.1 y Dev −2.6 a −3.7: **en mano** (Gross2Net; SUPERSEDE el placeholder "[por llegar: DS]"). Validación por modelo (886/735/545/53 = 2,219.4) **en mano**, cuadra exacto con el sell-in (verificado en el EXTRACT del deck Servicios).
- Altas de licitación: REGLA DE TAXONOMÍA — son biosimilares ganando licitación y NUNCA se rotulan "Lanzamientos" (Lanzamientos = 0 por diseño, los 13 autoritativos dan 0 en el canal).

## Notas para el dibujante
- El ÚNICO gold de la lámina es el total "$2,219.4M" de la validación por modelo (col 3), porque es el ancla de credibilidad: cuadra exacto con el sell-in. Nada más en gold.
- SIN ROJO DE ADVERTENCIA en esta lámina: la advertencia de churn desapareció con la decisión por valor. El único rojo es el semáforo cuantitativo de las barras negativas (Resto molécula −75.9; Volumen −8.6 y Mix −18.1 del panel).
- Proporciones relativas del waterfall: Resto molécula −75.9 es la barra flotante más grande (hacia abajo); Diálisis +69.4 casi igual hacia arriba; Servicios +54.3 mediana; VARIOS +36.7 chica-mediana. En el panel DP: Precio +96.2 domina; Mix −18.1 chica; Volumen −8.6 mínima.
- El panel de diálisis peritoneal es un mini-puente SEPARADO del waterfall principal (universo piezas/bolsa del pool DP): no conectarlo con flechas ni fundirlo con el puente por valor; su total +$69.4M coincide con la barra "Diálisis peritoneal" y eso se lee por la anotación, no por un conector.
- La línea de mapeo a la matriz consolidada ("sin unidad −$6.5M") es obligatoria: es lo que hace cuadrar esta lámina contra el puente total de L8.
- Los corchetes "[vacío declarado, no se inventa]" se dibujan literales en gris `#8A95A8`, sin ámbar ni iconos. Todos los corchetes con responsable son PLACEHOLDER INTERNO — kill antes del 27.
- Signo menos tipográfico "−"; signo "+" explícito; no usar el carácter de flecha (el puente se lee "1S25 a 1S26").
- NO mezclar universos: col 1 es n/a, col 2 es sell-in por valor (+ panel DP por bolsa), la validación de col 3 es venta real YTD por modelo. El caveat de Zona C es obligatorio.
- Tabular figures en toda cifra. Sin líneas verticales. Sin border-left. Sin caja de insight ni rótulos de bloque. Sin verde.

### Contenido diferido a anexo
- A ANEXO: la fragilidad del puente fino por moléculas que motivó la decisión: churn de 628 claves nuevas y 836 perdidas = ±32% sobre la base; por eso el puente del segmento se lee por VALOR y no por los 5 conceptos P/V/M.
- A ANEXO: referencia 2-vías del segmento (volumen −$671.6M · precio y mezcla +$756.1M = +$84.5M) y el diagnóstico de mix con unidades de biológicos dudosas (cobertura 18%): no se imprimen sin revisión.
- A ANEXO: desglose de Canastas VARIOS (ONCOLÓGICOS +53.0 / ANTIMICROBIANOS −7.7 / NPT −3.6 / otros −5.0 = +36.7) y de Resto molécula (continuas −97.3 / altas +26.9 / bajas −5.5 = −75.9), por si el Consejo pide la apertura.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; TODAS las cifras en figuras tabulares; acentos en español.

ESTRUCTURA EN BANDAS: banda de título arriba (~15%); cuerpo al centro (~66%) dividido en TRES columnas de anchos 15% / 50% / 35% de izquierda a derecha; una banda de caveat de dos renglones (~9%); y un pie delgado abajo (~10%).

BANDA DE TÍTULO (ancho completo): título grande navy oscuro #0F2845, sans-serif ligera, sin punto final, dos líneas: "Servicios crece +$84.5M: hemodiálisis pone el 73% y la diálisis sube 15% el precio por bolsa con volumen plano". Debajo, en gris azulado #44546A pequeño e itálica: "Sell-in Servicios de $2,134.9M a $2,219.4M (+$84.5M, 102.1% de meta); puente 100% por valor (45.6% del bruto sin unidad), idéntico en los tres niveles de conciliación". Línea horizontal fina gris #E5E9EE de margen a margen.

COLUMNA IZQUIERDA (15%) — arriba, texto plano navy #0F2845 negrita, pequeño: "Mercado vs PiSA". Debajo, un rectángulo tenue de fondo gris muy claro #FAFBFC con contorno fino gris #E5E9EE (sin barra lateral de color) que encierra, centrado, el texto "n/a" en gris #5A6679 y debajo, más pequeño en gris #8A95A8: "modelos propios sin mercado auditado comparable (se declara)". Esta columna NO lleva gráfica de barras (es una declaración).

COLUMNA CENTRAL (50%) — arriba, texto plano navy #0F2845 negrita: "Puente por valor, cuatro bloques". Debajo, en gris #5A6679 muy pequeño: "Sell-in Gob Servicios · workbook Downtrading GobServicios FINAL 16-jul · 100% por valor". Debajo, DOS bloques apilados:
BLOQUE SUPERIOR (~60% de la columna): una gráfica de cascada (waterfall) con conectores punteados finos gris #C5CDD9, eje Y en millones desde 0, etiqueta de valor con signo sobre cada barra. De izquierda a derecha:
1. Barra ancla "1S25 · $2,134.9M" — sólida navy oscuro #0F2845, alta.
2. "Servicios (serie 9)" = "+54.3" — positiva, azul #0F4C81, mediana; junto a ella, en gris #5A6679 pequeño: "hemodiálisis, material 9000915: +$61.5M = 73% de la Δ del segmento".
3. "Canastas VARIOS" = "+36.7" — positiva, azul #0F4C81, chica-mediana.
4. "Diálisis peritoneal" = "+69.4" — positiva, azul #0F4C81, grande; junto a ella, en gris #5A6679 pequeño: "ver panel P/V/M abajo".
5. "Resto molécula" = "−75.9" — negativa, roja #C00000, la barra flotante más grande hacia abajo; junto a ella, en gris #5A6679 pequeño: "Pembrolizumab −$60.4M, fin de contrato".
6. Barra ancla "1S26 · $2,219.4M (102.1% de meta)" — sólida navy oscuro #0F2845, alta.
Bajo la cascada, una línea en gris #3D4A5F: "Lanzamientos = $0 por diseño: las altas de licitación (+$26.9M; Ocrelizumab +$18.9M) son biosimilares ganando licitación y viven dentro de resto molécula, nunca en la línea Lanzamientos."
BLOQUE INFERIOR (~30% de la columna), rotulado en gris #5A6679 pequeño "Diálisis peritoneal: P/V/M por bolsa": un mini-puente horizontal de tres barras chicas con etiqueta: "Precio" = "+96.2" en azul #0F4C81 (la dominante), "Volumen" = "−8.6" en rojo #C00000 mínima (con nota chica "bolsas −1.3%"), "Mix de formato" = "−18.1" en rojo #C00000 chica (con nota chica "bolsa 2L"), cerrando en "= +$69.4M". Debajo, en gris #3D4A5F pequeño: "Precio por bolsa +15% con volumen plano: la diálisis es historia de precio, no de piezas." Este panel NO se conecta con flechas al waterfall de arriba.
Al pie de la columna, en gris #8A95A8 pequeño: "Δ +$84.5M idéntica en los tres niveles (sin reclasificaciones). En la matriz consolidada del total (L8), diálisis (+$69.4M) y resto molécula (−$75.9M) viajan neteados como 'sin unidad' −$6.5M."

COLUMNA DERECHA (35%) — arriba, texto plano navy #0F2845 negrita: "Palancas y validación". Primer bloque, tres renglones en gris #3D4A5F:
1. "Venta perdida: ~0 (no es palanca de este segmento)"
2. "PIN no solicitado: n/d [vacío declarado, no se inventa]"
3. "NC comerciales y sanciones: de ~0 a −$1.1M; devoluciones: de −$2.6M a −$3.7M, inmateriales (Gross2Net)"
Una línea fina gris #E5E9EE separa. Segundo bloque, validación por modelo (venta real YTD), cuatro renglones en gris #3D4A5F y un total:
"Mezclas: $886M (−4%)"
"Diálisis: $735M (+10%)"
"Hemodiálisis: $545M (+13%)"
"Anestesia: $53M (−13%)"
Total en DORADO #C5A55A negrita: "Total: $2,219.4M = sell-in Servicios, cuadra exacto" (este es el ÚNICO elemento dorado de toda la lámina). El corchete "[vacío declarado, no se inventa]" se dibuja literal, en gris, sin color de alerta.

BANDA DE CAVEAT (ancho completo, dos renglones, gris #8A95A8 pequeño): "Servicios no tiene mercado auditado comparable: la col 1 se declara n/a. El puente es 100% por valor porque 45.6% del bruto no trae molécula ni unidad; el único pool con P/V/M real por pieza es la diálisis peritoneal (panel). Las cuatro líneas por modelo (venta real YTD) suman exacto $2,219.4M, el mismo sell-in del segmento."

PIE (ancho completo): línea fina gris #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: workbook Downtrading GobServicios FINAL 16-jul sobre Sell-In cierre jun-26, Servicios 1S26 vs 1S25 (puente 100% por valor; anexo diálisis P/V/M por bolsa); líneas por modelo: venta real YTD (deck Servicios); NC y devoluciones: Gross2Net Finanzas." A la derecha: "PiSA Confidencial | 28".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde en cualquier barra o etiqueta; texto en rojo de advertencia (el rojo vive SOLO en las barras negativas de las cascadas); más de un elemento en dorado (solo el total "$2,219.4M"); rotular nada como "Opción A" u "Opción B" (la lectura ya está resuelta); rellenar cualquier corchete. El signo menos es "−" tipográfico y el "+" explícito; español con acentos; título sin punto final.
```


---

# Lámina 29 · Nefrología empuja el 102.1%; mezclas onco y anestesia marcan dónde nos faltó
- **Momento:** M6 · Servicios: entorno, 1S, 2S (13.4% de la venta)
- **Encabezado:** Nefrología empuja el 102.1%; mezclas onco y anestesia marcan dónde nos faltó
- **So-what subtitle:** Radiografía del 1S de Servicios: cinco aciertos, cuatro faltantes
- **Layout:** banda de título 13% + cuerpo 82% (dos columnas iguales 50/50 con gutter 0.3 in; zebra ALINEADA: la alternancia arranca igual en ambas y las alturas de fila se emparejan renglón a renglón) + footer 5%. Geometría: 13.333 × 7.5 in; márgenes 0.5 in; área útil 12.333 × 6.5 in. Título y 0.5–1.35; cuerpo y 1.5–6.6; footer y 6.7–7.0. Espejo exacto del layout de la L24 (misma familia visual "bien/faltó").

## Zona por zona

**Zona A — Banda de título (12.333 × 0.85 in).**
Título Calibri Light 32 pt `#0F2845`; so-what 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE`.

**Zona B — Tabla doble "bien / faltó" (dos tablas independientes lado a lado, 6.0 in de ancho cada una, gutter 0.3 in).**

*Columna izquierda — header:* fondo `#0F2845`, texto blanco Calibri bold 13 pt: **"Qué hicimos bien en el 1S"**. Renglones alternos blanco / `#F0F3F7`, Calibri Light 11.5 pt `#3D4A5F`, border inferior 1 px `#E5E9EE`, sin líneas verticales. Contenido final:
1. 102.1% de cumplimiento y +4.0% vs 1S25: el único segmento arriba de meta
2. Hemodiálisis +13% con precio y sesiones; blindada por infraestructura y costo
3. Diálisis +10% (disciplina de precio); nutrición: somos únicos
4. Mezclas: mejor margen con menos centros (bruto 63%, operativo 22% en 2025)
5. EBITDA del segmento 14.5%, +5.8pp vs 1S25: el margen que más expande [split Gross2Net; bendición Finanzas pendiente: VJ]

*Columna derecha — header:* mismo formato: **"Qué nos faltó en el 1S"**. Contenido final:
1. Mezclas −4% YTD: salidas de capacidad y −$50M en hospitales privados
2. Onco: la competencia seria ya está adentro (COI, centros de infusión) y el flujo migra
3. Anestesia −13% YTD
4. Presión de descuentos en diálisis peritoneal

**Zona C — Footer (12.333 × 0.3 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 29" derecha.

## Mensaje que manda la lámina
El único segmento arriba de meta también tiene faltantes concretos y se dicen completos: mezclas onco pierde flujo frente a la competencia que ya está adentro, anestesia cae −13% y la diálisis peritoneal recibe presión de descuentos; nefrología es lo que sostiene el 102.1%.

## Fuente (pie de lámina)
Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Servicios; márgenes de mezclas: histórico del canal Servicios, cierre 2025; EBITDA del segmento: Estado de Resultados v18 + split del bloque Gobierno por Gross2Net, ene-jun-26.

## Estado del dato
- Columna "bien": **en mano** (storyline v6; márgenes 63/22 verificados contra deck del canal, L10). El bullet 4 lleva riesgo de redacción (ver notas).
- Bien-5 (EBITDA 14.5%, +5.8pp): **en mano, NUEVO 16-jul** — split Gross2Net del bloque Gobierno, cuadra con v18 al peso; bendición Finanzas pendiente [VJ]. Deroga la instrucción previa de "no citar EBITDA del segmento": ya HAY split; se cita con su nota de fuente. El pleito de reclasificaciones con Finanzas NO se menciona.
- Columna "faltó": **en mano** (storyline v6; −4%, −$50M, −13% verificados contra deck del canal L9/L30).

## Notas para el dibujante
- Espejo visual exacto de la L24 (Hospitales bien/faltó): mismos anchos, mismos headers, mismo formato de renglones. La familia "bien/faltó" debe leerse como serie a lo largo del deck.
- ZEBRA Y ALTURA (16-jul): la alternancia blanco/`#F0F3F7` arranca igual en ambas columnas y las alturas de fila se emparejan renglón a renglón (con 5 vs 4 renglones, los primeros 4 quedan alineados y el 5o de "bien" cierra solo); la retícula debe verse limpia, no dispareja.
- Las dos columnas pesan igual: sin verde en "bien" ni rojo en "faltó"; deltas en el gris del texto, sin semáforo en prosa. Es radiografía.
- SIN gold en esta lámina. Negritas: máximo 3-4 palabras (sugerido: "102.1%" en bien-1 y "−4% YTD" en faltó-1).
- Los márgenes de mezclas (bruto 63%, operativo 22%) son del histórico del canal, cierre 2025 — universo P&L del canal, NO Finanzas: viven como texto en un bullet, jamás en gráfica junto a sell-in, y el pie los declara. El EBITDA del segmento (bien-5) es de OTRO universo (v18 + split Gross2Net): ambos conviven como texto, nunca en una misma gráfica. El pleito de reclasificaciones NO se menciona. El corchete [VJ] es [PLACEHOLDER INTERNO - kill antes del 27].
- Riesgo de revire en bien-4 (validar redacción con Rafael antes del 22): la serie del canal da Mg Op 2024 = 27% > 2025 = 22%; el récord 2025 es el margen BRUTO (63%). "Mejor margen operativo" tal cual es atacable — la spec ya lo suaviza a "mejor margen ... (bruto 63%, operativo 22%)"; si Rafael prefiere el texto literal del v6, restaurarlo consciente del revire.
- Tensión de tono declarada: el v6 escribe "nutrición sin competencia: somos únicos" y la regla transversal prohíbe "no hay competencia". La spec imprime "nutrición: somos únicos" (misma afirmación, sin la frase prohibida). Si Rafael quiere el literal del v6, es su decisión.
- Trampa de atribución en faltó-1: el deck del canal atribuye los −$50M a "salidas derivadas de capacidad" (sin decir "hospitales privados") y su propia gráfica marca −$39M (−4%) vs el texto −$50M. Se imprime el v6 tal cual (manda el storyline); conciliación −39/−50 con DS antes del 22.
- Tabular figures en toda cifra; sin caja de insight; sin rótulos de bloque; sin emojis; sin border-left.

## Instrucciones ChatGPT Images 2

```
Genera una diapositiva corporativa en formato horizontal 16:9 sobre fondo blanco puro, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera (tipo Calibri Light), negritas solo donde se indica, números alineados a la derecha. Márgenes amplios y homogéneos.

ESTRUCTURA VERTICAL: banda de título arriba (~13%), cuerpo al centro con DOS columnas iguales lado a lado 50/50 (~82%), y un pie delgado abajo (~5%). Mismo layout espejo que la lámina de la familia "bien/faltó".

BANDA DE TÍTULO (arriba, ancho completo): título en navy oscuro #0F2845, sans-serif ligera, grande: "Nefrología empuja el 102.1%; mezclas onco y anestesia marcan dónde nos faltó". Debajo, en gris azulado #44546A pequeño e itálica: "Radiografía del 1S de Servicios: cinco aciertos, cuatro faltantes". Línea horizontal fina gris claro #E5E9EE de margen a margen.

CUERPO: dos tablas independientes del mismo ancho, una a la izquierda y otra a la derecha, con un espacio entre ellas. Ambas pesan visualmente IGUAL (mismo ancho, mismo formato, mismo gris de texto). La alternancia de fondos ARRANCA igual en ambas (zebra alineada) y las alturas de fila se emparejan renglón a renglón. No usar verde en la izquierda ni rojo en la derecha; todo el texto de los renglones en gris #3D4A5F. Sin líneas verticales. Sin bordes laterales de color.

COLUMNA IZQUIERDA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué hicimos bien en el 1S". Debajo, 5 renglones con fondo alternado blanco / gris muy claro #F0F3F7, cada renglón con línea inferior fina gris claro #E5E9EE. Texto de los renglones (verbatim):
1. "102.1% de cumplimiento y +4.0% vs 1S25: el único segmento arriba de meta"
2. "Hemodiálisis +13% con precio y sesiones; blindada por infraestructura y costo"
3. "Diálisis +10% (disciplina de precio); nutrición: somos únicos"
4. "Mezclas: mejor margen con menos centros (bruto 63%, operativo 22% en 2025)"
5. "EBITDA del segmento 14.5%, +5.8pp vs 1S25: el margen que más expande [split Gross2Net; bendición Finanzas pendiente: VJ]" (el corchete se dibuja literal, en gris)
Dentro de esta columna, solo "102.1%" del renglón 1 va en negrita.

COLUMNA DERECHA — encabezado con fondo navy oscuro #0F2845 y texto blanco en negrita, alineado a la izquierda: "Qué nos faltó en el 1S". Debajo, 4 renglones con el mismo formato alternado blanco / gris muy claro #F0F3F7. Texto de los renglones (verbatim):
1. "Mezclas −4% YTD: salidas de capacidad y −$50M en hospitales privados"
2. "Onco: la competencia seria ya está adentro (COI, centros de infusión) y el flujo migra"
3. "Anestesia −13% YTD"
4. "Presión de descuentos en diálisis peritoneal"
Dentro de esta columna, solo "−4% YTD" del renglón 1 va en negrita.

PIE (abajo, ancho completo): línea fina gris claro #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: Sell-In cierre jun-26, ene-jun 2026 vs ene-jun 2025, segmento Servicios; márgenes de mezclas: histórico del canal Servicios, cierre 2025; EBITDA del segmento: Estado de Resultados v18 + split del bloque Gobierno por Gross2Net, ene-jun-26." A la derecha: "PiSA Confidencial | 29".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color; verde celebratorio en las cifras propias; cualquier semáforo de color en los renglones. Los signos menos en los deltas ("−4% YTD", "−$50M", "−13% YTD") van en el mismo gris del texto, no en rojo. Ningún elemento en gold en esta lámina. Los corchetes se dibujan literales en gris (placeholders internos del borrador).
```


---

# Lamina 30 · El plan 2S de Servicios tiene dos caras: achicar por decisión de riesgo y crecer donde invertimos
- **Momento:** M6 · Servicios: entorno, 1S, 2S (13.4% de la venta)
- **Encabezado:** El plan 2S de Servicios tiene dos caras: achicar por
  decisión de riesgo y crecer donde invertimos
- **So-what subtitle:** Mantener el 102.1% del 1S es una de las dos patas del compromiso del 2S
- **Layout:** Banda de título 16% (título 32 pt + subtitle 14 pt) · cuerpo 66% en 2 columnas 50/50 con gutter 0.15in (izquierda "Lo que achicamos por decisión" / derecha "Lo que crecemos e invertimos") · banda inferior 10% (nota EBITDA a todo lo ancho) · footer 8% (fuente + confidencial + página). Slide 16:9 (13.333 × 7.5 in), márgenes 0.5 in en los cuatro lados.

## Zona por zona

### Zona A — Título y subtitle (banda superior, 16%)
- Título: Calibri Light 32 pt, color `--color-primary-900` #0F2845, sentence case, sin punto final. Texto exacto: "El plan 2S de Servicios tiene dos caras: achicar por decisión de riesgo y crecer donde invertimos". Palabras en Calibri bold (énfasis puntual, máx 3-4 palabras): "dos caras".
- Subtitle: Calibri Light 14 pt italic, color #44546A. Texto exacto: "Mantener el 102.1% del 1S es una de las dos patas del compromiso del 2S".
- Separador opcional bajo el subtitle: línea 0.5 pt `--color-gray-200` #E5E9EE.

### Zona B — Columna izquierda (50%): "Lo que achicamos por decisión"
- **Header de columna:** bloque con top border 2 pt `--color-primary-700` #0F4C81 (nunca border-left), fondo `--color-gray-050` #FAFBFC, texto "Lo que achicamos por decisión" en Calibri bold 14 pt #0F2845.
- **Mini-gráfica de barras** (2 barras verticales, ancho ~40% de la columna):
  - Serie: Mezclas de gobierno, venta anual $M. Barra 1 = "~1,800" (base) [candidato]; barra 2 = "~1,600" (2026e, por decisión) [candidato].
  - Ambas barras en `--color-primary-700` #0F4C81 (NO rojo: la reducción es decisión propia, no alarma; el semáforo no aplica a decisiones deliberadas). Espacio entre barras ≥ 50% del ancho de barra. Eje Y arranca en cero, sin gridlines, sin leyenda.
  - Data labels directos Calibri Light 10 pt #1A2332: "~$1,800M" y "~$1,600M". Anotación sobre la flecha/delta en Calibri Light 10 pt `--color-gray-700` #3D4A5F: "−$200M por decisión de riesgo [candidato]".
  - Etiqueta de eje X: "Mezclas de gobierno, venta anual ($M) [año base por confirmar]".
- **Bullets** (Calibri Light 11 pt #3D4A5F, viñeta simple, máx 3):
  1. "SAFE: salida en curso; el negocio se hace más chico por decisión propia"
  2. "NPT (nutrición parenteral): salida acelerada, ya en ejecución [candidato]"
  3. "Mezclas de gobierno: de ~$1,800M hacia ~$1,600M anuales por decisión de riesgo [candidato]"

### Zona C — Columna derecha (50%): "Lo que crecemos e invertimos"
- **Header de columna:** mismo estilo que Zona B (top border 2 pt #0F4C81, fondo #FAFBFC), texto "Lo que crecemos e invertimos" en Calibri bold 14 pt #0F2845.
- **Mini-gráfica de barras** (2 barras verticales, mismo tamaño y estilo que la de Zona B para simetría):
  - Serie: Pacientes de hemodiálisis (SANEFRO). Barra 1 = "4,110" (hoy); barra 2 = "~5,200" (con ampliaciones propuestas).
  - Barra 1 en `--color-primary-900` #0F2845 sólida; barra 2 en #0F2845 con relleno al 40% de opacidad o contorno punteado 1 pt (indica propuesta pendiente de aprobación, no hecho). Data labels 10 pt: "4,110" y "~5,200".
  - Nota bajo la gráfica, Calibri Light 9 pt `--color-gray-500` #5A6679: "Ampliaciones propuestas; inversión pendiente de validación de Finanzas [César/DS]".
  - Etiqueta de eje X: "Pacientes de hemodiálisis (pacientes/año)".
- **Bullets** (Calibri Light 11 pt #3D4A5F, máx 4):
  1. "Hemodiálisis +13% YTD (6% sesiones + 7% precio); SANEFRO: 12 clínicas en 6 estados, ~$1,005M anuales"
  2. "Diálisis +10% YTD con disciplina de precio: descuentos solo con contraparte"
  3. "Anestesia: inversión propuesta [monto y alcance: DS/César]"
  4. "Renovación tecnológica de diálisis adelantada: que no se repita el caso de bombas de infusión"

### Zona D — Banda inferior (10%): EBITDA declarado (ACTUALIZADA 16-jul: ya hay dato)
- Bloque a todo lo ancho, fondo `--color-gray-100` #F0F3F7, sin etiqueta/rótulo, texto en Calibri Light 11 pt #3D4A5F, una sola línea (puede correr a 2 renglones visuales):
  - "EBITDA de Servicios 1S26: 14.5%. Por unidad: diálisis peritoneal 17.4% · SANEFRO 19.9% · SAFE 8.4% · SIA 23.9% (EBITDA UN; bendición Finanzas pendiente [VJ])".
- El placeholder anterior (combinado Gobierno+Servicios $804.8M / 12.9%) queda SUPERSEDED: ya existe el split; solo se usaría como fallback si Finanzas tumba el split antes del 27.

### Zona E — Footer
- Línea 0.5 pt #E5E9EE. Izquierda: fuente (ver abajo) Calibri Light 9 pt italic `--color-gray-400` #8A95A8. Derecha: "PiSA Confidencial  |  30" mismo estilo.

## Mensaje que manda la lamina
Servicios no pide permiso ni se disculpa: las salidas (SAFE, NPT, mezclas de gobierno) son decisión de riesgo tomada por nosotros, y el crecimiento (hemodiálisis, diálisis, anestesia) tiene inversión propuesta detrás. Mantener el 102.1% es una de las dos patas del compromiso del 2S.

## Fuente (pie de lamina)
"Fuente: Sell-In cierre junio 2026 (líneas de Servicios YTD, 1S26 vs 1S25); deck canal Servicios corte 02-jul-2026 (SANEFRO, pacientes); plan 2S en revisión interna 15-jul-2026 [cifras candidato]. Universo: sell-in / venta real por línea de servicio."

## Estado del dato
- Zona A/C bullets 1-2 (hemodiálisis +13%, sesiones/precio, SANEFRO 12 clínicas / ~$1,005M / 4,110 pacientes; diálisis +10%): **en mano** (deck canal Servicios + sell-in, cuadran exacto con $2,219.4M).
- Zona B mini-gráfica y bullet 3 (mezclas gobierno de ~$1,800 a ~$1,600): **[candidato]** — transcript 15-jul; año base del $1,800M sin especificar. No se imprime sin volverse canónico [DS/Rafael].
- Zona B bullet 2 (NPT salida acelerada): **[candidato]** — instrucción de presidencia vía transcript 15-jul.
- Zona C barra "~5,200" y bullet 3 (anestesia): **por completar [César/DS]** — inversiones sin bendición de Finanzas; se dibujan como propuesta (contorno punteado), no como hecho.
- Zona D (EBITDA): **en mano, ACTUALIZADO 16-jul** — Servicios 14.5% (split Gross2Net del bloque Gobierno, cuadra con v18 al peso) y sub-líneas DP 17.4% / SANEFRO 19.9% / SAFE 8.4% / SIA 23.9% del P&L split por UN. Nota obligada impresa: "EBITDA UN; bendición Finanzas pendiente [VJ]". Si VJ no bendice antes del 22, la banda regresa al fallback del combinado.

## Notas para el dibujante
- **El pleito con Finanzas por las reclasificaciones (diálisis al 0%, SAFE) NO se menciona en ninguna parte de la lámina.** La Zona D lleva el dato del split con su nota "EBITDA UN; bendición Finanzas pendiente [VJ]"; nada de "en disputa", "en revisión con Finanzas" ni equivalentes (una bendición pendiente NO es un pleito: no insinuarlo).
- Todo corchete con responsable ([candidato], [César/DS], [VJ], [DS/Rafael]) es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris y se elimina o resuelve antes de la sesión.
- Cero rótulos tipo "INSIGHT", "SO WHAT" o "RIESGO" en los bloques; los headers de columna son los únicos rótulos permitidos y son los indicados arriba.
- Sin caja de insight (deck de Consejo): la implicación vive en título y subtitle.
- Las barras de mezclas de gobierno NO van en rojo aunque el delta sea negativo: es reducción deliberada; el delta se anota en gris #3D4A5F con la leyenda "por decisión de riesgo". No usar verde tampoco.
- Sin gold en esta lámina (tono sobrio; nada que destacar por encima del balance de las dos caras).
- Las marcas [candidato] se imprimen en el borrador de trabajo tal cual (9 pt, gris); en la versión final o se resuelven o el dato sale. No quitarlas silenciosamente.
- Tabular figures en todos los números (Format, Font, OpenType, Tabular figures).
- No decir "no hay competencia" en ningún texto; el lenguaje es "decisión de riesgo", "disciplina de precio", "ventaja propia".
- No usar gradientes, sombras infladas, iconos de color ni border-left. Números a la derecha si hubiera tabla (aquí no hay).

## Instrucciones ChatGPT Images 2

```
Diapositiva corporativa 16:9 sobre fondo blanco, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera; negritas solo donde se indica; números alineados a la derecha. Todo el texto en español con acentos, impreso verbatim tal como aparece entre comillas.

LAYOUT vertical en cuatro franjas: banda de título arriba (16% de la altura), cuerpo central en dos columnas iguales 50/50 (66% de la altura), banda inferior gris a todo lo ancho (10%), y pie de página (8%). Márgenes amplios en los cuatro lados.

BANDA DE TÍTULO (arriba): título en navy oscuro #0F2845, sans-serif ligera grande, dos líneas, sin punto final: "El plan 2S de Servicios tiene dos caras: achicar por decisión de riesgo y crecer donde invertimos". Solo las palabras "dos caras" van en negrita. Debajo, subtítulo en itálica gris azulado #44546A, más pequeño: "Mantener el 102.1% del 1S es una de las dos patas del compromiso del 2S". Una línea divisoria gris muy clara #E5E9EE bajo el subtítulo.

COLUMNA IZQUIERDA (mitad izquierda). Arriba un encabezado de columna: caja con fondo gris muy claro #FAFBFC y una línea superior gruesa de 2 pt en azul #0F4C81 (línea SUPERIOR, nunca lateral), con el texto en negrita azul-navy #0F2845: "Lo que achicamos por decisión". Debajo, una mini-gráfica de dos barras verticales, ambas del mismo color azul #0F4C81 (NO rojo): la barra izquierda etiquetada arriba "~$1,800M" y la barra derecha ligeramente más baja etiquetada "~$1,600M" (la segunda barra es aproximadamente 11% más corta que la primera). Eje Y arranca en cero, sin líneas de cuadrícula, sin leyenda. Entre las dos barras una anotación en gris #3D4A5F: "−$200M por decisión de riesgo [candidato]". Bajo las barras, etiqueta de eje X en gris pequeño: "Mezclas de gobierno, venta anual ($M) [año base por confirmar]". Debajo, tres viñetas simples en gris #3D4A5F: "SAFE: salida en curso; el negocio se hace más chico por decisión propia" · "NPT (nutrición parenteral): salida acelerada, ya en ejecución [candidato]" · "Mezclas de gobierno: de ~$1,800M hacia ~$1,600M anuales por decisión de riesgo [candidato]".

COLUMNA DERECHA (mitad derecha). Encabezado de columna del mismo estilo (fondo #FAFBFC, línea superior 2 pt #0F4C81), texto en negrita #0F2845: "Lo que crecemos e invertimos". Debajo, mini-gráfica de dos barras verticales del mismo tamaño que la izquierda: la barra izquierda sólida en navy oscuro #0F2845 etiquetada "4,110"; la barra derecha, más alta (aproximadamente 27% más alta que la primera), dibujada con contorno punteado 1 pt o relleno tenue al 40% de opacidad en navy #0F2845 (indica propuesta pendiente), etiquetada "~5,200". Eje Y desde cero, sin cuadrícula. Bajo la gráfica, nota en gris pequeño #5A6679: "Ampliaciones propuestas; inversión pendiente de validación de Finanzas [César/DS]". Etiqueta de eje X: "Pacientes de hemodiálisis (pacientes/año)". Debajo, cuatro viñetas simples en gris #3D4A5F: "Hemodiálisis +13% YTD (6% sesiones + 7% precio); SANEFRO: 12 clínicas en 6 estados, ~$1,005M anuales" · "Diálisis +10% YTD con disciplina de precio: descuentos solo con contraparte" · "Anestesia: inversión propuesta [monto y alcance: DS/César]" · "Renovación tecnológica de diálisis adelantada: que no se repita el caso de bombas de infusión".

BANDA INFERIOR (franja gris a todo lo ancho, fondo #F0F3F7, sin ningún rótulo ni etiqueta): una sola línea de texto gris #3D4A5F (puede correr a dos renglones), dibujada literalmente incluyendo el corchete: "EBITDA de Servicios 1S26: 14.5%. Por unidad: diálisis peritoneal 17.4% · SANEFRO 19.9% · SAFE 8.4% · SIA 23.9% (EBITDA UN; bendición Finanzas pendiente [VJ])".

PIE DE PÁGINA: línea fina gris #E5E9EE. A la izquierda, en gris claro itálica pequeña #8A95A8: "Fuente: Sell-In cierre junio 2026 (líneas de Servicios YTD, 1S26 vs 1S25); deck canal Servicios corte 02-jul-2026 (SANEFRO, pacientes); plan 2S en revisión interna 15-jul-2026 [cifras candidato]. Universo: sell-in / venta real por línea de servicio." A la derecha, mismo estilo: "PiSA Confidencial  |  30".

Colores exactos: navy oscuro #0F2845, azul #0F4C81, grises #3D4A5F / #5A6679 / #8A95A8, gris muy claro de cajas #FAFBFC, gris de banda inferior #F0F3F7, línea divisoria #E5E9EE. NO usar gold en esta lámina. NO usar rojo ni verde en las barras aunque un delta sea negativo. Las marcas entre corchetes como [candidato] se dibujan tal cual, en gris neutro. PROHIBIDO: el carácter de flecha en cualquier texto, emojis, rótulos de caja tipo "INSIGHT" o "SO WHAT" o "RIESGO", border-left (bordes laterales), verde celebratorio en cifras propias.
```


---

# Lámina 31 · El 2S llega a [96] con palancas propias, no con mercado; la cascada dimensiona el hueco y su reparto por segmento
- **Momento:** M7 · La ruta consolidada al número (2 láminas)
- **Encabezado:** El 2S llega a [96] con palancas propias, no con mercado; la cascada dimensiona el hueco y su reparto por segmento
- **So-what subtitle:** Cascada year-to-go de repetir la venta del 1S ($16,518.5M) a [96] anual ($18,115.1M jul-dic, 98.5% del semestre); la forma está comprometida, los montos por escalón en construcción [RC]
- **Layout:** banda de título 15% + cuerpo 62% (una cascada de ancho completo, de repetir la venta del 1S a [96]) + banda de leyenda 13% + footer 10%. Geometría 13.333 × 7.5 in, márgenes 0.5 in, área útil 12.333 in. Título y 0.5–1.55 in; cascada y 1.7–6.05 in; leyenda y 6.1–6.75 in; footer y 6.85–7.1 in.

## Zona por zona

**Zona A — Banda de título (12.333 × 1.0 in).**
Título asertivo Calibri Light 28 pt `#0F2845` (2 líneas), sin punto final; so-what subtitle Calibri Light 14 pt itálica `#44546A`; separador 0.5 pt `#E5E9EE` de margen a margen.

**Zona B — Cascada year-to-go (ancho completo, ~4.35 in de alto).**
Waterfall horizontal de izquierda a derecha, $M, eje Y desde 0. Estructura: barra base (real) · 7 escalones placeholder · barra destino (derivado de [96]). Connectors punteados 0.5 pt `#C5CDD9`. Data labels Calibri Light 10 pt `#1A2332`.

- **Barra base (izquierda), navy `#0F2845`:** rótulo "Repetir la venta del 1S". Data label: **"$16,518.5M"** (dato duro: es el sell-in 1S-2026 cerrado; deja de ser placeholder).
- **ESCALA OBLIGATORIA:** el hueco completo (los 7 escalones juntos) mide ~10% de la altura de la barra base ($1,596.6M sobre $16,518.5M), NO 30%. La barra destino es apenas ~10% más alta que la base; los escalones son delgados sobre ese tramo.
- **7 escalones placeholder, siluetas gris `#E5E9EE`** (contorno 0.5 pt `#C5CDD9`, altura media uniforme dentro del tramo del hueco, SIN valor salvo donde se indica), cada uno rotulado bajo el eje X en Calibri Light 9.5 pt `#5A6679` y con "[monto: RC]" encima en `#8A95A8`. Orden de escalones (izquierda a derecha):
  1. "Servicio normalizado" — escalón VISIBLE (mejor fill rate, menos devoluciones).
  2. "NADAL neto jul-dic" — sobre esta silueta, en lugar de "[monto: RC]", va el ancla real en Calibri bold 12 pt `#C5A55A` (gold): "NADAL bruto full-year $2,337.1M · $1,402.2M a 60%". La porción jul-dic sigue "[monto jul-dic: RC]" en `#8A95A8`. ÚNICO elemento gold de la lámina.
  3. "2º incremento de precios (julio)" — "[monto: RC]".
  4. "Nuevos productos" — "[monto: RC]"; nota `#8A95A8`: "referencia 1S: lanzamientos +$94.4M total PiSA (Retail +$71.1M, L13)".
  5. "Disciplina comercial (NC y descuentos, defensa de mezcla)" — "[monto: RC]".
  6. "Plan invernal (orden 25-sep)" — "[monto: RC]".
  7. "Estacionalidad Q4" — "[monto: RC]".
- **Barra destino (derecha), navy `#0F2845` con contorno `#C5CDD9`:** rótulo "[96] anual". Data label en dos renglones: "[96] anual" (el "[96]" literal en gris `#8A95A8`, es placeholder) y "$18,115.1M jul-dic (98.5% de meta del semestre)" en `#1A2332`.
- Llave/corchete horizontal sobre el tramo de los 7 escalones (de la base al destino), rotulada Calibri Light 11 pt `#5A6679`: "hueco a cerrar: +$1,596.6M sobre repetir la venta del 1S". Junto a la llave, el chip literal en `#8A95A8`: "[definición del hueco pendiente de Rafael: repetir venta ($1,596.6M) o ritmo sobre plan (~$931M)]".

**Zona C — Banda de leyenda (12.333 × 0.65 in).**
Dos renglones, fondo `#F0F3F7` sin border-left, Calibri Light 11 pt `#1A2332`:
- Renglón 1: "Los aportes por escalón y por segmento deben sumar el hueco: en construcción [RC]. La forma del puente está comprometida; el único monto duro hoy es el NADAL."
- Renglón 2, Calibri Light 10 pt `#5A6679`: "El forecast de mercado vive en anexo, no aquí."

**Zona D — Footer (12.333 × 0.25 in).**
Línea 0.5 pt `#E5E9EE`; fuente Calibri Light 9 pt itálica `#8A95A8` izquierda; "PiSA Confidencial | 31" derecha.

## Mensaje que manda la lámina
El 2S no se llega con esperanza de mercado sino con palancas propias, ordenadas en una cascada cuya FORMA ya está comprometida (servicio normalizado visible, NADAL, segundo precio, nuevos productos, disciplina de NC, plan invernal, estacionalidad Q4). La base es un hecho, no una hipótesis: repetir la venta del 1S son $16,518.5M. El único monto duro entre los escalones es el NADAL; el tamaño del hueco (+$1,596.6M si la vara es repetir la venta) es aritmética visible, y su reparto por segmento está en construcción. La honestidad de la lámina es enseñar el "vamos a llegar" sin fingir montos que aún no existen.

## Fuente (pie de lámina)
Fuente: construcción del plan 2S (NADAL + palancas propias), no sell-in histórico; base = repetir la venta del 1S (Sell-In PiSA cierre jun-26, $16,518.5M); NADAL bruto full-year $2,337.1M / $1,402.2M a 60%; montos por escalón y por segmento en construcción [RC].

## Estado del dato
- **Forma de la cascada: comprometida** (hallazgo crítico convergente del consejo adversarial §2.1: la ruta 93.4% a 98.5% es EL número de la junta y no puede subir en blanco).
- **Base $16,518.5M (repetir la venta del 1S): en mano** — deja de ser "[monto: RC]": es el sell-in 1S-2026 cerrado. La definición del hueco sigue abierta y viaja como chip: repetir venta (+$1,596.6M) o ritmo sobre plan (~$931M) [Rafael].
- **NADAL full-year $2,337.1M / $1,402.2M a 60%: en mano** (plan NADAL, único monto duro entre los escalones, en gold).
- **Montos por escalón y aporte por segmento: [RC]** — impresos como corchete literal.
- **Destino [96] anual ($18,115.1M jul-dic, hueco +$1,596.6M): derivado de [96]**; el "[96]" se dibuja como placeholder literal. Aritmética: 16,518.5 + 1,596.6 = 18,115.1 exacto.
- **Andamiaje de negociación RETIRADO por orden del 16-jul:** fuera "Heriberto", "antes del 20/22" y "se recalcula al cerrar" — para la audiencia del 27 el número estará fijado. La nota de recálculo ya no se imprime.
- **$350M: SILENCIO por orden del 16-jul** — el disclaimer de exclusión ya no se imprime (antes decía "quedan FUERA de esta cascada"); tampoco se dibuja escalón de ahorros. La decisión de fondo (10-jul: fuera de la cascada) no cambia, solo deja de declararse en la lámina.
- **Nota del escalón 4 actualizada al canónico:** la referencia de lanzamientos 1S es +$94.4M total PiSA / +$71.1M Retail (Δ reclasificada, matriz 16-jul); supersede el "+$43.8M" de la vista bruta anterior.
- **Servicio normalizado: escalón VISIBLE.** La nota impresa de decisión provisional se retira del lienzo (era andamiaje interno); la trazabilidad vive aquí: decisión provisional del orquestador 16-jul (consejo §3.8: dimensionarlo como línea visible evita que huela a contrafactual), el storyline v6 lo dejaba implícito, Rafael puede revertir.

## Notas para el dibujante
- El ÚNICO gold de la lámina es el ancla NADAL "$2,337.1M · $1,402.2M a 60%" sobre el escalón 2: es el único monto duro entre placeholders. Nada más en gold. El "[96]" del destino NO va en gold (es placeholder: gris neutro, rule 5).
- ESCALA: el hueco completo mide ~10% de la altura de la barra base (1,596.6 / 16,518.5), no 30% como en el borrador anterior. Los 7 escalones son delgados y viven en la parte alta del dibujo; la base y el destino dominan la lámina. No exagerar el hueco: exagerarlo cuenta una historia falsa de tamaño.
- Los 7 escalones son SILUETAS grises `#E5E9EE` de altura media uniforme, SIN valor numérico (salvo el ancla NADAL en gold sobre el escalón 2): no darles altura-por-valor, la forma se compromete y el monto no existe. La base es barra navy sólida con dato duro ($16,518.5M); el destino navy con contorno y su "[96]" placeholder.
- El escalón 1 "Servicio normalizado" se dibuja VISIBLE, sin nota impresa de decisión provisional (esa trazabilidad vive en Estado del dato, no en el lienzo).
- Todos los "[monto: RC]", "[monto jul-dic: RC]", "[96]", "[RC]" y "[definición del hueco pendiente de Rafael: …]" se dibujan literales, en gris `#8A95A8`, sin ámbar/rojo ni iconos. Prohibido rellenarlos o estimarlos. Los corchetes con responsable son PLACEHOLDER INTERNO — kill antes del 27: viven en el storyboard de revisión, no en la versión del Consejo.
- NADA de "Heriberto", fechas de negociación ("antes del 20", "antes del 22") ni notas de recálculo en ningún texto de la lámina.
- NADA sobre los $350M de ahorros: ni escalón, ni disclaimer, ni mención (silencio ordenado el 16-jul).
- Universo declarado: construcción del plan 2S (NADAL + palancas), no sell-in histórico. No mezclar con las cascadas de segmento (L13/18/23/28), que son 1S25 vs 1S26 sell-in.
- Signo "+" explícito en el hueco; no usar el carácter de flecha (la cascada se lee "de repetir la venta del 1S a [96]").
- Tabular figures en toda cifra. Sin líneas verticales. Sin border-left. Sin caja de insight ni rótulos de bloque. Sin verde celebratorio.

## Instrucciones ChatGPT Images 2

```
Crea una diapositiva corporativa horizontal 16:9 sobre fondo blanco puro, estilo consulting flat: sin gradientes, sin sombras infladas, sin fotos, sin logos, sin emojis, sin iconos de color, sin círculos de semáforo. Tipografía sans-serif limpia y ligera (tipo Calibri Light); negritas solo donde se indica; TODAS las cifras en figuras tabulares; acentos en español.

ESTRUCTURA EN BANDAS: banda de título arriba (~15%); una cascada (waterfall) de ancho completo al centro (~62%); una banda de leyenda de dos renglones sobre fondo gris claro (~13%); y un pie delgado abajo (~10%).

BANDA DE TÍTULO (ancho completo): título grande navy oscuro #0F2845, sans-serif ligera, sin punto final, dos líneas: "El 2S llega a [96] con palancas propias, no con mercado; la cascada dimensiona el hueco y su reparto por segmento". El "[96]" se dibuja literal como placeholder. Debajo, en gris azulado #44546A pequeño e itálica: "Cascada year-to-go de repetir la venta del 1S ($16,518.5M) a [96] anual ($18,115.1M jul-dic, 98.5% del semestre); la forma está comprometida, los montos por escalón en construcción [RC]". Línea horizontal fina gris #E5E9EE de margen a margen.

CASCADA (ancho completo): un waterfall horizontal de izquierda a derecha, eje Y en millones desde 0, con conectores punteados finos gris #C5CDD9. ESCALA CRÍTICA: la barra destino es solo ~10% MÁS ALTA que la barra base (el hueco es $1,596.6M sobre una base de $16,518.5M); los siete escalones son delgados y viven en ese tramo alto de ~10%; NO dibujar un hueco de un tercio de la base. De izquierda a derecha:
- BARRA BASE sólida navy oscuro #0F2845, ALTA (domina el dibujo), rotulada abajo "Repetir la venta del 1S", con etiqueta de dato dura: "$16,518.5M".
- SIETE ESCALONES como SILUETAS PLACEHOLDER en gris muy claro #E5E9EE con contorno fino gris #C5CDD9, de altura media uniforme dentro del tramo del hueco y SIN número (salvo el escalón 2, ver abajo), cada uno rotulado debajo del eje en gris #5A6679 y con "[monto: RC]" encima en gris #8A95A8. Nombres en orden:
  1. "Servicio normalizado"
  2. "NADAL neto jul-dic" — sobre esta silueta, en DORADO #C5A55A negrita, el ancla real: "NADAL bruto full-year $2,337.1M · $1,402.2M a 60%" (este es el ÚNICO elemento dorado de toda la lámina); y aparte, en gris #8A95A8: "[monto jul-dic: RC]".
  3. "2º incremento de precios (julio)" — "[monto: RC]".
  4. "Nuevos productos" — "[monto: RC]", con nota gris #8A95A8: "referencia 1S: lanzamientos +$94.4M total PiSA (Retail +$71.1M, L13)".
  5. "Disciplina comercial (NC y descuentos, defensa de mezcla)" — "[monto: RC]".
  6. "Plan invernal (orden 25-sep)" — "[monto: RC]".
  7. "Estacionalidad Q4" — "[monto: RC]".
- BARRA DESTINO sólida navy oscuro #0F2845 con contorno gris #C5CDD9, apenas más alta que la base (~10%), rotulada abajo "[96] anual", con etiqueta en dos renglones: "[96] anual" (el "[96]" en gris #8A95A8, placeholder) y "$18,115.1M jul-dic (98.5% de meta del semestre)" en gris muy oscuro #1A2332.
Sobre el tramo de los siete escalones (de la base al destino), una llave/corchete horizontal con la leyenda en gris #5A6679: "hueco a cerrar: +$1,596.6M sobre repetir la venta del 1S". Junto a la llave, el chip literal en gris #8A95A8: "[definición del hueco pendiente de Rafael: repetir venta ($1,596.6M) o ritmo sobre plan (~$931M)]".

BANDA DE LEYENDA (ancho completo, fondo gris claro #F0F3F7, sin barra lateral de color), dos renglones:
Renglón 1 en gris muy oscuro #1A2332: "Los aportes por escalón y por segmento deben sumar el hueco: en construcción [RC]. La forma del puente está comprometida; el único monto duro hoy es el NADAL."
Renglón 2 en gris #5A6679 pequeño: "El forecast de mercado vive en anexo, no aquí."

PIE (ancho completo): línea fina gris #E5E9EE arriba. A la izquierda, itálica gris #8A95A8 pequeña: "Fuente: construcción del plan 2S (NADAL + palancas propias), no sell-in histórico; base = repetir la venta del 1S (Sell-In PiSA cierre jun-26, $16,518.5M); NADAL bruto full-year $2,337.1M / $1,402.2M a 60%; montos por escalón y por segmento en construcción [RC]." A la derecha: "PiSA Confidencial | 31".

PROHIBIDO: el carácter de flecha en cualquier texto; emojis; rótulos de caja tipo "INSIGHT" o "SO WHAT"; bordes laterales de color (border-left); verde celebratorio; más de un elemento en dorado (solo el ancla NADAL); poner el "[96]" en dorado (es placeholder, va en gris); dar altura-por-valor a los siete escalones placeholder o rellenar cualquier corchete; dibujar el hueco más grande que ~10% de la base; mencionar ahorros de $350M, la palabra "Heriberto", fechas de negociación o notas de recálculo. El signo "+" es explícito; español con acentos; título sin punto final.
```


---

# Lamina 32 · Tres riesgos del 2S, declarados hoy con métrica y fecha de lectura
- **Momento:** M7 · La ruta consolidada al número
- **Encabezado:** Tres riesgos del 2S, declarados hoy con métrica
  y fecha de lectura
- **So-what subtitle:** El drenaje del Q3 es secuencia planeada con el Q4 estacional detrás
- **Layout (RECORTE 16-jul):** Banda de título 16% · tablero de hipótesis (tabla 4 columnas, ahora la pieza central con aire) 48% · nota bajo tabla 4% · banda de mecanismo de seguimiento 14% · línea de leyenda de placeholders · footer 10%. Las 3 tarjetas de riesgo SALIERON (duplicaban la tabla); su dato duro se absorbió en la columna "Riesgo declarado" y el texto completo vive en "Contenido diferido a anexo". Slide 16:9 (13.333 × 7.5 in), márgenes 0.5 in.

## Zona por zona

### Zona A — Título y subtitle (16%)
- Título: Calibri Light 32 pt #0F2845 (`--color-primary-900`), sentence case, sin punto final: "Tres riesgos del 2S, declarados hoy con métrica y fecha de lectura". Énfasis Calibri bold en "declarados hoy".
- Subtitle: Calibri Light 14 pt italic #44546A: "El drenaje del Q3 es secuencia planeada con el Q4 estacional detrás".

### Zona B — Tablero de hipótesis del 2S (48%, tabla a todo lo ancho, con aire)
Tabla estándar del sistema: header fondo `--color-primary-700` #0F4C81 (alterno aceptado: #0F2845), texto blanco Calibri bold 11 pt; filas alternas blanco / `--color-primary-050` #E8F1F8; sin líneas verticales; texto a la izquierda (no hay columnas puramente numéricas); Calibri Light 11-11.5 pt #3D4A5F (sube medio punto: la tabla ganó el espacio de las tarjetas); tabular figures en toda celda con cifra. La columna "Riesgo declarado" absorbe el dato duro de las tarjetas retiradas.

| Riesgo declarado | Hipótesis del plan | Métrica de seguimiento | Lectura (propuesta) |
|---|---|---|---|
| Julio arranca hipotecado: compra adelantada de junio ~$104M [cerrar cifra: CC] y canal a 90-120 días de inventario contra 60 de estándar | El drenaje del Q3 es secuencia planeada para llegar sanos al Q4 estacional | DDI del top de clientes: de 120 a 70 días | Mensual; corte al cierre de sep-26 |
| Las últimas pólizas con IVA deducible vencen en Q4 (primas 2026 subiendo +6-10%, AMIS) | Las 7 palancas de Hospitales compensan calendario y pagador | Run-rate de palancas: $47M/mes contra gap de $57M/mes (medición formal desde julio) | Mensual, jul-dic |
| El gobierno sigue sin pagar: cartera $4,834M al 30-jun-26, +22% vs cierre 2025 | El 2S depende de surtir bien lo contratado y cobrar con disciplina, no de cobro rápido | Cartera junio-junio y meses de cartera (hoy FC 5.3 / Servicios 3.4) | Mensual |

- Nota bajo la tabla (4%), Calibri Light 9 pt `--color-gray-500` #5A6679, dos elementos:
  - "Fechas de la columna Lectura: propuesta del storyboard, validar Rafael."
  - Chip literal: "[Metas mensuales por métrica y fechas de corte definitivas: RC/FM/DS, antes del 22-jul]".

### Zona C — Mecanismo de seguimiento (14%, banda a todo lo ancho)
Bloque fondo `--color-gray-100` #F0F3F7, sin rótulo, una-dos líneas Calibri Light 11 pt #3D4A5F:
- "El avance se reporta con KPIs NADAL mensuales por segmento (el real de junio ya está medido palanca por palanca) sobre un plan de $2,337.1M brutos full-year, $1,402.2M a 60% de efectividad."
- Énfasis Calibri bold solo en "KPIs NADAL mensuales".

### Zona C2 — Línea de leyenda de placeholders (sobre el footer)
- Calibri Light 8 pt #8A95A8: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

### Zona D — Footer
- Línea 0.5 pt #E5E9EE. Izquierda: fuente Calibri Light 9 pt italic #8A95A8. Derecha: "PiSA Confidencial  |  32".

## Mensaje que manda la lamina
Los riesgos del 2S no los descubre el Consejo: los declaramos nosotros, cada uno con hipótesis, métrica y fecha de lectura. El Q3 flojo que viene es drenaje planeado del canal, no una sorpresa de octubre; el Q4 estacional está detrás.

## Fuente (pie de lamina)
"Fuente: Sell-In cierre junio 2026; inventarios de canal (DDI, jul-26); cartera Gobierno al 30-jun-2026 (universo cartera, junio-junio); plan NADAL jul-dic 2026; AMIS 2026 (primas GMM). Universos declarados por celda; no se mezclan en una misma gráfica."

## Estado del dato
- Riesgo 1 (~$104M): **por completar [CC]** — la cifra de compra adelantada está por cerrarse; el chip vive dentro de la celda. El desglose por cliente (Simi $30M, Nadro $30M, Fanasa $27M, JMP $17M) se movió a anexo y se imprime allí solo si CC lo confirma. 90-120 días vs 60: en mano.
- Riesgo 2 (primas +6-10%, vencimiento Q4): **en mano** (research validado en v6, fuente AMIS); ahora impreso dentro de la celda de riesgo.
- Riesgo 3 (cartera $4,834M, +22%, 5.3/3.4 meses): **en mano** (deck canal Servicios/Gobierno, corte 02-jul-26; universo cartera).
- Métricas (DDI de 120 a 70; $47M vs $57M/mes; cartera junio-junio): **en mano** (storyline v6, láminas 16 y 25); metas mensuales y fechas de corte definitivas: **por completar [RC/FM/DS]**. Las fechas de la columna "Lectura (propuesta)" son propuesta del storyboard, a validar por Rafael — la nota bajo la tabla lo declara impreso.
- Zona C (NADAL $2,337.1M / $1,402.2M a 60%): **en mano** (plan NADAL).
- A ANEXO: las 3 tarjetas de riesgo completas (ver Contenido diferido a anexo).

## Notas para el dibujante
- **Principio rector: esta lámina es la que más fácil se lee como justificación.** Cada riesgo se enuncia como hecho con dato, nunca con adjetivos ("difícil", "complicado") ni con culpas externas. La hipótesis siempre es una acción nuestra.
- Las 3 tarjetas YA NO SE DIBUJAN: la tabla es la pieza única de la lámina, con aire. No reintroducir tarjetas ni tiles.
- Calibrar redacción con la narrativa "junio bueno / julio hipotecado" para que no choque con el 98.5% sostenido (objeción de Fer): la salida ya está en el subtitle — drenaje planeado, Q4 estacional detrás. No agregar texto extra que reabra el choque.
- La palabra "Gap" está permitida; "boquete" prohibida.
- Sin gold en esta lámina: no hay cifra que celebrar en una lámina de riesgos.
- Sin semáforos de color en la tabla: los riesgos no se pintan de rojo (el semáforo es para deltas cuantitativos en tablas/charts, no para "este tema es serio"). Todo texto en navy/grises.
- Sin caja de insight; sin rótulos "RIESGO"/"MECANISMO" como etiquetas visibles.
- La tabla cabe en 4 columnas × 3 filas + header: no exceder; si algún texto no cabe, se recorta la hipótesis, nunca la métrica ni la fecha.
- Los ahorros de $350M NO aparecen aquí ni en ninguna lámina de M7 (decisión Rafael 10-jul).
- El chip del ~$104M se dibuja literal dentro de su celda; todos los corchetes son PLACEHOLDER INTERNO (kill antes del 27), declarado una sola vez en la línea de leyenda.
- Cero em-dash y cero carácter de flecha en texto imprimible ("de 120 a 70 días", con palabras). Tabular figures en todas las cifras. Números con separador de miles.

### Contenido diferido a anexo
**A ANEXO — Las 3 tarjetas de riesgo (texto completo retirado de la lámina):**
- **Tarjeta 1 — "Julio arranca hipotecado":** "Compra adelantada de junio ~$104M identificables (Simi $30M, Nadro $30M, Fanasa $27M, JMP $17M) [cerrar cifra: CC] y canal con 90-120 días de inventario contra 60 de estándar." (El desglose por cliente se imprime solo si CC lo confirma.)
- **Tarjeta 2 — "Las últimas pólizas con IVA deducible vencen en Q4":** "El pagador hospitalario aprieta: primas 2026 subiendo +6-10% general (AMIS); el efecto duro llega en Q4-2026."
- **Tarjeta 3 — "El gobierno sigue sin pagar":** "Cartera $4,834M al 30-jun-26, +22% vs cierre 2025; FC en 5.3 meses de cartera. El plan del 2S no depende de que pague pronto."
- Formato de origen si se reusa en anexo: fondo blanco, top border 1.5 pt #0F4C81 (nunca border-left), border-radius 4-6 px, nombre en Calibri bold 12 pt #0F2845, dato en Calibri Light 11 pt #3D4A5F, sin iconos ni rótulo "RIESGO".

## Instrucciones ChatGPT Images 2

```
Diapositiva corporativa 16:9 sobre fondo blanco, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera; negritas solo donde se indica; números con separador de miles alineados con dígitos de ancho uniforme. Todo el texto en español con acentos, verbatim tal como aparece entre comillas.

LAYOUT en cinco franjas horizontales apiladas: banda de título (16% de la altura), tabla de cuatro columnas como pieza central con aire (48%), nota chica bajo la tabla (4%), banda gris de mecanismo (14%), línea de leyenda muy chica y pie de página (10%). NO hay tarjetas: la tabla es el único elemento del cuerpo. Márgenes amplios.

BANDA DE TÍTULO: título en navy oscuro #0F2845, sans-serif ligera grande, dos líneas, sin punto final: "Tres riesgos del 2S, declarados hoy con métrica y fecha de lectura". Solo las palabras "declarados hoy" en negrita. Debajo, subtítulo itálica gris azulado #44546A: "El drenaje del Q3 es secuencia planeada con el Q4 estacional detrás".

TABLA a todo lo ancho, cuatro columnas y tres filas de datos más encabezado, con renglones altos y aire. Fila de encabezado con fondo azul #0F4C81 y texto blanco en negrita; filas alternas fondo blanco / azul muy claro #E8F1F8; sin líneas verticales; texto gris #3D4A5F alineado a la izquierda. Encabezados de columna: "Riesgo declarado" | "Hipótesis del plan" | "Métrica de seguimiento" | "Lectura (propuesta)". Filas:
- "Julio arranca hipotecado: compra adelantada de junio ~$104M [cerrar cifra: CC] y canal a 90-120 días de inventario contra 60 de estándar" | "El drenaje del Q3 es secuencia planeada para llegar sanos al Q4 estacional" | "DDI del top de clientes: de 120 a 70 días" | "Mensual; corte al cierre de sep-26"
- "Las últimas pólizas con IVA deducible vencen en Q4 (primas 2026 subiendo +6-10%, AMIS)" | "Las 7 palancas de Hospitales compensan calendario y pagador" | "Run-rate de palancas: $47M/mes contra gap de $57M/mes (medición formal desde julio)" | "Mensual, jul-dic"
- "El gobierno sigue sin pagar: cartera $4,834M al 30-jun-26, +22% vs cierre 2025" | "El 2S depende de surtir bien lo contratado y cobrar con disciplina, no de cobro rápido" | "Cartera junio-junio y meses de cartera (hoy FC 5.3 / Servicios 3.4)" | "Mensual"
El corchete "[cerrar cifra: CC]" se dibuja literal dentro de su celda, en gris neutro.
Bajo la tabla, una nota en gris pequeño #5A6679 en una línea: "Fechas de la columna Lectura: propuesta del storyboard, validar Rafael." y a continuación, con corchetes literales: "[Metas mensuales por métrica y fechas de corte definitivas: RC/FM/DS, antes del 22-jul]".

BANDA DE MECANISMO (franja gris a todo lo ancho, fondo #F0F3F7, sin rótulo): una línea de texto gris #3D4A5F: "El avance se reporta con KPIs NADAL mensuales por segmento (el real de junio ya está medido palanca por palanca) sobre un plan de $2,337.1M brutos full-year, $1,402.2M a 60% de efectividad." Solo las palabras "KPIs NADAL mensuales" en negrita.

LÍNEA DE LEYENDA (encima del pie), gris #8A95A8 muy chico: "Corchetes [ ]: PLACEHOLDER INTERNO, se cierran o se eliminan antes del 27; los responsables no viajan al deck final."

PIE DE PÁGINA: línea fina gris #E5E9EE. Izquierda, gris claro itálica pequeña #8A95A8: "Fuente: Sell-In cierre junio 2026; inventarios de canal (DDI, jul-26); cartera Gobierno al 30-jun-2026 (universo cartera, junio-junio); plan NADAL jul-dic 2026; AMIS 2026 (primas GMM). Universos declarados por celda; no se mezclan en una misma gráfica." Derecha, mismo estilo: "PiSA Confidencial  |  32".

Colores exactos: navy oscuro #0F2845, azul #0F4C81, azul muy claro #E8F1F8, grises #3D4A5F / #5A6679 / #8A95A8, gris de banda #F0F3F7, línea #E5E9EE. NO usar gold en esta lámina. NO dibujar tarjetas de riesgo. NO pintar celdas de rojo ni verde: todo el texto va en navy y grises. Las marcas entre corchetes se dibujan tal cual, en gris neutro. PROHIBIDO: el carácter de flecha o em-dash en cualquier texto, emojis, rótulos de caja tipo "INSIGHT" / "SO WHAT" / "RIESGO" / "MECANISMO", border-left (bordes laterales), verde celebratorio en cifras propias.
```


---

# Lamina 33 · Tres habilitadores empujan el 2S: e-commerce a la venta, transformación al gasto, elasticidad con IA
- **Momento:** M8 · Proyectos críticos, habilitadores y conclusiones
- **Encabezado:** Tres habilitadores empujan el 2S: e-commerce a la venta,
  transformación al gasto, elasticidad con IA
- **So-what subtitle:** El motor de elasticidad capitaliza 18-24 meses de experimentos de precio y alimenta la meta 2027
- **Layout:** Banda de título 18% · cuerpo 70% en 3 columnas iguales (~33% cada una, gutter 0.15in), una por habilitador · footer 12%. Slide 16:9 (13.333 × 7.5 in), márgenes 0.5 in. Lámina deliberadamente ligera: es puente entre la ruta al número (M7) y portafolio/conclusiones; no compite en densidad con las láminas de datos.

## Zona por zona

### Zona A — Título y subtitle (18%)
- Título: Calibri Light 32 pt #0F2845, sentence case, sin punto final: "Tres habilitadores empujan el 2S: e-commerce a la venta, transformación al gasto, elasticidad con IA". Sin negritas dentro del título (la enumeración ya carga la estructura).
- Subtitle: Calibri Light 14 pt italic #44546A: "El motor de elasticidad capitaliza 18-24 meses de experimentos de precio y alimenta la meta 2027".

### Zona B — Columna 1: E-commerce (33%)
- Header de columna: top border 2 pt `--color-primary-700` #0F4C81, fondo `--color-gray-050` #FAFBFC, "E-commerce" Calibri bold 14 pt #0F2845.
- Línea de tesis (Calibri Light 12 pt #3D4A5F): "Contribuye directamente a la venta del 2S."
- KPI card (estilo estándar: label 10.5 pt UPPERCASE #5A6679, valor Calibri bold 40 pt #0F2845, contexto 10 pt #5A6679):
  - Label: "VENTA E-COMMERCE 2S"
  - Valor: "[dato: responsable por asignar]"
  - Contexto: "[canal, alcance y periodo por declarar]"
- Bullet único (11 pt): "[Palancas y clientes del canal digital: responsable por asignar]".

### Zona C — Columna 2: Transformación digital y estructural (33%)
- Header de columna: mismo estilo, "Transformación digital y estructural" Calibri bold 14 pt #0F2845.
- Línea de tesis (12 pt): "Impacta el gasto, no la venta: disciplina de costo que protege la utilidad del compromiso."
- KPI card:
  - Label: "EFECTO EN GASTO 2S"
  - Valor: "[dato: responsable por asignar]"
  - Contexto: "[alcance por declarar]"
- Bullet único (11 pt): "[Frentes de la transformación con efecto 2026: responsable por asignar]".

### Zona D — Columna 3: Motor de elasticidad con IA (33%)
- Header de columna: mismo estilo, "Motor de elasticidad con IA" Calibri bold 14 pt #0F2845.
- Línea de tesis (12 pt): "Industrializa 18-24 meses de experimentos de precio; insumo directo de la meta 2027."
- KPI card (la evidencia del 1S):
  - Label: "EVIDENCIA 1S · IMPULSO"
  - Valor: "+$51M" — ÚNICO elemento gold de la lámina: valor en `--color-gold` #C5A55A, Calibri bold 40 pt.
  - Contexto: "beneficio de precio contra $32M de plan, con el volumen esperado (sell-in 1S26)"
- Bullet único (11 pt): "Segundo incremento de precios corrió en julio con gestión de elasticidad por canal [VJ]; el detalle del método vive en el Anexo D."

### Zona E — Footer
- Línea 0.5 pt #E5E9EE. Izquierda: fuente Calibri Light 9 pt italic #8A95A8. Derecha: "PiSA Confidencial  |  33".

## Mensaje que manda la lamina
Además de las palancas comerciales, el 2S tiene tres habilitadores trabajando: uno suma venta (e-commerce), uno protege gasto (transformación) y uno convierte 18-24 meses de experimentos de precio en un motor de elasticidad con IA que ya probó valor (+$51M en Impulso) y alimenta la meta 2027.

## Fuente (pie de lamina)
"Fuente: Sell-In cierre junio 2026 (evidencia de elasticidad en Impulso, 1S26); programas internos de e-commerce y transformación [alcances por declarar]. Detalle de elasticidad y precio ponderado en Anexo D."

## Estado del dato
- Zona B (e-commerce): **placeholder [responsable por asignar]** — el storyline v6 no asigna dueño ni cifra; sin monto no se imprime la KPI card, se deja la línea de tesis sola.
- Zona C (transformación): **placeholder [responsable por asignar]** — mismo caso. OJO: los ahorros de $350M están explícitamente FUERA del deck (decisión Rafael 10-jul); no rellenar este hueco con esa cifra.
- Zona D (elasticidad +$51M vs $32M plan; 18-24 meses; segundo incremento julio): **en mano** (sell-in 1S26 / storyline v6 L14-L16-L33).
- REGLA 16-jul (sin KPIs aún): los chips "[KPI por asignar: Felipe/RC]" SE MANTIENEN. Si los KPIs de e-commerce y transformación NO llegan el 21-jul, esta lámina SE COLAPSA a una franja dentro de la L34 (decisión Rafael); no viaja al Consejo con dos de tres columnas en placeholder.

## Notas para el dibujante
- **PROHIBIDO rellenar los placeholders de e-commerce y transformación con cifras de otras láminas o del research.** Si al ensamblar no hay dato, la columna baja a texto cualitativo (tesis + bullet) sin KPI card; nunca un número inventado.
- **NO meter los $350M de ahorros** en la columna de transformación (decisión Rafael 10-jul: fuera del deck).
- Único gold de la lámina: el "+$51M" de la Zona D. Nada más lleva gold.
- El "+$51M" NO va en verde semáforo: aquí es la cifra pivotal del habilitador (gold), no un delta de tabla. No duplicar el énfasis (gold y verde a la vez, jamás).
- Sin caja de insight; sin rótulos "HABILITADOR 1/2/3" — los headers de columna son los nombres propios de cada habilitador.
- Las tres columnas deben pesar visualmente igual aunque dos tengan placeholder: misma altura de card, mismo header. La asimetría de datos no se disfraza, se declara.
- La decisión pendiente "[ROI de un ejecutivo de ventas dentro de disciplina de gasto: Felipe/Rafa]" pertenece a la L31, no a esta lámina; no traerla aquí.
- Tono: habilitadores acotados, cero promesas de plataforma; "insumo de la meta 2027" es el techo de la ambición verbal en esta lámina (la estrategia completa llega en septiembre).
- Tabular figures en cifras; sin emojis, sin iconos de color, sin border-left.
- Todo corchete con responsable ([KPI por asignar: Felipe/RC], [VJ], [responsable por asignar]) es [PLACEHOLDER INTERNO - kill antes del 27]: se dibuja literal en gris y se resuelve o se corta antes de la sesión (ver regla de colapso en Estado del dato).

- DECISIÓN PROVISIONAL (orquestador, 16-jul, validable por Rafael): las columnas e-commerce y transformación van CUALITATIVAS (tesis + bullet, sin cifra); su KPI card se dibuja con el chip "[KPI por asignar: Felipe/RC]". La columna de elasticidad queda como está (+$51M en gold).

## Instrucciones ChatGPT Images 2

```
Diapositiva corporativa 16:9 sobre fondo blanco, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera; negritas solo donde se indica; números alineados a la derecha. Todo el texto en español con acentos, verbatim tal como aparece entre comillas. Lámina deliberadamente ligera, con mucho aire: es un puente, no una lámina densa de datos.

LAYOUT en tres franjas: banda de título arriba (18% de la altura), cuerpo central en TRES columnas iguales de ~33% cada una con separación (70% de la altura), y pie de página abajo (12%). Márgenes amplios.

BANDA DE TÍTULO: título en navy oscuro #0F2845, sans-serif ligera grande, dos líneas, sin punto final, SIN negritas: "Tres habilitadores empujan el 2S: e-commerce a la venta, transformación al gasto, elasticidad con IA". Debajo, subtítulo itálica gris azulado #44546A: "El motor de elasticidad capitaliza 18-24 meses de experimentos de precio y alimenta la meta 2027".

COLUMNA 1 (izquierda). Encabezado de columna: caja con fondo gris muy claro #FAFBFC y línea SUPERIOR de 2 pt en azul #0F4C81 (arriba, nunca lateral), texto en negrita navy #0F2845: "E-commerce". Debajo, línea de tesis en gris #3D4A5F: "Contribuye directamente a la venta del 2S." Debajo, una tarjeta de KPI: etiqueta pequeña en mayúsculas gris #5A6679 "VENTA E-COMMERCE 2S"; en lugar del número grande, un chip gris dibujado literalmente con corchetes "[KPI por asignar: Felipe/RC]"; contexto en gris pequeño, dibujado literal: "[canal, alcance y periodo por declarar]". Debajo, una viñeta gris dibujada literal: "[Palancas y clientes del canal digital: responsable por asignar]".

COLUMNA 2 (centro). Encabezado de columna del mismo estilo (fondo #FAFBFC, línea superior 2 pt #0F4C81), texto negrita #0F2845: "Transformación digital y estructural". Línea de tesis gris #3D4A5F: "Impacta el gasto, no la venta: disciplina de costo que protege la utilidad del compromiso." Tarjeta de KPI: etiqueta mayúsculas gris "EFECTO EN GASTO 2S"; chip gris literal con corchetes "[KPI por asignar: Felipe/RC]"; contexto literal "[alcance por declarar]". Viñeta gris literal: "[Frentes de la transformación con efecto 2026: responsable por asignar]".

COLUMNA 3 (derecha). Encabezado del mismo estilo, texto negrita #0F2845: "Motor de elasticidad con IA". Línea de tesis gris #3D4A5F: "Industrializa 18-24 meses de experimentos de precio; insumo directo de la meta 2027." Tarjeta de KPI: etiqueta mayúsculas gris "EVIDENCIA 1S · IMPULSO"; valor grande "+$51M" — ÚNICO elemento en color gold #C5A55A de toda la lámina, en negrita grande; contexto en gris pequeño #5A6679: "beneficio de precio contra $32M de plan, con el volumen esperado (sell-in 1S26)". Viñeta gris #3D4A5F: "Segundo incremento de precios corrió en julio con gestión de elasticidad por canal [VJ]; el detalle del método vive en el Anexo D."

Las tres columnas deben pesar visualmente igual: misma altura de tarjeta, mismo encabezado, aunque dos lleven chip placeholder y una lleve el número.

PIE DE PÁGINA: línea fina gris #E5E9EE. Izquierda, gris claro itálica pequeña #8A95A8: "Fuente: Sell-In cierre junio 2026 (evidencia de elasticidad en Impulso, 1S26); programas internos de e-commerce y transformación [alcances por declarar]. Detalle de elasticidad y precio ponderado en Anexo D." Derecha, mismo estilo: "PiSA Confidencial  |  33".

Colores exactos: navy oscuro #0F2845, azul #0F4C81, gold #C5A55A (SOLO en el "+$51M"), grises #3D4A5F / #5A6679 / #8A95A8, gris muy claro de cajas #FAFBFC, línea #E5E9EE. El "+$51M" va en gold, NUNCA en verde. Ninguna otra cifra o elemento lleva gold. Los chips y textos entre corchetes se dibujan tal cual, en gris neutro, sin rellenarlos con números. PROHIBIDO: el carácter de flecha en cualquier texto, emojis, rótulos de caja tipo "INSIGHT" / "SO WHAT" / "HABILITADOR 1/2/3", border-left (bordes laterales), verde celebratorio en cifras propias.
```


---

# Lamina 34 · Lanzamientos aportan +$94.4M, el motor #2 del crecimiento; lo inorgánico va por moléculas, marcas y registros
- **Momento:** M8 · Proyectos críticos, habilitadores y conclusiones
- **Encabezado:** Lanzamientos aportan +$94.4M, el motor #2 del crecimiento;
  lo inorgánico va por moléculas, marcas y registros
  (Título 16-jul: los lanzamientos CONSOLIDADOS +$94.4M encabezan como motor #2 del puente, con la vista reclasificada declarada; el +$43.8M de Retail baja a detalle. La ventana GLP-1 vive en la banda 2, no en el título.)
- **So-what subtitle:** Aprendemos con los chiquitos antes de que lleguen los grandotes; la estrategia completa viene en septiembre
- **Layout:** Banda de título 16% · banda 1 "Pipeline 2026" 30% (KPI row de 4 tarjetas + línea de lectura) · banda 2 "Ventana GLP-1" 24% (timeline horizontal) · banda 3 "Pincelada inorgánica" 20% (3 bullets + 1 dato) · footer 10%. Slide 16:9 (13.333 × 7.5 in), márgenes 0.5 in.

## Zona por zona

### Zona A — Título y subtitle (16%)
- Título: Calibri Light 32 pt #0F2845, sentence case, sin punto final, 2 líneas: "Lanzamientos aportan +$94.4M, el motor #2 del crecimiento; lo inorgánico va por moléculas, marcas y registros". Énfasis Calibri bold en "+$94.4M".
- Subtitle: Calibri Light 14 pt italic #44546A: "Aprendemos con los chiquitos antes de que lleguen los grandotes; la estrategia completa viene en septiembre".

### Zona B — Banda 1: Pipeline 2026 con credibilidad medida (30%)
- KPI row de 4 tarjetas iguales (padding 0.2 in; separación por border 0.5 pt #E5E9EE, sin fondo; label Calibri Light 10.5 pt UPPERCASE #5A6679; valor Calibri bold 40 pt; contexto Calibri Light 10 pt #5A6679):
  1. Label "LANZAMIENTOS 2026 · PUENTE CONSOLIDADO 1S" · Valor "+$94.4M" en `--color-gold` #C5A55A (ÚNICO gold de la lámina) · Contexto "vista reclasificada del puente consolidado, sell-in 1S26 vs 1S25; en Retail, +$43.8M de flujo genuino".
  2. Label "ALCANCE DE LANZAMIENTOS" · Valor "83%" #0F2845 · Contexto "proyección anual de la meta de lanzamientos (63% ene-jun); Votripax 57% · Pisalak 68% · Pixiba 73%".
  3. Label "PIXIBA · SHARE EN UNIDADES" · Valor "28%" #0F2845 · Contexto "junio, a meses del lanzamiento; levantamientos propios en hospitales (líder: Dynastat)".
  4. Label "SITAGLIPTINA · OBJETIVO DE SHARE" · Valor "10%" #0F2845 · Contexto "si no hay pausas de suministro".
- Línea de lectura bajo la KPI row (Calibri Light 11 pt #3D4A5F, una línea): "Hoy jugamos en la parte menos atractiva de un mercado que sí crece; el plan es movernos a las albercas que crecen. El detalle vive en el comité de nuevos productos."

### Zona C — Banda 2: La ventana GLP-1, dicha con precisión (24%)
- Timeline horizontal de 3 hitos (línea 1.5 pt `--color-gray-300` #C5CDD9; nodos círculo 10-12 px en `--color-primary-900` #0F2845; fecha en Calibri bold 11 pt #0F2845 arriba del nodo; descripción Calibri Light 10.5 pt #3D4A5F abajo, máx 2 líneas por nodo):
  1. "mar-26" — "Vence la patente base de semaglutida (global)"
  2. "hoy" — "México bloqueado por protección de datos clínicos; litigio en curso"
  3. "4T-26 / 2027" — "Genéricos posibles en México"
- Nota bajo el timeline (Calibri Light 10 pt #5A6679, una línea): "Las reformas de abril (DOF: 5 años de protección de datos + certificado que extiende patente hasta +5 años) alargan la fricción para todos: arma de doble filo para nuestro propio pipeline."

### Zona D — Banda 3: Pincelada inorgánica, acotada (20%)
- Bloque con top border 2 pt `--color-primary-700` #0F4C81, fondo blanco. Primera línea Calibri bold 12 pt #0F2845: "Inorgánico acotado a moléculas, marcas y registros, no compañías; sin montos en esta junta".
- 3 bullets Calibri Light 11 pt #3D4A5F:
  1. "Comprar registros sanitarios atorados: ahorra 12-18 meses de trámite"
  2. "Licenciar o comprar moléculas del innovador que se repliega"
  3. "Adquirir o crear marcas para rejuvenecer el portafolio: hoy 14% de la venta de AMSA es con marca contra 68% del mercado [validar fuente: CC]"

### Zona E — Footer
- Línea 0.5 pt #E5E9EE. Izquierda: fuente Calibri Light 9 pt italic #8A95A8. Derecha: "PiSA Confidencial  |  34".

## Mensaje que manda la lamina
Los lanzamientos ya son el motor #2 del crecimiento del semestre (+$94.4M consolidados en la vista reclasificada del puente, con +$43.8M de flujo genuino en Retail) y recuperan credibilidad con resultados medibles en productos chicos, mientras se prepara la ventana GLP-1 que en México abre hasta 4T-26/2027; la vía inorgánica existe pero acotada a moléculas, marcas y registros, sin comprometer montos hoy.

## Fuente (pie de lamina)
"Fuente: matriz consolidada Downtrading FINAL 16-jul (lanzamientos +$94.4M, vista reclasificada del puente consolidado; +$43.8M flujo genuino Retail; sell-in 1S26 vs 1S25, lista autoritativa de lanzamientos); alcance de lanzamientos deck canal Farmacias jun-26; share Pixiba: levantamientos propios en hospitales jun-26; semaglutida y reformas de PI: prensa mar-may 2026 y DOF 3/24-abr-2026; participación de marca AMSA vs mercado [fuente por confirmar: CC]. Universos: sell-in / sell-out estimado propio; no se mezclan."

## Estado del dato
- Zona B tarjeta 1 (+$94.4M): **en mano, ACTUALIZADO 16-jul** — línea Lanzamientos del TOTAL PiSA en la matriz consolidada FINAL 16-jul (vista reclasificada, DECLARADA en el contexto de la tarjeta y en el pie). Es el motor #2 del crecimiento del puente (título de Rafael #5). El +$43.8M (flujo genuino Retail) queda como detalle en el contexto. Caveat de citación: el único citable como sell-in del semestre sigue siendo +$239.3M; el +$94.4M es un componente del puente y viaja siempre con su etiqueta de vista reclasificada.
- Zona B tarjeta 2 (83% anual, 63% ene-jun, Votripax 57 / Pisalak 68 / Pixiba 73): **en mano** (deck canal Farmacias). Se rotula "alcance de lanzamientos" (nunca "GAP").
- Zona B tarjeta 3 (Pixiba 28%): **en mano como intel propio** — 11K pzs de un mercado estimado de 40-45K por levantamientos propios; se dice como estimación propia, nunca con fuente de auditor.
- Zona B tarjeta 4 (Sitagliptina objetivo 10%): **en mano** (storyline v6; es objetivo, no resultado — el label lo declara).
- Zona C (semaglutida mar-26, bloqueo por datos, 4T-26/2027, reformas DOF abril): **en mano con reserva** — research clasificado confiabilidad media; el v6 lo integró como imprimible, pero validar redacción final contra la regla "nada de confiabilidad media/baja sin validar" antes del 22-jul [Rafael].
- Zona D bullet 3 (14% vs 68%): **por completar [CC]** — cifra citada en revisiones internas; confirmar fuente (Knobloch u otro corte) antes de imprimir.

## Notas para el dibujante
- **SIN montos comprometidos en la banda inorgánica:** ni rangos, ni "estamos evaluando $X". Si alguien pide sizing, la respuesta vive con Estrategia, no en la lámina.
- Nombre del producto RESUELTO por Rafael (16-jul): se escribe PIXIBA (con b) en todo el deck; storyline v6 y esta spec ya lo aplican.
- Jerarquía de cifras de lanzamientos (16-jul): +$94.4M = consolidado PiSA, vista reclasificada DECLARADA (headline); +$43.8M = flujo genuino Retail (detalle). Los +$71.1M y +$58.7M siguen PROHIBIDOS sin su etiqueta de vista (analíticas internas). Nunca presentar el +$94.4M como si fuera sell-in puro: siempre con "vista reclasificada del puente consolidado".
- Único gold: el valor "+$94.4M" de la tarjeta 1. El "83%", "28%" y "10%" van en navy #0F2845.
- Todo corchete con responsable ([fuente por confirmar: CC], [Rafael]) es [PLACEHOLDER INTERNO - kill antes del 27].
- Tono de pipeline: "sin prometer al Gran Salvador". Nada de adjetivos ("gran oportunidad", "enorme potencial"); los números cargan el argumento.
- El timeline no lleva colores semáforo: es cronología, no evaluación. Nodos navy, línea gris.
- "GLP-1" y "share" se quedan en inglés/anglicismo (permitidos); "Gap" permitido; "boquete" prohibido.
- Sin caja de insight; sin rótulos "PIPELINE"/"INORGÁNICO" como etiquetas sueltas — los encabezados de banda indicados son frases integradas, no badges.
- Tabular figures en toda cifra. Sin emojis (los semáforos de color del deck fuente de Farmacias NO se heredan).

## Instrucciones ChatGPT Images 2

```
Diapositiva corporativa 16:9 sobre fondo blanco, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera; negritas solo donde se indica; números alineados a la derecha. Todo el texto en español con acentos, verbatim tal como aparece entre comillas.

LAYOUT en cinco franjas horizontales apiladas: banda de título (16% de la altura), banda 1 "Pipeline" con fila de cuatro tarjetas de KPI (30%), banda 2 con un timeline horizontal de tres hitos (24%), banda 3 con un bloque de bullets (20%) y pie de página (10%). Márgenes amplios.

BANDA DE TÍTULO: título en navy oscuro #0F2845, sans-serif ligera grande, dos líneas, sin punto final: "Lanzamientos aportan +$94.4M, el motor #2 del crecimiento; lo inorgánico va por moléculas, marcas y registros". Solo "+$94.4M" en negrita. Debajo, subtítulo itálica gris azulado #44546A: "Aprendemos con los chiquitos antes de que lleguen los grandotes; la estrategia completa viene en septiembre".

BANDA 1 (Pipeline): fila de CUATRO tarjetas iguales, separadas por una línea fina gris #E5E9EE, sin fondo. Cada tarjeta: etiqueta pequeña en mayúsculas gris #5A6679 arriba, valor grande en negrita al centro, contexto gris pequeño #5A6679 abajo.
- Tarjeta 1: etiqueta "LANZAMIENTOS 2026 · PUENTE CONSOLIDADO 1S"; valor "+$94.4M" en color gold #C5A55A (ÚNICO gold de la lámina); contexto "vista reclasificada del puente consolidado, sell-in 1S26 vs 1S25; en Retail, +$43.8M de flujo genuino".
- Tarjeta 2: etiqueta "ALCANCE DE LANZAMIENTOS"; valor "83%" en navy #0F2845; contexto "proyección anual de la meta de lanzamientos (63% ene-jun); Votripax 57% · Pisalak 68% · Pixiba 73%".
- Tarjeta 3: etiqueta "PIXIBA · SHARE EN UNIDADES"; valor "28%" en navy #0F2845; contexto "junio, a meses del lanzamiento; levantamientos propios en hospitales (líder: Dynastat)".
- Tarjeta 4: etiqueta "SITAGLIPTINA · OBJETIVO DE SHARE"; valor "10%" en navy #0F2845; contexto "si no hay pausas de suministro".
Bajo la fila, una línea de lectura en gris #3D4A5F: "Hoy jugamos en la parte menos atractiva de un mercado que sí crece; el plan es movernos a las albercas que crecen. El detalle vive en el comité de nuevos productos."

BANDA 2 (Timeline GLP-1): línea horizontal de 1.5 pt en gris #C5CDD9 con TRES nodos circulares navy #0F2845 espaciados de izquierda a derecha. Sobre cada nodo la fecha en negrita navy #0F2845; bajo cada nodo la descripción en gris #3D4A5F (máx 2 líneas). Nodo 1: fecha "mar-26", descripción "Vence la patente base de semaglutida (global)". Nodo 2: fecha "hoy", descripción "México bloqueado por protección de datos clínicos; litigio en curso". Nodo 3: fecha "4T-26 / 2027", descripción "Genéricos posibles en México". Bajo el timeline, una nota en gris pequeño #5A6679: "Las reformas de abril (DOF: 5 años de protección de datos + certificado que extiende patente hasta +5 años) alargan la fricción para todos: arma de doble filo para nuestro propio pipeline."

BANDA 3 (Pincelada inorgánica): bloque con línea SUPERIOR de 2 pt en azul #0F4C81 (arriba, nunca lateral), fondo blanco. Primera línea en negrita navy #0F2845: "Inorgánico acotado a moléculas, marcas y registros, no compañías; sin montos en esta junta". Debajo, tres viñetas simples en gris #3D4A5F: "Comprar registros sanitarios atorados: ahorra 12-18 meses de trámite" · "Licenciar o comprar moléculas del innovador que se repliega" · "Adquirir o crear marcas para rejuvenecer el portafolio: hoy 14% de la venta de AMSA es con marca contra 68% del mercado [validar fuente: CC]".

PIE DE PÁGINA: línea fina gris #E5E9EE. Izquierda, gris claro itálica pequeña #8A95A8: "Fuente: matriz consolidada Downtrading FINAL 16-jul (lanzamientos +$94.4M, vista reclasificada del puente consolidado; +$43.8M flujo genuino Retail; sell-in 1S26 vs 1S25, lista autoritativa de lanzamientos); alcance de lanzamientos deck canal Farmacias jun-26; share Pixiba: levantamientos propios en hospitales jun-26; semaglutida y reformas de PI: prensa mar-may 2026 y DOF 3/24-abr-2026; participación de marca AMSA vs mercado [fuente por confirmar: CC]. Universos: sell-in / sell-out estimado propio; no se mezclan." Derecha, mismo estilo: "PiSA Confidencial  |  34".

Colores exactos: navy oscuro #0F2845, azul #0F4C81, gold #C5A55A (SOLO en el "+$94.4M" de la tarjeta 1), gris de línea de timeline #C5CDD9, grises #3D4A5F / #5A6679 / #8A95A8, línea #E5E9EE. Los valores "83%", "28%" y "10%" van en navy, NO en gold. El timeline es cronología: nodos navy y línea gris, sin colores de semáforo. Las marcas entre corchetes se dibujan tal cual, en gris neutro (placeholders internos del borrador). PROHIBIDO: el carácter de flecha en cualquier texto, emojis, rótulos de caja tipo "INSIGHT" / "SO WHAT" / "PIPELINE" / "INORGÁNICO", border-left (bordes laterales), verde celebratorio en cifras propias, rayas largas (em-dash) en la prosa, y la palabra "GAP" como rótulo de la tarjeta 2 (se rotula "alcance").
```


---

# Lamina 35 · Nos comprometemos con el [96] y lo revisamos con ustedes cada mes
- **Momento:** M8 · Proyectos críticos, habilitadores y conclusiones
- **Encabezado:** Nos comprometemos con el [96] y lo revisamos
  con ustedes cada mes
- **So-what subtitle:** Esta junta es táctica y ya tiene número; la estrategia de largo plazo llega en septiembre
- **Layout:** Banda de título 16% · cuerpo 58% en 2 columnas 40/60 (izquierda: KPI hero del compromiso; derecha: 3 conclusiones) · banda inferior 14% (la línea de largo plazo, a todo lo ancho) · footer 12%. Slide 16:9 (13.333 × 7.5 in), márgenes 0.5 in. Es la lámina de cierre: la más limpia del deck, mucho aire.

## Zona por zona

### Zona A — Título y subtitle (16%)
- Título: Calibri Light 32 pt #0F2845, sentence case, sin punto final: "Nos comprometemos con el [96] y lo revisamos con ustedes cada mes". Énfasis Calibri bold en "[96]".
- Subtitle: Calibri Light 14 pt italic #44546A: "Esta junta es táctica y ya tiene número; la estrategia de largo plazo llega en septiembre".

### Zona B — Columna izquierda (40%): KPI hero del compromiso
- KPI hero único centrado en la columna:
  - Label: "COMPROMISO ANUAL 2026" Calibri Light 10.5 pt UPPERCASE tracking amplio #5A6679.
  - Valor: "[96]" Calibri bold 54 pt #0F2845 (placeholder tal cual, entre corchetes, hasta que Heriberto/Dirección cierren el número antes del 20-jul).
  - Contexto (Calibri Light 11 pt #5A6679, 2 líneas): "Exige $18,115.1M en jul-dic: 98.5% sostenido de la meta del semestre" y "Con contribución de 53 centavos por peso, alcanza la meta de utilidad del año".
- Sin recuadro de color; separación con border 0.5 pt #E5E9EE si se necesita delimitar.

### Zona C — Columna derecha (60%): las tres conclusiones + ask
- 3 bloques de texto apilados (Calibri Light 13 pt #3D4A5F, interlínea cómoda; sin numeración de framework, sin viñetas decoradas — guion o viñeta simple):
  1. "El 2S se construye con palancas propias, no con esperanza de mercado: NADAL, segundo incremento de precios, defensa de la mezcla y plan invernal."
  2. "Dos supuestos sostienen el número, ambos con métrica mensual: efectividad NADAL en frasco cerrado y sostenimiento de Servicios." (Redacción 16-jul: promesas convertidas a MECANISMO; no volver a "va a funcionar" / "se va a mantener".)
  3. "El seguimiento es mensual: KPIs NADAL por segmento y tablero de hipótesis con métrica y fecha; ustedes ven el avance cada mes."
- Bajo las tres conclusiones, chip literal en gris `#8A95A8`, fondo `#F0F3F7`, borde 0.5 pt `#C5CDD9`: "[ask al Consejo por definir: Rafael/Felipe]".
- Énfasis Calibri bold solo en "palancas propias" (bloque 1) y "mensual" (bloque 3) — máximo de negritas de la lámina ya usado con el [96] del título; si se excede, quitar la de "mensual".

### Zona D — Banda inferior (14%): la línea de largo plazo (UNA línea, la única mención)
- Bloque a todo lo ancho, fondo `--color-gray-050` #FAFBFC, top border 1 pt `--color-gray-300` #C5CDD9, texto Calibri Light 11.5 pt #3D4A5F en UNA sola oración (puede correr a 2 renglones visuales, pero es una oración; SIN em-dash):
  - "El largo plazo juega a favor: población envejeciendo, diabetes en 17-18% de los adultos, hipertensión en 29.4%, la enfermedad renal crónica ya quinta causa de muerte (Ensanut/INSP) y nearshoring; vientos de cola no para 2026, pero sí para los siguientes 20 años."
- Nada más en esta banda: ni gráfica, ni segunda oración, ni llamado a discutir estrategia.

### Zona E — Footer
- Línea 0.5 pt #E5E9EE. Izquierda: fuente Calibri Light 9 pt italic #8A95A8. Derecha: "PiSA Confidencial  |  35".

## Mensaje que manda la lamina
La sesión cierra donde abrió: el compromiso es [96], el mecanismo de revisión es mensual y las palancas son propias. El largo plazo se desliza en una sola línea con datos de salud pública; la sesión de estrategia es en septiembre, no hoy.

## Fuente (pie de lamina)
"Fuente: Sell-In cierre junio 2026 (base 1S y year-to-go); Ensanut 2022 y Ensanut continua 2021-2024 (INSP) para prevalencias. El compromiso anual se cierra con Dirección General antes del 20-jul."

## Estado del dato
- Zona A/B ([96]): **placeholder [Heriberto/Dirección, antes del 20-jul]** — pendiente exógeno; NADA aguas abajo de este número se recalcula hasta que llegue. El $18,115.1M y el 98.5% están calculados sobre el [96] actual: si el número negociado cambia, RECALCULAR ambos [RC]. Notación única "[96]", sin unidad (la unidad vive solo en L1).
- Zona B contexto (53 centavos por peso): **en mano** (storyline v6, marco de la sesión).
- Zona C (conclusiones): **en mano** (consolidan L31-L32; texto listo). Conclusión 2 REDACTADA 16-jul como mecanismo con métrica mensual (no promesa). El ASK al Consejo sigue placeholder [Rafael/Felipe]: se imprime como chip hasta que lo definan.
- Zona D (diabetes 17-18%, hipertensión 29.4%, ERC quinta causa): **en mano** (research validado confiabilidad alta: Ensanut 2022 = 18.3%, Ensanut continua 2021-2024 = 17.0%; hipertensión 29.4% Ensanut 2022; ERC quinta causa de muerte INSP).

## Notas para el dibujante
- **El largo plazo es UNA línea y nada más.** No expandir a bullets, no agregar mini-gráfica de prevalencias, no abrir sesión de estrategia. Si sobra espacio, se deja aire: es la lámina de cierre.
- El "[96]" se dibuja con corchetes visibles en toda versión de trabajo; solo la versión final (post-negociación con Heriberto) los quita. Prohibido rellenarlo con 96 "por mientras" sin corchetes.
- Sin gold en esta lámina: el compromiso va en navy hero; el cierre es sobrio, no celebratorio.
- Sin caja de insight; sin rótulo "CONCLUSIONES" como banner — el título carga el cierre.
- Meta contra real sin aplauso: cero frases de autofelicitación ("gran esfuerzo", "orgullosos"); el compromiso se afirma, no se celebra.
- El rango "17-18%" de diabetes es deliberado (dos mediciones Ensanut: 17.0% continua 2021-2024 y 18.3% 2022); no colapsarlo a un solo número ni "promediarlo".
- Cero contrafactuales y cero menciones de la simulación de servicio en el cierre.
- Cero em-dash en texto imprimible: la línea de largo plazo ya va con dos puntos y punto y coma.
- Todo corchete con responsable ([ask al Consejo por definir: Rafael/Felipe], [RC]) es [PLACEHOLDER INTERNO - kill antes del 27].
- Tabular figures en el hero y en las cifras de la línea de largo plazo. Sin emojis, sin iconos.
- Consistencia con la Lámina 1 (M0): el [96] del cierre debe ser idéntico en formato al de la apertura (allá con su unidad declarada, aquí a secas); verificar al ensamblar.

## Instrucciones ChatGPT Images 2

```
Diapositiva corporativa 16:9 sobre fondo blanco, estilo flat de consultoría: sin gradientes, sin sombras infladas, sin fotos de stock, sin logos, sin emojis, sin iconos de color. Tipografía sans-serif limpia y ligera; negritas solo donde se indica; números alineados a la derecha. Todo el texto en español con acentos, verbatim tal como aparece entre comillas. Es la lámina de cierre: la más limpia del deck, con mucho aire.

LAYOUT en cuatro franjas: banda de título arriba (16% de la altura), cuerpo central en dos columnas 40/60 (58% de la altura: izquierda estrecha con un KPI hero, derecha ancha con tres conclusiones), banda inferior a todo lo ancho (14%) y pie de página (12%). Márgenes amplios.

BANDA DE TÍTULO: título en navy oscuro #0F2845, sans-serif ligera grande, sin punto final: "Nos comprometemos con el [96] y lo revisamos con ustedes cada mes". Solo "[96]" en negrita (dibujado con corchetes visibles). Debajo, subtítulo itálica gris azulado #44546A: "Esta junta es táctica y ya tiene número; la estrategia de largo plazo llega en septiembre".

COLUMNA IZQUIERDA (40%, estrecha): un KPI hero centrado. Arriba, etiqueta pequeña en mayúsculas con tracking amplio, gris #5A6679: "COMPROMISO ANUAL 2026". Al centro, valor enorme en negrita navy #0F2845, dibujado literal con corchetes: "[96]". Debajo, contexto en gris #5A6679 en dos líneas: "Exige $18,115.1M en jul-dic: 98.5% sostenido de la meta del semestre" y "Con contribución de 53 centavos por peso, alcanza la meta de utilidad del año". Sin recuadro de color.

COLUMNA DERECHA (60%, ancha): tres bloques de texto apilados con interlínea cómoda, en gris #3D4A5F, cada uno precedido por un guion o viñeta simple (sin numeración de framework):
1. "El 2S se construye con palancas propias, no con esperanza de mercado: NADAL, segundo incremento de precios, defensa de la mezcla y plan invernal." (las palabras "palancas propias" en negrita)
2. "Dos supuestos sostienen el número, ambos con métrica mensual: efectividad NADAL en frasco cerrado y sostenimiento de Servicios."
3. "El seguimiento es mensual: KPIs NADAL por segmento y tablero de hipótesis con métrica y fecha; ustedes ven el avance cada mes." (la palabra "mensual" en negrita)
Bajo los tres bloques, un chip rectangular pequeño con fondo gris muy claro #F0F3F7 y borde fino gris #C5CDD9, texto gris #8A95A8 dibujado literal con sus corchetes: "[ask al Consejo por definir: Rafael/Felipe]".

BANDA INFERIOR (franja a todo lo ancho, fondo gris muy claro #FAFBFC, línea SUPERIOR de 1 pt en gris #C5CDD9, arriba nunca lateral): UNA sola oración en gris #3D4A5F (puede correr a dos renglones visuales, sin rayas largas): "El largo plazo juega a favor: población envejeciendo, diabetes en 17-18% de los adultos, hipertensión en 29.4%, la enfermedad renal crónica ya quinta causa de muerte (Ensanut/INSP) y nearshoring; vientos de cola no para 2026, pero sí para los siguientes 20 años." Nada más en esta banda: ni gráfica, ni segunda oración.

PIE DE PÁGINA: línea fina gris #E5E9EE. Izquierda, gris claro itálica pequeña #8A95A8: "Fuente: Sell-In cierre junio 2026 (base 1S y year-to-go); Ensanut 2022 y Ensanut continua 2021-2024 (INSP) para prevalencias. El compromiso anual se cierra con Dirección General antes del 20-jul." Derecha, mismo estilo: "PiSA Confidencial  |  35".

Colores exactos: navy oscuro #0F2845, grises #3D4A5F / #5A6679 / #8A95A8, gris muy claro de banda #FAFBFC, gris de línea superior #C5CDD9, línea #E5E9EE. NO usar gold en esta lámina: el compromiso va en navy hero, cierre sobrio. El "[96]" se dibuja con corchetes visibles, NUNCA rellenado con un número. El chip "[ask al Consejo por definir: Rafael/Felipe]" se dibuja literal (placeholder interno del borrador; se resuelve antes de la versión final). El rango "17-18%" de diabetes se deja como rango, sin colapsarlo. PROHIBIDO: el carácter de flecha en cualquier texto, emojis, rótulos de caja tipo "INSIGHT" / "SO WHAT" / "CONCLUSIONES", border-left (bordes laterales), verde celebratorio en cifras propias, rayas largas (em-dash) en la prosa.
```


---
