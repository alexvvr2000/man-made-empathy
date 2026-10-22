# Proceso de verificar esquema

**Unidad:** proceso.
**Aplica a:** verificar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

El esquema de fila define los campos del registro y nadie los comprueba. Una base sin verificación es un formulario, no un registro.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el esquema documentado y la base `../../.contexto/memoria.db`.
- **Falla:** un campo del documento no existe en la base, o al revés; hay filas que violan una vista de error.
- **Sale:** la correspondencia columna a columna, o la lista de desviaciones.
- **Consume:** quien edita y quien usa los datos.

## Cómo se aplica

1. **Leer el esquema documentado.** Los campos de `../../corpus/esquema-de-fila.md`.
2. **Leer la tabla real.** `select name from pragma_table_info('fila')` sobre `.contexto/memoria.db`.
3. **Comparar.** Campo documentado sin columna = falta. Columna sin campo documentado = sobra.
4. **Correr las vistas de error.** `v_fila_sin_origen`, `v_fila_sin_descarte`, `v_criterio_tardio`. Toda fila que aparezca es una violación.
5. **Declarar.** La correspondencia completa, o la desviación con su corrección.

`Campos: [n doc | n base] | Faltan: [cuáles] | Sobran: [cuáles] | Filas en error: [n]`

## Prueba

¿Cada campo del esquema tiene columna? ¿Las tres vistas de error devuelven cero filas?

**Falsificador:** un campo documentado sin columna; una columna sin campo documentado; una fila sin origen, sin descarte o con criterio tardío que no se declara.

## Estado

El esquema se define en `../../corpus/esquema-de-fila.md`. La base vive en `../../.contexto/`. Si la base se corrompe, se reconstruye: el `.md` es la fuente.

## Transiciones

- Si hay desviaciones → `editar.md` corrige el esquema o la base.
- Si la base se perdió → se recrea con `.read memoria.sql` y se reconstruye parseando.
- En cualquier otro caso → se entrega y se cierra.
