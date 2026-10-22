# Proceso de acotar costo

**Variables:** efecto · coste · techo · cierre
**Peor:** se mide el efecto sin techo y el gasto aparece cuando ya se comprometió
**Quién:** quien paga el techo, o `ninguno` si no hay techo

**Unidad:** proceso/
**Aplica a:** acotar/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un resultado cuesta más de lo que sirve y nadie lo midió/ Este proceso pone el techo antes y lo mide después/

Práctica de industria: economía de cómputo y presupuesto de inferencia/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el resultado y lo que costó obtenerlo/
- **Falla:** el costo supera el beneficio y no se declara/
- **Sale:** el costo con su techo y su veredicto/
- **Consume:** quien paga/

## Cómo se aplica

1/ **Fijar el techo antes/** Cuánto se está dispuesto a gastar/
2/ **Medir el efecto/** Qué cambió con el resultado/
3/ **Comparar/** El efecto contra el costo/
4/ **Declarar/** Sirve, no sirve, o empatan/

`Techo: [límite] | Costo: [medido] | Efecto: [qué cambió] | Veredicto: [sirve|no sirve|empata]`

## Prueba

¿El techo se fijó antes? ¿El efecto se midió?

**Falsificador:** se mide el costo después de gastarlo; el efecto no se mide; el techo se ajusta al resultado/

## Transiciones

- Si no sirve → se para y se declara/
- En cualquier otro caso → se entrega y se cierra/
