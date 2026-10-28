# CONTEXTO.md — de dónde vino, qué provocó, y que se usó bien

**Nombre.** CONTEXTO. **Y la expansión dice el acto:** **mostrar de dónde viene lo que se usa, qué provocó, y que la información se usó bien.**
**Y su otra mitad, que es la que lo separa de las fuentes:** **forzar lo justo, y mostrar lo demás.**

**Hecho:** 2026-10-28. **Clase:** aplicación. **Estado:** propuesto.
**Reemplaza:** `direcciones/CONTEXTO.md` (que se retiró), y absorbe lo que hacían `contexto/` y `ejemplos/`. **Los dos se retiran: no hay carpeta para lo que cabe en un archivo.**

**Lector:** quien va a citar algo ajeno, y quien va a leer el repo sin saber de dónde salió cada cosa.
**Dueño:** humano:autoridad.

**Sesgo:** se lee desde el que va a entender, no desde el que se defiende.
**Límite:** **no protege legalmente.** **Eso es `FUENTES.md` y `ATTRIBUTION.md`.** **Este muestra qué se usó, de dónde, y para qué.**
**Firma:** humano:autoridad · máquina:quien lo escriba.

---

## Por qué es un archivo, y no una carpeta

> **Un folder es molesto.** **Lo que cabía en un archivo no necesita un folder: necesita una forma.**

**Y por eso una sola pieza absorbe tres cosas que antes estaban separadas:**

| Lo que era | Ahora |
|---|---|
| **`contexto/`, una carpeta por obra** | **una entrada por obra, aquí** |
| **`ejemplos/`, lo que provoca** | **una entrada con su `Provoca:` y su `Límite:`, aquí** |
| **`direcciones/CONTEXTO.md`** | **este archivo, en la raíz: se lee junto a `FUENTES.md` y `ATTRIBUTION.md`, y no dentro de `direcciones/`** |

---

## Los tres archivos, y cada uno hace lo suyo

| Archivo | Para quién | Qué hace | Su prueba |
|---|---|---|---|
| **`FUENTES.md`** | **el que puede reclamar un nombre** | **registra la obra, con autoría y año** | **¿se verifica que existe, y que no se adjudicó?** |
| **`ATTRIBUTION.md`** | **el que revisa legalmente** | **qué es mío, qué es ajeno, qué se cede** | **¿se distingue lo propio de lo heredado?** |
| **`CONTEXTO.md`** | **el que va a entender** | **de dónde vino, qué provocó, y dónde se usó** | **¿el otro entiende por qué esto está aquí, y se ve que la info se usó bien?** |

**Y la regla que los separa, dicha por la autoridad:**

> **Una cosa es forzar, y otra es mostrar.**
> **Las fuentes existen para no meterse en un problema legal; el contexto, para que la gente entienda.**

**Y la meta de este repo es mostrar.** **Por eso el contexto no es un anexo: es lo que hace que el repo sea del que lo lee.**

---

## Lo que declara cada entrada, y son seis cosas

```plaintext
Obra:      [título, autor y año. Lo mínimo para encontrarla]
Soporte:   [libro | película | serie | cómic | artículo | página | conversación]
Provocó:   [la pregunta, en una línea]
Se usó:    [dónde, con su ruta, y para qué]
Se toma:   [la frase, el caso o la idea que se usa, y nada más]
Límite:    [lo que esa obra NO enseña, y por qué no se puede estirar]
```

**Y cada uno, con su por qué:**

| El campo | Sin él |
|---|---|
| **`Obra` + `Soporte`** | **no se puede encontrar, y sin encontrar no se verifica** |
| **`Provocó`** | **la obra se cita como autoridad, y no como lo que preguntó** |
| **`Se usó`** | **la idea queda sin saber a qué pieza sirvió** |
| **`Se toma`** | **se apropia la obra entera, cuando sólo se usó una línea** |
| **`Límite`** | **la obra se estira, y el que leyó la obra no reconoce la suya** |

---

## La regla de oro, y es la que evita el problema legal sin tocar la ley

> **Se cita la obra como lo que es: una obra que preguntó algo.**
> **Y lo que se toma se dice, y nada más. Lo que no se toma no se insinúa.**

**Y el daño que previene es doble, y el segundo es el que más duele:**

1. **Legal:** **no se presenta como propio lo que es ajeno.**
2. **De lectura:** **el que leyó la obra reconoce la suya, y no otra inventada por el que la citó.**

**Y por eso también protege del sesgo:** **la obra provoca la pregunta; no la prueba.**

---

## Cómo se ve una entrada

```plaintext
Obra:      Arrival (Ted Chiang, 1998; Denis Villeneuve, 2016)
Soporte:   cuento y película
Provocó:   ¿qué pasa si el otro ya tiene un canal, y el canal es otro?
Se usó:    direcciones/ALAS.md, «Lengua» — para la razón de declarar lo que se traduce
Se toma:   la idea de una lengua que se habita y no se traduce
Límite:    no enseña cómo se construye un canal que no existe
```

**Y eso es todo.** **Con seis líneas, el que lee sabe de dónde vino, para qué sirvió, y qué no se puede estirar.** **Y no tuvo que abrir una carpeta.**

---

## Lo que este archivo NO hace

**No protege legalmente.** **Eso es `FUENTES.md` y `ATTRIBUTION.md`.**

**No obliga a declarar todo.** **Declara lo que se tomó. Lo que no cambió una decisión, no se declara.**

**No juzga la obra.** **Dice qué provocó y dónde se usó. Si es buena o mala, no es asunto de este archivo.**

**No convierte una obra en fuente.** **Una fuente se cita; una obra que provocó, se agradece.**

---

## Su corte

**Entra:** una idea, un nombre o un caso que se usó y no nació aquí.

**Falla si:**
- **no se puede encontrar la obra con lo que se declara.**
- **se declara la obra entera cuando se usó una línea.**
- **se omite el `Límite`, y la obra se estira.**
- **se presenta como propio lo que provocó a otro.**

**Sale:** **la entrada con sus seis campos**, o **`[SIN CONTEXTO - NO SE SABE DE DÓNDE]`.**

**Consume:** **el que lee, y el que va a contestar la idea.**

---

## Prueba

**¿Cada entrada dice obra, soporte, qué provocó, dónde se usó, qué se toma y qué no enseña? ¿Se puede encontrar la obra con lo que dice? ¿Se distingue lo que se tomó de lo que sólo se menciona? ¿El que leyó la obra la reconoce?**

**Falsificador:** una obra citada como autoridad; una entrada sin `Límite`; una obra estirada más allá de su caso; una idea heredada presentada como propia; una entrada sin `Se usó`.

---

## Lo que queda abierto, y es de la autoridad

**1. ¿Las entradas se ordenan por obra, por uso, o por fecha?** **Mi recomendación: por uso, porque el que busca lo hace para saber qué sustentó una pieza.** **Y la columna `Se usó` es la que permite ordenar así.**

**2. ¿`futuros posibles.md` tiene su propia tabla de contexto, o cita ésta?** **Yo citaría ésta: una sola fuente de procedencia, y no dos.**

**3. ¿`FUENTES.md` adelgaza a agradecimientos y regla de nombres, y las obras quedan sólo aquí?** **Si sí, no hay duplicado; si no, hay dos listas que se van a desincronizar.**
