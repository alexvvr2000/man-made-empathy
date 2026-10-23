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

## Lo que este estándar no hace

**No nombra un motor ni un formato de archivo.** Una base relacional sirve; un archivo con columnas sirve; **lo que no sirve es una memoria que no declara desde dónde se sostiene.**

**No decide qué es verdad.** Guarda desde dónde se sostiene; la verdad la decide quien lee, contradeciendo.

**No obliga a acordarse.** Obliga a que lo que se recuerde diga desde dónde se recuerda.

**No impide equivocarse.** Hace que el error pueda ser visto por otro, que es lo único que impide que se vuelva absoluto.

## Prueba

¿Toda entrada declara sus seis partes? ¿La anterior quedó suplantada y visible? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿El techo está escrito? ¿Otra instancia reconstruye la posición leyendo solo la memoria? ¿`Contra` viene de fuera del que se corrigió?

**Falsificador:** una entrada sin sesgo; una que se firma a sí misma; una anterior editada en vez de suplantada; un `Sostengo` igual a `Sostuve` presentado como corrección; una entrada sin techo; un `Contra` firmado por el que se corrigió; lo descartado podado.
