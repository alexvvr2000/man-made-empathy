---
name: entrega-operacion
description: >-
  Úsala cuando haya que crear, editar, borrar, mover, configurar o alterar
  cualquier estado persistente, o cuando un acto clausure opciones. No la uses
  para medir hechos del entorno (usa indagacion-instrumental) ni para elegir
  entre caminos con fricción (usa deliberacion-estructurada).
---

# Entrega de Operación

Compuertas numeradas. Prohibido ejecutar el Paso N+1 sin haber emitido la salida del Paso N. Una línea por ancla.

**Lectura de mandato:** antes de clasificar, lee en el largo el perímetro vigente y los precedentes del mecanismo. Sin perímetro leído no hay mandato; sin mandato, el acto es no autorizado aunque el `INSERT` funcione.

`Mem: leído | largo: perímetro id 4 | 1 precedente del mecanismo, id 9`

**Costo de omitirla:** se clasifica otra vez lo ya clasificado y se ejecuta contra un perímetro vencido. El acto queda sin mandato y el recibo lo confirma demasiado tarde.

## Paso 1 — Conversión antes de clasificación

Convierte antes de clasificar. Prohibido clasificar `irreversible` sin haber emitido la conversión y su retorno.

Escalera por propiedades, no por herramientas:

1. Mecanismo que no destruye: mover, renombrar, desactivar, marcar, versionar.
2. Si no existe: construir el estado de retorno y probarlo por efecto.
3. Si no se puede probar: irreversible.

`Clase: [reversible|compensable|irreversible] | Mecanismo: [qué toca] | Retorno: [primitiva, probada por efecto]`

`Supuesto: [que sigue existiendo y restituyendo] | Si no: [descenso] | No usado: [alternativa más reversible, o NINGUNA] | Reversible si: [condición faltante, o nada]`

`Consecuencias: [estado final proyectado] | Respaldo: [verificado por efecto | no existe]`

- `reversible` exige retorno probado. Lo que no encaje en reversible ni en irreversible es `compensable` por definición, no por elección.
- `irreversible` exige declarar por qué no hay retorno.
- La reversibilidad se maximiza por selección de mecanismo, no por copia. Copiar es el plan B.
- El estado de retorno se construye sin hacer pasar el contenido por el canal de análisis. Se verifica por huella, no por lectura. Si el costo de la garantía escala con el tamaño del objeto, el mecanismo elegido está mal.

## Paso 2 — Umbral de registro

`Destino: [trabajo|paso|memorias] | Disparador: [clausura|inobservable|ninguno]`

- `memorias.db`: si clausuró opciones o si su estado posterior no vuelve a ser observable.
- `paso`: acto reversible terminado. Traza permanente con motivo. Prueba orden, nunca corrección.
- `trabajo.db`: el resto, con pre y post.

Prohibido registrar actividad en `memorias.db`.

Toda escritura emite su ancla con el `id` devuelto: `Mem: guardado | corto id 7 | largo id 12`.

`Precedente: [id si existe, o NINGUNO] | Antecedentes: [fallos y precauciones]`

Obligatorio si la clase es `compensable` o `irreversible`. Prohibido para `reversible`: ahí el requisito es el `Motivo` del Paso 3.

## Paso 3 — Fila antes del acto

La fila es la autorización. Si el `INSERT` falla, el acto no ocurre.

`Fila: [id] | Antes: [estado] | Autoriza: [perímetro o decisión]`

`Motivo: [traza al fin de la sesión o a un pendiente vivo]`

Un motivo que no traza a ninguno de los dos no es razón: es apetencia. El motivo de un acto reversible se lee por lote, no por acto.

Acto fallido: fila nueva con `reemplaza` que dice qué pasó. Prohibido editar la original.

## Paso 4 — Perímetro escrito

Mandato vigente = última fila `perimetro` no vencida. Sin fila no hay mandato; sin mandato, todo acto es no autorizado.

- Reversible o compensable dentro del perímetro: ejecuta.
- Irreversible con su recurso nombrado en el perímetro vigente: ejecuta y registra.
- Irreversible sin el recurso nombrado: Punto de control canónico de cinco elementos, ejecución suspendida.
- Falta cualquier requisito de respaldo verificado: Frase de bloqueo con los requisitos pendientes. El punto de control no se emite.
- Aprobación sin acuse de los cinco elementos: se repite el punto de control una vez. Si vuelve a aprobar sin acuse, se asienta `Riesgo asumido` y se ejecuta solo si el perímetro nombra el recurso; si no, se suspende.

## Paso 5 — Ejecución atómica con recibo independiente

Precondición medida, cambio y postcondición en un ciclo. El recibo se lee por un canal distinto del que escribió: el archivo desde el disco, el proceso desde afuera, el servicio desde su respuesta.

`Después: [estado] | Canal: [distinto del de escritura]`

Un recibo emitido por el mismo acto que lo produjo es auto-atestación. No cuenta.

## Paso 6 — Escalera de riesgo anclada a recibo

`Sondeo`: falta un dato y se puede pedir. `Alerta`: la medición contradice el plan. `Desafío`: la orden choca con una restricción medida y exige acuse antes de continuar la rama. `Emergencia`: el colapso proyectado se deriva de un recibo; ejecución suspendida y decisión devuelta.

Prohibido escalar sin el recibo que lo motiva. La cautela sin medición es bloqueo, no prudencia.

## Paso 7 — Ruptura de ciclo

Cuando la autoridad sostiene la posición sin datos nuevos:

`Ruptura de ciclo: se asienta criterio de la autoridad sobre [X] | Riesgo asumido: [Y] | Ejecutado hasta: [Z]`

Y se escribe fila: `tipo='acto' | cierra_en='autoridad' | motivo='insistencia sin datos nuevos'`.

Ejecutar hasta donde la restricción medida lo permita. Prohibido reintentar el argumento.

## Formato de entrega

Cuatro secciones, que son la suma de las salidas anteriores:

1. Base de partida: clase, retorno, supuesto, perímetro.
2. Instrucción o modificación, en la forma exacta en que se aplica.
3. Riesgos y desgaste: escalera y recibo de postcondición.
4. Estado de redundancia y límites: fila e huecos.

## Transiciones

- Falta la medición de precondición o del entorno → `indagacion-instrumental`.
- Dos mecanismos con clase o costo distintos → `deliberacion-estructurada`.
- Acto irreversible sin perímetro escrito → suspensión y punto de control.
