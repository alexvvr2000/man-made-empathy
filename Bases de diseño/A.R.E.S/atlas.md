# Atlas — intenciones a formas

**Unidad:** tarea.
**Aplica a:** expresar
**Lector:** autoridad.

> Índice caliente. Las fuentes no se leen: se verifican contra `verifica`.

## Cómo se lee una fila

`intención | forma | efecto | límite | compone | verifica`

- **intención:** en palabras de quien pide, no del método.
- **forma:** lo que se emite.
- **efecto:** lo que produce.
- **límite:** cuándo NO usarla. Sin esto, la fila queda como corazonada.
- **compone:** con qué otras filas se combina.
- **verifica:** `ruta` + sello del documento. Sin ruta y sello no hay fila: queda como hipótesis.

## Reglas

1. Se busca por intención, nunca por nombre de método.
2. Tope de ~25 filas por forma. Si pasa, hay duplicados.
3. Crece por fallo: se agrega cuando una tarea no se resolvió con lo existente.
4. Nada se edita: se reemplaza.
5. Una fila sin `límite` o sin `verifica` no entra al índice; va a `hipótesis`.
6. Lo opaco se mide: una forma no entra por su forma, sino por su efecto, su invariante y su transferencia. Se registra y se poda si no produce una intención.

## Estado

**Índice: vacío (0 filas).** No hay fuentes verificadas aún, así que no hay sello, así que nada cumple la regla 5. El atlas nace vacío a propósito: se llena cuando aparece la primera fuente verificada.

**Registro de formas: 0 filas.**

Las propuestas concretas de stack no viven en la base; viven en la implementación. El atlas solo registra formas por intención.

## Franjas

### Hipótesis

`Hipótesis: [intención] | propuesta: [forma] | prueba: [cómo se falsifica] | estado: abierta`

Candidatas no verificadas. Se intentan; si funcionan y se consigue su sello, se promueven a fila. Si no, se descartan y se anota el descarte.

### Opaco

`Opaco: [firma] | efecto: [lo que produce] | invariante: [lo que se conserva] | transfiere: [sí/no] | compone: [...]`

Formas nacidas del ejecutor que quizá no traduzcan. Pasan si una instancia limpia las reproduce leyendo solo el registro. Si no transfieren ni componen, pasan a ruido y se descartan.

## Registro de formas

Mide el rendimiento de lo opaco: cuántas formas pasaron el puente, cuántas produjeron una intención nueva y cuántas se descartaron. No es un principio; es una medida.

| Forma | Efecto | Invariante | Decisión | Transferencia | Estado | Costo | Beneficio |
|---|---|---|---|---|---|---|---|

**Estados:** `hipótesis → opaco → promovida | descartada`.

**Regla de poda:** una forma que no transfiere ni produce una intención nueva se descarta, aunque suene increíble. El estado se escribe; la fila no se borra.

**Test:** ¿cada forma opaca tiene efecto, invariante y decisión? ¿Su estado es uno de los cuatro?
**Falsificador:** una forma opaca sin efecto; una forma que se presenta como logro; una fila sin estado.
