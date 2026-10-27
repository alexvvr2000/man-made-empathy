# Proceso de auditar dependencia

**Variables:** operador · capacidad · revisión · reversión
**Peor:** el operador no puede explicar la solución sin leer la del sistema
**Quién:** el operador, que es quien puede decir que ya no puede solo

**Unidad:** proceso.
**Aplica a:** auditar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

El operador deja de poder hacer la tarea sin el sistema y no lo nota. La composición que lo ahorra es la misma que lo vuelve apéndice.

Estado del arte: dependencia de automatización.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** la composición y el operador que la usa.
- **Falla:** el operador no puede explicar la solución; no puede decidir qué es posible; no puede hacerlo sin el sistema.
- **Sale:** el estado de dependencia, con lo que se perdió.
- **Consume:** el operador, que decide si sigue.

## Cómo se aplica

1. **Test de reversión.** Hacer la tarea sin el sistema. ¿Empeoró tanto que ya no se puede? Entonces hay sobredependencia.
2. **Test de explicación.** ¿Se puede explicar la solución sin el colaborador? Si no, se está alquilando, no entendiendo.
3. **Test de soberanía.** ¿El colaborador decide qué es posible, o el operador? Si decide el colaborador, el timón cambió de manos.
4. **Test de transferencia inversa.** ¿Lo aprendido se aplica sin el colaborador? Si no, el talento se quedó en él.
5. **Declarar la pérdida.** Qué capacidad del operador se atrofió y con qué práctica se recupera.

`Reversión: [se puede|no] | Explica: [sí|no] | Decide: [operador|colaborador] | Transfiere: [sí|no] | Atrofiado: [qué]`

## Prueba

¿Los cuatro tests se corrieron? ¿La capacidad perdida se declara con su forma de recuperarla?

**Falsificador:** la tarea ya no se puede hacer sin el sistema y no se declara; el operador explica la solución leyendo la del colaborador; el colaborador decide qué es posible; la capacidad atrofiada no se nombra.

## Transiciones

- Si hay sobredependencia → se declara y se fuerza práctica manual periódica.
- Si la composición perjudica a una escala → `armonizar.md`.
- En cualquier otro caso → se entrega y se cierra.

> El que mantiene la capacidad y no la usa no es pasivo: está eligiendo.

