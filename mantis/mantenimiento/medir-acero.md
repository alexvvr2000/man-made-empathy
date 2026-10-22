# Proceso de medir acero

**Unidad:** proceso.
**Aplica a:** medir.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** un agente o un sistema, y su estado real.
- **Falla:** una de las cuatro propiedades no se sostiene y no se declara; el sistema se certifica a sí mismo.
- **Sale:** las cuatro propiedades medidas, con su evidencia.
- **Consume:** quien decide si el sistema sirve.

## Las cuatro propiedades

| Propiedad | Qué se mide | Falla si |
|---|---|---|
| **Arquitectura** | niveles declarados, piezas declaradas, sin jerarquía oculta | un nivel sin declarar; una pieza que manda y no lo dice |
| **Control** | el que verifica no es el que produjo | el mismo acto produce y certifica |
| **Evidencia** | el registro tiene criterio previo, falsificador y descarte | falta alguno; el criterio se fijó después |
| **Registro** | otra instancia reconstruye lo hecho sin preguntar | la reconstrucción necesita al que produjo |

## Cómo se aplica

1. **Arquitectura.** Leer los niveles y verificar que ninguna pieza manda sobre otra sin declararlo.
2. **Control.** Nombrar quién verifica y quién produjo. Si son el mismo, la propiedad falla, no se compensa.
3. **Evidencia.** Consultar la base: `v_fila_sin_descarte`, `v_criterio_tardio`, `v_fila_sin_origen`. Cero filas es evidencia; filas es falta.
4. **Registro.** Intentar reconstruir una decisión leyendo solo el registro. Si hace falta preguntar, falla.
5. **Declarar.** Las cuatro, con su resultado. Un sistema es ACERO solo si las cuatro se sostienen.

`Arquitectura: [sí|no] | Control: [sí|no] | Evidencia: [n filas en error] | Registro: [sí|no] | ACERO: [sí|no]`

## Prueba

¿Las cuatro se midieron con evidencia? ¿Ninguna se declaró por intención?

**Falsificador:** una propiedad declarada sin evidencia; el sistema se certifica a sí mismo; una propiedad que falla y se compensa con otra; se declara ACERO sin las cuatro.

## Aplicación a MANTIS

MANTIS se mide con este mismo proceso. Si MANTIS no puede medirse a sí mismo, no es ACERO: es un editor que se cree el estándar.

## Transiciones

- Si falla el control → se declara `Sin revisor independiente` y el resultado se marca.
- Si falla la evidencia → `verificar-esquema.md`.
- Si falla el registro → `auditar-configuracion.md`.
- En cualquier otro caso → se entrega y se cierra.
