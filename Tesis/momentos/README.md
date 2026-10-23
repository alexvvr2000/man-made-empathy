# Momentos

**Unidad:** nivel.
**Aplica a:** entender.
**Tipo:** puerta. No decide, no ejecuta: dice qué es un momento, cuál entra y cómo se lee.
**Lector:** quien no va a leer setenta procesos, y quiere saber qué pasó aquí.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** esto se escribe para quien pregunta antes de saber, no para quien ya sabe.
**Límite:** un momento no es una prueba. No sustituye a un proceso, ni a una corrida, ni a un resultado.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `<../Ouroboros/formato de proceso.md>`

## Qué es esto

**Un momento es una vez que se creyó algo, se dijo, y algo pasó que lo cambió.**

No es un diario. **No hay un solo momento aquí que no haya cambiado una decisión.**

**Y el criterio es uno, y es duro:**

> **Un momento entra si cambió una decisión. No si es interesante, no si es lindo, no si da vergüenza. Si cambió una decisión, tiene cabida. Si no, no.**

**Esto es el sesgo declarado en acción.** El sesgo, en el resto del repositorio, es una columna. Aquí es una persona equivocándose en voz alta. Rige `<../Ouroboros/1 Guantelete — primitivo/primitivos/sesgo.md>`.

## La diferencia, sin adornos

| | El artículo | El momento |
|---|---|---|
| Qué publica | el resultado | el proceso que llevó al resultado, incluidos los errores |
| Qué dice | *el método funciona* | *aquí está la vez que me equivoqué, en qué, y qué cambió después* |
| Qué le puede pasar al que lo firma | lo citan | **lo corrigen** |
| Qué pasa si se equivoca | lo defiende otro papel | **se ve, y se corrige aquí mismo** |

**No es una cuestión de inteligencia. Es de qué se puede publicar sin perder prestigio.**

Admitir un error no da carrera. **Y un sistema que no admite el error no puede aprender** — no porque lo diga este archivo, sino porque **el aprendizaje es la corrección de una posición anterior, y si la posición no se puede ver, no hay nada que corregir.**

**Y esto no es una opinión sobre nadie:** la fricción obliga a decidir antes de ver la respuesta, y **no hay fricción sin la posibilidad de equivocarse.** Entonces el que no admite el error no está siendo más riguroso: **está perdiendo la única fuente de criterio que existe.**

Rige `<../Ouroboros/2 S.A.R.A — mutación/aprendizaje/aprender.md>`, `La continuidad real`: *una corrección que solo la firma el que se corrigió no se distingue de una preferencia que se mantuvo.*

## La ley que comparte con referencias

**Un momento y una referencia son el mismo acto en dos tiempos.**

> **La referencia no enseña: provoca. El momento es la pregunta que provocó.**

Una obra, un caso, una frase oída al pasar **no educa.** Hace que alguien se haga una pregunta que no sabía que tenía. **Y sin el momento, la referencia no le hizo nada a nadie.**

**Ejemplo, y es del propio repo:** el cuento de piratas de *Watchmen* no explica nada. Y por eso importa — el que lo leyó y se hizo la pregunta correcta no fue un académico: fue alguien con su vida.

**Por eso una no puede ir sin la otra.** Una referencia sin Preguntó es un título. Un momento sin Provoca es una anécdota sin origen.

```
Provoca: [la obra, el caso, la frase, el momento] | Pregunta: [la que hizo nacer]
Preguntó: [quién, con nombre o «la autoridad»] | Cambió: [qué se hizo distinto]
```

## La forma de un momento

Cuatro campos. Ni uno más.

```
Lo que dije: [la frase, tal como salió]
Lo que pensaba: [qué querías decir con eso]
Qué pasó después: [la corrección, con quien la hizo]
Qué decisión cambió: [la decisión concreta, y qué se hizo distinto]
```

**Y dos más en la cabecera del archivo:** `Provoca` y `Preguntó`. Rige `La ley que comparte con referencias`.

**`Qué decisión cambió` es obligatorio y es el que decide si el momento entra.** Sin él, el momento es una anécdota, y una anécdota no cambia nada.

**No se escribe lo que uno aprendió.** Se escribe **qué se hizo distinto después.** Lo aprendido que no cambió un acto es un sentimiento, y un sentimiento no deja rastro que otro pueda leer. Rige `<../Ouroboros/2 S.A.R.A — mutación/aprendizaje/aprender.md>`, `Continuidad`.

## Cómo se lee

**Se lee como se lee un caso, no como se lee una regla:** primero el momento, después la pieza que faltaba, después tú.

**Si al terminar un momento no reconoces una vez que te pasó lo mismo, no lo entendiste todavía** — o no aplica a ti, y eso también es una respuesta.

## Las subcarpetas

**Esta carpeta es mutable: crece por subcarpeta, no por archivo suelto.** Rige `../../AGENTS.md`, `Las dos carpetas de la tesis son mutables`.

```
Se crea una subcarpeta cuando hay tres archivos que comparten algo claro.
Antes de tres, van a la raíz.
Lo que entra en una subcarpeta no vuelve a la raíz.
El nombre de la subcarpeta dice lo que comparten, no el tema.
La raíz solo admite: README, index y _PLANTILLA.
```

**Hoy, con tres momentos, corresponde partir.** **Las subcarpetas las nombra quien escribe, y se declaran en un renglón: qué comparten.**

## Qué no entra

**Una reflexión sin error.** Si no había una creencia que se rompió, no es un momento: es una idea, y va a `../` como tesis.

**Una anécdota sin consecuencia.** Si contarla no cambia cómo se lee algo, no entra.

**Una queja sobre cómo trabaja otro.** El momento es siempre **sobre el que lo firma.** Un momento que acusa a un tercero no puede ser falsificado por su autor, y por eso no sirve.

**Un momento firmado por quien ya sabía la respuesta.** Si el que escribe no creía lo que dice que creía, no hubo error: hubo teatro. Y el teatro no enseña nada porque no hubo nada que corregir.

## Prueba

¿Cada momento dice qué decisión cambió, y se puede señalar el cambio? ¿El error era del que firma? ¿La corrección trae quién la hizo? ¿Se lee sin conocer el repositorio?

**Falsificador:** un momento que no dice qué decisión cambió; un momento que acusa a un tercero; un momento que da vergüenza ajena pero no cambió nada; un momento escrito por alguien que ya sabía la respuesta; una anécdota presentada como evidencia.

## Transiciones

- Un momento cambia una decisión de forma → se agrega una fila a `../../.sesion-continua/mantis.db` con su pieza.
- Un momento se convierte en regla → se escribe el proceso, y el momento queda como su caso de origen.
- Un momento demuestra que el sistema no sirve → se anota como descarte, con su porqué, y no se poda.
- En cualquier otro caso → se entrega y se cierra.
