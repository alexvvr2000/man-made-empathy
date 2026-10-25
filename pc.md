# PC — la máquina donde esto corre, y por qué importa

**Qué es.** **El equipo con el que se hizo todo esto, y los números que la IA no controla.**

**Y existe por una razón concreta:** **la tesis no se sostiene en un centro de datos: se sostiene en una consola de mano de 16 GB.** **Ese es el punto, y aquí está medido.**

**Sesgo:** se lee desde el que va a correr esto en algo peor.
**Límite:** **no mide la calidad del trabajo.** **Mide con qué se hizo, y qué cuesta.**
**Firma:** humano:autoridad · máquina:aquí.
**Estado:** vigente.

## El equipo

| Pieza | Qué es | Qué significa para la IA |
|---|---|---|
| **Equipo** | **Legion Go S** | **una consola de mano, no un servidor** |
| **Procesador** | **AMD Ryzen Z2 Go** — 4 núcleos Zen 3, 8 hilos, hasta 4.3 GHz | **cuatro núcleos: un modelo local grande no cabe por cómputo** |
| **Gráficos** | **RDNA 2 integrada, 12 CU** | **la GPU comparte memoria con el sistema** |
| **Memoria** | **16 GB LPDDR5X-6400** | **el techo real: memoria compartida entre sistema y GPU** |
| **Modalidad** | **API remota, y no local** | **el cálculo no ocurre en la máquina: ocurre fuera, y la máquina solo pide** |

## Y por qué eso es el punto, y no una excusa

**El trabajo de este repo no lo hizo un centro de datos.** **Lo hizo una consola de mano que llama a una API.**

**Y eso significa tres cosas que se pueden probar:**

**1. El piso es bajo.** **Si corrió aquí, corre en casi cualquier cosa con acceso a la red.**

**2. La máquina no es el límite: la red sí.** **Con 4 núcleos y 16 GB, un modelo local grande no entra.** **Pero un modelo pequeño sí, y para muchas de las tareas de este repo basta.**

**3. Y por eso la promesa se puede hacer:** **si esto da resultados con una API, una máquina modesta con un modelo local modesto puede dar los mismos resultados con más paciencia.** **Lo que cambia no es el método: es la velocidad.**

## Y lo que hay que medir para probarlo

**Y no se mide con la boca. Se mide con `STATS.prs` y tres números:**

```
Trabajo por sesion:   pasos, tokens de entrada, tokens de salida, cache
Tiempo:               desde el primer evento hasta el ultimo
Costo:                lo que registre la fuente, o «no registrado»
```

**Y la comparación que importa:**

| | Con API | Con modelo local |
|---|---|---|
| **el método** | **el mismo** | **el mismo** |
| **la calidad del piso** | **la misma** | **la misma** |
| **el costo por resultado** | **se mide** | **se mide** |
| **el tiempo** | **minutos** | **minutos, o horas** |

**Y la conclusión que se sigue, y que es la tesis aplicada a su autor:** **el método no depende de tener la máquina más grande.** **Depende de que el que lo corre pueda contestar.**

## Lo que este archivo no hace

**No es un banco de pruebas.** **No mide rendimiento: dice con qué se hizo.**

**No promete que un modelo local dé lo mismo.** **Dice que el método no lo impide, y que la diferencia es de tiempo.**

**No esconde el límite.** **16 GB y cuatro núcleos son el techo de esta máquina, y están dichos.**

## Prueba

**¿El equipo está declarado con lo que importa para la IA: cómputo, memoria y modalidad? ¿Se dice que la modalidad es remota y que el cálculo no ocurre aquí? ¿Se declara el techo?**

**Falsificador:** un archivo de equipo que lista la marca y no la memoria; un equipo sin decir si el cálculo es local o remoto; una promesa de rendimiento sin números.
