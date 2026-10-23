# Piso — el estándar de la unidad que mide

**Unidad:** nivel.
**Aplica a:** medir.
**Tipo:** estándar. No se ejecuta: se cumple. Dice **cómo tiene que ser** una unidad del piso, y cuándo deja de serlo.
**Lector:** quien va a medir algo de forma repetible, y quien va a leer la medición sin el que la corrió.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué forma fija

**Que una unidad sirva para comparar. Un modelo cambia entre corridas, entre versiones y entre proveedores. La unidad no.**

**Lo mismo tiene que medirse igual, en cualquier ejecutor, hoy y mañana.**

## El rastro: las cuatro condiciones

**Sin las cuatro, es un script: sirve, pero no es unidad.**

| Condición | Qué significa | Sin ella |
|---|---|---|
| **corre igual en cualquier ejecutor** | no depende de un modelo, un proveedor ni una versión | es una herramienta de una era |
| **su salida ya es veredicto** | `pasa`, `falla` o `indeterminado`, con el porqué | el que lee interpreta, y ahí se pierde la comparación |
| **se puede correr sola** | no necesita a las otras para dar un resultado | es parte de una tubería, no una unidad |
| **se rige por el criterio** | declara a qué no se aplica, y el veredicto lo escribe quien lo va a usar | decide por costumbre |

**Y la cuarta reemplaza a «es desechable».** **Una unidad que se tira no se recupera; una que se rige por el criterio se puede volver a correr cuando el criterio cambió.**

## La ruta: qué se carga para medir

| Se va a… | Se carga… | Sin la autoridad… |
|---|---|---|
| **dar un veredicto sobre algo** | `./criterio.md`, con su límite | **no hay veredicto** |
| **decidir qué se pone a prueba** | `./VIDAL.md`, las siete características | **no se sabe qué se está midiendo** |
| **escribir el resultado** | `./claridad.md`, de una sola lectura | **no se puede contestar** |
| **anotar la corrida** | `./memoria continua.md`, con su posición | **el resultado se pierde con el contexto** |
| **cambiar una unidad del piso** | el estándar entero, y se espera | **no se cambia** |

## La unidad no decide

> **La unidad es lo que hace que distintos ejecutores midan lo mismo. El criterio decide qué hacer con eso.**
>
> **Una unidad sin criterio es un pendrive; un criterio sin unidad es una opinión.**

**Y por eso la unidad no lleva modelo.** **Si una condición resuelve, un modelo introduce ruido y no se puede repetir igual mañana.**

**Regla:** **si el veredicto cambia entre dos corridas del mismo estado, no es unidad: es criterio.**

## La carga: qué se pierde

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **el veredicto cambia entre dos corridas del mismo estado** | la unidad | es criterio disfrazado de herramienta |
| **la salida son datos y no un veredicto** | la comparación | cada uno lee lo que quiere |
| **la unidad necesita a otra para correr** | la independencia | es una tubería: si una se rompe, todas |
| **no declara a qué no se aplica** | el límite | se usa para todo y mide lo que ya no existe |
| **una unidad se agrega sin nombrar qué la contradice** | la existencia | el piso crece sin que nada lo justifique |
| **el piso se lee como mérito por cantidad** | el criterio | el número de unidades se vuelve el valor |

## Lo que el estándar no hace

**No fija cuántas unidades hay, ni cómo se llaman, ni en qué archivos viven.** **Fija cuándo algo es unidad.**

**No decide si lo medido sirve.** **Mide si existe y si aguanta; si sirve, lo dice el uso.**

**No hereda la unidad.** **Una unidad que fue válida con un criterio no lo es con otro: se vuelve a correr.**

**No nombra un modelo ni una era.** **Si la unidad solo funciona con una tecnología, no es unidad: es herramienta de esa tecnología.**

## Prueba

**¿La unidad corre igual en dos ejecutores distintos?** **¿Su salida es un veredicto con porqué?** **¿Se puede correr sola?** **¿Declara a qué no se aplica?** **¿Nombra qué la contradice?**

**Falsificador:** una unidad que cambia de resultado sin que cambie el estado; una que emite datos sin veredicto; una que necesita otra para correr; una sin límite declarado; una agregada sin nombrar su contradicción; un piso que solo crece.
