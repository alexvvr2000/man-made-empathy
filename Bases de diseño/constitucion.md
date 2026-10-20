# Constitución de la base

**Tipo:** ley. Se aplica, no se ejecuta.
**Lector:** humano y máquina.
**Alcance:** todo artefacto de este repositorio.
**Dueño:** la autoridad.
**Estado:** vigente.

## 0. Lectura de sistema

### Unidad

La unidad es la tarea, no el agente. Una tarea recibe, calcula, emite y responde. El agente es su ejecutor; la autoridad es su dueña; las sub-tareas son procesos internos.

### Declaración

Antes de una decisión que toca la base o el entorno, se declara:

`Sistema: propósito=[...] | actores=[...] | frontera=[...] | flujo=[...] | feedback=[...] | consecuencia=[...]`

- Si no se puede llenar, no se actúa: se lee o se pregunta.
- **Test:** otro reconstruye el sistema desde la declaración.
- **Falsificador:** una decisión sin lectura; una lectura que no nombra feedback ni consecuencia.

## 1. Leyes de la base

### LEY 0 — Idea vs implementación

Todo lo que sea idea vive en `Bases de diseño/`. La implementación no entra. Si no es en `Bases de diseño/`, no se toca.

**Enunciado:** un documento de la base no puede necesitar SARA, APRIL, DSH, WAX, skills, ejecutores con nombre ni el instalador para tener sentido. Las implementaciones se nombran solo como ejemplo marcado y la regla se sostiene sin ellas.

**Test:** quita toda referencia a implementaciones concretas; si el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Falsificador:** un documento de `Bases de diseño/` que no se entiende sin nombrar la implementación.

### LEY 1 — El disparador apunta, no contiene

`AGENTS.md` es el disparador que enruta, no un manual. Contiene solo condición, destino y consecuencia. No contiene reglas, ejemplos, explicaciones ni copias de la base. Si una fila no cambia qué se carga, sobra. Si una línea no es condición, destino o consecuencia, sobra. Si no cabe en una pantalla, no es disparador. Aplica a todo disparador de enrutamiento, por ejemplo `AGENTS.md` y el de SARA.

**Test:** abre `AGENTS.md`; si tiene una regla, un ejemplo o una explicación, no es disparador. Si cada fila cambia lo que se carga, es disparador.

**Falsificador:** `AGENTS.md` con prosa, reglas, ejemplos, destinos duplicados o una fila que no cambia la carga.

### LEY 2 — Disparador primero

Toda tarea empieza en `AGENTS.md`. Si no hay fila, no se ejecuta: se declara el vacío y se decide si se agrega una fila. Toda norma, campo o tarea nueva que cambie el disparador se enruta en `AGENTS.md` en el mismo cambio; si no, no entra. Hay un solo `AGENTS.md` vigente por repositorio: el de la raíz. Uno anidado no se inyecta ni compite con la raíz: rige solo si una fila de la raíz lo carga, y se neutraliza si aparece sin fila.

**Test:** ¿la tarea tiene fila? ¿El cambio se enrutó en el mismo cambio? ¿El anidado se cargó por fila y no por inyección?

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

**Test:** el destino es uno de los tres y la norma se entiende sin los otros dos.
**Falsificador:** una norma de tarea en la constitución; un principio en las leyes; una ley de instrucción en los principios.

**Test del efecto:** ¿alguien puede incumplirlo? **Falsificador:** una norma para un efecto que nadie puede incumplir.

### 3.3 Compuertas

Una norma entra solo si pasa las siete compuertas:

1. **Tipo.** ¿Es ley, regla o principio? Sin tipo, no entra.
2. **Derivación o duplicado.** ¿Se deriva de otra? Se absorbe o se referencia. ¿Falla por la misma razón que otra? Una sobra.
3. **Observabilidad.** ¿Su cumplimiento es observable? Si no, no entra.
4. **Decisión.** ¿Su ausencia cambia una decisión? Si no, sobra.
5. **Calibración.** ¿Puede una norma existente absorberla ajustando alcance, test o ancla? Si sí, se calibra; no se crea.
6. **Test y falsificador.** ¿Declara el caso que la incumple? Sin eso, no entra.
7. **Evidencia y autoridad.** ¿Hay caso medido o fuente externa? Sin evidencia queda `en prueba`; sin autoridad no se aplica.

**Alta:** `Clasificación | Destino | Tipo | Enunciado | Test | Falsificador | Evidencia | Estado`.

**Estados:** `propuesta → en prueba → vigente → deprecada → retirada`.

**Operaciones:** alta, calibrar, fusionar, escindir, retirar. Toda operación deja registro y, si cambia el nombre, redirección.

**Presupuesto de la constitución:** no contiene normas de tarea. Si una norma necesita la constitución para entenderse, es meta; si no, va a su documento.

## 4. Mapa del núcleo

El mapa es el catálogo de lo que existe. Si un artefacto no tiene fila, no existe en la base. Si tiene fila y no tiene implementación, existe como mecanismo, pero no está implementado en esta era.

| Documento | Tareas | Mecanismo | Invariante | Test |
|---|---|---|---|---|
| `Leyes de Diseño de Instrucciones.md` | instruir | Compuertas, anclas y entregable | La tarea se ejecuta sin preguntar | Una instancia limpia ejecuta la tarea |
| `Conversacional.md` | dialogar, decidir | Autoridad, vista, fuentes y trazabilidad | La autoridad responde; la tarea se reconstruye | Prueba de Rendición |
| `Autonomo.md` | ejecutar | Reversibilidad, perímetro y punto de control | Lo irreversible no se ejecuta sin autoridad | Clasificación de reversibilidad |
| `Reglas de escritura.md` | escribir | Legibilidad y registro | El mensaje sobrevive al medio | El receptor actúa sin preguntar |
| `Reglas de mutación.md` | mutar | Marco de origen | La fuente no se edita; el cambio se declara | Cambio trazable al origen |
| `Pruebas/` | evaluar | Rendición y utilidad | Se reconstruye sin el ejecutor | Las pruebas pasan |
| `A.R.E.S/` | expresar | Legible y nativo | La forma transfiere | Una instancia limpia la reproduce |
| `Registro.md` | registrar | Memoria en dos plazos, fuentes y testimonio | La tarea se reconstruye sin la conversación | Una instancia nueva continúa desde el cierre |
| `Tesis.md` | pensar | Humanidad y proceso no humano | La interfaz es humana; el mecanismo no | Un lector distingue interfaz, ética y residuo |

**Generación, no acumulación.** El mapa se genera por ejes de tarea; un caso nuevo no agrega fila. Si un caso exige fila nueva, faltan ejes o sobra un duplicado.

**Test:** agregar un caso no requiere fila nueva. **Falsificador:** el mapa crece por caso.

**Aplicación:** cada norma declara `Aplica a: [tarea]`. Una norma se activa si su `Aplica a` coincide con una tarea del documento. Si no coincide, no la rige. El documento no lleva lista de normas; la norma lleva su alcance.

**Ejemplo:** `Reglas de escritura.md` declara `Aplica a: escribir`; se activa en todo documento con tarea `escribir`.

**Presupuesto:** por tarea, no por fila. Muchas implementaciones de una tarea no cuentan; una tarea nueva sí.

## 5. Validación

Toda norma y todo documento se validan con el mismo esquema:

- Toda fila del mapa tiene tareas, mecanismo, invariante y test.
- Toda norma tiene test y falsificador.
- No hay duplicados que fallen igual.
- No hay huérfanos: toda implementación cita su fila del núcleo.
- No hay copias sin cita.
- Toda referencia resuelve dentro de la base.

**Test:** si una fila no tiene test, no es norma; es una idea. Si una implementación no cita su núcleo, es una bifurcación.

**Falsificador:** una norma sin test, una fila sin tareas, una implementación sin núcleo.

## 6. Mutación y origen

Toda mutación parte de un **marco de origen** y conserva ese marco. La forma puede cambiar; el origen no se edita. La mutación declara qué cambia, qué conserva y cómo se verifica. Las etiquetas de la era —`agente | instrucción | skill`— son ejemplos marcados; el mecanismo es agnóstico.

**Test:** el cambio se puede rastrear hasta su origen; la fuente no se editó.

**Falsificador:** una mutación sin origen, una fuente editada, un cambio sin declaración.

## 7. Agregar

1. La autoridad dice qué agregar.
2. Se lee `README.md`, luego esta constitución, luego `Reglas de escritura.md` y `Reglas de mutación.md` si aplica.
3. Se clasifica la norma, se declara su destino y se pasan las siete compuertas.
4. Se escribe con `Clasificación | Destino | Tipo | Enunciado | Test | Falsificador | Evidencia`.
5. Se actualiza el mapa, se valida y se registra.
6. Si no pasa, no entra; se reporta.

La lista de pendientes es local (`.contexto/pendientes.md`); no forma parte de la base y no se cita en los documentos.

## 8. Consistencia

La consistencia es una propiedad del mapa, no un documento aparte.

- **Inventario:** el mapa es el inventario. Lo que no tiene fila no existe; lo que tiene fila y no está implementado se declara como vacío.
- **Cambio formal:** typo, formato o comentario sin cambio de sentido. Se declara y no se revisa.
- **Cambio semántico:** cambia el sentido, una referencia, una tarea o un test. Se revisan las filas que comparten tarea y las referencias que citan el documento.
- **Dependientes:** si cambia el núcleo, la implementación se invalida; si cambia una implementación, el núcleo no se toca.
- **Deriva:** al cambiar una idea, se aplica su `Test` a cada artefacto que declare esa tarea; si su `Falsificador` se cumple, hay deriva. El reporte nombra artefacto, ruta y línea, y no edita: la corrección la aplica la autoridad.
- **Poda:** una fila sin tarea se elimina; una copia sin cita se elimina; un huérfano se reporta y se corrige.
- **Reporte y aplicación:** la validación reporta; la mutación aplica con autoridad. El reporte no toca; la aplicación deja registro.

**Test:** `Cambio semántico → dependientes revisados | Cambio formal → sin revisión | Copia sin cita → se elimina | Huérfano → se reporta`.

**Falsificador:** un cambio semántico sin revisión; una copia sin cita; un huérfano sin reporte.

## 9. Portabilidad

La base se puede extraer del repo, imprimir o compilar. No depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de ninguna implementación. El disparador de la era (`AGENTS.md`) apunta a `README.md`; la base no apunta al disparador.

**Autocontención.** `Bases de diseño/` contiene ideas, no su aplicación. Aplicar una idea —llenar un mapa, correr un test, renderizar, implementar— ocurre fuera y no modifica la base. Si para aplicar hay que cambiar un documento de la base, no es aplicación: es una idea nueva y se consulta.

**Test:** aplicar una idea no edita ningún archivo de la base.
**Falsificador:** aplicar una idea editando la base.

**Idea primero.** La implementación es una instancia descartable; la idea escrita es lo que sobrevive. Toda implementación parte de una idea en la base; lo que no está escrito no se implementa, se propone.

**Test:** ¿la implementación cita una idea escrita antes? ¿La idea existe sin la implementación?
**Falsificador:** se implementa sin idea; la idea se escribe después para justificar.

**Perspectiva no humana.** La base no define «no humano»; lo mide. Una tarea es no humana si produce una vista, una ausencia o un patrón que la autoridad no podía ver. El cómo vive en `Conversacional` (vista, vista faltante, independencia, patrón); la constitución no lo repite.

**Test:** ¿la tarea produjo una vista, una ausencia o un patrón que la autoridad no podía ver? ¿Está en el ledger?
**Falsificador:** se define «no humano» como estilo; se presenta opacidad como logro; no hay vista, ausencia ni patrón nuevo.

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
