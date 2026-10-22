# Proceso de mutación

**Unidad:** proceso. Lo que se transforma es el proceso, no la tarea.
**Aplica a:** mutar.
**Tipo:** proceso. Se ejecuta; no se interpreta.
**Nivel:** primitivo. Uno de los primitivos del guantelete.
**Alcance:** toda transformación de un proceso desde un estado inicial.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** pieza · nombre · lugar · fin · reemplazo
**Peor:** el cambio se llama mutación y conserva el nombre anterior: el lector cree que lee lo de antes y lee otra cosa
**Quién:** quien va a usar la pieza, y quien la va a mutar después


**Primitivo.** Vuelve sobre cualquiera de los otros primitivos: los puede rehacer, retirar o reemplazar. Es la arista de retorno del lenguaje.
**Trazabilidad.** Es el proceso que registra todo cambio de los otros cinco: origen, cambio declarado y responsable. Sin él, un proceso cambia y nadie puede reconstruir por qué.
**Forma.** `Entra | Falla | Sale | Consume`. Rige `./manipulacion.md`, `Pregunta de entrada`.
**Manipulación.** Todo cambio a un proceso pasa por `./manipulacion.md`: ahí se nombran las variables antes de que el proceso exista. Un proceso que se modifica sin pasar por ahí queda sin variables, y sin variables no hay contra qué chequearlo.

## Tesis

Mutar es cambiar un proceso desde un estado inicial sin borrar el origen ni al responsable. La forma se arma y se desarma; volver es otra mutación. Sin mutación no hay proceso nuevo, solo proceso congelado. Rige `./manipulacion.md`, `Lo que funciona ya está viejo`.

Lo que cambia siempre no es el resultado del proceso: es **el conjunto de procesos que lo produce**. Golpear mutó: hoy neutralizar es más pesado y a veces no usa manos. Cambió el proceso, no el fin.

## Mutar la serie

Un proceso no muta solo. El conjunto que lo contiene también muta: se quitan unos, se ponen otros, y el conjunto sigue siendo válido sin heredar nada de la versión anterior.

**Si tuviera un límite, la mutación ya se hubiera curado el cáncer hace mucho.**

**Enunciado:** el conjunto de procesos de un nivel se reemplaza entero o por partes, sin heredar de la versión anterior. Un proceso nuevo no tiene que parecerse al que reemplaza; tiene que cubrir el mismo fin.

**Sin herencia.** El reemplazo no hereda forma, nombre ni estructura del anterior. Si un proceso nuevo se parece al viejo, es coincidencia, no requisito.

**Sin crecimiento obligatorio.** El conjunto puede encogerse. Quitar un proceso es mutación; no se compensa agregando otro.

**Reordenar el nivel.** Si una tarea resulta ser sub-tarea de otra más grande, se reordena y se declara. El nivel no se hereda: se declara.

`Serie: [conjunto] | Antes: [n procesos] | Después: [n procesos] | Quita: [...] | Pone: [...] | Reordena: [ninguno|qué]`

**Prueba:** ¿el conjunto nuevo cubre el fin que el viejo cubría? ¿Se declaró qué se quitó y qué se puso?
**Falsificador:** un conjunto que solo crece; un proceso nuevo que copia la forma del viejo para seguir la línea; un proceso retirado sin declarar su reemplazo; un conjunto que cubre menos fin que antes.

## El nombre muta con la cosa

**Una mutación no cambia solo el contenido: cambia el nombre y el lugar.**

Si el nombre sobrevive a la mutación, **no hubo mutación: hubo edición.** Un nombre viejo sobre un cuerpo nuevo es una etiqueta que miente — y la etiqueta es lo único que el lector tiene para orientarse.

**Enunciado:** toda mutación acuña un nombre nuevo para lo que cambia, y declara su lugar nuevo si lo tiene.

| Qué muta | Qué cambia con ella |
|---|---|
| **un proceso** | su nombre, en su `Acta` |
| **una sub-tarea** | su nombre de carpeta, y el `Deterrente` que lo justificaba |
| **una tarea** | su `Acta` y su `carga.md` |
| **una rama** | el nombre de la rama, no el del tronco |

**El nombre se lee como nombre propio y la expansión dice qué significa.** Un acrónimo que solo se puede leer deletreando no es un nombre: es una etiqueta.

**`Reemplaza:` apunta al nombre anterior.** El anterior no se borra: se sustituye, y la razón se declara. **Sin `Reemplaza:` no hay cadena, y sin cadena el nombre nuevo no se distingue de un invento.**

**Sin cambio, no hay acuñación.** Una mutación que no cambió nada acuña igual, pero su `Muta:` declara el estado: *"sin cambio"*. Lo que no se permite es acuñar como si hubiera habido un cambio.

**La forma del nombre se cita, no se redefine:** rige `../../formato de proceso.md`, `La acuñación`. Aquí solo se declara **qué muta además del nombre** —el lugar.

```
Lugar: [carpeta nueva o NINGUNO] | Reemplaza: [nombre anterior o NINGUNA]
```

**Prueba:** ¿la mutación acuñó nombre? ¿`Reemplaza:` apunta al anterior? ¿Si cambió de nivel, cambió de carpeta?
**Falsificador:** un nombre que sirve para dos versiones distintas; una acuñación sin `Reemplaza:`; una sub-tarea que muta y conserva el nombre de carpeta; un proceso que cambia y no cambia de nombre; un proceso que copia la forma de la acuñación en vez de citarla.

**Sin reemplazo, no hay mutación: hay retiro.** Cuando el fin dejó de existir y no entra nada en su lugar, el proceso no se muta: se retira. Rige `./retiro.md`.

## Lo que no cambia

El fin no muta al mismo ritmo que el proceso. Un proceso puede reemplazarse entero y el fin seguir siendo el mismo. Si el fin cambia, eso no es mutación de la serie: es una mutación del fin, y se declara como tal.

`Fin: [qué se persigue] | Cambia: [sí|no] | Si cambia: [por qué]`


**Mutar tareas** es una abstracción sobre este proceso, no este proceso. Una tarea es la abstracción que se apoya en los cinco primitivos; el primitivo muta procesos.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el proceso y el cambio que se quiere hacer.
- **Falla:** el cambio no declara qué conserva, o no deja rastro.
- **Sale:** el proceso transformado, completo, con su ancla de mutación.
- **Consume:** quien va a usar el proceso transformado, y la autoridad que lo acepta.

## 1. Origen

**Enunciado:** toda mutación declara el estado inicial y el marco de origen: qué es el proceso desde el principio. Sin origen no hay mutación: hay reemplazo.
**Prueba:** ¿se puede decir de dónde viene el cambio?
**Falsificador:** un cambio sin estado inicial ni origen.

## 2. Cambio declarado

**Enunciado:** antes de mutar, se declara qué cambia, qué se conserva y qué se elimina. Lo no declarado se conserva.
**Prueba:** ¿el registro distingue cambio, conservación y eliminación?
**Falsificador:** un cambio que no declara qué tocó.

## 3. Trazabilidad

**Enunciado:** toda mutación deja el rastro necesario para reconstruir el cambio y al responsable, no solo el proceso. Si otro no puede reconstruirlo sin el mutador, no es mutación trazable.
**Prueba:** ¿otro lee el registro y reconstruye el cambio y el responsable?
**Falsificador:** una mutación que solo el mutador puede contar.

## 4. Libertad controlada

**Enunciado:** la autoridad muta el marco; el ejecutor muta su estado de tarea dentro del perímetro. Para tocar el marco de origen, el ejecutor pregunta y declara el estado actual, el cambio y el beneficio; sin esa captura no hay autorización. La buena intención no es autorización.
**Prueba:** ¿el ejecutor preguntó antes de tocar el marco? ¿La pregunta capturó estado, cambio y beneficio?
**Falsificador:** un ejecutor que cambia el marco sin preguntar, aunque el cambio sea bueno.

## 5. Retorno

**Enunciado:** mutar de regreso no está prohibido: es otra mutación. Se declara la clase `reversible | compensable | irreversible` como información, no como prohibición. La acción persistente irreversible se rige por `../../2 S.A.R.A — mutación/seguridad/contener.md`.
**Prueba:** ¿la clase y el retorno están declarados?
**Falsificador:** una mutación irreversible sin autoridad; una mutación de regreso sin registro.

## 6. Prueba

**Enunciado:** la mutación se prueba con reconstrucción independiente: otro lee el registro y reconstruye el cambio y el responsable. Sin eso, no entra.
**Prueba:** la Prueba de Rendición sobre el registro.
**Falsificador:** un registro que necesita al mutador para tener sentido.

## 7. Creación

**Enunciado:** crear un proceso es una mutación: declara origen, acta y prueba. Si el proceso puede actuar por su cuenta, es un subproceso: además pasa por el `Ciclo` y por la hard rule 8.

**Prueba:** ¿el proceso tiene acta? ¿Si actúa, tiene `Ciclo` y autoridad?
**Falsificador:** se crea sin acta; actúa sin `Ciclo`; se duplica sin autoridad.

## Acta de creación

**La forma se cita, no se redefine:** rige `../../formato de proceso.md`, `La acuñación`. Aquí solo se declara **lo que la creación agrega**.

```
Origen: [fuente|predecesor|ejecutor:<id>] | Reemplaza: [id o NINGUNA]
```

- **Origen.** Fuente, predecesor o ejecutor; **sin origen no hay creación**.
- **Encargo y fin.** La frase exacta y el estado observable; no se interpreta.
- **Muta y conserva.** Lo no declarado se conserva: rige `Sin herencia`, arriba.
- **Prueba.** Corrida, no corrida o pendiente; la no corrida se declara.
- **Autoridad y costo.** Quién autoriza y quién asume el costo.

**El subproceso la cita en su `Crear`; no la absorbe.**

**Prueba:** ¿el acta cita la forma y declara origen, encargo, mutado, conservado, ausencias y prueba?
**Falsificador:** se crea sin acta; el acta no declara ausencias; la prueba se declara corrida sin recibo; el acta copia la forma en vez de citarla.

## Ancla

Se emite antes de mutar; el registro se completa después.

`Origen: [...] | Antes: [...] | Cambia: [...] | Conserva: [...] | Después: [...] | Responsable: [...] | Autorización: [sí|no|no aplica] | Clase: [reversible|compensable|irreversible]`
