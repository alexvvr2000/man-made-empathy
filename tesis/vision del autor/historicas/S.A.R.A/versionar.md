# Proceso de versionar

**Variables:** estado · identificador · reemplazo · rastro
**Peor:** se edita el estado y no queda rastro de qué cambió
**Quién:** quien tiene que reconstruir el cambio

**Unidad:** proceso.
**Aplica a:** versionar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Algo cambia y nadie puede decir qué versión produjo qué resultado. Este proceso deja cada estado identificable y reemplazable.

Práctica de industria: control de versiones y gestión de configuración.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** un estado que cambia.
- **Falla:** se edita sin reemplazar; dos estados distintos comparten versión.
- **Sale:** la versión con su huella y su reemplazo declarado.
- **Consume:** quien reproduce o evalúa.

## Cómo se aplica

1. **Identificar el estado.** Qué es lo que cambia y desde qué versión.
2. **Calcular la huella.** Un identificador que cambia si cambia el contenido.
3. **Declarar el reemplazo.** Qué versión reemplaza y qué conserva.
4. **No editar.** Un estado no se edita: se reemplaza.

`Versión: [id] | Huella: [hash] | Reemplaza: [id] | Conserva: [qué]`

## Prueba

¿La versión identifica un solo estado? ¿Se reemplazó en vez de editarse?

**Falsificador:** dos estados con la misma versión; se edita el estado anterior; no se declara qué reemplaza.

## Transiciones

- Si el estado cambia lo que servía → `../evaluacion/probar-regresion.md`.
- En cualquier otro caso → se entrega y se cierra.
