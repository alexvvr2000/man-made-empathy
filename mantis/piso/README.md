# Piso — las unidades de esta instancia

**Unidad:** nivel.
**Aplica a:** trabajar.
**Tipo:** puerta del piso de esta instancia. No decide ni ejecuta: dice qué unidades hay, qué decide cada una y cuándo dejan de usarse.
**Lector:** quien va a usar MANTIS.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**El piso corre aquí y ahora.** Cada unidad decide una cosa, emite un veredicto y se lee sola: `pasa`, `falla` o `indeterminado`, con el porqué.

**La forma de cada unidad la dice `../../Ouroboros/piso.md`.** Aquí solo se declara cuáles hay, qué decide cada una, **y dónde deja de valer.**

**Estas siete no son las únicas posibles: son las que ganaron su lugar.** Una tarea que no vuelve es un tiro, y no se guarda. Rige `../../Ouroboros/CRITERIO.md`, `Unidad y tiro`.

## Las unidades

**Cada una declara qué decide, qué no puede ver, y su `No se aplica a`** — la cuarta condición del estándar. **Un límite es el que dice cuándo dejar de usarla**, y por eso no se omite.

| Unidad | Qué decide | Qué no puede ver | `No se aplica a` |
|---|---|---|---|
| `inventario.ps1` | qué procesos hay y qué campo les falta | si lo que tienen sirve | lo que no es proceso: un índice, un borrador, una nota |
| `rutas.ps1` | qué ruta relativa no resuelve a un archivo real | si el destino dice lo que debe | rutas externas, plantillas con `[corchete]` y enlaces de era |
| `duplicados.ps1` | dónde hay dos piezas para el mismo nombre o el mismo título | si el nombre repetido es legítimo | lo que se repite a propósito: las tres piezas del ente, un `README` por sub-tarea |
| `fantasmas.ps1` | qué ente no tiene `rastro.md`, `ruta.md` o `carga.md` | si el fallo que cubre sigue existiendo | carpetas sin ninguna de las tres: no son entes |
| `notas.ps1` | si la memoria se escribe como manda la carta, y si cada archivo cambiado tiene nota | si lo anotado es válido; qué archivo cambió por trabajo y qué por otra persona | el contenido de la fila: eso lo decide el aplanado |
| `ver.ps1` | si la memoria se puede leer sin un archivo publicado | si lo anotado sirve | escribir la base: eso es `anotar.ps1` |
| `indice.ps1` | qué hay en `Tesis/` y qué forma tiene | si un archivo está en el nivel correcto | `Ouroboros/` y `mantis/`: no los indexa |

## El tren

```
pwsh -File mantis/piso/piso.ps1
```

Corre las siete y emite **un solo veredicto**. **Cada una también se corre sola**: un tren no es una tubería.

## Reglas del piso

1. **No usa modelo.** Si un `if` resuelve, un modelo introduce ruido.
2. **Su salida ya es veredicto.** Nunca materia prima.
3. **Se puede correr sola.** No necesita las otras seis.
4. **Se rige por el criterio, y lo declara.** Cada unidad dice su `No se aplica a`, y **el veredicto lo escribe quien lo va a usar.**

**Y lo que descarta no se tira: se anota.** Rige `../mantenimiento/notas/notas-tesis.md`, y se lee con `./ver.ps1`.

## Prueba

¿Cada unidad se corre sola? ¿Cada una emite veredicto y por qué? ¿Cada una declara su `No se aplica a`? ¿El tren da un solo veredicto?

**Falsificador:** una unidad que necesita que otra corra antes; una que emite datos sin veredicto; una que cambia de resultado entre dos corridas del mismo estado; **una unidad sin `No se aplica a`.**
