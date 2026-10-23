**Fecha:** 2026-10
**Versión:** 1 | **Licencia:** CC-BY-4.0
**Estado:** borrador para depósito. **No está sometido a arbitraje.**

# El instrumento sobre el repositorio

**Tipo:** entregable. El protocolo de admisión corrido sobre el repositorio que lo hospeda: caso, corrida, resultado, fallas y vacío. **Lector:** quien va a replicar la corrida, y quien va a juzgar si el instrumento mide.

## 1. Caso

El repositorio que contiene la idea: un lenguaje de procesos con siete unidades de medición, sin modelo, que emiten un veredicto único.

**Por qué este caso y no otro:** el protocolo afirma que una afirmación no puede entrar sin el caso que la rompe. **El caso más honesto para probarlo es el repositorio que lo afirma.** Si el instrumento no puede encontrar una falla ahí, no mide: confirma.

## 2. Afirmación que se pone a prueba

**El falsificador como compuerta (apartado 4.2 del artículo) y la abstención declarada (4.3):** un instrumento que solo puede decir `pasa` no es instrumento; uno que dice `falla` cuando algo falta, sí.

**Y su propia negación:** si el instrumento nunca encuentra nada, el protocolo no se está aplicando. Se está decorando.

## 3. Corrida

Se ejecuta la unidad que corre todas (requiere PowerShell y `git`):

```
pwsh -File mantis/piso/piso.ps1
```

**Siete unidades, sin modelo, sin red, sin estado compartido.** Cada una se puede correr sola. El veredicto es uno.

| Unidad | Qué decide |
|---|---|
| `inventario` | qué procesos hay y qué campo les falta |
| `rutas` | qué ruta relativa no resuelve a un archivo real |
| `duplicados` | dónde hay dos piezas para el mismo nombre o el mismo título |
| `fantasmas` | qué ente no tiene sus tres piezas |
| `notas` | si cada archivo cambiado tiene su fila de memoria |
| `ver` | si la memoria se puede leer sin archivo publicado |
| `indice` | qué hay y qué clase es |

## 4. Resultado

Corrida reportada: **2026-10-22**.

| Medida | Valor |
|---|---|
| unidades en `pasa` | 7 de 7 |
| procesos admitidos por el formato | 73 de 73 |
| referencias relativas rotas | 0 |
| entes sin sus tres piezas | 0 |
| filas de memoria sin pieza | 0 |

**Un 7/7 no dice nada por sí solo.** Dice que, en esta corrida, ninguna de las siete condiciones falló. El valor está en las fallas que precedieron al 7/7.

## 5. Las fallas que encontró

**Falla 1: la memoria no se estaba escribiendo.** En una corrida intermedia, la unidad de memoria comparó los archivos cambiados contra las filas anotadas y encontró **9 de 16 sin fila**. No era un error de formato: era que el trabajo se entregaba sin dejar rastro, y nadie lo notaba porque el resto del instrumento pasaba.

**Lo que eso forzó:** la unidad dejó de verificar que la tabla tuviera las columnas correctas y pasó a medir **si cada archivo cambiado tiene su fila**. El instrumento cambió porque encontró algo, y ese es el único cambio que lo hace instrumento.

**Falla 2: dos referencias a un archivo mudado.** Otra corrida marcó dos rutas que apuntaban a un archivo que había cambiado de carpeta. El instrumento las encontró **antes de que nadie las usara**.

**Falla 3: el instrumento certificándose a sí mismo.** La primera versión de la unidad de memoria solo contaba filas. Con ese diseño, **un repositorio sin memoria pasaba**. Se corrigió cuando se le pidió que midiera cobertura y no existencia.

**Y una que el instrumento no veía, y se corrigió en esta misma serie:** la unidad de rutas y el conversor buscaban el artículo solo en su ruta histórica. El documento que se lee hoy vive en otra carpeta, y **ninguna de las dos unidades lo hubiera mirado.** Un instrumento que mira donde ya no hay nada también certifica: durante ese tiempo, la unidad de rutas midió **cero** archivos y declaró `pasa`. Lo que la volvió útil fue una prueba que se corre antes: la unidad tiene que **encontrar al menos un archivo**; si encuentra cero, la medición falla.

## 6. Vacío

**Lo que esta aplicación no puede medir, y se declara:**

- **Mide forma, no sentido.** Un proceso puede tener todos los campos y no decir qué decide. Eso lo detecta la fase que reescribe, no la que cuenta.
- **Corre sobre un caso.** No prueba que el instrumento funcione sobre otro repositorio, otro lenguaje u otro ejecutor.
- **No corre en dos ejecutores.** La propiedad que el protocolo necesita —que dos instancias lleguen al mismo veredicto— **está declarada y no medida**. Es el mismo hueco que la sección 6 del artículo declara.
- **No mide si un proceso sirve.** Mide si está completo y si dice qué decide. La utilidad se mide en el uso, y eso no está instrumentado.

## Prueba

¿La corrida se puede replicar con un comando? ¿El resultado trae números? ¿Las fallas que encontró están escritas, no solo el veredicto final? ¿El vacío declara lo que el instrumento no puede ver?

**Falsificador:** un resultado sin comando que lo reproduzca; un 7/7 sin las fallas que lo precedieron; una aplicación que declara que todo pasó y no dice qué encontró; un vacío vacío.
