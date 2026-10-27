# vocabulario

**Deterrente:** si un término se usa sin origen, esta sub-tarea deja de justificarse/ **Dos nombres para la misma cosa son una lengua sucia/**

**Fallo que cubre:** el término aparece sin origen, y después no se puede reconstruir de dónde vino/

**Piso:** `/////////1 Tesis/piso/md`/ Dos ejecutores que aplican esto tienen que coincidir en el resultado; si no, no se midió/

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · rastro · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe o ya lo cubre otra.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `vocabulario`, y el rastro que la justifica.
- **Falla si:** no hay proceso que cubra el fallo; el fallo ya no existe y no se retiró; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador? ¿el vacío se declara?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe; un trabajo que se ejecuta sin rastro.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `c` | o | n |
| `l` | a |   |
| `e` | l |   |

**X muta/** 3 hoy; mañana pueden ser otros/

> Todo término tiene origen antes de usarse/