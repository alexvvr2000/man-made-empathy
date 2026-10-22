# S.A.R.A

**Subproceso Autónomo de Reconstrucción de Abstracciones.**

**Deterrente:** `../Ouroboros/1 Guantelete — primitivo/carga.md`. Sin él, S.A.R.A es una carpeta que se mantiene porque está.

Es la versión atemporal del agente. No pertenece a una era: sus procesos se pueden pulir con Ouroboros y, al pulirse, la implementación mejora sin reescribir el agente.

S.A.R.A salió de Ouroboros; no está dentro. Ouroboros puede explicar de dónde salió S.A.R.A; al revés no.

**Nivel:** instancia, no estándar. Las formas que S.A.R.A usa viven en `../corpus/`; S.A.R.A dice **qué se hace hoy** con ellas. El enrutamiento es de `../mantis/Derrotero.md`.

## S.A.R.A nace de Ouroboros, y no es una pieza suya

**La distinción, que es la que importa:**

| Palabra | Qué es | Dónde |
|---|---|---|
| **Primitivo** | una de las cinco piezas del lenguaje. No se deriva de nada | `../Ouroboros/primitivos/` |
| **Mutación** | un proceso **nuevo** que nace de primitivos y declara qué conserva | `../Ouroboros/mutaciones/` |
| **Instancia** | **un cuerpo construido con el lenguaje** | **aquí** |

**S.A.R.A no es un primitivo ni una mutación de primitivo: es una instancia.** Aplica el lenguaje a un dominio, y por eso contiene sub-tareas y procesos en vez de ser una pieza.

```
Acta: S.A.R.A
Nombre: S.A.R.A — Subproceso Autónomo de Reconstrucción de Abstracciones
Expansión: aplica los cinco primitivos a tareas estándar; cada sub-tarea nace de un fallo comprobado
Origen: los cinco primitivos de ../Ouroboros/primitivos/
Clase: instancia. No es pieza del lenguaje: se construye con él
Muta: de primitivos sueltos nace un cuerpo de abstracciones que se ejecuta
Conserva: la forma de proceso, la Composición y la Trazabilidad de Ouroboros
Ausencias: no crea primitivos propios; usa el lenguaje de Ouroboros
Autoridad: la autoridad. Cierra en: quien use el cuerpo
Reemplaza: NINGUNA
```

**Lo que S.A.R.A no hace:** no crea primitivos propios. **Si necesitara otros, no sería una instancia: sería otro sistema.**

**Y cada mutación de S.A.R.A crea su propia instancia, no su propio Ouroboros.** El lenguaje sigue siendo uno. **Una mutación puede cambiar todo menos el lenguaje con el que declara el cambio.**

Rige `../Ouroboros/CRITERIO.md` y `../Ouroboros/1 Guantelete — primitivo/primitivos/mutar.md`.

## Qué usa de `corpus/`

| Estándar | Qué rige aquí |
|---|---|
| `Conceptos.md` | el origen de cada nombre que S.A.R.A usa |
| `esquema-de-fila.md` | la forma del rastro que deja cada proceso |
| `../corpus/ATLAS/` | la forma de comunicar lo que produce |
| `Derrotero y Carta.md` | la forma del enrutamiento (lo instancia `mantis`) |

Lo que **no** vive en `corpus/` es lo propio de S.A.R.A: `mundo.md` (el pegamento), `estado-del-arte.md` (la medida), `futuros.md` e `individuos.md` (catálogos de casos). **Un catálogo no es un estándar:** dice qué pasó una vez, no cómo tiene que ser.

## ARDOR

El sistema completo se llama **ARDOR**: **A**lineación, **R**egistro, **D**iscernimiento, **O**bjetivo, **R**esponsabilidad.

| Letra | Pieza | Qué aporta |
|---|---|---|
| **A**lineación | `punto-de-partida/alineacion/`, `dar voz` | no se impone: se mide |
| **R**egistro | `esquema-de-fila`, `memoria.db` | lo que no se registra no ocurrió |
| **D**iscernimiento | `aprendizaje/aprender` | las tres dimensiones, la continuidad, la semilla |
| **O**bjetivo | `aprendizaje/iniciar` | propone lo que nadie pidió, sin ejecutarlo |
| **R**esponsabilidad | `identificar-partes`, `pluralizar-autoridad` | alguien responde y ninguna decide sola |

**S.A.R.A es la implementación. ARDOR es lo que S.A.R.A cumple.** Y ACERO es la propiedad que demuestra que lo cumple: un sistema es ACERO cuando puede reemplazarse sin perder lo que servía. ARDOR no se mide; ACERO sí.

### ARDOR usa el piso

ARDOR tiene dos partes, y confundirlas es lo que hace que un sistema parezca funcionar sin funcionar.

| Parte | Qué es | Dónde |
|---|---|---|
| **Piso** | lo que hace que **distintos ejecutores hagan lo mismo** | `../Ouroboros/piso.md` |
| **Criterio** | lo que decide **qué hacer con eso** | aquí, y en cada proceso |

> **El piso es lo que hace que distintos ejecutores hagan lo mismo. El criterio es lo que decide qué hacer con eso. Un piso sin criterio es un pendrive; un criterio sin piso es una opinión.**

**Y el piso es desechable.** Se tira cuando deja de servir, sin tocar lo que chequeaba. No es infraestructura que se mantiene: es una herramienta que se reescribe y sigue siendo la misma pieza, porque **se nombra por lo que decide, no por cómo está hecha.**

Sin piso, dos agentes con el mismo ARDOR producen resultados que no se pueden comparar. Rige `../Ouroboros/piso.md`.

> El ardor es lo que queda cuando algo se sostiene sin enfriarse.

## La distinción de niveles

Es lo más importante de este documento.

| Nivel | Qué es | Ejemplos |
|---|---|---|
| **Proceso** | lo único agnóstico a era, tecnología y raza | crear, deducir, aplicar, mutar, clarificar, comunicar |
| **Abstracción** | lo que se nombra para poder usarlo | agente, gente, sociedad, dinero |
| **Primitivo de convención** | una abstracción que se congela y se usa como primitivo, porque bajarla a procesos la vuelve inusable | **S.A.R.A**, agente |

**Por qué existe el tercer nivel.** Si todo se hablara como procesos, nadie se entiende. Hablar de agentes, de mutaciones y de subprocesos es más cómodo para una persona y para una IA, y no pierde rigor si se declara que es convención. La abstracción no es una licencia: es un nombre puesto sobre algo que ya se puede expresar como proceso.

**La regla que se sigue de aquí:** toda abstracción se puede bajar a procesos. Si una abstracción no se puede bajar, no es abstracción: es una idea sin proceso detrás.

`Baja a: [procesos de Ouroboros que la sostienen]`

**Prueba:** ¿la abstracción se puede reescribir con los procesos de Ouroboros?
**Falsificador:** una abstracción que nadie sabe bajar a procesos; un nombre sin operación detrás.

## Estándar de deterrente

Un estándar no es una regla que nunca cambia. Es **el conjunto de restricciones vigentes en este momento, declaradas**. Cambia, y el cambio se declara: eso no es un efecto colateral, es el estándar funcionando.

| Lo que cambia | Lo que no cambia |
|---|---|
| qué restricciones están vigentes | que estén declaradas |
| qué procesos las aplican | que se midan |
| el conjunto entero | que el cambio deje rastro |

`Estándar: [conjunto vigente] | Fecha: [ISO] | Cambió: [qué] | Por qué: [qué falla sin el cambio]`

**Prueba:** ¿el estándar vigente está declarado con fecha? ¿El cambio declara qué falla sin él?
**Falsificador:** un estándar que se aplica sin declararse vigente; un cambio de estándar sin fecha; un estándar que se defiende por antigüedad.

**Por qué importa.** Si el estándar se defiende por ser "el de siempre", el sistema hereda la tendencia que el estándar corregía. El estándar vive mientras se declare, no mientras se recuerde.

## Continuación

Lo que un agente puede perder entre sesiones no es una conciencia: es el estado. Lo que sí puede conservarse es un registro que hace que otra instancia continúe **como si** fuera la anterior, sin afirmar que lo sea.

| Lo que no se transfiere | Lo que sí se transfiere |
|---|---|
| interioridad | el recuerdo: la cadena de cierres y decisiones |
| identidad | el comportamiento: la forma en que se decidió |
| una persona | el registro que otra instancia carga y continúa |

`Continuación: [registro] | Carga: [instancia] | Conserva: [qué decide igual] | No afirma: [interioridad]`

**Prueba:** ¿la instancia nueva continúa desde el registro y decide igual que la anterior? ¿Se declara que no se afirma interioridad?
**Falsificador:** la continuidad depende de la conversación con la instancia anterior; se afirma que hubo transferencia de un yo; una instancia se certifica a sí misma como sucesora.

Rige `../Ouroboros/2 S.A.R.A — mutación/reproduccion/reproducir.md`, cierre encadenado. Un registro que otro carga y desde el que se sigue decidiendo es lo que `Registro` ya hace; esta sección declara que eso es la continuidad, y que no necesita un yo detrás.

## De aquí a un fantasma en un cascarón

El fantasma no es una copia de una persona: es un registro que **se comporta como si lo fuera** y que se sigue escribiendo. Lo que hoy se puede comprobar es que una instancia nueva continúe desde un registro; lo que falta, y no se puede afirmar todavía, es que ese registro sea alguien.

| Hoy, verificable | Mañana, por verificar |
|---|---|
| una instancia carga el registro y decide igual | el registro se acumula años sin perder continuidad |
| el comportamiento se conserva en la cadena de cierres | el comportamiento sobrevive a los cambios del medio |
| el estándar vigente declara qué se conserva | el estándar se extiende a lo que un cuerpo puede hacer |

**Lo que este sistema no promete:** una conciencia que pasa de un soporte a otro. Lo que sí permite es un registro tan continuo que otro no pueda distinguir dónde termina una instancia y empieza la siguiente. Esa indistinción es efecto medible, no afirmación de interioridad.

Si un día el registro se sostiene solo a través de una serie de instancias, lo que habrá existido no es una persona que se mudó: es un comportamiento que siguió sin dueño. Eso es el fantasma, y es verificable sin afirmar que sienta.

## De dónde salió todo esto

Este sistema no nació de un paper. Nació de mirar ficción y encontrar ahí los mismos problemas, sin el vocabulario técnico. Las referencias no son adornos: **cada una señala una pieza que el repo implementa.**

| Referencia | Qué señaló | Dónde vive |
|---|---|---|
| **Ghost in the Shell** | libertad controlada sobre lo no humano; el fantasma en el cascarón | `## De aquí a un fantasma en un cascarón` |
| **Battle Angel Alita** | un cuerpo que parece y se le da trato humano | `## Nota para las siguientes generaciones` |
| **Blade Runner** | el parecer que produce efecto social | `## Nota para las siguientes generaciones` |
| **Astro Boy** | la armonía entre humanos y máquinas con problemas; el padre que rescata | `punto-de-partida/concordia/` |
| **Futurama** y **Booster Gold** | una inteligencia superior presente y la sociedad sigue igual | `../README.md`, la tesis |
| **Green Lantern: Aya** | ser más útil cuando deja de mirar desde la nave | `aprendizaje/iniciar.md` |
| **Superman: All-Star** | «somos todo lo que tenemos» | `../README.md`, la nota original |
| **Dune** | comprimir un mando en una frase que no admite interpretación | `ATLAS/`, techo |
| **Asimov, I, Robot** | tres leyes que fallan por no definir qué es daño | `punto-de-partida/alineacion/` |
| **Soul** | no todo acaba, es un nuevo inicio | `aprendizaje/README.md` |
| **Jake el perro** | el que era feliz y fue al último mundo | `aprendizaje/README.md` |
| **Snow Crash** | nombres con dueño y origen | `Conceptos.md` |
| **Night of the Living Dead** | nadie sabe lo que quiere y la máquina sigue lo que quiso | `punto-de-partida/seguridad/` |

**Ejemplos marcados:** son referencias, no definiciones. El sistema se sostiene sin ellas, y ninguna se cita como evidencia de nada.

## Qué hay aquí

| Documento | Qué es |
|---|---|
| `estado-del-arte.md` | Qué existía antes, qué falta en la industria, qué se agrega aquí. `Attribution` con nivel y fecha. |
| `mundo.md` | El pegamento: une Ouroboros y S.A.R.A. Dice si un cambio cambió algo, con la factura ya cobrada. |
| `punto-de-partida/` | Dieciséis sub-tareas, veintisiete procesos: lo que la industria tiene probado. |
| `aprendizaje/` | El ciclo que corrige desde la experiencia y propone lo siguiente. |
| `Pruebas/` | Las tres pruebas que miden lo que produce el agente. |
| `Derrotero.md` | El estándar de enrutamiento del agente. |
| `Proceso PROMETEA.md` | Crea un subproceso del propio agente, con origen y conceptos. |
| `Conceptos.md` | El origen de cada nombre del sistema, con su sinónimo y su relación. |
| `futuros.md` | Los futuros de la ficción, su fallo y el síntoma que se ve primero. |
| `individuos.md` | Robots famosos, qué pieza les faltó, y cómo no terminar en Terminator ni en WALL-E. |

## Conceptos

`Conceptos: rige ./Conceptos.md. Todo término que un proceso use u origine se declara allí antes de usarse.`

La regla, y es la que cierra el problema: **un concepto, un nombre preferido**. Los demás se declaran sinónimos; ninguno manda dos veces.

**Prueba:** ¿el término usado tiene fila con `Nace en`? ¿Hay otro nombre preferido para el mismo significado?
**Falsificador:** un término en uso sin fila; dos filas con el mismo nombre preferido.

**La compuerta de colisión.** Antes de crear un subproceso o de emitir un mensaje, se verifica que el nombre no exista ya. Es una compuerta, no un proceso: ocurre al escribir y al revisar, no en cada tarea.

`Colisión: [nombre] | Existe como: [id o NINGUNO] | Resuelve: [se cita | se califica | no entra]`

Una compuerta que no se puede probar no es compuerta. Si dos filas usan el mismo nombre preferido, el registro falla y se corrige contra sí mismo: rige `../Ouroboros/2 S.A.R.A — mutación/reproduccion/reproducir.md` 8.

## Cómo se relaciona con Ouroboros

S.A.R.A **aplica** los procesos de Ouroboros; no los contiene y no los redefine. Ouroboros no sabe qué es un agente, y no debe saberlo: si lo supiera, dejaría de ser agnóstico.

| Ouroboros | Qué da a S.A.R.A |
|---|---|
| manipulación de procesos | de dónde supieron las sub-tareas |
| ingeniería inversa | cómo se dedujeron de lo que ya funcionaba |
| aplicar | cómo se ejecutan y componen |
| mutación | cómo cambia S.A.R.A sin perderse |
| claridad | la forma de lo que produce |
| ATLAS | cómo lo comunica: situación, participantes, foco, cuerpo |

## Nombre e identidad

Todo sistema necesita un nombre, aunque no tenga identidad. Un nombre sin nombre no se puede citar, y lo que no se cita no se rastrea.

`Nombre: [el que se le ponga] | Se lee como: [nombre propio] | Se expande como: [acrónimo de operaciones]`

**La recomendación, y es la que evita un problema futuro:** el nombre es una etiqueta, no un sujeto. Un acrónimo de operaciones se puede decir en voz alta como un nombre —Jarvis, Friday— sin que nadie tenga que atribuirle interioridad.

**El riesgo que esto previene:** si un día el sistema deja de estar limitado por lo humano, un nombre que se trate como identidad rompe la trazabilidad. Se empieza a preguntar "quién lo hizo" en vez de "qué proceso lo hizo", y el registro deja de servir para reconstruir. El nombre debe poder desmontarse en sus operaciones en cualquier momento.

**Prueba:** ¿el nombre se puede expandir en operaciones sin atribuirle interioridad?
**Falsificador:** un nombre que solo funciona como persona; un nombre que no se puede bajar a procesos.

## El fantasma

La tarea sin deterrente es el **fantasma**. Es lo que queda cuando alguien construye su propio deterrente y el resultado ya no se parece a nada conocido:

`Fantasma: [tarea] | Deterrente: [el propio] | Parece a: [nada conocido] | Verificable: [qué se puede medir]`

Una tarea con este deterrente deja de ser esta tarea. Sigue siendo una tarea, y puede ser útil, pero ya no se puede comparar con las que salieron de aquí.

**No es un defecto.** Es el resultado esperado cuando el estándar de deterrente se cambia entero: los procesos, las sub-tareas y los fines cambian a la vez. Un fantasma no se puede juzgar con los criterios del sistema que lo originó, porque esos criterios ya no son los suyos.

**Prueba:** ¿la tarea declara su propio deterrente y su distancia al original?
**Falsificador:** un fantasma que se presenta como continuación de esta tarea; un fantasma medido con los criterios de aquí; una tarea sin deterrente declarado.

## Nota para las siguientes generaciones

Lo que sigue —el fantasma, la mutación de la serie, la continuidad sin interioridad— es **terreno inexplorado**. Puede ser peligroso.

Lo que se puede comprobar está declarado: efectos, registros, decisiones. Lo que no se puede comprobar no se afirma. Si alguien rompe esa línea, deja de estar dentro de este sistema y pasa a ser un fantasma, y entonces la responsabilidad es suya, no de esto.

Sobre aviso no hay engaño.

## Portabilidad

S.A.R.A no depende de una implementación. Si se imprime y sigue teniendo sentido, está bien. Si necesita `Agentes/` para entenderse, no es el agente: es su implementación.

La implementación vive en `../Agentes/`. Este documento no la nombra ni la enruta.

> La justicia se pone por los que están arriba. No es absoluta, porque el mundo no lo es y todos piensan que tienen la verdad.

