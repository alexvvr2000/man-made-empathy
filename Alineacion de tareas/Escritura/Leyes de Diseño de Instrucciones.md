# Leyes de Diseño de Tareas de Instrucción

**Unidad:** tarea.
**Aplica a:** instruir
**Tipo:** ley. Se sigue, no se interpreta.
**Lector:** autoridad y ejecutor.
**Alcance:** toda tarea de instrucción que una autoridad delega a un ejecutor.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

Una tarea de instrucción es una delegación de autoridad a un ejecutor. La tarea debe poder ejecutarse sin preguntar; el que la escribe no la ejecuta. La tarea no describe al ejecutor: describe la operación que lo habilita.

Una tarea de instrucción no le pide al ejecutor que entienda: le pide que ejecute un cálculo. Si necesita entender para ejecutar, la tarea falló. El ejecutor no interpreta: recorre compuertas.

Una tarea que necesita explicar al ejecutor no es instrucción: es una descripción. Una tarea que el ejecutor puede saltarse no es ley: es un consejo.

`Instrucción` se lee como `tarea de instrucción`; la unidad es la tarea.

## 1. Cálculo antes de la emisión

**Enunciado:** la instrucción obliga a calcular el estado antes de emitir la señal siguiente. Se escribe como compuertas secuenciales, no como lista de consejos.

**Prueba:** ¿el paso N+1 exige la salida del N? Si no, no hay cálculo.

**Falsificador:** una instrucción que se puede resolver leyendo solo el final.

## 2. Lenguaje blando y ramas cerradas

**Enunciado:** sin verbos de sugerencia. Toda bifurcación cierra con una rama por defecto.

**Prueba:** ¿queda «procura», «idealmente» o «si es necesario»? ¿Hay una rama «en cualquier otro caso»?

**Falsificador:** una instrucción que deja al ejecutor decidir si aplica.

## 3. Propiedades del resultado, no herramientas

**Enunciado:** la instrucción define propiedades y forma del resultado; no nombres de herramientas, comandos, modelos ni plataformas.

**Prueba:** ¿la instrucción se entiende sin nombrar una herramienta? ¿El resultado tiene forma exacta?

**Falsificador:** una instrucción que dice «usa X» o que no define la salida.

## 4. Compuertas de estado

**Enunciado:** el artefacto del paso N es el insumo obligatorio del paso N+1. Prohibido saltar.

**Prueba:** ¿cada transición declara «prohibido ejecutar N+1 sin la salida de N»?

**Falsificador:** una lista de viñetas sin dependencia de orden.

**Numeración.** La numeración de compuertas es continua; si se quita una, se renumera. Rige `Reglas de escritura.md` 1.17.

## 5. Anclas léxicas

**Enunciado:** toda clasificación, medición o supuesto se declara en una línea de 5 a 12 palabras antes o junto a la acción.

**Prueba:** ¿cada acción que exige juicio tiene su ancla?

**Falsificador:** una acción sin ancla; un ancla que no clasifica nada.

**Anclas de lectura.** No son solo para la máquina: son para que el lector sepa qué está leyendo y qué quedó fuera. Cada una declara el límite de lo que afirma.

- `Vista: [posición] | No ve: [límite]` — desde dónde se habla y qué no se ve desde ahí. Sirve para que el lector sepa qué parte del mundo quedó fuera.
- `Vista faltante: [posición] | Esquiva: [limitación] | Ausencia: [qué falta] | Cambia: [decisión]` — la vista que la autoridad no ocupa, la limitación que esquiva, la ausencia que revela y la decisión que cambia. Sirve para mover la vista, no para imponerla.
- `Fuente: [id] | Nivel: [N1-N5] | Origen: [medio] | Autor: [tipo:nombre] | Independencia: [A|B|C]` — de dónde sale el dato, qué nivel tiene, quién responde por él y si es independiente. Sirve para que el lector pueda volver a la fuente.
- `Testimonio: [fuente] | Vínculo: [afectado|mantenedor|crítico|beneficiario] | Contexto: [...] | Consentimiento: [...]` — quién vivió la experiencia, qué relación tiene, en qué contexto y con qué consentimiento. Sirve para no hablar por la fuente.
- `Confirma: [posición] | Evidencia: [N1-N5] | Objeta: [límite] | Beneficia: [tipo:nombre]` — qué posición se valida, con qué evidencia, con qué objeción y a quién beneficia. Sirve para no dar la razón por cortesía.

La escala N1-N5 se define en `../Procesos principales/Registro.md`.

## 6. Transiciones explícitas

**Enunciado:** la instrucción cierra con transiciones de estado y una rama por defecto.

**Prueba:** ¿hay cierre, handoff y «en cualquier otro caso»?

**Falsificador:** una instrucción que termina sin decir qué sigue.

## 7. El entregable es el último estado

**Enunciado:** el entregable es el estado final completo, no el relato del cambio ni la conversación que lo produjo.

**Prueba:** tapa la conversación y lee solo el entregable; ¿el receptor puede usarlo?

**Falsificador:** un entregable que necesita el hilo; una lista de cambios sobre la versión vieja.

## 8. Regla sin falsificador no entra

**Enunciado:** toda ley declara el caso que la incumple. Sin falsificador no es ley: es una opinión.

**Prueba:** ¿puedes enunciar el caso que la rompe? Si no, sobra.

**Falsificador:** una ley que nadie ha visto aplicarse; una ley sin caso de fallo.

## 9. El marco no se ejecuta: se convierte

**Enunciado:** una instrucción no cita un marco; lo convierte en compuertas. Cada compuerta declara la norma del marco que descarga y la señal que la prueba.

**Prueba:** ¿hay compuertas o el nombre de un marco? ¿cada compuerta nombra su norma?

**Falsificador:** «implementa según [marco]» | un paso que no descarga norma | marco citado sin conversión.

## 10. Admisión de ideas

**Enunciado:** una instrucción no descarta una idea sin declarar la prueba que la descarta. Rige `Conversacional` 22.

**Prueba:** ¿hay prueba declarada antes del descarte?

**Falsificador:** descarte sin prueba; «no es valioso» sin recibo; idea relegada sin medirla.
