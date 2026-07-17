# Gob Servicios — puente por VALOR H1 2026 vs 2025

> Borrador de hallazgos (el .docx se genera en Fase F tras adjudicación). Segmento Mercado `Gobierno` × Canal `Servicios Gob`. Ventana H1 (Ene–Jun), 2026-07 excluido. Cifras MXN M, 4 decimales. Fuente: cubo Sell-In Cierre-JUN, hoja MER-CAN-PROD. Δ del segmento = **+84.5225 M (+3.96%)**.

---

## 1. El segmento crece +84.5 M, pero el motor es un servicio sin unidades, no una molécula

El bloque **Servicios** (MATNR prefijo 9) aporta **+54.32 M, el 64% de la Δ**, y dentro de él **hemodiálisis suma +64.46 M** — la sola línea `9000915 SERVICIOS DE HEMODIALISIS` explica **+61.47 M = 72.7% de la Δ del segmento**. No hay precio ni volumen que descomponer: es facturación de servicio. Cualquier lectura del crecimiento que busque una molécula ganadora falla de origen.

*Fuente: Datos Hechos, bloque A; hemodiálisis 9000915 verificado del cubo.*

## 2. Diálisis peritoneal (+69.42 M) es una historia de PRECIO, no de volumen

El único pool limpio del segmento admite P/V/M real por pieza. La descomposición cierra al peso: **Precio +96.16 M · Volumen (bolsas) −8.62 M · Mix de formato −18.12 M = +69.42 M**. Las bolsas cayeron **1.3%** (9.88 M → 9.75 M) mientras el **precio por bolsa subió ~15%**; el mix de formato se desplazó hacia la bolsa de **2L** (más barata por unidad), restando −18.12 M. El alza de valor está en el precio, no en más producto colocado.

*Fuente: Anexo Dialisis PVM (6 SKU: 2L/6L × 1.5/2.5/4.25%); PZA = bolsa (factor_conteo=1, precio/ml 0.024–0.029 consistente en los 6).*

## 3. La oncología específica netea a la baja y es el único bloque negativo

El bloque **Resto molécula-específica** cae **−75.95 M**, y absorbe casi todo el crecimiento de servicios y diálisis. Lo arrastra **Pembrolizumab −60.41 M** (fin del contrato del código KEYTRUDA no-GOB) y varios contratos que no se renuevan. Las **continuas cosidas** valen −97.32 M; las **altas de licitación** +26.88 M y las **bajas** −5.50 M sólo amortiguan.

*Fuente: Datos Hechos, bloque D agregado por molécula nativa.*

## 4. Sin coser las sucesiones de SKU, el puente inventaría +24 M de "altas" falsas

Los códigos GOB nacen con historia cero, así que a nivel SKU parecen altas mientras su antecesor no-GOB cae a baja: doble conteo. Cosido al nivel de **molécula nativa**, esos códigos se sumergen en su continua. Los casos: **MAMITRA +17.95** (sucede a Trazimera dentro de Trastuzumab), **Opdivo GOB +6.17** (4063930/4063931, dentro de Nivolumab), **KEYTRUDA GOB** (dentro de Pembrolizumab). Sin cosido serían +24.1 M de altas espurias con bajas simétricas; el neto real por molécula es Trastuzumab −8.92 y Nivolumab −12.02.

*Fuente: Aristas Sucesion (E6); 5 aristas documentadas con molécula, dosis y presentación.*

## 5. Las "altas" reales del canal son biosimilares que ganan licitación, no lanzamientos comerciales

Las **altas de licitación/contrato** válidas suman **+26.88 M en 12 moléculas** nuevas al canal, encabezadas por **OCRELIZUMAB +18.88 M** (biosimilar OCREVUS entrando a gobierno) y **DOXORUBICINA/ZODOX +3.74 M**. En este canal "lanzamiento" y "cambio de proveedor ganador de licitación" son indistinguibles a nivel dato; por eso van como sub-línea propia dentro de Gestión de portafolio, nunca en la línea Lanzamientos.

*Fuente: Datos Hechos, bloque D clase `alta`; decisión D2 de Rafael.*

## 6. Los 13 lanzamientos autoritativos valen 0.0000 en gobierno

Los 13 son productos del canal Privado; **ninguno registra venta en Servicios Gob** en ninguna ventana. La palanca de reclasificación nov-dic 2025 que operó en Privado **no aplica aquí**. La línea se mantiene visible en 0.0000 por consistencia con los otros tres puentes.

*Fuente: Lanzamientos; reclasificación = 0 (E9, verificada del cubo).*

## 7. Las canastas VARIOS crecen +36.73 M pero no admiten precio ni volumen

`ONCOLOGICOS` (un solo cajón de mezcla) sube **+52.96 M**; `ANTIMICROBIANOS` −7.66 M, `NPT` −3.56 M y el resto de nutrición parenteral −5.01 M. Son bloques facturados sin molécula ni unidad: entran al puente como línea de valor. Representan el 19.4% del bruto del segmento y son estructuralmente no-normalizables.

*Fuente: Datos Hechos, bloque B (molécula VARIOS, MATNR de 4 dígitos).*

## 8. Unidades y valor están desacoplados: 5.84 M piezas a $0 sostienen la decisión de no hacer P/V/M por unidades

**1,812 materiales entregan 5,835,918 piezas a valor cero** (consumibles del servicio: soluciones, jeringas, antibióticos IMSS). Con miles de renglones donde `precio = valor/piezas` es inválido, un puente Precio/Volumen/Mezcla por unidades a nivel titular sería humo. La línea de consignación se reporta en piezas y **no toca el puente de valor**.

*Fuente: Consignacion (info), E7; filas PZA>0 y Vta=0 en H1.*

---

**Control del entregable:** suma de bloques = Δ = +84.5225 (control 0.0000); anexo P/V/M cierra contra la Δ del bloque 3 (control 0.0000); 0 errores de fórmula; partición MECE sobre 2,856 materiales, cada uno en exactamente un bloque.
