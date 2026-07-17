# HANDOFF — Reporte Down-trading Privado: línea de Lanzamientos 2026

**Proyecto:** PVM / Down-trading sell-in PiSA — reestructura del reporte Privado (Precio · Volumen · Mix · **Lanzamientos** · Gestión de portafolio).
**Fecha:** 2026-07-15.
**Estado en una línea:** el v3 formulado está construido y reconcilia (Δ +31.3, control 0), **EN PAUSA esperando UNA decisión de Rafael** sobre cómo tratar los lanzamientos; falta un ajuste de 2 líneas + verificación + entrega.

---

## LEE PRIMERO, EN ESTE ORDEN (no actúes antes)

1. **Este handoff** (completo).
2. **Memoria `project_pvm_downtrading.md`** — el proyecto base (v1 Privado CERRADO y entregado; cifras citables; roles).
3. **`APRENDIZAJES_y_metodo.md`** (misma carpeta) — el método y las trampas; sección "Lanzamientos 2026".
4. **`SPEC_PVM_UNIDADES_v2.md`** (v2.4, CONGELADA) — la constitución del modelo; no re-derives reglas.
5. **Tab "Datos Lanzamientos"** de `Downtrading_Privado_v3_FORMULADO.xlsx` + **`v3_launch_analysis.json`** — la reconciliación producto-por-producto ya hecha.
6. **`INSIGHTS_Downtrading_Privado_v3.md`** — borrador del reporte con la nueva estructura.

---

## LA DECISIÓN QUE DESTRABA TODO (pendiente exógeno — es de Rafael)

Rafael pidió partir el reporte en 5 conceptos: Precio · Volumen · Mix · **Lanzamientos 2026** · **Gestión de portafolio** (agregada arriba, detalle abajo). Dio una lista autoritativa de 19 lanzamientos con su "Vta Ene-Jun 26" (pivote all-channel, Grand Total $96M). Al aterrizarla en el sell-in del cubo surgieron **dos conflictos que necesitan su lectura antes de finalizar** (se le presentaron; falta su respuesta):

**Conflicto 1 — Votripax-L NO es lanzamiento 2026.** El cubo lo muestra vendiendo **desde febrero 2025**: H1-2025 = $18.0M, H2-2025 = $9.1M, H1-2026 = $10.9M. Su venta 2025 no fue "adelanto de diciembre" (está repartida en el semestre). En el puente Ene-Jun contribuye **−$7.1M (cae 40%)**: es base continua declinante, no un lanzamiento. Como "lanzamiento" saldría con signo negativo, engañoso.
→ **Recomendación de Fable:** sacarlo de Lanzamientos; su −$7.1M vuelve a la base continua (Volumen/Mix), que es como estaba en v2.

**Conflicto 2 — el pivote de Rafael ($96M) ≠ sell-in del cubo.** El puente se construye sobre sell-in. Los mismos productos en el cubo suman ~$74M all-channel matched; varios renglones del pivote superan el actual del cubo por mucho: Rivastigmina pivote $7.3M vs cubo $0.8M (solo NARIVITAE existe); Agrifen Lub pivote $7.4M vs cubo $0.8M (los ~$124M de "Agrifen" son las **tabletas existentes**, no el Lub); Donepezilo+Memantina pivote $13.1M vs cubo combo MEDONEVITAE $7.3M (los ~$61M de Memantina sola son **molécula existente**, no el combo lanzado). El pivote parece medir otra cosa (sell-out / plan / PIN), no sell-in.
→ **Recomendación de Fable:** Lanzamientos en el puente = **sell-in Privado ~$44M** (genuinos, sin Votripax-L), con **nota de reconciliación** al pivote de $96M (de los cuales ~$18M son hospital/gobierno — Parecoxib $15.5M, Ertapenem $4.0M — fuera del alcance Privado).

**Pregunta abierta a Rafael:** (a) ¿saca Votripax-L? (b) ¿Lanzamientos = sell-in cube ~$44M con nota al $96M, o su $96M sale de una fuente que sí quiere reflejar (y cuál)?

---

## SIGUIENTE PASO (exacto)

1. **Recibir la decisión de Rafael** sobre los dos conflictos de arriba.
2. **Instruir a Codex** el ajuste (2 líneas): (i) quitar el flag `es_lanzamiento` a los materiales de Votripax-L (`4040348`, `4040349`) → su −$7.1M regresa a familias continuas; (ii) confirmar Lanzamientos = sell-in Privado (SUMIFS sobre el flag). Regenerar el xlsx formulado + insights_v3 desde el script.
3. **Verificar de primera mano** (Fable dirige, no construye): recalc LibreOffice headless, control = 0, Δ +31.3, Precio/Volumen/Mix vuelven ≈ v2 (392.9/−169.7/−197.9 al restaurar Votripax-L a continua), Lanzamientos ≈ $44M, celdas = fórmulas.
4. **Entregar** v3 final a Rafael (Excel formulado + insights, solo-conclusiones).

---

## ESTADO CANÓNICO ACTUAL (verdad de hoy, en `~/Downloads/PVM_Reconstruido_scripts/v2/`)

| Archivo | Rol | Estado |
|---|---|---|
| `Downtrading_Privado_v3_FORMULADO.xlsx` | Entregable en curso (formulado, 8 tabs incl. Datos Lanzamientos) | **EN PAUSA** — reconcilia pero con Votripax-L mal clasificado |
| `INSIGHTS_Downtrading_Privado_v3.md/.docx` | Reporte de insights nueva estructura | Borrador; ajustar tras decisión |
| `build_downtrading_v3.py` | Generador del v3 (Codex) | Reproducible; editar el flag de lanzamientos aquí |
| `v3_launch_analysis.json`, `v3_launch_materials.csv` | Reconciliación producto→material→segmento | Auditados por Fable |
| `Downtrading_Privado_v2_FORMULADO.xlsx` | **Entregable v2 APROBADO** (respaldo) | Verde, verificado; NO tocar |
| `SPEC_PVM_UNIDADES_v2.md` (v2.4) | Constitución congelada | Verde; fuente de verdad |
| `unit_master_v2.csv`, `build_unit_master_v2.py`, `gates_v2.py` | Maestro de unidades + motor + gates | Verde; base del v2 y v3 |
| `Downtrading_Privado_v2.xlsx` | Excel v2 valores-pegados | **STALE** (superado por FORMULADO) |
| `REPORTE_downtrading_privado_v2.md` | Reporte técnico v2 | Verde (histórico) |

Roles del proceso (regla de Rafael): **Fable dirige/adjudica/verifica; Codex Sol xhigh construye.** Fable NUNCA construye entregables. Los Excel se entregan **formulados** (fórmulas sobre datos originales), nunca valores pegados de motor Python. Trampa del wrapper de Codex: lanza y devuelve control sin relevar resultado → vigila el archivo en disco, verifica ahí, no re-delegues (carrera de escritura). Ver [[feedback_codex_delegation_async]].

---

## NÚMEROS CLAVE (auditados; sell-in cubo Cierre-JUN, Privado, Ene-Jun 2026 vs 2025, MXN M)

**Puente v2 APROBADO (base, sin línea de lanzamientos):**
Precio **+392.9** · Volumen **−169.7** · Mix **−197.9** · Altas netas **+149.9** · Bajas netas **−106.6** · Valor no normalizado **−37.2** · **Δ +31.3** (control 0). Cobertura G5b 96.02%. Top-5 down-traders: Amox/Clav −45.6 · Levofloxacino −32.9 · Ceftriaxona −24.7 · Enoxaparina −21.3 · Fexofenadina −15.9. FRISO **+16.4 up-trader**. Piso citable del Mix = **−107.3** (solo-alta; es sensibilidad composicional, NO piso de intervalo).

**Puente v3 EN PAUSA (con lanzamientos, incluyendo Votripax-L — a corregir):**
Precio +393.89 · Volumen −166.38 · Mix −195.07 · **Lanzamientos +36.73** · **Gestión de portafolio −37.82** · Δ +31.35 (control −0.0). Detalle Gestión: Bajas/discontinuaciones −106.64 · Sustituciones/recodificaciones (altas no-lanzamiento) +106.86 · Valor no normalizado/servicios −38.05. (Precio/Vol/Mix se movieron vs v2 porque Votripax-L se sacó de continua; al corregir vuelven ≈ v2.)

**Reconciliación de lanzamientos (tab Datos Lanzamientos, verificado):**
Matched all-channel H1-26 = **$74.4M** vs pivote Rafael **$95.7M** → residual **$21.3M** (pivote > sell-in). Matched Privado H1-26 **$54.8M**; Hospitales **$19.5M** (Parecoxib $15.5M + Ertapenem $4.0M); Gob $0.2M. Contribución Privado V26−V25 = **$36.7M incluyendo Votripax-L −$7.1M** → lanzamientos genuinos sin Votripax-L ≈ **$43.8M**.

**Votripax-L (materiales 4040348+4040349, verificado por mes):** H1-25 $18.0M (feb $8.6M, mar $2.8M, abr $2.4M, may $1.0M, jun $3.3M) · H2-25 $9.1M · H1-26 $10.9M → contribución **−$7.1M**.

**Los 7 productos con $0 en H1-26** (Tadalafil, Tadalafil Inorg, Vitamina A/C/D, Naproxeno, Azitromicina, Oseltamivir, Combesteral) no impactan el puente H1.

---

## DECISIONES TOMADAS ESTA SESIÓN + POR QUÉ

- **La lista de Rafael es la verdad comercial de "qué es lanzamiento"; el resto de las altas = gestión de portafolio** (recodificaciones, SKUs nuevos de moléculas existentes). Coincide con el concepto "molécula nueva a PiSA" del análisis previo.
- **El puente solo puede usar sell-in del cubo** (es su base). El pivote de $96M no puede meterse crudo porque rompería la reconciliación y mezcla otra medida.
- **Exclusiones correctas confirmadas:** PISALAK 6000 cortesía ($15.7M, es el probiótico existente con empaque promocional, NO lanzamiento) y OXITAL C ($2.6M, Vitamina C, no es "Vitamina A/C/D") — bien excluidos por Codex.
- **Se pausó en vez de entregar** porque Votripax-L y el gap pivote-vs-cubo son materiales y necesitan juicio de negocio de Rafael (regla: si los datos contradicen el framing, se para y se reporta; no se fuerza).

---

## RIESGOS / PENDIENTES / LO QUE NO ESTÁ HECHO

- **Bloqueante suave:** la decisión de Rafael (arriba). Sin ella no se finaliza.
- **No re-abrir el proyecto base:** el down-trading v2 (Mix −197.9, 5 franquicias, FRISO, cobertura 96%) está CERRADO y verificado (6 rondas build↔verificación). El v3 solo AGREGA la partición de lanzamientos; no toca esas conclusiones.
- **Pendiente exógeno menor (no bloqueante):** archivar en `v2/evidencia/` las fotos de empaque que Rafael mandó (BROSPINA, Glargina×2, Budesonida, Lincomicina, Ketorolaco) y la tabla T-Padre de tarimas — para trazabilidad de los 12 overrides documentales del v2.
- **Extensión futura (cuando Rafael la pida):** v1.1 = Hospitales + Gob Frasco Cerrado con la misma maquinaria (boot: SPEC v2.4 §9/§10; no re-derivar reglas).
