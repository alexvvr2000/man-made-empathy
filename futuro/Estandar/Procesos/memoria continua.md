# Memoria continua

**Unidad:** proceso.
**Aplica a:** recordar.
**Tipo:** proceso único de memoria. Se ejecuta al recordar y al leer. **No decide qué es verdad: guarda desde dónde se sostiene, y cómo se compila.**
**Nivel:** proceso de `Ouroboros/`. Baja a los tres instrumentos del piso y no los repite.
**Lector:** quien escribe la memoria, quien la va a leer sin poder preguntar, y quien va a compilarla.
**Reemplaza:** `mantis/mantenimiento/notas/notas-tesis.md` como proceso autónomo. Conserva todo lo que ese proceso hacía —la fila, la base, la vista que muta, la purga, la compilación— y lo junta con la posición: **había dos procesos de memoria y era uno solo repartido.**
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** la memoria se lee desde la posición de quien la escribió, no desde la posición de quien la lee.
**Límite:** no decide si lo recordado es verdad; mide si el otro puede reconstruir la posición y contradecirla. **No juzga el contenido de una fila:** eso lo decide quien la lee después.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra el techo declarado

**Variables:** memoria · posición · relación · sesgo · techo · vista · contabilidad
**Peor:** la memoria guarda hechos sin posición, otra instancia los hereda como verdades, y nadie puede ver de dónde vienen; **o se llena de lo que no cambia una decisión hasta que ya no se puede leer, y lo que valía se pierde entre ruido.**
**Quién:** quien va a leer la memoria mañana y no vio quién la escribió, y quien carga con que su error se lea como hecho.

**Forma:** `Entra | Falla | Sale | Consume`.
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`.

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

## La fila

**Toda entrada tiene la misma forma.** Sin forma común no hay conjunto: hay registros que no se agregan.

```
Dicho: [la frase, citada, tal como se dijo] | De: [qué pieza del sistema ilumina] | Tipo: [analogía|referencia|cita|frase|decisión|descarte] | Usa: [dónde se va a usar] | Sostenido: [prueba|frontera|nada] | Estado: [vivo|descartado|cubierto] | Vista: [la de hoy, con fecha o nombre]
```

- **`De` no es opcional:** una nota sin pieza es una idea suelta y no se puede recuperar.
- **`Tipo` no es una etiqueta de cortesía:** un `descarte` se guarda con su porqué **y no se poda**; un descarte sin rastro se vuelve a proponer.
- **`Sostenido` dice qué tan fuerte es:** `prueba` es lo que se midió, `frontera` lo que se sostiene por un límite, `nada` lo que se dice porque se dijo.

## La base

**La memoria vive en una sola base SQLite, y no se publica.** Una fuente, sin export: un `.md` publicado que se edita a mano es una segunda fuente, y dos fuentes es el trabajo que sobra.

```
.sesion-continua/mantis.db   la base única, oculta y en gitignore
notas/corrida-<uuid>/        la corrida: esquema.sql y un .csv por tabla
```

| Tabla | Qué guarda |
|---|---|
| `fila` | lo que se dijo: sección, dicho, pieza, tipo, sostenido, estado, vista, compilado |
| `sesion` | un solo bloque vivo; se sustituye en el sitio |
| `generacion` | cada compilación, con su vista y qué dejó vivo |
| `prueba` | las cuatro pruebas y su corrida |
| `seccion` | el orden en que se leen las secciones |
| `trabajo` | lo que no es la sesión ni la tesis, y se sigue entre turnos |
| `turno` | la apertura y el cierre de cada turno, con las filas antes y después |

**No se escribe con INSERT a mano: se anota con `anotar.ps1`, que valida contra el esquema.**

```
pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo decisión -Sostenido prueba
pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "(lo que mide el piso)"
pwsh -File mantis/piso/anotar.ps1 -Chequear
```

**La sesión no se escribe de memoria: se escribe con lo que el piso midió.** `-Sesion` exige el `Estado` medido, y sin él no deja escribir.

**Y `notas.ps1` mide si cada archivo cambiado tiene nota.** Compara el diff contra el último commit y Git status con los archivos nuevos no ignorados: un archivo cambiado o nuevo sin fila es una decisión sin rastro, y el veredicto es `falla` con la lista de los que faltan. **Un archivo ignorado no sale del repo y no entra en esta medida.** **Un turno que se anota al final se olvida; un turno que no pasa el piso no se entrega.**

## La vista muta

**El conocimiento muta.** Hoy hay una vista y mañana hay otra, y **la memoria tiene que poder reflejar eso sin romperse.** Por eso **cada fila declara desde qué vista se escribió.**

**Una nota no es una verdad: es una vista con fecha.** Lo que hoy se cree se anota como se cree; **si mañana cambia, la fila vieja no se edita: se agrega la nueva con su `Vista` y la vieja queda con `Estado: cubierto` o `descartado`.** Rige `integridad.md`, `El triángulo`: el sesgo se declara, no se corrige.

**La ficción y la analogía son material, no ruido.** Se usan para hacer la tesis digerible, y la nota guarda **de dónde sale la idea y hacia dónde se cruza.** Rige `../../AGENTS.md`, `La tesis`.

## Entra | Falla | Sale | Consume

- **Entra:** lo que se sostiene hoy, la posición desde la que se sostiene, y la memoria que hay.
- **Falla si:** se guarda un hecho sin su posición; se edita la entrada anterior en vez de suplantarla; la entrada no declara techo, firmante ni continuidad; la memoria se satura de lo que no cambia una decisión; se compila sin declarar desde qué vista.
- **Sale:** la memoria con la posición nueva abierta, la anterior suplantada y visible, el corte compilado con su vista, y el veredicto de si se puede leer sin el que la escribió.
- **Consume:** otra instancia que va a decidir leyendo la memoria, y quien carga con lo que se guardó.

## Cómo se aplica

1. **Leer la memoria que hay.** No se juzga por su forma: se lee lo que sostiene.
2. **Declarar la posición.** `Sesgo` de la entrada nueva, y `Límite`: qué no alcanza. Rige `../1 Guantelete — primitivo/primitivos/sesgo.md`, `Su forma`.
3. **Friccionar antes de guardar.** La entrada pasa por quien la sostiene. Se puede contestar «ninguno», «no sé» o «no puedo». **Lo único que no se puede es guardar sin contestar.** Rige `../1 Guantelete — primitivo/primitivos/friccion.md`.
4. **Abrir la continuidad.** `Sostuve` (la entrada anterior), `Contra` (qué la contradijo), `Sostengo` (la entrada nueva). Si `Sostengo` es igual a `Sostuve`, se declara `Muta: sin cambio`. Rige `../2 S.A.R.A — mutación/aprendizaje/aprender.md`, `La continuidad real`.
5. **Suplantar, no editar.** La entrada anterior no se borra: queda suplantada, con la posición nueva encima. **Lo suplantado queda visible.**
6. **Declarar el techo.** Sin techo, la entrada no entra.
7. **Verificar la lectura.** Otra instancia reconstruye qué se sostiene y de qué posición viene, leyendo solo la memoria. Si necesita preguntar, la entrada falló.
8. **Anotar en el mismo turno.** Toda interacción que produce algo —una decisión, una lectura que cambia una posición, un descarte— se guarda **en el turno en que ocurre**. Lo que queda en el contexto se pierde y lo que queda aquí se lee.

**Prohibido** ejecutar el paso N+1 sin la salida del N.

```
Entrada: [id] | Sesgo: [posición] | Límite: [qué no alcanza] | Firma: [quién contesta]
Sostuve: [la entrada anterior, como se sostenía] | Contra: [qué la contradijo] | Sostengo: [la entrada nueva]
Se corrigió porque: [la razón que se repite sin el autor] | Techo: [qué reconstruye el otro] | Muta: [sin cambio | qué cambió]
```

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

## Purga

**Lo que se creía con otra vista no es la memoria.** Lo que está en un contexto viejo **no se toma como verdad:** se lee, se anota lo que sirve en la base con su vista, y **se purga del repo.**

```
Purgado: [qué] | De: [ruta] | Por qué: [qué vista lo hacía verdad] | Se anotó en: [fila de notas|nada]
```

**Un bloque que se purga y no se anota, se pierde.** Rige la sección `La purga`.

## Compilar

**Compilar es graduar, no vaciar.** Lo que entra en la tesis **sale de la base y queda en `notas/generaciones/` como corte**; lo que no entra **se queda vivo**; **lo que se descartó se queda siempre.**

**Y compilar usa claridad:** lo que se compila se escribe con la forma de `../1 Guantelete — primitivo/herramientas/claridad.md`, y **lo que no se puede escribir con ella no se compila.** Es el filtro, no el formato.

| Al compilar | Qué pasa con la fila |
|---|---|
| entró en un archivo de la tesis | `Estado: cubierto` + `Compilado en: [archivo]` |
| no entró pero sirve | `Estado: vivo`, se queda |
| se descartó | se queda, siempre, con su porqué |

**Cada corte es una generación, y una generación no es la verdad:** es **desde qué vista se compiló**. La tesis de mañana puede compilar otra cosa de las mismas notas, **y ninguna de las dos miente.**

```
notas/generaciones/[AAAAMMDD]-[nombre]/
├── registro.md            la generación: fecha, vista, qué se compiló
└── …                      el corte, tal como quedó
```

```
Generación: [id] | Fecha: [ISO] | Vista: [la de ese día]
Compilado en: [N archivos de la tesis] | Dejó vivo: [n filas] | Descartó: [n]
Reemplaza: [generación anterior o NINGUNA]
```

**`Vista` declara desde dónde se compiló.** Sin eso, la tesis compilada se toma como definitiva y deja de ser una vista.

**Prueba:** ¿la generación tiene su registro? ¿cada fila compilada tiene `Compilado en:`? ¿lo que no entró sigue vivo en la base? ¿lo descartado sigue?

**Falsificador:** un corte sin registro; una generación borrada; la memoria vaciada sin corte; una fila compilada sin `Compilado en:`; una tesis compilada sin declarar la vista.

## Las pruebas se toman en cuenta

**Lo que se prueba no va dentro de la tesis: vive en `../../Pruebas/`, y se toma en cuenta cuando la tesis final se escriba.** Cada prueba mide una cosa distinta, y su resultado es material de la tesis:

| Prueba | Qué mide |
|---|---|
| `prueba de rendición.md` | que el otro pueda reconstruir lo producido sin el que lo produjo |
| `prueba de utilidad real.md` | que lo producido sirva en el uso, no en el papel |
| `prueba de talento utilizable.md` | que el sistema produzca algo que alguien pueda usar |
| `prueba de cruce.md` | que dos miradas se crucen sin fundirse |

**Al compilar, una prueba no se cita por su nombre: se cita su resultado.** Una prueba sin corrida se declara `[NO CORRIDA]`, y no se escribe como si hubiera pasado.

## Las dos referencias

**No se copian: se citan.**

- **claridad** — `../1 Guantelete — primitivo/herramientas/claridad.md`. **Cada fila se lee igual en cualquier IA:** sin ambigüedad, sin glosario.
- **sesgo declarado** — `../1 Guantelete — primitivo/extensiones/sesgo-declarado.md`. **Cada fila declara su `Vista`:** lo que hoy se cree no se presenta como lo que siempre fue.

**Y lo que vale solo para esta sesión no va aquí: se declara en la sesión de la base, no como nota de tesis.**

## Lo que no hace

**No decide qué es verdad.** Guarda desde dónde se sostiene; la verdad la decide quien lee, contradeciendo.

**No pide una tecnología.** Una base relacional cualquiera sirve. Si el proceso nombra un motor, dejó de ser memoria y volvió a ser programación.

**No obliga a acordarse.** Un cerebro tampoco. Obliga a que lo que se recuerde diga desde dónde se recuerda.

**No impide equivocarse.** Hace que el error pueda ser visto por otro, que es lo único que impide que se vuelva absoluto.

**No juzga el contenido de una fila.** Si lo anotado es válido lo decide quien lo usa; la unidad mide la forma y la contabilidad.

## Prueba

¿Toda entrada declara su posición y su límite? ¿La anterior quedó suplantada y visible, no borrada? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿El techo está escrito? ¿Otra instancia reconstruye la posición leyendo solo la memoria? ¿Cada frase que vale tiene su fila? ¿Cada fila nombra su pieza y declara su vista? ¿El turno cerró con su pase, y el pase tiene `Retoma` como acción? ¿Lo compilado declara desde qué vista se compiló?

**Falsificador:** un hecho guardado sin posición; una entrada anterior editada en vez de suplantada; una entrada sin firmante que se lee como válida; un `Sostengo` igual a `Sostuve` presentado como corrección; una entrada que no cambia lo que el otro puede decidir; el proceso nombrando un motor o un esquema concreto; un turno que cierra sin pase; una nota sin pieza; una analogía que se vuelve prueba; una vista nueva que borra la vieja en vez de declararla; un corte sin registro; una generación borrada; la memoria vaciada sin corte; una prueba citada sin corrida.

## Transiciones

- La entrada no declara posición → no se guarda: se fricciona, y si nadie contesta, se declara el vacío.
- `Sostengo` es igual a `Sostuve` → se declara `Muta: sin cambio` y no se finge corrección.
- Otra instancia no puede reconstruir la posición → la memoria no alcanza el techo: se declara y se corrige la entrada, no la lectura.
- La relación necesita otra forma → se declara la relación nueva, con `Reemplaza:` y `Conserva:`. La base entera muta; la memoria no se parte.
- El turno termina → se entrega el pase, o la próxima instancia arranca sin saber qué hacer.
- Un bloque viejo sirve para la tesis → se anota en la base con su vista, y se purga.
- La vista cambió → fila nueva; la vieja no se edita.
- Se compila la tesis → el corte va a `notas/generaciones/` con su vista.
- En cualquier otro caso → se entrega la memoria leída, no la tabla de lo que se guardó.
