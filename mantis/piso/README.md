# Piso — las unidades de esta instancia

**Unidad:** nivel.
**Aplica a:** trabajar.
**Tipo:** puerta del piso de esta instancia. No decide ni ejecuta: dice qué unidades hay y cómo se corren.
**Lector:** quien va a usar MANTIS.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

**El piso corre aquí y ahora.** Cada unidad de esta carpeta decide una cosa, emite un veredicto y se lee sola: `pasa`, `falla` o `indeterminado`, con el porqué.

**La forma de cada unidad la dice `../../Ouroboros/piso.md`.** Aquí solo se declara cuáles hay y qué decide cada una.

## Las unidades

| Unidad | Qué decide | Qué no puede ver |
|---|---|---|
| `inventario.ps1` | qué procesos hay y qué campo les falta | si lo que tienen sirve |
| `rutas.ps1` | qué ruta relativa no resuelve a un archivo real | si el destino dice lo que debe |
| `duplicados.ps1` | dónde hay dos piezas para el mismo nombre o el mismo título | si el nombre repetido es legítimo |
| `fantasmas.ps1` | qué ente no tiene `rastro.md`, `ruta.md` o `carga.md` | si el fallo que cubre sigue existiendo |
| `notas.ps1` | si la memoria se escribe con sus seis columnas | si lo anotado es válido |
| `indice.ps1` | qué hay en `Tesis/` y qué forma tiene | si un archivo está en el nivel correcto |

## El tren

```
pwsh -File mantis/piso/piso.ps1
```

Corre las seis y emite **un solo veredicto**. **Cada una también se corre sola**: un tren no es una tubería.

## Reglas del piso

1. **No usa modelo.** Si un `if` resuelve, un modelo introduce ruido.
2. **Su salida ya es veredicto.** Nunca materia prima.
3. **Se rige por el criterio.** Corre igual en cualquier ejecutor, y se vuelve a correr cuando el criterio cambió.
4. **Lo que descarta no se tira: se anota.** Rige `../../notas/actuales.md`.

## Prueba

¿Cada unidad se corre sola? ¿Cada una emite veredicto y por qué? ¿El tren da un solo veredicto?

**Falsificador:** una unidad que necesita que otra corra antes; una que emite datos sin veredicto; una que cambia de resultado entre dos corridas del mismo estado.