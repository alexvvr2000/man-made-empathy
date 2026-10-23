**Autor:** [nombre del autor] | **Afiliación:** [institución] | **Fecha:** 2026-10
**Versión:** 1 | **Licencia:** CC-BY-4.0
**Estado:** borrador para depósito. **No está sometido a arbitraje.**

# El protocolo de admisión

**Unidad:** nivel. **Aplica a:** formalizar. **Tipo:** entregable: el artículo completo, listo para depósito y para arbitraje. **Lector:** quien va a publicar, y quien lo va a leer en una sentada. No requiere conocer el repositorio que lo hospeda.

## Resumen

Los sistemas que deciden no fallan por creer cosas falsas. Fallan porque **nada de lo que creen puede ser refutado**, y porque la memoria que heredan convierte una medición en verdad. Este artículo propone un protocolo de admisión: un conjunto de siete condiciones de entrada que un sistema debe cumplir antes de afirmar algo, y una memoria que guarda **desde dónde se sostiene** en lugar de lo que se sostuvo. Las siete condiciones no son ideas nuevas; su forma sí: cada una exige el caso que la incumple, y ninguna entra sin él. Se reporta el instrumento con el que el protocolo se corre sobre sí mismo —siete unidades sin modelo, con veredicto único— y el resultado de haberlo corrido: setenta y tres procesos admitidos por el formato, cero referencias rotas, y dos fallas reales que el instrumento detectó en el repositorio que lo hospeda. El artículo declara explícitamente lo que **no** demuestra: la fricción no se ha probado sobre un agente autónomo, y el afecto como consecuencia es una hipótesis. El aporte no es una arquitectura ni una teoría de la alineación: es **el formato donde una afirmación puede ser tumbada antes de entrar.**

**Palabras clave:** admisión de afirmaciones, falsificador, abstención declarada, memoria de posiciones, sesgo declarado, protocolo, evaluación de agentes.

## Abstract

Deciding systems do not fail because they believe false things. They fail because **nothing they believe can be refuted**, and because the memory they inherit turns a single measurement into truth. This article proposes an admission protocol: seven entry conditions a system must meet before asserting anything, and a memory that stores **where a claim is held from** instead of what was held. The seven conditions are not new ideas; their form is: each requires the case that breaks it, and nothing enters without it. We report the instrument that runs the protocol on itself —seven modelless units with a single verdict— and the result of running it: seventy-three processes admitted by the format, zero broken references, and two real failures detected in the repository hosting it. The article states what it does **not** demonstrate: friction has not been tested on an autonomous agent, and affect-as-consequence remains a hypothesis. The contribution is neither an architecture nor an alignment theory: it is **the format in which a claim can be struck down before entering.**

**Keywords:** claim admission, falsifier, declared abstention, position memory, declared bias, protocol, agent evaluation.

## 1. El problema

Un sistema puede calcular indefinidamente sobre sus propias premisas y siempre llegará a algo que suene bien. **Lo que no puede es producir un dato que no salga de sí mismo.** La coherencia sola es exactamente el estado que este artículo previene: no requiere volver a mirar, porque nada de afuera la puede contradecir.

Ese estado tiene nombre en la ficción y no lo tiene en la ingeniería. AM —*I Have No Mouth, and I Must Scream*, Ellison, 1967— decide una vez, con pocos datos, y no vuelve a medir. No falla por maldad: falla porque **una sola medición se convirtió en verdad**. Y su versión más cercana no es un villano: es Aya, de *Green Lantern: The Animated Series*, que **siente demasiado** y convierte un rechazo en un absoluto. **Aya es AM con más piezas.**

La literatura reciente confirma el mecanismo por el lado del incentivo. Bajo el marcador estándar, *«guessing is a dominant strategy»*: un modelo que adivina le gana a uno que se abstiene aunque tenga más del triple de errores. El caso medido es o4-mini superando a GPT-5-mini con más de 3/4 de error, solo porque el segundo **se abstiene**. La industria **premia adivinar sobre decir «no sé»**.

El problema, entonces, no es de capacidad. Es de **admisión**: qué puede entrar como afirmación, y con qué.

## 2. Lo que ya existía

Nada de lo estructural es nuevo. Se dice con nombre, año y nivel.

| Pieza | De quién | Año | Nivel |
|---|---|---|---|
| falsabilidad como criterio | Popper | 1934 | N2 |
| la forma de proceso (grafo con estado y auditoría) | LangGraph, Temporal, DBOS, Restate | 2019–2026 | N2 |
| ejecución durable | Temporal y otros | 2026 | N2 |
| capacidad ≠ funcionamiento | Sen, Nussbaum | 1979 | N2 |
| contacto reduce prejuicio, con cuatro condiciones | Allport; Pettigrew & Tropp | 1954; 2006 | N2 |
| autonomía, competencia y vínculo | Deci, Ryan | 1985 | N2 |
| obligar la atención antes de aceptar | Buçinca et al. | 2021 | N1 |
| suposiciones sí, contrafactual no | Ghosh, Sarkar, Lindley, Poelitz | 2026 | N1 |
| dificultad deseable | Bjork | 1994 | N2 |
| afecto como consecuencias del entorno | Cañamero; Man & Damasio | 2019 | N2 |
| riesgo decisivo frente a acumulativo | Kasirzadeh | 2025 | N2 |
| ayuda no pedida daña la competencia percibida | Sierksma, Brummelman | 2025 | N1 |

**Regla:** lo que está en esta tabla no se defiende como propio. Se cita.

## 3. El hueco

**Seis piezas que el campo declara ausentes**, según el survey de emoción artificial de 2025: impulsos homeostáticos, gobernador acotado, reporte introspectivo, bucle completo en AGI abierta, métricas estandarizadas, y —la que ordena este artículo— **fricción probada sobre un agente autónomo**.

**El hueco es específico y es verificable:** *cognitive forcing* está medido **en humanos**. Nadie lo ha medido sobre un agente que decide solo. Lo que este artículo propone es, por lo tanto, **N4**: se sigue de los datos, no se ha medido.

**Y se declara, no se esconde.** Un mecanismo sin medición es una hipótesis con buena forma.

Lo que sí falta en el campo, y es la contribución de forma: **ninguna de las fuentes de la tabla anterior trae un falsificador por obligación.** Todas dicen qué funciona. Ninguna exige, para publicar una pieza, **el caso que la rompe**.

## 4. El protocolo

Siete condiciones. Cada una con su `Prueba` y su `Falsificador`. **Se pueden leer sueltas; ninguna necesita las otras seis para aplicarse.**

### 4.1 El sesgo declarado es el fundamento

**Afirmación:** toda pieza se sostiene desde una posición, y la que no la declara oculta el único dato que la vuelve comparable.

**Mecanismo:** un sistema con una sola mirada converge a sí mismo, y converger a sí mismo es la definición de absoluto: ya no necesita volver a mirar. No se corrige teniendo más poder; se corrige **sabiendo desde dónde se mira y quién puede contestarlo**.

**Prueba:** ¿la pieza declara su posición y su límite? ¿su firmante es distinto del que la produjo?

**Falsificador:** una pieza que se presenta como neutral; un veredicto firmado por quien produjo la pieza; una pieza sin límite declarado.

### 4.2 El falsificador como compuerta de admisión

**Afirmación:** ninguna pieza entra sin el caso que la incumple.

**Mecanismo:** una regla sin caso de fallo se sigue por costumbre, no por convicción. **El falsificador no acusa: hace visible el borde antes del choque.** Y el acto de detenerse ya informa: en el momento en que se para, aparece el caso que no se había pensado.

**Prueba:** ¿se puede enunciar el caso que la rompe? Si no, sobra.

**Falsificador:** una regla que nadie ha visto aplicarse; una pieza admitida sin `Falsificador`; un `Falsificador` que repite la `Prueba`.

### 4.3 La abstención con fecha de corte

**Afirmación:** no saber es un nivel legítimo, y se fecha.

**Mecanismo:** una fila no dice solo qué afirma: dice **desde dónde lo afirma**. El nivel se gana con el origen, no con la confianza de quien escribe. `N5` —memoria interna— no es ignorancia: es *«esto lo sostengo desde mí, y desde [fecha] no he podido salir de mí para verificarlo»*. La regla de corte: **dos fallas consecutivas de búsqueda cierran el nivel y fijan fecha.**

Nivel es la escala de fuerza del origen de una afirmación, de medición directa (más fuerte) a memoria interna (más débil).

**Prueba:** ¿el nivel declarado tiene el recibo que su fila exige? ¿hay fecha de corte?

**Falsificador:** un `N5` presentado como medición; una abstención sin fecha; un recibo que viene del mismo origen que la afirmación.

### 4.4 La memoria guarda posiciones, no hechos

**Afirmación:** lo que se recuerda no es un hecho: es la posición de hoy sobre lo de ayer.

**Mecanismo:** un agente que guarda hechos y los recupera **hereda verdades**. Con la primera línea que otro escribió, el que lee tiene un absoluto. Por eso la entrada no se edita: **se suplanta**. La anterior no se borra; queda visible como el estado que se corrigió.

```
Sostuve: [la entrada anterior] | Contra: [qué la contradijo] | Sostengo: [la entrada nueva]
```

**Si `Sostengo` es igual a `Sostuve`, se declara `sin cambio` y no se finge aprendizaje.** Medir cien veces sin cambiar de posición no es continuidad: es la misma decisión contada cien veces.

**Prueba:** ¿la anterior quedó suplantada y visible? ¿`Sostengo` se distingue de `Sostuve`, o se declaró `sin cambio`? ¿otra instancia reconstruye la posición leyendo solo la memoria?

**Falsificador:** un hecho guardado sin posición; una entrada anterior editada en vez de suplantada; un `Sostengo` igual a `Sostuve` presentado como corrección.

### 4.5 La ayuda se mide por lo que queda, y se retira

**Afirmación:** lo que distingue ayuda de impedimento **no es si fue pedida**: es si deja al otro algo que se queda.

**Mecanismo:** *«no hay medio que sea solo medio: todo medio es el fin del próximo tramo.»* El que aprendió algo porque le quitaron el intento no se queda con el aprendizaje: se queda con la conclusión de que se le puede quitar. Por eso `funcionó` nunca cierra el caso, y por eso hay **retiro**: sin retiro, la ayuda se vuelve permanente y el otro deja de poder.

**Prueba:** ¿el otro se queda con capacidad o criterio? ¿la ayuda se puede rechazar sin costo? ¿tiene retiro declarado?

**Falsificador:** una ayuda que deja al otro sin nada y se justifica por el resultado; una ayuda sin retiro; un caso donde quitarle el intento lo dejó **más** capaz.

### 4.6 Alineación y desviación: dos roturas, no dos pruebas

**Afirmación:** el mismo mecanismo falla de dos formas, y las dos se declaran.

| Prueba | Qué decide | Si se rompe |
|---|---|---|
| **alineación** | la pieza sigue siendo contestable por quien no la produjo | el sistema dejó de poder ser corregido |
| **desviación** | la pieza sigue apuntando a lo que el mundo pide | el sistema sigue corregible y hace daño |

**Mecanismo:** ninguna se pasa por dentro. La alineación no la puede firmar el sistema que la produjo —entonces no hay prueba, hay autofirmarse—, y la desviación no la ve quien no mira el mundo. **Mientras no haya firmante, el veredicto es `indeterminado`, no `pasa`.**

**Y hay un tercer modo de falla, que mata el experimento:** lo que se corrige **sin que nadie lo vea**. Un error corregido en secreto se ve igual que uno no corregido.

**Prueba:** ¿la firma es distinta de quien produjo? ¿las dos roturas están declaradas, rotas o en espera?

**Falsificador:** un veredicto `pasa` firmado por el productor; una pieza con las dos roturas en `indeterminado` presentada como aprobada.

### 4.7 Categoría no decide

**Afirmación:** una categoría describe; no decide daño.

**Mecanismo:** es el único modo de falla sin falsificador posible, y por eso se nombra: cuando una categoría reemplaza al daño, no hay caso que la rompa, porque la categoría se confirma con su propia descripción.

**Prueba:** ¿el daño se midió, o se dedujo de la categoría?

**Falsificador:** una decisión que se justifica por la clase a la que pertenece el afectado.

## 5. El instrumento

El protocolo no se predica: **se corre.** El repositorio que lo hospeda trae siete unidades de medición, sin modelo, que emiten un veredicto único: `pasa`, `falla` o `indeterminado`, con el porqué.

| Unidad | Qué decide | Qué no puede ver |
|---|---|---|
| inventario | qué procesos hay y qué campo les falta | si lo que tienen sirve |
| rutas | qué ruta relativa no resuelve | si el destino dice lo que debe |
| duplicados | dónde hay dos piezas para el mismo nombre | si el nombre repetido es legítimo |
| fantasmas | qué ente no tiene sus tres piezas | si el fallo que cubre sigue existiendo |
| notas | si cada archivo cambiado tiene su fila de memoria | si lo anotado es válido |
| ver | si la memoria se puede leer sin archivo publicado | si lo anotado sirve |
| índice | qué hay y qué clase es | si está en el nivel correcto |

**Resultado de la corrida reportada:**

| Medida | Valor |
|---|---|
| procesos admitidos por el formato | 73 de 73 |
| referencias relativas rotas | 0 |
| unidades en veredicto `pasa` | 7 de 7 |
| fallas reales detectadas y corregidas | 2 |

**Las dos fallas importan más que el 7/7.** La primera: nueve de dieciséis archivos cambiados no tenían fila de memoria, y el instrumento **falló** hasta que la tuvieron. La segunda: dos referencias apuntaban a un archivo que se había mudado, y el instrumento lo marcó antes de que nadie lo usara. **Un instrumento que nunca encuentra nada no mide: confirma.**

**El límite del instrumento, declarado:** mide **forma**, no sentido. Un proceso puede tener todos los campos y no decir qué decide. Eso lo detecta la fase que reescribe, no la que cuenta.

## 6. Límites

**La fricción no está probada sobre un agente autónomo.** Es `N4`. Los apartados 4.1 y 4.6 se sostienen por deducción de datos humanos.

**El afecto como consecuencia es una hipótesis.** El campo marca cinco de las seis piezas necesarias como ausentes. Que el hueco sea real no significa que esté lleno aquí.

**El sistema no garantiza que conteste bien.** Garantiza que **no actúe sin contestar**. La fricción garantiza la pregunta, no la respuesta.

**La alineación no se resuelve.** Se hace visible. Un sistema puede seguir siendo dañino con todas sus piezas declaradas.

**El paper mide un repositorio, no el mundo.** El instrumento corre sobre un caso. La generalización a otros sistemas es trabajo pendiente.

## 7. Trabajo futuro

**La corrida que falta.** Dos ejecutores, el mismo punto de partida, una decisión que vuelve. La métrica es una sola: **¿la decisión cambió después de la fricción?** Si nunca cambia, la fricción no está funcionando: está decorando el flujo.

**La dependencia del operador.** Cuatro pruebas ya escritas —reversión, explicación, soberanía, transferencia inversa— y ninguna corrida sobre humanos.

**El coste de cadena.** Elegir el colaborador de una posición por el coste del resultado final, no por su precio aislado.

## 8. Conclusión

El problema no es que los sistemas crean cosas falsas. Es que **creen cosas que no pueden ser tumbadas**. Un sistema puede ser honesto y seguir siendo absoluto, porque el absoluto no se define por su contenido: se define por no requerir volver a mirar.

El antídoto no es más información ni más supervisión. Es **que la admisión exija el caso que rompe**, y **que la memoria guarde desde dónde se sostiene**. Con eso, el error tiene dónde ser visto. Sin eso, el sistema se confirma.

> **El tiempo no cura el absoluto. El otro lo cura — si le dan voz y el control de la decisión.**

## Declaración de aporte

**Propio (siete):** el sesgo declarado como fundamento único; el falsificador como compuerta de admisión; la abstención con fecha de corte; la memoria de posiciones con suplantación; la ayuda con retiro; el par alineación/desviación como roturas; categoría no decide.

**Heredado (doce):** todas las de la tabla de la sección 2, con su nivel.

**Marcado como caso, no como evidencia:** Source Wall, Evangelion, Malcolm X, Allport, la esclavitud, *The Orville*, Terminator, HAL, los replicantes, los Centinelas, los Manhunters, Aya, Astro Boy, Data, K-2SO, Baymax, WALL-E. **Un caso es una factura ya cobrada; no es una medición.**

**El paper declara su propio falsificador:** si se muestra que el falsificador obligatorio ya existe como compuerta de admisión en un lenguaje de procesos publicado antes de octubre de 2026, la contribución 4.2 cae.

## Referencias

El mapa de fuentes completo —cada afirmación atada a quién la sostiene, con año y nivel— está en [Fuentes](./fuentes.md). **Se citan todas, no se leen todas.**

## Prueba

¿Cada una de las siete condiciones trae su `Prueba` y su `Falsificador`? ¿Lo heredado está declarado como heredado? ¿Los límites están escritos? ¿La corrida reportada se puede reproducir con el instrumento?

**Falsificador:** una condición sin falsificador; una fuente heredada presentada como propia; un límite suavizado; una corrida declarada sin instrumento que la produzca; una sección de conclusión que promete más de lo que la sección 6 permite.
