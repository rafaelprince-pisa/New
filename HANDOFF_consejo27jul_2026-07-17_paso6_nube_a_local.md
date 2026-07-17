# HANDOFF · Consejo 27-jul · Paso 6 TERMINADO en la nube; ejecutar pasos 7-8 en local
**Proyecto:** Presentación al Consejo de Pharma MX, lunes 27-jul-2026 · **Fecha:** 17-jul-2026 · **Escrito por:** sesión de nube (Claude Code remoto)
**Estado en una línea:** las **38 specs v7 están escritas, auditadas por 9 agentes, corregidas y en `main`** del repo `rafaelprince-pisa/New`; la sesión LOCAL en la Mac de Rafael ejecuta los pasos 7 (9 carriles Codex) y 8 (PPT por momentos). Nada del paso 6 queda pendiente.

## 0. BOOT de la sesión local (en este orden)

1. `cd "/Users/rafaelprince/Claude Code/Consejo27jul_nube"` (o donde viva el clon) y `git pull origin main` — el PR #1 ya está mergeado; `main` trae todo.
2. Copia `storyboard_v3_specs_AQUI_ESCRIBE_LA_NUBE/` a `consejo-27jul/storyboard_v3/` (flujo de regreso del handoff v7 §0).
3. Lee `storyboard_v3_specs_AQUI_ESCRIBE_LA_NUBE/00_INDEX.md` — es el mapa: momentos, absorciones, decisiones tomadas, pendientes exógenos y la propuesta de 9 carriles.
4. Verificación de primera mano (opcional pero recomendada, ~10 min): re-corre los cuadres de las 3-4 specs más cargadas (L02 tabla, L05 waterfall rector, L06 ejecución, L19 ruta) contra `HANDOFF_consejo27jul_2026-07-16_NOCHE_rediseno_v7.md` §3 y `puentes_insights/INSIGHTS_PiSA_Consolidado_FINAL.md`. La nube ya lo hizo (auditoría de 9 agentes + fixes re-verificados), pero la regla de la casa es no heredar "todo verde" sin reproducirlo.
5. Ejecuta **paso 7** y luego **paso 8** (abajo).

## 1. Qué entregó la nube (paso 6)

- **38 specs** (`SB_L01.md` a `SB_L38.md`): cuerpo 22 (títulos VERBATIM de la `PROPUESTA_rediseno_v7`) + anexos A1-A16 (A1=L23 … A16=L38). Formato heredado de v2: encabezado/layout/zona por zona/mensaje/fuente/estado del dato/notas + sección final "## Instrucciones ChatGPT Images 2" autocontenida por lámina (texto verbatim entre comillas, hex del design system, proporciones relativas, prohibiciones).
- **`00_INDEX.md`**: mapa completo + decisiones + carriles propuestos.
- **Auditoría**: 9 agentes (mecánica · cuadres cuerpo · cuadres anexos · kill-list/estilo Brunswick · coherencia cross-lámina · 4 lecturas profundas adversariales). Veredicto: **la aritmética cuadró exacta** contra las fuentes canónicas (matriz 8×4, conciliación 272.1→239.3, tabla por canal, EBITDA v18+Gross2Net, VP/PIN/NC/Dev). Hallazgos (2 críticos, 12 mayores, ~20 menores) fueron de citación/consistencia/ejecutabilidad y TODOS se corrigieron y re-verificaron (0 flechas, 0 emojis, 0 kill-list en tinta, pies y casing correctos).
- Git: rama `claude/consejo-handoff-execution-df78tx`, commit final `2f9ed2e`, PR #1 mergeado a `main`.

## 2. Decisiones que tomó la nube — Rafael valida (detalle en 00_INDEX.md §Decisiones)

1. **Bandas de "aporte al hueco" CORTADAS en las 4 láminas de plan** (L09/L12/L15/L18); el reparto vive SOLO en la cascada de L19 (gate: los [RC] suman +$1,596.6M). Razón: fix de simetría del consejo 2 + montos aún [RC].
2. **L01, objetivo 2 de la DG re-redactado**: "Presentar la ruta del segundo semestre hacia el compromiso anual" (mata "vamos a llegar", Brunswick). NO aprobado verbatim por Rafael.
3. **Gold de L08 en el ~$195M** (poder de precio neto); el −$197.9M conserva su gold solo en L07. Dueños de cifra: −197.9 solo L07/L08/A8.
4. **PIN de gobierno jamás impreso como cifra** (859/869 solo en notas internas): placeholder "[PIN gobierno por planchar: Hugo/DT]".
5. **Fuente de VP/PIN impresa: "IC, cierre 16-jul"** (INPUT canónico supersede DP).
6. Eyebrows de universo UPPERCASE únicos con marca "PiSA"; asterisco de junio anclado en "+1.5%*" de la fila total de L02; excepciones de densidad declaradas en A8/A10 (anexos técnicos).

## 3. Paso 7 — dibujo (9 carriles Codex)

- Carriles propuestos en `00_INDEX.md` (C1-C9, 38 láminas balanceadas; C2 = L05/L06/L07, las más densas).
- Patrón probado del 16-jul: `CODEX_TASK_<carril>.md` en `storyboard_v3/renders/`, una-por-una DENTRO del carril, `PROGRESS_<carril>.md` tras cada lámina, OVERWRITE explícito, "DONE <carril>: n de N" al final; watcher por conteo de PNGs/mtime, no confiar en el forwarder.
- Corchetes placeholder se dibujan LITERALES en gris; siluetas grises donde falte dato; el carácter de flecha JAMÁS; QA visual siempre (falla conocida: typos de diacríticos en render).

## 4. Paso 8 — PPT por momentos

- Adaptar `consejo-27jul/storyboard_v2/build_storyboard_ppt.py` a las secciones v7: M0 Apertura y el semestre (L01-07) · M1 Retail (L08-09) · M2 Gobierno FC (L10-12) · M3 Hospitales (L13-15) · M4 Servicios (L16-18) · M5 Ruta y cierre (L19-22) · M6 Anexos A1-A16 (L23-38).
- Reglas de Rafael: índice de momentos primero, máx 4 fotos/hoja, jamás mezclar momentos. Entregar a Rafael para la revisión lámina-por-lámina con el equipo.

## 5. Pendientes exógenos (NO construir aguas abajo; se dibujan como placeholders)

[96] y todo lo condicionado al 2S [Heriberto, antes del 20] · montos de la cascada L19 [RC, gate +$1,596.6M] · burbujas A3 [CC] · comparador −40% Baxter y respuesta del frente [Martín] · VP/PIN gobierno [DS/FM/Hugo/DT] · meta de cobranza [DS] · split EBITDA y 25.2% vs 23.5% [VJ] · ASK de L22 [Rafael/Felipe] · unidad/base share gobierno [CC/DS] · pull-forward ~$104M [CC] · kill-list de corchetes con árbitro el 21-jul.

**Calendario:** número del 2S antes del 20 · kill-list el 21 · PPT con financieros finales a Presidencia el miércoles 22 · junta lunes 27.

## 6. Deuda no bloqueante

- `build_storyline_v6.py` → Word v7 al canónico antes del 22 (sigue UN PASO ATRÁS de las specs).
- Pre-read 3pp y deck real a Presidencia.

---
*Gemelo de método: `APRENDIZAJES_y_metodo.md`, sección "Sesión 17-jul (nube)" — léela antes de repetir el patrón nube/multi-agente.*
