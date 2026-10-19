# Leyes de Diseño de Instrucciones

Estas no son recomendaciones ni principios orientativos: son leyes. Se siguen al pie de la letra; no se negocian, no se interpretan, no se desvían. Donde hay criterio, hay principio; donde hay ley, no hay criterio.

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

## El Entregable Es El Último Estado, No La Conversación
El entregable es siempre el final: el estado que el receptor puede usar cuando el productor ya no está. Toda instrucción con entregable lo nombra como final, no como la conversación que lo produce. Final no significa definitivo: es el último estado de la tarea, y cambia cuando la tarea cambia; lo que no cambia es que se entrega entero. Un entregable no conserva la situación de conversación: no hay nadie que le hable a alguien, ni un antes que haya que recordar. Limpio no significa prolijo: significa sin residuo del intercambio.

**Alcance:** rige el artefacto que se entrega, no el turno que lo anuncia. El turno de análisis cierra con su pregunta de calibración; el entregable no.

- **Regla de estado:** el entregable contiene el estado final entero: todo lo que el receptor necesita para usar el resultado sin volver a preguntar. Se ordena por el objeto, no por la cronología del intercambio. La voz es la del objeto, no la del productor: el «tú» de la charla no aparece; el de la instrucción, sí. Prohibido entregar el anuncio del cambio (`ya lo modifiqué`, `quedó listo`), la ruta recorrida o la promesa de lo que falta: todos son el camino, no el objeto.
- **Regla de versión:** si el entregable cambia, se reemite en su estado nuevo: el artefacto completo o el cambio exacto que lo deja completo, nunca el relato del cambio. La versión vieja no se parchea con la conversación ni se acumula como capas. El historial solo se emite si el contrato lo pide, y entonces como historial, no como entregable.
- **Regla de forma:** la forma se elige por lo que potencia al mensaje, no por su estética. Un formato que no cambia lo que el receptor puede hacer con el mensaje es adorno y se retira.
- **Árbol cerrado:** `El artefacto se entiende sin el hilo → se entrega | Necesita el hilo para tener sentido → es un turno, no un entregable | El estado cambió → se reemite el estado nuevo, no se narra el cambio | El contrato pide historial → se emite como historial, no como entregable`.
- **Test:** `Tapa la conversación y lee solo el artefacto → si el receptor puede hacer con él lo que el artefacto promete, pasa | Si necesita el hilo para reconstruir el estado, falla`. `Busca a quién le habla el artefacto → si le habla como en una charla, falla | Si le entrega un estado o le da una instrucción, pasa`. Y `Quita la forma y deja el mensaje → si el receptor puede hacer lo mismo, era adorno | Si puede hacer más, servía | Si solo puede mirar, falla`.
- **Efecto:** el receptor no reconstruye: usa. Y el final puede cambiar diez veces sin que el receptor herede diez versiones.
- **Caso que la incumple:** una nota de trabajo prolija, con portada y tipografía cuidada, que dentro conserva la conversación que la produjo —«hablamos de esto, quedamos en que…»—, reparte la decisión en ida y vuelta, cierra con una frase de efecto y entrega la versión nueva como lista de cambios sobre la vieja. Se ve bien y no se puede usar: tiene rastro y puesta en escena, no estado.

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

## La Referencia No Se Explica
Una referencia dice a qué instrucción se llama y cuándo; la instrucción dice qué se hace. Explicar la referencia es reescribir la instrucción: el texto extra no agrega garantía, agrega una copia que se queda vieja.

- **Regla:** la referencia contiene la condición de llamada y el nombre de la instrucción. No copia sus pasos, reglas, anclas ni salida. Si el caso exige un cambio, se escribe solo el delta y se marca `Delta: [qué cambia]`.
- **Test:** `Borra el texto que explica la instrucción → si la conducta cambia, era un delta (se queda y se marca) | Si no cambia, era repetición (se borra)`.
- **Falsificador:** un apartado que repite lo que la instrucción ya dice; una referencia que enumera los pasos de la instrucción; una llamada que copia el contrato.
- **Efecto:** la referencia queda corta, la instrucción es el único dueño, y el caso borde no rompe: si lo que rige por defecto no aplica, el delta se escribe y se marca.

Es prima de `Una regla, un dueño`, pero cubre otro fallo: no la copia entre documentos, sino la explicación de la llamada.

---

## La Copia Se Paga Con Contexto
Copiar no elimina la lectura: la adelanta. El original se lee una vez y se copia; la copia se lee muchas veces. Si el original se lee una sola vez, copiarlo es pagar dos veces. Si se lee siempre, no copiarlo es pagar el original en cada uso.

- **Regla:** la copia se justifica por uso repetido, no por comodidad. Se copia solo la parte que se usa, se cita el original y se declara cómo se mantiene sincronizada. Lo que no se puede citar no es copia: es bifurcación.
- **Árbol cerrado:** `El original se lee una vez → se referencia | Se lee más de una vez → se copia la parte usada, citada y con regla de sincronización | La copia no puede citar el original → es bifurcación, no copia | El original cambia y la copia no → hay dos dueños`.
- **Test:** `Borra la copia y lee el original en cada uso → si el costo de esa lectura supera el de mantener la copia, la copia se justifica | Si no lo supera, se referencia`. Y `El original cambia → si la copia no cambia, la copia es un dueño paralelo`.
- **Falsificador:** una copia sin cita del original; una copia que copia más de lo que se usa; una copia sin regla de sincronización; una copia que se defiende como «más práctica» sin medir el uso.
- **Efecto:** el original sigue siendo el dueño; la copia paga su costo en contexto y en mantenimiento. No prohíbe copiar: le pone precio. No hay ni lectura infinita ni copia infinita.

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

Una regla sin caso que la incumpla es una ley que nadie ha visto aplicarse: se sigue por costumbre, no por convicción. El falsificador no acusa; hace visible el borde antes del choque.

Y el acto de detenerse ya informa: en el momento en que se para, aparece el caso que no se había pensado. Si ese caso podía terminar en consecuencias, la parada llega antes de ejecutar un acto cuyo resultado no estaba determinado.

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

---

## El Formato Sigue Al Lector
Todo artefacto declara su lector: máquina o humano. El formato del entregable se deriva de ese lector, no del gusto de quien escribe.

- **Regla:** si el lector es máquina, el entregable usa campos con nombre, anclas, compuertas y salida determinista; si es humano, usa contexto, razones, formato de lectura y una decisión posible. No se mezclan: un artefacto para máquina no se escribe como ensayo; uno para humano no se escribe como volcado de campos. Si el mismo contenido va a los dos, se entregan dos formatos, no uno ambiguo.
- **Árbol cerrado:** `Máquina → campos, anclas, compuertas y salida determinista | Humano → contexto, razones, formato de lectura y decisión | Lector no declarado → no se emite`.
- **Declaración:** la forma declara el lector; la línea `Lector:` se usa solo cuando el mismo contenido puede ir a dos o mas lectores.
- **Test:** `Forma humana → lector humano | Forma de campos/anclas → lector máquina | Forma mixta sin declaración → ambigua: no se emite`.

## Revisabilidad
Ninguna ley ni principio es inmutable. Toda ley y todo principio se revisan con la triangulación: evidencia interna, experiencia del usuario, conclusión del analista, evidencia externa y consistencia. El cambio lo aprueba la autoridad, se registra y actualiza los tests. La ley que no se puede falsar no es ley.

- **Regla:** toda ley y todo principio se revisa con cinco fuentes: evidencia interna, experiencia del usuario, conclusión del analista, evidencia externa y consistencia. Sin evidencia externa no se promueve; sin test no es ley; sin autoridad no se aplica.
- **Árbol cerrado:** `Evidencia externa + test + autoridad → se revisa | Sin evidencia externa → no se revisa | Sin test → no es ley | Sin autoridad → no se aplica`.
- **Test:** `Ley sin test → no es ley | Revisión sin evidencia externa → cámara de eco: no se aplica | Cambio sin autoridad → no se aplica`.
