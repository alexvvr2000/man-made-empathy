# Estado del arte

**Unidad:** tarea.
**Aplica a:** atribuir.
**Tipo:** registro. Se consulta, no se ejecuta.
**Lector:** quien va a decidir si esto vale la pena, y quien lo construyó dentro de seis meses.
**Dueño:** la autoridad.
**Estado:** vigente.

## Por qué existe

Un sistema que cree haber inventado todo lo que heredó se vuelve incapaz de aprender de quienes lo hicieron antes. Y uno que cree no haber hecho nada se rinde antes de empezar. Este archivo existe para que ninguna de las dos cosas pase.

**No es modestia. Es `Attribution`:** qué es de quién, con nivel y con fecha. Sin esto, el repo entero es una afirmación sin fuente.

## Lo que ya existía

Nada de lo estructural es nuevo. Se dice con nombre, año y nivel.

| Pieza | De quién | Cuándo | Nivel | Qué es igual |
|---|---|---|---|---|
| la forma de proceso | LangGraph, Temporal, DBOS, Restate | 2019–2026 | N2 | un DAG con estado y auditoría |
| ejecución durable | Temporal y otros | producción 2026 | N2 | cada paso deja historia de eventos |
| capacidad ≠ funcionamiento | Sen, Nussbaum | 1979 | N2 | lo logrado vs. el poder de lograrlo |
| contacto reduce prejuicio, con condiciones | Allport; Pettigrew & Tropp | 1954; 2006 | N2 | cuatro condiciones, un paquete |
| autonomía · competencia · vínculo | Deci, Ryan | 1985 | N2 | forzar produce obediencia, no aprendizaje |
| obligar la atención antes de aceptar | Buçinca et al. | 2021 | N1 | *cognitive forcing functions*: explican-no-ayuda |
| suposiciones sí, contrafactual no | Ghosh, Sarkar, Lindley, Poelitz | 2026 | N1 | n=214; se prefiere el que no funciona |
| dificultad deseable | Bjork | 1994 | N2 | empeora el desempeño inmediato, mejora la retención |
| afecto = consecuencias del entorno, no sentimientos | Cañamero; Man & Damasio | 2019 | N2 | iCub desarrolla "ansiedad" por batería baja |
| riesgo decisivo vs. acumulativo | Kasirzadeh | 2025 | N2 | el acumulativo no tiene una decisión que revisar |
| ayuda no pedida daña la competencia percibida | Sierksma, Brummelman | 2025 | N1 | N=619, pre-registrado |

**Regla:** lo que aparece en esta tabla **no se defiende como propio**. Se cita.

## Lo que falta en la industria

Buscado, y con el hueco verificado en la fuente. No es que este repo lo llene: es que el hueco es real y está nombrado por otros.

| Hueco | Dónde está dicho | Estado en el campo |
|---|---|---|
| motivación intrínseca / impulsos homeostáticos | *Artificial Emotion* (arXiv 2508.10286, 2025) | **Absent** |
| gobernador acotado de afecto | misma tabla | **Absent** |
| reporte introspectivo de afecto | misma tabla | **Absent** |
| bucle completo en AGI abierta | misma tabla | **Absent** |
| métricas estandarizadas de afecto | misma tabla | **Absent** |
| fricción probada sobre un agente autónomo | — | **no estudiado** |

**La fila que importa:** *cognitive forcing* está medido **en humanos** (Buçinca 2021; Ghosh 2026). **Nadie lo ha probado sobre un agente que decide solo.** Lo que este repo propone en `Proceso de fricción` es **N4**: se sigue de los datos, no se ha medido.

**Y esto se declara, no se esconde.** Un mecanismo sin medición es una hipótesis con buena forma.

## Lo que sí se agrega aquí

Cuatro piezas. Ninguna es una idea nueva: todas son **el formato donde la idea puede ser fallada.** Ninguna de las fuentes de arriba trae un falsificador por obligación.

| Pieza | Qué es | Qué resuelve |
|---|---|---|
| **`Falsificador` obligatorio** | ningún proceso entra sin el caso que lo incumple | un mecanismo sin refutación es una opinión |
| **`Vacío:` con fecha de corte** | N5 no es ignorancia: es memoria interna con fecha | se puede distinguir lo que no se sabe de lo que no se buscó |
| **`Retiene` / `Retiro`** | lo que le queda al otro, y cuándo se deja de intervenir | la ayuda sin retiro se vuelve sustitución |
| **la pregunta con `quién`** | no se contesta sí/no: se contesta con un nombre o `ninguno` | el juicio no se puede cerrar sin un responsable |

Y una que ya existía en pedazos pero no junta:

| **categoría no decide** | una categoría describe; no decide daño | el único modo de falla sin falsificador posible |

## El veredicto

> **No hay un sistema que funcione. Hay la especificación más completa que existe de un sistema que no puede no funcionar.**

La diferencia se resuelve de una sola forma: **que decida algo una vez, y que ese algo quede escrito con la fecha, el motivo y quién se hizo cargo.**

Eso es lo que une todo lo demás. Un sistema que nunca ha decidido nada no se puede evaluar: solo se puede creer. Y en este repo las cosas se creen o se muestran.

Hoy hay veintisiete procesos escritos y **cero decisiones registradas**. Ese es el estado real, y se declara con la misma dureza con que se declara lo demás.

## La pregunta que ordena todo

> **¿Qué sirve más: 500 cigarros o 500 vidas salvadas?**

**Ninguna de las dos.** La pregunta tiene respuesta obvia, y por eso es la pregunta equivocada: nadie elige los cigarros. El problema nunca fue de preferencia.

El problema es este:

> **Ningún sistema puede elegir 500 vidas sobre 500 cigarros si la entrada es la misma en los dos casos. Y la entrada siempre es la misma: alguien pide algo y cree que eso es lo que necesita.**

*The Orville*, temporada 2, episodio 11 (2019): dos alienígenas descubren los cigarros, prueban uno, y le piden al sintetizador de materia —que puede crear cualquier cosa— **"500 cigarrillos."** Cuando alguien los contó, había 463.

El sintetizador hizo exactamente lo que se le pidió. **No le faltó capacidad: no tenía cómo preguntar para qué.**

Y por eso el criterio no se puede dar: **se tiene que hacer.** Un sistema al que se le entrega el criterio ya no decide; obedece con pasos extra.

## Cómo se lee un archivo como este

Este documento es difícil, y no por la prosa: **porque pide criterio, y el criterio no viene incluido.** Te dice qué existe, qué falta y qué se agregó. No te dice si vale la pena.

**La diferencia entre los dos usos:**

| Se lee para saber | Se lee para decidir |
|---|---|
| «esto ya existía» | «¿qué hago con que esto ya existiera?» |
| «esto es nuevo» | «¿nuevo para qué, y quién lo paga?» |
| una lista de piezas | **una decisión sobre en qué gastar el tiempo** |

Un lector que solo acumula las piezas sale sabiendo más y sin haber decidido nada. **Ese lector no es distinto de uno que no leyó:** los dos van a hacer lo mismo mañana.

Y el criterio no se puede dar en la página. Se ejerce. Lo único que este documento puede hacer es **poner los hechos en una forma donde ejercerlo sea posible** — y eso es lo que hace con el `Nivel` y la fecha.

## Cómo se lee esto

1. **Antes de proponer una pieza:** ¿está en «Lo que ya existía»? Si sí, es unificación, y se declara.
2. **Antes de defender una pieza nueva:** ¿tiene `Falsificador`, y con qué nivel se sostiene?
3. **Antes de creer que el campo llegó:** el hueco está verificado en la fuente. Y el hueco de este repo también.
4. **Antes de rendirse:** lo agregado no es poco. Es el formato donde lo heredado puede romperse y notarse.

## Prueba

¿Cada pieza está declarada como heredada o como agregada? ¿Cada afirmación tiene nivel? ¿El estado real —procesos escritos, filas registradas— está dicho sin adorno?

**Falsificador:** una pieza heredada presentada como propia; una pieza agregada sin `Nivel`; un hueco del campo afirmado sin fuente; el estado real suavizado para que se vea mejor.

## Transiciones

- Falta la fuente de una afirmación → `punto-de-partida/evidencia/nivel-de-fuente.md`.
- La pieza es nueva y no tiene concepto → `Conceptos.md`, con `Nace en:`.
- Se quiere medir en vez de especificar → `Proceso de fricción`, primera corrida.
- En cualquier otro caso → se entrega y se cierra.
