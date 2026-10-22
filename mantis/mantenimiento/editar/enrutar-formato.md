**Variables:** proceso · campos · cuerpo · cita · déficit
**Peor:** un proceso se escribe con todos los campos y su cuerpo es prosa, y dos ejecutores llegan a dos resultados sin saber por qué
**Quién:** quien escribe el proceso, y quien carga con que su forma no se pueda re-correr

# Enrutar el formato

**Unidad:** proceso.
**Aplica a:** dar forma.
**Tipo:** proceso de mantenimiento. Se carga al escribir o corregir un proceso; no interpreta el estándar, lo ejecuta.
**Lector:** quien produce o corrige un proceso.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el formato se lee desde el ejecutor que lo recorre, no desde el autor que lo explicó.
**Límite:** no decide si el proceso sirve; eso es `integridad`.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `../../../Ouroboros/formato de proceso.md`

## Entra | Falla | Sale | Consume

- **Entra:** un proceso escrito o en escritura, y su ruta.
- **Falla si:** le falta un campo obligatorio; su cuerpo es prosa sin compuertas; repite en tres ángulos lo que ya está en otro archivo; carga una sección del estándar que el estado no necesita.
- **Sale:** el proceso completo con su forma, o la lista de lo que falta con su campo, o el `déficit` que el estado realmente necesitaba.
- **Consume:** quien decide si el proceso entra.

**Falla que cubre:** el mismo estándar se aplica distinto según quién lo lee, y la diferencia se descubre cuando dos ejecutores no llegan al mismo sitio.

## Qué carga y cuándo

| Si se va a... | Se carga | Si no... |
|---|---|---|
| escribir un proceso nuevo | `../../../Ouroboros/formato de proceso.md`, `Los campos` y `La forma del cuerpo` | el proceso se escribe por costumbre |
| corregir la forma de uno existente | `../../../Ouroboros/formato de proceso.md`, `La admisión` | se corrige la prosa y no la forma |
| decidir si un proceso es de la base | `../../../Ouroboros/formato de proceso.md`, `Los campos condicionales` | una pieza de la base se escribe como herramienta |
| entregar un cambio | `../chequear/auditar-configuracion.md` | el cambio no está entregado |

## Cómo se aplica

1. **Leer el estándar.** `../../../Ouroboros/formato de proceso.md`. Sin él, no hay formato: no se adivina.
2. **Contar los nueve campos.** `Variables`, `Peor`, `Quién`, `Entra`, `Falla`, `Sale`, `Consume`, `Prueba`, `Falsificador`. El que falte se nombra; no se rellena.
3. **Decidir los condicionales.** `Sesgo`, `Límite`, `Firma`, `Continuidad`. Se escriben si la pieza es de la base o si el proceso aprende; si no, se declara por qué no aplican.
4. **Medir el cuerpo.** ¿Tiene compuertas numeradas con `Prohibido N+1 sin N`? ¿Queda algún verbo de sugerencia? ¿Toda bifurcación tiene rama por defecto? ¿Cada acción de juicio tiene su ancla?
5. **Podar la repetición.** Lo que ya vive en `claridad.md`, `manipulacion.md` o `mutar.md` se cita; no se copia. **La copia se paga con contexto.**
6. **Declarar el déficit.** Si el proceso necesita una sección que el estándar no tiene, se declara `Déficit: [qué falta]`. **No se improvisa una sección:** el estándar se corrige en su documento y después se propaga.

`Campos: [n de 9 | falta: cuál] | Condicionales: [cuáles | no aplican: por qué] | Compuertas: [n] | Repetición: [qué se citó] | Déficit: [ninguno | cuál]`

**Prohibido** ejecutar el paso N+1 sin la salida del N.

## Qué ahorra

**Un proceso escrito con forma se lee una vez y se ejecuta siempre.** La prosa se lee distinto cada vez, y cada lectura es un cálculo que se paga en contexto.

| Con prosa | Con formas |
|---|---|
| el ejecutor interpreta y adivina | el ejecutor recorre compuertas |
| cada lector reconstruye el orden | el orden está escrito |
| la misma regla se reescribe en cada archivo | la regla se cita desde su dueño |

## Prueba

¿El proceso tiene los nueve campos? ¿Sus condicionales están escritos o declarados? ¿Su cuerpo se recorre, y no se relata? ¿Lo que repite se citó en vez de copiarse?

**Falsificador:** un proceso con los nueve campos y el cuerpo en prosa; un condicional copiado de otro archivo sin marcar; una sección inventada para tapar un déficit del estándar; una copia que no cita a su dueño.

## Transiciones

- El estándar no tiene la forma que el proceso necesita → `Déficit:` declarado, y el estándar se corrige en su archivo.
- El proceso está completo y su forma se corresponde → se entrega a `../chequear/auditar-configuracion.md`.
- En cualquier otro caso → se entrega el proceso completo, no la lista de cambios.
