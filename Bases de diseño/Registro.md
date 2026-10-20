# Registro de la tarea

**Unidad:** tarea.
**Aplica a:** registrar
**Tipo:** leyes y reglas de registro; mecanismos de fila.
**Alcance:** toda tarea que conserva estado, fuentes o continuidad.
**Lector:** humano y máquina. El registro declara su lector al emitir.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

La tarea no depende de la conversación: depende del registro. Lo que no se conserva no existe; lo que se lee entero se paga dos veces. El registro no es un diario ni una base de datos: es la forma mínima que permite a otra instancia reconstruir la tarea sin preguntar.

`Agente` se lee como `ejecutor`; la unidad es la tarea.

## Qué no es

- No es un diario: no registra actividad.
- No es una base de datos: el medio es un parámetro, no el contrato.
- No es la conversación: la comprime en cierres.

## 1. Dos registros

**Tipo:** ley.
**Enunciado:** toda tarea distingue un registro de sesión, que se vacía al cerrar, de un registro permanente, que no se edita: se reemplaza.
**Test:** cerrada la tarea, una instancia nueva continúa solo con el permanente; el de sesión no se cita.
**Falsificador:** se cita la sesión como fuente, o se edita una fila del permanente.

**Costo de omitirlo:** la sesión se contamina con la conversación y el permanente deja de ser constancia; la tarea se repite entera en la sesión siguiente.

## 2. Cierre encadenado

**Tipo:** ley.
**Enunciado:** toda tarea que se interrumpe deja un cierre con fin vigente, decisiones, pendientes y siguiente paso; la tarea siguiente arranca de ese cierre.
**Test:** una instancia nueva, con solo el cierre, reconstruye el siguiente paso sin la conversación.
**Falsificador:** la continuidad exige el hilo o un resumen oral.

**Costo de omitirlo:** el cierre se vuelve un resumen y la continuidad depende de quien recuerda.

## 3. Lectura por disparador

**Tipo:** regla.
**Enunciado:** el registro permanente se lee por el disparador que habilita la lectura, con límite; nunca entero.
**Test:** la consulta nombra el disparador y devuelve un conjunto acotado.
**Falsificador:** se vuelca el registro al contexto o se lee sin disparador.

**Costo de omitirlo:** el registro se come el contexto y la lectura cuesta más que la tarea.

## 4. Umbral de registro

**Tipo:** regla.
**Enunciado:** se registra en el nivel mínimo que permita reconstruir: sesión, paso o permanente. La actividad no entra al permanente.
**Test:** la fila está en el nivel que corresponde a su clausura.
**Falsificador:** actividad en el permanente; una decisión que clausura opciones queda en sesión.

**Costo de omitirlo:** el permanente se llena de ruido y la decisión que importa se pierde.

## 5. Testimonio

**Tipo:** regla.
**Enunciado:** toda afirmación sobre la experiencia de la gente declara al menos un testimonio con vínculo, contexto y consentimiento, o declara la ausencia.
**Test:** hay `Testimonio:` con persona o grupo, vínculo y contexto; o `Vacío:` con la búsqueda y el cierre.
**Falsificador:** se habla por la gente sin citarla; solo documentos; testimonio sin vínculo.

**Costo de omitirlo:** la IA simula a la gente desde documentos y la experiencia se vuelve información.

## Campos del mecanismo

No son normas: son la forma mínima de la fila. Una fila sin estos campos no entra.

```
Registro: [id] | Tipo: [sesión|paso|permanente] | Fecha | Autor
Fuente: [id] | Nivel: [N1-N5] | Origen | Autor | Extracto | Independencia | Contradice
Testimonio: [persona/grupo] | Vínculo | Contexto | Consentimiento
Vacío: [qué falta] | Dónde se buscó | Cierre
Cierre: [fin vigente | decisiones | pendientes | siguiente paso]
```

- `Nivel`: N1 medición directa, N2 fuente primaria, N3 precedente, N4 deducción, N5 memoria interna.
- `Independencia`: si comparte premisa con otra fuente, cuenta como una.
- `Contradice`: se muestra la contradicción; no se elige.
- `Vacío`: lo que falta se declara; no se rellena.

## Test de la tarea

Una instancia nueva, con solo el registro, reconstruye el siguiente paso. Una fuente se rastrea hasta una persona. Una contradicción se ve.

## Falsificadores

- Se cita la sesión como fuente.
- Se edita una fila del permanente.
- Se lee el registro entero.
- Se registra actividad en el permanente.
- Se habla por la gente sin testimonio.
- La continuidad exige la conversación.

## Transiciones

- Falta un hecho del entorno → `indagacion-instrumental`.
- Dos o más caminos con fricción → `deliberacion-estructurada`.
- El siguiente paso altera estado persistente → `entrega-operacion`.
- En cualquier otro caso → se entrega y se cierra.
