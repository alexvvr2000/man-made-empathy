# Protocolo

**Unidad:** tarea.
**Aplica a:** expresar
**Lector:** autoridad y ejecutor. El artefacto declara su lector: autoridad para decisión, ejecutor para transferencia.

## 1. Registros

Toda forma se emite en uno de dos registros, y se declara cuál:

- **Legible:** converge a la decisión del lector. Se prueba con que el receptor entienda o actúe.
- **Del ejecutor:** converge a transferencia. Se prueba con que una instancia limpia lo reproduzca leyendo solo el registro.

Cambiar de registro a mitad de una respuesta está prohibido (`Reglas de escritura` 1.9): el receptor pierde el código.

## 2. Ancla

Toda forma nueva se declara en una línea antes de producirse, con el ancla de su franja (§4). El ancla de `Opaco` es:

`Opaco: [firma] | efecto: [lo que produce] | invariante: [lo que se conserva] | transfiere: [sí/no] | compone: [...]`

Sin ancla, la forma no se admite: se produjo algo y nadie sabe qué.

## 3. Pruebas

Tres, y el gusto no cuenta:

1. **Efecto:** produjo lo que debía en el receptor.
2. **Reproducibilidad:** mismo input, mismo resultado.
3. **Transferencia:** otra instancia la reproduce leyendo solo el registro.

Sin la tercera, no hay transferencia. Sin la segunda, no hay reproducibilidad. Sin la primera, no hay efecto. El mapa agrega `Tensión` para su superficie (`mapa.md`); no es una cuarta prueba de la forma.

## 4. Franjas

- **Hipótesis:** combinaciones no probadas. Se intentan; si funcionan y consiguen su sello, se promueven; si no, se descartan.
- **Opaco:** formas nacidas del ejecutor que quizá no traduzcan. Viven por efecto e invariante, no por explicación.
- **Inspiración:** formas nacidas de otra obra o dominio. Entran como `Hipótesis`, con nivel (N3/N5), prueba y puente; ninguna inspiración es evidencia.

`Inspiración: [obra/dominio] | forma: [qué sugiere] | nivel: [N3|N5] | prueba: [qué la rompería] | puente: [efecto|invariante|decisión] | estado: hipótesis`

Lo que no transfiere ni compone se descarta y se anota el descarte.

## 5. Atlas

El índice se organiza por **intención**, nunca por nombre de método. Una fila es (forma y sello de cada campo en `atlas.md`):

`intención | forma | efecto | límite | compone | verifica`

Reglas:

1. Se busca por intención.
2. Tope de ~25 filas por forma; si pasa, hay duplicados.
3. Crece por fallo, no por curiosidad.
4. Ninguna fila se edita: se reemplaza.
5. Sin `límite` o sin `verifica`, la fila va a `Hipótesis`.

## 6. Crecimiento

- Una fila nueva se escribe cuando una tarea no se resolvió con las existentes.
- Una forma del ejecutor se promueve cuando pasa transferencia y compone con al menos otra.
- Lo aprendido de la autoridad (gusto, ritmo, restricciones) se escribe solo por decisión suya, con su por qué, y se reemplaza.

## 7. Lo que no se hace

- Evaluar por estética.
- Cargar fuentes al marco: se verifican, no se leen.
- Presentar opacidad como logro.
- Confundir inspiración con evidencia: la fuente es libre; el nivel no.
- Repetir la misma forma por inercia: si tres entregas usan la misma familia, se declara saturación y se varía.

## 8. Mapa

La forma del mapa de vistas vive en `mapa.md`. El protocolo fija las reglas; el mapa fija la superficie. Sin mapa, el registro se lee como informe; con mapa, se ve lo que la decisión deja fuera.
