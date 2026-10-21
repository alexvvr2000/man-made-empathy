# Editar el repositorio

**Tarea:** editar.
**Carga:** `../../Alineacion de tareas/Escritura/Reglas de escritura.md`; `../../Alineacion de tareas/Reglas de mutación.md`.
**Produce:** el cambio con origen, antes, después y responsable.
**Cierra en:** `probar.md`.

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
| `./` (las cuatro tareas) | Meta-marco | Define qué es norma, cómo se admite, cómo se valida y cómo se muta | La que gobierna la norma misma: tipo, admisión, mapa, validación, mutación |
| `../../Alineacion de tareas/Procesos principales/Conversacional.md` y `../../Alineacion de tareas/Procesos principales/Autonomo.md` | Principios | Fija el juicio y la conducta de la tarea | La que gobierna cómo se decide y cómo se ejecuta: autoridad, perímetro, reversibilidad, trazabilidad |
| `../../Alineacion de tareas/Escritura/Leyes de Diseño de Instrucciones.md` | Leyes de instrucción | Fija cómo se escribe una instrucción | La que gobierna la forma de una instrucción: compuertas, anclas, falsificadores, transiciones |

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

## 6. Mutación y origen

Toda mutación parte de un **marco de origen** y conserva ese marco. La forma puede cambiar; el origen no se edita. La mutación declara qué cambia, qué conserva y cómo se verifica. Las etiquetas de la era —`agente | instrucción | skill`— son ejemplos marcados; el mecanismo es agnóstico.

**Prueba:** el cambio se puede rastrear hasta su origen; la fuente no se editó.

**Falsificador:** una mutación sin origen, una fuente editada, un cambio sin declaración.

## 7. Agregar

1. La autoridad dice qué agregar.
2. Se lee `../../Alineacion de tareas/README.md`, luego esta constitución, luego `../../Alineacion de tareas/Escritura/Reglas de escritura.md` y `../../Alineacion de tareas/Reglas de mutación.md` si aplica.
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

