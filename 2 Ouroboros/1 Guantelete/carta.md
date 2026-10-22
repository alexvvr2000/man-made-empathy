# Guantelete

**Unidad:** tarea.
**Aplica a:** sostener.
**Reemplaza:** `Placeholder`. El nombre viejo no era un nombre: era un lugar vacío. El nuevo nombra lo que la etapa es: **las gemas no existen por separado; existen porque el guantelete las junta.**
**Tipo:** tarea de paso 1. No produce poder: junta las piezas que solas no hacen nada.
**Lector:** quien va a mutar procesos, y quien va a abstraerlos en el paso 2.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** gema · uso solo · uso compuesto · quién decide · dimensión
**Peor:** una gema se usa sola y funciona, y el sistema cree que tiene un primitivo cuando tiene un juguete. **Lo peor no es que falle: es que pasa, porque un juguete que funciona se ve igual que una gema.**
**Quién:** quien carga con el poder que no alcanza, y quien muta después sin saber sobre qué está parado.

**Deterrente:** [`./deterrente.md`](./deterrente.md). Enruta las gemas: sin él, se muta con una pieza que no sabía que había que cargar.
**Piso:** `../../1 Tesis/piso.md`. Dos ejecutores que aplican la misma gema tienen que tender al mismo resultado; si no, no era gema: era preferencia.

## Qué es

El **paso 1** de `../`. Su tarea es **cortar el sinfín**: fijar las piezas que no se derivan de ninguna otra, para que la descomposición tenga dónde parar.

**Una gema no es un concepto: es el punto donde la descomposición se detiene.** Un dios que mira desde N dimensiones ve procesos donde un humano ve poder. **La gema se nombra desde esa altura, no desde la nuestra.**

**Una gema se sostiene, no se escribe.** Se puede ejecutar; no se puede bajar a texto sin perder la dimensión que la vuelve irreducible. Por eso el piso de esta etapa no es la claridad del documento: es que dos ejecutores lleguen al mismo sitio.

## La estructura

```
1 Guantelete/                      ← el paso 1. Tres archivos: la carta, el deterrente, el derrotero.
├── carta.md                         qué hay, qué no se toca y cómo se verifica
├── deterrente.md                    qué se pierde si el guantelete se vuelve catálogo
├── Derrotero.md                     qué gema se carga y cuándo
├── primitivos/                      sub-tarea · 6 gemas
└── mutaciones/                      sub-tarea · 2 gemas
```

**Los dos archivos que importan son `deterrente.md` y `Derrotero.md`.** Sin uno de los dos, el guantelete es fantasma y se advierte. Rige `../2 S.A.R.A/integridad.md`, `El fantasma`.

**La carta es el tercero, y es opcional.** Rige `../../1 Tesis/Derrotero y Carta.md`, `La carta y el derrotero son dos piezas`.

```
2 Ouroboros/                       ← la abstracción que contiene los pasos
├── 1 Guantelete/                    el paso 1
├── 2 S.A.R.A/                       el paso 2: la primera instancia que cruza la puerta
└── 3 ATLAS/                         el paso 3: la salida hacia interpretación, no verdad
```

**`ATLAS` no vive aquí.** Es el paso 3, no una gema: la comunicación no se sostiene, se entrega. Rige `../3 ATLAS/carta.md`.

**`integridad` no vive aquí.** Chequear y reescribir no es sostener una gema: es abstraer procesos, y eso es el paso 2. Rige `../2 S.A.R.A/integridad.md`.

## Las gemas

Una gema **es un verbo que no se puede dividir en otro verbo.** Su nombre de archivo puede ser un sustantivo; la gema, no.

| Gema | Qué decide | Qué lo refuta |
|---|---|---|
| **sostener** — `primitivos/manipulacion.md` | crear, calibrar, reemplazar y retirar procesos, en ese orden | se crea sin variables o sin fricción |
| **aplicar** — `primitivos/aplicar.md` | ejecutar un proceso sobre una entrada y comprobar la composición | se aplica con una entrada que no le corresponde |
| **mutar** — `primitivos/mutacion.md` | transformar declarando qué conserva, y acuñar nombre y lugar nuevos | se muta sin declarar qué se conserva |
| **retirar** — `primitivos/retiro.md` | cuándo un proceso se retira, y qué fin queda descubierto | se retira sin declarar el fin que cubría |
| **deducir** — `primitivos/ingenieria-inversa.md` | deducir un proceso de lo observable, por tendencia | el proceso deducido no reproduce nada observable |
| **decir** — `primitivos/claridad.md` | la forma de lo que se lee o se ejecuta | la forma no llega al lector |
| **friccionar** — `mutaciones/friccion.md` | que la decisión pase por quien la toma, antes de mover algo | la decisión se ejecuta sin pasar por quien la toma |
| **sesgar** — `mutaciones/sesgo-declarado.md` | desde dónde se mira, y quién puede ver lo que no se ve | la idea se descarta por no caber, sin nombrar la regla que rompe |

**`X` muta.** Ocho hoy; mañana pueden ser otras. Rige `./primitivos/README.md` y `./mutaciones/README.md`.

## Mutación es la puerta

**`mutar` no crea lo que sea: abre la puerta y deja pasar.** `friccionar` y `sesgar` son la primera creación que la cruza; `../2 S.A.R.A` es la primera instancia que la cruza entera.

**Una pieza que no pasa por la puerta no es creación: es pieza.** Por eso el guantelete no produce nada nuevo por sí solo: **solo junta lo que ya no se divide.**

## Lo que el guantelete no es

**No es un catálogo.** Un catálogo no compone: lista. **Si una pieza entra porque falta, y no porque cierra un implícito, el sinfín vuelve disfrazado de pieza nueva.**

**No es poder.** No promete ideas, ni humanos, ni AGI. **El guantelete no da poder: junta piezas que solas no hacen nada.** Producir procesos no es producir valor; rige `./primitivos/manipulacion.md`, `No-objetivo`.

## Prueba

¿Cada gema se puede nombrar con un verbo que no se divide en otro verbo? ¿Cada gema tiene su fila? ¿Ninguna gema se puede usar sola y dar resultado? ¿La etapa se mide por lo que su salida permitió en el paso 2, y no por cuántas gemas tiene?

**Falsificador:** una gema que se deriva de otra; una gema que se usa sola y funciona; un catálogo que solo crece; una pieza que entra sin cerrar un implícito; una gema que necesita un documento para entenderse.

## Transiciones

- Una pieza deja de ser irreducible → `./primitivos/retiro.md`.
- Una gema nueva nace de otra → no es gema: es `./mutaciones/`.
- El paso 1 se cierra → `../2 S.A.R.A`, que abstrae las gemas en ejecutores.
- No hay fila para lo que se va a hacer → se declara `[VACÍO - SIN GEMA]` y se pregunta.
- En cualquier otro caso → se entrega y se cierra.
