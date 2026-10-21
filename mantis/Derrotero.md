# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.
**Tarea:** editar los archivos de `../Alineacion de tareas/`.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Alcance:** los archivos de `../Alineacion de tareas/` y de este derrotero.
**Base:** `../Alineacion de tareas/`. Se cita, no se copia.
**Forma:** `../Alineacion de tareas/Derrotero.md`.
**Abstracciones:** `../Alineacion de tareas/punto-de-partida/`. Se carga solo cuando el cambio toca una abstracción.
**Claridad:** `../Alineacion de tareas/Ouroboros/Proceso de claridad.md`.
**Creación de procesos:** `../Alineacion de tareas/Ouroboros/Proceso de creación de procesos.md`. Se carga cuando el cambio produce o reemplaza un proceso.
**Ley:** `./mantenimiento/editar.md`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar.md` | no hay edición |
| El cambio produce o reemplaza un proceso | `../Alineacion de tareas/Ouroboros/Proceso de creación de procesos.md` | se edita sobre el proceso existente |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado y su rastro, o declara el vacío. Un turno sin archivo cambiado no es una edición.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre.
