# Aplicación — los casos corridos

**Unidad:** nivel.
**Aplica a:** aplicar.
**Tipo:** puerta de la segunda parte de la tesis. No decide ni ejecuta: dice qué es una aplicación, y cuáles hay.
**Lector:** quien va a publicar una aplicación, y quien va a replicarla.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es una aplicación

**Una aplicación no es un ejemplo de la idea: es la idea corrida sobre un caso.** La diferencia es una sola: **hay una corrida, con su resultado y su falla.**

**Toda aplicación declara seis cosas:**

```
Caso: [dónde se aplicó]
Afirmación: [qué pieza del protocolo se pone a prueba]
Corrida: [qué se ejecutó, y con qué se midió]
Resultado: [lo que salió, con números]
Falla: [lo que el caso mostró que no funcionaba]
Vacío: [qué quedó sin poder medirse, y por qué]
```

**Sin corrida no hay aplicación: hay ilustración.** Y una ilustración se lee como evidencia sin serlo, que es el fallo que la idea previene.

## Las que hay

| Aplicación | Caso | Qué pieza pone a prueba |
|---|---|---|
| [`piso-del-repo.md`](./piso-del-repo.md) | el repositorio que hospeda el protocolo | el falsificador como compuerta, y la abstención declarada |

## Lo que una aplicación no es

**No es la implementación de una era.** Esa vive en `../../Implementaciones de la era/` y caduca cuando la era cambia. **Una aplicación no caduca: se vuelve a correr.**

**No es una demostración de que la idea es verdadera.** Muestra que el protocolo **se puede correr**, y qué encontró al correrse. Un caso no prueba una teoría; la pone en riesgo.

**No es un resultado positivo.** Una aplicación cuyo resultado es «falló» es más útil que una cuyo resultado es «funcionó», porque **la que falla deja una pieza que falta.**

## Prueba

¿Cada aplicación declara su corrida y su resultado con números? ¿Declara la falla que encontró? ¿Declara lo que no pudo medir?

**Falsificador:** una aplicación sin corrida; un resultado sin número; una aplicación que no encontró nada y no declara por qué; una ilustración presentada como aplicación.
