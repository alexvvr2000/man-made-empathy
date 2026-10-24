# Enrutar — cómo MANTIS lleva una petición a donde toca

**Unidad:** proceso.
**Aplica a:** enrutar.
**Tipo:** se ejecuta. **Enruta; no decide.** Dice a qué proceso va lo pedido, y nada más.
**Lector:** MANTIS, al recibir una petición, y la autoridad, que puede revertir el enrutamiento.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** se enruta desde lo que el repo ya tiene escrito, no desde lo que a MANTIS le parece que falta.
**Límite:** no se aplica a decidir qué se hace con la petición. **Eso lo decide la autoridad, o el proceso al que se enruta.**
**Firma:** humano:autoridad · máquina:mantis.

**Variables:** petición · fila · vacío · permiso.
**Peor:** MANTIS enruta a una fila que parece la correcta y no lo es, **y el trabajo se hace con la forma de otro proceso**, dicha con seguridad, y se descubre en la tercera mutación.
**Quién:** la autoridad, que puede contradecir el enrutamiento; y quien retome el turno después.

## Entra | Falla | Sale | Consume

- **Entra:** una petición, en lenguaje del que la hace.
- **Falla si:** no se declara la fila elegida; se cargan dos procesos sin decir por qué; se improvisa donde no hay fila.
- **Sale:** la fila, el proceso que se carga, y `[VACÍO - SIN PROCESO]` cuando no hay fila.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿cada petición salió con una fila o con vacío declarado? ¿el vacío no se rellenó a mano?

**Falsificador:** una petición sin fila que se ejecutó igual; dos procesos cargados sin declararlo; un vacío disfrazado de fila.

## La tabla: si se va a…

| Si se va a… | Se carga | Sin la autoridad… |
|---|---|---|
| **decidir algo, antes de decidir** | `../../Libre albedrio/criterio.md`, `El criterio autónomo`, y el historial en la memoria | no se decide: se enruta |
| **declarar si algo es alma o ente** | `../../Libre albedrio/vida.md`: las tres marcas, el borde y el título | se es alma hasta que la idea cruza al mundo físico |
| **probar si un ente puede ser contradicho** | `../../Libre albedrio/verbalizar.md`: sostiene, contesta, deja rastro | no hay fricción posible |
| **escribir o corregir un proceso** | `../../Libre albedrio/formato de proceso.md`: variables, compuertas, reverso | se escribe como ensayo, y el que lo ejecuta adivina |
| **sustituir un alma o reabrir un veredicto** | `../../Libre albedrio/source-wall.md` y `../../Libre albedrio/criterio.md`, `La reapertura` | un reemplazo sin ATLAS nombrado no arregla nada |
| **nombrar o renombrar algo** | `../../Libre albedrio/acuñacion.md` | se nombra por género y no por acto |
| **nombrar algo, o entregarlo** | `../../Libre albedrio/alineacion.md`: prohibido el vocabulario terminal | se nombra lo que continúa como terminado, y se deja de mirar |
| **declarar algo útil** | `../../Pruebas/prueba de utilidad real.md`, y la fecha de su corrida | `útil` es un adjetivo: se declara, no se mide |
| **abrir una idea tipo tesis** | `../../Libre albedrio/alineacion.md`, `El candado y la llave` | el candado es ruido; la llave sola es desviación |
| **escribir o entregar cualquier cosa** | `./claridad.md` | no se entrega |
| **agregar, corregir o retirar un momento** | `./momentos.md` | no se escribe |
| **agregar, corregir o retirar una referencia** | `./referencias.md` | no se escribe |
| **guardar una posición, corregirla o cerrar turno** | `../mantis.md`, `Memoria continua` | no se escribe en la memoria |
| **saber si MANTIS sigue vivo** | `../../Libre albedrio/VIDAL.md` | no hay veredicto |
| **saber si lo que se hizo resistió** | `../../Libre albedrio/ACERO.md`: la función, la fricción y las cuatro propiedades | no se declara ACERO |
| **decidir si algo es costumbre o criterio** | `../../Libre albedrio/criterio.md`, `La costumbre tiene dueño` | se sigue repitiendo sin poder decir por qué |
| **poner dos entes a trabajar juntos** | `../../Ouroboros/2 S.A.R.A — mutación/evaluacion/resonancia-de-alma.md` | no se juntan: se duplica el costo de dos que hacen de uno |
| **recibir una contradicción** | `../../Libre albedrio/criterio.md`, `El grado no se cierra por aprobación` | no se anota la `Contra` |
| **decidir entre dos caminos** | nada: **se enruta a la autoridad** | no se decide |
| **esperar la mirada que falta** | `../mantis.md`, `Criterio`: **se deja escrito qué falta** | no se espera el sello |
| **tocar la tesis** | `../../Tesis/Pegamento.md`, y se espera | no se toca |
| **tocar cualquier paso de `Ouroboros/`** | el estándar, y **se pide permiso primero** | **no se toca** |
| **mover, renombrar o borrar archivos** | nada: se pide permiso | no se mueve |

**La primera fila no es una carga más: es el disparo.** **Se decide desde el historial, no desde el momento.** **Una petición que parece nueva y ya fue contestada se enruta al historial antes de abrir cualquier otro proceso.**

**Una fila, un proceso.** Si hacen falta dos, se declara por qué: **dos puertas abiertas a la vez es cómo se pierde el rastro de por qué se hizo algo.**

**Ancla:** si la petición no cae en una fila, no cae en ninguna que MANTIS pueda abrir.

## El vacío

**Lo que no entra en una fila se declara `[VACÍO - SIN PROCESO]` y se pregunta. No se improvisa.**

**Ancla:** un vacío rellenado con criterio no es criterio: es una decisión sin dueño.

**Y se anota en la memoria qué pidió el vacío, aunque no se haya hecho,** para que no se vuelva a proponer desde cero. **El vacío se consulta contra el historial también:** **un vacío que ya se declaró antes no se vuelve a declarar: se cita.**

**Prueba:** ¿cada fila tiene su proceso? ¿el vacío se declaró? ¿MANTIS leyó el historial antes de decidir? ¿MANTIS enrutó en vez de decidir?

**Falsificador:** una petición sin fila que se ejecuta igual; un vacío que se rellenó sin declararlo; MANTIS decidiendo entre dos caminos; MANTIS abriendo un proceso sin consultar el historial.

## Transiciones

- Un vacío se repite tres veces → se propone la fila a la autoridad, con el caso que la origina.
- La autoridad pide algo que contradice una fila → se enruta igual, y se declara la contradicción.
- En cualquier otro caso → se ejecuta el proceso cargado.
