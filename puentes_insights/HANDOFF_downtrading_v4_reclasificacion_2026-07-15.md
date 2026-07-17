# HANDOFF — Down-trading Privado: v3 Lanzamientos + v4 Reclasificación (anti-compactación)

**Proyecto:** PVM / Down-trading sell-in PiSA — reporte Privado en 5 conceptos (Precio · Volumen · Mix · Lanzamientos · Gestión de portafolio).
**Fecha:** 2026-07-15 (sesión tarde-noche).
**Propósito de este handoff:** sobrevivir una compactación de contexto de ESTA conversación y preservar aprendizajes. No hay trabajo pendiente de construcción.
**Estado en una línea:** v4 ENTREGADO Y ADJUDICADO (auditoría Fable 27 checks, APROBADO; dos constructores independientes convergen al mismo puente); la única puerta abierta es el OK final de Rafael al artefacto.

> El handoff previo `HANDOFF_downtrading_lanzamientos_2026-07-15.md` (mañana) quedó **STALE**: las dos decisiones que esperaba ya se tomaron y se ejecutaron, más una tercera (reclasificación) que no existía entonces.

---

## LEE PRIMERO, EN ESTE ORDEN (no actúes antes)

1. **Este handoff** (completo).
2. `APRENDIZAJES_y_metodo.md` — sección "SESIÓN 2026-07-15 (tarde-noche)": el método y las trampas.
3. `CIERRE_v4_reclasificacion_2026-07-15.md` — cierre del v4 con proceso y gates.
4. `CODEX_RUN_v4_2026-07-15.md` — reporte de la corrida de Codex (llegó tarde pero completó PASS).
5. Memoria `project_pvm_downtrading.md` — estado acumulado del proyecto.
6. Solo si vas a tocar números: `audit_fable_v4_2026-07-15.py` (los 27 checks ejecutables) y `make_v4_claude.py` (generador del canónico).

---

## QUÉ SE HIZO ESTA SESIÓN

- **v3 (línea Lanzamientos):** Rafael decidió (a) Votripax-L fuera de lanzamientos → base continua (vendía desde feb-2025: H1-25 $18.0M → H1-26 $10.9M, −$7.1M); (b) abandonar el pivote de $96M (sin nota de reconciliación; el reporte es 100% sell-in del cubo). Entregado verificado: Lanzamientos +43.8, Δ +31.3, PVM = v2 exacto.
- **Revisión Agrifen Lub (reto de Rafael, resuelto):** no hubo confusión con Agrifen tabletas. Agrifen Lub = AGUA DE MAR, materiales 4059190/4059191 ($0.84M flujo H1-26); Agrifen tabletas = CLORFENAMINA COMPUESTA (~$100M, base continua, jamás marcado lanzamiento). Su imagen de BD confirmó los mismos 2 materiales y cifras idénticas al peso. Su "$7.37M" era **acumulado life-to-date**, no flujo del semestre.
- **v4 (reclasificación):** Rafael instruyó reclasificar la venta **nov-dic 2025 de los lanzamientos** como ene-2026 (adelantos de cierre que corresponden al lanzamiento 2026). Alcance: SOLO lanzamientos. Con **ambas vistas** (puente reclasificado + conciliación al sell-in bruto). Construido, entregado y adjudicado.
- **Decisión adicional de Rafael:** los 11 lanzamientos se mantienen JUNTOS (no partir en nuevos-2026 vs continuación-2025); la venta 2025 fue adelanto de cierre, corresponde al lanzamiento 2026.
- **Auditoría Fable (cambio de modelo a Fable 5):** 27 checks sobre el canónico; 26 OK directos + 1 discrepancia investigada y explicada al peso (ver Números). Veredicto: APROBADO.

## ESTADO CANÓNICO ACTUAL (verdad de hoy, en `~/Downloads/PVM_Reconstruido_scripts/v2/`)

| Archivo | sha256[:16] | Rol / estado |
|---|---|---|
| **`Downtrading_Privado_v4_FINAL_2026-07-15.xlsx`** | `d5927374d14cc3de` | **CANÓNICO entregado a Rafael.** Formulado; puente reclasificado + conciliación. Construido por Opus (`make_v4_claude.py`), verificado 3 veces + auditoría Fable |
| **`INSIGHTS_Downtrading_Privado_v4_FINAL.md` / `.docx`** | `c4d3de0f` / `9762c11c` | Reporte entregado (nota de método + conciliación; sin pivote $96M) |
| `Downtrading_Privado_v4_FORMULADO.xlsx` | `9f2d3e3f6b99a1d3` | Construcción PARALELA de Codex (completó 21:01, tarde). **Verificada por Fable: mismos gates, mismo puente.** Extras: tab Datos Lanzamientos actualizada, QA visual 8/8 págs, auto_filter A4:J. Candidata a reemplazar al canónico SI Rafael quiere una sola línea — no promovida |
| `Downtrading_Privado_v3_FORMULADO.xlsx` | `4642afc005eba4da` | v3 histórico, verde, intacto (base del v4) |
| `Downtrading_Privado_v2_FORMULADO.xlsx` | `befdde09489089e4` | v2 aprobado, intacto, NO tocar |
| `make_v4_claude.py` / `verify_v4_final_claude.py` / `audit_fable_v4_2026-07-15.py` | — | Generador del canónico / verificador independiente / auditoría Fable (los 3 reproducibles) |
| `analyze_v3_launches.py` / `build_downtrading_v3.py` | — | Pipeline de Codex, editado a v4 (a pesar del nombre "v3"); genera los `_FORMULADO` |
| `reclass_novdec25_GATE.json` | — | Gate del ajuste por material (fuente: cubo) |
| `HANDOFF_downtrading_lanzamientos_2026-07-15.md` | — | **STALE** (superado por este) |
| `INSIGHTS_Downtrading_Privado_v3.md/.docx`, `QA_v3.json` | — | Históricos v3, verdes |

## NÚMEROS CLAVE (auditados; sell-in cubo Cierre-JUN, Privado = Farmacias+Impulso+Expansión, Ene-Jun 2026 vs 2025, MXN M)

**Puente v4 (reclasificado) — el entregado:**
Precio **+392.9** · Volumen **−169.7** · Mix **−197.9** (los tres = v2/v3 exactos, sin cambio) · **Lanzamientos +71.1** · Gestión de portafolio **−37.8** (bajas −106.6 / sustituciones-recodificaciones +106.9 / valor-no-norm −38.0) · **Δ Venta Privado +58.7** · Control 0. Suma verificada: 392.9498−169.7100−197.8992+71.1360−37.8222 = 58.6544 ✓.

**Conciliación (ambas vistas, filas 35-38 del Resumen):** Δ reclasificada +58.65 − reclasificación 27.31 = **sell-in bruto +31.35** ✓.

**Ajuste de reclasificación = $27.3073M** (venta nov+dic 2025 privado de lanzamientos, 9 materiales con valor): Rivastigmina 6.49 · Agrifen Lub 6.53 (3.37+3.17) · Donepezilo+Mem 5.80 (2.57+3.23) · Pisalak Lipigo 5.31 (**5.25 en NOV**) · Brimo+Dorzo 2.55 · Pisalak Forte 0.46 · Parecoxib 0.16. Verificado por material al centavo contra el cubo (13/13; los 4 restantes = 0).

**Lanzamientos:** flujo H1-26 genuino +43.83 (11 productos; nuevos-2026 26.45 + continuación-2025 17.38) + ajuste 27.31 = **+71.14** ✓. Votripax-L (−7.1) FUERA, en base continua.

**Hallazgo de la auditoría Fable (F6):** Δ bruta del universo privado completo del cubo = **+31.760**, no +31.347. Gap = **+$413,102.22 exactos** = Δ de las **filas del canal FLP sin MATNR** (serie mensual 2023-2026, ~$0.3-0.5M/mes; V25H1 $1.66M → V26H1 $2.08M). Exclusión ESTRUCTURAL del modelo desde v2 (sin material no hay llave física); no es error del v4. Con la exclusión aplicada el cuadre es exacto.

**Down-trading (sin cambio, cerrado desde v2):** Mix −197.9 central; top-5 = Amox/Clav −45.6 · Levofloxacino −32.9 · Ceftriaxona −24.7 · Enoxaparina −21.3 · Fexofenadina −15.9 (71%); FRISO +16.4 up-trader; G5b 96.02%.

## DECISIONES TOMADAS + POR QUÉ

1. **Votripax-L → base continua** (Rafael): vendía en H1-2025 desde febrero; no es lanzamiento del año comparado. Como lanzamiento saldría negativo, engañoso.
2. **Pivote $96M abandonado** (Rafael): el puente usa solo sell-in. Diagnóstico posterior: su columna "Vta Ene-Jun 26" es ACUMULADO (FY25+H1-26), no otra fuente — la corrección del diagnóstico "sell-out/PIN" quedó registrada.
3. **11 lanzamientos juntos** (Rafael): las ventas 2025 fueron adelantos de cierre del lanzamiento 2026, no base continua (a diferencia de Votripax-L, que vendía en H1).
4. **Reclasificación nov-dic 25 → ene 26, SOLO lanzamientos** (Rafael): los continuos venden en ambos H1 y su patrón de cierre se cancela en la comparación; los lanzamientos no tenían H1-25.
5. **Ambas vistas** (Rafael): puente reclasificado como headline + conciliación al sell-in bruto para auditoría contra la fuente oficial.
6. **Canónico = `_FINAL` con nombre único** (Opus/Fable): tras dos fallas async de Codex y una carrera de escritura, el entregable se blindó fuera del alcance de regeneración de la tarea de Codex. El `_FORMULADO` de Codex (llegó tarde, PASS verificado) queda como paralelo no promovido.

## SIGUIENTE PASO

**Ninguno de construcción.** La puerta es el **OK de Rafael al v4_FINAL** (ya lo tiene: xlsx + docx). Si pide cambios, el generador es `make_v4_claude.py` (canónico) o el pipeline de Codex (paralelo). Si Rafael quiere consolidar en una sola línea de artefactos, adjudicar formalmente el `_FORMULADO` de Codex como reemplazo (ya pasó los gates numéricos; faltaría solo decisión).

## RIESGOS / PENDIENTES / LO QUE NO ESTÁ HECHO

- **La tarea background de Codex puede despertar de nuevo** y regenerar los `_FORMULADO`. Los `_FINAL` (canónicos) están fuera de su alcance por nombre. No borrar los `_FORMULADO` mientras esa tarea viva; no re-delegar sobre los mismos archivos.
- **Pendiente exógeno menor** (desde v2, no bloqueante): archivar en `v2/evidencia/` las fotos de empaque de Rafael (BROSPINA, Glargina×2, Budesonida, Lincomicina, Ketorolaco) y la tabla T-Padre de tarimas.
- **No re-abrir:** v2 (cerrado, 6 rondas) ni la SPEC v2.4 (congelada). El v4 no tocó Precio/Volumen/Mix/Gestión.
- **Comunicación del +58.7:** la Δ reclasificada NO es el sell-in oficial del semestre; quien audite contra el cubo debe pasar por la conciliación (−27.3). Ya está visible en Excel e insights; cuidar que no se cite +58.7 como "crecimiento sell-in" sin la nota.
- **Extensión futura** (cuando Rafael la pida): v1.1 Hospitales + Gob Frasco Cerrado con la misma maquinaria (boot: SPEC v2.4 §9/§10).
