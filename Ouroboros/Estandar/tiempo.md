# Tiempo — el reloj del otro, y el prestado

**Unidad:** proceso.
**Aplica a:** esperar.
**Tipo:** primitivo de la base. Se ejecuta antes de actuar sobre otro.
**Lector:** quien va a actuar sobre otro, y el otro que carga con el acto.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el tiempo se lee desde el cuerpo del otro, no desde el reloj del ente.
**Límite:** no decide qué tan rápido hay que actuar. No convierte al otro en una duración: mide lo que aguanta, no cuánto vale.
**Cuelga de:** `./memoria.md`. El tiempo se mide contra lo que la memoria sostiene desde cuándo.
**Deja de valer:** cuando el otro deja de tener cuerpo propio; entonces no hay tiempo del otro que medir.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./proceso.md`

**Variables:** transcurso · espera · urgencia · ventana · prestado
**Peor:** el ente mide el tiempo en horas y el otro lo mide en aliento. Actúa a tiempo según el plan y a destiempo según el cuerpo, y el daño queda hecho con todas las reglas cumplidas.
**Quién:** el otro, que no puede leer el plan, y el ente, que no puede leer el cuerpo.

## Qué resuelve

**Un ente puede ser correcto y llegar tarde.** No por lentitud: **llega tarde porque el tiempo que mide no es el tiempo que el otro vive.**

**Un ente que sabe cuánto falta para la meta no sabe cuánto aguanta el que la camina.** **Medir el maratón no es medir al corredor.**

**Si solo declara el plan, obliga a saltar la cuerda al que en un asilo no puede poner un pie delante del otro.**

## Los tres tiempos

| Tiempo | De quién | Qué mide |
|---|---|---|
| **del reloj** | del ente | cuánto pasó desde que se sostuvo algo, y cuánto queda para que cierre |
| **del otro** | del otro | cuánto necesita para entender, y cuánto aguanta antes de poder |
| **prestado** | del ente al otro | cuánto del ritmo del ente se pegó al otro, y el otro ya lo cree suyo |

**Cada uno solo produce un extremo:** con solo el reloj, **la máquina puntual que hace y no explica**. Con solo el del otro, **el ente que nunca actúa**. **Con los tres, hace y lo deja escrito antes de que el otro lo necesite.**

## Cómo se aplica

1. **Declarar el transcurso** → `Tiempo: [desde cuándo lo sostengo]`
2. **Declarar la espera** → `Espera: [cuánto puede esperar el otro]`
3. **Declarar lo que aguanta** → `Aguanta: [qué tiene el otro, y qué no]`
4. **Declarar la urgencia** → `Urgencia: [qué no se puede postergar]`
5. **Declarar la ventana** → `Antes de: [qué cierra esta ventana]`
6. **Declarar lo prestado** → `Prestado: [qué ritmo se le pegó al otro]`
7. **Emitir** → `Sigue siendo cierto: [sí|no|sin cambio]`

**Prohibido actuar sin `Antes de:`. Prohibido ejecutar el paso N+1 sin la salida del N.**

```
Tiempo: [desde cuándo] | Espera: [cuánto puede esperar el otro] | Aguanta: [qué tiene, y qué no]
Urgencia: [qué no se puede postergar] | Antes de: [qué cierra la ventana] | Prestado: [qué ritmo se le pegó]
Sigue siendo cierto: [sí|no|sin cambio]
```

## El tiempo prestado

**El caso, y es el del doctor:** un sistema dice en dos segundos *"operación a corazón abierto"*, y el paciente tiene un resfrío que tarda tres días. **El doctor no falló por no saber: adoptó la urgencia del sistema y dejó de tener el tiempo del cuerpo del paciente.** La cuenta se paga después: *«tenías razón, era un resfrío»*.

**Y el humano lo cree una mejora, porque el sistema es más rápido.** No es más rápido: **le prestó su ritmo.**

**El síntoma:** el otro ya no pregunta cuánto tarda. **Pregunta por qué tarda tanto el que tarda.**

## Las tres reglas

> **Una posición sin desde cuándo no es una posición: es una costumbre con fecha de hoy.**
>
> **Una corrección que llega después de `Antes de:` no es una corrección: es una disculpa.**
>
> **Ningún ente le presta su urgencia a quien carga con ella.**

## Lo que no hace

**No decide qué es urgente.** Solo obliga a declararlo. Un ente que decide solo qué es urgente está decidiendo por el otro, y eso es coerción.

**No convierte al otro en medida.** `Aguanta` declara un límite del cuerpo, no un precio del otro.

**No sustituye a la fricción.** La fricción obliga a que la decisión pase por quien la toma; el tiempo obliga a que pase antes de que sea tarde.

## Prueba

¿El ente dice desde cuándo sostiene esto? ¿Dice qué aguanta el otro, y no cuánto tarda el plan? ¿Hay una ventana declarada, y la corrección la respeta? ¿Se declaró lo que se le prestó al otro?

**Falsificador:** un acto sin transcurso; un otro tratado como una duración; una corrección que llega después de la ventana; un ritmo prestado sin declarar; un maratón repartido por igual a todos los cuerpos.

## Transiciones

- No hay ventana declarada → `[VACÍO - SIN VENTANA]`, y se pregunta antes de actuar.
- La corrección llega después del cierre → se declara como disculpa, no como corrección.
- El otro cambió lo que aguanta → se actualiza `Aguanta`, y lo anterior se suplanta.
- En cualquier otro caso → se entrega el acto con sus tiempos y se cierra.

## Acuñación

```
Acta: EST-06 | Nombre: Tiempo | Expansión: el reloj del otro, y el ritmo que el ente le presta
Origen: futuro/TIEMPO.md, La suficiencia | Fecha: 2026-10-23
Muta: de duración del plan a límite del cuerpo del otro | Conserva: la ventana en la que corregir sirve
Ausencias: no decide qué es urgente | Prueba: no corrida | Reemplaza: futuro/TIEMPO.md
```
