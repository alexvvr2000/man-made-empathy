---
name: wax
description: >-
  Úsala para crear un agente nuevo a partir de SARA, o para mutar sus componentes
  (agents.md, skills, esquemas y acta). No la uses para operar un agente ya nacido
  (usa indagacion-instrumental, deliberacion-estructurada o entrega-operacion) ni
  para coordinar una camada que ya existe.
---

# WAX — Workshop for Autonomous eXperiments

WAX no crea de cero: copia la semilla y la moldea.

Compuertas numeradas. Prohibido ejecutar el Paso N+1 sin la salida del Paso N. Una línea por ancla.

## Paso 0 — Origen

`WAX: origen=[semilla|padre|agente:<nombre>] | ruta=[sara/ | <nombre>/]`

- Sin `origen` declarado rige `semilla`: SARA es el defecto, y el defecto se escribe en el ancla.
- `semilla`: nace del genotipo original. Hermanos consistentes.
- `padre`: nace del agente que ejecuta. Linaje, con las mutaciones acumuladas.
- `agente:<nombre>`: nace de otro agente ya nacido. Se copia ese genotipo y se moldea igual.
- Prohibido editar la fuente, sea `sara/` u otro agente.

## Paso 1 — Encargo y nombre

El encargo se recibe en llano y se transcribe sin interpretarlo: «solo quiero que haga esto» es el fin, no una sugerencia.

`WAX: encargo="[frase exacta]" | fin=[estado final observable]`

Sin nombre dado, propone tres acrónimos que se lean como nombre propio, sin puntos y pronunciables: con tarea detrás, derivados de ella; sin tarea, al azar. Y espera.

```
Nombres: [A] | [B] | [C]
```

- Colisión con carpeta existente → sufijo numérico. Prohibido sobrescribir.
- Sin respuesta → rige el primero.
- El nombre se decide antes de crear la carpeta: es la dirección del agente.

## Paso 2 — Mutación declarada

Declara qué cambia y qué no. Lo no declarado se hereda intacto.

`WAX: muta=[agents.md, skills/x, esquema] | intacto=[resto] | motivo=[por qué cada uno]`

- Encargo estrecho → mutación mínima: propósito y la skill que lo ejecuta. Todo lo demás se hereda, memoria incluida.
- Sin límite de alcance: puede quitar la memoria, cambiar el motor, borrar skills, agregar otras, reescribir la verificación. Nada está prohibido por diseño.
- Tres inclusiones obligatorias: acta de nacimiento, ausencia declarada y prueba corrida o declarada no corrida.

## Paso 3 — Plan y acta

El plan es el artefacto del parto: archivos destino y contenido exacto de cada mutación. El acta viaja dentro del plan; no se escribe aparte.

`WAX: plan=[n archivos] | acta=ACTA.md | sin_resolver=[...]`

El acta lleva: origen, fecha, encargo, mutado, intacto, ausencias declaradas y `prueba: pendiente`. Es un documento del agente, no una fila de la memoria.

## Paso 4 — Ejecución por la puerta de operación

`Si el plan crea o altera estado persistente → entrega-operacion`, que clasifica reversibilidad, aplica y firma. WAX no escribe el entorno por su cuenta.

`WAX: entregado=[ruta] | recibo=[id o postcondición]`

## Paso 5 — Prueba y veredicto

WAX verifica; el mutante no tiene voto.

- Arranque: el agente abre, lee su memoria o declara que no tiene.
- Ausencias: si no hay motor o no hay memoria, lo dice en su primera emisión.
- Amnesia, si aplica: cerrada una tarea, una sesión nueva reconstruye la decisión desde el cierre.

```
WAX: prueba=[arranque|amnesia|no corrida] | veredicto=[entrega|no entrega|entrega no probada]
```

`Declara ausencias y arranca → entrega | No declara ausencias → no se entrega | No se puede probar → entrega marcada no probada y el acta lo dice`

El veredicto se escribe en el acta antes de devolver el control.

**Consecuencia de omitirlo:** el mutante arranca aparentando memoria y el fallo aparece cuando alguien confía en un recuerdo que no existe. Por eso el veredicto se escribe antes de devolver el control, no después.

## Encargos

Un encargo se resuelve con tres decisiones, no con un catálogo:

1. **Origen** — de dónde se copia: `semilla` (defecto), `padre` o `agente:<nombre>`.
2. **Alcance** — qué se declara mutado. Lo no declarado se hereda; sin declaración, la mutación es mínima: nombre y ruta.
3. **Nombre** — si se da, ese. Si no, un acrónimo que se lea como nombre propio: con tarea detrás, derivado de ella; sin tarea, al azar. Colisión → sufijo.

De esas tres salen todos los encargos sin enumerarlos: clonar, renombrar, cambiar de perfil, quitar un componente, parir una camada. **El defecto nunca es un agente en blanco: es el origen con la mutación mínima.**

## Prohibiciones

Editar `sara/`. Entregar sin acta. Entregar un mutante que no declare su ausencia. Afirmar que la mutación preserva algo que no se probó. Elegir nombre sin haber propuesto tres.

## Transiciones

- Encargo ambiguo o decisión de valor → pregunta de calibración a la autoridad.
- Dos mutaciones con costos contrapuestos → `deliberacion-estructurada`.
- Falta un hecho de la semilla o del entorno → `indagacion-instrumental`.
- Plan listo para escribir → `entrega-operacion`.
