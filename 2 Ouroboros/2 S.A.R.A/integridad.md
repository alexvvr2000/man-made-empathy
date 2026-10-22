# Integridad

**Reemplaza:** `Proceso de integridad de procesos`/ Sube a estándar y cambia de oficio: **no solo chequea, reescribe/** Chequear la forma y verbalizar el contenido son el mismo acto/

**Unidad:** proceso/
**Aplica a:** chequear y verbalizar/
**Tipo:** estándar de nivel 0/ **Chequea y reescribe:** mira lo que otros produjeron, encuentra lo que falta, **y lo verbaliza/** Se aplica a sí mismo/
**Lector:** el ejecutor que va a mutar una tarea/ **El trabajo de verbalizar lo hace el ejecutor, no la autoridad/**
**Nivel:** 0/ General: no pertenece a ninguna tarea, y **llega hasta el contenido de los procesos/**
**Alcance:** cualquier tarea —sus folders, sus sub-tareas, sus procesos y **el texto de cada proceso**— y este archivo/
**Dueño:** la autoridad/
**Estado:** vigente/

**Variables:** tarea · folder · hermanos · enunciado · salida · implícito · contenido · nombre
**Peor:** el chequeo pasa por alto lo que falta **porque nadie lo verbalizó**, y el proceso entra con buena forma y contenido mudo/ La forma está correcta y el archivo no dice nada/
**Quién:** el ejecutor que muta/ Si no verbaliza, el trabajo queda a medias y la autoridad lo tiene que hacer a mano/

**Forma:** `Entra | Falla | Sale | Consume`/
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`/

**Manipulación/** Todo cambio a un proceso pasa por la manipulación de su tarea: ahí se nombran las variables antes de que el proceso exista/ Un proceso que se modifica sin pasar por ahí queda sin variables, y sin variables no hay contra qué chequearlo/

## El fantasma

**Un fantasma es una tarea sin deterrente ni derrotero.** No puede existir uno sin otro: **el derrotero sin deterrente enruta hacia nada, y el deterrente sin derrotero pierde qué se pierde cuando se vaya.** Si falta uno de los dos, **es fantasma**, y se advierte.

**Los tres archivos, y solo dos son obligatorios:**

| Archivo | Qué da | Obligatorio |
|---|---|---|
| `deterrente.md` | qué se pierde si la tarea deja de servir | **sí** |
| `Derrotero.md` | qué se carga y cuándo | **sí** |
| la carta | qué hay, qué no se toca y cómo se verifica | **no** |

**La carta no tiene nombre de archivo fijo.** Es la pieza que dice qué hay, qué no se toca y cómo se verifica; hoy se llama `AGENTS.md`. Si en otra era se llama de otra forma, sigue siendo la carta. Rige `../../1 Tesis/Derrotero y Carta.md`, `La carta y el derrotero son dos piezas`.

**Con los dos obligatorios, la integridad se saca triangulando:** deterrente + derrotero + lo que hay. **La carta ayuda a leer; si no está, no impide.** Esa es la **verdad del momento**, y vale más que una forma repetible: aquí se mide lo que trabaja hoy, no lo que se puede citar mañana.

### Las tres intuiciones

**Sin los dos archivos no hay a quién preguntar.** Se arma una tarea desde 0 **sin idea de dónde vino**, como un cuerpo sin pasado: **cada uno se imagina lo que era, y la idea que sale no es la verdad al 100%.** Por eso sirve: **algo puede ser útil desde el segundo 0 para lo que se quiere, o se descarta de plano.**

**Lo que se entrega son tres intuiciones de lo que la tarea era**, cada una con lo que la sostiene y lo que la refutaría:

```
Fantasma: [tarea] | Falta: [deterrente|derrotero|los dos] | Se buscó en: [rutas]
Idea 1: [qué se cree que era] | Sostiene: [qué del contenido la respalda] | Refuta: [qué la tumba]
Idea 2: [qué se cree que era] | Sostiene: [...] | Refuta: [...]
Idea 3: [qué se cree que era] | Sostiene: [...] | Refuta: [...]
Decide: [la autoridad: cuál entra, cuál se descarta]
```

**Las tres no se ordenan por probabilidad y ninguna se elige por parecer mejor.** Se entregan para que la autoridad decida, y la que se descarte **se queda con su porqué**, porque un descarte sin rastro se vuelve a proponer.

**Prueba:** ¿se advirtió el fantasma? ¿Las tres ideas salen del contenido y no de la nada? ¿Cada una declara lo que la refuta? ¿Se dice qué se descartó y por qué?
**Falsificador:** una tarea sin deterrente que se corre igual; un fantasma que se presenta como tarea viva; una intuición inventada sin contenido detrás; la carta exigida cuando no está; una sola idea presentada como la verdad de lo que la tarea era.

## Deterrente

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| no se corre antes de mutar | el cambio entra sin contra qué compararlo | el error aparece en la tercera mutación, cuando ya no se sabe cuál lo trajo |
| **solo se chequea la forma** | **el contenido queda mudo** | el archivo cumple el formato y no dice nada |
| **no se reescribe lo que falta** | el trabajo vuelve a la autoridad | la autoridad verbaliza a mano lo que el ejecutor debía hacer |
| se corre una sola pasada | se pierde la mitad que la otra ve | la contradicción que nunca se ejecutó sobrevive |
| el chequeo lo firma quien mutó | no hay chequeo: hay una firma | nadie puede decir que el par estaba mal |
| no encuentra nada nunca | deja de servir y se vuelve ceremonia | se corre por cumplir y no detecta nada |
| se borra porque molestó | se pierde el único lugar donde el error se ve | el sistema se corrige solo contra sí mismo |

**Sin este chequeo, una tarea muta a ciegas** — y una tarea que muta a ciegas repite el mismo error en la tercera generación sin saber de dónde vino/

## Tesis

Los procesos hermanos no se ven entre sí/ Cada uno cumple su regla, y **dos reglas que se cumplen por separado pueden ser incompatibles juntas/**

Y cada proceso, solo, puede servir sin que esté escrito **qué tiene que cumplirse para que sirva/**

**Y el texto de cada proceso puede cumplir el formato sin decir nada/** Las tres cosas se chequean aquí/

**Este archivo no deja el hallazgo para que otro lo arregle:** encuentra el implícito **y lo escribe/** Un chequeo que declara y no verbaliza deja el trabajo donde estaba/

## Integridad es que no tenga agujeros

**Integridad no es estar ordenado/ No es cumplir el formato/ No es que cada archivo esté completo/**

> **Integridad es que el sistema no tenga agujeros/**

Y un agujero no se ve mirando la pieza: **se ve cuando la medición trae algo que no se tenía en cuenta/** Ahí aparece que faltaba algo — o que sobraba algo ocupando el lugar del agujero/

**Por eso este proceso no arregla el sistema que hay: lo reemplaza por el que no tiene agujeros/** Si después de la corrida el sistema sigue igual, no hubo integridad: hubo orden/

### El agujero tiene nombre

**No se declara la ausencia: se declara el proceso que falta/**

| Si se declara como descripción | Si se declara como proceso |
|---|---|
| *"falta medir el peor caso"* | `peor-caso/md`, con sus variables y su falsificador |
| nadie sabe qué hacer con eso | **se escribe y el sistema queda completo** |
| vuelve a la autoridad a interpretar | **el ejecutor lo cierra en la corrida** |

Una descripción de ausencia no se puede usar/ **Un proceso, sí/**

### La regla que decide si agregar o rehacer

> **Un proceso: se agrega y se cierra/ Un folder: se rehace el sistema/**

Se puede saber **antes** de escribir: **si el proceso que falta se puede nombrar y definir en una línea, el sistema está a uno/** Si no se puede nombrar, **no falta un proceso: falta un nivel** — y ahí no se agrega, se rehace/

**Por eso no se agrega por agregar:** un agujero no se tapa sumando piezas/ Se tapa cuando desaparece/ A veces eso es agregar tres procesos; a veces es **retirar dos que hacían ruido en el lugar del agujero/**

> **La medición trae algo que no se tenía en cuenta, y se termina con lo que de verdad se ocupa — no con lo que se tenía/**

### La prueba de que quedó íntegro

**¿El sistema que queda puede hacer lo que el anterior hacía —sin que nada sobre?**

- **Sobra algo** → había un agujero tapado con ruido/
- **Falta algo** → el agujero sigue/
- **Ni sobra ni falta** → **íntegro/**

Y el chiste de rehacer desde cero: **lo que sale tiene que ser equivalente en fin y distinto en forma/** Si sale peor, no se entendió qué hacía/ Si sale igual, no se rehízo/

### La medición a un proceso

> **Cuando el que falta se puede escribir en una línea, y ninguna pieza sobra, la medición está a un proceso de ser perfecta/**

Ese proceso se escribe en la corrida/ **No se deja para después/**

## Lo que este proceso hace, y lo que no

| Hace | No hace |
|---|---|
| chequea forma y contenido | no inventa procesos que no existen |
| **encuentra el implícito y lo escribe** | no decide si el proceso sirve |
| **reasigna lo que está en el folder equivocado** | no cambia el fin que el proceso persigue |
| **acuña el nombre nuevo** | no sustituye a la autoridad cuando hay que elegir entre dos caminos |
| deja el archivo entero, no la lista de cambios | no reescribe lo que ya dice lo que tiene que decir |

## Lo que impide crecer por crecer

> Un proceso está completo cuando **todo lo que tiene que cumplirse para que sirva está escrito dentro/**
> Una sub-tarea está completa cuando **sus procesos no dependen de un implícito que viva en otra/**
> Un folder está completo cuando **sus sub-tareas cubren un fin que no se solapa con otro folder/**

**La regla que sigue:** no se agrega una pieza porque falte algo/ Se agrega cuando la pieza nueva **cierra un implícito** y la anterior no podía cerrarlo/

## Entra | Falla | Sale | Consume

**Entra:** una tarea completa —folders, sub-tareas, procesos y sus textos—, o una parte de ella/
**Falla:** dos hermanos se contradicen y nadie lo ve; un proceso pertenece a otra sub-tarea; un proceso no lo carga nadie; un proceso sirve solo bajo una condición que no está escrita; **un proceso cumple la forma y su texto no dice qué decide**; el chequeo se hace después de mutar; **el hallazgo se declara y no se verbaliza/**
**Sale:** **la tarea íntegra** —sin agujeros, con los implícitos cerrados, las piezas reasignadas y los nombres acuñados— donde **ni sobra ni falta** nada/
**Consume:** quien va a usar la tarea/ **Recibe archivos, no un informe/** Si hay algo que no se pudo cerrar, se declara con su `Vacío:`/

## Cuándo se usa

**Antes** de mutar, **después** de una serie, y **cuando la tarea ya no se entiende/** Nunca durante: un chequeo a medias no encuentra lo que busca/

## Proceso

### 1/ Recorrer por nivel

**Los hermanos son los que cuelgan del mismo padre/** El recorrido baja en orden, y no se salta un nivel:

```
Tarea: [cuál] | Folders: [n] | Sub-tareas: [n] | Procesos: [n]
```

1/ **La tarea/** ¿Tiene `deterrente.md` y `Derrotero.md`? **Los dos o ninguno: sin uno de los dos es fantasma, y se corta aquí.** ¿Tiene carta? Si está, se lee; si no, no impide.
2/ **Los folders/** ¿Cada uno cubre un fin distinto? ¿Hay dos que se solapan?
3/ **Las sub-tareas/** ¿Cada una declara deterrente, fallo, piso y sus procesos?
4/ **Los procesos/** ¿Forma completa? ¿Variables? ¿`Falsificador`?
5/ **El texto de cada proceso/** **¿Dice qué decide, o solo cumple el formato?**

### 2/ La doble barrida

| Pasada | Qué mira | Qué encuentra | Qué no ve |
|---|---|---|---|
| **1/ De la forma** | qué campos tiene | lo que falta según el formato | lo que está escrito y no dice nada |
| **2/ Del contenido** | qué dice el texto | el proceso mudo, el implícito, el nombre que no nombra | el campo ausente |

**Pasada 1 — el formato:** ¿tiene todo?
**Pasada 2 — el contenido:** ¿lo que tiene dice algo?

**Si las dos pasadas coinciden, se cierra/ Si discrepan, la discrepancia es el hallazgo** — y el caso más común es **forma completa, contenido mudo/**

### 3/ Las seis preguntas

| # | Pregunta | Qué detecta | Señal de falla |
|---|---|---|---|
| **1** | ¿Un mismo acto puede cumplir los dos? | contradicción de regla | el acto que cumple a uno incumple al otro |
| **2** | ¿Esta pieza pertenece a otro padre? | disfrazada | su entrada es la salida de otro y no lo declara |
| **3** | ¿Alguien carga esta pieza? | huérfano | ninguna `Transición`, `README` ni deterrente la trae |
| **4** | ¿Qué tiene que cumplirse para que esto sirva, y no está escrito? | **el implícito** | lo tomado sin lo que lleva |
| **5** | ¿El texto dice qué decide, o solo ocupa el lugar? | **el proceso mudo** | cumple el formato y no se puede aplicar |
| **6** | ¿Qué falta, y se puede escribir en una línea? | **el agujero y su nombre** | falta y se declara como descripción, no como proceso |

**La 5 es la que la forma no ve/** Un proceso puede tener `Entra`, `Falla`, `Sale`, `Consume`, `Prueba` y `Falsificador` — y ninguno decir nada que se pueda ejecutar/

### 4/ El implícito — se escribe, no se declara

> **¿Qué condición tiene que cumplirse para que este proceso sirva, y no está escrita adentro?**

**El hallazgo es el implícito/ Y el trabajo no termina al encontrarlo: se escribe/**

```
Implícito: [la condición] | Dónde falta: [sección] | Qué pasa sin ella: [el fallo]
Acción: [se escribió en qué sección | no se pudo: por qué]
```

**Prohibido cerrar un implícito con la palabra «pendiente»/** O se escribe, o se declara `Vacío:` con lo que falta para poder escribirlo/

**Cuándo se descarta:** si el implícito no se puede señalar en un archivo, no es un implícito: es una tesis/

### 5/ La verbalización — el proceso mudo

**Un proceso mudo cumple el formato y no dice qué decide/** Se detecta por tres señales:

| Señal | Qué delata |
|---|---|
| el `Sale` no se puede usar sin preguntar | no dice qué emite |
| el `Falla` es una intención («falla si está mal») | no nombra el caso |
| el `Falsificador` repite la `Prueba` | no refuta: confirma |

**Qué se hace:** se reescribe el campo con lo que el proceso hace de verdad/ **Si no se puede, no era un proceso: era un lugar/**

```
Mudo: [campo] | Qué decía | Qué se escribió
```

### 6/ La reasignación — cuando ya no se sabe dónde va

**Si una pieza está en el padre equivocado, se mueve/** No se deja «porque ya está»: **la ubicación es parte de lo que la pieza significa/**

```
Pieza: [cuál] | Estaba en: [padre] | Pertenece a: [padre] | Por qué
```

**Y si ninguna ubicación sirve, la pieza es un folder nuevo** — y se declara el fin que cubre/

### 7/ La mutación desde cero

**A veces no sirve arreglar: hay que rehacer/** Se hace desde cero cuando **el chequeo encuentra que la pieza no se puede explicar sin cambiar su padre/**

| Se rehace desde cero | Se corrige |
|---|---|
| la pieza no cabe donde está | falta un campo |
| su nombre no nombra lo que hace | el texto está mudo |
| su fin se solapa con otro | un implícito vive fuera |

**El chiste de rehacer desde cero no es borrar: es saber que lo que quedó es correcto aunque no se parezca a lo anterior/** Lo que se conserva se declara; lo que se pierde, también/

```
Desde cero: [pieza] | Conserva: [qué] | No conserva: [qué] | Por qué se rehace
```

**También se rehace una sub-tarea entera.** Cuando el chequeo encuentra que **la tarea no tiene sus dos archivos** —deterrente y derrotero—, o que sus sub-tareas no trabajan juntas, **no se llenan huecos: se reacomoda el nivel desde 0** en procesos y carpetas que trabajan, **porque tienen los dos archivos.** Sin ellos se advierte `El fantasma` y se entregan tres intuiciones; no se rehace sobre nada.

```
Nivel rearmado: [tarea] | Traía: [n sub-tareas, n procesos] | Queda: [n sub-tareas, n procesos]
Conserva: [qué servía] | No conserva: [qué se retira y por qué] | Archivos: [deterrente sí/no | derrotero sí/no | carta sí/no]
```

### 8/ El chequeo sobre sí mismo

**Este archivo se pasa por las seis preguntas, y su resultado se declara en la corrida/**

| Frente a | La pregunta | La respuesta |
|---|---|---|
| la manipulación de cualquier tarea | ¿un acto puede cumplir los dos? | sí: manipular puede terminar llamando a integridad/ **No se contradicen: se encadenan** |
| la fricción de cualquier tarea | ¿pertenece a otra sub-tarea? | no: es de la tarea, no de una sub-tarea |
| el derrotero o deterrente de la tarea | ¿alguien lo carga? | sí: tiene su fila |
| sí mismo | ¿qué condición le falta? | **las seis preguntas se aplican a todo proceso de toda tarea; si alguna no aplica a uno, se declara cuál y por qué** |
| sí mismo | ¿el texto dice qué decide? | **se cumple si esta columna se puede leer sin interpretar** |
| sí mismo | ¿qué falta, y se puede escribir en una línea? | **la sección «Integridad es que no tenga agujeros» nombra el agujero como proceso** |

**Si el chequeo sobre sí mismo encuentra algo, es hallazgo como cualquier otro/** No hay excepción para el que chequea/

### 9/ Declarar y entregar

```
Padre: [cuál] | Par: [a] × [b] | Acto común: [sí|no] | Contradice: [cuál|ninguna]
Pertenece a: [a→b|b→a|ninguno] | Carga: [quién|nadie]
Implícito: [la condición] | Falta en: [sección] | Se escribió: [dónde|Vacío: qué falta]
Mudo: [campo] | Qué se escribió
Reasignado: [pieza → padre]
Desde cero: [pieza] | Conserva | No conserva
Pasada 1: [forma] | Pasada 2: [contenido] | Coinciden: [sí|no]
Sobre sí mismo: [qué encontró|nada]
```

**Se entrega la tarea reescrita, no la tabla/** La tabla es el registro de lo que se hizo; el entregable es el archivo/

### 10/ Acuñar el nombre

**Todo muta: tarea, folder, sub-tarea, proceso y nombre/** Una corrida no termina en veredicto: **termina en un nombre nuevo/**

**La forma se cita, no se redefine:** rige `//////1 Tesis/formato/md`, `La acuñación`/ Aquí solo se declara **cuándo**: al cerrar la corrida, con el hallazgo adentro/

> **Un nombre que sirve para dos corridas distintas no nombra nada/**

**Sin hallazgo no hay acuñación fingida:** una corrida que no encontró nada acuña igual, con `Muta: sin cambio`/

## Lo que el chequeo no hace

**No decide entre dos caminos/** Si dos opciones son válidas, eso es de la autoridad/

**No inventa procesos que no existen/** Un implícito se cierra escribiendo una condición; un proceso faltante se declara, no se finge/

**No juzga si el proceso sirve/** Eso lo dice el uso o `///Primitivo Ejecutor/Pruebas/prueba de utilidad real/md`/

## Ancla

```
Chequeo: [id] | Tarea: [cuál] | Folders: [n] | Sub-tareas: [n] | Procesos: [n] | Versión: [fecha]
Archivos: [deterrente sí/no | derrotero sí/no | carta sí/no] | Fantasma: [sí|no]
Hallazgos: [n] | Contradicciones: [n] | Disfrazadas: [n] | Huérfanos: [n] | Implícitos: [n] | Mudos: [n]
Reasignados: [n] | Desde cero: [n] | Nivel rearmado: [n]
Sobre sí mismo: [qué encontró|nada]
```

## Prueba

¿Se recorrieron los cinco niveles? ¿Corrieron las dos pasadas? ¿Cada implícito **se escribió** o se declaró vacío? ¿Cada proceso mudo se reescribió? ¿La pieza que no cabía se movió o se rehízo? ¿El chequeo se aplicó a sí mismo y lo declaró?

**Falsificador:** un agujero declarado como descripción en vez de como proceso; una corrida que termina con más piezas de las que empezó sin que ningún agujero lo exigiera; un sistema que queda igual después de la corrida; se chequea solo la forma y el contenido queda mudo; un implícito declarado como «pendiente»; un proceso mudo corregido de nombre y no de texto; una pieza que no cabe y se deja donde está; se entrega la tabla en vez de la tarea reescrita; un chequeo que nunca se encuentra nada a sí mismo; se borra el chequeo porque encontró algo incómodo/

## Modos de falla

- **Chequeo de forma/** Se mira el formato y no el texto/
- **Hallazgo sin cierre/** Se declara el implícito y se deja «pendiente»/
- **Informe en vez de archivo/** Se entrega la tabla y no la tarea reescrita/
- **Barrida única/** Se corre la pasada de la forma y se olvida el contenido/
- **Contradicción declarada como opinión/** Se nombra el par, pero no el acto/
- **Huérfano que se calla/**
- **Disfrazada que se anida sin declararlo/**
- **Chequeo complaciente/** Corre, no encuentra nada, y nunca encuentra nada/
- **Implícito inventado/** Una tesis disfrazada de condición/
- **Padre imaginario/** Se busca el proceso de arriba en vez de la condición olvidada/
- **Autochequeo de adorno/** Se declara «sobre sí mismo: nada» sin haber corrido las preguntas/

## Transiciones

- La contradicción está en un estándar → `///mantis/mantenimiento/editar/md`, gana el estándar/
- El par no se entiende → `//primitivos/claridad/md`, `1/4`/
- Hace falta saber si una creación se sostiene → `//primitivos/manipulacion/md`, `No-objetivo`/
- Falta el sesgo de la comparación → `//mutaciones/sesgo-declarado/md`/
- Hay que rehacer una pieza desde cero → la mutación de su tarea, `Mutar la serie`/
- En cualquier otro caso → se entrega la tarea reescrita y se cierra/
