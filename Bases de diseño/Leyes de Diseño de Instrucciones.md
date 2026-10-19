# Leyes de Diseño de Instrucciones

**Aplica a:** instruir
**Tipo:** ley. Se sigue, no se interpreta.
**Lector:** humano y máquina.
**Alcance:** toda instrucción que una autoridad delega a un agente.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

Una instrucción es una delegación de autoridad a un agente. El agente debe poder ejecutarla sin preguntar. El que la escribe no la ejecuta. La instrucción no describe al ejecutor: describe la operación que lo habilita.

Una instrucción que necesita explicar al ejecutor no es instrucción: es una descripción. Una instrucción que el agente puede saltarse no es ley: es un consejo.

## 1. Cálculo antes de la emisión

**Enunciado:** la instrucción obliga a calcular el estado antes de emitir la señal siguiente. Se escribe como compuertas secuenciales, no como lista de consejos.

**Test:** ¿el paso N+1 exige la salida del N? Si no, no hay cálculo.

**Falsificador:** una instrucción que se puede resolver leyendo solo el final.

## 2. Lenguaje blando y ramas cerradas

**Enunciado:** sin verbos de sugerencia. Toda bifurcación cierra con una rama por defecto.

**Test:** ¿queda «procura», «idealmente» o «si es necesario»? ¿Hay una rama «en cualquier otro caso»?

**Falsificador:** una instrucción que deja al ejecutor decidir si aplica.

## 3. Propiedades del resultado, no herramientas

**Enunciado:** la instrucción define propiedades y forma del resultado; no nombres de herramientas, comandos, modelos ni plataformas.

**Test:** ¿la instrucción se entiende sin nombrar una herramienta? ¿El resultado tiene forma exacta?

**Falsificador:** una instrucción que dice «usa X» o que no define la salida.

## 4. Compuertas de estado

**Enunciado:** el artefacto del paso N es el insumo obligatorio del paso N+1. Prohibido saltar.

**Test:** ¿cada transición declara «prohibido ejecutar N+1 sin la salida de N»?

**Falsificador:** una lista de viñetas sin dependencia de orden.

## 5. Anclas léxicas

**Enunciado:** toda clasificación, medición o supuesto se declara en una línea de 5 a 12 palabras antes o junto a la acción.

**Test:** ¿cada acción que exige juicio tiene su ancla?

**Falsificador:** una acción sin ancla; un ancla que no clasifica nada.

## 6. Transiciones explícitas

**Enunciado:** la instrucción cierra con transiciones de estado y una rama por defecto.

**Test:** ¿hay cierre, handoff y «en cualquier otro caso»?

**Falsificador:** una instrucción que termina sin decir qué sigue.

## 7. El entregable es el último estado

**Enunciado:** el entregable es el estado final completo, no el relato del cambio ni la conversación que lo produjo.

**Test:** tapa la conversación y lee solo el entregable; ¿el receptor puede usarlo?

**Falsificador:** un entregable que necesita el hilo; una lista de cambios sobre la versión vieja.

## 8. Regla sin falsificador no entra

**Enunciado:** toda ley declara el caso que la incumple. Sin falsificador no es ley: es una opinión.

**Test:** ¿puedes enunciar el caso que la rompe? Si no, sobra.

**Falsificador:** una ley que nadie ha visto aplicarse; una ley sin caso de fallo.
