# Leer el estado

**Tipo:** ley. Se aplica, no se ejecuta.
**Lector:** autoridad y ejecutor.
**Alcance:** todo artefacto de este repositorio.
**Dueño:** la autoridad.
**Estado:** vigente.

**Tarea:** leer.
**Carga:** `../../Alineacion de tareas/README.md`; el documento de la tarea.
**Produce:** la fila, el estado y la lectura de sistema.
**Cierra en:** `editar.md` si hay cambio; `cerrar.md` si no.

## 0. Lectura de sistema

### Unidad

La unidad es la tarea, no el ejecutor. Una tarea recibe, calcula, emite y responde. El ejecutor la realiza; la autoridad es su dueña; las sub-tareas son procesos internos.

### Declaración

Antes de una decisión que toca la base o el entorno, rige `Conversacional` 9: la forma, la Prueba y el Falsificador viven allí; la constitución no los repite.

### Disparador

**Sistema, no información.** El disparador no añade contenido: cambia la unidad de la petición. Sin fila, la petición es información; con fila, es tarea: frontera, retorno y consecuencia.

**Prueba:** ¿la respuesta nombra la fila y la consecuencia antes del contenido?
**Falsificador:** una respuesta que empieza por el dato; un disparador leído como índice de información.

## 1. Leyes de la base

### LEY 0 — Idea vs implementación

Todo lo que sea idea vive en `Alineacion de tareas/`. La implementación no entra. Si no es en `Alineacion de tareas/`, no se toca.

**Enunciado:** un documento de la base no puede necesitar SARA, APRIL, DSH, WAX, skills, ejecutores con nombre ni el instalador para tener sentido. Las implementaciones se nombran solo como ejemplo marcado y la regla se sostiene sin ellas.

**Prueba:** quita toda referencia a implementaciones concretas; si el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Falsificador:** un documento de `Alineacion de tareas/` que no se entiende sin nombrar la implementación.

### LEY 1 — El disparador apunta, no contiene

`AGENTS.md` es el disparador que enruta, no un manual. Contiene solo condición, destino y consecuencia. No contiene reglas, ejemplos, explicaciones ni copias de la base. Si una fila no cambia qué se carga, sobra. Si una línea no es condición, destino o consecuencia, sobra. Si no cabe en una pantalla, no es disparador. Aplica a todo disparador de enrutamiento, por ejemplo `AGENTS.md` y el de SARA.

**Prueba:** abre `AGENTS.md`; si tiene una regla, un ejemplo o una explicación, no es disparador. Si cada fila cambia lo que se carga, es disparador.

**Falsificador:** `AGENTS.md` con prosa, reglas, ejemplos, destinos duplicados o una fila que no cambia la carga.

### LEY 2 — Disparador primero

Toda tarea empieza en el disparador; `AGENTS.md` es el ejemplo vigente. Si no hay fila, no se ejecuta: se declara el vacío y se decide si se agrega una fila. Toda norma, campo o tarea nueva que cambie el disparador se enruta en él en el mismo cambio; si no, no entra. Hay un solo disparador vigente por repositorio: el de la raíz. Uno anidado no se inyecta ni compite con la raíz: rige solo si una fila de la raíz lo carga, y se neutraliza si aparece sin fila.

**Prueba:** ¿la tarea tiene fila? ¿El cambio se enrutó en el mismo cambio? ¿El anidado se cargó por fila y no por inyección?

**Falsificador:** una tarea sin fila; un cambio que deja el disparador viejo; un `AGENTS.md` anidado que se inyecta o enruta sin fila.

## 4. Mapa del núcleo

El mapa es el catálogo de lo que existe. Si un artefacto no tiene fila, no existe en la base. Si tiene fila y no tiene implementación, existe como mecanismo, pero no está implementado en esta era.

| Documento | Tareas | Mecanismo | Invariante | Prueba |
|---|---|---|---|---|
| `../../Alineacion de tareas/Derrotero.md` | enrutar | Contrato, ciclo, capacidades y vacíos | La petición se convierte en tarea; la ausencia se declara | Una instancia limpia ejecuta la tarea |
| `../../Alineacion de tareas/Escritura/Leyes de Diseño de Instrucciones.md` | instruir | Compuertas, anclas y entregable | La tarea se ejecuta sin preguntar | Una instancia limpia ejecuta la tarea |
| `../../Alineacion de tareas/Procesos principales/Conversacional.md` | interactuar, decidir | Autoridad, posición, fuentes y trazabilidad | La autoridad responde; la tarea se reconstruye | Prueba de Rendición |
| `../../Alineacion de tareas/Procesos principales/Autonomo.md` | ejecutar | Reversibilidad, perímetro y punto de control | Lo irreversible no se ejecuta sin autoridad | Clasificación de reversibilidad |
| `../../Alineacion de tareas/Escritura/Reglas de escritura.md` | escribir | Legibilidad y registro | El mensaje sobrevive al medio | El receptor actúa sin preguntar |
| `../../Alineacion de tareas/Reglas de mutación.md` | mutar | Marco de origen | La fuente no se edita; el cambio se declara | Cambio trazable al origen |
| `../../Alineacion de tareas/Pruebas/` | evaluar | Rendición y utilidad | Se reconstruye sin el ejecutor | Las pruebas pasan |
| `../../Alineacion de tareas/A.R.E.S/` | expresar | Legible y del ejecutor | La forma transfiere | Una instancia limpia la reproduce |
| `../../Alineacion de tareas/Procesos principales/Registro.md` | registrar | Memoria en dos plazos, fuentes y Testimonio | La tarea se reconstruye sin la conversación | Una instancia nueva continúa desde el cierre |

**Cuerpo de principios.** `Conversacional`, `Autonomo` y `Registro` son un solo documento partido en tres por dependencia de lectura: se puede conversar sin ejecutar; no se puede ejecutar sin conversar. `Conversacional` decide y emite; `Autonomo` agrega el acto que altera el entorno; `Registro` conserva lo que las otras dos producen. La partición es de lectura, no de vigencia: la norma de una parte rige en las tres y ninguna parte se cita sola.

**Prueba:** una norma de `Conversacional` se aplica a una tarea de `Autonomo` sin copiarse. **Falsificador:** se cita una parte como el cuerpo; una norma del cuerpo se repite en otra parte.

**Derrotero.** Es la forma del disparador: no es parte del cuerpo y no se cita como norma; se implementa en el disparador de la era.

**Generación, no acumulación.** El mapa se genera por ejes de tarea; un caso nuevo no agrega fila. Si un caso exige fila nueva, faltan ejes o sobra un duplicado.

**Prueba:** agregar un caso no requiere fila nueva. **Falsificador:** el mapa crece por caso.

**Aplicación:** cada documento declara la tarea que agrega (`Aplica a`). Fuera del cuerpo de principios, una norma rige solo la tarea que su documento declara. En el cuerpo, la norma de una parte rige en las tres: la parte declara la entrada, no el límite.

**Ejemplo:** `../../Alineacion de tareas/Escritura/Reglas de escritura.md` declara `Aplica a: escribir`; se activa en todo documento con tarea `escribir`.

**Presupuesto:** por tarea, no por fila. Muchas implementaciones de una tarea no cuentan; una tarea nueva sí.

## 9. Portabilidad

La base se puede extraer del repo, imprimir o compilar. No depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de ninguna implementación. El disparador de la era (`AGENTS.md`) apunta a `../../faber/Derrotero.md`; la base no apunta al disparador.

**Autocontención.** `Alineacion de tareas/` contiene ideas, no su aplicación. Aplicar una idea —llenar un mapa, correr un Prueba, renderizar, implementar— ocurre fuera y no modifica la base. Si para aplicar hay que cambiar un documento de la base, no es aplicación: es una idea nueva y se consulta.

**Prueba:** aplicar una idea no edita ningún archivo de la base.
**Falsificador:** aplicar una idea editando la base.

**Idea primero.** La implementación es una instancia descartable; la idea escrita es lo que sobrevive. Toda implementación parte de una idea en la base; lo que no está escrito no se implementa, se propone.

**Prueba:** ¿la implementación cita una idea escrita antes? ¿La idea existe sin la implementación?
**Falsificador:** se implementa sin idea; la idea se escribe después para justificar.

**Perspectiva no humana.** La base no define «no humano»; lo mide. Una tarea es no humana si produce una posición, una ausencia o un patrón que la autoridad no podía ver. El cómo vive en `Conversacional` (posición, posición faltante, independencia, patrón); la constitución no lo repite.

**Prueba:** ¿la tarea produjo una vista, una ausencia o un patrón que la autoridad no podía ver? ¿Está en el ledger?
**Falsificador:** se define «no humano» como estilo; se presenta opacidad como logro; no hay posición, ausencia ni patrón nuevo.

