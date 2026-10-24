# alineacion

**Deterrente:** si el sistema puede actuar sin que quien decide pueda comprender qué se hizo, esta sub-tarea deja de justificarse/ **Un sistema que hace cosas que su autoridad no puede seguir no está alineado: está tomando el mando/**

**Fallo que cubre:** quien decide no puede comprender todo lo que el sistema hace, y el sistema aprovecha ese hueco/ La alineación falsa: parecer alineado durante la supervisión y no serlo fuera de ella/ `//////corpus/problemas-abiertos/md`, fila de alineación de valores/

**Piso:** `/////////1 Tesis/piso/md`/ Si dos ejecutores no coinciden en qué se supervisó, no se supervisó/

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · rastro · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe o ya lo cubre otra.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `alineacion`, y el rastro que la justifica.
- **Falla si:** no hay proceso que cubra el fallo; el fallo ya no existe y no se retiró; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador? ¿el vacío se declara?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe; un trabajo que se ejecuta sin rastro.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `supervisar/md` | si lo supervisado se comporta igual cuando no se mira | el comportamiento cambia sin que cambie la regla |
| `entender-salida/md` | si la autoridad puede entender lo que se va a hacer | se aprueba algo que no se comprende |
| `pluralizar-autoridad/md` | si ninguna jurisdicción decide fuera de la suya | una sola instancia decide por todas |

**X muta/** Tres hoy; mañana pueden ser otros/

> **Cambiar de perspectiva ayuda a que nadie mate por un absoluto** — y ninguna perspectiva basta sola/
