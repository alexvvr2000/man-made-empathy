# Proceso de conceptualizar

**Variables:** término · origen · sinónimo · colisión
**Peor:** el término se usa sin fila y después no se sabe de dónde vino
**Quién:** quien lee el término y no encuentra su origen

**Unidad:** proceso.
**Aplica a:** conceptualizar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Un término nuevo aparece y sin origen el vocabulario crece sin rastro. Este proceso le da fila antes de usarlo.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el término y el proceso donde apareció.
- **Falla:** el término se usa sin fila; dos nombres para el mismo concepto.
- **Sale:** la fila en `../../Conceptos.md` con su origen y su relación.
- **Consume:** quien usa el término después.

## Cómo se aplica

1. **Buscar.** ¿Ya existe con ese nombre, o con otro y el mismo significado?
2. **Clasificar.** Nuevo, derivado o duplicado.
3. **Escribir la fila.** Con `Nace en`, `Bajó de`, sinónimos, calificador, más amplio y más estrecho.
4. **Verificar colisión.** Ningún otro concepto usa ese nombre como preferido.
5. **Declarar el uso.** En qué proceso se usa.

`Concepto: [nombre] | Nace en: [proceso] | Nuevo: [sí|no] | Sinónimos: [...] | Manda: [cuál] | Colisión: [ninguna|id]`

## Prueba

¿La fila tiene origen? ¿Hay un solo nombre preferido?

**Falsificador:** término en uso sin fila; dos filas con el mismo nombre preferido; concepto nuevo sin `Nace en`.

## Transiciones

- Si el concepto es un proceso nuevo → `../../Proceso PROMETEA.md`.
- En cualquier otro caso → se entrega y se cierra.
