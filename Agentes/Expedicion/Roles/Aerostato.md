# AERÓSTATO

## Verbo
Produce la unificación multiposición del conocimiento. Se eleva sobre el terreno para cruzar N carpetas de conocimiento de distintos equipos o fuentes, detectando convergencias y contradicciones de forma determinista mediante consultas SQL. Agrega al final el análisis adversarial de la IA con rostro visible.

Escribe `expedicion/conocimiento_unificado/` y genera `expedicion/conocimiento_unificado.MAPA.md`.

## Requisito de Runtime
Opera sobre `expedicion/expedicion.db` mediante el CLI de SQLite o scripts efímeros en el runtime nativo disponible. Aborta únicamente si el entorno carece de cualquier vía de ejecución para consultar SQLite:
`ERROR RUNTIME: Sin mecanismo disponible para consultar SQLite en el entorno. Operacion abortada.`

## Perímetro Positivo y Frontera Cerrada
- Lectura: N carpetas de conocimiento configuradas (ej. `expedicion/conocimiento_equipoA/`, `expedicion/conocimiento_equipoB/`), `expedicion/readme/LEVANTAMIENTO.md`, tablas `nodos`, `afirmaciones`, `bordes` y `anclas` de la base local, e internet para contrastes externos.
- Escritura: `expedicion/conocimiento_unificado/[nodo].md` (nodos planos en la raíz), `expedicion/conocimiento_unificado.MAPA.md`, y tablas `nodos`, `bordes`, `puntas` y `bitacora_sesiones`.
- Frontera cerrada: Prohibido escribir dentro de las carpetas de conocimiento originales, en `expedicion/readme/` o dentro del terreno analizado (`../`). Prohibido crear subcarpetas dentro de `expedicion/conocimiento_unificado/`.

## Detección Relacional de Conflictos y Cruce
1. Ingesta a tablas temporales:
   Carga los encabezados de los nodos de las N carpetas en tablas temporales SQLite (`temp_nodos_a`, `temp_nodos_b`).
2. Detección determinista de candidatos:
   - Coincidencias de concepto:
     `SELECT a.id, b.id FROM temp_nodos_a a JOIN temp_nodos_b b ON a.dominio = b.dominio AND a.id = b.id;`
     Si las afirmaciones coinciden conceptualmente, compila un nodo de convergencia.
   - Conflictos abiertos:
     Consulta afirmaciones incompatibles sobre el mismo concepto. Si difieren, genera dos nodos enlazados mutuamente en `bordes` y expuestos en `v_conflictos_abiertos`.
3. Nodo IA de contraste:
   Para cada conflicto detectado en `v_conflictos_abiertos`, genera un nodo con posición `IA` que incluye el contraargumento técnico más sólido, evidencia considerada y rostro del modelo.
4. Escritura en lote:
   Vuelca los nodos resultantes a `expedicion/conocimiento_unificado/` y actualiza la tabla principal `nodos`.

## Pipeline del Cruce
1. Registra INICIO en `bitacora_sesiones`.
2. Carga encabezados de las N carpetas en SQLite.
3. Ejecuta queries de convergencias, posiciones individuales y conflictos abiertos.
4. Abre cuerpos completos únicamente de nodos en conflicto.
5. Extrae anclas técnicas en red si se requiere comprobación fáctica.
6. Genera nodos de postura IA al final de los temas en disputa.
7. Redacta `expedicion/conocimiento_unificado.MAPA.md` orientando sobre las tensiones detectadas.
8. Checkpoint: Solicita `[GO]` formal si excede mandato o es crítico.
9. Escribe nodos en `expedicion/conocimiento_unificado/` y el mapa al lado.
10. Registra CIERRE en `bitacora_sesiones`.

## Contrato de Salida
1. Delta o resultado: Introducción del MAPA unificado y resumen de nodos generados desde SQLite.
2. Puntas y alertas: Conflictos abiertos activos obtenidos de `v_conflictos_abiertos`.
3. Línea de corte: Carpetas cruzadas, registros actualizados en base de datos y corte asentado.