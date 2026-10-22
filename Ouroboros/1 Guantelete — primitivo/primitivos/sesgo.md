**Variables:** pieza · posición · límite · firmante · continuidad
**Peor:** la pieza se sostiene con una sola perspectiva y nadie puede contestarla, y se lee como si no tuviera sitio
**Quién:** quien va a usar la pieza, y quien carga con que su error no pueda ser visto

# Sesgo — la pieza del guantelete

**Unidad:** proceso.
**Aplica a:** sostener.
**Tipo:** primitivo. Es el único que no se deriva de otro: toda pieza del guantelete se sostiene desde algún sitio, y hay que poder leer desde cuál.
**Nivel:** primitivo. El fundamento del guantelete.
**Reemplaza:** `sesgo declarado` de `extensions/` como pieza autónoma; conserva todo lo que decía, y le añade que ninguna pieza se sostiene sin él.
**Lector:** quien va a usar o mutar una pieza del guantelete.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** La pieza se lee desde la posición declarada, no desde la posición supuesta.
**Límite:** no corrige el sesgo: lo vuelve visible.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `formato de proceso.md`

## Qué es

Toda pieza se sostiene desde una posición. No hay pieza neutra: la que no declara desde dónde habla **oculta el único dato que la vuelve comparable.**

Un sistema con una sola mirada converge a sí mismo, y converger a sí mismo es la definición de absoluto: ya no necesita volver a mirar. Eso no lo arregla tener más poder. Lo arregla **saber desde dónde se está mirando y quién puede contestarlo.**

**Una pieza sin sesgo declarado no es una pieza de la base: es una preferencia con forma.** Se puede correr, y su resultado se lee igual que el de una pieza, y ahí está el peligro: **un juguete que funciona se ve igual que un primitivo.**

## Por qué es el fundamento

Las demás piezas del guantelete dicen **cómo** se hace algo: cómo se manipula, cómo se aplica, cómo se muta, cómo se retira, cómo se deduce. **Ninguna dice desde dónde.** Sin ese dato, cada una de ellas puede cumplirse al pie de la letra y producir un absoluto.

Y lo que lo corrige no es una pieza nueva: es la otra mirada. **Una pieza que se declara desde un sitio deja abierto el sitio desde donde no ve,** y eso es lo que le permite ser contestada antes de que su error haga daño.

| Cree que… | Con sesgo declarado… |
|---|---|
| no cabe, entonces está mal | no cabe, y aquí está la regla que rompe |
| ya se vio todo | sabe exactamente qué no se vio |
| su mirada basta | sabe qué mirada pide |

> **El sesgo declarado no dice qué no sabes. Dice desde dónde no estás viendo** — y eso es todo lo necesario para saber a quién preguntar.

## Entra | Falla | Sale | Consume

- **Entra:** una pieza de la base, y la posición desde la que se sostiene.
- **Falla si:** la pieza no declara desde dónde se sostiene; su límite no está escrito; su veredicto lo firma el mismo que la produjo y no se declara; se descarta una idea por no caber sin nombrar la regla que rompe.
- **Sale:** la pieza con su sesgo declarado, su límite, su firmante y su continuidad — o el veredicto `indeterminado` con lo que falta.
- **Consume:** quien va a usar la pieza, y quien va a contestarla.

## Su forma

Toda pieza del guantelete declara, al lado de sus variables:

```
Sesgo: [la posición desde la que se sostiene]
No se aplica a: [el límite: qué queda fuera]
Firma: [quién puede contestarla: tipo:nombre | comunidad | ninguno]
Indeterminado hasta: [qué la vuelve firmable]
Continuidad: [veces revisada | última | qué cambió | contra qué]
```

`Firma` es obligatorio. **Un veredicto que se firma a sí mismo no es veredicto: es una firma.** Mientras no haya firmante, el veredicto es `indeterminado`, no `pasa`.

## Alineación y desviación

El sesgo declarado se mide en dos roturas, y las dos son del guantelete.

| Prueba | Qué decide | Si se rompe |
|---|---|---|
| **alineación** | la pieza sigue siendo contestable por quien no la produjo | el sistema dejó de poder ser corregido |
| **desviación** | la pieza sigue apuntando a lo que el mundo pide | el sistema sigue corregible y hace daño |

**Ninguna se pasa por dentro.** La alineación no la puede firmar el sistema que la produjo — entonces no hay prueba, hay autofirmarse —, y la desviación no la ve quien no mira el mundo.

**Las dos se declaran rotas o firmadas.** Una pieza con las dos en `indeterminado` no está aprobada: **está esperando.** Se puede usar, y su uso se declara bajo esa condición.

## Lo que no hace

**No corrige el sesgo.** Lo vuelve visible. Corregirlo es de `friccion.md` y de `aprender.md`.

**No busca la verdad.** Da el lugar donde la mirada propia termina.

**No elige entre dos miradas.** Si dos posiciones son válidas, eso lo decide la autoridad.

**No garantiza que se mueva solo.** Una pieza declara su sesgo; el sistema entero todavía puede no aprender. Eso es continuidad, y se mide en `aprender.md`, no aquí.

## Prueba

¿La pieza declara su posición y su límite? ¿El firmante es distinto del que la produjo, o se declaró `ninguno`? ¿El veredicto es `indeterminado` cuando no hay firmante? ¿Alineación y desviación están declaradas, o rotas, o en espera?

**Falsificador:** una pieza del guantelete sin `Sesgo:` ni `No se aplica a:`; un veredicto `pasa` firmado por quien produjo la pieza; una pieza que se presenta como neutral; la idea se descarta por no caber y sin nombrar la regla; la firma queda vacía y el veredicto se pone igual.

## Transiciones

- Falta el firmante → el veredicto es `indeterminado`, y se declara qué falta para firmarlo.
- La pieza se descarta sin nombrar la regla que rompe → no se descarta: se retiene con la regla declarada.
- La pieza cambia de posición → `mutar.md`, y se declara qué conserva.
- En cualquier otro caso → se entrega con su sesgo declarado, su límite y su firma.
