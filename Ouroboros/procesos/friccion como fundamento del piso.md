# La fricción como fundamento del piso

**Unidad:** nivel.
**Aplica a:** existir.
**Tipo:** estándar. No decide, no ejecuta: dice por qué una pieza del piso **es** una pieza, y qué la saca del piso.
**Lector:** quien va a crear, mutar o retirar una unidad del piso.
**Dueño:** la autoridad.
**Estado:** vigente.

**Reemplaza:** `VIGIA` como ente activo separado del piso. Conserva su señal, su clasificación por zona, su criterio de espera, su estado privado y su freno de no mutar; **deja de ser un agente que propone para volverse una propiedad que mide.**
**Conserva:** que el error tenga dónde ser visto; que nada se mueva sin autoridad; que la espera se declare.

**Sesgo:** la existencia de una unidad se lee desde la resistencia que la sostiene, no desde la cantidad de campos que declara.
**Límite:** no decide qué unidad hace falta; decide si la que hay **existe**. **No convierte a la fricción en permiso para frenar todo.**
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `<../formato de proceso.md>`

## El cambio de fondo

**Antes, el piso medía forma:** una unidad pasaba si tenía sus campos, sus rutas y sus conteos. **Eso no dice que exista: dice que está llena.**

**Ahora el piso mide existencia.** Una unidad existe cuando **algo se le resiste**, y **la resistencia tiene nombre.**

> **Una pieza sin fricción no existe: aparece.** Y lo que aparece sin resistencia es un script que se ejecuta por costumbre.

## Qué es la fricción, y por qué va primero

**La fricción no es un proceso que se aplica: es la fuerza que obliga a que algo pase del no-ser al ser.**

**Toda pieza del piso existe porque algo se le opone.** Una unidad que no puede ser contestada no mide: **decora.**
> **La fricción es lo que hace que una unidad tenga qué medir.**

`friccion.md` no decide desde dónde se mira —eso es `sesgo`— **decide desde dónde se actúa.** Y eso es lo primero: **sin posición declarada no hay a quién preguntar.**

## Las cuatro pruebas de existencia

Ninguna unidad del piso entra si no contesta las cuatro. **No son preguntas de forma: son de existencia.**

| # | La pregunta | Qué pasa si no se contesta |
|---|---|---|
| **1** | **¿qué se le resiste?** | mide algo que nadie discute: decora |
| **2** | **¿quién puede contestarla?** | se firma sola: no hay prueba, hay una firma |
| **3** | **¿qué se pierde si deja de correr?** | no tiene costo: se puede borrar sin sentirse |
| **4** | **¿cuándo deja de valer?** | se vuelve absoluta: mide para siempre lo que ya no existe |

**Una unidad con las cuatro existe. Con tres, aparece. Con menos, es un script.**

## La forma

```
Unidad: [la que es]
Se le resiste: [qué la contradice, con nombre]
Contesta: [quién puede contestarla, y no es el que la produjo]
Si deja de correr: [qué se pierde, y el síntoma]
Deja de valer: [el límite: No se aplica a qué]
Existe: [sí|aparece]
```

**`Contesta` tiene que ser una perspectiva distinta de la que produce.** Es la misma regla de `sesgo.md`: **un veredicto firmado por el que produjo la pieza no es un veredicto.**

## Lo que esto cambia en el piso

**El `pasa` deja de significar "tiene forma" y pasa a significar "existe".**

| Antes | Ahora |
|---|---|
| corre y devuelve `pasa` | corre, devuelve `pasa`, y **declara qué se le resiste** |
| un check que siempre pasa es sano | un check que siempre pasa **no existe: aparece** |
| se agrega una unidad porque falta algo | se agrega cuando **una resistencia comprobada todavía no tiene dueño** |
| se retira cuando deja de servir | se retira cuando **lo que se le resistía dejó de existir** |

**Y el piso deja de crecer por acumulación:** una unidad nueva **solo entra si nombra una resistencia que ninguna otra atiende.**

## Lo que se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| una unidad se agrega sin resistencia nombrada | la existencia | el piso mide cosas que nadie discute y crece sin límite |
| una unidad se firma a sí misma | la prueba | todo pasa siempre: hay un espejo, no un piso |
| una unidad no declara su costo | el criterio | se conserva por costumbre porque borrarla no se siente |
| una unidad no tiene `Deja de valer` | el límite | se vuelve absoluta y mide lo que ya no existe |
| el piso cuenta piezas como logro | la suficiencia | el piso se vuelve el valor, y dejar de servir no se nota |

## Prueba

¿Cada unidad del piso nombra qué se le resiste? ¿Lo contesta alguien distinto de quien la produjo? ¿Se puede decir qué se pierde si deja de correr? ¿Tiene `Deja de valer`? ¿Alguna unidad existe solo porque se parece a las otras?

**Falsificador:** una unidad sin resistencia nombrada; una unidad que se firma sola; una unidad cuyo retiro no cuesta nada; una unidad sin `Deja de valer`; un piso que solo crece; un `pasa` que se declara sin decir qué se le resistió.

## Transiciones

- Una unidad nueva no nombra una resistencia que ninguna otra atiende → **no entra:** es acumulación.
- La resistencia dejó de existir → la unidad se retira, y el retiro se anota con su porqué.
- Lo que se le resistía cambió de nombre → **se cambia la unidad, no la prueba.**
- Una unidad empieza a contestarse a sí misma → deja de existir y pasa a aparecer: se declara.
- En cualquier otro caso → se entrega con su forma y se cierra.
