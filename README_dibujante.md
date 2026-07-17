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

## Dirección de la SIGUIENTE versión (Rafael 16-jul noche; NO aplicar aún, se replantea tras revisar la actual)
Estilo "corporate road show de investor relations": 1 a 3 gráficas por diapositiva, mucho menos texto; converge con el corte de BCG (núcleo ~20) y el veredicto del art director. El PPT de revisión se organiza por momentos (índice primero, máx 4 fotos por diapositiva, sin mezclar momentos).
- **Calibración de Rafael (16-jul, tarde-noche): NO abusar del "número héroe por lámina".** Datos memorables sí, pero no en cada lámina: las de contexto, plan o transición pueden vivir de una gráfica limpia o de pocas líneas bien escritas sin KPI gigante. El ritmo del deck alterna láminas con dato ancla y láminas que respiran.
- Redacción humana de director (prohibido "villano" y toda plantilla con olor a IA); rediseño en curso: 3 arquitectos → síntesis Fable → PAUSA para propuesta a Rafael antes de specs/dibujo (9 carriles Codex tras su OK).

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
