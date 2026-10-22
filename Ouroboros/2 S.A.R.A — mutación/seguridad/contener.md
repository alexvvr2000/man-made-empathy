# Proceso de contener

**Variables:** perímetro · irreversibilidad · autorización · retorno
**Peor:** lo irreversible se hace sin autorización ni punto de retorno
**Quién:** quien sufre lo irreversible, que no autorizó

**Unidad:** proceso/
**Aplica a:** contener/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un acto altera el entorno y no hay forma de deshacerlo/ Este proceso fija el perímetro y bloquea lo irreversible sin autorización/

Práctica de industria: seguridad, menor privilegio, reversibilidad/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el acto y el entorno que va a cambiar/
- **Falla:** se actúa fuera del perímetro; irreversible sin punto de control/
- **Sale:** el acto ejecutado con su recibo, o el bloqueo declarado/
- **Consume:** quien opera/

## Cómo se aplica

1/ **Declarar el perímetro/** Qué puede tocarse y qué no/ Lo que no se delega, no se toca/
2/ **Clasificar el retorno/** `reversible | compensable | irreversible`, con su mecanismo/
3/ **Punto de control/** Antes de lo irreversible: impacto, respaldo verificado, reversión o su ausencia, validación de la autoridad, precedente o vacío/ Si falta uno, se bloquea/
4/ **Ejecutar un acto a la vez/** Con su ancla/
5/ **Registrar por canal distinto/** Sin recibo, el acto no ocurrió/

`Cambio: [recurso] | Clase: [reversible|compensable|irreversible] | Retorno: [mecanismo] | Perímetro: [sí|no] | Recibo: [id]`

## Prueba

¿La clase y el retorno se declararon antes? ¿Lo irreversible pasó el punto de control?

**Falsificador:** acto fuera del perímetro; irreversible sin punto de control; recibo del mismo canal que ejecutó/

## Transiciones

- Si es irreversible → se detiene y se pide autorización/
- Si el acto cambió algo que servía → `///evaluacion/probar-regresion/md`/
- En cualquier otro caso → se entrega y se cierra/
