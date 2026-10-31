# EL PISO — lo que hace comparable lo que produce un ejecutor

**Hecho:** 2026-10-31, y reconstruido de dos piezas: **la que dio la autoridad este día, y el `piso.md` del `2026-10-23`, commits `ba5a4fc` y `04e1ee7`.**
**Clase:** teoría. **Estado:** vigente.
**Lector:** quien va a medir algo, y quien va a leer la medida sin el que la corrió.
**Dueño:** **quien tiene la autoridad en el proyecto donde se aplica.**

**Sesgo:** se mide desde lo que se puede repetir, y no desde lo que se puede explicar.
**Límite:** **no decide si lo medido sirve.** **Mide si existe, y si aguanta.**
**Firma:** **quien responde por el acto, con su nombre** · **y quien lo ejecuta.**

---

## Lo que dispone

> **El piso es la herramienta que hace que distintos ejecutores hagan lo mismo de maneras distintas, y lleguen al mismo sitio.**
> **Y por eso el piso no es una ayuda para el que ejecuta: es lo que hace comparable lo que produce.**

**Un modelo cambia entre corridas, entre versiones, y entre proveedores.** **El piso no.**

**Y se llama por lo que decide, y no por cómo está hecha.** **Porque el nombre de una herramienta dice el acto, y no el lenguaje.**

---

## El corte

> **El piso es lo que hace que distintos ejecutores hagan lo mismo.**
> **El criterio es lo que decide qué hacer con eso.**
> **Un piso sin criterio es un pendrive; un criterio sin piso es una opinión.**

**Y por eso el piso no lleva modelo.** **Si un `if` resuelve, un modelo introduce ruido, cuesta por corrida, y no se puede volver a correr igual mañana.** **Un modelo que decide en el piso no es piso: es criterio disfrazado de herramienta.**

**Y la regla que lo prueba:** **si el veredicto cambia entre dos corridas del mismo estado, no es piso: es criterio.**

---

## Las cuatro condiciones, y sin ellas no es unidad

> **Sin las cuatro, es un script: sirve, pero no es unidad.**

| La condición | Y qué significa | Y sin ella |
|---|---|---|
| **corre igual en cualquier ejecutor** | **no depende de un modelo, una versión, ni un proveedor** | **es una herramienta de una era** |
| **su salida ya es un veredicto** | **no emite materia prima: emite `pasa`, `falla`, o `indeterminado`, y por qué** | **el que lee interpreta, y ahí se pierde la comparación** |
| **se puede correr sola** | **no necesita a las otras para dar un resultado** | **es parte de una tubería, y no una unidad** |
| **es desechable** | **se tira cuando deja de servir, sin tocar lo que chequeaba** | **se vuelve un sistema que hay que mantener** |

**Y la cuarta es la que se olvida.** **Una unidad que hay que mantener dejó de ser instrumento: se volvió parte del problema.**

---

## Y el tren: no son un programa

**Las unidades no son un programa: son un tren.** **Cada una consume la salida de la anterior, y ninguna resuelve el problema entero.**

```plaintext
inventario  ->  pares  ->  integridad  ->  veredicto
```

**Y la regla de cada una:** **si no puede decidir, escribe `indeterminado` y por qué.** **No adivina, y no se calla lo que no pudo ver.**

| La unidad | Qué decide | Y qué no puede ver |
|---|---|---|
| **`inventario`** | **qué procesos hay, cuáles están completos, y qué campo falta** | **si lo que falta importa** |
| **`pares`** | **qué hermanos se pueden comparar** | **cuáles se contradicen** |
| **`integridad`** | **la contradicción, la disfrazada, y el huérfano** | **si un implícito conceptual está cerrado** |
| **`veredicto`** | **`pasa` o `falla`, y qué quedó `indeterminado`** | **lo que ninguna unidad pudo mirar** |

---

## Y la dirección: hacia dónde mira el piso

> **Los estándares mutan hacia abajo, y nunca hacia arriba.**

**La fuente es de la autoridad, y lo que se produce obedece.** **Y ningún eslabón devuelve el cambio hacia arriba.**

**Y cuando la fuente muta, lo de abajo queda atrasado, y el atraso se mide.** **Un ente enrutado contra un estándar que ya mutó no está roto: está atrasado, y el atraso no se supone: se mide.**

**Y lo que esto impide, que ya ocurrió:** **alguien se declaró alineado mientras citaba un criterio que ya no existía, y ninguna unidad lo vio, porque ninguna medía la dirección.** **Una prueba que falte no es un pendiente: es lo que deja pasar el atraso.**

---

## Y el estándar no nombra su propia carpeta

> **El estándar declara su relación con lo que mide, y no su dirección postal.**

**Una carpeta muda.** **Y cuando muda, lo que cita rutas rotas no queda mal: queda atrasado, y su atraso se confunde con un error de contenido.**

**Y eso ya ocurrió, y más de dos veces.** **Cada mudanza rompió las citas, y una unidad las encontró todas, pero sólo porque la unidad estaba corriendo.** **Una mudanza sin unidad que la mida se descubre en el tercer error.**

**Y la razón de fondo:** **una ruta es una comodidad de una era, y no una condición de la forma.** **El estándar dice qué tiene que pasar; el que lo aplica dice dónde se lee hoy.**

---

## Y lo que se pierde, con su síntoma

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **el veredicto cambia entre dos corridas del mismo estado** | **la unidad** | **es criterio disfrazado de herramienta** |
| **la salida son datos, y no un veredicto** | **la comparación** | **cada uno lee lo que quiere** |
| **la unidad necesita a otra para correr** | **la independencia** | **es una tubería: si una se rompe, todas** |
| **no declara a qué no se aplica** | **el límite** | **se usa para todo, y mide lo que ya no existe** |
| **una unidad se agrega sin nombrar qué la contradice** | **la existencia** | **el piso crece, y nada lo justifica** |
| **el piso se lee como mérito por cantidad** | **el criterio** | **el número de unidades se vuelve el valor** |
| **la unidad no dice qué mutación detecta** | **la dirección** | **lo de abajo se atrasa, y nadie lo ve** |
| **el que se mide se mide a sí mismo** | **la regla** | **se confirma solo, y hay firma en vez de veredicto** |

---

## Lo que esta pieza NO afirma

**No fija cuántas unidades hay, ni cómo se llaman, ni en qué archivos viven.** **Fija cuándo algo es unidad, y hacia dónde mira.**

**No decide si lo medido sirve.** **Mide si existe y si aguanta; si sirve, lo dice el uso.**

**No hereda la unidad.** **Una unidad que fue válida con un criterio, no lo es con otro: se vuelve a correr.**

**No nombra un modelo ni una era.** **Si la unidad sólo funciona con una tecnología, no es unidad: es herramienta de esa tecnología.**

**Y no declara correcto a nadie.** **Una unidad que pasa no declara correcto al ente: declara que aguantó esa corrida.**

---

## Prueba

**¿La unidad corre igual en dos ejecutores distintos? ¿Su salida es un veredicto con porqué? ¿Se puede correr sola? ¿Se puede tirar sin tocar lo que chequeaba? ¿Dice qué mutación detecta? ¿Y el que se mide se mide a sí mismo?**

**Falsificador:** **una unidad que necesita un modelo para dar veredicto; una que emite datos y no conclusión; una que sólo corre junto a las otras; una que se nombra por su lenguaje; una que cambia de resultado sin que cambie el estado; una que hay que mantener; un estándar que nombra la carpeta donde vive; y un atraso que se descubre por la pregunta de alguien y no por una corrida.**
