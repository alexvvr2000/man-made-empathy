# La fila verbalizada — cómo una salida se verbaliza sin romper al siguiente

**Qué fija.** **Que una salida de un proceso se pueda consumir sin que el que la lee adivine.** **Y que si no se puede, el proceso no entrega: declara.**

**Sesgo.** se sostiene desde `verbalizar.md`: **una salida no es lo que el proceso dice que hizo: es lo que otro puede sostener, contestar y reconstruir.**
**Límite.** no juzga si la salida es buena. **Juzga si el siguiente puede consumirla sin preguntar.**
**Firma.** humano:autoridad · máquina:quien la produzca.
**Estado.** vigente.

**Y su ejecutor es un proceso:** **`procesos/EXPRESION.prs` escribe la fila, y ningún `.prs` entrega sin pasar por él.**

## Por qué existe

**Hoy cada `.prs` dice qué sale, pero no**cómo** sale.** **Y ahí es donde se rompe:** **el siguiente lo lee, adivina, y la cadena se corta sin que nadie lo note.**

**Y es exactamente lo que pasa cuando se filosofa a lo pendejo con la IA:** **la respuesta suena, no dice qué se sostuvo, y el que sigue no tiene de dónde agarrarla.** **La fila verbalizada es el corte que impide eso.**

## La fila

**Toda salida de un proceso se escribe así, y nada más:**

```
Sostengo: [lo que se afirma, en una línea]
Contra:   [qué la contradijo, o «ninguno», o «no se probó»]
Rastro:   [dónde quedó, y quién lo puede leer]
Siguiente: [qué proceso la consume, y qué campo usa]
Borde:    [qué no se afirma todavía]
```

- **`Sostengo`:** la posición, no el relato. **Si no se puede citar, no es salida.**
- **`Contra`:** lo que la movió. **`ninguno` es legítimo y se lee como «no se probó», no como «es cierta».**
- **`Rastro`:** la huella. **Sin esto, la salida vive solo en el acto, y el siguiente no tiene qué leer.**
- **`Siguiente`:** **el nombre del proceso y el campo exacto que usa.** **Es lo que vuelve la cadena una función y no una conversación.**
- **`Borde`:** lo que no se afirma. **Sin esto, el siguiente cree que la salida cubre más de lo que cubre.**

## Cómo se hace una función sin volverla programa

**Y esto es lo que pedías: una salida que se puede componer.**

```
ENTRAR:  [Sostengo | Contra | Rastro | Siguiente | Borde]  →  el .tra de la tarea
MIRAR:   [Sostengo | Contra | Rastro | Siguiente | Borde]  →  el nombre vigente
EXTRAER: [Sostengo | Contra | Rastro | Siguiente | Borde]  →  la capacidad con su costo
```

**Y la cadena se lee de arriba abajo:**

```
salida de ENTRAR  ──(Siguiente: MIRAR, campo Rastro)──→  MIRAR lo consume
salida de MIRAR   ──(Siguiente: EXTRAER, campo Sostengo)──→  EXTRAER lo consume
```

**Es una función porque:** **una sola salida, un solo consumidor, un campo nombrado.** **Y no es un programa porque:** **la ejecuta un lector, no un motor.**

## La regla de la no-ruptura

> **Si la salida no cabe en la fila, el proceso no entrega: declara `[VACÍO - SIN SALIDA]`.**

**Y el que la consume no la completa.** **La completa quien la produce o no hay cadena.** **Un siguiente que rellena es un siguiente que inventó.**

**Y la prueba, que es la única:**

> **Otro proceso consume la salida sin preguntarle nada al que la produjo.**

**Si tiene que preguntar, la salida no estaba verbalizada.**

## Las cuatro cosas que rompen una salida, y su corte

| Se rompe así | Cómo se ve | Su corte |
|---|---|---|
| **la salida es una narrativa** | "el proceso hizo X y luego Y" | **se reescribe en `Sostengo`** |
| **la salida no dice qué consume** | el siguiente adivina el campo | **`Siguiente` con nombre y campo** |
| **la salida no dice lo que no afirma** | el siguiente cree que cubre todo | **`Borde`** |
| **la salida se completa al consumirla** | el segundo inventa lo que falta | **`[VACÍO - SIN SALIDA]`** |

## Lo que esta forma no hace

**No vuelve automático al proceso.** **Un lector lo ejecuta; un motor no.**

**No reemplaza al `.tra`.** **El `.tra` es la tarea; esto es la salida con la que la cadena sigue.**

**No impide equivocarse.** **Hace que el error tenga dónde verse por el que sigue.**

## Prueba

**¿La salida cabe en las cinco líneas? ¿`Siguiente` nombra el proceso y el campo? ¿`Borde` dice lo que no se afirma? ¿Otro proceso la consume sin preguntar? ¿Si no cabe, se declara `[VACÍO - SIN SALIDA]`?**

**Falsificador:** una salida que es un relato; `Siguiente` sin campo; `Borde` vacío; el consumidor rellenando lo que falta; un proceso que entrega una salida que el siguiente no puede leer.



