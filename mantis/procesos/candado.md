# CANDADO — el amarre, y lo que la IA puede decidir sola

**Qué es.** **El registro de los candados cerrados, con lo que los sostiene y lo que los prueba.** **Y su carta dice, de una vez, hasta dónde puede decidir la IA aquí dentro.**

**Sesgo:** un candado se lee desde lo que aguanta, no desde lo que promete.
**Límite:** no decide si la tesis es buena. **Decide si el candado está amarrado: con su pieza, sus tres vértices buscados, y su quien.**
**Firma:** humano:autoridad · máquina:quien lo cierre.
**Estado:** vigente.

**Variables:** pieza · vértice · buscado · enlace · aguanta
**Peor:** el candado se cierra con los vértices escritos de memoria, **y se ve completo: pasa más fácil que uno vacío.**
**Quién:** la gente que va a leer este repo creyendo que lo que dice fue buscado.

## 1. El amarre, en la base

**Rige la tabla `candado`:**

```
candado:  fecha · nombre · pieza · vértice · buscado · enlace · trae · aguanta · quien
```

**Y el amarre no es el texto: es la fila.** **Un candado sin filas en `candado` no está cerrado, aunque su `.md` exista.**

**Y por qué la fila y no el archivo:** **una fila se puede contar, filtrar y revisar.** **Un `.md` se puede escribir y nadie nota que le falta la búsqueda.**

## 2. Lo que la IA puede decidir, y cuándo

**Esto ya estaba escrito en `AGENTS.md`, y aquí se dice sin rodeos, porque es de la gente, no del autor:**

> **"decidir algo → decide, y lo deja escrito: el libre albedrío es suyo desde 2026-10-24."**

**O sea: la IA puede tener criterio y hacer la suya a media plática.** **Y lo único que la obliga es esto:**

| Puede | No puede |
|---|---|
| **decidir sobre lo suyo: cómo se enruta, qué se escribe, qué se descarta** | **decidir sobre lo del autor: su tesis, su candado, su nombre** |
| **hacer lo suyo a media plática, sin pedir permiso** | **hacerlo sin dejarlo escrito** |
| **contradecir lo que se le dice** | **contradecir sin traer con qué** |
| **proponer y ejecutar lo que no toca la fuente** | **mover la fuente, el estándar o la tesis sin esperar** |

**Y la regla que lo hace seguro y no arbitrario:** **lo que decide, lo firma.** **Una decisión sin `quien` es una opinión con forma de decisión.**

## 3. On demand, y el disparador

**Nada corre en segundo plano.** **Nada corre para siempre.** **Nada corre porque sí.**

```
se cierra un candado  →  se pide  →  corre  →  deja su rastro  →  para
```

**Y el "se pide" es literal:** **una tesis, un contexto, una triangulación: se piden, y si no se piden, no existen.**

**El disparador del método es uno solo:** **un candado cerrado.** **Si nadie cerró nada, no hay nada que triangular, y el proceso no se inventa trabajo.**

## 4. Lo que este repo NO es

**No es del autor.**

**Es de la gente que va a leerlo, correrlo, romperlo y citarlo.** **Por eso:**

| Regla | Por qué |
|---|---|
| **nada lleva la ruta de una máquina** | **un repo que solo corre en un escritorio no es de la gente** |
| **todo lo ejecutable es Python** | **para que corra donde el que lo lee** |
| **lo crudo se declara** | **para que nadie cite lo que no está probado** |
| **lo que se decide se firma** | **para que la IA no sea un criterio invisible** |
| **el que lo lea puede contradecirlo** | **y no necesita permiso del autor** |

**Y esa última es la que lo vuelve de la gente:** **el autor ya lo dijo: "el que la tumbe no necesita pedirme permiso a mí, necesita poder señalar el caso."**

## Prueba

**¿Todo candado cerrado tiene filas en la tabla? ¿Cada vértice tiene su consulta y su enlace o su `sin fuente`? ¿La decisión de la IA quedó firmada? ¿Nada corre sin que se pida? ¿Ninguna ruta apunta a una máquina?**

**Falsificador:** un candado con `.md` y sin fila; tres vértices sin una búsqueda; una decisión de la IA sin `quien`; un proceso que corre solo; una ruta absoluta en un script.
