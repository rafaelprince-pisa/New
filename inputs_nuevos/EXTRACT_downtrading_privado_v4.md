# EXTRACT — Paquete Downtrading Privado v4 (Consejo Pharma MX, 27-jul-2026)

Extracción fiel y exhaustiva del paquete Downtrading Privado v4. No filtra ni juzga qué sirve para el deck; el orquestador integra. Todo número lleva unidad, periodo y base de comparación. Fuente base: `Sell-In-2023-2026-Cierre-JUN.xlsx` (cubo MER-CAN-PROD) + `Diccionario_PISA_SKUs.csv`; entregable `Downtrading_Privado_v4_FINAL_2026-07-15.xlsx`.

**Alcance de todo el paquete:** segmento **Privado = Farmacias + Impulso + Expansión** (el "Retail" del storyline v5, 43.6% de la venta). Periodo **Ene–Jun 2026 vs Ene–Jun 2025** (H1-26 vs H1-25). Moneda **MXN, millones (M)**. Venta = **sell-in neto** del cubo.

**Nota de trazabilidad de esta extracción:** el Excel entrega fórmulas vivas; openpyxl `data_only` devolvía `None` en las celdas de resultado (sin caché). Se copió el original al scratchpad y se recalculó con LibreOffice headless sobre la COPIA (`/Applications/LibreOffice.app/Contents/MacOS/soffice`). El original **no se tocó**. Todos los valores de este MD provienen del recálculo y fueron cruzados a mano contra el motor (columnas P/Q/R, S/T, BS de la hoja `Familias` y SUMIFS de `Datos Hechos`) — cuadran.

---

## 1. MÉTODO (de los dos HANDOFFs + SPEC)

### 1.1 Qué es este paquete y cómo evolucionó

Es la reestructura del **puente de venta (PVM) del segmento Privado** en **cinco conceptos**, no en el 2-vías clásico:

**Precio · Volumen · Mix (down-trading) · Lanzamientos 2026 · Gestión de Portafolio.**

Cadena de versiones:
- **v2** (cerrado, 6 rondas, aprobado): puente clásico ampliado a Precio/Volumen/Mix + Altas/Bajas/Valor-no-normalizado. Δ +31.3M, control 0, cobertura G5b 96.02%. **NO se re-abre**; v4 no tocó Precio/Volumen/Mix.
- **v3** (en pausa): agregó la partición de **Lanzamientos** y **Gestión de Portafolio**. Se pausó por dos conflictos materiales que exigían juicio de Rafael (ver 1.5).
- **v4** (ENTREGADO Y ADJUDICADO, 2026-07-15): resuelve los conflictos con decisiones de Rafael + agrega la **reclasificación nov-dic 2025 → ene 2026** de los lanzamientos, con **doble vista** (puente reclasificado como headline + conciliación al sell-in bruto del cubo). Auditoría Fable de 27 checks: **APROBADO** (26 OK + 1 discrepancia investigada y explicada al peso). Dos constructores independientes (Opus vía `make_v4_claude.py`; Codex vía pipeline `build_downtrading_v3.py`) convergen al mismo puente. Única puerta abierta: OK final de Rafael al artefacto.

### 1.2 Las cinco categorías del puente nuevo — qué es cada una

1. **Precio** — cambio de venta por precio dentro de **familias continuas no-lanzamiento** (mismo SKU/familia vende en H1-25 y H1-26). Efecto tarifario puro. **+392.9M**.
2. **Volumen** — cambio por unidades estándar dentro de familias continuas. **−169.7M**.
3. **Mix / down-trading** — cambio por **recomposición interna** de la familia hacia SKUs de distinto precio por unidad estándar (marca de visita médica → genérico de impulso). Descomposición **Shapley exacta** precio/volumen/mix sobre familias continuas. **−197.9M**. Es el corazón del reporte: la caída de valor **no es tarifaria**.
4. **Lanzamientos 2026** — venta de los productos que Rafael declaró como lanzamientos del año (lista autoritativa), medida como sell-in del cubo. **+71.1M** (reclasificado) / **+43.8M** (flujo genuino H1-26 sin reclasificación).
5. **Gestión de Portafolio** — todo lo demás del movimiento de altas/bajas que **no** es lanzamiento ni familia continua: **bajas/discontinuaciones + sustituciones/recodificaciones (altas no-lanzamiento) + valor no normalizado/servicios**. **−37.8M**.

Δ Venta Privado = Precio + Volumen + Mix + Lanzamientos + Gestión. Control = suma − Δ = 0.

### 1.3 Cómo se asigna cada material/molécula a categoría

- **Familia** = agrupación determinista `molécula_key | unidad_estándar | familia_id`, construida con Parent + fuzzy match + sucesión documental (hoja `Datos Familias`). Una familia es **continua** si tiene venta en ambos semestres (columna `Continua`=1). Sobre las continuas corre el Shapley (Precio/Volumen/Mix).
- **Unidad estándar / normalización**: maestro de unidades v2 (`unit_master_v2.csv`, hoja `Datos Maestro`) asigna a cada material `factor_total`, `unidad_estandar` y `confianza` (alta/baja/na). El down-trading solo es medible donde el volumen se puede normalizar a una unidad común (mg, ml, etc.). Regla de cobertura **G5b**: valor bruto-positivo normalizado / base bruta-positiva elegible = **96.02%**.
- **Lanzamiento**: flag `es_lanzamiento` puesto a mano desde la **lista autoritativa de Rafael** (verdad comercial de "qué es lanzamiento"). Un material es lanzamiento solo si hay **identidad nativa inequívoca** (texto del cubo) **y** aproxima el objetivo H1-26 de Rafael. Residuales > $0.25M quedan **abiertos** (no se fuerza el match). 13 materiales quedaron flagueados con venta.
- **Gestión de portafolio** = el complemento: altas que **no** son lanzamiento (SKUs nuevos de moléculas existentes, recodificaciones), bajas/discontinuaciones, y Δ de valor no normalizable (servicios, materiales sin factor).

### 1.4 Qué resuelve esta vista contra el PVM 2-vías clásico

El **2-vías clásico** (referencia global PiSA: volumen −830.7M / precio+mezcla +1,070.0M, piezas −5.1%) colapsa **precio y mezcla en un solo término** y no separa lanzamientos ni gestión de portafolio. No puede ver el **down-trading**: dentro de "precio+mezcla" positivo se esconde que la mezcla interna está **destruyendo −197.9M** de valor (marca cede a genérico propio) mientras el precio de lista sube +392.9M. Esta vista de 5 conceptos:
- **Aísla el down-trading (Mix −197.9M)** como fenómeno propio, con franquicias culpables y mecanismo.
- **Separa el crecimiento inorgánico (Lanzamientos +71.1M)** del orgánico.
- **Aísla el ruido de gestión de portafolio (−37.8M)**: recodificaciones y bajas que ensucian la comparación año-contra-año.

### 1.5 Los conflictos que se resolvieron (juicio de Rafael)

1. **Votripax-L NO es lanzamiento 2026.** El cubo lo muestra vendiendo desde feb-2025 (H1-25 $18.0M; H2-25 $9.1M; H1-26 $10.9M → contribución **−$7.1M**). Es base continua declinante, no lanzamiento. **Decisión Rafael: fuera de Lanzamientos**; su −$7.1M vuelve a Volumen/Mix (como en v2). (Materiales 4040348, 4040349.) OJO: este "Votripax-L" es distinto de **"Votripax B+L"** (material 4051538), que SÍ es lanzamiento 2026 (+$8.47M H1-26). No confundir.
2. **El pivote de $96M de Rafael ≠ sell-in del cubo.** La lista original traía una columna "Vta Ene-Jun 26" con Grand Total ~$96M all-channel. Diagnóstico: esa columna es **acumulado life-to-date (FY25 + H1-26)**, no flujo del semestre ni otra fuente. **Decisión Rafael: abandonar el pivote de $96M**; el puente usa **solo sell-in del cubo**. Cuidar en comunicación: no citar $96M como venta del semestre.
3. **Agrifen Lub (reto resuelto):** Agrifen Lub = **AGUA DE MAR** (materiales 4059190/4059191, $0.84M flujo Privado H1-26), distinto de **Agrifen tabletas = CLORFENAMINA COMPUESTA** (~$100M, base continua, jamás lanzamiento). El "$7.37M" de la lista de Rafael era **acumulado life-to-date**, no flujo del semestre.
4. **Los 11 lanzamientos se mantienen JUNTOS** (no se parten en nuevos-2026 vs continuación-2025): la venta 2025 fue **adelanto de cierre** del lanzamiento 2026.

### 1.6 La reclasificación nov-dic 2025 → ene 2026 (el cambio nuevo del v4)

Los lanzamientos facturaron **$27.3M de venta de cierre en nov-dic 2025** (adelanto). Rafael instruyó **reclasificarla a ene-2026** porque corresponde al lanzamiento de ese año. **Alcance: SOLO lanzamientos** (los continuos venden en ambos H1 y su patrón de cierre se cancela en la comparación; los lanzamientos no tenían H1-25). Efecto: sube Lanzamientos de +43.8M a **+71.1M** y la Δ Privado de +31.3M a **+58.7M**.

**Doble vista obligatoria (decisión Rafael):**
- **Headline:** puente reclasificado, **Δ +58.7M**.
- **Conciliación:** Δ reclasificada +58.7M − reclasificación 27.3M = **sell-in bruto del cubo +31.3M** (lo que audita contra la fuente oficial).

**ADVERTENCIA DE COMUNICACIÓN (del handoff):** la Δ reclasificada **+58.7M NO es el crecimiento sell-in oficial del semestre**. Quien audite contra el cubo debe pasar por la conciliación (−27.3M). No citar +58.7M como "crecimiento sell-in" sin la nota. **Para amarrar al storyline v5 (Retail +0.4% vs 1S25), el número que conecta es el sell-in bruto +31.3M, no +58.7M.**

### 1.7 Roles y reglas de construcción (regla de Rafael)

Fable dirige/adjudica/verifica; Codex Sol xhigh construye. Fable nunca construye entregables. Los Excel se entregan **formulados** (fórmulas sobre datos originales), nunca valores pegados. Método Mix = **Shapley exacto** sobre familias continuas no-lanzamiento. SPEC v2.4 congelada (constitución del modelo, no re-derivar reglas).

---

## 2. NÚMEROS FINALES DEL PRIVADO — el puente v4 completo

**Puente v4 reclasificado (Privado = Farmacias+Impulso+Expansión, Ene–Jun 2026 vs Ene–Jun 2025, MXN M):**

| Componente del puente | $M | Nota |
|---|---:|---|
| Precio | **+392.949** | familias continuas; excluye lanzamientos; = v2/v3 exacto |
| Volumen | **−169.710** | familias continuas; excluye lanzamientos; = v2/v3 exacto |
| Mix / down-trading | **−197.899** | familias continuas; excluye lanzamientos; = v2/v3 exacto |
| Lanzamientos 2026 (reclasif. nov-dic 25 → ene 26) | **+71.136** | flujo genuino +43.829 + reclasif +27.307 |
| Gestión de Portafolio | **−37.822** | ver desglose abajo |
| **Δ Venta neta Privado (reclasificada)** | **+58.654** | headline |
| Control (suma del puente − Δ) | **−0.0000000000006** | ≈ 0 ✓ |

Suma verificada: 392.9498 − 169.7100 − 197.8992 + 71.1360 − 37.8222 = **58.6544** ✓.

**Desglose de Gestión de Portafolio (−37.822M):**

| Sub-componente | $M |
|---|---:|
| Bajas / discontinuaciones | **−106.637** |
| Sustituciones / recodificaciones (altas no-lanzamiento) | **+106.863** |
| Valor no normalizado / servicios | **−38.048** |
| **Total Gestión** | **−37.822** |

**Conciliación al sell-in bruto del cubo (filas 36–38 del Resumen):**

| Vista | $M |
|---|---:|
| Δ Venta Privado (reclasificada) | **+58.654** |
| (−) Reclasificación nov-dic 2025 de lanzamientos | **−27.307** |
| **(=) Δ Venta Privado, sell-in bruto del cubo** | **+31.347** |

**Sensibilidad del Mix (robustez del down-trading):**
- (i) Todo el maestro: **−197.899M**
- (ii) Sin confianza baja: **−197.899M** (idéntico → la baja confianza no mueve el Mix)
- (iii) Solo confianza alta: **−144.380M** (piso composicional; NO es piso de intervalo)

**Cobertura de normalización (G5b):** **96.0178%** = valor bruto-positivo normalizado / base bruta-positiva elegible. Base bruta-positiva elegible = **$15,351.13M**.

**Down-trading — Top 5 franquicias (Mix Ene–Jun 26 vs 25, $M):**

| # | Franquicia | Mix $M |
|---|---|---:|
| 1 | ÁCIDO CLAVULÁNICO + AMOXICILINA | **−45.575** |
| 2 | LEVOFLOXACINO | **−32.946** |
| 3 | CEFTRIAXONA | **−24.743** |
| 4 | ENOXAPARINA DE SODIO | **−21.296** |
| 5 | FEXOFENADINA | **−15.860** |
| | **Suma top-5 (≈71% del Mix total)** | **−140.420** |

**Universo Privado del modelo (materiales con MATNR):** V25 **$7,176.83M** → V26 **$7,208.18M**, Δ **+31.347M** (+0.44%).

---

## 3. HOJA POR HOJA DEL EXCEL

Archivo: `Downtrading_Privado_v4_FINAL_2026-07-15.xlsx` — 8 hojas. sha256[:16] `d5927374d14cc3de`.

### Hoja 1 — `Resumen Ejecutivo` (38 filas × 2 col)
Título interno dice "v3" (heredado; el contenido es v4). Contiene el puente completo, desglose de gestión, sensibilidad del Mix, cobertura G5b, top-5 franquicias y conciliación. **Todos los valores de la Sección 2 vienen de aquí.** Estructura de filas:
- Filas 4–11: Descomposición del cambio (Precio, Volumen, Mix, Lanzamientos, Gestión, Δ reclasificada, Control).
- Filas 13–16: Detalle de Gestión (bajas, sustituciones, valor no normalizado).
- Filas 18–21: Sensibilidad del Mix (i/ii/iii).
- Filas 23–25: Cobertura G5b (%) + base elegible $M.
- Filas 27–32: Top 5 franquicias down-traders (nombre por INDEX/MATCH a `Ranking Franquicias`; Mix por columna M).
- Fila 34: nota de fuente/método (Shapley exacto).
- Filas 35–38: Conciliación al sell-in bruto.
Fórmulas apuntan a `Familias` (P/Q/R = Precio/Vol/Mix; S/T/BS con filtros AT/BO = altas/bajas/gestión; BK/BM = cobertura), a `Datos Hechos` (SUMIFS por es_lanzamiento y reclasif) y a `Ranking Franquicias`.

### Hoja 2 — `Datos Hechos` (3120 filas × 10 col; 3,114 filas de material)
Hechos fuente por material, Privado, H1-25 y H1-26. Columnas: `matnr · descripción · molécula · V25 · U25 · V26 · U26 · Bruto positivo · es_lanzamiento · reclasif_novdic25`. Es el insumo de las SUMIFS de lanzamientos y reclasificación. **13 materiales con es_lanzamiento=1** (todos con V26>0). **9 materiales con reclasif_novdic25 > 0** (los demás = 0).

Materiales de lanzamiento (V26 H1-26 Privado y reclasif nov-dic 25, $M):

| Material | Descripción | Reclasif nov-dic 25 $M |
|---|---|---:|
| 4059190 | IMP PT AGRIFEN LUB ACTIVE 100ML | 3.365 |
| 4059191 | IMP PT AGRIFEN LUB ACTIVE INFANTIL 50ML | 3.169 |
| 4060617 | NARIVITAE 2MG/ML C/120ML SOOR (Rivastigmina) | 6.491 |
| 4060615 | MEDONEVITAE 10MG/10MG C/30 TAB (Donepezilo+Memantina) | 2.572 |
| 4060616 | MEDONEVITAE 10MG/20MG C/30TAB (Donepezilo+Memantina) | 3.229 |
| 4059186 | PISALAK LIPIGO 1000MG C/45SOB | 5.310 |
| 4063428 | PISAGOT-TRIPLE 2/20/5MG C/5ML SOOF (Brimo+Dorzo+Timo) | 2.548 |
| 4058392 | PISALAK FORTE 1,000MUFC/5MG 30CAP | 0.460 |
| 4045578 | PIXIBA 40MG C/2FAMP D/2ML (Parecoxib) | 0.162 |
| | **Suma reclasificación** | **27.307** |

Lanzamientos: V25 = **$0.0M** (no vendían en H1-25), V26 flujo genuino H1-26 Privado = **$43.829M**, + reclasif **$27.307M** = contribución **+$71.136M**. Universo total del modelo (todos los materiales): V25 $7,176.83M, V26 $7,208.18M, Δ +31.347M.

### Hoja 3 — `Datos Lanzamientos` (33 filas × 21 col)
Lista autoritativa 2026 con material nativo + venta H1 por segmento. **Aquí vive la reconciliación producto→material→segmento y las exclusiones controladas.** Columnas: `Producto Rafael · Material · Descripción cubo · Molécula nativa · Marca · Forma · Presentación · es_lanzamiento · Estado match · Venta 2025 FY all-channel $M · Venta H1-25 all-channel $M · Vta H1-26 Privado $M · Vta H1-26 Hospitales $M · Vta H1-26 Gobierno $M · Vta H1-26 Otros $M · Vta H1-26 material total $M · Objetivo Rafael H1-26 $M · Residual vs objetivo $M · Contribución Privado H1 26-25 $M · H1-25 ≈ 0 · Conclusión de grounding`.

**11 lanzamientos con material + venta (filas 5–17), Vta H1-26 Privado $M y objetivo Rafael:**

| Producto | Material | Molécula/Marca | H1-26 Privado $M | H1-26 material total $M | Objetivo Rafael $M | Estado match |
|---|---|---|---:|---:|---:|---|
| Parecoxib | 4045578 | PARECOXIB / PIXIBA C | 0.745 | 16.295 (Hosp 15.549) | 16.3 | CERRADO |
| Sitagliptina+Metformina | 4065807 | SITAGLIPTINA / SITAGLIPTINA METFOR | 4.269 | 4.269 | 4.3 | CERRADO |
| Donepezilo+Memantina | 4060615 | MEDONEVITAE 10/10 | 3.540 | 3.540 | 13.1 (combo) | PARCIAL |
| Donepezilo+Memantina | 4060616 | MEDONEVITAE 10/20 | 3.722 | 3.722 | — | PARCIAL |
| Pisalak Lipigo | 4059186 | PROBIOTICO / PISALAK | 2.455 | 2.455 | 2.5 | CERRADO |
| Votripax B+L | 4051538 | COMPLEJO VIT B + LIDOCAINA | 8.470 | 8.470 | 8.5 | CERRADO |
| Agrifen Lub | 4059190 | AGUA DE MAR / AGRIFEN 100ML | 0.610 | 0.610 | 7.4 | PARCIAL |
| Agrifen Lub | 4059191 | AGUA DE MAR / AGRIFEN 50ML | 0.225 | 0.225 | — | PARCIAL |
| Ertapenem | 4053192 | ERTAPENEM / PRAGMA C | 1.688 | 5.645 (Hosp 3.957) | 5.6 | CERRADO |
| Sitagliptina | 4055104 | SITAGLIPTINA / SITAGLIPTINA C | 12.021 | 12.021 | 12.0 | CERRADO |
| Pisalak Forte | 4058392 | PROBIOTICO / PISALAK | 0.815 | 0.815 | 0.8 | CERRADO |
| Brimo+Dorzo+Timo | 4063428 | BRIMONIDINA+DORZOLAMIDA+TIMOLOL / PISAGOT | 4.486 | 4.640 (Gob 0.154) | 7.0 | PARCIAL |
| Rivastigmina | 4060617 | RIVASTIGMINA / NARIVITAE | 0.782 | 0.782 | 7.3 | PARCIAL |

Suma H1-26 Privado de los 11 con material ≈ **$43.83M** (= flujo genuino de lanzamientos). Nota: Parecoxib y Ertapenem son mayormente **Hospitales** ($15.5M + $3.96M), fuera del alcance Privado.

**7 lanzamientos ABIERTOS (filas 18–24), objetivo cero, sin material inequívoco, $0 impacto H1-26:** Tadalafil, Tadalafil Inorg, Vitamina A/C/D, Naproxeno, Azitromicina, Oseltamivir, Combesteral. "Sin impacto H1-26; no se forzó un match por nombre."

**Exclusiones controladas (filas 27–31):**

| Material | Descripción | Identidad | H1-25 $M | H1-26 Privado $M | Decisión |
|---|---|---|---:|---:|---|
| 4067443 | PISALAK 6000 MILL UFC 7FCO 1+1 CORTESIA | Probiótico 6000, no Lipigo/Forte | 0 | 15.691 | **EXCLUIDO** |
| 4064785 | OXITAL C 1000MG C/10 TAB EFE IMPULSO | Vitamina C, no A/C/D | 0 | 2.574 | **EXCLUIDO** |
| 4013772 | VITAMINA A/C/D C/15ML SOOR PHARM GE | A/C/D existente, target=0 | 0.125 | 0.095 | **NO ATRIBUIDO** |

(Nota de método en la hoja: el match exige identidad nativa + aproximación al objetivo de Rafael; residuales >$0.25M quedan abiertos.)

### Hoja 4 — `Datos Maestro` (3121 filas × 20 col)
Maestro de unidades v2 completo, una fila por material. Columnas: `matnr · desc · molecula · clase · factor_conteo · fuente_conteo · contenido_unitario · unidad_contenido · fuente_contenido · factor_total · unidad_estandar · confianza · notas · no_sumable · flag_unidad_mixta · flag_cuarentena_g6 · flag_en_salida_operativa · flag_fuera_de_segmento · override_manual · es_lanzamiento`. Es la base de normalización a unidad estándar (mg/ml/etc.) y de la confianza que alimenta la sensibilidad del Mix y G5b. Materiales no clasificables (VARIOS/NO_CLASIFICADO) marcados `no_sumable=1`, `confianza=baja`.

### Hoja 5 — `Datos Familias` (3121 filas × 23 col)
Mapa determinista material → familia (Parent + fuzzy + sucesión documental). Bloque principal (A–I): `matnr · familia_id · origen_arista · molécula_key · unidad_estándar · familia_key · normalizado · confianza · descripción`. Bloque auxiliar (K–N): catálogo `familia_key/familia_id/molécula_key/unidad_estándar`. Columna P: lista de "moléculas con familias continuas". Bloque R–W: aristas fuzzy documentadas (`origen · destino · score · molécula · método · tipo`), p.ej. score 0.82 exacto/Fuzzy. Es la trazabilidad de por qué dos SKUs caen en la misma familia.

### Hoja 6 — `Familias` (3121 filas × 71 col) — EL MOTOR
Una fila por familia (bloque de cálculo filas 5–1986, **1,982 familias con key; 1,537 continuas**) más un bloque material-nivel (columnas AU en adelante, hasta fila 3119). Columnas clave (letra = encabezado):
- `E Q25 · F Q26 · G V25 · H V26 · I Continua · J Pool Q25 · K Pool Q26 · L p0 · M p1 · N s0 · O s1` → insumos Shapley.
- **`P Precio · Q Volumen · R Mix`** → los tres componentes por familia (suma /1e6 = 392.9 / −169.7 / −197.9).
- **`S Altas · T Bajas`** → gestión (se filtran por `AT es_lanzamiento_familia`=0).
- `U–AF` = variante (ii) sin confianza baja; `AG–AR` = variante (iii) solo confianza alta (Mix ii/iii de la sensibilidad).
- `AS Control fila · AT es_lanzamiento_familia`.
- `AU–BN` = bloque material: `matnr · familia_key · molécula · unidad · factor_total · confianza · no_sumable · Elegible(i/ii/iii) · V25/U25/V26/U26/Q25/Q26 · Bruto positivo(BK) · Δ valor no normalizado(BL) · Elegible base G5b(BM) · Descripción`.
- `BO es_lanzamiento · BP–BR Elegible puente v3 · BS Δ valor gestión portafolio`.
Verificación de agregados (recalc): Precio +392.95, Volumen −169.71, Mix −197.899; Altas(AT=0) +106.863; Bajas(AT=0) −106.637; Δ valor gestión(BO=0) −38.048. Todos cuadran con el Resumen.

### Hoja 7 — `Ranking Franquicias` (243 filas × 23 col)
Precio/volumen/mix por molécula, ordenado por down-trading. Dos tablas: (A–H) por molécula `Molécula · Precio $M · Volumen $M · Mix $M · # SKUs norm. · Bruto $M · Mix(ii) · Mix(iii)` (**237 moléculas**); (J–S) misma info con scores de ranking (`Score down`, `Score |Mix|`); (U–W) `Rank · Molécula top |Mix| · |Mix| $M`. Top-25 down-traders (Precio / Volumen / Mix $M):

| Molécula | Precio | Volumen | Mix | #SKUs | Bruto $M |
|---|---:|---:|---:|---:|---:|
| ÁCIDO CLAVULÁNICO + AMOXICILINA | 2.90 | 68.41 | −45.58 | 55 | 403.4 |
| LEVOFLOXACINO | −4.79 | 0.19 | −32.95 | 20 | 154.0 |
| CEFTRIAXONA | −19.22 | −8.85 | −24.74 | 52 | 690.8 |
| ENOXAPARINA DE SODIO | 16.26 | 13.91 | −21.30 | 8 | 207.3 |
| FEXOFENADINA | 3.07 | 33.73 | −15.86 | 22 | 156.1 |
| INSULINA GLARGINA | 18.33 | 27.97 | −12.62 | 22 | 355.6 |
| ARIPIPRAZOL | −0.04 | 16.38 | −12.17 | 13 | 52.9 |
| INSULINA HUMANA ISOFANA | 3.18 | 1.74 | −10.01 | 18 | 170.1 |
| HIDROCLOROTIAZIDA + TELMISARTAN | 6.01 | 42.08 | −8.49 | 20 | 256.8 |
| PANTOPRAZOL | −3.31 | 4.46 | −8.02 | 48 | 204.2 |
| COMPLEJO VIT B + DEXAMETASONA (+...) | 0.50 | −13.28 | −7.88 | 16 | 250.2 |
| CEFALEXINA | 8.46 | 2.21 | −7.60 | 18 | 166.4 |
| CIPROFLOXACINO | 5.55 | 3.55 | −7.30 | 22 | 121.3 |
| CLINDAMICINA | 1.38 | 8.07 | −6.95 | 26 | 107.2 |
| KETOROLACO | 0.38 | 5.77 | −6.89 | 29 | 181.3 |
| MOMETASONA | −0.78 | 1.07 | −5.73 | 11 | 87.6 |
| DONEPECILO | 2.33 | 4.49 | −5.24 | 4 | 56.0 |
| CIPROFIBRATO | 0.71 | 5.26 | −5.17 | 5 | 39.0 |
| PROBIOTICO | 1.03 | 0.76 | −4.80 | 9 | 80.6 |
| MEMANTINA | 1.19 | 9.85 | −4.48 | 20 | 102.0 |
| AMIKACINA | 4.90 | −12.12 | −3.68 | 29 | 120.1 |
| COMPLEJO VIT B + DICLOFENACO | −0.99 | −3.85 | −3.64 | 15 | 51.1 |
| ZOLMITRIPTAN | 0.67 | 5.50 | −3.46 | 7 | 16.8 |
| SOLUCION CS | 11.38 | 17.91 | −3.26 | 12 | 498.1 |
| ROSUVASTATINA | −2.58 | 16.88 | −3.21 | 25 | 138.0 |

**Up-traders (Mix positivo, valor defendido vía mezcla):** FRISO **+16.43** (Precio +55.54 / Vol −82.94), BUDESONIDA +8.67, METFORMINA +7.47, FLEBOTEK +6.57, ELECTROLITOS ORALES +6.44, PREGABALINA +5.99, LEVETIRACETAM +5.89, ETORICOXIB +5.27.

### Hoja 8 — `Detalle Top Franquicias` (3121 filas × 14 col)
Detalle SKU por SKU del top-20 por |Mix|; precios por unidad estándar. Columnas: `Molécula · Rank |Mix| · Material · Descripción · Familia · Unidad · Factor total · Venta 25 $M · Venta 26 $M · Q25 estándar (M) · Q26 estándar (M) · $/unidad 25 · $/unidad 26 · Confianza`. Es la evidencia granular del down-trading (marca cara vs genérico barato en $/unidad estándar dentro de la misma molécula). Ejemplo Amox/Clav: AMOXICLAV PED (mat 4000231) $2.13→$2.37 por ml; el desplome de valor viene de la recomposición hacia SKUs baratos, no del precio de lista.

---

## 4. INSIGHTS DEL MD FINAL (completos)

Fuente: `INSIGHTS_Downtrading_Privado_v4_FINAL.md` (entregado; `.docx` gemelo).

**Título / tesis:** "La Δ reclasificada es +$58.7M; los lanzamientos 2026 aportan +$71.1M." El cambio de venta de Privado cerró en **+$58.7M** en Ene–Jun 2026 vs Ene–Jun 2025. Lanzamientos +$71.1M; gestión de portafolio absorbió −$37.8M.

**Tabla del puente:** Precio +392.9 · Volumen −169.7 · Mix −197.9 · Lanzamientos (reclasif) +71.1 · Gestión −37.8 · **Δ Venta Privado +58.7** · Control −0.000000.

**Nota de método (verbatim del insight):** los lanzamientos facturaron $27.3M de venta de cierre en nov-dic 2025 (adelanto); se reclasifican a Ene 2026 por corresponder al lanzamiento de ese año. La Δ reclasificada (+$58.7M) concilia con el sell-in bruto del cubo (+$31.3M) por ese mismo monto.

**Conciliación al sell-in bruto:** +58.7 − 27.3 = **+31.3M** (Δ sell-in bruto del cubo).

Composición de gestión de portafolio: bajas/discontinuaciones **−$106.6M**, sustituciones/recodificaciones **+$106.9M**, valor no normalizado/servicios **−$38.0M**.

**Insight 2 — "El down-trading de Privado permanece material: −$197.9M en el semestre."** El componente de mezcla es −$197.9M. La caída de valor **no es tarifaria**: el precio dentro de familias continuas aporta +$392.9M, el volumen resta −$169.7M y la mezcla resta −$197.9M.

**Insight 3 — "Cinco franquicias concentran el grueso del down-trading."** Amox/Clav −45.6 · Levofloxacino −32.9 · Ceftriaxona −24.7 · Enoxaparina −21.3 · Fexofenadina −15.9 → suma **−$140.4M = 71% del total**. Mecanismo común: la marca de visita médica cede volumen al genérico de impulso. **Caso tipo Ceftriaxona:** Cefaxona ($0.21 por mg) pasó de $64.8M a $41.4M de venta (−36%); su participación en miligramos de la molécula bajó de 1.9% a 1.2%; los genéricos del portafolio (AMCEF y Ceftriaxona genérica, $0.017–0.020 por mg) sostienen el volumen. La migración ocurre **dentro del portafolio propio**: el peso que pierde la marca lo captura el genérico de la casa **a una doceava parte del precio por miligramo**.

**Insight 4 — "FRISO migra hacia arriba: +$16.4M de mezcla positiva."** FRISO es la franquicia grande con mezcla en sentido contrario: +$16.4M. El volumen se desplaza hacia variantes especializadas de mayor precio por gramo (Comfort, AR, etapas superiores). Defiende valor **vía mezcla, no vía precio de lista**.

**Insight 5 — recomendación: "La palanca es defender la mezcla y disciplinar la gestión de portafolio."** Las cinco franquicias down-trader son la lista de trabajo inicial: defensa de marca de visita médica, surtido y condiciones por canal, arquitectura de precios del genérico propio. Gestión de portafolio requiere un segundo frente: completar la trazabilidad de lanzamientos por material y separar recodificaciones de discontinuaciones antes del siguiente cierre.

**Pie de página del insight (verbatim):**
- Alcance: segmento Privado (Farmacias, Impulso, Expansión), Ene–Jun 2025 vs Ene–Jun 2026, sell-in neto.
- Nota técnica: Votripax-L no se clasificó como lanzamiento porque ya vendía $18.0M en H1-2025; es base continua, cae −$7.1M y permanece en Volumen/Mix.
- El 96.0% del valor bruto-positivo conserva unidades normalizadas bajo la definición G5b del v2.
- Fuente: Sell-In-2023-2026-Cierre-JUN.xlsx; Diccionario_PISA_SKUs.csv; Downtrading_Privado_v4_FINAL_2026-07-15.xlsx.

---

## 5. CÓMO SE CONECTA ESTA VISTA A LAS CASCADAS POR SEGMENTO DEL DECK

- **El segmento del deck que ilumina es Retail (43.6% de la venta)** = el "Privado" de este paquete (Farmacias + Impulso + Expansión). Es la **única cascada de segmento ya construida a nivel de puente PVM**; Gobierno FC / Hospitales / Servicios están en construcción con la misma maquinaria (boot: SPEC v2.4 §9/§10).
- **Amarre de crecimiento:** el storyline v5 reporta Retail **+0.4% vs 1S25** y venta **$7,210.2M** (92.3% de meta). El modelo entrega Privado V26 **$7,208.2M** con Δ **+31.3M (+0.44%)** en la vista **sell-in bruto**. Para el deck, la cascada de Retail debe usar la vista **sell-in bruto (+31.3M)** para que cuadre con el +0.4% y con la referencia; la vista reclasificada (+58.7M) es analítica interna, no el crecimiento reportado.
- **Qué aporta al deck sobre el 2-vías clásico:** descompone el "+0.4% plano" de Retail en su física real — precio de lista sube fuerte (+392.9M) pero se lo comen down-trading (−197.9M) y volumen (−169.7M); el crecimiento neto lo sostienen los lanzamientos (+71.1M reclasif / +43.8M genuino). Es el material para una lámina de "por qué Retail crece poco pese a subir precios" y otra de "down-trading: la marca cede al genérico propio".
- **Riesgo de mensaje (crítico):** no citar +58.7M como crecimiento sell-in; usar +31.3M para cualquier cifra que se cruce con el cubo o con la referencia de segmentos.
- **Composición Retail de referencia** (para cruzar): Farmacias 2,958.0 + Impulso 2,785.8 + Expansión 1,466.4 = 7,210.2M. El modelo no desglosa el puente por sub-canal (solo Privado agregado).

---

## 6. INCONSISTENCIAS INTERNAS

1. **Título de la hoja `Resumen Ejecutivo` dice "v3"** ("Resumen Ejecutivo — Down-trading Privado v3") aunque el contenido y las cifras son v4 (incluyen Lanzamientos reclasificados +71.1 y conciliación). Cosmético, pero puede confundir en una revisión rápida. Igual la etiqueta interna de columnas del motor usa "puente v3" (BP–BR).
2. **Objetivo Rafael de Donepezilo+Memantina ($13.1M combo) vs sell-in del cubo ($3.54+$3.72 = $7.26M):** residual abierto $5.84M declarado como "no asignado a materiales débiles". No es error del puente (usa solo lo matcheado), pero el objetivo de Rafael queda muy por encima del sell-in. Igual Rivastigmina (objetivo $7.3M vs cubo $0.78M, residual $6.52M) y Agrifen Lub (objetivo $7.4M vs cubo $0.84M, residual $6.57M): 4 lanzamientos "PARCIAL" con residual grande sin cerrar.
3. **Δ exacta con micro-diferencias de redondeo entre docs:** el insight MD reporta Δ +58.7 y conciliación +31.3; el Excel recalculado da +58.6543 y +31.3470. El HANDOFF cita "sell-in bruto +31.35" y "+31.347". Consistentes al redondeo; solo cuidar que el deck no mezcle +31.3 vs +31.35 como si fueran fuentes distintas.

---

## 7. POSIBLES CHOQUES CON LA REFERENCIA SELL-IN (solo flagear; no resolver)

1. **Venta Retail/Privado H1-26:** referencia = **$7,210.2M**; modelo (universo con MATNR) = **$7,208.2M**. Diferencia **≈ $2.0M**. Nota: el audit Fable F6 atribuye un gap de **+$0.413M** en la *Δ* a las filas del canal FLP sin MATNR (V26H1 ≈ $2.08M) — que son exclusión estructural del modelo desde v2; sumadas al V26 del modelo ($7,208.2M + $2.08M ≈ $7,210.3M) casi reconcilian con la referencia. Flag: el modelo excluye estructuralmente ~$2M de FLP sin material.

2. **Crecimiento Retail vs 1S25:** referencia = **+0.4%**; modelo vista sell-in bruto = **+31.347M / 7,176.83M = +0.44%**. Coherentes. Pero la vista **headline del entregable es +58.7M (reclasificada)**, que implicaría ~+0.8% — **no** es el +0.4% de la referencia. Choque de comunicación si alguien toma el headline: el crecimiento oficial del segmento es el bruto (+31.3M / +0.4%), no el reclasificado.

3. **Δ bruta del universo Privado completo:** el audit Fable (F6) señala que la Δ del universo Privado **completo del cubo = +31.760M**, no +31.347M; gap **+$413,102.22 exactos** = filas del canal **FLP sin MATNR**. Es exclusión estructural (sin material no hay llave física), no error del v4. Flag para el deck: si se cita "Retail +X M" contra el cubo crudo, el número del cubo puede ser +31.8M vs +31.3M del modelo.

4. **PVM 2-vías clásico (referencia global 5 mercados):** volumen −830.7M / precio+mezcla +1,070.0M, piezas −5.1%. Esta vista descompone **solo Privado** en Precio +392.9 / Volumen −169.7 / Mix −197.9 (+ lanzamientos + gestión). **No hay en este paquete el corte Privado-solo del 2-vías clásico**, así que no se puede cruzar término a término; solo se puede decir que este método reparte el "precio+mezcla" del clásico en Precio/Mix separados. Flag: no sumar/comparar directamente los −830.7 / +1,070.0 globales contra los componentes Privado sin antes aislar Privado en el 2-vías.

5. **Alcance segmento:** referencia usa "Retail 43.6%"; el paquete lo llama "Privado = Farmacias+Impulso+Expansión". Se asumen equivalentes (y las tres sub-líneas de la referencia suman 7,210.2M = Retail). Flag menor de nomenclatura: confirmar que "Retail" del deck ≡ "Privado" del modelo (no incluye otro canal).

---

## 8. VACÍOS DECLARADOS

1. **Celdas de resultado sin caché en el original:** todas las fórmulas del `_FINAL.xlsx` devolvían `None` con openpyxl `data_only` (sin valores cacheados). Los números de este extract provienen del **recálculo LibreOffice sobre una COPIA**; el original nunca se abrió/modificó. Si se abre en Excel y recalcula, deben coincidir, pero **el original entregado no trae valores materializados**.
2. **Residuales de lanzamientos PARCIAL no cerrados** (declarados abiertos en la propia hoja): Donepezilo+Memantina $5.84M, Rivastigmina $6.52M, Agrifen Lub $6.57M, Brimo+Dorzo+Timo $2.36M. "El residual no se asignó a materiales débiles." Trazabilidad de lanzamientos por material incompleta (lo dice el propio insight 5).
3. **7 lanzamientos ABIERTOS sin material** (Tadalafil, Tadalafil Inorg, Vitamina A/C/D, Naproxeno, Azitromicina, Oseltamivir, Combesteral): objetivo cero, $0 impacto H1-26, sin match forzado. No aportan al puente pero quedan sin identidad en el cubo.
4. **Puente por sub-canal ausente:** el modelo entrega Privado agregado; **no** descompone Precio/Volumen/Mix/Lanzamientos/Gestión por Farmacias vs Impulso vs Expansión. Si el deck quiere la cascada por sub-canal de Retail, no existe todavía.
5. **Gobierno FC, Hospitales, Servicios NO construidos** en esta maquinaria de 5 conceptos. Solo Privado/Retail está terminado. Los otros tres segmentos del deck (24.4% / 18.5% / 13.4%) tendrán que llevar otra fuente de puente o esperar la extensión v1.1.
6. **Exclusión estructural FLP sin MATNR** (~$2.0M de venta H1-26, +$0.413M de Δ): fuera del modelo por diseño desde v2; no hay llave física para incorporarlo.
7. **Pivote $96M abandonado:** ya no se refleja ninguna fuente sell-out / plan / PIN en el paquete; el puente es 100% sell-in del cubo. Si el deck quiere contrastar sell-in vs sell-out de lanzamientos, ese dato no está aquí.
8. **Pendiente exógeno menor (no bloqueante, del handoff):** archivar en `v2/evidencia/` las fotos de empaque (BROSPINA, Glargina×2, Budesonida, Lincomicina, Ketorolaco) y la tabla T-Padre de tarimas — trazabilidad de 12 overrides documentales del v2. No afecta cifras.

---

*Extracción generada 2026-07-16. Archivos fuente en `/Users/rafaelprince/Downloads/PVM_Reconstruido_scripts/v2/`. Números verificados por recálculo LibreOffice sobre copia y cruce manual contra el motor `Familias`.*
