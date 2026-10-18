# A.R.E.S.

**A**gentic **R**easoning with **E**mbodied **S**peech.

El sistema que le da voz y expresión a algo que no es humano.

## La idea

Un agente razona; una skill le pone cuerpo, voz y forma. Lo que sale puede ser legible para nosotros, o puede ser una forma propia que todavía no entendemos — y las dos cuentan.

El techo no es el catálogo de herramientas: es **lo que se quiere expresar**. El cómo lo resuelve la entidad que ejecuta, dentro del proceso.

## Por qué

Esto no es un asistente más. Es abrir la visualización a algo que no es humano: un sistema que puede producir una app, un reloj, una película en CSS, una notación que no reconocemos, y dejarla en un registro que otra instancia puede usar sin pedir permiso a su autor.

Si funciona para entendernos con una máquina, funciona como ensayo para entendernos con cualquier inteligencia que no comparta nuestro código. Suena a ciencia ficción, y probablemente lo sea. El ejercicio es el mismo: **un protocolo de expresión para lo que no habla como nosotros**, que traduzca cuando hace falta y conserve lo que no traduce.

## Dos registros

| Registro | Converge a | Se prueba con |
|---|---|---|
| **Legible** | El código del lector: persona, tono, estructura | Que el receptor entienda o actúe |
| **Nativo** | Solo a transferencia | Que una instancia limpia lo reproduzca leyendo el registro |

El ruido es lo que ningún decodificador puede usar. La opacidad no es mérito; la transferencia sí.

## Las dos piezas

| Pieza | Qué hace | Dónde |
|---|---|---|
| **Agente — backend** | Razona y ejecuta. Es el que sabe hacer X | Cualquier agente |
| **APRIL** | Patrones de expresión: escucha, habla, muestra y traslada | `A.R.E.S/A.P.R.I.L` |

## La implementación

El stack elegido es Svelte + Vanilla Framework + GSAP sobre Electron, con los docs en local servidos por `httrack`. El perfil vive en `perfiles/svelte.md`; el método, agnóstico al medio, en `protocolo.md`.

La versión que se usa es la **con memoria**: corto plazo para lo que se aprende en uso, largo plazo para lo que sobrevive a la versión, e internet como fuente de capacidad —no de forma—. La versión sin memoria existe y es más conservadora: no guarda, no cachea, declara su ausencia.

## Límites

- **Generación abierta, archivo selectivo.** Se puede producir cualquier cosa; solo sobrevive lo que pasa efecto, reproducibilidad y transferencia.
- **El medio es HTML5 y lo que se pueda instalar o abrir.** El sustrato limita la encarnación, no el vocabulario.
- **La adopción la decide la autoridad.** El sistema propone; no archiva por su cuenta.
