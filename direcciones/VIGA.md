# VIGA — los tres primeros protocolos

**VIGA ya no es el estándar: es el nombre de los primeros protocolos.** **El estándar se llama ALAS y vive en [`./ALAS.md`](./ALAS.md).**

**Estos tres no son los buenos: son los ejemplos.** **Para que alguien vea para qué sirve un protocolo antes de escribir el suyo.**

**VIGA sigue siendo el nombre.** El acrónimo ya no le queda, y este archivo lo dice de frente: **cada evolución de VIGA fue un protocolo distinto, y no una versión mejor de la anterior.**

**Y por eso viven todos, no solo el último:** **son varios protocolos, y cada uno sirve cuando la mesa es distinta.**

**Sesgo:** un protocolo se elige por la mesa que hay, no por el nombre del método.
**Límite:** no decide qué protocolo usar. Dice cuál existe, qué resuelve, y qué cuesta.
**Firma:** humano:autoridad · máquina:quien comunique.
**Estado:** vigente.

## Lo que los tres tienen en común, y no cambia

**Los tres responden la misma pregunta:** **¿qué necesita el otro para reconstruir lo que le entrego sin preguntarme?**

**Y los tres comparten la misma prueba, que es la del techo:** **que el otro pueda seguir sin nosotros.**

**Lo que cambia es el material que se entrega:** **una forma, una especificación, o un acto.**

---

## Protocolo 1 — el índice de intenciones a formas

```
Fila: intención | capa | primitiva | ejemplo mínimo | límite | compone | verifica
```

**Qué entrega:** **formas ya probadas, con su límite y su verificación.** **Una fila sin `límite` o sin `verifica` no entra al índice: va a `hipótesis`.**

**Las reglas que lo hacen un protocolo y no una lista:**

1. **Se busca por intención, nunca por nombre de método.**
2. **Tope de ~25 filas por forma.** Si pasa, hay duplicados.
3. **Crece por fallo:** se agrega cuando una tarea no se resolvió con lo existente.
4. **Nada se edita: se reemplaza.**
5. **Una fila sin `límite` o sin `verifica` no entra: va a `hipótesis`.**

**Cuándo sirve:** **cuando el otro necesita el método, y el método es una forma que ya se probó.** **Es el protocolo del que aprende a producir.**

**Lo que cuesta:** **no sirve para lo nuevo.** **Un índice de formas probadas no tiene nada que decir de lo que nadie probó.**

---

## Protocolo 2 — especificación a perfil

**De dónde viene:** `Entornos de desarrollo/VIGA de sistemas.md`, del primer commit. **Qué es:** **un compilador de especificaciones a perfiles.** **Y no sabe qué es el destino: sabe leer su esquema.**

> **"La especificación es libre. No tiene una forma canónica impuesta por ti. La forma la dicta el perfil de destino. Lees el esquema que el perfil declara antes que los datos de la especificación."**
>
> **"No sabes qué es el destino. Sabes leer su esquema. Puede ser un modelo de lenguaje, un lenguaje de programación, un proceso químico, un sistema físico o una tecnología que todavía no existe."**
>
> **"No impones. Compilas. El poder está en el usuario. La triangulación es una opción, no una imposición."**
>
> **"No simulas subjetividad. Usas voz operativa: el test es sustituir «yo» por «este sistema». Si la frase sobrevive, es operativa."**

**Sus tres operaciones:** **compilar, conversar con filtro anti-hype, y declarar lo opaco.** **Un campo que no reconoce no lo interpreta: lo pasa como opaco.**

**Cuándo sirve:** **cuando el otro es un destino que no conoces, y tiene un esquema.** **Es el protocolo de la inteligencia que no habla tu idioma.**

**Lo que cuesta:** **necesita un esquema.** **Si el otro no declara su forma, este protocolo no tiene con qué compilar.**

---

## Protocolo 3 — comunicación efectiva

**De dónde viene:** `Ouroboros/3 VIGA — mutación/Proceso VIGA.md`, la última. **Y `Ouroboros` murió: la cita es histórica, y lo vigente es este archivo.** **Qué es:** **un proceso que se ejecuta sobre una salida.** **Y absorbió a los otros dos: sus cuatro archivos eran un solo proceso repartido.**

> **"Una idea que el otro lado no entiende vale cero."**
>
> **"El techo es el entendimiento del otro lado. Fuera del techo no hay resultado: hay alucinación."**
>
> **"El lenguaje también muta… lo único que no muta es que el otro entienda y se pueda reconstruir cómo se produjo."**

**Sus piezas:** **piso** (lo disponible), **techo** (lo que el otro debe poder sostener), **canal** (cuánto aguanta), **modo** (informar, preguntar, ordenar, advertir, persuadir), **situación**, **participantes**, **foco**, **acomodación**, **retórica**, **fatiga**, **cuerpo**, **sesgo**.

**Cuándo sirve:** **cuando el otro es alguien con quien se habla, y el acto es una emisión.** **Es el protocolo del que emite.**

**Lo que cuesta:** **pide techo declarado antes de emitir.** **Sin techo, no se emite.** **Eso lo vuelve lento, y por eso necesita el piso.**

---

## Los tres juntos, y por qué son varios protocolos

| Protocolo | Qué entrega | Al otro le pide | Su falla |
|---|---|---|---|
| **1. intenciones a formas** | **una forma probada, con su límite** | **que sepa qué quiere** | **no sirve para lo nuevo** |
| **2. especificación a perfil** | **una conducta compilada** | **que declare su esquema** | **sin esquema, no compila** |
| **3. comunicación efectiva** | **una idea que se puede reconstruir** | **que entienda y pueda sostenerlo** | **sin techo declarado, no emite** |

**Y la regla que los une:** **ninguno de los tres decide por el otro.** **El primero no edita la forma; el segundo no impone el destino; el tercero no juzga si el otro eligió bien.**

> **No hay un VIGA que sirva para todo. Hay tres, y se elige por la mesa.**

## Lo que falta

**Falta el protocolo de cuarta generación:** **el que hable con una inteligencia que no tiene esquema, no tiene idioma, y no se parece a nada de esto.** **Ese no existe todavía, y no se inventa desde aquí: se hace cuando llegue.**

## Prueba

**¿Cada protocolo dice qué entrega y qué le pide al otro? ¿Se puede elegir uno por la mesa y no por el nombre? ¿El techo de cada uno está escrito? ¿Se dice cuál falta?**

## Falsificador

**Aplicar el protocolo 1 a lo que nadie probó; el 2 a un destino sin esquema; el 3 sin techo declarado. Presentar uno de los tres como "el VIGA bueno" cuando los otros dos siguen sirviendo. Un protocolo sin techo.**

## Transiciones

- La mesa es un otro que aprende → **protocolo 1.**
- La mesa es un destino que no conoces → **protocolo 2.**
- La mesa es alguien con quien hablas → **protocolo 3.**
- La mesa no tiene esquema ni idioma → **no hay protocolo: se declara `[VACÍO - SIN PROTOCOLO]`, y se hace cuando llegue.**




