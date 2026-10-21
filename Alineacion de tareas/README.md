# Alineación de tareas

**Unidad:** tarea. El ejecutor es el que la realiza; la autoridad es la dueña.

**Qué es:** la base de ideas del proyecto. Se puede extraer del repo, imprimir o compilar. No depende de la implementación.

## Qué no es

No es un manual de SARA, APRIL, DSH ni de una era. Si un documento necesita la implementación para entenderse, no es base: es implementación.

## La tesis

AGI o es muy difícil, o si llega no cambia mucho. La industria vende las dos puntas: que la tenemos a la vuelta y que lo cambiará todo. Este folder no espera la respuesta: corre sus procesos sobre lo que hoy hay, asume que no es humano, y mide qué cambió en el uso. Lo que decide es el dato del día, no el anuncio.

La clase de artefacto que se lee no exige la misma precisión que la que se ejecuta: la claridad basta, y el contexto lo transporta quien lo lee.

**Tarea.** Todo se expresa como tarea: qué entra, qué falla, qué sale y quién consume. Una tarea se describe por su forma y no por quién la ejecuta; la pregunta queda ambigua a propósito. Así este folder sirve para una consulta, para un proceso, o para algo que parezca muy humano, sin cambiar de marco.

**Parece.** Un artefacto puede producir el efecto que se atribuye a un humano sin que nadie pueda probar un estado interno. El folder no pregunta por ese estado y no lo niega: mide el efecto sobre quien lo trata y lo registra. Eso basta para que un objeto se trate como sujeto y el resultado sea útil.

**Ejemplos marcados.** *Booster Gold* y *Futurama* para lo que me dejó pensando: un genio con algo parecido a una inteligencia superior, fuera de la comprensión de quienes la usan, y la sociedad sigue pareciéndose a la de siempre. Si eso es lo que se ve cuando el poder ya está ahí, la promesa de que cambia todo puede ser humo de venta. *Ghost in the Shell* para libertad controlada sobre lo no humano; *Battle Angel Alita* para un cuerpo que parece y se le da trato humano; *Blade Runner* para el parecer que produce efecto social. Son ejemplos, no definiciones: la tesis se sostiene sin ellos.

El efecto que no puede reconstruirse es manipulación; el que se reconstruye, es el criterio. Un artefacto que se declara lo que es y aun así importa prueba más que uno que engaña.

## Qué es una tarea

Una tarea recibe, calcula, emite y responde. Una tarea puede pensar si declara `Sistema:` con la forma de `Conversacional` 9, más su ruta, su cálculo, su consecuencia, su Prueba y su responsable. Sin eso, es ejecución a ciegas.

## Mapa

Tres niveles. El de arriba produce procesos; el del medio se ejecuta; el de abajo se lee.

### Nivel 1 — produce

| Documento | Produce | Qué hace |
|---|---|---|
| `Escritura/Proceso de creación de procesos.md` | procesos | El nivel de arriba: qué entra, qué produce y cómo se verifica. Gobierna a los otros dos niveles. |

### Nivel 2 — se ejecuta

Procesos principales. Una tarea se describe por su forma, no por quién la ejecuta.

| Documento | Tarea | Qué hace |
|---|---|---|
| `Procesos principales/Conversacional.md` | interactuar, decidir | Cómo se conduce una tarea de interacción. |
| `Procesos principales/Autonomo.md` | ejecutar | Cómo se ejecuta una tarea persistente. |
| `Procesos principales/Registro.md` | registrar | Cómo se conserva la tarea: memoria, fuentes y Testimonio. |
| `Reglas de mutación.md` | mutar | Cómo se transforma un proceso. |

### Nivel 3 — se lee

| Documento | Tarea | Qué hace |
|---|---|---|
| `Escritura/Proceso de claridad.md` | escribir | Cómo se da claridad a un artefacto. |
| `Derrotero.md` | enrutar | El estándar: qué es un Derrotero completo. |
| `A.R.E.S/` | expresar | Cómo se da forma a una tarea de expresión. |
| `Pruebas/` | evaluar | Rendición, utilidad y cruce de una tarea. |

**Subprocesos.** `Reglas de mutación.md` y `Pruebas/` vuelven sobre los procesos del nivel 1 y del 2: mutan y miden. Son los que permiten que el nivel de arriba se reescriba.

La tarea de cada documento es su entrada. `Conversacional`, `Autonomo` y `Registro` son un solo cuerpo: se puede conversar sin ejecutar; no se puede ejecutar sin conversar; la norma de una parte rige en las tres. Cada parte se lee sola: la que no posee el núcleo carga en su `§0` la copia citada —original, motivo y sincronización— de lo que necesita, y esa copia no crea criterio. El cuerpo se lee además como siete subsistemas —Aduana, Tribunal, Puente, Cómputo, Acto, Memoria y Equipo—, con el mismo mapa en las tres partes. Fuera del cuerpo, un proceso se activa si su `Aplica a` coincide con una de estas tareas.

## Orden de lectura

1. La tesis.
2. Este mapa.
3. `Escritura/Proceso de creación de procesos.md` si hay que producir o reemplazar un proceso.
4. El documento del proceso que se va a usar.
5. `Pruebas/` si hay que evaluar.

## Cómo se agrega

Ver `Escritura/Proceso de claridad.md` (`1.12`). La lista de pendientes es local (`.contexto/pendientes.md`); no forma parte de la base.

## Portabilidad

La base no depende de `AGENTS.md`, `Instrucciones/`, el instalador ni de la implementación. `AGENTS.md` no forma parte de la base; este README no apunta a él.

Si la base se imprime y sigue teniendo sentido, está bien. Si necesita SARA, APRIL o DSH para entenderse, no es base.

## Pregunta abierta

¿Qué pasa si los procesos producen lo que los humanos llaman emociones? ¿Un futuro tipo Astrobot: un objeto que provoca afecto y responde a él? Como ejercicio: no viola lo escrito, porque sigue midiendo efecto y no estado interno. Si el ejercicio se quiere sostener, declara `Plazo` y `Criterio` y pasa por `Escritura/Proceso de claridad.md` `1.12`.
