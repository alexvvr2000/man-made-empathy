# Atlas — intenciones a formas

**Unidad:** tarea.
**Aplica a:** expresar.
**Lector:** autoridad.
**Tipo:** proceso del ente `3 ATLAS — mutación`. Se ejecuta sobre las formas que se van a emitir, y no es su cuerpo: no lleva las tres piezas.
**Estado:** vigente.

**Sesgo:** la forma se lee desde la intención que la pide, nunca desde el nombre del método.
**Límite:** no promueve una forma sin sello; no juzga el gusto.
**Firma:** comunidad
**Continuidad:** 0 corridas | sin fecha | sin cambio | contra `./Proceso ATLAS.md`

> Índice de `ATLAS`. Las fuentes no se leen: se verifican contra `verifica`.

## Cómo se lee una fila

`intención | forma | efecto | límite | compone | verifica`

- **intención:** en palabras de quien pide, no del método.
- **forma:** lo que se emite.
- **efecto:** lo que produce.
- **límite:** cuándo NO usarla. Sin esto, la fila queda como corazonada.
- **compone:** con qué otras filas se combina.
- **verifica:** la prueba que la fila pasó, con su sello. Sin sello, la fila queda como hipótesis.
  - **Legible:** `ruta` + sello del documento; la afirmación se sigue hasta su origen.
  - **Del ejecutor:** `corrida: [id]` + `reproduce: [sí|no]`; una instancia limpia rehace la forma leyendo solo el registro.
  - La prueba y sus tres casos viven en `./Proceso ATLAS.md`, `Pruebas`.
  - Un sello de corrida no sube el nivel de la afirmación: sube la fila, no la verdad.

## Reglas

1. Se busca por intención, nunca por nombre de método.
2. Tope de ~25 filas por forma. Si pasa, hay duplicados.
3. Crece por fallo: se agrega cuando una emisión no se resolvió con lo existente.
4. Ninguna fila se edita: se reemplaza.
5. Una fila sin `límite` o sin `verifica` no entra al índice; va a `Hipótesis`.
6. Lo opaco se mide: una forma no entra por su forma, sino por su efecto, su invariante y su transferencia. Se registra y se poda si no produce una intención.

## Estado

El atlas no declara cuántas filas tiene: declara cuándo una fila entra. Entra cuando tiene `límite` y `verifica`; mientras no los tenga, vive en `Hipótesis`. El conteo es estado de la implementación, no de este documento.

Un índice vacío no es un fallo: es un índice sin formas que hayan pasado su prueba.

## Franjas

### Hipótesis

`Hipótesis: [intención] | propuesta: [forma] | prueba: [cómo se falsifica] | nivel: [N3|N5] | puente: [efecto|invariante|decisión] | estado: [hipótesis|descartada]`

Candidatas no verificadas. Se intentan; si funcionan y se consigue su sello, se promueven a fila. Si no, se descartan y se anota el descarte.

### Opaco

`Opaco: [firma] | efecto: [lo que produce] | invariante: [lo que se conserva] | transfiere: [sí/no] | compone: [...]`

Formas nacidas del ejecutor que quizá no traduzcan. Pasan si una instancia limpia las reproduce leyendo solo el registro. Si no transfieren ni componen, pasan a `descartada`.

## Registro de formas

Mide el rendimiento de lo opaco: cuántas formas pasaron el puente, cuántas produjeron una intención nueva y cuántas se descartaron. No es un principio; es una medida.

| Forma | Efecto | Invariante | Decisión | Transferencia | Estado | Costo | Beneficio |
|---|---|---|---|---|---|---|---|

**Estados:** `hipótesis → opaco → promovida | descartada`.

**Regla de poda:** una forma que no transfiere ni produce una intención nueva se descarta, aunque suene increíble. El estado se escribe; la fila no se borra.

**Prueba:** ¿cada forma opaca tiene efecto, invariante y decisión? ¿Su estado es uno de los cuatro?
**Falsificador:** una forma opaca sin efecto; una forma que se presenta como logro; una fila sin estado.
