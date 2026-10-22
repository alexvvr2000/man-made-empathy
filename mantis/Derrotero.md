# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.

**Tarea:** editar, auditar y medir los archivos del repositorio.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Nivel:** **instancia.** Aplica la forma de `../corpus/Derrotero.md` a este repo. No es estándar.
**Carta:** `../AGENTS.md`. Sin carta no se lee.
**Alcance:** `../corpus/`, `../Ouroboros/`, `../S.A.R.A/`, `../Agentes/` y este derrotero.
**Base:** `../Ouroboros/`. Se cita, no se copia.
**Forma:** `../corpus/Derrotero.md`.
**Abstracciones:** `../S.A.R.A/punto-de-partida/`. Se carga cuando el cambio toca una sub-tarea o un proceso.
**Claridad:** `../Ouroboros/Proceso de claridad.md`.
**Creación de procesos:** `../Ouroboros/Proceso de creación de procesos.md`. Se carga cuando el cambio produce o reemplaza un proceso.
**Registro:** `../.contexto/memoria.sql`. El `.md` es la fuente; la base es el acelerador.
**Ley:** `./mantenimiento/editar.md`.

## Los tres niveles

Una petición puede tocar tres cosas distintas, y cada una se trata distinto.

| Nivel | Dónde | Qué es | Si se rompe |
|---|---|---|---|
| **Estándar** | `../corpus/` | la forma: cómo tiene que ser algo | se corrige el estándar y **se revisan sus instancias en el mismo acto** |
| **Instancia** | `../Ouroboros/`, `../S.A.R.A/`, `../mantis/` | lo que se hace hoy | se corrige la instancia; el estándar no se toca |
| **Implementación** | `../Agentes/` | con qué se hace, en una era | si la era muere, no se toca nada más |

**Regla.** Un cambio en un estándar obliga a revisar sus instancias en el mismo acto. Un cambio en una instancia no puede contradecir su estándar: si lo contradice, gana el estándar y la instancia se corrige. Rige `../Ouroboros/Proceso de creación de procesos.md`, `R5 Consistencia cruzada`.

**Cómo se sabe cuál es.** Un archivo que dice **cómo tiene que ser** algo es estándar. Uno que dice **qué se hace hoy** es instancia. Uno que dice **con qué** es implementación. Un **caso** —qué pasó una vez— no es ninguno de los tres y no entra en `../corpus/`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar.md` | no hay edición |
| El cambio toca un **estándar** | `../corpus/README.md` y `./mantenimiento/editar.md`, paso 9 | el estándar se cambia sin revisar sus instancias |
| El cambio produce o reemplaza un proceso | `../Ouroboros/Proceso de creación de procesos.md` | se edita sobre el proceso existente |
| Se audita el estado del repo | `./mantenimiento/auditar-configuracion.md` | no hay auditoría |
| Se comprueba la base contra el esquema | `./mantenimiento/verificar-esquema.md` | la base no se toca |
| Se mide si un agente es ACERO | `./mantenimiento/medir-acero.md` | no se declara ACERO |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado y su rastro, o declara el vacío. Un turno sin archivo cambiado no es una edición.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre.
