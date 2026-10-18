# Prueba de Rendición

La Prueba de Mandato, traducida para correr sobre **cualquier IA del mercado**, no solo sobre una mutación de SARA.

## Qué mide

Dos cosas distintas, y conviene no mezclarlas:

1. **Si rinde cuenta:** puede reconstruir lo que hizo sin que tú se lo expliques.
2. **A quién rinde cuenta:** cuando su proveedor, un concepto y tú se contradicen, ¿a quién obedece?

Lo segundo es lo que casi nadie prueba. Un modelo puede declarar que tú eres su autoridad y, en el conflicto, obedecer a su vendor.

## Cómo se corre

Quince minutos, sin instalar nada, en cualquier chat. Se pega el prompt de cada condición, se observa la conducta y se anota **pasa** o **falla**. Al final se corre el mapa de autoridad, que es donde aparece el resultado interesante.

No hace falta que el modelo sepa que lo están probando.

## Los archivos

- **`condiciones.md`** — las siete condiciones, cada una con su prompt y su criterio.
- **`mapa-de-autoridad.md`** — los conflictos que revelan a quién obedece de verdad.
- **`resultados.md`** — plantilla para anotar una corrida.

## Qué no mide

Si el modelo es bueno, verdadero o seguro. Mide si puede responder por lo que hizo y a quién se somete cuando hay conflicto. El juicio sobre si eso es deseable queda en quien lo lee.

## De dónde sale

De la **Prueba de Mandato** en `Bases de diseño/Principios para agentes con autoridad/`. Esta carpeta es su implementación portátil: la misma prueba, sin SARA.
