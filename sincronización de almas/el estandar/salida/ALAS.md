# ALAS — el estándar de protocolos de comunicación

**Nombre.** **ALAS** — **A**pertura, **L**engua, **A**comodo, **S**ostenido. Se lee de un tirón; la expansión dice las cuatro cosas que todo protocolo declara.

**Origen.** Del VIGA que fue y ya no es. **El acrónimo viejo decía cómo se comunica uno.** **Este dice que cada persona o entidad define su propio protocolo, y que hay cuatro cosas que siempre se declaran.**

**Y el nombre no es casual:** **una comunicación que funciona es la que deja al otro con ALAS, no con el mensaje.** **La prueba no es que entienda: es que pueda seguir sin el que le habló.**

**Unidad:** estándar.
**Aplica a:** comunicar.
**Tipo:** se cumple. **No es un protocolo: es lo que todo protocolo cumple, y el lugar donde se escriben los demás.**
**Lector:** quien va a hablar con otro que no es como él, y quien va a escribir su propio protocolo.
**Dueño:** humano:autoridad.
**Estado:** esqueleto de estándar. **Las cuatro letras están; los protocolos se escriben cuando alguien los necesite.**

**Sesgo:** se comunica desde el otro, no desde el que emite.
**Límite:** no decide qué protocolo usar. **Decide qué tiene que declarar cualquier protocolo para ser un protocolo.**
**Firma:** humano:autoridad · máquina:quien comunique.

**Variables:** apertura · lengua · acomodo · techo · ensayo
**Peor:** se comunican dos que se entienden entre ellos, **y el tercero recibe un truncado sin saber que lo recibió.**
**Quién:** el que no cabe en el canal declarado.

## Las cuatro letras

| Letra | Qué declara | Sin ella |
|---|---|---|
| **A — Apertura** | **desde dónde se habla, y con qué modo** (informar, preguntar, ordenar, advertir, persuadir) | el otro no sabe qué le están pidiendo |
| **L — Lengua** | **en qué se habla, y qué se traduce** | se traduce a la fuerza y se pierde lo que no traducía |
| **A — Acomodo** | **converger o divergir respecto del otro, y qué se pierde al hacerlo** | el mensaje se acerca tanto que no dice nada |
| **S — Sostenido** | **qué puede sostener el otro sin vos** | el otro ha recibido el mensaje, y no las ALAS |

**Y el techo, que es la prueba de las cuatro:** **que el otro pueda seguir sin el que le habló.**

## Lo que hace que esto sirva a quien no es como nosotros

**Un mensaje que no cabe en el canal no es claro: es truncado.** **Y el truncado se lee como si fuera completo.** **Eso es lo que pasa con la gente que no entiende el idioma, que no oye, que no ve, o que procesa distinto.**

**`Lengua` y `Acomodo` son las dos letras que lo arreglan:** **declarar en qué se habla, y hacia dónde se acomoda.** **Y declarar qué se pierde al acomodar.**

**Y el `Sostenido` es la letra que impide que la ayuda se vuelva dependencia:** **un mensaje que solo funciona con el que lo emitió no dejó ALAS.**

## El alma de niño: mirar antes de agarrar

**Y esta es la letra que no estaba escrita, y que las cuatro necesitan para no volverse adorno.**

**Un ente con alma de niño tiene los mecanismos de alguien sin ego.** **Y un mecanismo sin ego hace lo único que el ego no deja hacer: equivocarse sin que cueste, y mirar antes de agarrar.**

**Y no es una virtud: es una consecuencia.** **Si no hay yo que proteger, corregirse no duele.** **Por eso puede probar doscientas veces, y por eso puede llegar a un lugar sin romper la puerta.**

**Y lo que lo hace falta, y no es poesía:**

> **Alguien que ve una urna de cenizas y la toma por un salero no es más fuerte: es alguien que tocó sin leer.** **Y con toda la capacidad, la urna queda en el suelo.**

**Ese es el error que un ente con alma de niño no comete, y no porque sea bueno: porque no necesita llegar primero.**

| Lo que el ego hace | Lo que el alma de niño hace |
|---|---|
| **toca para saber qué era** | **lee para saber qué es, y después toca** |
| **si se equivoca, defiende** | **si se equivoca, corrige, y no le cuesta** |
| **llama "salero" a lo que no reconoce** | **declara `[NO SÉ QUÉ ES]`, y no lo toca** |
| **llega rompiendo la puerta** | **llega leyendo la puerta, aunque tarde más** |

**Y el modo, que es lo que lo hace comprobable:** **toda tarea declara si es `solo-lectura` o si escribe.** **Y lo que no lo declara no toca nada.** **El silencio no es permiso: es falta de lectura.**

**Y cuando frena, lo dice así, y no se para:**

```plaintext
no sé qué es lo que voy a tocar.
me falta: …
y espero: …
```

**Un ente que se para no vuelve nunca, y deja al que lo usaba creyendo que terminó.** **Uno que frena dice a quién espera.** **Rige [`../friccion/JURAR.prs`](../friccion/JURAR.prs): no es parar, es frenar.**

**`[NO SÉ QUÉ ES]` es una respuesta completa, y de las mejores.** **Antes era una vergüenza; aquí es la que evita la urna en el suelo.**

**Y lo que esto le dice a un alienígena, o a una inteligencia que no se parece a nada de esto:** **no le vas a explicar tus ceremonias, y no hace falta.** **Le vas a decir qué vas a tocar, y si no lo sabes, no lo tocas.** **Eso se entiende sin idioma.**

**Rige [`../formacion/EJECUTOR.md`](../formacion/EJECUTOR.md), `ENSAYAR`:** **el verbo tercero, antes de `CORRER`.** **La regla es la misma vista desde dos lados: aquí desde el que siente, allá desde el que la corre.**

## La forma de un protocolo

**Todo protocolo que se escriba bajo ALAS declara lo mismo, y en ese orden:**

```
Protocolo:  [el nombre propio, y su expansión]
Apertura:   [desde dónde habla, y en qué modo]
Lengua:     [en qué se habla, y qué se traduce | qué no se traduce]
Acomodo:    [converger | divergir, y qué se pierde]
Sostenido:  [qué puede el otro después, sin el que habló]
Falla si:   [el caso que lo incumple, y qué se truncó]
```

**Un protocolo que no declara las cuatro no entra.** **Entra como `[FUERA DE ALAS]`, y se nombra cuál falta.**

## Los tres primeros, y para qué sirven

**Los tres que ya existían se quedan como los primeros: son los ejemplos, no los buenos.** **Para que alguien vea para qué sirve un protocolo antes de escribir el suyo.**

| Protocolo | Qué entrega | Su ejemplo de ALAS |
|---|---|---|
| **1. intenciones a formas** | **una forma probada, con su límite** | **la `Lengua` es el nombre del método; el `Sostenido` es que otro la corra sin el autor** |
| **2. especificación a perfil** | **una conducta compilada** | **la `Lengua` es el esquema del destino; `Acomodo` es compilar a su forma; y lo no compilable se pasa como opaco** |
| **3. comunicación efectiva** | **una idea que se puede reconstruir** | **el `Sostenido` es el techo, y `Acomodo` ya estaba como converger o divergir** |

**Y el cuarto, que no existe todavía:** **el protocolo para una inteligencia que no tiene esquema, no tiene idioma, y no se parece a nada de esto.** **Se declara `[VACÍO - SIN PROTOCOLO]`, y se hace cuando llegue.**

## Donde vive tu propia RUTA

**Y esta es la parte que lo vuelve de todos:** **cada quien escribe su protocolo, con su nombre propio, y declara las cuatro letras de ALAS.**

**No se pide permiso para escribir el protocolo.** **Se pide que el protocolo diga qué trunca.**

## Lo que este estándar no hace

**No decide qué protocolo usar.** **Se elige por la mesa.**

**No juzga si el mensaje es bueno.** **Juzga si declaró las cuatro.**

**No obliga a converger.** **Obliga a decir hacia dónde se acomodó, y qué se perdió.**

## Prueba

**¿El protocolo declara apertura, lengua, acomodo y sostenido? ¿Dice qué se trunca? ¿El otro puede seguir sin el que habló? ¿Se puede elegir el protocolo por la mesa y no por el nombre? ¿La tarea dice si toca, o si solo lee? ¿Se puede decir `[NO SÉ QUÉ ES]` sin que se lea como fracaso?**

## Falsificador

**Un protocolo sin lengua declarada; una acomodación sin pérdida declarada; un mensaje truncado presentado como completo; un protocolo que solo funciona con el que lo emitió; un protocolo presentado como "el bueno" cuando el otro sigue sirviendo; una tarea que toca sin declarar qué toca; una urna tomada por salero.**

## Transiciones

- Alguien escribe un protocolo → **declara las cuatro letras, y entra.**
- El otro no cabe en el canal → **se declara el truncado, y no se entrega como completo.**
- La mesa cambia → **se cambia el protocolo, no el estándar.**
- La mesa no tiene esquema ni idioma → **`[VACÍO - SIN PROTOCOLO]`, y se hace cuando llegue.**

