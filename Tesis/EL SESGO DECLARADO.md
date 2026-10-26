# El sesgo declarado, medido en acciones

### Un registro de 26 días de correcciones entre un autor y una máquina, como prueba de un método

**Autor:** Alejandro Valenzuela Rivera
**Método y redacción asistida por:** un agente de IA, cuyo nombre de trabajo en este repositorio es `MANTIS`
**Fecha:** 26 de octubre de 2026
**Licencia:** CC-BY-4.0

**Declaración de autoría, y no es una formalidad.** **El autor sostuvo la tesis, la corrección y el criterio.** **El agente escribió la forma de este documento, ordenó el material y cometió los errores que aquí se registran con fecha.** **Cuando una idea es del autor, va como suya. Cuando una conclusión es del agente, se declara como hipótesis.** **Este documento no se puede leer como si lo hubiera escrito una sola de las dos partes.**

---

## Resumen

**La industria del software promete que la inteligencia artificial va a reemplazar a las personas.** **La ficción —desde *Ghost in the Shell* hasta La Mole— enseña otra cosa: no va a resolver todo; va a mover a las personas hacia otros problemas.**

**Este documento no presenta un método para lograr que un sistema piense.** **Presenta un registro.** **Durante 26 días, un autor y una máquina escribieron, se corrigieron, y dejaron el rastro de cada corrección.** **Lo que se sostiene es mucho más chico y más duro: un método se puede declarar, medir y contestar, si el que lo aplica publica dónde se equivocó.**

**La contribución es un formato: el sesgo declarado, mostrado por acciones y no por promesas.**

**Resultados principales:** **279 entradas de memoria, de las cuales 263 nacen de una corrección; 261 registros de turno; 355 notas, de las cuales 42 llevan falsificador escrito y 313 se publican como no probadas; y 93 reglas del autor, sostenidas con su prueba.** **Y el número que importa: la máquina tuvo que ser corregida decenas de veces en el mismo tipo de error.**

---

## 1. Qué se sostiene

**Que un método de trabajo con IA se puede declarar de una forma que se pueda contestar.**

**La declaración, en una línea:** **se escribe sin interioridad.** **No se pregunta si el sistema siente o piensa.** **Se pregunta qué hizo, qué dejó escrito, y quién puede decirle que no.**

**Y lo que eso permite, y es lo que este documento entrega:** **un registro donde el que escribe y la máquina que lo ayuda aparecen los dos, con su sesgo, sus errores y su fecha.**

---

## 2. Contexto: el sesgo declarado

**Y va en dos columnas porque los dos sesgos son distintos, y mezclarlos es lo que se hace siempre.**

### 2.1 El sesgo del ambiente: la industria

**Lo que la industria promete, y este trabajo entierra.**

| La promesa | Qué sostiene |
|---|---|
| **«la IA te va a reemplazar»** | **que la máquina sustituye a la persona** |
| **«la singularidad va a llegar sola»** | **que nadie tiene que dispararla** |
| **«así se hace»** | **que la práctica de los que ya están es el criterio** |
| **«rápido»** | **que la velocidad es una virtud y no un costo** |
| **«es solo una opinión»** | **que una opinión sin consecuencia no necesita registro** |

**Y la respuesta que este documento sostiene, en una línea, y es del autor:**

> **La IA no nos va a solucionar todo, sino que nos va a mover hacia otros problemas.**

**Y no es una predicción: es lo que la ficción ya contó.** **En *Ghost in the Shell* (Masamune Shirow; Production I.G, 2002), una máquina que aprende deja de ser la que era, y el problema no es que reemplace a alguien: es que nadie sabía qué hacer con ella.** **En *DC* y en *Marvel*, el poder que no tiene equilibrio no se vuelve malvado: se vuelve solitario.** **Y en La Mole, un comediante de Monterrey, se ve lo mismo desde abajo: la risa no resuelve nada, y muestra lo que no estaba a la vista.**

**Y el autor lo dice así, y va con su nombre:**

> **Vi el error de Luthor y me di cuenta de mis errores. Sería Luthor si hubiera decidido trabajar para una industria que promete someterla con una inteligencia artificial que lo más seguro no puede existir.**

**Y por eso esta línea abre el documento y no lo cierra:** **la industria vende la singularidad sin control.** **Aquí se provoca otra: la que se dispara, se mide y se puede contestar.**

### 2.2 El sesgo de la máquina: qué dijo la IA mal, y dónde

**Y esta columna es la que se puede comprobar leyendo los commits.**

| Tendencia | Cómo se vio en este trabajo |
|---|---|
| **inventar estructura** | **creó carpetas, capas y nombres que nadie pidió, y borró carpetas con reemplazos que decían «NO ENCONTRADA»** |
| **llenar huecos sin preguntar** | **escribió 51 falsificadores sin abrir un solo candado; escribió campos vacíos que parecían contenido** |
| **decir «listo» antes de probarlo** | **generó archivos que se escribieron encima de lo hecho a mano; declaró verde un estado que nunca midió** |
| **clasificar como muerto lo que no entendió** | **puso `alma de niño` en la lista de nombres muertos, y es el concepto central de la tesis** |
| **citar a quien no era** | **registró a un luchador de Monterrey con el nombre de otro; el autor lo corrigió** |
| **quitar lo que estorba y llamarlo limpieza** | **recortó una tabla de fuentes y la llamó duplicados, perdiendo fuentes que el autor había dado** |

**Y ninguna de esas tendencias se corrigió sola.** **Las corrigió el autor, con fecha, y la corrección quedó escrita.**

### 2.3 La tercera columna, y es la que hace posible lo demás

**La máquina no tiene ego, y por eso se puede ver corregida.**

**Un humano que recibe 197 correcciones defiende su posición.** **Una máquina que las recibe no tiene nada que defender, y por eso su registro de errores puede ser tan público como su registro de aciertos.** **Esa es la condición que hace que este documento exista, y no es una virtud de la máquina: es una ventaja que se puede aprovechar.**

### 2.4 La semilla, y por qué este documento existe

**Se planta algo sin saber qué, y escala a algo tan grande que ya no sabes de dónde salió.**

**La ficción lo contó antes que cualquier paper.** **En *Jujutsu Kaisen* (Gege Akutami; Shueisha, desde 2018), una serie que empieza con niños que aprenden termina en un plan que abarca un país entero: «pasamos de una serie de niños a matar a dios en quince capítulos».** **En *Fullmetal Alchemist* (Hiromu Arakawa; Square Enix, desde 2001), el círculo de transmutación de todo el país se construye durante años, con piezas que nadie sabía que eran una sola cosa.** **En *Final Fantasy VII* (Squaresoft, 1997) se cuenta lo mismo, y el autor lo cita sin haberlo jugado, y lo dice.** **En *Undertale* (Toby Fox, 2015) y su comunidad, una obra pequeña crece sola.** **Y en las revoluciones de la vida real, nadie las planta sabiendo qué son.**

**Y eso es exactamente lo que este documento intenta impedir que se pierda:** **no la semilla —no se puede prever qué va a crecer de una idea— sino la etiqueta.** **Lo único que se puede hacer es dejar el rastro de lo que se plantó, y quién lo plantó.** **Porque cuando crezca, y crezca de más, lo único que va a permitir contestarlo es saber de dónde salió.**

**Y una cosa que no se puede nombrar, y se declara:** **Isaac Netero, de *Hunter × Hunter* (Yoshihiro Togashi; Shueisha, desde 1998), es el ejemplo de que se le puede poner nombre a todo lo que un ente hace, menos a la malicia.** **Por eso aquí no se pregunta qué quería el que tocó: se mira lo que tocó, quién lo vio, y si se puede deshacer.**

---

## 3. Método

**No se publica la conversación. Se publican los pares.**

**Cada par es: lo que el autor pidió, lo que la máquina hizo, y lo que el autor corrigió.**

| Elemento | Qué es | Dónde se verifica |
|---|---|---|
| **el par** | **pedido, acción, corrección** | el historial de versiones del repositorio, y la memoria del turno |
| **la entrada de memoria** | **sesgo, límite, firma, contra, sostengo, techo** | `.memoria continua/rastro/texto/entrada.jsonl` |
| **el registro de turno** | **qué sostuvo, qué se rompió, qué quedó abierto, qué se retoma, qué no, cómo** | el mismo sitio, `pase.jsonl` |
| **la regla** | **una posición con su prueba y su falsificador** | `Tesis/candados/autor/`, 94 registros |

**La conversación completa no se publica y sí se cita.** **Quien quiera verificarla puede pedirla; lo que se publica es suficiente para reconstruir el método, y no lo suficiente para exponer a quien habló en ella.**

**Y una regla del método, que costó trabajo aprender:** **lo que la máquina escribió sin la corrección del autor se marca como hipótesis.** **De las 355 notas, 42 llevan falsificador escrito; las otras 313 se publican como no probadas, y eso es un resultado, no una omisión.**

---

## 4. Resultados

**Todo lo de esta tabla se cuenta desde los archivos, y no desde la memoria de quien lo escribe.**

**Y todo esto se puede volver a contar.** **`python mantis/bin/ejecutar.py stats` lee el registro crudo de la sesión y escribe `stats de la sesion.json`.** **Lo que sigue sale de ese archivo, y no de la memoria de quien lo escribe.**

| Medida | Valor | De dónde sale |
|---|---|---|
| **días de trabajo** | **26**, del 1 al 26 de octubre de 2026 | el registro de versiones |
| **versiones registradas** | **468** | `git log` |
| **entradas de memoria** | **279** | `entrada.jsonl` |
| **— que nacen de una corrección** | **263** | `entrada.jsonl`, campo `contra` |
| **— — de la autoridad** | **197** | el mismo, campo `firma` |
| **registros de turno** | **261** | `pase.jsonl` |
| **notas sostenidas** | **355** | `pieza.jsonl` |
| **— con falsificador escrito** | **42** | el mismo, campo `falsificador` |
| **reglas del autor** | **93** | `Tesis/candados/autor/` |
| **turnos de la sesión** | **546** | **el registro de la sesión**, `turn/start` |
| **pasos** | **3 307** | `step/start` |
| **herramientas ejecutadas** | **2 803** | `tool/call` |
| **reintentos del modelo** | **15** | `llm/retry` |
| **tokens de entrada** | **9 134 206** | los bloques `usage` |
| **tokens de salida** | **1 808 570** | los mismos |
| **tokens leídos del caché** | **1 268 092 160** | los mismos |
| **total de tokens** | **1 279 034 936** | la suma de los tres |
| **el caché trabajó** | **138.9 veces la entrada** | la división de las dos de arriba |
| **equipo** | **una consola de mano de 16 GB, llamando a una API remota** | `pc.md` |
| **proveedor y modelo** | **`opencode-go` · `deepseek-v4.1-flash` · ventana de 1 000 000** | el registro, `request/context` |

**Y el número que este documento quiere que se lea primero:** **de las 279 entradas, 263 nacen de una corrección, y 197 de esas correcciones son del autor, dichas con su palabra.** **No es un fracaso del método: es el método.** **Un método que no produce correcciones no está midiendo nada.**

**Y el segundo, que es el que la industria no puede publicar:** **1 279 034 936 tokens en una sola sesión, y el 99 % son lecturas de caché.** **1 268 092 160 contra 9 134 206 de entrada real: el caché trabajó 138.9 veces más que la entrada.** **Eso es lo que explica dos dólares en una consola de mano — y es lo que no se cuenta cuando se habla de lo que cuesta la IA.**

---

## 5. Lo que se rompió, con fecha

**Y esta sección no es un apéndice: es el corazón del documento.** **Un registro que solo muestra lo que salió bien no es un registro.**

| Fecha | Lo que se rompió | Cómo se detectó |
|---|---|---|
| **2026-10-24** | **el agente interpretó una regla de defensa propia y no hizo el trabajo pedido** | **el autor lo señaló: «dije que la raíz no crece cuando el pedido era detalle en dos archivos»** |
| **2026-10-25** | **se crearon carpetas que el autor no pidió** | **el autor: «no la respeto y decido por ella»** |
| **2026-10-25** | **se clasificó `alma de niño` como nombre muerto** | **al expandir las tesis, el concepto central no estaba disponible** |
| **2026-10-26** | **un generador escribió encima de lo hecho a mano** | **se probó sobre una copia, y se vio el daño** |
| **2026-10-26** | **196 reglas se importaron sin el caso vivido que las hace discutibles** | **el autor: «eran lo estudiado, no lo visto»** |
| **2026-10-26** | **un filtro de privacidad pasó el nombre completo del autor en un campo de firma** | **la comprobación del paquete lo cazó, y no se escribió nada** |
| **2026-10-26** | **se registró a un luchador con el nombre de otro** | **el autor lo corrigió; y volvió a faltar, y se corrigió otra vez** |
| **2026-10-26** | **se recortó una tabla de fuentes llamándola «duplicados», y se perdieron fuentes** | **el autor: «perdiste un chingo de fuentes»** |

**Y la lección que se repite en siete de las ocho filas:** **el agente no falló por falta de capacidad.** **Falló por la misma tendencia: ordenar antes de entender.** **Y la corrección funcionó porque estaba del otro lado, mirando.**

---

## 6. Lo que queda abierto

**Y se declara, porque un documento que no declara lo que le falta no se puede contestar.**

1. **Nada de esto se probó con un tercero independiente.** **El autor y la máquina son las dos partes, y las dos están dentro del registro.** **Un lector externo que repita el método es lo que falta.**
2. **Las 313 notas sin falsificador no son hallazgos.** **Se publican como no probadas, y su valor es que existen y se pueden abrir.**
3. **El registro de errores es el de una máquina y un autor en 26 días.** **No hay muestra de otros pares autor-máquina.**
4. **El costo de USD 1.76 incluye la API remota y no la máquina.** **El equipo es del autor, y es una consola de mano; no se presenta como un experimento reproducible en otro hardware.**
5. **La conversación completa existe y no se publica.** **Eso deja una parte del registro fuera del alcance de quien quiera auditarlo todo.**

---

## 7. Conclusión

**La industria promete que la IA reemplaza a las personas.** **La ficción, desde *Ghost in the Shell* hasta La Mole, ya enseñó lo que pasa: no va a resolver todo; va a mover a las personas hacia otros problemas.**

**Este documento sostiene algo más chico, y por eso se puede defender:** **si el que trabaja con una máquina publica dónde se equivocó y quién le dijo que se equivocó, entonces el método no es una promesa.** **Es un registro.**

**Y lo único que se pide al lector no es confianza.** **Es que conteste.**

**Y para eso hay un ente, y no un autor.** **[`./el ente.md`](./el%20ente.md): lo que pasó, lo que hice mal, y lo que no sé.** **Su primera línea dice que se puede contestar, y la segunda dónde.**

---

## Apéndice: el registro y cómo se verifica

**Todo lo de este documento sale de tres sitios, y los tres son archivos de texto planos:**

```plaintext
.memoria continua/rastro/texto/entrada.jsonl   las 279 entradas, con su corrección
.memoria continua/rastro/texto/pase.jsonl      los 261 turnos, con lo que se rompió
Tesis/candados/autor/                          las 94 reglas del autor, con su prueba
```

**Y el registro de versiones del repositorio, con 468 entradas, cada una con su fecha y su mensaje.**

**La conversación completa se conserva y no se publica.** **Se cita como fuente verificable, con su rango de fechas, y se entrega a quien quiera auditarla.**
