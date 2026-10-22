# requisitos

**Deterrente:** si un requisito entra sin poder medirse, nadie puede decir después si se cumplió y la cadena entera queda sin piso/ **Un requisito que no se distingue de su ausencia no es un requisito: es un deseo con formato/**

**Fallo que cubre:** la cadena multi-paso que arranca con la **declaración** del paso anterior en vez de su salida verificada/ Es la debilidad documentada de los agentes: acumulan el error en vez de corregirlo/ `//////corpus/problemas-abiertos/md`, filas de agentes multi-paso y razonamiento fiable/

**Piso:** `/////////1 Tesis/piso/md`/ La verificación de un paso corre igual en dos ejecutores; si uno la da por buena y el otro no, no se verificó: se opinó/

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · rastro · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe o ya lo cubre otra.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `requisitos`, y el rastro que la justifica.
- **Falla si:** no hay proceso que cubra el fallo; el fallo ya no existe y no se retiró; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador? ¿el vacío se declara?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe; un trabajo que se ejecuta sin rastro.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `especificar/md` | si una intención se puede escribir como requisito observable | el requisito no distingue cumplido de incumplido |
| `verificar-requisito/md` | si el requisito se puede medir antes de aceptarlo | dos lectores entienden cosas distintas |
| `verificar-paso/md` | si el paso N+1 arranca con la salida verificada del N | la cadena sigue con la declaración, no con la prueba |

**X muta/** Tres hoy; mañana pueden ser otros/

> **Declarar no es verificar/** Si el paso N está mal, el N+1 no lo arregla: lo hereda/
