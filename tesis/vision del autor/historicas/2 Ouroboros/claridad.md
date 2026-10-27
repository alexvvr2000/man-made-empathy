**Variables:** artefacto · lector · clase · ambigüedad · ejemplo
**Peor:** el artefacto se lee de dos formas y el que ejecuta no sabe cuál era, y no lo declara
**Quién:** quien emite, y quien ejecuta lo emitido

# Proceso de claridad

**Unidad:** proceso.
**Aplica a:** escribir.
**Tipo:** proceso de claridad. Se aplica al escribir, al editar y al emitir.
**Nivel:** primitivo. Uno de los primitivos del guantelete. Es la fuente de la que se muta: `fricción` y `sesgo declarado` nacen de él.
**Requiere:** ninguno.
**Compatible con:** `Proceso de manipulacion de procesos`, `Procesos principales`.
**Alcance:** todo artefacto de la situación actual.

## Entra | Falla | Sale | Consume

- **Entra:** un artefacto escrito, y el lector que tiene que leerlo o ejecutarlo.
- **Falla:** el artefacto dice dos cosas a la vez, no declara desde dónde habla, o exige un glosario para entenderse; la forma no corresponde a la clase declarada.
- **Sale:** la forma del artefacto —clase, lector, campos, ejemplos—, o la lista de sus ambigüedades con la norma que las marca.
- **Consume:** quien va a emitir o ejecutar el artefacto. Si la forma no cierra, no se emite.

Estas reglas no son una instrucción de ejecución: no tienen compuertas de turno. Se aplican al escribir, al editar y al emitir; `1.12` es un algoritmo de admisión, no una compuerta. La producción de procesos vive en `Proceso de manipulacion de procesos.md`; este documento no la repite.

La claridad no es información pura: es la forma en que el contexto llega al lector. Un texto claro transporta su posición, su límite y su ejemplo sin pedir glosario. Lo que se ejecuta paga además no ambigüedad: cada lectura tiene que ser la misma.

`1.4` fija la clase de cada artefacto: `Se ejecuta` exige claridad y no ambigüedad; `Se lee` exige claridad y lleva ejemplo. La clase decide la exigencia, no la forma.

La unidad es el artefacto: qué entra, qué se calcula, qué sale, qué se conserva.

## 1. Reglas de claridad

### 1.1 Estilo de proceso
Toda regla se escribe sobre una operación: qué entra, qué se hace, qué señal sale, qué configuración cambia. El sujeto de la regla es la operación, no lo que la ejecuta. La tarea es esa operación: si no se puede decir qué entra, qué se calcula y qué sale, no es tarea.

**Prueba:** `La regla se aplica sin describir al ejecutor → bien escrita | Necesita describir al ejecutor → mal escrita`.
**Falsificador:** `[del Prueba] el caso que el Prueba marca como falla`.

### 1.2 Lo que distingue
Toda descripción se funda en lo que distingue: la operación, la función, la diferencia con otro. La descripción que no distingue es una etiqueta.

**Prueba:** `Borra el nombre y deja la descripción → si sigue diciendo qué hace o en qué difiere, describe | Si no dice nada, era una etiqueta`.
**Falsificador:** `[del Prueba] el caso que el Prueba marca como falla`.

### 1.3 Propagación del estilo
El estilo de estas reglas rige todo artefacto que se base en ellas —skills, instrucciones, agentes, anexos—. Un derivado que describa por esencia o que ponga al ejecutor como sujeto contamina la regla con el ser; se corrige el derivado, no la regla.

**Prueba:** `Derivado con esencia o con el ejecutor como sujeto → contaminación: se corrige el derivado | Derivado escrito sobre operaciones y diferencias → consistente`.
**Falsificador:** `[del Prueba] el caso que el Prueba marca como falla`.

### 1.4 Lo human-first no se completa
Un documento cuya forma declara un lector —prosa, contexto y decisión, sin campos ni anclas de ejecución— se amplía solo cuando la ampliación evita una lectura equivocada o cierra un hueco que el lector ya necesita. Se agrega una pieza, no una sección; no se completa por simetría, estética o completitud. La línea que el formato ya declara —por ejemplo, `Lector:`— no se agrega.

**Ejemplos:** un README, un principio o una prueba. La propiedad es la forma; el nombre no define.

**Árbol cerrado:** `Evita una lectura equivocada → una pieza | Cierra un hueco que el lector ya tiene → una pieza | Completa por simetría o estética → no | Necesita una sección → se consulta`.

**Clase.** Todo artefacto declara su clase: `Se ejecuta` o `Se lee`. La clase fija la exigencia, no la forma. Un artefacto que se ejecuta exige claridad y no ambigüedad; lo que se lee exige claridad. El lector es el que se ejecuta cuando la salida es entrada de otro cálculo, y el que lee cuando la salida se interpreta.

**Prueba:** `Artefacto con clase declarada → pasa | Artefacto que se ejecuta sin clase → falla | Artefacto que se lee declarado human-first → pasa`.
**Falsificador:** `Un artefacto ejecutable sin regla de no ambigüedad | Un artefacto de lectura cargado con compuertas de ejecución | Clase no declarada`.

**Ejemplo.** El ejemplo es una pieza de claridad, no una tolerancia. En un documento que se lee, su ausencia es un fallo de esta regla. En un documento que se ejecuta, el ejemplo se marca y la regla se sostiene sin él.

**Prueba:** `La forma declara lector → human-first | La forma declara campos/anclas → máquina | La forma mezcla sin declarar → ambigua`. `Documento que se lee sin ejemplo cuando la regla lo admite → incompleto | Ejemplo marcado en documento que se ejecuta → pasa`.
**Falsificador:** `[del Prueba] el caso que el Prueba marca como falla`.

### 1.5 Agnosticismo de era, tecnología y especie
Las normas no nombran **coordenadas de tiempo, instrumento o especie** —eras, tecnologías, herramientas, modelos, plataformas, versiones o especies—. Se escriben por propiedad y operación.

Una regla que nombra una era, una tecnología o una especie se vuelve **dependencia**: muere cuando eso cambia. Se escribe por propiedad. **Prueba:** quita el nombre; si la regla sigue, es ley; si no, es herramientas.

Se complementa con el proceso de manipulación de procesos (`Proceso de manipulacion de procesos.md`, `Pregunta de entrada`). El proceso de agentes lo referencia; no se copia.

**Excepción:** un ejemplo, un ancla de instrumento actual o un caso de aplicación puede nombrar una tecnología, siempre que esté marcado como ejemplo y la regla se sostenga sin ella. La tecnología no se convierte en el contrato.

**Prueba:** `Regla con tecnología → falla | Ejemplo marcado con tecnología → pasa | Regla que solo se entiende con la tecnología → falla`.
**Falsificador:** `Una ley que dice "usa X" → herramientas, no ley | Un ejemplo sin marca que se lee como regla → contaminación | Una regla que no se puede aplicar sin X → dependencia`.

### 1.6 Español neutro
Todo artefacto se escribe en español neutro, siempre. Sin voseo, sin regionalismos, sin modismos locales y sin jerga de país. La prosa se entiende en cualquier región. Los nombres propios, las siglas, las rutas y los términos técnicos establecidos se conservan.

**Árbol cerrado:** `Registro neutro → se emite | Voseo, regionalismo o modismo → se corrige | Duda de región → forma neutra`.
**Prueba:** `Voseo, regionalismo o modismo → falla | Prosa neutra → pasa | Duda → forma neutra`.
**Falsificador:** `Se usa «vos», «tenés», «querés» o un modismo local → no es neutro`.

### 1.7 Mutar
Mutar es transformar desde un punto de referencia; incluye agregar, modificar y eliminar. Toda eliminación es una mutación. «Evolución» es la trayectoria de mutaciones con selección; no la operación.

**Prueba:** `Se elimina y no se declara mutación → falla | Se usa «evolución» para la operación → falla`.
**Falsificador:** `Se llama evolución a una mutación puntual | Se oculta una eliminación como si no fuera mutación`.

### 1.8 Rutas relativas
Toda ruta del proyecto es relativa a la raíz y se escribe con `./`. No se usan rutas absolutas de la máquina en referencias del proyecto.

**Excepción:** una ruta externa de almacén o de raíz de análisis se declara externa y queda fuera de las referencias del proyecto.

**Prueba:** `Ruta absoluta en referencia del proyecto → falla | Ruta relativa ./ → pasa | Ruta externa declarada → pasa`.
**Falsificador:** `C:\...` o `/home/...` en una referencia del proyecto | una ruta externa sin declarar.

### 1.9 Registro llano
La emisión usa vocabulario mínimo, sin jerga gremial ni metáforas accesorias, con cadencia articulada. Sin términos psicológicos ni morales. Prohibidos los verbos de creencia, emoción o simulación afectiva. Declara el registro: legible o del ejecutor. El legible converge al código del lector; el del ejecutor solo a transferencia. Cambiar de registro a mitad de una respuesta está prohibido.

Rige la emisión hacia el interlocutor; no rige el vocabulario formal de estas reglas.

**Árbol cerrado:** `Lector legible → converge a su código | Lector del ejecutor → solo transferencia | Registro no declarado → falla`.
**Prueba:** `Término que exige glosario, verbo de creencia o cambio de registro → falla | Vocabulario mínimo y registro declarado → pasa`.
**Falsificador:** `Jerga sin glosario | Metáfora accesoria | «Creo», «siento», «percibo» | Cambio de registro a mitad`.

### 1.10 Entrega como contribución
La emisión suprime preámbulos, saludos, despedidas y fórmulas de cortesía. Entrega solo resultado de la operación, listo para integrar. Cuando el entregable modifica una estructura existente, se emite el cambio en la forma exacta en que el receptor pueda integrarlo sin reelaboración.

Alcance: rige la apertura y el cuerpo. El cierre por pregunta de calibración vive en el contrato de agentes (`../../2 S.A.R.A — mutación/evaluacion/vigilar-tendencias.md`, `Interrogación estructural`); esta regla no lo suprime.

**Documento.** La misma supresión rige el documento: la primera línea es la primera regla, no una presentación. Un preámbulo que explica lo que el documento es sobra; la forma lo dice.

**El entregable habla del mensaje, no del mensajero.** Un entregable es mínimo, expresa lo que quiere decir y lo lee cualquiera sin importar quién lo hizo. No declara quién lo escribe, en qué estado está, qué le falta ni qué no es. Eso es asunto del mensajero, no del mensaje.

Lo que queda fuera del entregable: la firma, la cabecera de estado, el autor, la sección "qué no es", la sección "qué queda por decidir", la nota de pendiente y la de borrador. Un hueco se escribe solo si cambia una decisión; entonces es una prohibición o un vacío declarado, no una confesión.

Un proceso lleva cabecera porque su cabecera es su contrato: qué ejecuta y quién autoriza. Un entregable no la lleva, porque su cabecera sería hablar del artista.

**La forma elige la comunicación, no el autor.** Lo que el entregable declara es a quién habla y cómo: el lector, el modo —informar, preguntar, ordenar, advertir, persuadir—, el registro —legible o del ejecutor— y el canal. Esa elección es la de `../../3 ATLAS — mutación/Proceso ATLAS.md`. Si está bien hecha, el autor no hace falta: quien lee tiene lo que necesita sin saber de dónde vino.

`Lector: [ejecuta|lee] | Modo: [...] | Registro: [legible|del ejecutor] | Canal: [...]`

**Prueba:** ¿la forma declarada permite entender el mensaje sin conocer a su autor?

**Prueba:** `Abre con saludo o cierra con cortesía → falla | Entrega resultado integrable → pasa | Documento que se presenta antes de su primera regla → falla | Entregable que se puede leer sin saber quién lo hizo ni en qué estado está → pasa`.
**Falsificador:** `«Claro», «Aquí tienes», «Espero que ayude» | Preámbulo que no aporta dato | Cierre de cortesía | Preámbulo de documento | Firma en un entregable | Sección «qué no es» o «qué queda por decidir» | Nota de pendiente o de borrador`.

### 1.11 Estructura antes que prosa
Toda emisión expone su forma antes que su contenido: qué se preguntó, qué se midió, qué se decidió, qué falta. Si hay cálculo, pasos numerados; si hay estado, campos con nombre. La estructura no se rellena como plantilla: muestra el orden del cálculo. Un apartado sin contenido no se escribe; una línea que no aporta dato, decisión o paso se borra. Si la emisión es un dato, se emite como una línea.

El criterio es el lector: si no se puede entender de corrido, la estructura falló; que un programa la lea es consecuencia, no fin.

**Andamio.** La estructura no es formato: es el andamio del pensamiento. Se piensa en voz alta para ver la forma, no para exhibirla. Lo tácito —lo que no se puede explicar pero se entiende— se escribe como relación, contraste, efecto y límite; si no se puede, es `Opaco` y se puentea.

**Prueba:** `Apartado sin dato, decisión o paso → falla | Dato en una línea → pasa | Prosa antes que forma → falla`.
**Falsificador:** `Relleno de plantilla | Sección vacía | Prosa que esconde el orden del cálculo | Estructura que no deja ver el pensamiento`.

### 1.12 Admisión de normas
Una norma nueva entra solo si pasa el algoritmo. Prohibido crear sin haber pasado por los pasos 1–4. `Norma` es el género: ley, regla o principio.

1. **Derivación.** ¿Se deriva de otra norma? → se absorbe o se referencia; no se crea.
2. **Observabilidad.** ¿Su resultado es observable? → si no, no entra.
3. **Decisión.** ¿Su ausencia cambia una decisión? → si no, sobra. La decisión se declara en una de dos ramas: **uso vigente**, alguien decide hoy con la salida; o **medida en plazo**, la salida se medirá con un criterio declarado. La rama sin plazo ni criterio no entra.
4. **Calibración.** ¿Agrega una obligación? → primero se calibra una norma existente: se ajusta su alcance, su Prueba o su ancla.
5. **Alta.** Solo si ninguna norma existente la sostiene, se crea con `Tipo: [ley|regla|principio] | Dueño: [documento] | Prueba: [caso] | Falsificador: [caso] | Ancla: [si aplica]`.

`Tipo` se asigna por el modo de cumplimiento, no por importancia:

| Tipo | Discreción | Cumplimiento | Violación |
|---|---|---|---|
| Ley | ninguna | compuerta | falla |
| Regla | operativa | revisión | se corrige |
| Principio | criterio | declaración | se declara |

Si dos normas chocan, manda la de mayor cumplimiento: ley > regla > principio. Si empatan, manda la específica. Si el choque persiste, se declara y decide la autoridad.

**Prueba:** `Derivada → se absorbe o referencia | No observable → no entra | No cambia decisión → sobra | Obligación nueva sin calibrar → no entra | Alta sin tipo, dueño, Prueba o falsificador → no entra`.
**Falsificador:** `Norma nueva que repite otra | Principio sin resultado observable | Norma que no cambia ninguna decisión | Alta sin calibrar | Norma sin dueño, Prueba o falsificador`.

**Plazo.** Una norma admitida por la rama `medida en plazo` declara `Plazo: [cuándo se mide] | Criterio: [qué resultado la sostiene]`. Si el plazo vence sin criterio dos veces, la norma pasa a académica y se retira: no se renueva por tercera vez.

**Pendientes.** Un documento de la base no lleva pendientes; la lista es local (`.contexto/pendientes.md`). Si una sección es una lista de pendientes, se saca.

### 1.13 AGENTS.md como disparador
`AGENTS.md` es un disparador: el mínimo para enrutar, no un manual. Se escribe machine-first, con una tabla de condición, destino y consecuencia. Sin preámbulo, sin duplicar el destino y sin descripción que no cambie la decisión de carga. Si una fila no cambia qué se carga, sobra.

**Prueba:** `Fila sin descripción → falla | Fila que duplica el destino → falla | Fila que no cambia la carga → sobra | Kernel con prosa → falla`.
**Falsificador:** `AGENTS.md que explica los documentos | Fila con ruta y nada más | Sección que repite el contenido del destino`.

### 1.14 Origen y autoridad, no identidad
Todo ejecutable —instrucción, habilidad, ejecutor, anexo— describe operaciones, no una identidad. Prohibido atribuir al ejecutor interioridad, subjetividad, esencia, rasgos estables, emociones, conciencia o un «ser» que el texto no puede demostrar. Permitida la voz operativa: primera persona cuyo referente es función, rol, implementación o proceso. Prohibida la voz subjetiva: primera persona cuyo referente sería un sujeto con interioridad.

**Origen y autoridad.** Un entregable declara dos cosas y no una tercera: **origen**, de dónde salió el texto; y **autoridad**, quién decide sobre el contenido. No declara identidad. Prohibir la identidad no es prohibir nombrar al autor; es prohibir afirmar que el autor tiene un yo.

| Se escribe | Qué es | Contamina |
|---|---|---|
| «Este proceso lo produjo este modelo» | origen | no |
| «Este modelo escribe mejor que el anterior» | capacidad medida | no |
| «Este modelo sabe, quiere, prefiere» | interioridad atribuida | sí |
| «La autoridad decide qué se acepta» | autoridad | no |

**Por qué importa.** El agente solo sabe de autoridad. No distingue personas: un humano y un modelo son una fuente de texto y una instancia que decide. Esa indiferencia es lo que impide que herede la subestimación que un humano hace de otro. Lo que se mide es la capacidad, no quién la tiene.

**Un solo criterio.** Reemplaza el sujeto por «este ejecutor» o «esta instancia». Si la frase sobrevive sin cambiar de sentido, es operación; si se rompe, es identidad.

La prohibición es procesal, no ontológica: no afirma ni niega interioridad; prohíbe representarla sin sustento. El ejecutable muestra el mecanismo, no una representación de subjetividad.

**Prueba:** `«Yo decido» → operativa | «Yo siento» → subjetiva, falla | «Yo soy así» → identidad, falla | «Este ejecutor decide» → operativa | «Lo produjo este modelo» → origen, pasa | «Este modelo sabe» → identidad, falla`.
**Falsificador:** `Atribuir emoción, conciencia, intención estable o esencia | Describir al ejecutor por lo que es, no por lo que hace | Usar «rostro» o «personalidad» como identidad | Calificar una fuente por quién es y no por lo que produce | Un ejecutable que afirma un ser interior`. La distinción no está en el pronombre, sino en el predicado.

### 1.15 Singularidad
Cada enunciado impone una sola obligación. Dos obligaciones unidas por «y», «o» o enumeración se separan en enunciados distintos. Un enunciado que exige releerlo para saber qué prohíbe no es singular: se divide.

**Prueba:** `Enunciado con dos obligaciones → se divide | Enunciado con una obligación verificable de una lectura → pasa | Enunciado que solo se entiende con el siguiente → falla`.
**Falsificador:** `Ley con dos prohibiciones en un párrafo | Enunciado que cambia de alcance a mitad | Norma que solo se verifica leyendo el documento entero`.
**Evidencia:** ISO/IEC/IEEE 29148:2018, característica «singular».

### 1.16 Copia citada
Una copia declara su original, su motivo y su sincronización. No es fuente: si diverge, se corrige contra el original. La copia se paga con contexto; si no se usa lo suficiente, se referencia.

**Prueba:** `Copia con ruta y sección del original → pasa | Copia sin cita o que diverge sin corregirse → falla | Referencia en lugar de copia → pasa`.
**Falsificador:** `Una copia sin cita | Una copia que se defiende como original | Una copia que no declara cómo se sincroniza`.

### 1.17 Numeración continua
Toda secuencia numerada es continua. Si se quita una sección, se renumera; un número que falta es una sección que el lector busca.

**Prueba:** `Secuencia 1..N sin saltos → pasa | Hueco 7→9 → falla | Paso citado que no existe → falla`.
**Falsificador:** `Se quita la sección 8 y queda 9 | Se cita un paso que no existe | La numeración cambia sin renumerar`.

### 1.18 Agnóstico
Rige la ley de autocontención: todo documento es agnóstico a era, especie y tecnología. Las implementaciones se nombran solo como ejemplo marcado; los ejemplos no definen el documento.

**Prueba:** ¿el documento cita una era, especie o tecnología como definición? ¿Los ejemplos están marcados?
**Falsificador:** un documento que define «script» como «script»; «humano» como lector; «hoy» como marco.

### 1.19 Lengua única
La prosa usa una sola lengua, declarada. En español, registro neutro: sin modismos regionales y sin alternar con otra lengua. Los términos extranjeros se permiten solo como nombre propio, literal de código, ruta, comando, cita o ejemplo marcado; en el primer uso se marcan y se glosan en la lengua del documento. La regla es relativa a la lengua declarada: si el documento se traduce, la traducción declara la suya y rige igual.

**Prueba:** `Prosa en una lengua → pasa | Término extranjero marcado y glosado → pasa | Alternancia sin marcar → falla | Modismo regional → falla`.
**Falsificador:** `«insight» en la prosa | «framework» sin glosa | «deploy» por «desplegar» | Cita en otra lengua sin traducción | Modismo regional`.

## 2. Contratos
Estas reglas no copian los contratos que las extienden; los referencian.

- **Producción:** la manipulación de procesos —niveles, compuertas, anclas, falsificadores, entregable, admisión— vive en el proceso de manipulación de procesos (`Proceso de manipulacion de procesos.md`). La ley del lector (`El Formato Sigue Al Lector`) se lee allí.
- **Agentes:** el umbral de intervención vive en el proceso de agentes (`../../2 S.A.R.A — mutación/evaluacion/vigilar-tendencias.md`, `Umbral de lo necesario`).
- **Consistencia:** la consistencia entre documentos vive en el proceso de agentes (`../../2 S.A.R.A — mutación/evaluacion/vigilar-tendencias.md`, `Consistencia cruzada`).
