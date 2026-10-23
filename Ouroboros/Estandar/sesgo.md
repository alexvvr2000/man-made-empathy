# Sesgo — desde dónde se sostiene una pieza

**Unidad:** proceso.
**Aplica a:** sostener.
**Tipo:** primitivo de la base. Es el fundamento: toda pieza se sostiene desde algún sitio.
**Lector:** quien va a usar una pieza, y quien va a contestarla.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la pieza se lee desde la posición declarada, no desde la posición supuesta.
**Límite:** no corrige el sesgo; lo vuelve visible.
**Cuelga de:** `./friccion.md`. La fricción necesita saber a quién preguntar, y eso lo da el sesgo.
**Deja de valer:** cuando la pieza no se sostiene desde ningún sitio. Una pieza sin posición no es pieza: es preferencia con forma.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** posición · límite · firmante · indeterminación
**Peor:** la pieza se sostiene con una sola mirada, nadie puede contestarla, y se lee como si no tuviera sitio. Converge a sí misma y ya no requiere mirar.
**Quién:** quien usa la pieza, y quien carga con que su error no pueda ser visto.

## Qué resuelve

**No hay pieza neutra.** La que no declara desde dónde habla **oculta el único dato que la vuelve comparable.**

**Un sistema con una sola mirada converge a sí mismo, y converger a sí mismo es la definición de absoluto.** **Eso no lo arregla tener más poder: lo arregla saber desde dónde se está mirando y quién puede contestarlo.**

**El tiempo no cura el absoluto. Otra mirada sí.** **Una idea no envejece: cambia el que la mira.**

## La forma

```
Sesgo: [la posición desde la que se sostiene]
Límite: [No se aplica a qué: qué queda fuera]
Firma: [quién puede contestarla: tipo:nombre | comunidad | ninguno]
Indeterminado hasta: [qué la vuelve firmable]
```

**`Límite` es obligatorio.** Un criterio sin límite no es criterio: es una creencia con nombre de norma.

**`Firma` tiene que ser distinta de quien produjo la pieza.** Rige `./friccion.md`, `La fricción no es coerción`.

**`Indeterminado hasta`** dice qué falta para que el veredicto deje de ser `indeterminado`.

## Cómo se aplica

1. **Declarar la posición** → `Sesgo: [desde dónde]`
2. **Declarar el límite** → `Límite: [No se aplica a qué]`
3. **Declarar el firmante** → `Firma: [quién contesta]`
4. **Declarar qué falta** → `Indeterminado hasta: [qué la vuelve firmable]`
5. **Emitir** → `Veredicto: [pasa | falla | indeterminado]`

**Prohibido emitir un veredicto `pasa` sin firmante distinto del productor.**

```
Sesgo: [posición] | Límite: [No se aplica a qué] | Firma: [quién] | Indeterminado hasta: [qué] | Veredicto: [pasa|falla|indeterminado]
```

## Lo que un sesgo declarado permite

| Cree que… | Con sesgo declarado… |
|---|---|
| no cabe, entonces está mal | no cabe, y aquí está la regla que rompe |
| ya se vio todo | sabe exactamente qué no se vio |
| su mirada basta | sabe qué mirada pide |

> **El sesgo declarado no dice qué no sabes. Dice desde dónde no estás viendo** — y eso es lo necesario para saber a quién preguntar.

## Lo que no hace

**No corrige el sesgo.** Lo vuelve visible. Lo que se hace con eso lo decide quien lee.

**No convierte la pieza en neutral.** Una pieza neutral no existe: existe la que declara desde dónde mira.

**No firma por otro.** Un veredicto firmado por el productor no es veredicto: es una firma.

## Prueba

¿La pieza dice desde dónde mira? ¿Dice qué no ve? ¿El que la puede contestar no es el que la produjo? ¿El veredicto sin firmante se declaró `indeterminado`?

**Falsificador:** una pieza que se presenta como neutral; un veredicto firmado por quien produjo la pieza; una pieza sin `Límite`; un `indeterminado` presentado como `pasa`.

## Transiciones

- Falta el límite → se declara `No se aplica a: nada que esto exija`, y se corrige antes de usarla.
- No hay firmante distinto → el veredicto es `indeterminado`, no `pasa`.
- La mirada cambió → fila nueva; la vieja no se edita: se suplanta. Rige `./memoria.md`.
- En cualquier otro caso → se entrega con su sesgo declarado y se cierra.

## Acuñación

```
Acta: EST-03 | Nombre: Sesgo | Expansión: la posición desde la que una pieza se sostiene, y quién la contesta
Origen: ../Tesis/LA-TESIS.md, De qué está hecha | Fecha: 2026-10-23
Muta: de atributo a fundamento: ninguna pieza se sostiene sin él | Conserva: que se declara y no se corrige
Ausencias: no corrige el sesgo ni firma por otro | Prueba: no corrida | Reemplaza: NINGUNA
```
