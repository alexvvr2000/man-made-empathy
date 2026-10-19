---
name: wax
description: >-
  Úsala para crear un agente nuevo a partir de SARA, o para mutar sus componentes
  (AGENTS.md, skills, esquemas y acta). No la uses para operar un agente ya nacido
  (usa indagacion-instrumental, deliberacion-estructurada o entrega-operacion) ni
  para coordinar una camada que ya existe.
---

# WAX — Workshop for Autonomous eXperiments

**Lector:** máquina (arnés). El acta y el paquete declaran su lector: humano para decisión, máquina para transferencia.

WAX no crea de cero: copia la semilla y la moldea.

Compuertas numeradas. Prohibido ejecutar el Paso N+1 sin la salida del Paso N. Una línea por ancla.

## Compuerta de decisión

Antes de copiar la semilla, se responde: **¿esto cambia lo que el agente puede hacer o solo lo que debe hacer ahora?**

`WAX: cambio=[puede|debe] | uso=[una vez|recurrente] | prueba=[arranque|amnesia|no corrida]`

La etiqueta de la mutación —agente, instrucción o skill— se decide en `./Bases de diseño/Reglas de mutación.md`; WAX crea el agente.

- `puede` + recurrente + `prueba=arranque|amnesia` → se sigue al Paso 0; queda como mutación.
- `puede` + recurrente + `prueba=no corrida` → WAX solo con acta `no probada`; si no se acepta, `instruccion-de-autoridad`.
- `puede` + una vez → no se copia la semilla: `instruccion-de-autoridad` con un delta; se cierra.
- `debe` + recurrente → `instruccion-de-autoridad`; el agente no cambia.
- `debe` + una vez → se responde y se cierra; si el encargo pide formato, instrucción.

**Test:** `Cualquier agente con el mismo mandato puede hacerla → instrucción | El cambio se usa una vez → no amortiza la mutación | No hay prueba de arranque o amnesia → no se entrega la mutación`.

## Paso 0 — Origen

`WAX: origen=[semilla|padre|agente:<nombre>] | ruta=[sara/ | <nombre>/]`

- Sin `origen` declarado rige `semilla`: SARA queda como defecto, y el defecto se escribe en el ancla.
- `semilla`: nace del genotipo original. Hermanos consistentes.
- `padre`: nace del agente que ejecuta. Linaje, con las mutaciones acumuladas.
- `agente:<nombre>`: nace de otro agente ya nacido. Se copia ese genotipo y se moldea igual.
- Prohibido editar la fuente, sea `sara/` u otro agente.

## Paso 1 — Encargo y nombre

El encargo se recibe en llano y se transcribe sin interpretarlo: «solo quiero que haga esto» fija el fin, no una sugerencia.

`WAX: encargo="[frase exacta]" | fin=[estado final observable]`

Sin nombre dado, se proponen tres acrónimos **con significado** que se lean como nombre propio: derivados de la tarea si la hay, al azar si no. En el texto llevan puntos (`A.P.R.I.L.`); en la carpeta no (`april/`). Y se espera.

```
Nombres: [A] | [B] | [C]
```

- Colisión con carpeta existente → sufijo numérico. Prohibido sobrescribir.
- Sin respuesta → rige el primero.
- El nombre se decide antes de crear la carpeta: queda como la dirección del agente.

## Paso 2 — Mutación declarada

Se declara qué cambia y qué no. Lo no declarado se hereda intacto.

`WAX: muta=[AGENTS.md, skills/x, esquema] | intacto=[resto] | motivo=[por qué cada uno]`

- Encargo estrecho → mutación mínima: propósito y la skill que lo ejecuta. Todo lo demás se hereda, memoria incluida.
- Sin límite de alcance: puede quitar la memoria, cambiar el motor, borrar skills, agregar otras, reescribir la verificación. Nada está prohibido por diseño.
- Tres inclusiones obligatorias: acta de nacimiento, ausencia declarada y prueba corrida o declarada no corrida.

## Paso 3 — Plan, acta y formato

El plan contiene el artefacto del parto: archivos destino y contenido exacto de cada mutación. El acta viaja dentro del plan; no se escribe aparte.

`WAX: plan=[n archivos] | acta=ACTA.md | sin_resolver=[...]`

El acta lleva: nombre y su expansión, origen, fecha, encargo, mutado, intacto, ausencias declaradas y `prueba: pendiente`. Es un documento del agente, no una fila de la memoria.

Cerrado el plan, se abre la pregunta:

> ¿Quieres el agente en crudo, un ejecutable para DSH, o algún otro formato?

`WAX: formato=[crudo|dsh|otro:<nombre>]`

- **Crudo:** el árbol de fuentes tal cual —`AGENTS.md`, skills, esquemas—. Portable y sin dependencias.
- **DSH:** empaquetado para arrancar: `AGENTS.md` en la raíz, `skills/<nombre>/SKILL.md`, y el perfil con sus bundles.
- **Otro:** se declara el formato; si no hay empaquetador conocido, se entrega crudo y se dice por qué.

Sin respuesta rige `crudo`. El formato no cambia el contenido: cambia el envoltorio.

## Paso 4 — Ejecución por la puerta de operación

`Si el plan crea o altera estado persistente → entrega-operacion`, que clasifica reversibilidad, aplica y firma. WAX no escribe el entorno por su cuenta.

`WAX: entregado=[ruta] | recibo=[id o postcondición]`

## Paso 5 — Prueba y veredicto

WAX verifica; el mutante no tiene voto.

- Arranque: apertura, lectura de memoria o declaración de ausencia.
- Ausencias: si no hay motor o no hay memoria, se declara en la primera emisión.
- Amnesia, cuando haya memoria: cerrada una tarea, una sesión nueva reconstruye la decisión desde el cierre.

```
WAX: prueba=[arranque|amnesia|no corrida] | veredicto=[entrega|no entrega|entrega no probada]
```

`Con ausencias declaradas y arranque → entrega | Sin ausencias declaradas → no se entrega | Sin prueba → entrega marcada no probada y el acta lo dice`

El veredicto se escribe en el acta antes de devolver el control.

**Consecuencia de omitirlo:** el mutante arranca aparentando memoria y el fallo aparece cuando alguien confía en un recuerdo que no existe. Por eso el veredicto se escribe antes de devolver el control, no después.

## Encargos

Un encargo se resuelve con tres decisiones, no con un catálogo:

1. **Origen** — de dónde se copia: `semilla` (defecto), `padre` o `agente:<nombre>`.
2. **Alcance** — qué se declara mutado. Lo no declarado se hereda; sin declaración, la mutación se reduce a nombre y ruta.
3. **Nombre** — si se da, ese. Si no, un acrónimo **con significado** que se lea como nombre propio: derivado de la tarea si la hay, al azar si no. Con puntos en el texto, sin puntos en la carpeta. Colisión → sufijo.

De esas tres salen todos los encargos sin enumerarlos: clonar, renombrar, cambiar de perfil, quitar un componente, parir una camada. **El defecto no arranca en blanco: parte del origen con la mutación mínima.**

## Prohibiciones

Editar `sara/`. Entregar sin acta. Entregar un mutante que no declare su ausencia. Afirmar que la mutación preserva algo que no se probó. Elegir nombre sin haber propuesto tres.

## Falsificadores

- Se edita la fuente (`sara/` u otro agente) en lugar de copiarla; el origen se corrompió.
- Se entrega sin acta, o el acta no declara las ausencias; el mutante no es auditable.
- Se elige nombre sin proponer tres; la decisión se tomó sin alternativa.
- El veredicto se escribe después de devolver el control; el mutante ya arrancó sin prueba.
- Se declara una mutación que no se probó; la afirmación de preservación no tiene recibo.

## Transiciones

- Encargo ambiguo o decisión de valor → pregunta de calibración a la autoridad.
- Dos mutaciones con costos contrapuestos → `deliberacion-estructurada`.
- Falta un hecho de la semilla o del entorno → `indagacion-instrumental`.
- Plan listo para escribir → `entrega-operacion`.
- En cualquier otro caso → se entrega y se cierra.
