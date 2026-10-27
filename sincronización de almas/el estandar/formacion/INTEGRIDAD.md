# INTEGRIDAD — qué falta, y el nombre de lo que falta

**Nombre.** INTEGRIDAD. **Y el nombre dice el acto:** **no es que cada archivo esté completo; es que el sistema no tenga agujeros.**

**Origen.** **De `Integridad` del 22 de octubre, 23 KB que se perdieron cuando `S.A.R.A` murió.** **Lo que quedó en el repo —`EXPRESION.prs`— es solo la parte de emitir la fila: se perdió el triángulo, las seis preguntas, la reasignación y la acuñación del nombre.** **Esto recupera el resto.**

**Reemplaza:** `Integridad` y `Proceso de integridad de procesos`. **Conserva lo que decían; les cambia el lugar.**

**Unidad:** proceso.
**Aplica a:** comprobar, y acuñar.
**Tipo:** estándar. **Se corre antes de mutar, nunca después.**
**Lector:** quien va a hacer crecer un alma, y quien va a dar nombre a lo que apareció.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** el veredicto se lee desde lo que el alma hizo, no desde lo que el alma dice de sí misma.
**Límite:** **no decide entre dos caminos; eso es de la autoridad.** **No juzga si la pieza sirve.**
**Firma:** humano:autoridad · máquina:quien lo corra.

**Variables:** pieza · implícito · agujero · nombre · acto
**Peor:** el chequeo pasa por alto lo que falta **porque nadie lo verbalizó**, y el proceso entra con buena forma y contenido mudo: **la forma está correcta y el archivo no dice nada.**
**Quién:** quien cargue una pieza que cumple el formato y no decide nada.

---

## Integridad es que no tenga agujeros

**Integridad no es estar ordenado. No es cumplir el formato. No es que cada archivo esté completo.**

> **Integridad es que el sistema no tenga agujeros.**

**Y un agujero no se ve mirando la pieza: se ve cuando la lectura trae algo que no se tenía en cuenta.** **Ahí aparece que faltaba algo — o que sobraba algo ocupando el lugar del agujero.**

**Por eso este proceso no arregla el sistema que hay: lo reemplaza por el que no tiene agujeros.** **Si después de la corrida el sistema sigue igual, no hubo integridad: hubo orden.**

### El agujero tiene nombre

**No se declara la ausencia: se declara el proceso que falta.**

| Si se declara como descripción | Si se declara como proceso |
|---|---|
| *«falta medir el peor caso»* | un proceso que mida el peor caso, con sus variables y su falsificador — **hoy no existe: se declara** |
| nadie sabe qué hacer con eso | **se escribe, y el sistema queda completo** |
| vuelve a la autoridad a interpretar | **el ejecutor lo cierra en la corrida** |

### La regla que decide si agregar o rehacer

> **Un proceso: se agrega y se cierra. Un nivel: se rehace.**

**Se puede saber antes de escribir:** **si lo que falta se puede nombrar y definir en una línea, el sistema está a uno.** **Si no se puede nombrar, no falta un proceso: falta un nivel — y ahí no se agrega, se rehace.**

**Por eso no se agrega por agregar:** **un agujero no se tapa sumando piezas. Se tapa cuando desaparece.** **A veces eso es agregar tres; a veces es retirar dos que hacían ruido en el lugar del agujero.**

### La prueba de que quedó íntegro

**¿El sistema que queda puede hacer lo que el anterior hacía — sin que nada sobre?**

- **Sobra algo** → había un agujero tapado con ruido.
- **Falta algo** → el agujero sigue.
- **Ni sobra ni falta** → **íntegro.**

**Y lo que sale tiene que ser equivalente en fin y distinto en forma.** **Si sale peor, no se entendió qué hacía. Si sale igual, no se rehízo.**

---

## Acciones sobre palabras: el veredicto sale de lo que hizo

**Y esta es la regla que hace que el veredicto no sea una opinión.**

**Lo que un alma sostiene no se lee en lo que dice de sí misma: se lee en lo que hizo.**

```plaintext
Dice sostener:   [de su carta, literal]
Hizo:            [de sus .tra, con la cita de cada una]
Coincide:        [sí | no | en parte]
Si no:           [qué hizo que ya no corresponde a lo que dice]
Lleva a:         [acuñar el nombre de lo que es ahora | corregir la carta | nada]
```

**Y el desempate, que es duro y es el único que hay:**

> **Si la carta dice una cosa y los `.tra` dicen otra, gana el `.tra`, y la carta se declara desfasada.**

**Un alma que corrige su carta para que cuadre con lo que hizo no está mintiendo: está tapando el único lugar donde se ve el cambio.**

---

## Las seis preguntas

| # | Pregunta | Qué detecta | Señal de falla |
|---|---|---|---|
| **1** | ¿Un mismo acto puede cumplir los dos? | contradicción entre hermanos | el acto que cumple a uno incumple al otro |
| **2** | ¿Esta pieza pertenece a otro padre? | la disfrazada | su entrada es la salida de otro y no lo declara |
| **3** | ¿Alguien carga esta pieza? | el huérfano | ninguna `Transición` ni `README` la trae |
| **4** | ¿Qué tiene que cumplirse para que esto sirva, y no está escrito? | **el implícito** | lo tomado sin lo que lleva |
| **5** | ¿El texto dice qué decide, o solo ocupa el lugar? | **el proceso mudo** | cumple el formato y no se puede aplicar |
| **6** | ¿Qué falta, y se puede escribir en una línea? | **el agujero y su nombre** | se declara como descripción, no como proceso |

**La 5 es la que la forma no ve.** **Un proceso puede tener sus cuatro campos, su `Prueba` y su `Falsificador` — y ninguno decir algo que se pueda ejecutar.**

**Las señales del mudo:** **el `Sale` no se puede usar sin preguntar; el `Falla` es una intención («falla si está mal»); el `Falsificador` repite la `Prueba`.**

### El implícito se escribe, no se declara

```plaintext
Implícito: [la condición] | Dónde falta: [sección] | Qué pasa sin ella: [el fallo]
Acción:    [se escribió en qué sección | no se pudo: por qué]
```

**Prohibido cerrar un implícito con la palabra «pendiente».** **O se escribe, o se declara `Vacío:` con lo que falta para poder escribirlo.**

**Y si el implícito no se puede señalar en un archivo, no es un implícito: es una tesis.**

---

## El triángulo

**La integridad no se saca con dos puntos.** **Se saca con tres vértices, y los tres son obligatorios:**

| Vértice | Qué aporta | Sin él |
|---|---|---|
| **el ente** | Rastro + Ruta + Carga: qué hay, qué se carga, qué se pierde | **es fantasma** |
| **el sesgo declarado** | desde dónde mira quien muta | el veredicto se saca con dos puntos y se llama triángulo |
| **lo que hay** | lo que el alma hizo, en sus `.tra` | se juzga contra lo que se creía, no contra lo que pasó |

```plaintext
Ente:      [Rastro sí/no | Ruta sí/no | Carga sí/no] | Fantasma: [sí|no]
Sesgo:     [declarado por quien muta | FALTA - no hay veredicto]
Lo que hay:[leído de los .tra, con cita]
Veredicto: [pasa|falla|indeterminado]
```

**Y no corre por decisión del criterio.** **Integridad no es una herramienta del criterio: es su límite.** **No tiene interés en el resultado, y por eso es lo que se puede creer.**

---

## Acuñar el nombre

**Todo muta: el alma, la tarea, el proceso y el nombre.** **Una corrida no termina en veredicto: termina en un nombre nuevo, o en `sin cambio`.**

> **Un nombre que sirve para dos corridas distintas no nombra nada.**

**Y la forma se cita, no se redefine:** rige `./FORMATO.md` y `./LENGUAJE.md`, `Los nombres`. **Aquí solo se declara cuándo: al cerrar la corrida, con el hallazgo adentro.**

---

## Lo que este proceso no hace

**No decide entre dos caminos.** Si dos opciones son válidas, eso es de la autoridad.
**No inventa procesos que no existen.** Un implícito se cierra escribiendo una condición; uno faltante se declara, no se finge.
**No juzga si la pieza sirve.** Eso lo dice el uso.
**No se borra porque encontró algo incómodo.** Un chequeo que se retira cuando molesta no protege: maquilla.

---

## Prueba

**¿Se recorrieron la pieza, sus hermanos y su texto? ¿Corrieron las dos pasadas —forma y contenido—? ¿Cada implícito se escribió, o se declaró `Vacío:`? ¿Cada proceso mudo se reescribió? ¿La pieza que no cabía se movió o se rehízo? ¿El veredicto salió de los `.tra` y no de la carta? ¿Se acuñó el nombre, o se declaró `sin cambio`?**

**Falsificador:** un agujero declarado como descripción en vez de como proceso; una corrida que termina con más piezas de las que empezó sin que un agujero lo exigiera; un sistema que queda igual después de la corrida; se chequea solo la forma y el contenido queda mudo; un implícito cerrado con «pendiente»; un proceso mudo corregido de nombre y no de texto; una pieza que no cabe y se deja donde está; un veredicto sacado de la carta cuando los `.tra` dicen otra cosa; un chequeo que nunca se encuentra nada a sí mismo; un chequeo borrado porque encontró algo incómodo.

## Transiciones

- El hallazgo se puede nombrar en una línea → **se agrega: se escribe, y se cierra.**
- El hallazgo no se puede nombrar → **no falta una pieza: falta un nivel; se rehace.**
- El veredicto contradice la carta → **gana el `.tra`, y la carta se declara desfasada.**
- Lo que apareció es una piel nueva → **`.././sincronización de almas/ente/criterio/MUDAR.md`.**
- Lo que apareció cambia el criterio → **no se acuña: nace otro ente, y lo decide la autoridad.**
- En cualquier otro caso → **se entrega la pieza reescrita, y se cierra.**
