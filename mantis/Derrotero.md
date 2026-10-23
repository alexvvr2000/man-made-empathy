# Derrotero de MANTIS

**MANTIS:** Memoria, Análisis, Navegación, Triangulación, Integridad y Sistema. Nombre del derrotero, no de quien lo ejecuta: lo implementa cualquier agente que lo cargue.

**Tarea:** editar, auditar y medir los archivos del repositorio.
**Tipo:** disparador. Solo las filas que coinciden se cargan; el resto no.
**Nivel:** **instancia.** Aplica la forma de .../Ouroboros/formato de ente.md.. No es estándar. **Nace de S.A.R.A:** rige ../acta.md., y sin esa acta MANTIS es indistinguible de un invento.
**Carta:** .../AGENTS.md.. Sin carta no se lee.
**Alcance:** .../Tesis/. y .../Ouroboros/.. **Este repo es el reino de las ideas:** lo que se ejecuta sale de aquí ya con formato de ente y vive fuera.
**Estándar:** .../Ouroboros/.. Se cita, no se copia.
**Forma:** .../Ouroboros/formato de ente.md., .formato de proceso.md., .mutacion.md..
**Puerta:** .../Ouroboros/CRITERIO.md..
**Abstracción:** .../Ouroboros/2 S.A.R.A — mutación/.. Se carga cuando el cambio toca una sub-tarea o un proceso.
**Integridad:** .../Ouroboros/procesos/integridad.md.. **Corre siempre antes de mutar:** el criterio no decide si corre, solo qué se hace con su veredicto.
**Claridad:** .../Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md..
**Manipulación de procesos:** .../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md.. Se carga cuando el cambio produce o reemplaza un proceso.
**Registro:** `.sesion-continua/mantis.db`. **Es la memoria: lo que no se anota se pierde con el contexto.** **Esquema:** `../notas/corrida-<uuid>/esquema.sql`.
**Memoria:** `../Ouroboros/procesos/memoria continua.md`. Se carga al recordar y al leer la memoria: dice qué se guarda y cómo se suplanta. **Su paso 8: cada interacción deja su entrada, no al final.**
**Ley:** ../mantenimiento/editar/editar.md..
**Formato:** ../mantenimiento/editar/enrutar-formato.md.: todo proceso se carga por las nueve piezas y los condicionales antes de escribirse. Rige .../Ouroboros/formato de proceso.md.; no lo copia.
**Piso:** ../piso/.. Corre aquí y ahora; la forma que sigue está en .../Ouroboros/piso.md..
**Carga:** ../deterrente.md.. Sin él, MANTIS ayuda a editar sin decir qué se pierde si deja de ayudar, y una herramienta que no declara su pérdida se conserva por costumbre.

## Los tres niveles

Una petición puede tocar tres cosas distintas, y cada una se trata distinto.

| Nivel | Dónde | Qué es | Si se rompe |
|---|---|---|---|
| **Estándar** | .../Ouroboros/. | la forma: cómo tiene que ser algo | se corrige y **se revisan sus instancias en el mismo acto** |
| **Instancia** | .../Tesis/., .../mantis/. | lo que se hace hoy o lo que explica el porqué | se corrige la instancia; el estándar no se toca |

**Regla.** Un cambio en el estándar obliga a revisar sus instancias en el mismo acto. Una instancia no puede contradecir el estándar: si lo contradice, gana el estándar y la instancia se corrige.

**Cómo se sabe cuál es.** Un archivo que dice **cómo tiene que ser** algo es estándar y vive en .../Ouroboros/.. Uno que dice **qué se hace hoy** es instancia. Uno que dice **por qué** es tesis, y vive en .../Tesis/.. **Lo que dice "con qué" no vive aquí: sale ya con formato de ente y se ejecuta fuera.**

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se cambia un archivo | ../mantenimiento/editar/editar.md. | no hay edición |
| **Se cambia el esquema de la memoria** | **../acta.md.**, .El esquema con UUID.: se acuña otro UUID y el anterior se declara sucedido | la base deja de saber con qué forma se escribió |
| **Se produce una decisión, una frase o un descarte** | **../mantenimiento/notas/notas-tesis.md.**: se anota con ../piso/anotar.ps1. (la regla vive en .../AGENTS.md., .Escribir notas.) | el turno no está entregado |
| **Se abre un turno con trabajo** | **`./piso/turno.ps1 -Abrir "..."`**: el turno no cierra sin su entrada | el turno se cierra sin dejar rastro |
| **Se guarda o se lee memoria** | **.../Ouroboros/procesos/memoria continua.md.**: posición, .Sostuve./.Contra./.Sostengo., y lo anterior se suplanta | la memoria guarda hechos y hereda verdades |
| **Termina un turno con archivos cambiados** | **../piso/notas.ps1.**: un archivo cambiado sin nota es .falla. | el turno se entrega sin rastro |
| Se cierra la sesión | `../piso/anotar.ps1 -Sesion -Estado <lo que midió el piso>` | la sesión se escribe de memoria |
| La vista cambió | ../mantenimiento/notas/notas-tesis.md., .La vista muta.: fila nueva, la vieja no se edita | se toma lo viejo como verdad |
| **Se compila la tesis** | ../mantenimiento/notas/notas-tesis.md., .Compilar.: lo compilado va a .../notas/generaciones/. con su vista | la tesis se toma como definitiva |
| Se purga algo de lo viejo | ../mantenimiento/notas/notas-tesis.md., .Purga.: se anota su vista y se purga | se pierde lo que se creía |
| **Se emite cualquier archivo** | .../Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md., .Entrega como contribución. | no se emite |
| **Se escribe o corrige un proceso** | **../mantenimiento/editar/enrutar-formato.md.** | el proceso se escribe por costumbre |
| **Se escribe un archivo final** | **.claridad.**: el entregable habla del mensaje, no del mensajero | declara su estado y deja de ser entregable |
| Se va a mutar cualquier cosa | .../Ouroboros/procesos/integridad.md., **siempre** | no se muta |
| Se saca algo del estándar | ..sesion-continua/mantis.db., entero y con su archivo | se pierde el porqué |
| El cambio toca el **estándar** | .../Ouroboros/CRITERIO.md. y ../mantenimiento/editar/editar.md., paso 9 | el estándar se cambia sin revisar sus instancias |
| El cambio produce o reemplaza un proceso | .../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md. | se edita sobre el proceso existente |
| Se crea un subproceso | .../Ouroboros/2 S.A.R.A — mutación/Proceso PROMETEA.md.: **integridad antes, sí o sí** | se crea lo que debía rehacerse |
| Se audita el estado del repo | ../mantenimiento/chequear/auditar-configuracion.md. | no hay auditoría |
| **Cambió una idea de la base** | **../mantenimiento/chequear/derivar.md.**: se reporta la deriva, no se corrige | el repo queda con artefactos apuntando a lo viejo |
| Se mide si un agente es ACERO | .../Ouroboros/procesos/medir-acero.md. | no se declara ACERO |
| **Se chequea el estado del piso** | **../piso/piso.ps1.** (las siete unidades) y .../Ouroboros/piso.md. | no hay veredicto |
| **Se entregó un cambio** | ../mantenimiento/chequear/.: **editar cambia, chequear verifica** | el cambio no está entregado |
| **Se emite el paper como documento** | **../compilar.ps1.**: LaTeX siempre, PDF si hay motor | el paper se queda en Markdown |

**Vacío.** Lo que no entra en una fila se declara .[VACÍO - SIN PROCESO]. y se pregunta; no se improvisa.

**Salida.** Todo turno deja un archivo cambiado, su rastro, y **sus filas de notas si produjo algo que valga.** Un turno sin archivo cambiado no es una edición; uno con decisión y sin fila no está entregado.

**Lectura.** Sin archivo no hay edición; sin rastro no hay cierre; sin notas no hay tesis.
