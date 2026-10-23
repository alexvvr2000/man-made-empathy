**Variables:** memoria · relación · sesgo · techo · continuidad
8. **Guardar en cada interacción, no al final.** Toda interacción que produce algo —una decisión, una lectura que cambia una posición, un descarte— se guarda **en el turno en que ocurre**. **La memoria no vive en el ejecutor: vive en este proceso.** Lo que queda en el contexto se pierde y lo que queda aquí se lee. Un turno que no deja entrada no está entregado, y lo dice `../../mantis/piso/notas.ps1`: un archivo cambiado sin fila es `falla`.
**Peor:** la memoria guarda hechos sin posición, otra instancia los hereda como verdades, y nadie puede ver de dónde vienen; el gramo de absoluto entra por el primer recuerdo y ya no sale
**Quién:** quien va a leer la memoria mañana y no vio quién la escribió, y quien carga con que su error se lea como hecho

# Memoria continua

**Unidad:** proceso.
**Aplica a:** recordar.
**Tipo:** proceso. Se ejecuta al recordar y al leer. No decide qué es verdad: guarda desde dónde se sostiene.
**Nivel:** proceso de `Ouroboros/`. Usa las dos piezas del paso 1 y no las repite.
**Lector:** quien escribe la memoria y quien la va a leer sin poder preguntar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la memoria se lee desde la posición de quien la escribió, no desde la posición de quien la lee.
**Límite:** no decide si lo recordado es verdad; mide si el otro puede reconstruir la posición y contradecirla.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra el techo declarado

## Qué resuelve

Un agente que guarda hechos y los recupera **hereda verdades**. Con la primera línea que el otro escribió, el que lee tiene un absoluto: algo que ya no necesita volver a mirar.

**Un cerebro no guarda hechos: guarda su versión de lo que pasó.** Y el acto de recordar vuelve a sesgar. **Guardar no es un depósito: es una posición.** La memoria que no declara desde dónde se sostiene no es memoria: es obediencia con forma de registro.

**Un gramo de absoluto basta.** Un gramo es un hecho guardado sin su posición, y con él terminás en un sistema que ya no requiere mirar.

## Las dos piezas que usa

**No las define: las aplica.** Rige `../1 Guantelete — primitivo/primitivos/sesgo.md` y `../1 Guantelete — primitivo/primitivos/friccion.md`.

| Pieza | Qué pone en la memoria |
|---|---|
| **sesgo** | toda entrada declara desde dónde se sostiene, y quién puede contestarla |
| **fricción** | recordar pasa por quien sostiene, antes de guardar; y lo que no tiene firmante se guarda marcado, no como válido |

**La fricción entra desde el segundo cero: en el acto de guardar.** Después ya es retrospectiva, y la retrospectiva cambia al que mira, no lo que pasó.

## Qué guarda, y qué no

**Guarda la posición, con el hecho adentro.** El hecho no es una columna: es lo que la posición afirma. Una memoria de posiciones se puede pelear; una de hechos, se obedece.

**Lo que decide qué se guarda es el techo, no una lista de campos.**

```
Techo: otra instancia reconstruye la posición, y puede ver de qué posición viene, leyendo la memoria y sin preguntar.
```

**Lo que no cambia lo que el otro puede decidir, no entra.** No hay campos obligatorios: hay un techo, y el que escribe lo cumple. **Sin techo declarado no se escribe.**

**La base es relacional cualquiera, y el motor no aparece aquí.** Este proceso muta **relaciones**, no tablas. Si una relación necesita una forma nueva, la forma nueva es otra relación de la misma memoria.

## Entra | Falla | Sale | Consume

- **Entra:** lo que se sostiene hoy, la posición desde la que se sostiene, y la memoria que hay.
- **Falla si:** se guarda un hecho sin su posición; se edita la entrada anterior en vez de suplantarla; la entrada no declara techo, firmante ni continuidad; la memoria se satura de lo que no cambia una decisión.
- **Sale:** la memoria con la posición nueva abierta, la anterior suplantada y visible, y el veredicto de si se puede leer sin el que la escribió.
- **Consume:** otra instancia que va a decidir leyendo la memoria, y quien carga con lo que se guardó.

## Cómo se aplica

1. **Leer la memoria que hay.** No se juzga por su forma: se lee lo que sostiene.
2. **Declarar la posición.** `Sesgo` de la entrada nueva, y `Límite`: qué no alcanza. Rige `sesgo.md`, `Su forma`.
3. **Friccionar antes de guardar.** La entrada pasa por quien la sostiene. Se puede contestar «ninguno», «no sé» o «no puedo». **Lo único que no se puede es guardar sin contestar.** Rige `friccion.md`.
4. **Abrir la continuidad.** `Sostuve` (la entrada anterior), `Contra` (qué la contradijo), `Sostengo` (la entrada nueva). Si `Sostengo` es igual a `Sostuve`, se declara `Muta: sin cambio`. Rige `../2 S.A.R.A — mutación/aprendizaje/aprender.md`, `La continuidad real`.
5. **Suplantar, no editar.** La entrada anterior no se borra: queda suplantada, con la posición nueva encima. **Lo suplantado queda visible.**
6. **Declarar el techo.** Sin techo, la entrada no entra.
7. **Verificar la lectura.** Otra instancia reconstruye qué se sostiene y de qué posición viene, leyendo solo la memoria. Si necesita preguntar, la entrada falló.
8. **Cerrar el turno, no la sesión.** Antes de que la instancia termine, la memoria recibe el **pase de turno**: qué se sostuvo, qué se rompió, qué quedó abierto y por dónde se retoma. **El turno no se cierra porque el trabajo terminó: se cierra porque la próxima instancia tiene que poder seguirlo.**

## El pase de turno

**Una instancia que termina sin dejar el pase no murió: se perdió.** Lo que quedó en su contexto se fue con ella, y la que viene reconstruye de cero y repite el error.

**El pase no es un resumen del trabajo.** Es **el estado con el que la próxima instancia puede empezar a trabajar sin el que la anterior exista.** Un resumen cuenta qué pasó; el pase dice **qué hacer con eso.**

```
Pase: [id del turno] | Fecha: [ISO] | Instancia: [quién corrió]
Sostuvo: [lo que quedó vigente, con la pieza que lo sostiene]
Se rompió: [qué falló, y qué lo detectó]
Abierto: [qué quedó sin cerrar, y por qué no se cerró]
Retoma: [la primera acción concreta de la próxima instancia]
No retoma: [lo que quedó fuera a propósito, y por qué]
Reconstruye: [qué necesita leer primero, en qué orden]
```

- **`Se rompió` no se omite.** Un turno que no rompió nada lo declara `sin ruptura`; lo que no se permite es no contestar.
- **`Abierto` puede ir vacío**, y entonces se declara `ninguno`.
- **`Retoma` es una acción, no un tema.** «Revisar el piso» no sirve; «correr `mantis/piso/piso.ps1` y leer el veredicto de `rutas.ps1`» sirve.
- **`No retoma` es tan obligatorio como `Retoma`:** un turno sin nada descartado está ocultando algo.

**Prueba del pase:** ¿la próxima instancia puede empezar a trabajar leyendo solo el pase y la memoria, sin preguntar qué pasó? ¿`Retoma` es una acción y no un tema? ¿`Se rompió` se contestó o se declaró `sin ruptura`?

**Falsificador:** un turno que cierra sin pase; un pase que resume en vez de indicar la próxima acción; un `Se rompió` vacío sin `sin ruptura`; un `No retoma` vacío; un pase que necesita al que lo escribió para entenderse.

```
Entrada: [id] | Sesgo: [posición] | Límite: [qué no alcanza] | Firma: [quién contesta]
Sostuve: [la entrada anterior, como se sostenía] | Contra: [qué la contradijo] | Sostengo: [la entrada nueva]
Se corrigió porque: [la razón que se repite sin el autor] | Techo: [qué reconstruye el otro] | Muta: [sin cambio | qué cambió]
```

**Prohibido** ejecutar el paso N+1 sin la salida del N.

## Lo que no hace

**No decide qué es verdad.** Guarda desde dónde se sostiene; la verdad la decide quien lee, contradeciendo.

**No pide una tecnología.** Una base relacional cualquiera sirve. Si el proceso nombra un motor, dejó de ser memoria y volvió a ser programación.

**No obliga a acordarse.** Un cerebro tampoco. Obliga a que lo que se recuerde diga desde dónde se recuerda.

**No impide equivocarse.** Hace que el error pueda ser visto por otro, que es lo único que impide que se vuelva absoluto.

## Prueba

¿Toda entrada declara su posición y su límite? ¿La anterior quedó suplantada y visible, no borrada? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿El techo está escrito? ¿Otra instancia reconstruye la posición leyendo solo la memoria? ¿El turno cerró con su pase, y el pase tiene `Retoma` como acción?

**Falsificador:** un hecho guardado sin posición; una entrada anterior editada en vez de suplantada; una entrada sin firmante que se lee como válida; un `Sostengo` igual a `Sostuve` presentado como corrección; una entrada que no cambia lo que el otro puede decidir; el proceso nombrando un motor o un esquema concreto; un turno que cierra sin pase.

## Transiciones

- La entrada no declara posición → no se guarda: se fricciona, y si nadie contesta, se declara el vacío.
- `Sostengo` es igual a `Sostuve` → se declara `Muta: sin cambio` y no se finge corrección.
- Otra instancia no puede reconstruir la posición → la memoria no alcanza el techo: se declara y se corrige la entrada, no la lectura.
- La relación necesita otra forma → se declara la relación nueva, con `Reemplaza:` y `Conserva:`. La base entera muta; la memoria no se parte.
- El turno termina → se entrega el pase, o la próxima instancia arranca sin saber qué hacer.
- En cualquier otro caso → se entrega la memoria leída, no la tabla de lo que se guardó.
