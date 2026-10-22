# Derrotero de MANTIS

**MANTIS:** Mantenimiento, Auditoría, Normas, Trazabilidad e Integridad del Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.

**Tarea:** editar, auditar y medir los archivos del repositorio.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Nivel:** **instancia.** Aplica la forma de `../Ouroboros/formato de ente.md`. No es estándar.
**Carta:** `../AGENTS.md`. Sin carta no se lee.
**Alcance:** `../Tesis/`, `../Ouroboros/` y `../Implementaciones de la era/`.
**Estándar:** `../Ouroboros/`. Se cita, no se copia.
**Forma:** `../Ouroboros/formato de ente.md`, `formato de proceso.md`, `mutacion.md`.
**Puerta:** `../Ouroboros/CRITERIO.md`.
**Abstracción:** `../Ouroboros/2 S.A.R.A — mutación/`. Se carga cuando el cambio toca una sub-tarea o un proceso.
**Integridad:** `../Ouroboros/procesos/integridad.md`. **Corre siempre antes de mutar:** el criterio no decide si corre, solo qué se hace con su veredicto.
**Claridad:** `../Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md`.
**Manipulación de procesos:** `../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md`. Se carga cuando el cambio produce o reemplaza un proceso.
**Registro:** `../notas/actuales.md`. **Es la memoria: lo que no se anota se pierde con el contexto.**
**Ley:** `./mantenimiento/editar/editar.md`.
**Formato:** `./mantenimiento/editar/enrutar-formato.md`: todo proceso se carga por las nueve piezas y los condicionales antes de escribirse. Rige `../Ouroboros/formato de proceso.md`; no lo copia.
**Piso:** `./piso/`. Corre aquí y ahora; la forma que sigue está en `../Ouroboros/piso.md`.
**Carga:** `./deterrente.md`. Sin él, MANTIS ayuda a editar sin decir qué se pierde si deja de ayudar, y una herramienta que no declara su pérdida se conserva por costumbre.

## Los tres niveles

Una petición puede tocar tres cosas distintas, y cada una se trata distinto.

| Nivel | Dónde | Qué es | Si se rompe |
|---|---|---|---|
| **Estándar** | `../Ouroboros/` | la forma: cómo tiene que ser algo | se corrige y **se revisan sus instancias en el mismo acto** |
| **Instancia** | `../Tesis/`, `../mantis/` | lo que se hace hoy o lo que explica el porqué | se corrige la instancia; el estándar no se toca |
| **Implementación** | `../Implementaciones de la era/` | con qué se hace, en una era | si la era muere, no se toca nada más |

**Regla.** Un cambio en el estándar obliga a revisar sus instancias en el mismo acto. Una instancia no puede contradecir el estándar: si lo contradice, gana el estándar y la instancia se corrige.

**Cómo se sabe cuál es.** Un archivo que dice **cómo tiene que ser** algo es estándar y vive en `../Ouroboros/`. Uno que dice **qué se hace hoy** es instancia. Uno que dice **con qué** es implementación. Uno que dice **por qué** es tesis, y vive en `../Tesis/`.

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | `./mantenimiento/editar/editar.md` | no hay edición |
| **Se produce una decisión, una frase o un descarte** | **`./mantenimiento/notas/notas-tesis.md`** (la regla vive en `../AGENTS.md`, `Escribir notas`) | el turno no está entregado |
| La vista cambió | `./mantenimiento/notas/notas-tesis.md`, `La vista muta`: fila nueva, la vieja no se edita | se toma lo viejo como verdad |
| **Se compila la tesis** | `./mantenimiento/notas/notas-tesis.md`, `Compilar`: lo compilado va a `../notas/generaciones/` con su vista | la tesis se toma como definitiva |
| Se purga algo de lo viejo | `./mantenimiento/notas/notas-tesis.md`, `Purga`: se anota su vista y se purga | se pierde lo que se creía |
| **Se emite cualquier archivo** | `../Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md`, `Entrega como contribución` | no se emite |
| **Se escribe o corrige un proceso** | **`./mantenimiento/editar/enrutar-formato.md`** | el proceso se escribe por costumbre |
| **Se escribe un archivo final** | **`claridad`**: el entregable habla del mensaje, no del mensajero | declara su estado y deja de ser entregable |
| Se va a mutar cualquier cosa | `../Ouroboros/procesos/integridad.md`, **siempre** | no se muta |
| Se saca algo del estándar | `../notas/actuales.md`, entero y con su archivo | se pierde el porqué |
| El cambio toca el **estándar** | `../Ouroboros/CRITERIO.md` y `./mantenimiento/editar/editar.md`, paso 9 | el estándar se cambia sin revisar sus instancias |
| El cambio produce o reemplaza un proceso | `../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md` | se edita sobre el proceso existente |
| Se crea un subproceso | `../Ouroboros/2 S.A.R.A — mutación/Proceso PROMETEA.md`: **integridad antes, sí o sí** | se crea lo que debía rehacerse |
| Se audita el estado del repo | `./mantenimiento/chequear/auditar-configuracion.md` | no hay auditoría |
| Se mide si un agente es ACERO | `../Ouroboros/procesos/medir-acero.md` | no se declara ACERO |
| **Se chequea el estado del piso** | **`./piso/piso.ps1`** (las seis unidades) y `../Ouroboros/piso.md` | no hay veredicto |
| **Se entregó un cambio** | `./mantenimiento/chequear/`: **editar cambia, chequear verifica** | el cambio no está entregado |

**Vacío.** Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado, su rastro, y **sus filas de notas si produjo algo que valga.** Un turno sin archivo cambiado no es una edición; uno con decisión y sin fila no está entregado.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre; sin notas no hay tesis.