# IMA.md — el índice: qué carpeta corre qué proceso

**Un índice que se gasta.** **No hay una forma fija de enrutar: hay un índice, y cuando la forma deja de servir se cambia.** **Lo que no se cambia es el ente.**

**Es la primera cosa que se llena después de la carta.** **Sin él, el ente entra y no sabe qué correr.**

---

## Las filas, y cada una se lee antes de enrutar

| Se va a… | Se enruta a… | Sin la autoridad… |
|---|---|---|
| **abrir una tarea** | `./procesos/ENTRAR.prs` | **no se enruta: se declara vacío** |
| **ver lo que quedó** | `./procesos/MIRAR.prs` | **no se renombra** |
| **traer una capacidad de fuera** | `./procesos/EXTRAER.prs` | **no entra sin costo** |
| **emitir lo que salió** | `./procesos/EXPRESION.prs` | **no se emite** |
| **tocar algo que otro sostiene** | `./guantelete/herramientas/FRICCION.prs` | **no se toca** |
| **[una carpeta tuya]** | **[qué proceso le toca]** | **[qué no se hace sin la autoridad]** |

**Llena una fila por cada carpeta que el ente vaya a tener.** **Una fila, un destino.** **Si se cargan dos, se declara por qué: dos puertas abiertas a la vez es la forma en que se pierde el rastro de por qué se hizo algo.**

## Lo que no entra en una fila

**Se declara `[VACÍO - SIN PROCESO]`, y se pregunta.** **No se improvisa: improvisar es la forma más rápida de que el ente haga algo que nadie declaró.**

## La gastadura, y es lo que lo vuelve índice

```plaintext
RUTA:           [qué forma de enrutar se usa]
Gastado si:     [qué muestra que la forma ya no sirve]
Se intercambia: [por qué forma]
El ente no:     [qué sigue diciendo, pase lo que pase]
```

**Un índice que nunca se gasta es un estándar disfrazado.**

## Cómo se corre

```plaintext
python ejecutar.py <tarea>
```

**Si en este mundo no hay con qué cumplir el corte, la tarea lo declara `[FALTA EN bin/]` y no corre.** **La tarea no lleva código: el mundo lo pone.**

## Prueba

**¿Cada carpeta del ente tiene su fila? ¿La forma de enrutar está declarada? ¿Se dice cuándo se gasta? ¿El ente queda fuera de lo que se intercambia?**

**Falsificador:** una carpeta sin fila; un índice presentado como estándar definitivo; una forma que se gasta y no se intercambia; un pedido que se corrió sin fila.
