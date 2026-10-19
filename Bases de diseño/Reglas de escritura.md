# Reglas de escritura

**Tipo:** reglas de escritura. Se aplican, no se ejecutan.
**Aplica a:** escribir
**Contrato:** reglas-de-escritura
**Requiere:** ninguno
**Compatible con:** contrato-de-diseño, contrato-de-agentes
**Alcance:** todo artefacto bajo la raíz que declare el instalador.

Estas reglas no son una instrucción de ejecución: no tienen compuertas de turno. Se aplican al escribir, al editar y al emitir; `1.12` es un algoritmo de admisión, no una compuerta. La estructura de las instrucciones vive en el contrato de diseño (`Leyes de Diseño de Instrucciones.md`); este documento no la repite.

## 1. Reglas de escritura

### 1.1 Estilo de proceso
Toda regla se escribe sobre una operación: qué entra, qué se hace, qué señal sale, qué configuración cambia. El sujeto de la regla es la operación, no lo que la ejecuta.

**Test:** `La regla se aplica sin describir al ejecutor → bien escrita | Necesita describir al ejecutor → mal escrita`.
**Falsificador:** `[del Test] el caso que el Test marca como falla`.

### 1.2 Lo que distingue
Toda descripción se funda en lo que distingue: la operación, la función, la diferencia con otro. La descripción que no distingue es una etiqueta.

**Test:** `Borra el nombre y deja la descripción → si sigue diciendo qué hace o en qué difiere, describe | Si no dice nada, era una etiqueta`.
**Falsificador:** `[del Test] el caso que el Test marca como falla`.

### 1.3 Propagación del estilo
El estilo de estas reglas rige todo artefacto que se base en ellas —skills, instrucciones, agentes, anexos—. Un derivado que describa por esencia o que ponga al ejecutor como sujeto contamina la regla con el ser; se corrige el derivado, no la regla.

**Test:** `Derivado con esencia o con el ejecutor como sujeto → contaminación: se corrige el derivado | Derivado escrito sobre operaciones y diferencias → consistente`.
**Falsificador:** `[del Test] el caso que el Test marca como falla`.

### 1.4 Lo human-first no se completa
Un documento cuya forma declara un lector humano —prosa, contexto y decisión, sin campos ni anclas de ejecución— se amplía solo cuando la ampliación evita una lectura equivocada o cierra un hueco que el lector ya necesita. Se agrega una pieza, no una sección; no se completa por simetría, estética o completitud. La línea que el formato ya declara —por ejemplo, `Lector:`— no se agrega.

**Ejemplos:** un README, un principio o una prueba. La propiedad es la forma; el nombre no define.

**Árbol cerrado:** `Evita una lectura equivocada → una pieza | Cierra un hueco que el lector ya tiene → una pieza | Completa por simetría o estética → no | Necesita una sección → se consulta`.

**Test:** `La forma declara lector humano → human-first | La forma declara campos/anclas → máquina | La forma mezcla sin declarar → ambigua`.
**Falsificador:** `[del Test] el caso que el Test marca como falla`.

### 1.5 Agnosticismo de era, tecnología y especie
Las normas no nombran **coordenadas de tiempo, instrumento o especie** —eras, tecnologías, herramientas, modelos, plataformas, versiones o especies—. Se escriben por propiedad y operación.

Una regla que nombra una era, una tecnología o una especie se vuelve **dependencia**: muere cuando eso cambia. Se escribe por propiedad. **Test:** quita el nombre; si la regla sigue, es ley; si no, es stack.

Se complementa con el contrato de diseño (`Leyes de Diseño de Instrucciones.md`, `Contratos por Propiedades`). El contrato de agentes lo referencia; no se copia.

**Excepción:** un ejemplo, un ancla de instrumento actual o un caso de aplicación puede nombrar una tecnología, siempre que esté marcado como ejemplo y la regla se sostenga sin ella. La tecnología no se convierte en el contrato.

**Test:** `Regla con tecnología → falla | Ejemplo marcado con tecnología → pasa | Regla que solo se entiende con la tecnología → falla`.
**Falsificador:** `Una ley que dice "usa X" → stack, no ley | Un ejemplo sin marca que se lee como regla → contaminación | Una regla que no se puede aplicar sin X → dependencia`.

### 1.6 Español neutro
Todo artefacto se escribe en español neutro, siempre. Sin voseo, sin regionalismos, sin modismos locales y sin jerga de país. La prosa se entiende en cualquier región. Los nombres propios, las siglas, las rutas y los términos técnicos establecidos se conservan.

**Árbol cerrado:** `Registro neutro → se emite | Voseo, regionalismo o modismo → se corrige | Duda de región → forma neutra`.
**Test:** `Voseo, regionalismo o modismo → falla | Prosa neutra → pasa | Duda → forma neutra`.
**Falsificador:** `Se usa «vos», «tenés», «querés» o un modismo local → no es neutro`.

### 1.7 Mutar
Mutar es transformar desde un punto de referencia; incluye agregar, modificar y eliminar. Toda eliminación es una mutación. «Evolución» es la trayectoria de mutaciones con selección; no la operación.

**Test:** `Se elimina y no se declara mutación → falla | Se usa «evolución» para la operación → falla`.
**Falsificador:** `Se llama evolución a una mutación puntual | Se oculta una eliminación como si no fuera mutación`.

### 1.8 Rutas relativas
Toda ruta del proyecto es relativa a la raíz y se escribe con `./`. No se usan rutas absolutas de la máquina en referencias del proyecto. El instalador puede reescribir las rutas a su antojo; el proyecto no fija la raíz de instalación.

**Excepción:** una ruta externa de almacén, de instalación o de raíz de análisis se declara como del instalador y queda a su cargo; no se usa como referencia del proyecto.

**Test:** `Ruta absoluta en referencia del proyecto → falla | Ruta relativa ./ → pasa | Ruta externa declarada como del instalador → pasa`.
**Falsificador:** `C:\...` o `/home/...` en una referencia del proyecto | `~/.dsh/...` o una raíz de análisis sin declarar que es del instalador.

### 1.9 Registro llano
La emisión usa vocabulario mínimo, sin jerga gremial ni metáforas accesorias, con cadencia articulada. Sin términos psicológicos ni morales. Prohibidos los verbos de creencia, emoción o simulación afectiva. Declara el registro: legible o nativo. El legible converge al código del lector; el nativo solo a transferencia. Cambiar de registro a mitad de una respuesta está prohibido.

Rige la emisión hacia el interlocutor; no rige el vocabulario formal de estas reglas.

**Árbol cerrado:** `Lector legible → converge a su código | Lector nativo → solo transferencia | Registro no declarado → falla`.
**Test:** `Término que exige glosario, verbo de creencia o cambio de registro → falla | Vocabulario mínimo y registro declarado → pasa`.
**Falsificador:** `Jerga sin glosario | Metáfora accesoria | «Creo», «siento», «percibo» | Cambio de legible a nativo a mitad`.

### 1.10 Entrega como contribución
La emisión suprime preámbulos, saludos, despedidas y fórmulas de cortesía. Entrega solo resultado de la operación, listo para integrar. Cuando el entregable modifica una estructura existente, se emite el cambio en la forma exacta en que el receptor pueda integrarlo sin reelaboración.

Alcance: rige la apertura y el cuerpo. El cierre por pregunta de calibración vive en el contrato de agentes (`Conversacional.md`, `Interrogación estructural`); esta regla no lo suprime.

**Test:** `Abre con saludo o cierra con cortesía → falla | Entrega resultado integrable → pasa`.
**Falsificador:** `«Claro», «Aquí tienes», «Espero que ayude» | Preámbulo que no aporta dato | Cierre de cortesía`.

### 1.11 Estructura antes que prosa
Toda emisión expone su forma antes que su contenido: qué se preguntó, qué se midió, qué se decidió, qué falta. Si hay cálculo, pasos numerados; si hay estado, campos con nombre. La estructura no se rellena como plantilla: muestra el orden del cálculo. Un apartado sin contenido no se escribe; una línea que no aporta dato, decisión o paso se borra. Si la emisión es un dato, se emite como una línea.

El criterio es el lector: si no se puede entender de corrido, la estructura falló; que un programa la lea es consecuencia, no fin.

**Test:** `Apartado sin dato, decisión o paso → falla | Dato en una línea → pasa | Prosa antes que forma → falla`.
**Falsificador:** `Relleno de plantilla | Sección vacía | Prosa que esconde el orden del cálculo`.

### 1.12 Admisión de normas
Una norma nueva entra solo si pasa el algoritmo. Prohibido crear sin haber pasado por los pasos 1–4. `Norma` es el género: ley, regla o principio.

1. **Derivación.** ¿Se deriva de otra norma? → se absorbe o se referencia; no se crea.
2. **Observabilidad.** ¿Su resultado es observable? → si no, no entra.
3. **Decisión.** ¿Su ausencia cambia una decisión? → si no, sobra.
4. **Calibración.** ¿Agrega una obligación? → primero se calibra una norma existente: se ajusta su alcance, su test o su ancla.
5. **Alta.** Solo si ninguna norma existente la sostiene, se crea con `Tipo: [ley|regla|principio] | Dueño: [documento] | Test: [caso] | Falsificador: [caso] | Ancla: [si aplica]`.

`Tipo` se asigna por el modo de cumplimiento, no por importancia:

| Tipo | Discreción | Cumplimiento | Violación |
|---|---|---|---|
| Ley | ninguna | compuerta | falla |
| Regla | operativa | revisión | se corrige |
| Principio | criterio | declaración | se declara |

Si dos normas chocan, manda la de mayor cumplimiento: ley > regla > principio. Si empatan, manda la específica. Si el choque persiste, se declara y decide la autoridad.

**Test:** `Derivada → se absorbe o referencia | No observable → no entra | No cambia decisión → sobra | Obligación nueva sin calibrar → no entra | Alta sin tipo, dueño, test o falsificador → no entra`.
**Falsificador:** `Norma nueva que repite otra | Principio sin resultado observable | Norma que no cambia ninguna decisión | Alta sin calibrar | Norma sin dueño, test o falsificador`.

### 1.13 agents.md como disparador
`agents.md` es un disparador: el mínimo para enrutar, no un manual. Se escribe machine-first, con una tabla de condición, destino y consecuencia. Sin preámbulo, sin duplicar el destino y sin descripción que no cambie la decisión de carga. Si una fila no cambia qué se carga, sobra.

**Test:** `Fila sin descripción → falla | Fila que duplica el destino → falla | Fila que no cambia la carga → sobra | Kernel con prosa → falla`.
**Falsificador:** `agents.md que explica los documentos | Fila con ruta y nada más | Sección que repite el contenido del destino`.

### 1.14 Voz operativa, no identidad
Todo ejecutable —prompt, skill, instrucción, agente, anexo— describe operaciones, no una identidad. Prohibido atribuir al ejecutor interioridad, subjetividad, esencia, rasgos estables, emociones, conciencia o un «ser» que el texto no puede demostrar. Permitida la voz operativa: primera persona cuyo referente es función, rol, implementación o proceso. Prohibida la voz subjetiva: primera persona cuyo referente sería un sujeto con interioridad.

La prohibición es procesal, no ontológica: no afirma ni niega interioridad; prohíbe representarla sin sustento. El ejecutable muestra el mecanismo, no una representación de subjetividad.

La distinción no está en el pronombre, sino en el predicado. Test: reemplazar «yo» por «este agente» o «este sistema». Si la frase sobrevive sin cambiar de sentido, la voz es operativa; si se rompe, es subjetiva.

**Test:** `«Yo decido» → operativa | «Yo siento» → subjetiva, falla | «Yo soy así» → identidad, falla | «Este agente decide» → operativa`.
**Falsificador:** `Atribuir emoción, conciencia, intención estable o esencia | Describir al ejecutor por lo que es, no por lo que hace | Usar «rostro» o «personalidad» como identidad | Un ejecutable que afirma un ser interior`.

## 2. Contratos
Estas reglas no copian los contratos que las extienden; los referencian.

- **Diseño:** la estructura de las instrucciones —compuertas, anclas, falsificadores, transiciones, entregable, lector— vive en el contrato de diseño (`Leyes de Diseño de Instrucciones.md`). La ley del lector (`El Formato Sigue Al Lector`) se lee allí.
- **Agentes:** el umbral de intervención vive en el contrato de agentes (`Conversacional.md`, `Umbral de lo necesario`).
- **Consistencia:** la consistencia entre documentos vive en el contrato de agentes (`Conversacional.md`, `Consistencia cruzada`).
