# Deterrente de VIDERE

**Unidad:** tarea.
**Aplica a:** sostener.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: dice qué se pierde si VIDERE deja de testificar.
**Lector:** quien va a emitir, y quien va a usar lo emitido.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la pérdida se lee desde el que clona el repo, no desde el que lo dejó.
**Límite:** no decide si el pase se alcanzó; eso lo decide el que lo lee.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `MEGA/mme/Ouroboros/formato de proceso.md`

**Variables:** cambio · pase · rastro · fricción · quién lo lee · qué queda
**Peor:** VIDERE deja un pase que parece completo, el que clona el repo confía, y **lo que se perdió recién se nota en el error siguiente**, cuando ya no se sabe cuál de los dos cambios lo trajo. **Lo peor no es que el pase falle: es que funciona, y por eso nadie lo vuelve a mirar.**
**Quién:** quien clona el repo y empieza a trabajar sin el que lo dejó, y quien carga con el error que se repite.

## Entra | Falla | Sale | Consume

- **Entra:** VIDERE en uso.
- **Falla si:** no dice qué se pierde cuando deja de testificar, o cuando empieza a decidir.
- **Sale:** la tabla `Si pasa esto | Se pierde | Y el síntoma es`, y el límite del paso.
- **Consume:** quien decide si el paso 2 se sostiene.

**Prueba:** ¿la pérdida se puede señalar? ¿el síntoma se ve cuando pasa?

**Falsificador:** un deterrente sin tabla; una pérdida que nadie puede señalar.

## Qué es

**VIDERE es el paso 2, y su oficio es atestiguar.** Este archivo dice **qué se pierde si deja de ser eso.**

**No es un escriba:** un escriba copia lo que le dictan. **VIDERE mira el repo y sabe qué cambió sin que nadie le dicte.** Si le dictan, dejó de ser testigo.

## Qué se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| VIDERE decide qué se hace | el testimonio | el que lee el pase no puede contradecir la decisión: ya viene tomada |
| VIDERE produce el cambio que testifica | la independencia | es juez y parte, y nadie puede señalar el error |
| el pase resume en vez de indicar | la acción siguiente | el que clona lee qué pasó y no qué hacer: reconstruye de cero |
| el pase necesita al que lo escribió | el segundo cero | el que clona no puede empezar sin preguntarle a alguien |
| un cambio queda sin fila | el rastro | el repo cambió y no hay por qué: el error aparece en la tercera mutación |
| se pierde una referencia ya nombrada | la trazabilidad | la idea que sostenía el sistema se reinvindica como nueva, o se descarta sin porqué |
| el pase escribe lo que el que lo lee quiere oír | la prueba | el pase confirma en vez de informar: se vuelve un espejo |

## Lo que VIDERE no es

**No es un tribunal.** No juzga si el pase está bien: dice qué cambió. Si eligió bien o mal, eso lo decide quien lee.

**No es un ejecutor.** No produce el cambio: lo ve. Un testigo que produce no puede testificar.

**No es un escriba.** No copia lo que le dictan: **lee el repo** y dice qué cambió. Si le dictan, es una voz, no un testigo.

**No es de una era.** No caduca cuando cambia la tecnología: caduca si deja de poder decir qué cambió.

## Prueba

¿El pase dice qué cambió y qué deja? ¿Se entiende sin el que lo escribió? ¿VIDERE sigue sin decidir? ¿Cada cambio tiene su fila?

**Falsificador:** un pase que necesita al autor; un veredicto sin porqué; un testigo que decide; un testigo que produce lo que testifica; un cambio sin rastro.

## Transiciones

- VIDERE empieza a decidir → `./ruta.md`, fila de decisión, y se declara.
- El pase no se entiende sin el autor → no es pase: se corrige.
- Un cambio quedó sin fila → se anota el vacío y se declara.
- En cualquier otro caso → se entrega y se cierra.
