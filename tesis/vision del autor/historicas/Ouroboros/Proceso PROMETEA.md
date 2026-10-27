# Proceso PROMETEA — crear un subproceso

**Nombre/** PROMETEA — **P**roceso de **R**econstrucción y **O**btención de **M**ódulos **E**mergentes con **T**razabilidad, **E**tiqueta y **A**utonomía/ Se lee como nombre propio; la expansión dice qué hace/

**Origen del nombre/** Prometeo moldeó al primer humano y le dio el fuego; la Mujer Maravilla está hecha de arcilla y animada/ El proceso no usa arcilla: usa cera, porque se puede fundir y rehacer/ El nombre dice el acto, no el material/

**Unidad:** subproceso/
**Aplica a:** crear/
**Tipo:** proceso/ Se ejecuta; no se interpreta/
**Nivel:** abstracción operativa/ Baja a `manipulación de procesos` y `mutación` de Ouroboros/
**Lector:** autoridad y ejecutor/
**Dueño:** la autoridad/
**Estado:** vigente/

**Sesgo:** el subproceso se lee desde la falta que cubre, no desde la idea que lo motivó.
**Límite:** no decide si el subproceso sirve en el uso; eso es integridad.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `formato de proceso.md`

**Variables:** subproceso · función · término · conceptos · autoridad
**Peor:** se crea un subproceso sin término ni autoridad, y se queda para siempre sin que nadie pueda retirarlo
**Quién:** quien carga el subproceso, y quien debe retirarlo


**Manipulación/** Todo cambio a un subproceso pasa por `//////1 Guantelete — primitivo/herramientas/manipulacion/md`: ahí se nombran las variables antes de que el proceso exista/ Un subproceso creado sin pasar por ahí queda sin variables, y sin variables no hay contra qué chequearlo/

## Tesis

Un agente necesita subprocesos: piezas propias que hagan algo que el agente no hace/ PROMETEA los crea, y hace tres cosas que ningún proceso suelto hacía juntas: les da origen trazable, les exige concepto, y les pone término/

Lo que un subproceso produce no se pierde cuando termina: queda en su registro y en el registro de conceptos/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** la función que el agente no cubre y la autoridad que la pide/
- **Falla:** el término del subproceso no está declarado, o su nombre ya existe, o no deja rastro/
- **Sale:** un subproceso con contrato completo, y sus conceptos dados de alta/
- **Consume:** el agente que lo carga, y `Registro` que lo conserva/

## No se crea sin integridad

**Antes de crear, integridad corre.** No es opcional y no lo decide el criterio: **PROMETEA la llama sí o sí antes de hacer algo con el subproceso.**

**Por qué:** integridad no solo rellena huecos — **también puede rehacer todo desde 0.** Si PROMETEA crea sin llamarla, **puede pasar que el proceso se use sin que nadie se dé cuenta de que en realidad era un momento de rehacer, no de agregar.**

**PROMETEA es un proceso estándar ya no se preocupa por fantasmas:** su regla es **no crear implícitos**. Lo que queda fuera del subproceso se cierra en la creación o no se crea.

Rige ./integridad.md, Cuándo se usa.

**Prueba:** ¿integridad corrió antes de crear? ¿el veredicto fue hueco o desde 0?
**Falsificador:** un subproceso creado sin integridad corrida; un indicio de rehacer tratado como hueco; un implícito que se deja para después.
## Cómo se crea

1/ **Nombrar la falta/** Qué función del agente no está cubierta/ Sin falta nombrada, no hay subproceso: hay duplicado/
2/ **Buscar el existente/** ¿Ya hay un subproceso o una abstracción que haga eso? Si sí, se calibra esa; no se crea otra/
3/ **Declarar el nombre y su expansión/** El nombre se lee como nombre propio; la expansión dice operaciones/ Sin expansión en operaciones, no entra/
4/ **Declarar los conceptos/** Todo término nuevo que el subproceso use o origine se da de alta en `//Conceptos/md` antes de la primera ejecución/
5/ **Declarar el ciclo/** `Crear`, `Terminar` y `Cierra en`/ Sin término, no se crea/
6/ **Verificar la colisión/** ¿El nombre ya existe? ¿El concepto ya tiene otro nombre? Se resuelve antes de crear/
7/ **Correr una vez/** La primera ejecución es su prueba; sin corrida, queda en hipótesis/

**Prohibido** ejecutar el paso N+1 sin la salida del N/

## Lo que todo subproceso declara

`Subproceso: [nombre] | Expansión: [operaciones] | Función: [qué cubre que el agente no cubre] | Entra: [///] | Falla: [///] | Sale: [///] | Consume: [///] | Crear: [condición] | Terminar: [condición] | Cierra en: [quién] | Conceptos: [ids de //Conceptos/md] | Autoridad: [tipo:nombre]`

Sin función, es duplicado/ Sin término, es fuga/ Sin conceptos, contamina la lengua/ Sin autoridad, no existe/

## De dónde salen los principios

Este proceso no inventa reglas: las junta, que era lo que faltaba/

| Principio | Dónde vivía | Qué aporta aquí |
|---|---|---|
| No auto-replicación | `//punto-de-partida/evaluacion/vigilar-tendencias/md` 8 | crear un subproceso exige autorización explícita |
| Ciclo | `//punto-de-partida/reproduccion/reproducir/md` | crear, servir y terminar con condición |
| Equipo y subprocesos | `//punto-de-partida/reproduccion/reproducir/md` §Equipo | toda sub-tarea se declara y deja traza |
| Acta de creación | `////////////1 Guantelete — primitivo/herramientas/mutar/md` | origen, encargo, mutado, conservado, ausencias |
| Conceptos | `//punto-de-partida/reproduccion/reproducir/md`, `conceptualizar` | todo término nuevo se registra |

## El molde de cera

Un subproceso se crea como se moldea cera: se le da forma con lo que hay, se quema, y si no sirve se funde y se vuelve a molde/ Nada de lo moldeado es permanente; lo permanente es el molde/

**El molde** es la forma de este proceso/ **La cera** es el subproceso concreto/ Rehacer un subproceso no es un fracaso: es el proceso funcionando/

## Lo que previene

| Riesgo | Cómo lo previene |
|---|---|
| duplicar en vez de crear | paso 2: buscar el existente antes de crear |
| subproceso sin fin | paso 5: `Terminar` y `Cierra en` obligatorios |
| subproceso que no sirve a nadie | paso 1: la falta se nombra antes |
| vocabulario que crece sin origen | paso 4: conceptos en el registro |
| proliferación de copias | regla 8 de `Conversacional`: cada subproceso exige autoridad |

## Prueba

¿El subproceso declara función, término y conceptos? ¿Corrió una vez? ¿Su nombre se lee como nombre propio?

**Falsificador:** un subproceso sin término; un nombre ya usado; un concepto sin alta; una creación sin autoridad.
## Transiciones

- Si el subproceso cubre la falta y corre una vez → se entrega con su contrato y sus conceptos/
- Si ya existe uno que cubre la falta → se calibra ese y se declara la equivalencia/
- Si el nombre o un concepto colisionan → `[VACÍO - SIN NOMBRE]` y se resuelve antes de crear/
- Si no declara término → no se crea/
- En cualquier otro caso → se entrega y se cierra/
