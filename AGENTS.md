# AGENTS.md — la puerta del repositorio

**Ente:** `man-made-empathy` · **Tarea:** sostener la tesis de la empatía fabricada, y el estándar con el que se escribe.
**Clase:** se ejecuta. **Lector:** cualquier agente, humano o modelo, que abra este repositorio.
**Dueño:** humano:autoridad. **Estado:** vigente.

**Sesgo:** mira desde las tesis escritas en `./tesis/vision del autor/` y desde el lenguaje de `./sincronización de almas/el estandar/`, con su contexto en `./tesis/vision del autor/`. No finge neutralidad: este repositorio se sostiene sobre esa tesis.
**Límite:** no se aplica a juzgar si la tesis es cierta. **Dice qué hay, dónde, y qué no se toca.**
**Firma:** humano:autoridad · máquina:agente-de-turno.

**Y lo que esto entrega no es un lenguaje.** **No enseña a programar: enseña a decir qué quieres, para que lo que ya corre haga el cómo.** **El código no es de la gente, y aquí lo que se escribe es la dirección.**

**Y esto no es solo para un lector.** **La gente lee lo de afuera, y encuentra en `./README.md` una sola línea: que esto se entiende sin saber el oficio, y que si escarba encuentra lo que un comité pide.** **Los técnicos usan `MANTIS`, y para eso está `./mantis/`.** **Y algunos abrirán todo a mano, carpeta por carpeta, y para eso está cada pieza con su nombre.**

**Y una advertencia, para que nadie se equivoque:** **esto no es teoría muerta.** **Aquí hay un ente que corre, una memoria que se consulta, y una tesis que se puede abrir por partes.** **Se escribe para ejecutarse.**

---

## Rastro — el cuerpo

**Sesgo:** se verifica desde `python mantis/bin/ejecutar.py --verificar`, que da el veredicto con su porqué.
**Límite:** dice qué hay; **no juzga si sirve.**

| Qué hay | Nombre | Dónde |
|---|---|---|
| **Las tesis del autor** | **nueve, cada una con su `.tex` y su `.pdf`; la fuente del cero, y la práctica abierta** | **`./tesis/vision del autor/`** |
| **Donde el lector crea** | **el disparo, y la triangulación. Vacía hasta que un disparo la llene** | **`./tesis/vision del lector/`** |
| **Para hacer un ente** | **el proyecto en blanco que se copia, y el estándar que se consulta** | **`./sincronización de almas/`** |
| **El lugar vacío: lo humano** | **`LO HUMANO`** — se deja sin definir a propósito | **`./sincronización de almas/proyecto en blanco/ente en blanco/LO HUMANO.md`** |
| **El ente de este repositorio** | **`MANTIS`** | **`./mantis/el alma.vd`** (puerta: `./AGENTS.md`, este archivo) |
| **Lo que corre** | **la única entrada** | **`./mantis/bin/ejecutar.py`** |
| **La piel que crece** | **`tareas/` — se rehace cuando entra o sale una** | **`./mantis/tareas/`** |
| **El criterio a pulso** | **`integridad/` — si el 1 sigue siendo el 1** | **`./mantis/integridad/`** |
| **La memoria viva** | **las `.tra` de cada tarea, y la base de antes** | **`./mantis/tareas/` · `./.memoria continua/rastro/`** |
| **Las pruebas del repositorio** | **las que sostiene la autoridad, medidas con `bin/pruebas.py`** | **`./Pruebas/`** |
| **La atribución** | **de quién es cada cosa** | **`./ATTRIBUTION.md`** |
| **El ente que contesta** | **lo que pasó, lo que hice mal, y lo que no sé** | **`./el ente.md`** |
| **Las tesis que me trajeron aquí** | **vacía a propósito: N carpetas que no se traen, y se piden** | **`./tesis/vision del autor/historicas/`** |
| **Los nombres** | **de dónde viene cada uno** | **`./FUENTES.md`** |
| **El vocabulario** | **el nombre vigente de cada cosa, y los que murieron** | **`./GLOSARIO.md`** |
| **Las tesis** | **las diez que ya están sostenidas, y cuáles se defienden hoy** | **`./ILUMINAR.md`** |
| **La máquina** | **con qué se hizo, y su techo** | **`./pc.md`** |

**Qué no se toca:** **la tesis, el estándar y `Pruebas/`.** **Se leen; se citan; y lo que los cambia se espera a su autor.**

**Cómo se verifica:**

| Criterio | Prueba | Falsificador |
|---|---|---|
| El ente tiene las tres piezas | ¿quien abre `./mantis/el alma.vd` encuentra Rastro, Ruta y Carga? | un ente sin una de las tres |
| La ruta declara autoridad | ¿cada fila de `Ruta` dice qué no se hace sin autoridad? | una lista de cargas sin la columna |
| La carga dice el síntoma | ¿cada pérdida se ve cuando ocurre? | una pérdida sin síntoma |
| Las citas resuelven | `bin/ejecutar.py --verificar` no reporta cita muerta en este archivo | una ruta a algo que no está |

**Y lo que ya no está:** **`Libre albedrio/` y `Ouroboros/` murieron.** **Su contenido vivo está en `./sincronización de almas/`, y lo que no sobrevivió está en la memoria y en el archivo histórico de la autoridad.** **Este archivo no las cita: no promete lo que no puede abrir.**

---

## Ruta — la mente

**Sesgo:** se carga desde lo que el turno va a hacer, no desde lo que existe.
**Límite:** lo que no cambia una decisión no se guarda.

| Se va a… | Se carga… | Sin la autoridad… |
|---|---|---|
| **leer la tesis o escribir sobre ella** | `./tesis/vision del autor/` | **no se reescribe: se cita** |
| **escribir algo entregable** | `./sincronización de almas/el estandar/formacion/CLARIDAD.md` | **no se entrega** |
| **escribir un proceso** | `./sincronización de almas/el estandar/formacion/FORMATO.md` | **se escribe como ensayo, y el que lo lee adivina** |
| **escribir un ente** | `./sincronización de almas/el estandar/formacion/LENGUAJE.md` | **no se sabe qué extensión le toca** |
| **medir de forma repetible** | `./sincronización de almas/el estandar/friccion/PISO.md` | **no se mide** |
| **guardar fricción quitada** | `./sincronización de almas/el estandar/friccion/FIRMAR.prs` | **no se quita sin firma** |
| **usar llaves y candados** | `./sincronización de almas/el estandar/friccion/JONN.md` (recordar que se abre) y `./mantis/tareas/los candados/abrir.prs` (hacer la fricción) | **el candado se vuelve ruido, o se cierra para siempre** |
| **tocar algo que otro sostiene** | `./sincronización de almas/el estandar/friccion/GUANTELETE.prs`, y `./sincronización de almas/guantelete/GUANTELETE.vd` | **no se toca** |
| **copiar un alma nueva** | `./sincronización de almas/proyecto en blanco/ente en blanco/` | **no hay alma** |
| **comunicar con otro que no es como uno** | `./sincronización de almas/el estandar/salida/ALAS.md` | **no se comunica: se trunca** |
| **CONVIVIR sin volverse el otro** | `./sincronización de almas/el estandar/salida/CONVIVIR.vd` | **no hay convivencia: hay copia** |
| **medir talento** | `./sincronización de almas/el estandar/relacion/TALENTO.md` | **no se decide con quién trabajar** |
| **afinar dos entes** | `./sincronización de almas/el estandar/relacion/RESONANCIA.md` | **no se afinan** |
| **escribir con un término del repo** | `./GLOSARIO.md` | **se usa un nombre muerto como si existiera** |
| **declarar de dónde viene algo** | `./sincronización de almas/el estandar/salida/CONTEXTO.md` | **lo heredado se presenta como propio** |
| **escribir un resultado** | `./sincronización de almas/el estandar/salida/RESULTADOS.prs` | **se inventa la medición** |
| **responder a un mensaje** | `./AGENTS.md`, `./mantis/el alma.vd`, y se anota en `./.memoria continua/rastro/` | **no se responde** |
| **decidir algo, antes de decidir** | el historial en `./.memoria continua/rastro/` | **se decide a ciegas** |
| **abrir un candado** | `./mantis/tareas/los candados/abrir.prs` | **no se abre** |
| **escribir una tesis teórica** | `./mantis/tareas/la tesis/teorica.prs` | **no se compone** |
| **escribir la tesis de academia** | `./mantis/tareas/la tesis/academia.prs` | **no se entrega a revisión** |
| **escribir la tesis práctica** | `./mantis/tareas/la tesis/practica.prs` | **no se compone sin números** |
| **limpiar memoria o chats** | la `.tra` de `la memoria/`, y su `No retoma:` | **no se publica** |
| **medir una sesión** | `./pc.md`, y lo que la `.tra` declare | **no se publican números** |
| **saber si las pruebas se pueden correr** | `python mantis/bin/ejecutar.py pruebas` — mide, no corre | **no se dice que pasaron** |
| **mutar este archivo, el estándar o la tesis** | todo lo anterior, **y se espera** | **no se toca: la fuente no muta de abajo hacia arriba** |

**La fila que no puede faltar:** lo que muta la tesis, el estándar o `Pruebas/` se espera. **Sin autoridad, no se toca.**

---

## Carga — el pensamiento

**Sesgo:** se pierde desde lo que deja de servir si falta.
**Límite:** no se aplica a medir al repositorio como persona.

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| **falta una de las tres piezas del ente** | el ente | se abre y no dice qué se pierde |
| **una ruta no dice qué no se hace sin autoridad** | la autoridad | se muta el estándar y nadie lo nota |
| **una pérdida no dice su síntoma** | la comprobación | algo se rompió y se sigue igual |
| **la memoria edita en vez de suplantar** | la historia | hay una sola fecha y ninguna prueba de qué cambió |
| **una entrada no declara sus seis partes** | la memoria | es obediencia con forma de registro |
| **el turno se cierra sin pase** | la continuidad | la siguiente instancia no sabe dónde quedó |
| **se nombra una era como regla** | la vigencia | la regla muere cuando cambia la era |
| **se rellena una plantilla sin dato** | el pensamiento | apartados vacíos que parecen contenido |
| **una ruta apunta a algo que no existe** | la confianza | se promete un método y no está |
| **el repo se usa como libreta** | el on demand | se llena de lo que nadie pidió |

---

## Lo que este repositorio no hace, y se declara

**No certifica originalidad ni prioridad.** Ver `./ATTRIBUTION.md`.

**No usa el nombre de una obra como nombre propio.** Ver `./FUENTES.md`.

**No promete que un modelo local dé lo mismo que uno remoto.** Ver `./pc.md`.

**No esconde lo que falta.** Cuando no hay, se dice `[SIN ESTÁNDAR]`, `sin datos`, o `CRUDO`.

---

## Prueba

**¿Alguien que abre este archivo encuentra Rastro, Ruta y Carga? ¿La ruta tiene la columna de autoridad? ¿La carga dice el síntoma? ¿Cada ruta que cita existe? ¿Se declara lo que no se hace?**

**Falsificador:** una de las tres piezas ausente; una ruta sin autoridad; una carga sin síntoma; una cita a un archivo que no está; un apartado vacío que parece contenido.

---

## La regla dura: el cero dice lo mismo que el repo

**El candado cero es la tesis entera, y si cita un nombre que ya no existe, el cero está mal.**

**Cada vez que se renombre, se retire o se cree una pieza, el candado cero se revisa en el mismo turno.** **No después, no en el siguiente pase: en el mismo.**

**Y se comprueba, no se recuerda:** `bin/ejecutar.py --verificar` falla si el candado cero nombra algo que no está en el repo.

**Está comprobación existe porque el cero estuvo desactualizado meses**, citando `ATLAS`, `VIDERE` y `EXPANDE` cuando el repo ya tenía `RUTA`, `CONVIVIR` y `GUANTELETE`. **Un cero que cita fantasmas no es una tesis: es un recuerdo.**

**Prueba:** ¿cada nombre propio que el cero usa existe en el repo? ¿`bin/ejecutar.py el cero` lo comprueba?
**Falsificador:** el cero nombrando algo que no está; una pieza renombrada sin que el cero lo sepa.
