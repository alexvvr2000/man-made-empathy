# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.
**Tarea:** editar los archivos de `../Alineacion de tareas/`.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Alcance:** los archivos de `../Alineacion de tareas/` y de este derrotero.
**Base:** `../Alineacion de tareas/`. Se cita, no se copia.
**Forma:** `../Alineacion de tareas/Derrotero.md`.
**Cuerpo:** `../Alineacion de tareas/Procesos principales/`. Se carga solo cuando el cambio toca una norma.
**Escritura:** `../Alineacion de tareas/Escritura/Reglas de escritura.md`.
**Ley:** `./mantenimiento/editar.md`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar.md` | no hay edición |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado y su rastro, o declara el vacío. Un turno sin archivo cambiado no es una edición.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre.
