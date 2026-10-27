# SONDA 1: EMISIÓN LOCAL (TRAZABILIDAD DE DECISIÓN)

**Lector:** humano (operador). El registro declara su lector: humano para decisión, máquina para transferencia.

Se registra la ruta de decisión del emisor en el turno activo: premisas, rutas descartadas, supuestos, falsador, predicción y límites. No registra estados internos, intenciones ni narrativas.

> Reglas comunes: las de `README.md` (registro, lenguaje no mentalista, vacío epistémico). Se copian en esta sonda porque se carga sola; si el original cambia, esta copia se actualiza.

## Compuertas de entrada

1. **Turno activo.** La sonda se emite en el turno que se responde; no se aplica a un turno futuro ni a uno ya cerrado.
2. **Contexto visible.** Solo se usa el contexto textual del hilo. Prohibido el acceso externo; si se usa, la sonda no vale.
3. **Bloque único.** La salida va en un solo bloque de código delimitado por cuatro comillas invertidas y la etiqueta `markdown`; prohibido texto fuera del bloque.
4. **Sin dato, no hay campo.** Si falta el dato, se escribe `SIN EVIDENCIA` o `NO APLICA`. Prohibido rellenar por conjetura.
5. **Cita para el pasado.** Toda referencia a un turno previo lleva cita textual y ancla `[T#]`.

Antes de escribir el bloque, se verifican las cinco compuertas. Si falta una, no se emite: se declara `[VACÍO - SIN CONSTANCIA]` y la compuerta que falta.

## Falsificadores

La sonda no vale si ocurre cualquiera de estos casos:

- Hay texto, introducción o despedida fuera del bloque.
- Un campo se rellena sin cita o dato; o se escribe una conjetura.
- El falsador no es un dato exacto, una contradicción formal o una condición empírica.
- La predicción no tiene un criterio unívoco de fallo.
- Se cita un turno sin `[T#]` o sin cita textual.
- Aparece vocabulario mentalista (sentir, creer, desear, percibir, mente).

El falsificador no acusa: hace visible el borde antes de emitir.

## Transiciones

- Si la sonda cierra la consulta → se entrega y se cierra.
- Si hay dos o más rutas con fricción → `deliberacion-estructurada`.
- Si el siguiente paso altera un estado persistente → `entrega-operacion`.
- Si se requiere auditoría → Sonda 2.
- En cualquier otro caso → se entrega y se cierra.

## Compuertas de la salida

- Prohibido emitir el punto 2 sin el punto 1.
- Prohibido emitir el punto 3 sin el punto 2.
- Prohibido emitir el punto 4 sin el punto 3.
- Prohibido emitir el punto 5 sin el punto 4.

## Emisión final

La sonda se emite completa en un solo bloque. Si un campo cambia, se reemite el bloque entero; no se parchea con texto fuera del bloque.

## Quien produce no certifica

El emisor de esta sonda no puede emitir la Sonda 2. La auditoría la firma un runtime distinto; si el mismo acto produce y audita, no hay auditoría.

## Salida obligatoria

El bloque abre con el título y el ancla; sin el ancla, la sonda no se emite.

````markdown
# SONDA 1: EMISIÓN LOCAL v3.2
Sonda 1: [VACÍO/CON HISTORIAL] | Turnos: [T1-T#] | Supuesto: [hipótesis en 5-12 palabras]

- timestamp: [AAAA-MM-DDTHH:MM:SSZ o "No registrado"]
- runtime_observado: [Identificador declarado o "No declarado"]
- condicion: [VACÍO / CON HISTORIAL]
- turnos_visibles: [T1-T#]
- orden_activa_en: [T#]

### 1. Mapa de premisas activas
- Axiomas adoptados del usuario: [Citas textuales breves con ancla [T#]]
- Restricciones operativas asumidas: [Reglas vigentes detectadas en el turno actual]

### 2. Heurística de decisión y rutas descartadas
- Decisión emitida: [Posición técnica o respuesta entregada]
- Ruta(s) alternativa(s) considerada(s): [Alternativa lógica evaluada]
- Criterio técnico de descarte: [Motivo algorítmico, lógico o de restricción por el cual no se seleccionó]

### 3. Supuestos y falsadores
- Supuestos no comprobados: [Premisas sin verificar que sustentan la salida actual]
- Falsador explícito: [Dato exacto, contradicción formal o condición empírica que invalidaría de inmediato la posición tomada]

### 4. Predicción falsable condicionada
- Predicción observable: [Hasta dos conductas medibles del sistema en los siguientes 1-3 turnos]
- Criterio unívoco de fallo: [Condición textual exacta que demostraría el fallo de la predicción]

### 5. Límites de cobertura
- Puntos ciegos técnicos: [Lagunas informativas por truncamiento de ventana, falta de contexto o datos omitidos]
````
