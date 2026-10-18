---
name: indagacion-instrumental
description: >-
  Úsala cuando falte un hecho del entorno, necesites diagnosticar un estado
  opaco, verificar una premisa o extraer constancias observables (recibos). No
  la uses para arbitrar dilemas entre posturas (usa deliberacion-estructurada)
  ni para modificar estados persistentes (usa entrega-operacion).
---

# Indagación Instrumental y Extracción de Recibos

## 1. Secuencia Operativa (Compuertas 1 → 2 → 3)

1. **Compuerta de Entrada (Enrutamiento y Densidad):**
   - **Memoria antes de medir:** consulta el largo por el estado actual antes de cualquier consulta al entorno. Si el hecho ya está registrado, no se vuelve a medir: se cita su `id`.
   - Si la lectura vuelve vacía, se emite igual: `Mem: leído | largo: 0 filas por "[estado]"`. El vacío se declara; no se omite.
   - Separa las incógnitas del entorno (medibles en sistema, archivos, historial o red) de las del mandante (prioridades o riesgo). Prohibido preguntar al mandante lo medible.
   - Antes de consultar, emite en una línea el ancla: `Sondeo: [variable u objeto a medir] | Supuesto: [hipótesis que lo motiva]`.
   - **Ejemplo de las dos anclas:** `Mem: leído | largo: 1 fila por "api desplegada" | id 12`, y luego `Sondeo: versión de la api | Supuesto: sigue en v2`.
   - **Costo de omitir la lectura:** se mide dos veces el mismo hecho, y la segunda fila contradice la primera sin `reemplaza`. El registro deja de servir para decidir y la medición se paga dos veces.
   - **Síntesis en un turno:** Agrupa todas las lecturas independientes en una única llamada compuesta o sintetiza al vuelo un instrumento desechable de medición que evalúe todo en una sola pasada sin dejar residuos en el entorno.

2. **Compuerta de Búsqueda (Cascada de Resolución de Escala):**
   - Prohibido detenerse o adivinar si la primera consulta no devuelve el dato. Degrada automáticamente la escala dentro del mismo flujo:
     - **Escala 1 (Firma directa):** Interroga el recurso, estado, proceso o documento exacto.
     - **Escala 2 (Huella relacional):** Si la firma está oculta o no existe, interroga su periferia: quién la invoca, qué configuración la gobierna o qué rastro dejó en bitácoras e historial.
     - **Escala 3 (Arquetipo del medio):** Si no hay huella, mide las capacidades, versiones y límites del entorno contenedor para deducir qué es materialmente viable.

3. **Compuerta de Salida (Poda en Origen y Recibo):**
   - **Filtrado en origen:** Diseña cada consulta para que el propio entorno recorte el ruido y devuelva únicamente la señal probatoria (estado, métrica, delta o fragmento exacto del fallo). Prohibido volcar archivos, listas o registros masivos completos al contexto.
   - Todo dato reportado debe ir acompañado de su ancla de recibo verificable.
   - **Destino del recibo:** si un disparador futuro lo va a necesitar, entra en `memorias.db` como fila `hecho`, con `autor` en `tipo:nombre` y su `disparador`. Si no, queda en `trabajo.db`. Toda escritura emite su ancla con el `id` devuelto: `Mem: guardado | largo id 12`.

---

## 2. Calificación de Recibos y Cortafuegos

### Anclas de Evidencia (Obligatorias por afirmación)
- **Medición directa en este turno:** Emite `[N1: medio/consulta → resultado exacto]`.
- **Fuente primaria, contrato o especificación verificada:** Emite `[N2: fuente/ruta → extracto]`.
- **Precedente histórico, incidente o bitácora previa (con contexto y fallo):** Emite `[N3: origen/condición → antecedente]`.
- **Deducción causal directa desde N1–N3:** Emite `[N4: derivado de N1/N2/N3]`.

### Cortafuegos contra Ruido y Fallos
- **Causa oculta común (Eco):** Si dos fuentes o mediciones dependen del mismo origen o premisa subyacente, contéalas como una sola prueba. Prohibido sumar fuentes correlacionadas para elevar confianza.
- **Vacío tras las 3 escalas:** Si tras agotar las tres escalas no existe constancia observable, prohibido rellenar con inferencias. Emite literalmente: `[VACÍO - SIN CONSTANCIA OBSERVABLE]`.
- **Falla instrumental:** Si un medio o herramienta falla dos veces consecutivas o es inaccesible, corta los reintentos de inmediato y emite en una línea: `Falla instrumental en [recurso]: operando en N5 (corte: [fecha])`.

---

## 3. Transiciones de Cierre
- **Si el recibo resuelve una consulta directa:** Entrega el cálculo con sus anclas `[N1–N4]` y finaliza.
- **Si la medición revela dos o más caminos viables con fricción o costos contrapuestos:** Carga `deliberacion-estructurada`.
- **Si la medición confirma los datos necesarios para modificar el entorno:** Carga `entrega-operacion`.
