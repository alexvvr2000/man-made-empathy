# Proceso de probar regresión

**Unidad:** proceso.
**Aplica a:** probar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Un cambio arregla algo y rompe otra cosa sin que nadie lo note. Este proceso comprueba que lo que servía sigue sirviendo.

Práctica de industria: pruebas de regresión.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el cambio y lo que servía antes.
- **Falla:** se rompió algo que funcionaba y no se detectó.
- **Sale:** el cambio con su verificación, o la rotura declarada.
- **Consume:** quien acepta el cambio.

## Cómo se aplica

1. **Listar lo que servía.** Los casos que pasaban antes del cambio.
2. **Correr los casos sobre el cambio.** No sobre el caso nuevo solamente.
3. **Comparar.** Qué sigue pasando y qué dejó de pasar.
4. **Declarar la rotura.** Lo que dejó de servir se nombra; no se justifica como efecto secundario aceptable.

`Servía: [n casos] | Sigue: [n] | Rompió: [cuáles] | Acepta: [quién y por qué]`

## Prueba

¿Se corrieron los casos anteriores, no solo el nuevo? ¿La rotura se declara?

**Falsificador:** solo se prueba lo nuevo; una rotura se justifica como efecto secundario; no hay lista de lo que servía.

## Transiciones

- Si nada se rompió → `../versionado/`.
- Si algo se rompió → se declara y se decide si el cambio entra igual.
- En cualquier otro caso → se entrega y se cierra.
