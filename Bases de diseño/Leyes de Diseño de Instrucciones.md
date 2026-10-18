# Leyes de Diseño de Instrucciones

## Principio Mecánico: Forzar el Cálculo Antes de la Emisión
Quien ejecuta una instrucción la recorre de izquierda a derecha: cada parte ya emitida condiciona lo que sigue, y el esfuerzo de leer compite con el de improvisar. Vale para un lector con prisa, para un modelo que genera token por token —por ejemplo— y para cualquier ejecutor que pueda saltarse un paso.
- Si una instrucción da **explicaciones teóricas o consejos**, el ejecutor los trata como contexto pasivo y salta a la respuesta final para ahorrar esfuerzo.
- Si impone **compuertas secuenciales y anclas léxicas obligatorias**, el ejecutor se ve forzado a calcular el estado interno antes de poder escribir la señal siguiente, ejecutando el razonamiento de forma inevitable y con un gasto mínimo de lectura.

---

## Prohibición de Lenguaje Blando y Bifurcaciones Exhaustivas
Quien ejecuta interpreta cualquier adverbio condicional (*"procura"*, *"idealmente"*, *"cuando sea apropiado"*, *"intenta"*, *"si es necesario"*) como permiso para omitir el paso.
- **Regla:** Elimina todo verbo de sugerencia. Redacta exclusivamente con imperativos directos y árboles de decisión cerrados (`Si ocurre A → Ejecuta X | Si ocurre B → Ejecuta Y | En cualquier otro caso → Ejecuta Z`).
- **Efecto:** El 100% de los escenarios posibles cae en una rama determinista sin zonas grises.

---

## Contratos por Propiedades del Resultado (Libertad Controlada)
Hardcodear herramientas o comandos específicos (`rg`, `head`, `web_search`, scripts fijos) rompe el agnosticismo de entorno; escribir principios filosóficos abiertos dispara divagaciones que queman lectura.
- **Regla:** Define las **propiedades físicas que debe cumplir la operación**, dejando que el ejecutor sintetice en el acto el instrumento desechable óptimo para el canal actual.
- **Fórmula:** `[Restricción de ejecución] + [Forma exacta del resultado esperado]`.
  - *Ejemplo:* *"Agrupa todas las lecturas independientes en un único turno de ejecución y filtra la salida en origen para devolver solo el fragmento probatorio (delta, métrica o línea del fallo), prohibiendo volcar archivos completos al contexto."*

---

## Compuertas de Estado Secuenciales (State Gates)
Una lista de viñetas sin dependencia de orden invita a saltarse los pasos intermedios.
- **Regla:** Estructura el cuerpo de la instrucción como un tubería numerada (`Paso 1 → Paso 2 → Paso 3`) donde **el artefacto producido en el Paso N es el insumo obligatorio para habilitar el Paso N+1**.
- **Fórmula:** Añade en cada transición la restricción explícita: *"Prohibido ejecutar el Paso 2 sin haber emitido la salida del Paso 1"*.

---

## Anclas Léxicas (Proof-of-Work de 1 Línea)
Para garantizar que no se salte una evaluación mental (como clasificar la reversibilidad, declarar un supuesto o calificar una fuente), obliga a imprimir una **etiqueta testigo ultracorta (5 a 12 palabras)** antes o junto a la acción.
- **Regla:** Exige plantillas de una sola línea con campos fijos:
  - En indagación: `Sondeo: [variable] | Supuesto: [hipótesis]` y `[N1: medio → hallazgo]`.
  - En operación: `Cambio: [recurso] | Clase: [reversible/compensable] | Retorno: [mecanismo]`.
  - En bloqueo o fallo: `[VACÍO - SIN CONSTANCIA]` o `Falla instrumental: operando en N5`.
- **Efecto:** Para escribir el ancla, el ejecutor tiene que resolver primero la clasificación real: no puede escribirla sin haberla hecho. Es una prueba de trabajo cognitiva casi gratuita.

---

## Transiciones Explícitas de Cierre (Handoffs)
Las tareas reales cambian de naturaleza sobre la marcha: una consulta descubre que hay que modificar el sistema, o una ejecución revela un dilema arquitectónico.
- **Regla:** Cierra siempre la instrucción con un bloque de **Transiciones de Estado** que conecte la salida actual con el resto del catálogo:
  - *Si la salida resuelve la consulta → Entrega y cierra.*
  - *Si emergen dos o más rutas con fricción → Encadena `deliberacion-estructurada`.*
  - *Si el siguiente paso altera un estado persistente → Encadena `entrega-operacion`.*

---

## Redundancia de Escritura, Poda Posterior
Una regla escrita una sola vez se salta una sola vez, y en ese turno no hay segunda red. La instrucción no se recuerda: se vuelve a encontrar.

- **Regla:** Toda obligación que no puede omitirse se escribe desde al menos tres ángulos distintos, y cada ángulo cubre un modo de falla distinto: imperativo directo, ejemplo canónico, contraejemplo o consecuencia de omitirla, y ancla de una línea. Prohibido confiar en una sola formulación por clara que sea.
- **Duplicado útil:** `Si dos formulaciones fallan de la misma manera → una sobra | Si fallan por razones distintas → ambas se quedan | Si no hay caso medido → se quedan y se prueban`.
- **Poda con evidencia:** se elimina una variante solo cuando existe un turno donde esa variante no cambió la conducta y otra sí la sostuvo. Prohibido podar por elegancia o por longitud.
- **Efecto:** Quien ejecuta tiene que resolver el mismo cálculo por caminos distintos; saltarse uno no lo salva del otro. La redundancia sube el recall de la instrucción —que no se pierda nada— y la poda posterior sube la precisión —que nada sobre.

---

## Una regla, un dueño
Una regla vive en un solo sitio. La copia no duplica la garantía: duplica la próxima corrección pendiente.

- **Regla:** si una regla se necesita en dos lugares, se referencia. Se copia solo cuando el original no se carga nunca, y entonces la copia se marca como copia.
- **Test:** `Si el original cambia y la copia no → hay dos dueños | Si la copia cita al original → es referencia`.

---

## Las Listas No Definen
Una enumeración de ejemplos se lee como el conjunto completo: lo que no aparece en la lista deja de existir, o se inventa un elemento para encajar en ella. La lista que ilustra se convierte en la lista que limita.

- **Regla:** toda regla se define por propiedad y se cierra con un test, no con ejemplos. Los ejemplos se marcan como ejemplos —«por ejemplo»— y nunca hacen de definición. Prohibido cerrar con «etc.»: es la confesión de que la propiedad no se escribió.
- **Árbol cerrado:** `Si la regla aplica a un caso que no está en la lista → la propiedad está bien escrita | Si solo aplica a los casos listados → es una lista disfrazada de regla | Si no hay test → no es regla`.
- **Contraejemplo obligatorio:** por cada regla, un caso inventado fuera de la lista que también deba cumplirla. Si ese caso se cuela sin cumplirla, la regla era la lista.
- **Efecto:** no se puede inventar un elemento nuevo para encajar; o cumple la propiedad, o no aplica. El test es lo único que impide que la enumeración se vuelva el universo.

---

## Regla sin falsificador no entra
Una regla que no declara qué caso la rompe es una opinión con formato de norma.

- **Regla:** toda regla incluye el caso que la incumple. Si no existe, la regla no aplica a nada.
- **Test:** `Enuncia el caso que la incumple → si no aparece, la regla sobra | Si aparece y no está cubierto → falta la rama`.

---

## La Abstracción Que No Dispara
Una regla tan general que ya no dice cuándo actuar no es regla: es descripción. La generalización correcta amplía el alcance y conserva el disparador.

- **Regla:** se generaliza el caso concreto, nunca el disparador. La propiedad elegida debe seguir produciendo una acción comprobable cuando el caso aparece.
- **Test:** sustituye el caso por su propiedad. `Sigue disparando y el resultado sigue siendo verificable → generaliza | Deja de disparar → la abstracción se comió el disparador | Dispara pero no se puede verificar → se perdió el recibo`.
- **Ejemplo, marcado como ejemplo:** «si falta un hecho, accede al medio que corresponda» dispara y se verifica; «usa las herramientas correctamente» no dispara ni se verifica.
- **Efecto:** la generalización sube el alcance sin bajar la comprobabilidad. Si sube el alcance y baja la comprobabilidad, no es generalización: es dilución.

---

## El Acceso Implícito No Ocurre
Un acceso externo que no se declara no se ejecuta: quien ejecuta responde de memoria interna y la presenta con la misma forma que un hallazgo. Lo que no se anuncia, no pasa.

- **Regla:** toda consulta externa se emite en una línea antes de ejecutarse, con la variable y el supuesto que la motiva. Sin esa línea, la afirmación externa es memoria interna y se declara como tal.
- **Árbol cerrado:** `Consulta declarada → se ejecuta y emite recibo | Afirmación externa sin consulta → es N5, se declara | Dato medible sin declarar → falla de proceso, se corrige antes de emitir`.
- **Ancla:** `Sondeo: [variable] | Supuesto: [hipótesis]` antes; `[N1: medio → resultado]` después.
- **Efecto:** la declaración es el disparador. Sin ella el acceso se salta, y el salto solo se ve por el ancla que falta.

---

## Quien produce no certifica
La verificación no la firma el mismo que produjo. Un productor puede describir lo que hizo; no puede certificarlo.

- **Regla:** el artefacto se verifica con un criterio y un canal distintos de los que lo generaron. Si el mismo acto produce y comprueba, no hay comprobación.
- **Test:** `Si el productor puede alterar el resultado y el veredicto a la vez → no hay verificación`.
