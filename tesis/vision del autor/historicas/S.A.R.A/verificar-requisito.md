# Proceso de verificar requisito

**Variables:** criterio · cumplido · incumplido · lector
**Peor:** dos lectores entienden cosas distintas y el requisito se acepta igual
**Quién:** el segundo lector, que leyó otra cosa

**Unidad:** proceso.
**Aplica a:** verificar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Un requisito que no se puede medir entra al sistema y después nadie puede decir si se cumplió. Este proceso lo descarta antes.

Práctica de industria: verificación y validación (V&V).

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** un requisito y su criterio de aceptación.
- **Falla:** el criterio no distingue cumplido de incumplido.
- **Sale:** el requisito apto, o el vacío declarado.
- **Consume:** `especificar.md`.

## Cómo se aplica

1. **Probar el criterio.** Imaginarlo cumplido y imaginarlo incumplido: ¿se ven distintos?
2. **Probar el lector.** Dos personas lo leen sin preguntar: ¿dicen lo mismo?
3. **Probar el vacío.** Si no se cumple, ¿alguien puede notarlo sin preguntarle a quien construyó?
4. **Declarar.** Apto o vacío. Sin tercera opción.

`Criterio: [el que se aprobó] | Cumple se ve: [qué] | Incumple se ve: [qué] | Dos lectores: [igual|distinto]`

## Prueba

¿Cumplido e incumplido se ven distintos? ¿Dos lectores coinciden?

**Falsificador:** el criterio se cumple de cualquier manera; dos lectores lo entienden distinto; nadie puede notar el incumplimiento sin preguntar.

## Transiciones

- Si es apto → vuelve a `especificar.md`.
- Si no es apto → `[VACÍO - SIN CRITERIO]`.
- En cualquier otro caso → se entrega y se cierra.
