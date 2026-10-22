# Proceso de componer

**Variables:** cadena · colaboradores · coste · tramo
**Peor:** se optimiza la pieza y se rompe la cadena
**Quién:** el tramo de la cadena que carga el coste

**Unidad:** proceso/
**Aplica a:** componer/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un colaborador con buen rendimiento aislado arruina la cadena por su posición/ La unidad no es qué colaborador para qué tarea: es qué colaborador, en qué posición, recibiendo qué, produciendo qué para el siguiente/

Estado del arte: enrutamiento en cascada y coste por éxito/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** la tarea completa y los colaboradores disponibles/
- **Falla:** se elige por precio unitario; se elige por rendimiento aislado; el ahorro de un paso se paga en el siguiente/
- **Sale:** la cadena, con la posición y el coste por resultado exitoso de la tarea entera/
- **Consume:** quien opera la cadena/

## Cómo se aplica

1/ **Partir la tarea en pasos/** Qué produce cada paso y qué necesita el siguiente/
2/ **Medir la sensibilidad/** Qué tan frágil es cada paso al output del anterior/ Frágil exige colaborador estable; robusto tolera varianza/
3/ **Asignar por coste de cadena/** El colaborador de una posición se elige por el coste del resultado final, no por su precio aislado/
4/ **Declarar la varianza/** Una posición inestable frente a un paso frágil es riesgo declarado, no sorpresa/
5/ **Escalar solo con verificación/** Se sube a un colaborador mejor si el paso falló su control, no por intuición/

`Cadena: [n pasos] | Frágil: [cuáles] | Coste de la cadena: [CRE] | Varianza: [P50/P90]`

## Prueba

¿Cada posición se eligió por el coste de la cadena? ¿La varianza frente a pasos frágiles está declarada?

**Falsificador:** se elige por precio unitario; se elige por rendimiento aislado sin mirar aguas abajo; una posición inestable frente a un paso frágil sin declararlo; se escala sin verificación/

## Transiciones

- Si la cadena supera su presupuesto → `///costo/acotar/md`/
- Si la composición afecta a otros → `armonizar/md`/
- En cualquier otro caso → se entrega y se cierra/
