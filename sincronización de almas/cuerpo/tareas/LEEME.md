# TAREAS — una carpeta por tarea, y por pasos

**Una tarea no es un archivo: es una carpeta.** **Porque una tarea puede tener muchos procesos, y el orden importa.**

**Y lo que la IA enseña es exactamente eso: no tiene orden propio, pero es secuencial al final. Si el orden no está declarado, se pierde en medio.**

## Cómo se ve

```
tareas/
└── <Nombre tarea>/
    ├── LEEME.md        qué entra, qué falla, qué sale, y el orden
    ├── paso 1.prs      el primero
    ├── paso 2.prs      y su `Si falla:`
    ├── paso 3.prs
    └── rastro.tra      dónde se quedó
```

## Y cada paso, además del corte, dice qué pasa si falla

```plaintext
Entra:      qué necesita para empezar
Falla si:   qué lo deja mal
Sale:       qué entrega
Consume:    quién lo usa
Si falla:   [se detiene | se revierte | sigue, y se marca]
```

| | Qué deja |
|---|---|
| **se detiene** | **el rastro dice en qué paso se quedó, y lo anterior queda hecho** |
| **se revierte** | **vuelve a como estaba antes del paso, y se dice qué se deshizo** |
| **sigue** | **el paso se marca fallido, y los siguientes corren con eso a la vista** |

**Y ninguno de los tres se decide después: se decide al escribir el paso.**

## Y el rastro es por pasos

```plaintext
Paso 1:  pasó
Paso 2:  falló — se detuvo aquí
Paso 3:  no corrió
```

**Y eso es lo que salva el trabajo: si se cae en el 2 de 5, el 1 está hecho, y se retoma en el 3.**

## Y las tareas pueden reagruparse

**Muchas tareas, en conjunto, pueden mutar: no solo su contenido, su agrupamiento.** **Lo que era `integridad` hace mucho no cambió de contenido: cambió de agrupamiento.**

**Se parte una tarea que creció; se funden dos que se repiten. Y se dice qué se conservó.**
