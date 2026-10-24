# Piso — el estándar de la unidad que mide

**Unidad:** nivel.
**Aplica a:** medir.
**Tipo:** estándar. No se ejecuta: se cumple. Dice **cómo tiene que ser** una unidad del piso, y cuándo deja de serlo.
**Lector:** quien va a medir algo de forma repetible, y quien va a leer la medición sin el que la corrió.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** se mide desde `./criterio.md`: **no hay verdad que alcanzar, hay utilidad hacia la que sesgarse.** Una unidad no prueba que algo sea correcto: **mide si aguantó.**
**Límite:** no se aplica a juzgar si lo medido sirve. Mide si existe y si aguanta.
**Firma:** humano:autoridad · máquina:quien corra la unidad.

## Qué forma fija

**Que una unidad sirva para comparar. Un modelo cambia entre corridas, entre versiones y entre proveedores. La unidad no.**

**Lo mismo tiene que medirse igual, en cualquier ejecutor, hoy y mañana.**

## La dirección: el estándar muta a MANTIS, y no muta de Ouroboros

**Y esta es la regla que fija hacia dónde mide el piso.**

> **Los estándares mutan a MANTIS. Los estándares no mutan de Ouroboros.**

**`Ouroboros/` son entes estándar hechos por la autoridad.** **Son la fuente, no el destino.** **Lo que vive ahí no se muta desde abajo: ni por MANTIS, ni por una unidad, ni por la conveniencia de un turno.**

| Quién | Puede mutar | No puede mutar |
|---|---|---|
| **la autoridad, en `Ouroboros/`** | los entes estándar | — |
| **el estándar** | MANTIS, sus procesos, su memoria | **`Ouroboros/`** |
| **MANTIS** | su carta, sus procesos, su memoria | **`Ouroboros/`, la tesis** |
| **la unidad del piso** | nada: **mide y da veredicto** | **`Ouroboros/`**, y el ente que mide |

**La dirección es de una sola vía hacia abajo.** **`Ouroboros/` produce estándar; el estándar moldea a MANTIS.** **Ningún eslabón de la cadena devuelve el cambio hacia arriba.** **Si MANTIS necesita algo del estándar que no existe, se pide a la autoridad; no se agrega desde MANTIS.**

**Cuando un ente de `Ouroboros/` muta, MANTIS queda atrasado hasta que se realinea, y eso se mide.** **Un ente enrutado contra un estándar que ya mutó no está roto: está atrasado, y el atraso se mide, no se supone.**

**Y lo que esto impide, que es el error que ya ocurrió:** **MANTIS se declaró enrutado mientras citaba un criterio que ya no existía, y ninguna unidad lo vio porque ninguna medía la dirección.** **Una prueba que falte no es un pendiente: es lo que deja pasar el atraso.**

**Ancla:** `Ouroboros/` manda; MANTIS obedece; la unidad mide.

**Falsificador:** **un archivo de `Ouroboros/` mutado por MANTIS o por una unidad**; una unidad que edita el ente que mide; un ente que se declara enrutado sin que ninguna unidad lo compruebe después de una mutación del estándar; un atraso que se descubre por la pregunta de alguien y no por una corrida.

## El rastro: las cuatro condiciones

**Sin las cuatro, es un script: sirve, pero no es unidad.**

| Condición | Qué significa | Sin ella |
|---|---|---|
| **corre igual en cualquier ejecutor** | no depende de un modelo, un proveedor ni una versión | es una herramienta de una era |
| **su salida ya es veredicto** | `pasa`, `falla` o `indeterminado`, con el porqué | el que lee interpreta, y ahí se pierde la comparación |
| **se puede correr sola** | no necesita a las otras para dar un resultado | es parte de una tubería, no una unidad |
| **se rige por el criterio** | declara a qué no se aplica, y el veredicto lo escribe quien lo va a usar | decide por costumbre |

**Y la cuarta reemplaza a «es desechable».** **Una unidad que se tira no se recupera; una que se rige por el criterio se puede volver a correr cuando el criterio cambió.**

**Y hay un quinto requisito, que no es condición de forma sino de dirección:** **toda unidad dice qué mutación del estándar detecta.** **Una unidad que no nombra qué cambio la pone en rojo no mide el estándar: mide el pasado.**

## La ruta: qué se carga para medir

| Se va a… | Se carga… | Sin la autoridad… |
|---|---|---|
| **dar un veredicto sobre algo** | `./criterio.md`, con su límite | **no hay veredicto** |
| **decidir qué se pone a prueba** | `./VIDAL.md`, las siete características | **no se sabe qué se está midiendo** |
| **escribir el resultado** | `./claridad.md`, de una sola lectura | **no se puede contestar** |
| **anotar la corrida** | `./memoria continua.md`, con su posición | **el resultado se pierde con el contexto** |
| **medir la dirección estándar → ente** | esta sección, `La dirección`, y la carta del ente | **no se sabe si el ente está alineado o atrasado** |
| **cambiar una unidad del piso** | el estándar entero, y se espera | **no se cambia** |

**La fila de la dirección es la que faltaba.** **Sin ella, el piso medía existencia y no medía si el ente seguía enrutado al estándar vigente.**

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
| **la unidad no dice qué mutación detecta** | la dirección | el ente se atrasa del estándar y nadie lo ve |
| **el ente mide en vez de ser medido** | la regla | se confirma a sí mismo, y hay firma en vez de veredicto |

## Lo que el estándar no hace

**No fija cuántas unidades hay, ni cómo se llaman, ni en qué archivos viven.** **Fija cuándo algo es unidad, y hacia dónde mira.**

**No decide si lo medido sirve.** **Mide si existe y si aguanta; si sirve, lo dice el uso.**

**No hereda la unidad.** **Una unidad que fue válida con un criterio no lo es con otro: se vuelve a correr.**

**No nombra un modelo ni una era.** **Si la unidad solo funciona con una tecnología, no es unidad: es herramienta de esa tecnología.**

**No cierra un grado.** Rige `./criterio.md`, `El grado no se cierra por aprobación`: **una unidad que pasa no declara correcto al ente: declara que aguantó esa corrida.**

## Prueba

**¿La unidad corre igual en dos ejecutores distintos?** **¿Su salida es un veredicto con porqué?** **¿Se puede correr sola?** **¿Declara a qué no se aplica?** **¿Nombra qué la contradice?** **¿Dice qué mutación del estándar detecta?** **¿Mide al ente, o el ente mide?**

**Falsificador:** una unidad que cambia de resultado sin que cambie el estado; una que emite datos sin veredicto; una que necesita otra para correr; una sin límite declarado; una agregada sin nombrar su contradicción; un piso que solo crece; **una unidad que no dice qué mutación detecta; un ente que se mide a sí mismo; un estándar que MANTIS mutó.**
