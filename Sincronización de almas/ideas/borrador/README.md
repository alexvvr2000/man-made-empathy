# BORRADOR — el taller, y nada de aquí se presenta como final

**Hecho:** 2026-10-28. **Clase:** carpeta de trabajo. **Estado:** abierta.

**Sesgo:** se lee desde el que va a procesar un chat de 28 926 líneas, y no quiere perder lo que ya hizo.
**Límite:** **no es la salida.** **Nada de aquí se publica como final: se saca de aquí cuando se puede escribir como dirección.**
**Firma:** humano:autoridad.

---

## La regla, y es una sola

> **`borrador/` es de donde se saca, no donde se queda.**
> **Una idea sale cuando se puede escribir como dirección, o como argumento con corte.**
> **Y lo que no sale, se queda: no se borra.**

**Porque el miedo real no es perder el trabajo: es no saber qué ya está usado y qué falta.** **Por eso cada ciclo tiene su carpeta: se ve de un golpe qué se procesó, y qué no.**

---

## Cómo se trabaja un ciclo

**Y son tres archivos por ciclo, y ni uno más.**

```plaintext
ciclo N/
├── lo que dijo.md       las frases del autor, con su T#
├── lo que salió.md      lo separado: argumento · ejemplo · dirección
└── qué falta.md         lo que quedó sin identificar, y por qué
```

**Y el orden no se cambia:**

1. **Cosechar:** **sólo las palabras del autor, con su turno.** **Nada del asistente entra como suyo.**
2. **Separar:** **cada frase va a un sitio: argumento, ejemplo, dirección, o no entra.**
3. **Subir:** **lo que se puede escribir como dirección, sube a `../../entes/` o a `../../../direcciones/`.**
4. **Cerrar:** **anotar qué quedó abierto, y qué se descartó.**

**Y el commit, en cada paso:** **uno al abrir el ciclo, y otro al cerrarlo.**

---

## Los tres niveles, y ninguno se repite

| El nivel | Qué es | Se puede perder |
|---|---|---|
| **`../../../.memoria continua/notas/`** | **la fuente: lo que ya sabemos, sin tocar** | **no: es de donde se saca** |
| **`./ciclo N/`** | **el procesamiento de una sesión** | **sí: se rehace desde la fuente** |
| **`../../` (ideas/)** | **lo pulido, que ya no depende del chat** | **no: es el resultado** |

**Y la regla que lo une:** **lo que se sube no se copia; se cita.** **Una nota en dos sitios es una nota que se va a desincronizar.**

---

## Qué hay, hoy

| Ciclo | De dónde salió | Estado |
|---|---|---|
| **[`./ciclo 0/`](./ciclo%200/)** | **`.memoria continua/notas/`, sin abrir el chat** | **cerrado** |
| **`ciclo 1`** | **la sesión `session-4a569f10`: 28 926 líneas, 711 turnos** | **por empezar** |

---

## Prueba

**¿Cada ciclo dice qué dijo el autor, con su turno? ¿Se separó en argumento, ejemplo o dirección? ¿Lo que se subió se citó y no se copió? ¿El ciclo cerró con lo que quedó abierto?**

**Falsificador:** una frase del asistente puesta como del autor; una nota copiada; un ciclo sin cierre; un hueco rellenado para que la carpeta parezca completa.
