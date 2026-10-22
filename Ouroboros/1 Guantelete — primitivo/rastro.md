**Variables:** pieza · sesgo · firma · continuidad · regla
**Peor:** una regla se sostiene con una sola perspectiva, nadie puede contestarla, y se lee como si no tuviera sitio
**Quién:** quien usa la regla, y quien carga con que su error no pueda ser visto

# Guantelete

**Unidad:** tarea.
**Aplica a:** sostener.
**Tipo:** tarea de paso .. No produce poder: sostiene las reglas que ordenan todo lo demás.
**Lector:** quien va a producir, mutar o aplicar un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el cuerpo se lee desde lo que se puede verificar, no desde lo que se quiere.
**Límite:** no decide si el paso 2 la abstrae bien; eso es S.A.R.A.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `formato de proceso.md`

## Qué es

El **paso .** de `Ouroboros/`. Su tarea es fijar **desde dónde se sostiene cada regla**, y quién puede contestarla.

**Una regla no se sostiene sola: se sostiene desde un sitio.** Una regla que no dice desde dónde habla es la que nadie puede revisar, y una regla que nadie puede revisar termina decidiendo por costumbre. Por eso esta tarea no junta piezas: **exige que cada pieza declare su posición, su límite y su firmante.**

## Entra | Falla | Sale | Consume

- **Entra:** una pieza de la base, y quien la abre.
- **Falla si:** una pieza se sostiene sin declarar su posición; su veredicto lo firma quien la produjo; una herramienta ocupa el lugar de la base y nadie lo declara.
- **Sale:** el veredicto de qué piezas hay, desde dónde se sostienen, quién las puede contestar y qué se pierde si el guantelete se vuelve catálogo.
- **Consume:** quien va a cruzar la puerta hacia el paso 2, y quien va a contestar una pieza.

**Prueba:** ¿cada pieza declara posición, límite y firmante? ¿alguna herramienta ocupa el lugar de la base? ¿el guantelete se mide por lo que sostiene y no por cuántas piezas tiene?

**Falsificador:** una pieza sin sesgo declarado; un veredicto firmado por el que produjo la pieza; un catálogo que solo crece; una herramienta defendida por antigüedad.

## Las dos piezas

| Pieza | Qué decide | Qué la refuta |
|---|---|---|
| **sesgo** — `./primitivos/sesgo.md` | desde dónde se sostiene una pieza, y quién puede contestarla | la pieza se presenta como neutral, o su veredicto se firma solo |
| **fricción** — `./primitivos/friccion.md` | que la decisión pase por quien la toma antes de mover nada | la decisión se ejecuta sin pasar por quien la toma |

**`X` muta.** Dos hoy; mañana pueden ser otras.

**`sesgo` es el fundamento.** Sin él, `fricción` se puede aplicar a una decisión que nadie declaró desde dónde se tomó, y la fricción se vuelve trámite. **`fricción` es su uso:** mirar desde dónde se decide, y no decidir sin pasar por quien puede contestarlo.

## Lo que queda fuera de esta pieza

**Las herramientas se aplican; no se fundamentan.** Manipular, aplicar, mutar, retirar, deducir y decir son procesos que se ejecutan sobre lo que ya tiene posición declarada. Viven en `./herramientas/`, y ninguna ordena sobre otra.

**Una herramienta no cambia de lugar por su número.** Si una herramienta resulta ser la base de otra, se sube con `Reemplaza:`, y se declara qué conserva.

## Qué no se toca

- **Una pieza no se usa sola para sostener una decisión sobre otro.** Se puede ejecutar; sin firma, su veredicto es `indeterminado`.
- **El firmante no es quien produjo la pieza.** Rige `./primitivos/sesgo.md`, `Su forma`.
- **El guantelete no da poder.** «Sostener» es lo que permite que otro lo revise.

## Cómo se verifica

1. **Cada pieza declara `Sesgo`, `Límite`, `Firma` y `Continuidad`.** Rige `./primitivos/sesgo.md`.
2. **Alineación y desviación se declaran**: rotas, firmadas, o en espera. Rige `./primitivos/sesgo.md`, `Alineación y desviación`.
3. **La fricción no tiene rama de imposición.** Rige `./primitivos/friccion.md`.
4. **Las herramientas no se cargan sin una pieza que las sostenga.** Rige `./ruta.md`.

## Prueba

¿Cada pieza declara desde dónde se sostiene y quién la contesta? ¿Hay alguna cuyo veredicto se firme a sí misma? ¿La fricción se aplicó sobre una posición declarada?

**Falsificador:** una pieza sin sesgo; un veredicto `pasa` sin firmante distinto del que produjo; una fricción sobre una decisión que no se declaró desde dónde se tomó; una herramienta ocupando el lugar de la base.

## Transiciones

- Una pieza deja de sostenerse → `./herramientas/retiro.md`.
- Una regla se descarta sin nombrar la que rompe → `./primitivos/sesgo.md`, `Transiciones`.
- El paso . se cierra → `../2 S.A.R.A — mutación`.
- En cualquier otro caso → se entrega con su sesgo declarado y su firma.
