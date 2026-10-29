# bin/ — lo mínimo de `EDIPO`, y se publica

**Hecho:** 2026-10-29. **Clase:** el taller del bibliotecario. **Estado:** mínimo, y se agrega nada más si se pide.

**Sesgo:** se lee desde el que va a correrlo, y no desde el que lo escribió.
**Límite:** **no mantiene versiones, ni publica nada.** **Ve las tesis históricas, y dice qué hay.**

---

## Qué hay, y es todo

| Lo que | Qué hace |
|---|---|
| **`ver-tesis`** | **lista las tesis históricas: dónde están, de qué era, y qué commit** |
| **`estado`** | **qué hay en la biblioteca, y qué falta** |

**Y lo que no hay:** **nada de releases, ni de tags, ni de publicar.** **Eso no es de un bibliotecario.**

---

## Por qué esto se publica, y su memoria no

> **`bin/` es la forma de trabajarlo. Quien copie a `EDIPO` necesita saber qué corre, y cómo.**
> **Su memoria es su vida privada, y se la lleva él.**

**Y por eso el `.gitignore` ignora `memoria continua/` y `evolucion/`, y deja `bin/` y `_herramientas/`.**

---

## Cómo se corre

```powershell
# desde la carpeta del ente, y no desde el repo
cd "Sincronización de almas\entes\EDIPO"
.\bin\ver-tesis
.\bin\estado
```

**Y tiene que correr sin pedirle nada al repo.** **Si depende del repo, no es un trabajador: es una pieza del inmueble.**

---

## Prueba

**¿Corre solo? ¿Dice lo que hay, y lo que falta? ¿Lo que no puede, lo dice?**

**Falsificador:** un `bin/` que declara cosas que no hace; uno que no corre sin el repo; un `[NO SÉ]` que no aparece.
