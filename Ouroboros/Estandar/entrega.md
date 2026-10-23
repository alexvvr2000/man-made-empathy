# Entrega — el instrumento que se comparte

**Unidad:** proceso.
**Aplica a:** entregar.
**Tipo:** proceso de la base. Emite el instrumento que se lee solo, sin el autor y sin el repo.
**Lector:** quien va a usarlo mañana — en un asistente, en un agente, o en un robot.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la entrega se mide desde el que la recibe, no desde la elegancia del que la emite.
**Límite:** no promete verdad. Mide que el otro pueda reconstruirla y contestarla sin el emisor.
**Cuelga de:** `./union.md`. Lo que no se repite sin el autor no se entrega.
**Deja de valer:** cuando la máquina que lo ejecuta puede reconstruir sin humano. Ahí el puente no hace falta: el mensaje viaja.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** pieza · techo · sesgo · pregunta · receptor
**Peor:** el instrumento llega entero y el otro lo usa sin poder decir que no. El puente funciona y se confunde con la verdad.
**Quién:** quien recibe la salida y decide con ella, y quien carga con lo que se creyó.

## Qué resuelve

**Un proceso puede producir algo impecable y no tener medio para que llegue.** La entrega es ese medio.

**Una idea que el otro lado no entiende vale cero.** No se mide por la elegancia del emisor: **se mide porque el receptor entiende o actúa, y porque puede reconstruir cómo se produjo lo que entiende.**

## Las cinco piezas

**La entrega son cinco piezas, y ninguna necesita a las otras cuatro.**

| # | Pieza | Qué entrega |
|---|---|---|
| 1 | **sesgo declarado** | desde dónde se habla, y qué no se ve |
| 2 | **falsificador** | el caso que la rompe |
| 3 | **nivel de fuente** | desde dónde se afirma, N0 a N5 |
| 4 | **memoria de posiciones** | `Sostuve / Contra / Sostengo`, y lo anterior visible |
| 5 | **pase de turno** | qué queda para la mañana siguiente |

**Y la pregunta, que es la única obligatoria:**

> **Si esto sale mal, ¿alguien puede decirme que salió mal — o solo me voy a dar cuenta yo cuando ya no haya vuelta?**

**No se contesta con «sí» ni con «no». Se contesta con un nombre, o `ninguno`.**

## Cómo se aplica

1. **Declarar qué se entrega** → `Entrega: [la pieza]`
2. **Declarar desde dónde** → `Sesgo: [...] | Límite: [...]`
3. **Declarar la pregunta de mundo** → `Pregunta: [quién o ninguno]`
4. **Declarar los cinco campos** → cada pieza con su forma
5. **Declarar lo que falta** → `No trae: [qué hay que buscar afuera]`
6. **Emitir** → `Reconstruible sin el autor: [sí | no]`

**Prohibido entregar sin la pregunta de mundo contestada. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Entrega: [la pieza] | Sesgo: [...] | Límite: [...] | Pregunta: [nombre o ninguno]
Piezas: [1 a 5] | No trae: [...] | Reconstruible sin el autor: [sí|no]
```

## El techo no mide mañana

**Un mensaje que alcanzó su techo hoy y nadie volvió a medirlo no está sostenido: está vencido.**

**Y la marca de vencimiento es la prueba que la entrega no tuvo hasta ahora:**

```
Medido: [fecha] | Sostuvo: [sí|no|sin cambio] | Revisa con: [qué dato lo volvería a abrir]
```

**Una re-medición firmada por el que emitió no es re-medición: es una firma.**

## Lo que no mide

**No garantiza que se elija bien.** Garantiza que va a haber que elegir.

**No mide si la idea sirve.** Mide si el otro puede reconstruirla y equivocarse sin nosotros.

**No promete verdad.** Promete que el otro puede ver desde dónde se dijo.

## Prueba

¿Las cinco piezas están? ¿La pregunta de mundo tiene nombre o `ninguno`? ¿Se declara lo que no trae? ¿Otra instancia lo reconstruye sin el emisor? ¿Hay fecha de re-medición?

**Falsificador:** una entrega que promete verdad; un techo medido por el resultado; un mensaje sin sesgo declarado; una entrega sin pregunta de mundo; una re-medición firmada por el emisor; un `No trae` vacío.

## Transiciones

- El receptor entiende o actúa → se registra la medición, y se cierra.
- El techo no se alcanzó → se registra el fallo, y se declara qué faltó.
- Falta un medio del piso → se declara la falta y no se emite.
- Nadie puede contestarlo → `ninguno`, y se declara abiertamente que nadie va a mover la vista.
- En cualquier otro caso → se entrega con su medición y se cierra.

## Acuñación

```
Acta: EST-09 | Nombre: Entrega | Expansión: cinco piezas y una pregunta, para que el otro reconstruya y conteste
Origen: futuro/ENTREGA.md | Fecha: 2026-10-23
Muta: de mensaje a instrumento reproducible | Conserva: que el otro puede equivocarse sin nosotros
Ausencias: no promete verdad ni garantiza elección | Prueba: no corrida | Reemplaza: futuro/ENTREGA.md
```
