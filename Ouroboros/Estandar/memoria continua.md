# Memoria continua — el estándar

## Qué forma fija

**Que una memoria se lea sin el que la escribió.** Eso es todo: el resto son consecuencias.

**Una base de datos no hereda verdades si guarda posiciones.** si las posiciones están. **El soporte no es el estándar: la forma lo es.**

## Qué es la memoria

**Un cerebro no guarda hechos: guarda su versión de lo que pasó.** Y el acto de recordar vuelve a sesgar. **Guardar no es un depósito: es una posición.**

**La memoria que no declara desde dónde se sostiene no es memoria: es obediencia con forma de registro.**

**Un gramo de absoluto basta.** Un gramo es un hecho guardado sin su posición, y con él el sistema ya no requiere volver a mirar.

## La posición, y las seis partes

**Toda entrada tiene las mismas seis partes.** Sin forma común no hay conjunto: hay registros que no se agregan.

| Parte | Qué declara | Sin ella |
|---|---|---|
| **Sesgo** | desde dónde se sostiene | se lee como si no tuviera sitio |
| **Límite** | qué no alcanza | el sesgo se aplica a todo y se vuelve absoluto |
| **Firma** | quién puede contestarla | se firma a sí misma: hay una firma, no una prueba |
| **Contra** | qué la contradijo | una corrección sin contra es una preferencia que se mantuvo |
| **Sostengo** | la posición nueva | no se distingue del hecho heredado |
| **Techo** | qué reconstruye el otro | sin techo no se sabe si la entrada alcanzó |

**`Contra` no puede firmarlo el que se corrigió.** Si lo firma el mismo, no hubo corrección: hubo persistencia.

**Y `Contra` no es un campo de auditoría: es la mitad que forma el criterio.** Rige `./criterio.md`, `El criterio autónomo`: **somos un historial de sesgos, y el criterio es ese historial leído antes de decidir.** **Una memoria sin `Contra` no guarda criterio: guarda un catálogo de conclusiones.**

**Sin `Sesgo` no hay historial tampoco:** **una entrada sin sesgo se lee como si no tuviera sitio, y un historial sin sitios es una lista de respuestas.**

## El techo, que es la única condición de entrada

```
Techo: otra instancia reconstruye la posición, y puede ver de dónde viene, leyendo la memoria y sin preguntar.
```

**Lo que no cambia lo que el otro puede decidir, no entra.** No hay una lista de campos obligatorios: hay un techo, y el que escribe lo cumple.

**Sin techo declarado no se escribe.**

## La continuidad

**Medir otra vez no basta: hay que decir qué se sostenía antes y qué se sostiene ahora.**

**Un sistema puede medir cien veces y conservar la misma posición; eso no es continuidad, es la misma decisión contada más veces.**

**Si `Sostengo` es igual a `Sostuve`, se declara `sin cambio` y no se finge aprendizaje.**

## Suplantar, no editar

**La entrada anterior no se borra: queda suplantada, con la posición nueva encima. Lo suplantado queda visible.**

**Una memoria que edita no tiene historia. Una que suplanta tiene dos fechas y una sola posición vigente.**

**Y lo que se descarta no se poda.** Un descarte sin rastro se vuelve a proponer.

## La vista muta

**Una nota no es una verdad: es una vista con fecha.**

**Si mañana cambia, la fila vieja no se edita: se agrega la nueva con su vista, y la vieja queda con `Estado: cubierto` o `descartado`.**

**El tiempo no cura el absoluto: otra mirada sí.** **Una idea no envejece: cambia el que la mira.** Por eso lo que vence no es la idea, es el sesgo que la hacía verdadera — y lo que lo vence es **otra mirada**, no el calendario.

## Qué guarda, y qué no

| Guarda | No guarda |
|---|---|
| la posición, con el hecho adentro | hechos sueltos |
| lo que cambia lo que el otro puede decidir | lo que no cambia nada |
| lo descartado, con su porqué | nada que se pueda volver a proponer |
| la cadena: qué se sostuvo, contra qué, qué se sostiene | un estado sin historia |

## El disparo: cada interacción deja su entrada

**La memoria no se escribe al final del turno: se escribe en cada interacción.** **Un turno que solo deja una entrada al cerrar guarda el resumen de lo que pasó, y un resumen no es una posición.**

**El disparo es la interacción, no el cierre.** Cada vez que hay un mensaje del que tiene autoridad y una respuesta, **se evalúa una fila. Si cambió una decisión, se escribe. Si no, se declara `sin cambio` y no se finge memoria.**

**Y qué vuelve la interacción escribible es la fricción.** Rige `./criterio.md`: **el criterio se dispara al entrar en fricción.** **La interacción es el momento de anotar; la fricción es la condición de que haya algo que anotar.**

| Una interacción dispara… | Cuando… | Qué deja |
|---|---|---|
| **una entrada** | hubo fricción, y cambió lo que se sostiene | las seis partes y el techo |
| **un `sin cambio`** | hubo fricción, y no movió ninguna posición | una fila que dice que se miró y no se movió |
| **una fila de `ruta`** | la interacción se enrutó a un proceso, o a un vacío | qué fila se cargó y quién decidió |
| **un descarte** | algo se propuso y no entra | el porqué, **y no se poda** |

**Y sin fricción también se anota, pero como pasada:** **una interacción sin fricción no es una decisión: se declara `pasada` y no se finge que hubo posición nueva.**

**Regla:** **si una interacción terminó y no hay ni entrada, ni `sin cambio`, ni `pasada`, no pasó.** **Lo que no se anota no existió, y lo que existió y no se anotó no se puede contestar.**

**Y el orden no es negociable:** **se anota la interacción antes de responder a la siguiente.** **Anotar al final es anotar de memoria, y la memoria de quien anotó es la menos confiable que hay.**

**Lo que no se cuenta es la interacción como mérito.** Rige `../../2 S.A.R.A — mutación/evaluacion/friccion-en-agente.md`: **se cuenta cuántas decisiones cambiaron, no cuántas veces se preguntó.**

**Ancla:** el disparo es la interacción; la fricción es la condición; el pase es el turno.

## El pase de turno

**Una instancia que termina sin dejar el pase no murió: se perdió.**

**El pase no es un resumen del trabajo: es el estado con el que la próxima instancia puede empezar sin el que la anterior exista.**

```
Sostuvo: [lo que quedó vigente]
Se rompió: [qué falló, y qué lo detectó — o «sin ruptura»]
Abierto: [qué quedó sin cerrar, y por qué]
Retoma: [la primera acción concreta de la próxima instancia]
No retoma: [lo que quedó fuera a propósito, y por qué]
```

**`Retoma` es una acción, no un tema.** «Revisar el piso» no sirve; «correr X y leer el veredicto de Y» sirve.

**`No retoma` es tan obligatorio como `Retoma`:** un turno sin nada descartado está ocultando algo.

## Purga y compilación

**Lo que se creía con otra vista no es la memoria.** Lo que está en un contexto viejo no se toma como verdad: **se lee, se anota lo que sirve con su vista, y se purga.** Un bloque que se purga y no se anota, se pierde.

**Compilar es graduar, no vaciar.** Lo que entra en la tesis sale de la memoria y queda como corte con su vista; **lo que no entra se queda vivo; lo que se descartó se queda siempre.**

**El corte no es la verdad: es desde qué vista se compiló.** La tesis de mañana puede compilar otra cosa de la misma memoria, y ninguna de las dos miente.

## La forma de la memoria

**La forma de la memoria no es fija: muta con el criterio.** **No hay una carpeta que sea la de la memoria para siempre.** **El criterio decide dónde vive, y lo declara.**

| La forma la declara | Qué fija |
|---|---|
| **el criterio** | dónde vive la memoria, con qué motor y en qué archivo |
| **el ente que la usa** | lo declara en un solo lugar, junto a su carta |
| **este estándar** | no la fija: **exige que esté declarada, y que se lea sin el que la escribió** |

**Y hay una sola memoria por ente.** Dos memorias que guardan lo mismo se desincronizan, **y la que se lee deja de ser la que se sostiene.**

**Cuando el criterio cambia, cambia la forma, y no se mantienen dos.** **Una memoria vieja no se respalda como memoria: se lee, se anota lo que sirve con su vista, y se purga.**

**Lo que no muta con la forma es la forma de la entrada:** las seis partes y el techo. **Cambia el soporte; no cambia qué hay que declarar para que otro reconstruya la posición.**

**El esquema vive donde vive la memoria.** **Un esquema separado de su base es una base sin forma, y una forma sin base es un folleto.**

## Lo que este estándar no hace

**No decide qué es verdad.** Guarda desde dónde se sostiene; la verdad la decide quien lee, contradeciendo.

**No obliga a acordarse.** Obliga a que lo que se recuerde diga desde dónde se recuerda.

**No impide equivocarse.** Hace que el error pueda ser visto por otro, que es lo único que impide que se vuelva absoluto.

## Prueba

¿Toda entrada declara sus seis partes? ¿La anterior quedó suplantada y visible? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿El techo está escrito? ¿Otra instancia reconstruye la posición leyendo solo la memoria? ¿`Contra` viene de fuera del que se corrigió? ¿Cada entrada dice qué fricción la disparó, y las pasadas no se cuentan como decisión?

**Falsificador:** una entrada sin sesgo; una que se firma a sí misma; una anterior editada en vez de suplantada; un `Sostengo` igual a `Sostuve` presentado como corrección; una entrada sin techo; un `Contra` firmado por el que se corrigió; lo descartado podado; **una entrada sin fricción declarada; una `pasada` contada como decisión; se cuenta la interacción y no el cambio.**
