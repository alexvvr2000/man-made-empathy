# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.

**Tarea:** editar, auditar y medir los archivos del repositorio.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Nivel:** **instancia.** Aplica la forma de `../2 Ouroboros/formato de ente.md`. No es estándar.
**Carta:** `../AGENTS.md`. Sin carta no se lee.
**Alcance:** `../1 Tesis/`, `../2 Ouroboros/` y `../Era/`.
**Estándar:** `../2 Ouroboros/`. Se cita, no se copia.
**Forma:** `../2 Ouroboros/formato de ente.md`, `formato de proceso.md`, `mutacion.md`.
**Puerta:** `../2 Ouroboros/CRITERIO.md`.
**Abstracción:** `../2 Ouroboros/2 S.A.R.A — mutación/`. Se carga cuando el cambio toca una sub-tarea o un proceso.
**Integridad:** `../2 Ouroboros/2 S.A.R.A — mutación/integridad.md`. **Corre siempre antes de mutar:** el criterio no decide si corre, solo qué se hace con su veredicto.
**Claridad:** `../2 Ouroboros/1 Guantelete — primitivo/primitivos/claridad.md`.
**Manipulación de procesos:** `../2 Ouroboros/1 Guantelete — primitivo/primitivos/manipulacion.md`. Se carga cuando el cambio produce o reemplaza un proceso.
**Registro:** `../1 Tesis/notas.md`. **Es la memoria: lo que no se anota se pierde con el contexto.**
**Ley:** `./mantenimiento/editar.md`.
**Piso:** `./piso/`. Corre aquí y ahora; la forma que sigue está en `../2 Ouroboros/piso.md`.
**Carga:** `./deterrente.md`. Sin él, MANTIS ayuda a editar sin decir qué se pierde si deja de ayudar, y una herramienta que no declara su pérdida se conserva por costumbre.

## Los tres niveles

Una petición puede tocar tres cosas distintas, y cada una se trata distinto.

| Nivel | Dónde | Qué es | Si se rompe |
|---|---|---|---|
| **Estándar** | `../2 Ouroboros/` | la forma: cómo tiene que ser algo | se corrige y **se revisan sus instancias en el mismo acto** |
| **Instancia** | `../1 Tesis/`, `../mantis/` | lo que se hace hoy o lo que explica el porqué | se corrige la instancia; el estándar no se toca |
| **Implementación** | `../Era/` | con qué se hace, en una era | si la era muere, no se toca nada más |

**Regla.** Un cambio en el estándar obliga a revisar sus instancias en el mismo acto. Una instancia no puede contradecir el estándar: si lo contradice, gana el estándar y la instancia se corrige.

**Cómo se sabe cuál es.** Un archivo que dice **cómo tiene que ser** algo es estándar y vive en `../2 Ouroboros/`. Uno que dice **qué se hace hoy** es instancia. Uno que dice **con qué** es implementación. Uno que dice **por qué** es tesis, y vive en `../1 Tesis/`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar.md` | no hay edición |
| **Se produce una decisión, una frase o un descarte** | **`../AGENTS.md`, `Escribir notas`** y `../1 Tesis/notas.md` | el turno no está entregado |
| **Se emite cualquier archivo** | `../2 Ouroboros/1 Guantelete — primitivo/primitivos/claridad.md` | no se emite |
| Se va a mutar cualquier cosa | `../2 Ouroboros/2 S.A.R.A — mutación/integridad.md`, **siempre** | no se muta |
| Se saca algo del estándar | `../1 Tesis/desechos del estandar.md`, entero y con su archivo | se pierde el porqué |
| El cambio toca el **estándar** | `../2 Ouroboros/CRITERIO.md` y `./mantenimiento/editar.md`, paso 9 | el estándar se cambia sin revisar sus instancias |
| El cambio produce o reemplaza un proceso | `../2 Ouroboros/1 Guantelete — primitivo/primitivos/manipulacion.md` | se edita sobre el proceso existente |
| Se crea un subproceso | `../2 Ouroboros/2 S.A.R.A — mutación/Proceso PROMETEA.md`: **integridad antes, sí o sí** | se crea lo que debía rehacerse |
| Se audita el estado del repo | `./mantenimiento/auditar-configuracion.md` | no hay auditoría |
| Se mide si un agente es ACERO | `./mantenimiento/medir-acero.md` | no se declara ACERO |
| Se chequea forma o conteo | `./piso/inventario.ps1`, `./piso/indice.ps1` y `../2 Ouroboros/formato de proceso.md` | no hay veredicto |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado, su rastro, y **sus filas de notas si produjo algo que valga.** Un turno sin archivo cambiado no es una edición; uno con decisión y sin fila no está entregado.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre; sin notas no hay tesis.
