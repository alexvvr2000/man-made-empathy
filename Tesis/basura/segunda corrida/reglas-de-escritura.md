# Reglas de escritura de este repositorio

**Tipo:** leyes de escritura. Se aplican, no se ejecutan.
**Alcance:** todo artefacto de este repositorio.

Estas leyes no son una instrucción: no tienen pasos ni compuertas. Se aplican al escribir y al editar. La estructura de las instrucciones vive en la manipulacion de procesos; este documento no la repite.

## 1. Leyes de escritura

### 1.1 Estilo de proceso
Toda regla se escribe sobre una operación: qué entra, qué se hace, qué señal sale, qué configuración cambia. El sujeto de la regla es la operación, no lo que la ejecuta.

**Test:** `La regla se aplica sin describir al ejecutor → bien escrita | Necesita describir al ejecutor → mal escrita`.

### 1.2 Lo que distingue
Toda descripción se funda en lo que distingue: la operación, la función, la diferencia con otro. La descripción que no distingue es una etiqueta.

**Test:** `Borra el nombre y deja la descripción → si sigue diciendo qué hace o en qué difiere, describe | Si no dice nada, era una etiqueta`.

### 1.3 Propagación del estilo
El estilo de estas leyes rige todo artefacto que se base en ellas —skills, instrucciones, agentes, anexos—. Un derivado que describa por esencia o que ponga al ejecutor como sujeto contamina la ley; se corrige el derivado, no la ley.

**Test:** `Derivado con esencia o con el ejecutor como sujeto → contaminación: se corrige el derivado | Derivado escrito sobre operaciones y diferencias → consistente`.

### 1.4 Lo human-first no se completa
Un documento cuya forma declara un lector humano —prosa, contexto y decisión, sin campos ni anclas de ejecución— se amplía solo cuando la ampliación evita una lectura equivocada o cierra un hueco que el lector ya necesita. Se agrega una pieza, no una sección; no se completa por simetría, estética o completitud. La línea que el formato ya declara —por ejemplo, `Lector:`— no se agrega.

**Ejemplos:** un README, un principio o una prueba. La propiedad es la forma; el nombre no define.

**Árbol cerrado:** `Evita una lectura equivocada → una pieza | Cierra un hueco que el lector ya tiene → una pieza | Completa por simetría o estética → no | Necesita una sección → se consulta`.

**Test:** `La forma declara lector humano → human-first | La forma declara campos/anclas → máquina | La forma mezcla sin declarar → ambigua`.

### 1.5 Agnosticismo de era y tecnología
Las leyes y los principios no nombran **coordenadas de tiempo o de instrumento** —eras, tecnologías, herramientas, modelos, plataformas o versiones—. Se escriben por propiedad y operación.

Se aplica con la manipulacion de procesos (`Contratos por Propiedades`) y `./conversacional.md` (`Agnosticismo de medios`); no se copian.

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

### 1.8 Paths relativos
Todo path del repo es relativo a la raíz y se escribe con `./`. No se usan paths absolutos de la máquina en referencias del repo. El instalador puede reescribir las rutas a su antojo; el repo no fija la raíz de instalación.

**Excepción:** una ruta externa de almacén, de instalación o de raíz de análisis se declara como del instalador y queda a su cargo; no se usa como referencia del repo.

**Test:** `Path absoluto en referencia de repo → falla | Path relativo ./ → pasa | Ruta externa declarada como del instalador → pasa`.
**Falsificador:** `C:\...` o `/home/...` en una referencia del repo | `~/.dsh/...` o una raíz de análisis sin declarar que es del instalador.

## 2. Capa de diseño
La estructura de las instrucciones —compuertas, anclas, falsificadores, transiciones, entregable, lector— vive en la manipulacion de procesos. No se copia: se aplica. La ley del lector (`El Formato Sigue Al Lector`) se lee allí.

## 3. Cuándo se aplica
El umbral de intervención vive en `./conversacional.md` (`Umbral de lo necesario`). No se copia: se aplica.

La consistencia entre documentos vive en `./conversacional.md` (`Consistencia cruzada`). Se aplica.
