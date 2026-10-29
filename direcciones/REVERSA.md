# REVERSA — el ciclo combinado: cada paso atrás solidifica el repo y el legajo

**Hecho:** 2026-10-29. **Clase:** dirección, y es el ciclo de trabajo. **Estado:** vigente.
**Lector:** quien vaya a escarbar el historial, y quien tenga que defender el repositorio después.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el commit 1, que es la meta, y no desde el último commit, que es donde estamos.
**Límite:** **no dice qué se va a rescatar.** **Dice cómo se rescata, y qué tiene que quedar en cada paso.**
**Firma:** humano:autoridad · máquina:quien lo corra.

**Peor:** se escarba el historial durante meses, **y al llegar al commit 1 el repo tiene la misma historia de siempre y ni un documento más para defenderse.** **Eso no es rescatar: es caminar.**

---

## La idea, y es de la autoridad

> **Entre más vayamos para atrás, el repo no sólo queda más sólido: queda más sólido legalmente.**

**Y eso no pasa solo.** **Pasa si cada paso hace dos cosas a la vez:**

| Cada paso atrás | Qué produce |
|---|---|
| **en el árbol** | **un repo más exacto: números que cuadran, rutas que existen, un solo árbol** |
| **en el legajo** | **un registro más grueso: qué se leyó, qué se tomó, y qué se dejó** |

**Y si un paso sólo hace una de las dos, no cuenta.** **Un paso que rescata y no documenta es trabajo perdido.** **Un paso que documenta y no rescata es burocracia.**

---

## El ciclo, y son ocho pasos por era

```plaintext
1. ABRIR ERA      una rama por era, y se anota en el registro
2. LEER EL GIT    commit por commit, con su hash, y qué cambió
3. CLASIFICAR     se sostiene · se cayó · no se puede juzgar
4. SOLIDIFICAR    lo que se sostiene entra al árbol de hoy
5. ASEGURAR       el inventario se actualiza, y cuadra
6. DECLARAR       lo que se cayó, con su porqué; y lo que no se puede juzgar, con qué falta
7. COMMIT         uno por era, con el hash de origen y qué se tomó de él
8. CERRAR         el registro de la era, y el pase del día
```

**Y la regla que lo vuelve medible:**

> **No se avanza de era hasta que el inventario cuadre, y las rutas den cero.**

**Porque un paso atrás que deja un número roto no solidificó: oxidó.**

---

## Lo que cada era deja escrito, y no se puede saltar

**Y es un archivo por era, en `registro/`, y no un resumen en la memoria:**

```plaintext
Era:            [el nombre, y su rango de commits]
Commits:        [cuántos, del hash A al hash B]
Se sostiene:    [qué entró al árbol de hoy, con su hash de origen]
Se cayó:        [qué no, y por qué]
No se juzga:    [qué falta para poder juzgarlo]
Inventario:     [los números, antes y después del paso]
Rutas:          [cero rotas, o cuántas quedan y por qué]
Legajo:         [qué documento creció, y cómo]
```

**Y ese archivo es la prueba de que el paso se dio.** **Sin él, la era no se cerró.**

---

## Y por qué esto es lo que defiende en un juzgado

**Porque el git ya guarda la historia, y el abogado no necesita el pasado.**

**Necesita tres cosas, y este ciclo las produce:**

| Lo que el abogado necesita | Cómo lo produce este ciclo |
|---|---|
| **saber qué hay, y que se pueda contar** | **el inventario se actualiza en cada era, y cuadra** |
| **saber cómo cambió, y cuándo** | **el registro de eras, con hashes** |
| **saber que lo que se quitó se quitó a propósito** | **el campo `Se cayó`, con su porqué** |

**Y el cuarto, que no se produce escribiendo:** **que lo que se declara sea verdad.** **Eso se prueba abriendo el repo, y el ciclo no lo puede sustituir.**

---

## Lo que este ciclo NO hace

**No decide si algo es legal.** **Lo deja documentado para que un abogado lo decida.**

**No borra la historia.** **Si algo se quitó, se dice dónde estaba y por qué se quitó.** **El hash del commit original se guarda.**

**No promete que todo se pueda rescatar.** **Algunas eras no se van a poder juzgar, y se declara así en vez de inventarles una lectura.**

**Y no sustituye al abogado.** **Le da el expediente ordenado, y lo llama a tiempo.**

---

## El orden de las eras, y por dónde se empieza

```plaintext
hoy  →  las eras nombradas  →  los commits sueltos  →  el commit 1
       faro · mantis · v182838 · antes-del-corte · ciclo-0
```

**Y de atrás hacia adelante, y no al revés:** **lo viejo está sin filtro.** **Lo nuevo ya se pensó hoy, y empezar por ahí es repetir lo que ya se sabe.**

**Rige [`./LO LEGAL.md`](./LO%20LEGAL.md), que tiene el ciclo de antes del commit 1, y [`./DEMANDAS.md`](./DEMANDAS.md), que tiene la regla de arriba.**

---

## Prueba

**¿Cada era tiene su registro? ¿El inventario cuadra después de cada paso? ¿Las rutas dan cero? ¿Lo que se cayó tiene su porqué? ¿El commit de la era lleva el hash de origen? ¿Se avanza sólo cuando todo lo anterior se cumplió?**

**Falsificador:** una era sin registro; un paso que rescató y no documentó; un inventario que no cuadra y se siguió; una era saltada; un commit de era sin hash de origen; un paso atrás que oxidó y se declaró sólido.
