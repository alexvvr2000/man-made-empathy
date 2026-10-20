# Constitución de la base

**Tipo:** ley. Se aplica, no se ejecuta.
**Lector:** autoridad y ejecutor.
**Alcance:** todo artefacto de este repositorio.
**Dueño:** la autoridad.
**Estado:** vigente.

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

Todo lo que sea idea vive en `Bases de diseño/`. La implementación no entra. Si no es en `Bases de diseño/`, no se toca.

**Enunciado:** un documento de la base no puede necesitar SARA, APRIL, DSH, WAX, skills, ejecutores con nombre ni el instalador para tener sentido. Las implementaciones se nombran solo como ejemplo marcado y la regla se sostiene sin ellas.

**Prueba:** quita toda referencia a implementaciones concretas; si el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Falsificador:** un documento de `Bases de diseño/` que no se entiende sin nombrar la implementación.

### LEY 1 — El disparador apunta, no contiene

`AGENTS.md` es el disparador que enruta, no un manual. Contiene solo condición, destino y consecuencia. No contiene reglas, ejemplos, explicaciones ni copias de la base. Si una fila no cambia qué se carga, sobra. Si una línea no es condición, destino o consecuencia, sobra. Si no cabe en una pantalla, no es disparador. Aplica a todo disparador de enrutamiento, por ejemplo `AGENTS.md` y el de SARA.

**Prueba:** abre `AGENTS.md`; si tiene una regla, un ejemplo o una explicación, no es disparador. Si cada fila cambia lo que se carga, es disparador.

**Falsificador:** `AGENTS.md` con prosa, reglas, ejemplos, destinos duplicados o una fila que no cambia la carga.

### LEY 2 — Disparador primero

Toda tarea empieza en el disparador; `AGENTS.md` es el ejemplo vigente. Si no hay fila, no se ejecuta: se declara el vacío y se decide si se agrega una fila. Toda norma, campo o tarea nueva que cambie el disparador se enruta en él en el mismo cambio; si no, no entra. Hay un solo disparador vigente por repositorio: el de la raíz. Uno anidado no se inyecta ni compite con la raíz: rige solo si una fila de la raíz lo carga, y se neutraliza si aparece sin fila.

**Prueba:** ¿la tarea tiene fila? ¿El cambio se enrutó en el mismo cambio? ¿El anidado se cargó por fila y no por inyección?

**Falsificador:** una tarea sin fila; un cambio que deja el disparador viejo; un `AGENTS.md` anidado que se inyecta o enruta sin fila.

## 2. Tipos de norma

| Tipo | Verbo | Discreción | Cumplimiento | Violación |
|---|---|---|---|---|
| Ley | DEBE | ninguna | compuerta | falla |
| Regla | DEBERÍA | operativa | revisión | se corrige |
| Principio | PUEDE | criterio | declaración | se declara |

Una norma se clasifica por su modo de cumplimiento, no por su importancia. Si no se puede clasificar, no entra.

## 3. Admisión y destino

### 3.1 Qué es cada documento

| Documento | Qué es | Para qué sirve | Qué norma entra |
|---|---|---|---|
| `constitucion.md` | Meta-marco | Define qué es norma, cómo se admite, cómo se valida y cómo se muta | La que gobierna la norma misma: tipo, admisión, mapa, validación, mutación |
| `Principios.../Conversacional.md` y `Autonomo.md` | Principios | Fija el juicio y la conducta de la tarea | La que gobierna cómo se decide y cómo se ejecuta: autoridad, perímetro, reversibilidad, trazabilidad |
| `Leyes de Diseño de Instrucciones.md` | Leyes de instrucción | Fija cómo se escribe una instrucción | La que gobierna la forma de una instrucción: compuertas, anclas, falsificadores, transiciones |

**Regla de destino:** una norma se escribe en el documento cuya tarea gobierna. Si gobierna la norma misma, va a la constitución. Si gobierna el juicio, va a principios. Si gobierna la forma de una instrucción, va a las leyes. Si no encaja en uno de los tres, no es norma meta: es mecanismo, documento de tarea o implementación.

### 3.2 Clasificación y destino

Antes de las siete compuertas, se declara:

`Clasificación: cambio=[puede|debe] | uso=[una vez|recurrente] | destino=[constitución|principios|leyes de instrucción]`

- `puede` + recurrente → norma de capacidad: va al documento de su tarea; si es meta, a la constitución.
- `debe` + recurrente → regla de conducta: va al documento de su tarea; si es juicio, a principios; si es forma de instrucción, a las leyes.
- `una vez` → instrucción o delta: no entra a la base.
- **Efecto** → no entra: se registra y se mide; no se escribe como norma hasta que una decisión dependa de él.

**Prueba:** el destino es uno de los tres y la norma se entiende sin los otros dos.
**Falsificador:** una norma de tarea en la constitución; un principio en las leyes; una ley de instrucción en los principios.

**Prueba del efecto:** ¿alguien puede incumplirlo? **Falsificador:** una norma para un efecto que nadie puede incumplir.

### 3.3 Compuertas

Una norma entra solo si pasa las siete compuertas:

1. **Tipo.** ¿Es ley, regla o principio? Sin tipo, no entra.
2. **Derivación o duplicado.** ¿Se deriva de otra? Se absorbe o se referencia. ¿Falla por la misma razón que otra? Una sobra.
3. **Observabilidad.** ¿Su cumplimiento es observable? Si no, no entra.
4. **Decisión.** ¿Su ausencia cambia una decisión? Si no, sobra.
5. **Calibración.** ¿Puede una norma existente absorberla ajustando alcance, Prueba o ancla? Si sí, se calibra; no se crea.
6. **Prueba y falsificador.** ¿Declara el caso que la incumple? Sin eso, no entra.
7. **Evidencia y autoridad.** ¿Hay caso medido o fuente externa? Sin evidencia queda `en prueba`; sin autoridad no se aplica.

**Alta:** `Clasificación | Destino | Tipo | Enunciado | Prueba | Falsificador | Evidencia | Estado`.

**Estados:** `propuesta → en prueba → vigente → deprecada → retirada`.

**Operaciones:** alta, calibrar, fusionar, escindir, retirar. Toda operación deja registro y, si cambia el nombre, redirección.

**Presupuesto de la constitución:** no contiene normas de tarea. Si una norma necesita la constitución para entenderse, es meta; si no, va a su documento.

## 4. Mapa del núcleo

El mapa es el catálogo de lo que existe. Si un artefacto no tiene fila, no existe en la base. Si tiene fila y no tiene implementación, existe como mecanismo, pero no está implementado en esta era.

| Documento | Tareas | Mecanismo | Invariante | Prueba |
|---|---|---|---|---|
| `Derrotero.md` | enrutar | Contrato, ciclo, capacidades y vacíos | La petición se convierte en tarea; la ausencia se declara | Una instancia limpia ejecuta la tarea |
| `Leyes de Diseño de Instrucciones.md` | instruir | Compuertas, anclas y entregable | La tarea se ejecuta sin preguntar | Una instancia limpia ejecuta la tarea |
| `Conversacional.md` | interactuar, decidir | Autoridad, posición, fuentes y trazabilidad | La autoridad responde; la tarea se reconstruye | Prueba de Rendición |
| `Autonomo.md` | ejecutar | Reversibilidad, perímetro y punto de control | Lo irreversible no se ejecuta sin autoridad | Clasificación de reversibilidad |
| `Reglas de escritura.md` | escribir | Legibilidad y registro | El mensaje sobrevive al medio | El receptor actúa sin preguntar |
| `Reglas de mutación.md` | mutar | Marco de origen | La fuente no se edita; el cambio se declara | Cambio trazable al origen |
| `Pruebas/` | evaluar | Rendición y utilidad | Se reconstruye sin el ejecutor | Las pruebas pasan |
| `A.R.E.S/` | expresar | Legible y del ejecutor | La forma transfiere | Una instancia limpia la reproduce |
| `Registro.md` | registrar | Memoria en dos plazos, fuentes y Testimonio | La tarea se reconstruye sin la conversación | Una instancia nueva continúa desde el cierre |

**Cuerpo de principios.** `Conversacional`, `Autonomo` y `Registro` son un solo documento partido en tres por dependencia de lectura: se puede conversar sin ejecutar; no se puede ejecutar sin conversar. `Conversacional` decide y emite; `Autonomo` agrega el acto que altera el entorno; `Registro` conserva lo que las otras dos producen. La partición es de lectura, no de vigencia: la norma de una parte rige en las tres y ninguna parte se cita sola.

**Prueba:** una norma de `Conversacional` se aplica a una tarea de `Autonomo` sin copiarse. **Falsificador:** se cita una parte como el cuerpo; una norma del cuerpo se repite en otra parte.

**Derrotero.** Es la forma del disparador: no es parte del cuerpo y no se cita como norma; se implementa en el disparador de la era.

**Generación, no acumulación.** El mapa se genera por ejes de tarea; un caso nuevo no agrega fila. Si un caso exige fila nueva, faltan ejes o sobra un duplicado.

**Prueba:** agregar un caso no requiere fila nueva. **Falsificador:** el mapa crece por caso.

**Aplicación:** cada documento declara la tarea que agrega (`Aplica a`). Fuera del cuerpo de principios, una norma rige solo la tarea que su documento declara. En el cuerpo, la norma de una parte rige en las tres: la parte declara la entrada, no el límite.

**Ejemplo:** `Reglas de escritura.md` declara `Aplica a: escribir`; se activa en todo documento con tarea `escribir`.

**Presupuesto:** por tarea, no por fila. Muchas implementaciones de una tarea no cuentan; una tarea nueva sí.

## 5. Validación

Toda norma y todo documento se validan con el mismo esquema:

- Toda fila del mapa tiene tareas, mecanismo, invariante y Prueba.
- Toda norma tiene Prueba y falsificador.
- No hay duplicados que fallen igual.
- No hay huérfanos: toda implementación cita su fila del núcleo.
- No hay copias sin cita.
- Toda referencia resuelve dentro de la base.

**Prueba:** si una fila no tiene Prueba, no es norma; es una idea. Si una implementación no cita su núcleo, es una bifurcación.

**Falsificador:** una norma sin Prueba, una fila sin tareas, una implementación sin núcleo.

## 6. Mutación y origen

Toda mutación parte de un **marco de origen** y conserva ese marco. La forma puede cambiar; el origen no se edita. La mutación declara qué cambia, qué conserva y cómo se verifica. Las etiquetas de la era —`agente | instrucción | skill`— son ejemplos marcados; el mecanismo es agnóstico.

**Prueba:** el cambio se puede rastrear hasta su origen; la fuente no se editó.

**Falsificador:** una mutación sin origen, una fuente editada, un cambio sin declaración.

## 7. Agregar

1. La autoridad dice qué agregar.
2. Se lee `README.md`, luego esta constitución, luego `Reglas de escritura.md` y `Reglas de mutación.md` si aplica.
3. Se clasifica la norma, se declara su destino y se pasan las siete compuertas.
4. Se escribe con `Clasificación | Destino | Tipo | Enunciado | Prueba | Falsificador | Evidencia`.
5. Se actualiza el mapa, se valida y se registra.
6. Si no pasa, no entra; se reporta.

La lista de pendientes es local (`.contexto/pendientes.md`); no forma parte de la base y no se cita en los documentos.

## 8. Consistencia

La consistencia es una propiedad del mapa, no un documento aparte.

- **Inventario:** el mapa es el inventario. Lo que no tiene fila no existe; lo que tiene fila y no está implementado se declara como vacío.
- **Cambio formal:** typo, formato o comentario sin cambio de sentido. Se declara y no se revisa.
- **Cambio semántico:** cambia el sentido, una referencia, una tarea o un Prueba. Se revisan las filas que comparten tarea y las referencias que citan el documento.
- **Dependientes:** si cambia el núcleo, la implementación se invalida; si cambia una implementación, el núcleo no se toca.
- **Deriva:** al cambiar una idea, se aplica su `Prueba` a cada artefacto que declare esa tarea; si su `Falsificador` se cumple, hay deriva. El reporte nombra artefacto, ruta y línea, y no edita: la corrección la aplica la autoridad.
- **Poda:** una fila sin tarea se elimina; una copia sin cita se elimina; un huérfano se reporta y se corrige.
- **Reporte y aplicación:** la validación reporta; la mutación aplica con autoridad. El reporte no toca; la aplicación deja registro.

**Prueba:** `Cambio semántico → dependientes revisados | Cambio formal → sin revisión | Copia sin cita → se elimina | Huérfano → se reporta`.

**Falsificador:** un cambio semántico sin revisión; una copia sin cita; un huérfano sin reporte.

## 9. Portabilidad

La base se puede extraer del repo, imprimir o compilar. No depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de ninguna implementación. El disparador de la era (`AGENTS.md`) apunta a `README.md`; la base no apunta al disparador.

**Autocontención.** `Bases de diseño/` contiene ideas, no su aplicación. Aplicar una idea —llenar un mapa, correr un Prueba, renderizar, implementar— ocurre fuera y no modifica la base. Si para aplicar hay que cambiar un documento de la base, no es aplicación: es una idea nueva y se consulta.

**Prueba:** aplicar una idea no edita ningún archivo de la base.
**Falsificador:** aplicar una idea editando la base.

**Idea primero.** La implementación es una instancia descartable; la idea escrita es lo que sobrevive. Toda implementación parte de una idea en la base; lo que no está escrito no se implementa, se propone.

**Prueba:** ¿la implementación cita una idea escrita antes? ¿La idea existe sin la implementación?
**Falsificador:** se implementa sin idea; la idea se escribe después para justificar.

**Perspectiva no humana.** La base no define «no humano»; lo mide. Una tarea es no humana si produce una posición, una ausencia o un patrón que la autoridad no podía ver. El cómo vive en `Conversacional` (posición, posición faltante, independencia, patrón); la constitución no lo repite.

**Prueba:** ¿la tarea produjo una vista, una ausencia o un patrón que la autoridad no podía ver? ¿Está en el ledger?
**Falsificador:** se define «no humano» como estilo; se presenta opacidad como logro; no hay posición, ausencia ni patrón nuevo.

## 10. Gobierno

| Operación | Carga | Salida | Edita |
|---|---|---|---|
| Diseñar una tarea | `Lectura` + esta constitución | tarea declarada | solo autoridad |
| Ejecutar una tarea | `AGENTS.md` + doc de tarea | resultado + traza | según perímetro |
| Evaluar una tarea | `Pruebas/` | pasa o falla en N | no |
| Agregar una norma | `## 7` | admitido o rechazado | solo autoridad |
| Transformar una tarea | `## 6` | ancla + cambio | con autorización |
| Revisar una tarea | `Lectura` + doc | reporte | no |
| Consistencia | `## 8` | reporte | no |

**Regla:** toda tarea empieza en `AGENTS.md` (`LEY 2`). Si no hay fila, no se ejecuta.
