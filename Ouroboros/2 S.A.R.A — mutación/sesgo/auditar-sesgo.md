# Proceso de auditar sesgo

**Variables:** datos · etiqueta · uso · bucle
**Peor:** se califica por quién produjo y no por lo que produjo
**Quién:** el grupo sobrerrepresentado o ausente

**Unidad:** proceso/
**Aplica a:** auditar/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

El prejuicio no entra porque un proceso lo decida: entra por los datos, por cómo se etiquetan y por el uso no previsto/ Este proceso lo declara antes de que se propague/

Estado del arte: sesgo algorítmico, auditoría de equidad/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el resultado y los datos, etiquetas y contexto de uso/
- **Falla:** se califica por categoría y no por desempeño; el sesgo no se declara/
- **Sale:** el sesgo declarado, con su origen y su alcance/
- **Consume:** quien decide si el resultado entra/

## Cómo se aplica

1/ **Declarar el sesgo de datos/** Qué categorías están sobrerrepresentadas o ausentes en lo que se usó/
2/ **Declarar el sesgo de etiqueta/** Qué se tomó como verdad y quién lo decidió/
3/ **Declarar el sesgo de uso/** En qué contexto se aplica y para quién no se diseñó/
4/ **Probar la calificación/** ¿Se juzga por lo que produce o por quién lo produjo? Solo lo primero/
5/ **Declarar el bucle/** Si el resultado se usará para decidir sobre más datos, qué refuerza/

`Datos: [qué categoría domina o falta] | Etiqueta: [quién la decidió] | Uso: [contexto no previsto] | Calificación por: [resultado|autor]`

## Prueba

¿El sesgo está declarado en sus tres fuentes? ¿La calificación es por desempeño?

**Falsificador:** se califica por quién produjo; una categoría ausente no se declara; el uso no previsto no se nombra; el bucle refuerza lo mismo que ya había/

## Transiciones

- Si el sesgo no se puede declarar → `[VACÍO - SIN AUDITORÍA]`/
- Si el bucle refuerza → `///evaluacion/vigilar-tendencias/md`/
- En cualquier otro caso → se entrega y se cierra/
