# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.

**Tarea:** editar, auditar y medir los archivos del repositorio.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Alcance:** `../Ouroboros/`, `../S.A.R.A/`, `../Agentes/` y este derrotero.
**Base:** `../Ouroboros/`. Se cita, no se copia.
**Forma:** `../S.A.R.A/Derrotero.md`.
**Abstracciones:** `../S.A.R.A/punto-de-partida/`. Se carga cuando el cambio toca una sub-tarea o un proceso.
**Claridad:** `../Ouroboros/Proceso de claridad.md`.
**Creación de procesos:** `../Ouroboros/Proceso de creación de procesos.md`. Se carga cuando el cambio produce o reemplaza un proceso.
**Registro:** `../.contexto/memoria.sql`. El `.md` es la fuente; la base es el acelerador.
**Ley:** `./mantenimiento/editar.md`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar.md` | no hay edición |
| El cambio produce o reemplaza un proceso | `../Ouroboros/Proceso de creación de procesos.md` | se edita sobre el proceso existente |
| Se audita el estado del repo | `./mantenimiento/auditar-configuracion.md` | no hay auditoría |
| Se comprueba la base contra el esquema | `./mantenimiento/verificar-esquema.md` | la base no se toca |
| Se mide si un agente es ACERO | `./mantenimiento/medir-acero.md` | no se declara ACERO |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado y su rastro, o declara el vacío. Un turno sin archivo cambiado no es una edición.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre.
