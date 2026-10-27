# BIN — el código del cuerpo

**Clase:** carta de carpeta. **Estado:** **aquí no se diseña: se pone código.**

**Sesgo:** se lee desde el que va a agregar un programa, no desde el que lo va a explicar.
**Límite:** **no es estándar y no tiene forma.** **Aquí vive el código, y el código no se abstrae.**

---

## Qué es

**Los programas que este cuerpo puede correr.** **El cómo, y no el qué.**

**`bin/` no se lee para entender el sistema:** **se ejecuta.** **Lo que el alma necesita saber de aquí lo dice `../procesos/`, que es donde se declara el corte.**

---

## La regla, y es una sola

> **Cada cuerpo agrega, no muta.** **Si un programa ya funciona, se usa; si se reemplaza, se declara `Reemplaza:` y el viejo queda visible hasta que nadie lo cite.**

**Y nada de `bin/` se copia a otro cuerpo.** **El código es del metal, no del alma.** **Un cuerpo nuevo trae el suyo, y el alma trae su criterio.**

---

## Cómo crece, y es lo que la autoridad dijo

> **El cuerpo lo va mejorando entre más almas lo usen y más tiempo lo llenan de funcionalidad.**

| Cada vez que… | Crece |
|---|---|
| **un alma necesita algo que no hay** | **se agrega el programa, y `../procesos/` declara su corte** |
| **un programa se usa y sirve** | **se queda, y se pone en `../utilidades/`** |
| **un programa se rompe** | **no se borra: se marca, y se dice con qué se cumplía antes** |

**Y la forma estándar de cuerpo existe para esto:** **el código se hace solo cuando el corte está declarado.** **No se escribe el programa primero: se declara qué entra y qué sale, y el cuerpo lo implementa.**

---

## Lo que este archivo no hace

**No enseña a programar.** **No dice qué lenguaje.** **No lista capacidades: eso es `../reconocimiento/RUTA.md`.**

**Y no se documento aquí lo que hace cada programa:** **eso lo declara su proceso en `../procesos/`, y su utilidad en `../utilidades/`.**

---

## Prueba

**¿Lo que hay se usa? ¿Cada programa que se agregó tiene su corte en `../procesos/`? ¿Algo se reemplazó sin `Reemplaza:`? ¿Se copiaron programas de otro cuerpo?**

**Falsificador:** un programa sin corte declarado; un programa copiado de otro cuerpo presentado como propio; un programa reemplazado en silencio; un programa que nadie usa y se queda sin decir por qué.
