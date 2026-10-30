# HISTORIA — el historial de git, una era cuando se pide

**Cuándo se abre:** **cuando alguien necesita una era del historial, y no quiere traerlo todo.**

**Hecho:** 2026-10-28. **Clase:** taller. **Estado:** el script corre.
**Dueño:** **quien tiene la autoridad en el proyecto donde se aplica.**

**Sesgo:** se lee desde el que va a buscar algo viejo, y no quiere traerlo todo.
**Límite:** **no trae nada al repo.** **Trae a una carpeta fuera, y lo que se queda se declara primero.**
**Firma:** **quien responde por el acto, con su nombre** · **y quien lo ejecuta.**

---

## La regla que lo hace seguro

> **Se trae UNA era cuando alguien la pide, y no todas.**
> **Y lo que se trae va fuera del repo, se lee, y si se sostiene se declara.**

**Porque traer sin decidir es lo que infla un registro.** **Y un historial con muchos días no es un argumento: es un historial.**

## Lo que tiene el historial, medido

| Lo que | Cuánto |
|---|---|
| **commits** | **594**, en 28 días |
| **y en una sola, del 27** | **237 archivos, en cinco carpetas** |

---

## Los cuatro comandos

```plaintext
python bin/historia.py listar --limite 20
    los días, con su fecha y su tema. Sin el contenido.

python bin/historia.py buscar "un gramo de registro"
    qué commits tocan ese texto. Sin traerlo.

python bin/historia.py era ce31de5
    qué carpetas y cuántos archivos había en ese commit.

python bin/historia.py traer ce31de5 "ruta/del/archivo.md"
    escribe el archivo fuera del repo, y declara de dónde salió.
```

**Y ninguno toca el repo:** **`traer` escribe en `%TEMP%/historia/`, y lo dice con qué commit, qué ruta y qué día.**

---

## Y lo que no hace, y se declara

**No busca en la base de la memoria vieja.** **Ese histórico vive fuera de la biblioteca, y se lee con `sqlite3`, no con esto.**

**No decide qué se sostiene.** **Trae; el juicio es de quien lo lee.**

**No trae las tesis históricas.** **Ese es el siguiente paso, y va con el mismo criterio: una se pide, y se trae sola.**

---

## Prueba

**¿Trae una era y no todas? ¿Escribe fuera del repo? ¿Dice de qué commit y qué día? ¿Se niega cuando el texto no está en ninguna era?**

**Falsificador:** un `traer` que escribe en el repo; un `buscar` que devuelve todo; un archivo traído sin decir de dónde.
