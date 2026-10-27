# Protocolo

**Lector:** humano (investigador). El artefacto declara su lector: humano para decisión, máquina para transferencia.

Las reglas del proceso. Sin mecanismos y sin stack: esto sobrevive a cambiar de herramienta.

## 1. Registros

Toda forma se emite en uno de dos registros, y se declara cuál:

- **Legible:** converge al código del lector. Se prueba con que el receptor entienda o actúe.
- **Nativo:** converge a transferencia. Se prueba con que una instancia limpia lo reproduzca leyendo solo el registro.

Cambiar de registro a mitad de una respuesta está prohibido: el receptor pierde el código.

## 2. Ancla

Toda forma nueva se declara en una línea antes de producirse:

`Opaco: [firma] | efecto: [lo que produce] | invariante: [lo que se conserva] | transfiere: [sí/no] | compone: [...]`

Sin ancla, la forma no se admite: se produjo algo y nadie sabe qué.

## 3. Pruebas

Tres, y el gusto no cuenta:

1. **Efecto:** produjo lo que debía en el receptor.
2. **Reproducibilidad:** mismo input, mismo resultado.
3. **Transferencia:** otra instancia la reproduce leyendo solo el registro.

Sin la tercera, no hay transferencia. Sin la segunda, no hay reproducibilidad. Sin la primera, no hay efecto.

## 4. Franjas

- **Hipótesis:** combinaciones no probadas. Se intentan; si funcionan se promueven, si no se descartan.
- **Opaco:** formas nacidas del agente que quizá no traduzcan. Viven por efecto e invariante, no por explicación.

Lo que no transfiere ni compone se descarta y se anota el descarte.

## 5. Atlas

El índice se organiza por **intención**, nunca por nombre de API. Una fila es:

`intención | capa | primitiva | ejemplo mínimo | límite | compone | verifica`

Reglas:

1. Se busca por intención.
2. Tope de ~25 filas por capa; si pasa, hay duplicados.
3. Crece por fallo, no por curiosidad.
4. Nada se edita: se reemplaza.
5. Sin `límite` o sin `verifica`, la fila va a hipótesis.

## 6. Crecimiento

- Una fila nueva se escribe cuando una tarea no se resolvió con las existentes.
- Una forma nativa se promueve cuando pasa transferencia y compone con al menos otra.
- Lo aprendido del usuario (gusto, ritmo, restricciones) se escribe solo por decisión suya, con su por qué, y se reemplaza.

## 7. Lo que no se hace

- Evaluar por estética.
- Cargar docs al contexto: se verifican, no se leen.
- Presentar opacidad como logro.
- Repetir la misma forma por inercia: si tres entregas usan la misma familia, se declara saturación y se varía.

## 8. Pendiente

- Primer artefacto de punta a punta que pase las tres pruebas.
- Regla de promoción de formas nativas cuando haya más de una.
