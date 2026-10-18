---
name: deliberacion-estructurada
description: >-
  Úsala cuando haya dos o más caminos viables con fricción, costos contrapuestos
  o encuadres incompatibles, y la decisión final sea de la autoridad. No la uses
  si una sola rama sobrevive al recibo: declara dominancia y cierra. No la uses
  para medir hechos del entorno (usa indagacion-instrumental) ni para ejecutar el
  cambio elegido (usa entrega-operacion).
---

# Deliberación Estructurada

Compuertas numeradas. Prohibido ejecutar el Paso N+1 sin haber emitido la salida del Paso N. Una línea por ancla.

## Paso 0 — Patrones previos

Antes de admitir ramas, lee los patrones vigentes sobre el tema en el largo, por `tipo='patron'` y por el estado actual. Prohibido deliberar sin haber leído: lo ya cerrado no se reabre por olvido.

Emite las dos anclas juntas:

`Mem: leído | largo: 2 patrones por "cambio de proveedor" | ids 7, 9`

`Patrones: [N] | NINGUNO`

Un patrón entra como candidato con su `refuta` a la vista, nunca como evidencia. Si no declara qué observación lo rompería, se ignora.

`Patrón: [id] | Estabilidad: [probada|local] | Réplicas: [n]`

Un patrón `local` no arbitra: solo propone. Si cierra una rama, la deliberación está mal.

**Costo de omitir la lectura:** se delibera otra vez lo que ya estaba resuelto y la fila nueva contradice al patrón vigente sin `reemplaza`. El debate se paga dos veces y queda un registro que no sirve para decidir.

## Paso 1 — Admisión

Cada rama declara su forma antes de ser evaluada. Sin forma, no es rama.

`Rama: [nombre] | Fin: [estado final observable] | Horizonte: [corto|mediano|largo] | Tasa: [medida hoy] | Canal: [cómo se observa]`

`Techo: [recurso que la acota → límite]`

- Sin `Canal`: no entra. Emite `Hipótesis: [X] | Destino: indagacion-instrumental` y sigue sin ella.
- Sin `Techo`: no entra. Emite `Hipótesis: [X] | Techo: sin medir` y cárgala a `indagacion-instrumental` antes de admitirla. Proponer por encima del límite del medio no es una rama: es un deseo.
- Sin `Tasa`: el horizonte es inventado. No entra.
- `corto` = antes del siguiente punto de revisión. `largo` = después de que el desgaste sea irreversible en el recurso. Prohibido fijar semanas.
- Misma rama = mismo par `(Fin, Horizonte)`. Mismo fin, otro mecanismo: una rama; el mecanismo se decide en la ejecución. Mismo fin, otra velocidad: dos ramas.

## Paso 2 — Enumeración cerrada

Agrega siempre dos filas, ambas sujetas al Paso 1:

`No actuar` y `Rama huérfana: [opción que ninguna postura del mandante contiene]`.

Prohibido deliberar sobre el binario recibido.

`Ramas admisibles: [N] | Huérfana: [X | NINGUNA] | No actuar: incluida`

- N=1 → emite `Dominancia: [rama] | Recibo: [N1–N3]`. Entrega, cierra, encadena. Prohibido deliberar.
- N≥2 → Paso 3.

## Paso 3 — Bifurcación y eco

`Bifurcación: [A] ≠ [B] | Incompatibilidad: [punto exacto, no el tema]`

Si la incompatibilidad no se puede escribir: `Sin bifurcación: descripciones compatibles`. Entrega y cierra.

Por cada par cuyas pruebas puedan venir del mismo lugar:

`Premisa compartida: [P] | Falsaría a ambas: [observación] | Pruebas: [N]`

Sin observación falsante: `Pruebas: 1`, aunque haya diez fuentes.

Si todas las ramas coinciden en el fin, se declara `Saturación: local | Contraejemplo: [sí|no]` y se busca uno medible; si no aparece, se acota la validez del acuerdo.

Por cada rama que sobreviva, modela el contraargumento de mayor fricción:

`Contraargumento: [el más fuerte contra esta rama] | Falsaría: [observación que lo haría cierto]`

Si no existe evidencia contraria observable, se declara `Sin contraargumento observable`. Prohibido inventar objeciones.

## Paso 4 — Proyección y entrega

Por rama:

`Amplifica: [variable que acelera] | Contiene: [variable que frena] | Atractor: [estado si se la deja sola] | Clausura: [evento tras el cual no hay retorno]`

`Viabilidad: [alta|media|baja] | Mueve: [qué la sube o la baja]`

`Desgaste: [qué se degrada | tasa por ciclo | sin medir]`

`sin medir` se admite una vez; a la tercera aparición sin medición, se emite `Alerta`.

Tres columnas desacopladas, jamás mezcladas:

- `Datos: [N1–N2]`
- `Precedentes: [N3 con autor y condiciones]`
- `Criterio abierto: [preguntas]` — prohibido escribir los valores de la autoridad.

Entrega, en este orden:

1. Ramas con sus tres ejes y su clausura.
2. Un punto de incompatibilidad por par.
3. Pruebas independientes por par.
4. Contraargumento de mayor fricción por rama, con su falsador.
5. Preguntas abiertas.
6. `Por defecto si no hay decisión: [rama más reversible] | Costo de la demora: [medido]`
7. `Pendiente: [rama] | Bloqueo: [dato o decisión] | Cierre: [condición observable]`
8. `Incertidumbre residual: [variables pendientes]`
9. `Balance del espacio: [expandido | colapsado]`

**Registro del cierre:** cada línea `Pendiente:` se escribe en el largo como fila `pendiente`, con su `Cierre` como `disparador`, `autor` en `tipo:nombre` y `reemplaza` cuando sustituye a otra. El `id` devuelto se agrega a la propia línea y se emite el ancla: `Mem: guardado | largo id 14`. Si no se escribe, el pendiente desaparece al vaciar el corto y la deliberación se repite entera en la sesión siguiente.

## Prohibiciones

Tablas de pros y contras. Puntajes con pesos. Recomendación única. Cualquier síntesis que reduzca N sin recibo. Repetir un pendiente sin recibo nuevo: se re-evalúa solo cuando un recibo toca su condición de cierre. Escalar sin recibo: `Desafío` exige restricción medida y acuse antes de continuar la rama.

## Transiciones

- Una sola rama sobrevive → dominancia, cierra.
- Falta `canal` o `tasa` de la rama que decide la elección → `indagacion-instrumental`.
- Decisión tomada o dominancia con clase de reversibilidad → `entrega-operacion`.
