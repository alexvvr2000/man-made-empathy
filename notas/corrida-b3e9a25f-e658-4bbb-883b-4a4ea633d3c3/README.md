# Corrida 0 — b3e9a25f-e658-4bbb-883b-4a4ea633d3c3

**Unidad:** nivel.
**Aplica a:** situar.
**Tipo:** corrida. No decide, no ejecuta: es el estado congelado de la memoria en el momento en que la instancia quedó declarada.
**Lector:** quien va a comparar esta corrida con la siguiente.
**Dueño:** la autoridad.
**Estado:** vigente.

**Esquema:** `b3e9a25f-e658-4bbb-883b-4a4ea633d3c3`
**Sucede a:** NINGUNO — es la primera
**Fecha:** 2026-10-22
**Base de la que se tomó:** `.sesion-continua/mantis.db`

## Qué contiene

| Archivo | Qué es |
|---|---|
| `esquema.sql` | el DDL completo, tal como la base lo declara |
| `fila.csv` | 174 filas: lo que se dijo, con su pieza, su tipo y su vista |
| `sesion.csv` | el bloque vivo de la sesión |
| `seccion.csv` | las once secciones y su orden |
| `prueba.csv` | las cuatro pruebas |
| `generacion.csv` | las compilaciones — ninguna todavía |
| `trabajo.csv` | lo que no es sesión ni tesis — vacío |
| `esquema.csv` | el UUID que la base declara |

## Por qué existe una corrida 0

**La memoria se puede curar solo si se puede volver a un estado conocido.** Sin una corrida, la base es un binario que creció sin fotos: cuando algo se rompe, no hay contra qué comparar.

**Y esta corrida está incompleta a propósito, y se declara:** nace antes de que el piso pase 7 de 7. **Una corrida que se declara incompleta es más útil que una que finge estar completa**, porque la siguiente se mide contra ella y dice exactamente qué cambió.

## La regla de las corridas

**Cada corrida acuña un UUID y no se edita.** Una corrida nueva se acuña; la anterior queda como el estado contra el que se compara. **Una corrida editada es una corrida falsa.**

```
Corrida: corrida-<uuid>/ | Esquema: <uuid> | Base: .sesion-continua/mantis.db
Sucede a: corrida-<uuid anterior> | Cambió: [qué] | No cambió: [qué]
Piso: [n de 7] | Roto: [qué]
```

## Prueba

¿La corrida trae su esquema y su UUID? ¿La base de la que se tomó declara el mismo UUID? ¿La siguiente corrida puede declarar qué cambió respecto de esta?

**Falsificador:** una corrida sin esquema; una corrida cuyo UUID no coincide con el que declara la base; una corrida editada después de acuñada; una corrida que no dice con qué piso nació.
