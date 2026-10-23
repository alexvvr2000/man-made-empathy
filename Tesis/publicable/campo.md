**Fecha:** 2026-10
**Versión:** 1 | **Licencia:** CC-BY-4.0
**Estado:** borrador para depósito. **No está sometido a arbitraje.**

# El mapa del campo

**Tipo:** entregable. Qué problema documentado toca cada pieza, qué le falta, y qué no se resuelve. **Lector:** quien va a decidir en qué gastar el tiempo.

## 1. Por qué existe

El campo publica listas de problemas; los proyectos publican capacidades. **Nadie publica las dos columnas juntas.** Este documento las une.

**No dice que el protocolo resuelva los problemas: dice cuáles toca, con qué, y qué le falta.**

## 2. Lo que ya existía

Nada de lo estructural es nuevo. Se dice con nombre, año y nivel.

| Pieza | De quién | Cuándo | Nivel | Qué es igual |
|---|---|---|---|---|
| la forma de proceso | LangGraph, Temporal, DBOS, Restate | 2019–2026 | N2 | un grafo con estado y auditoría |
| ejecución durable | Temporal y otros | producción 2026 | N2 | cada paso deja historia de eventos |
| capacidad ≠ funcionamiento | Sen, Nussbaum | 1979 | N2 | lo logrado frente al poder de lograrlo |
| contacto reduce prejuicio, con condiciones | Allport; Pettigrew & Tropp | 1954; 2006 | N2 | cuatro condiciones, un paquete |
| autonomía, competencia y vínculo | Deci, Ryan | 1985 | N2 | forzar produce obediencia, no aprendizaje |
| obligar la atención antes de aceptar | Buçinca et al. | 2021 | N1 | *cognitive forcing functions*: explicar no ayuda |
| suposiciones sí, contrafactual no | Ghosh, Sarkar, Lindley, Poelitz | 2026 | N1 | n=214; se prefiere el que no funciona |
| dificultad deseable | Bjork | 1994 | N2 | empeora el desempeño inmediato, mejora la retención |
| afecto como consecuencias del entorno | Cañamero; Man & Damasio | 2019 | N2 | iCub desarrolla ansiedad por batería baja |
| riesgo decisivo frente a acumulativo | Kasirzadeh | 2025 | N2 | el acumulativo no tiene una decisión que revisar |
| ayuda no pedida daña la competencia percibida | Sierksma, Brummelman | 2025 | N1 | N=619, pre-registrado |

**Regla:** lo que aparece en esta tabla **no se defiende como propio**. Se cita.

## 3. Los problemas abiertos del campo

Diez problemas, según el seguimiento de abril de 2026. **Ninguno resuelto.**

| # | Problema | Estado | ¿Lo toca este trabajo? |
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

## 4. El resultado que valida la pieza central

*«Evaluating large language models for accuracy incentivizes hallucinations»*, **Nature**, abril 2026.

> *«under standard scoring, **guessing is a dominant strategy**. A model that guesses outscores a trustworthy model that abstains when uncertain.»*

El caso concreto del paper: **o4-mini supera a GPT-5-mini en exactitud con más de 3/4 de error**, solo porque el segundo **se abstiene.**

**La industria premia adivinar sobre decir «no sé».**

Y la solución que propone no es un modelo mejor: es una rúbrica abierta — declarar el sistema de puntuación junto con la pregunta. Con eso, una mitigación que **antes bajaba la nota** ahora la sube en los cuatro modelos frontera probados.

**Lo que eso significa aquí:** el protocolo de admisión ya tiene **abstención con fecha de corte**, y `N5` existe como nivel legítimo. **Ya paga por abstenerse.**

> **Se llegó por criterio. La ciencia llegó al mismo sitio por medición.** No es coincidencia: la abstención declarada es la única forma de que un sistema no adivine, y el campo acaba de publicarlo.

**Lo que falta para que sea las dos cosas:** declarar **el costo del error**, no solo el hueco. Hoy se dice «no sé»; no se dice «y equivocarme aquí cuesta tanto».

## 5. Problema por problema

| Problema abierto | La pieza que lo toca | Qué tiene hoy | Qué le falta |
|---|---|---|---|
| **alucinación por incentivo** | abstención con fecha · niveles de fuente | abstención declarada con fecha | **el costo del error declarado** |
| **sycophancy** | sesgo declarado · la perspectiva que puede contradecir | una mirada que no confirma | un ejecutor que **no** busque agradar, probado |
| **sobreconfianza** | lo que retiene el otro · el techo · peor caso | el techo mide lo que sobrevive | **reportar el peor caso, no la media** |
| **sobre-dependencia** | fricción · *cognitive forcing* | la decisión pasa por el que la toma | **probar sobre un agente, no sobre un humano** |
| **agentes multi-paso** | fricción sin rama de imposición · integridad | la decisión no se puede saltar | **que el instrumento corra en dos ejecutores** |
| **evaluación de agentes** | talento utilizable · el instrumento | consistencia entre ejecutores | **que se corra** |
| **alineación de valores** | el mundo · la fricción · ayuda no pedida | el sistema no puede actuar sin contestar | que conteste **bien**, y eso no está garantizado |
| **razonamiento fiable** | compuertas de manipulación de procesos | el paso N+1 exige la salida del N | que el paso N sea **verificado**, no solo declarado |

La columna de la derecha es el diseño que corresponde a cada problema. **No es una lista de pendientes: es la pieza que falta para esa fila.**

## 6. Lo que no se resuelve, y hay que decirlo

**La alucinación como fenómeno.** El resultado de *Nature* demuestra que la presión viene de la predicción del siguiente token, y eso es estructural: no lo arregla ningún proceso. Lo que sí se arregla es **el incentivo**, que es la mitad que se puede tocar.

**La alineación de valores.** El sistema puede garantizar que **no actúe sin contestar**. No puede garantizar que conteste bien. **La fricción garantiza la pregunta, no la respuesta.**

**El ejecutor.** Si el proceso decide todo, un modelo barato empata **por la razón equivocada**. Lo que se mide es consistencia entre ejecutores, no identidad.

## 7. Prueba

¿Cada problema del campo tiene su pieza, o se declara que no la tiene? ¿Cada «falta» es concreta? ¿Lo que no se resuelve está dicho?

**Falsificador:** un problema presentado como resuelto sin corrida; una pieza asignada a un problema que no toca; una capacidad reclamada sin decir qué le falta; un problema del campo que se omite para que el mapa se vea completo.
