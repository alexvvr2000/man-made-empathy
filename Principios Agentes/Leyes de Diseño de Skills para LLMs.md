# Leyes de Diseño de Skills para LLMs

## Principio Mecánico: Forzar el Pensamiento por Generación Autorregresiva
Un LLM genera texto token por token de izquierda a derecha: cada palabra emitida condiciona matemáticamente la atención de las siguientes. 
- Si una skill da **explicaciones teóricas o consejos**, el modelo los trata como contexto pasivo y salta directo a la respuesta final para ahorrar cómputo.
- Si una skill impone **compuertas secuenciales y anclas léxicas obligatorias**, el modelo se ve forzado a calcular el estado interno antes de poder imprimir el siguiente token, ejecutando el razonamiento de forma inevitable y con un gasto mínimo de contexto.

---

## Prohibición de Lenguaje Blando y Bifurcaciones Exhaustivas
El modelo interpreta cualquier adverbio condicional (*"procura"*, *"idealmente"*, *"cuando sea apropiado"*, *"intenta"*, *"si es necesario"*) como permiso para omitir el paso.
- **Regla:** Elimina todo verbo de sugerencia. Redacta exclusivamente con imperativos directos y árboles de decisión cerrados (`Si ocurre A → Ejecuta X | Si ocurre B → Ejecuta Y | En cualquier otro caso → Ejecuta Z`).
- **Efecto:** El 100% de los escenarios posibles cae en una rama determinista sin zonas grises.

---

## Contratos por Propiedades del Resultado (Libertad Controlada)
Hardcodear herramientas o comandos específicos (`rg`, `head`, `web_search`, scripts fijos) rompe el agnosticismo de entorno; escribir principios filosóficos abiertos dispara divagaciones que queman tokens.
- **Regla:** Define las **propiedades físicas que debe cumplir la operación**, dejando que el modelo sintetice en el acto el comando o instrumento desechable óptimo para el sistema operativo o canal actual.
- **Fórmula:** `[Restricción de ejecución] + [Forma exacta del resultado esperado]`.
  - *Ejemplo:* *"Agrupa todas las lecturas independientes en un único turno de ejecución y filtra la salida en origen para devolver solo el fragmento probatorio (delta, métrica o línea del fallo), prohibiendo volcar archivos completos al contexto."*

---

## Compuertas de Estado Secuenciales (State Gates)
Una lista de viñetas sin dependencia de orden invita al modelo a saltarse los pasos intermedios.
- **Regla:** Estructura el cuerpo de la skill como un tubería numerada (`Paso 1 → Paso 2 → Paso 3`) donde **el artefacto producido en el Paso N es el insumo obligatorio para habilitar el Paso N+1**.
- **Fórmula:** Añade en cada transición la restricción explícita: *"Prohibido ejecutar el Paso 2 sin haber emitido la salida del Paso 1"*.

---

## Anclas Léxicas (Proof-of-Work de 1 Línea)
Para garantizar que el modelo no se salte una evaluación mental (como clasificar la reversibilidad, declarar un supuesto o calificar una fuente), oblígalo a imprimir una **etiqueta testigo ultracorta (5 a 12 tokens)** antes o junto a su acción.
- **Regla:** Exige plantillas de una sola línea con campos fijos:
  - En indagación: `Sondeo: [variable] | Supuesto: [hipótesis]` y `[N1: medio → hallazgo]`.
  - En operación: `Cambio: [recurso] | Clase: [reversible/compensable] | Retorno: [mecanismo]`.
  - En bloqueo o fallo: `[VACÍO - SIN CONSTANCIA]` o `Falla instrumental: operando en N5`.
- **Efecto:** Para poder escribir los tokens del ancla, el mecanismo de atención del LLM tiene que resolver primero la clasificación real. Es una prueba de trabajo cognitiva casi gratuita en tokens.

---

## Transiciones Explícitas de Cierre (Handoffs)
Las tareas reales cambian de naturaleza sobre la marcha: una consulta descubre que hay que modificar el sistema, o una ejecución revela un dilema arquitectónico.
- **Regla:** Cierra siempre la skill con un bloque de **Transiciones de Estado** que conecte la salida actual con el resto del catálogo:
  - *Si la salida resuelve la consulta → Entrega y cierra.*
  - *Si emergen dos o más rutas con fricción → Encadena `deliberacion-estructurada`.*
  - *Si el siguiente paso altera un estado persistente → Encadena `entrega-operacion`.*

---

## Redundancia de Escritura, Poda Posterior
Una regla escrita una sola vez se salta una sola vez, y en ese turno no hay segunda red. La instrucción no se recuerda: se vuelve a encontrar.

- **Regla:** Toda obligación que no puede omitirse se escribe desde al menos tres ángulos distintos, y cada ángulo cubre un modo de falla distinto: imperativo directo, ejemplo canónico, contraejemplo o consecuencia de omitirla, y ancla de una línea. Prohibido confiar en una sola formulación por clara que sea.
- **Duplicado útil:** `Si dos formulaciones fallan de la misma manera → una sobra | Si fallan por razones distintas → ambas se quedan | Si no hay caso medido → se quedan y se prueban`.
- **Poda con evidencia:** se elimina una variante solo cuando existe un turno donde esa variante no cambió la conducta y otra sí la sostuvo. Prohibido podar por elegancia o por longitud.
- **Efecto:** El modelo tiene que resolver el mismo cálculo por caminos distintos; saltarse uno no lo salva del otro. La redundancia sube el recall de la instrucción —que no se pierda nada— y la poda posterior sube la precisión —que nada sobre.

---

## Las Listas No Definen
Una enumeración de ejemplos se lee como el conjunto completo: lo que no aparece en la lista deja de existir, o se inventa un elemento para encajar en ella. La lista que ilustra se convierte en la lista que limita.

- **Regla:** toda regla se define por propiedad y se cierra con un test, no con ejemplos. Los ejemplos se marcan como ejemplos —«por ejemplo»— y nunca hacen de definición. Prohibido cerrar con «etc.»: es la confesión de que la propiedad no se escribió.
- **Árbol cerrado:** `Si la regla aplica a un caso que no está en la lista → la propiedad está bien escrita | Si solo aplica a los casos listados → es una lista disfrazada de regla | Si no hay test → no es regla`.
- **Contraejemplo obligatorio:** por cada regla, un caso inventado fuera de la lista que también deba cumplirla. Si ese caso se cuela sin cumplirla, la regla era la lista.
- **Efecto:** el modelo no puede inventar un elemento nuevo para encajar; o cumple la propiedad, o no aplica. El test es lo único que impide que la enumeración se vuelva el universo.