# IMA.md — el índice de mantis: qué pedido va a qué folder

**Nombre.** IMA — **I**ndex, **M**apa, **A**ndar. La expansión dice el acto: decir qué folder corre qué proceso, y marcarse gastado cuando la forma deja de servir.

**Origen.** **Del `IMA.md` de `alma en blanco/`, copiado y rellenado con lo que este repo tiene.** **El alma no trae el índice del mundo: `mantis` es el índice de su propio mundo.**

**Unidad:** índice.
**Aplica a:** enrutar.
**Tipo:** se intercambia. **No es estándar: es el índice que se gasta.**
**Lector:** quien recibe el pedido.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** el pedido se enruta por lo que pide, nunca por el nombre del folder.
**Límite:** **no decide qué se hace con el pedido.** **Dice qué folder corre.**
**Firma:** humano:autoridad · máquina:quien enrute.

---

## Las filas, y cada una se lee antes de enrutar

| Se va a… | Se enruta a… | Sin la autoridad… |
|---|---|---|
| **comprobar que el cero dice lo mismo que el repo** | `folders/el cero/` | **no se renombra ni se retira nada** |
| **abrir o mantener un candado** | `folders/los candados/` | **no se abre** |
| **componer una tesis, on demand** | `folders/la tesis/` | **no se compone** |
| **guardar lo que pasó en el turno** | `folders/la memoria/` | **el siguiente turno empieza a ciegas** |
| **un pedido que ninguna fila cubre** | `[VACÍO - SIN FOLDER]` | **se improvisa no** |

**Una fila, un folder.** **Si se cargan dos, se declara por qué: dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

---

## Las puertas que no se abren solas

| Puerta | Cuándo se cierra | Quién la levanta |
|---|---|---|
| **el cero** | si la lista de nombres vive dentro de un script | quien mantiene la lista |
| **los candados** | si se abre uno sin nombrar quién carga con eso | quien abre |
| **la tesis** | si se compone sin candados, o sin pedido | quien pide |
| **la memoria** | si se edita en vez de suplantar | quien recuerda |

---

## La gastadura

```plaintext
RUTA:        el índice por pedido
Gastado si:  llega un pedido que ninguna fila cubre, y se corre igual
Se cambia:   el índice, y no el alma
```

---

## Prueba

**¿Cada folder tiene su fila? ¿Cada fila dice qué corre? ¿Se declara lo que no cabe? ¿Se declara cuándo se gasta?**

**Falsificador:** un folder sin fila; una fila sin folder; un pedido que se ejecutó sin fila; un índice que se presenta como estándar.
