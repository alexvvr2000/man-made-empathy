# Bases de diseño

Imagina que mañana algo aterriza. No sabemos si tiene leyes, si obedece a alguien o si solo reacciona al viento. Antes de decidir si es una amenaza, un igual o una herramienta, hay dos preguntas que se pueden contestar sin hablar su idioma:

**¿Cómo se le da una instrucción?** y **¿cómo se sabe si responde por lo que hace?**

Este folder existe para esas dos preguntas. La primera se contesta escribiendo bien; la segunda, probando.

## Qué hay aquí

- **`Leyes de Diseño de Instrucciones.md`** — cómo se escribe algo que no se pueda saltar. Vale para una skill, un manual, un contrato o un mensaje a una máquina.
- **`Principios para agentes con autoridad/`** — cómo se juzga a quien ejecuta: qué es un mandatario, qué prueba que lo es, y qué no prueba.

No son dos niveles: son dos funciones. Uno escribe el encargo; el otro examina al que lo recibe.

## Orden de lectura

1. Las leyes, para saber cómo se construye una instrucción.
2. Los principios, para saber qué se le puede exigir a quien la ejecuta.
3. La **Prueba de Mandato**, para saber si lo cumple.

## La regla de la casa

Toda ley cierra con el caso que la incumple. Todo principio lleva su test. Una regla sin caso es una opinión con formato de norma.

## Dónde se prueba

- La prueba abstracta: **`Principios para agentes con autoridad/README.md`**.
- Una implementación de esta era: **`Agentes/Proyecto S.A.R.A/Pruebas/`**.

La prueba no depende de estas máquinas. La máquina es el primer caso donde se pudo correr.
