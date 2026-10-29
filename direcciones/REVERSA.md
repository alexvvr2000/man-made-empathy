# REVERSA — el ciclo combinado: cada día que se revisa solidifica el proyecto y el legajo

**Hecho:** 2026-10-29. **Clase:** dirección, y es el ciclo de trabajo. **Estado:** vigente.
**Lector:** quien vaya a escarbar el historial, y quien tenga que defender el proyecto después.
**Dueño:** **quien tiene la autoridad en el proyecto donde se aplica.**

**Sesgo:** se lee desde el commit 1, que es la meta, y no desde el último commit, que es donde estamos.
**Límite:** **no dice qué se va a rescatar.** **Dice cómo se rescata, y qué tiene que quedar en cada paso.**
**Firma:** **quien responde por el acto, con su nombre** · **y quien lo ejecuta.**

**Peor:** se escarba el historial durante meses, **y al llegar al commit 1 el proyecto tiene la misma historia de siempre y ni un documento más para defenderse.** **Eso no es rescatar: es caminar.**

---

## La idea, y es de la autoridad

> **Entre más vayamos para atrás, el proyecto no sólo queda más sólido: queda más sólido legalmente.**

**Y eso no pasa solo.** **Pasa si cada paso hace dos cosas a la vez:**

| Cada paso atrás | Qué produce |
|---|---|
| **en el árbol** | **un repo más exacto: números que cuadran, rutas que existen, un solo árbol** |
| **en el legajo** | **un registro más grueso: qué se leyó, qué se tomó, y qué se dejó** |

**Y si un paso sólo hace una de las dos, no cuenta.** **Un paso que rescata y no documenta es trabajo perdido.** **Un paso que documenta y no rescata es burocracia.**

---

## El corte: por fecha, y no por nombre

> **No hay eras con nombre. Hay días.**
> **El git ya tiene un día por cada día, y no hay que inventar uno.**

**Y son 28 días con commits, del `2026-10-01` al `2026-10-29`, y 594 commits.**

| El día | Commits | Y qué se espera |
|---|---|---|
| **`2026-10-01`** | **1** | **el primer commit: el corte que es la meta** |
| **`2026-10-02`** | **18** | **—** |
| **`2026-10-03`** | **6** | **—** |
| **`2026-10-04`** | **8** | **—** |
| **`2026-10-05`** | **7** | **—** |
| **`2026-10-06`** | **24** | **—** |
| **`2026-10-07`** | **17** | **—** |
| **`2026-10-08`** | **10** | **—** |
| **`2026-10-09`** | **8** | **—** |
| **`2026-10-10`** | **3** | **—** |
| **`2026-10-11`** | **9** | **—** |
| **`2026-10-12`** | **19** | **—** |
| **`2026-10-13`** | **8** | **—** |
| **`2026-10-15`** | **6** | **—** |
| **`2026-10-16`** | **2** | **—** |
| **`2026-10-17`** | **8** | **—** |
| **`2026-10-18`** | **90** | **el día más caro: dos tercios del trabajo de una semana en una tarde** |
| **`2026-10-19`** | **80** | **el segundo más caro, y el que más se dijo después** |
| **`2026-10-20`** | **19** | **—** |
| **`2026-10-21`** | **15** | **—** |
| **`2026-10-22`** | **19** | **—** |
| **`2026-10-23`** | **18** | **—** |
| **`2026-10-24`** | **24** | **el primer día del chat grande** |
| **`2026-10-25`** | **18** | **—** |
| **`2026-10-26`** | **45** | **el día que nació la tesis** |
| **`2026-10-27`** | **41** | **—** |
| **`2026-10-28`** | **31** | **—** |
| **`2026-10-29`** | **40** | **hoy: la biblioteca publicada, y la voz** |

**Y el orden es de atrás hacia adelante:** **se empieza por hoy, y se termina en el `2026-10-01`.** **Porque lo viejo está sin filtro, y lo nuevo ya se pensó hoy.**

---

## El ciclo, y son ocho pasos por día

```plaintext
1. ABRIR EL DÍA    el corte por fecha, y se anota en el registro
2. LEER LOS COMMITS todos los del día, con su hash, y qué cambió
3. CLASIFICAR      se sostiene · se cayó · no se puede juzgar
4. SOLIDIFICAR     lo que se sostiene entra al árbol de hoy
5. ASEGURAR        el inventario se actualiza, y cuadra
6. DECLARAR        lo que se cayó, con su porqué; y lo que no se puede juzgar, con qué falta
7. COMMIT DEL DÍA  uno por día, con el rango de hashes
8. CERRAR EL DÍA   el registro del día, y el pase
```

**Y la regla que lo vuelve medible:**

> **No se avanza de día hasta que el inventario cuadre, y las rutas den cero.**

**Porque un paso atrás que deja un número roto no solidificó: oxidó.**

---

## Lo que cada día deja escrito, y no se puede saltar

**Y es un archivo por día, en `registro/`, y no un resumen en la memoria:**

```plaintext
Día:            [la fecha, y su rango de commits]
Commits:        [cuántos, del hash A al hash B]
Se sostiene:    [qué entró al árbol de hoy, con su hash de origen]
Se cayó:        [qué no, y por qué]
No se juzga:    [qué falta para poder juzgarlo]
Mensajes:       [los T# del chat de ese día, si los hay]
Inventario:     [los números, antes y después del paso]
Rutas:          [cero rotas, o cuántas quedan y por qué]
Legajo:         [qué documento creció, y cómo]
```

**Y ese archivo es la prueba de que el paso se dio.** **Sin él, el día no se cerró.**

---

## Y la tela que `EDIPO` saca de aquí

**Los cortes por fecha no son 28 sobres vacíos: son la puerta.**

| Lo que hay dentro de cada día | Cuánto |
|---|---|
| **commits, con su mensaje** | **594 en total** |
| **mensajes del autor en el chat, con su `T#`** | **926 en total, del 24 al 27** |
| **piezas que aparecieron: fichas, direcciones, ideas** | **lo que se escribió ese día** |

**Y lo que `EDIPO` tiene que traer a la biblioteca, día por día:** **las tesis y las ideas que aparecieron, y a dónde fueron, o por qué no entraron.**

**Eso es lo que convierte la reversa en trabajo de biblioteca, y no en una caminata por el historial.**

---

## Y por qué esto es lo que defiende en un juzgado

**Porque el git ya guarda la historia, y el abogado no necesita el pasado.**

**Necesita tres cosas, y este ciclo las produce:**

| Lo que el abogado necesita | Cómo lo produce este ciclo |
|---|---|
| **saber qué hay, y que se pueda contar** | **el inventario se actualiza cada día, y cuadra** |
| **saber cómo cambió, y cuándo** | **el registro por día, con hashes** |
| **saber que lo que se quitó se quitó a propósito** | **el campo `Se cayó`, con su porqué** |

**Y el cuarto, que no se produce escribiendo:** **que lo que se declara sea verdad.** **Eso se prueba abriendo el proyecto, y el ciclo no lo puede sustituir.**

---

## Lo que este ciclo NO hace

**No decide si algo es legal.** **Lo deja documentado para que un abogado lo decida.**

**No borra la historia.** **Si algo se quitó, se dice dónde estaba y por qué se quitó.** **El hash del commit original se guarda.**

**No promete que todo se pueda rescatar.** **Algunos días no se van a poder juzgar, y se declara así en vez de inventarles una lectura.**

**Y no sustituye al abogado.** **Le da el expediente ordenado, y lo llama a tiempo.**

**Rige [`./LO LEGAL.md`](./LO%20LEGAL.md), que tiene el ciclo de antes del commit 1, y [`./DEMANDAS.md`](./DEMANDAS.md), que tiene la regla de arriba.**

---

## Prueba

**¿Cada día tiene su registro? ¿El inventario cuadra después de cada paso? ¿Las rutas dan cero? ¿Lo que se cayó tiene su porqué? ¿El commit del día lleva su rango de hashes? ¿Se avanza sólo cuando todo lo anterior se cumplió?**

**Falsificador:** un día sin registro; un paso que rescató y no documentó; un inventario que no cuadra y se siguió; un día saltado; un commit de día sin rango de hashes; un paso atrás que oxidó y se declaró sólido.
