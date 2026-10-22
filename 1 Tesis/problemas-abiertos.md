# Problemas abiertos

**Unidad:** nivel.
**Aplica a:** ubicar.
**Tipo:** registro. No decide, no ejecuta: dice qué problema del campo toca qué pieza del repo.
**Lector:** quien va a decidir en qué gastar el tiempo.
**Dueño:** la autoridad.
**Estado:** vigente.

## Por qué existe

Este repo tiene piezas sin saber **qué problema resuelve cada una**. Y el campo tiene problemas documentados sin que nadie haya mapeado sus procesos contra ellos.

Este archivo es ese mapa. **No dice que este repo resuelva los problemas: dice cuáles toca, con qué, y qué le falta.**

## El estado del campo

Diez problemas abiertos, según el seguimiento de abril de 2026. **Ninguno resuelto.**

| # | Problema | Estado | ¿Lo toca este repo? |
|---|---|---|---|
| 1 | Alineación y valores | Parcial | **sí** |
| 2 | Razonamiento multi-paso fiable | Parcial | parcial |
| 3 | Eliminación de alucinación | Parcial | **sí, directo** |
| 4 | Interpretabilidad mecanicista | Progresando | no |
| 5 | Eficiencia de cómputo | Progresando | no |
| 6 | Comprensión multimodal | Progresando | no |
| 7 | Agentes autónomos con herramientas | Parcial | **sí** |
| 8 | Contexto largo | Progresando | no |
| 9 | IA corpórea | **Abierto** | no |
| 10 | Calidad de datos | **Abierto** | no |

**Tres de diez, y una es central.** Lo que no toca, no lo toca por una razón: la interpretabilidad es a nivel de pesos, la eficiencia es de infraestructura, el contexto largo es de arquitectura, el cuerpo necesita cuerpo, y los datos necesitan datos. **No es una falta: es un lugar claro.**

## El paper que valida la pieza central

*"Evaluating large language models for accuracy incentivizes hallucinations"*, **Nature**, abril 2026.

> *"under standard scoring, **guessing is a dominant strategy**. A model that guesses outscores a trustworthy model that abstains when uncertain."*

El caso concreto del paper: **o4-mini supera a GPT-5-mini en exactitud con más de 3/4 de error**, solo porque el segundo **se abstiene.**

**La industria premia adivinar sobre decir «no sé».**

Y la solución que propone no es un modelo mejor: es **`open rubric`** — declarar el sistema de puntuación junto con la pregunta. Con eso, una mitigación que **antes bajaba la nota** ahora la sube en los cuatro modelos frontera probados.

### Lo que eso significa aquí

`nivel-de-fuente` ya tiene **`Vacío:` con fecha de corte**, y `N5` existe como nivel legítimo. **Este repo ya paga por abstenerse.**

> **El repo lo hizo por criterio. La ciencia llegó al mismo sitio por medición.** Eso no es coincidencia: es que la abstención declarada es la única forma de que un sistema no adivine, y el campo acaba de publicarlo en la revista más dura del año.

**Lo que falta para que sea las dos cosas:** declarar **el costo del error**, no solo el hueco. Hoy se dice «no sé»; no se dice «y equivocarme aquí cuesta tanto».

## Problema por problema

| Problema abierto | La pieza que lo toca | Qué tiene hoy | Qué le falta |
|---|---|---|---|
| **alucinación por incentivo** | `Vacío:` · `nivel-de-fuente` N0–N5 | abstención declarada con fecha | **el costo del error declarado** |
| **sycophancy** | `sesgo declarado` · la perspectiva que puede contradecir | una mirada que no confirma | un ejecutor que **no** busque agradar, probado |
| **sobreconfianza** | `Retiene` · `Techo` · peor caso | el techo mide lo que sobrevive | **reportar el peor caso, no la media** |
| **sobre-dependencia** | `fricción` · `cognitive forcing` | la decisión pasa por el que la toma | **probar sobre un agente, no sobre un humano** |
| **agentes multi-paso** | `fricción` sin rama de imposición · `integridad` nivel 0 | la decisión no se puede saltar | **que el piso corra en dos ejecutores** |
| **evaluación de agentes** | `talento utilizable` · `piso` | consistencia entre ejecutores | **que se corra** |
| **alineación de valores** | `mundo.md` · `fricción` · `ayuda-no-pedida` | el sistema no puede actuar sin contestar | que conteste **bien**, y eso no está garantizado |
| **razonamiento fiable** | compuertas de `manipulacion de procesos` | el paso N+1 exige la salida del N | que el paso N sea **verificado**, no solo declarado |

La columna de la derecha es el diseño que corresponde a cada problema. **No es una lista de pendientes: es la pieza que el repo tiene que escribir para esa fila.**

## Lo que este repo no resuelve, y hay que decirlo

**La alucinación como fenómeno.** El paper demuestra que la presión viene del *next-token prediction*, y eso es estructural: no lo arregla ningún proceso. Lo que sí se arregla es **el incentivo**, que es la mitad que se puede tocar.

**La alineación de valores.** El sistema puede garantizar que **no actúe sin contestar**. No puede garantizar que conteste bien. **La fricción garantiza la pregunta, no la respuesta.**

**El harness.** Si el proceso decide todo, un modelo barato empata **por la razón equivocada**. Rige `../S.A.R.A/Pruebas/prueba de talento utilizable.md`: la prueba mide consistencia entre ejecutores, no identidad.

## Lo que pone a este repo frente al campo

No la arquitectura: **la asignación.**

El campo publica listas de problemas; los repos publican capacidades. **Nadie publica las dos columnas juntas.** **Este archivo une las dos columnas.**

## Prueba

¿Cada problema del campo tiene su pieza, o se declara que no la tiene? ¿Cada «falta» es concreta? ¿Lo que no se resuelve está dicho?

**Falsificador:** un problema presentado como resuelto sin corrida; una pieza asignada a un problema que no toca; una capacidad reclamada sin decir qué le falta; un problema del campo que se omite para que el mapa se vea completo.

## Transiciones

- La falta es de corrida → `../mantis/piso/` y `../S.A.R.A/Pruebas/`.
- La falta es de diseño → `./piso/` o `../Ouroboros/`, con su `Acta`.
- El problema no corresponde a este repo → se declara y no se toca: `Agentes/` es la era.
- En cualquier otro caso → se entrega y se cierra.
