# Proceso de evaluar

**Variables:** resultado · criterio · momento · veredicto
**Peor:** el criterio se fija después de ver el resultado
**Quién:** quien confía en el veredicto, que no vio cuándo se fijó

**Unidad:** proceso/
**Aplica a:** evaluar/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

El resultado se mide contra un criterio declarado antes, no después/ El fallo que corrige es la evaluación que se ajusta al resultado ya obtenido/

Práctica de industria: evaluación de modelos y validación cruzada/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el resultado y el criterio de acepción del requisito/
- **Falla:** el criterio se fijó después; la muestra sirve para el modelo/
- **Sale:** el veredicto con su cuenta/
- **Consume:** la autoridad, y `///versionado/` si cambia el estado/

## Cómo se aplica

1/ **Fijar el criterio antes/** El que vino de `///requisitos/`/ Sin criterio previo, no hay evaluación: hay justificación/
2/ **Separar la muestra/** Lo que se mide no se usó para construir/ Un modelo que se evalúa con sus propios datos solo confirma lo que ya sabía/
3/ **Declarar la métrica/** Qué se cuenta y qué no/
4/ **Medir/** El resultado con su cuenta/
5/ **Declarar el veredicto/** Pasa, no pasa, o no se puede saber/

`Criterio: [el previo] | Métrica: [qué se cuenta] | Muestra: [de dónde] | Veredicto: [pasa|no pasa|indeterminado]`

## Prueba

¿El criterio es anterior al resultado? ¿La muestra es independiente de lo evaluado?

**Falsificador:** el criterio se ajustó después; se evalúa con los datos de entrenamiento; la métrica se elige para que pase/

## Transiciones

- Si el criterio no existe o se fijó después → `[VACÍO - SIN CRITERIO PREVIO]`/
- Si el resultado cambia lo que hay → `probar-regresion/md`/
- Si el cambio debe versionarse → `///versionado/`/
- En cualquier otro caso → se entrega y se cierra/
