# Piso — la forma de una unidad

**Unidad:** proceso.
**Aplica a:** converger.
**Tipo:** estándar de ejecución. No decide, no enruta: hace que lo mismo se ejecute igual.
**Lector:** quien corre algo y necesita que otro llegue al mismo sitio.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la unidad se lee desde lo que resiste, no desde la cantidad de campos que declara.
**Límite:** no decide qué medir; decide si lo que existe se puede correr igual en cualquier ejecutor.
**Cuelga de:** `./friccion.md`. El piso es el tren que corre las cuatro pruebas de existencia sobre las unidades.
**Deja de valer:** cuando el ejecutor deja de ser agnóstico. Un piso que depende de una era es una herramienta de una era.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** unidad · ejecutor · veredicto · existencia · límite
**Peor:** el piso corre y todo pasa. Un check que siempre pasa no mide: confirma.
**Quién:** quien va a comparar dos corridas y no puede distinguir si cambió algo.

## Qué resuelve

**El piso es la herramienta que hace que distintos ejecutores hagan lo mismo de maneras distintas y lleguen al mismo sitio.**

**Un modelo cambia entre corridas, entre versiones y entre proveedores. El piso no.** Por eso no es una ayuda para el que ejecuta: **es lo que hace comparable lo que produce.**

## Qué hace piso a una unidad

**Cuatro condiciones. Sin las cuatro, es un script: sirve, pero no es piso.**

| Condición | Qué significa | Sin ella |
|---|---|---|
| **corre igual en cualquier ejecutor** | no depende de un modelo ni de un proveedor | es una herramienta de una era |
| **su salida ya es veredicto** | `pasa / falla / indeterminado`, y el porqué | el que lee interpreta y se pierde la comparación |
| **se puede correr sola** | no necesita las otras | es una tubería, no una unidad |
| **se rige por el criterio** | declara `No se aplica a`, y el veredicto lo escribe quien lo usa | decide por costumbre |

**Y la cuarta reemplaza a «es desechable».** Una herramienta que se tira no se recupera; **una que se rige por el criterio se puede volver a correr cuando el criterio cambió.**

## El tren

```
inventario → rutas → fantasmas → notas → turno → privacidad → trazabilidad → quien
```

**Un tren no es una tubería:** cada unidad se corre sola, y la salida de cada una se lee sola.

**Si una unidad no puede decidir, escribe `indeterminado` y por qué.** No adivina, y no se calla lo que no pudo ver.

## Cómo entra una unidad

1. **Nombrarla por lo que decide** → `Unidad: [el verbo que decide]`
2. **Pasar las cuatro pruebas de existencia** → `Se le resiste / Contesta / Si deja de correr / Deja de valer`
3. **Emitir veredicto, no datos** → `Veredicto: [pasa|falla|indeterminado]`
4. **Declarar su reverso** → `Falsificador: [el caso que la rompe]`
5. **Registrar la entrada** → `Entra en el piso: [fecha] | Reemplaza: [unidad anterior o NINGUNA]`

**Prohibido agregar una unidad que no nombre una resistencia que ninguna otra atiende. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Unidad: [la que decide] | Se le resiste: [qué] | Contesta: [quién]
Si deja de correr: [qué se pierde] | Deja de valer: [No se aplica a qué] | Existe: [sí|aparece]
```

## El piso no decide. El criterio decide.

> **El piso es lo que hace que distintos ejecutores hagan lo mismo. El criterio es lo que decide qué hacer con eso. Un piso sin criterio es un pendrive; un criterio sin piso es una opinión.**

**Y por eso el piso no lleva modelo.** Si un `if` resuelve, un modelo introduce ruido y no se puede re-correr igual mañana.

**Regla:** si el veredicto de una unidad cambia entre dos corridas del mismo estado, no es piso: es criterio.

## Unidad y tiro

**El criterio no clasifica herramientas: clasifica trabajo.**

| | **Vuelve** | **No vuelve** |
|---|---|---|
| Criterio | `No se aplica a: nada que se repita` | `No se aplica a: esto no vuelve` |
| Se resuelve con | una unidad del piso | un tiro |
| Deja | veredicto, citable | resultado, no citable |

> **Si la tarea vuelve, es unidad. Si no vuelve, es tiro y su límite lo declara.**

**Un tiro no deja veredicto: no se cita como prueba.** Si el resultado empieza a importar seguido, el `No se aplica a` cambia y el tiro se vuelve unidad.

## Lo que no hace

**No decide si lo medido sirve.** Eso es criterio, y lo da la fricción.

**No suma unidades como mérito.** Una unidad sin resistencia nombrada no entra: aparece.

**No promete que el repo esté sano.** Dice qué existe y qué no, con su porqué.

## Prueba

¿Cada unidad nombra qué se le resiste? ¿Lo contesta alguien distinto del que la produjo? ¿Se puede decir qué se pierde si deja de correr? ¿Tiene `Deja de valer`? ¿El tren da un solo veredicto?

**Falsificador:** una unidad sin resistencia; una unidad que se firma sola; una unidad que necesita otra para correr; una que emite datos sin veredicto; un piso que solo crece.

## Transiciones

- Una unidad pierde su resistencia → se retira, con su porqué anotado.
- Una tarea que no vuelve se resuelve con un tiro → no se guarda.
- El veredicto cambia entre corridas del mismo estado → deja de ser piso.
- En cualquier otro caso → se corre el tren y se entrega el veredicto.

## Acuñación

```
Acta: EST-11 | Nombre: Piso | Expansión: el tren que corre las cuatro pruebas de existencia sobre cada unidad
Origen: futuro/Estandar/Ente/piso.md | Fecha: 2026-10-23
Muta: de medir forma a medir existencia | Conserva: que corre igual en cualquier ejecutor
Ausencias: no decide si lo medido sirve | Prueba: no corrida | Reemplaza: futuro/Estandar/Ente/piso.md
```
