# Proceso de desplegar

**Unidad:** proceso.
**Aplica a:** desplegar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Lo que funciona en prueba se suelta en producción y se rompe, o se suelta sin medir. Este proceso entrega con condición y con retorno.

Práctica de industria: entrega continua y despliegue gradual.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el cambio verificado y el entorno donde va.
- **Falla:** se despliega sin condición de aceptación; sin forma de retorno.
- **Sale:** el despliegue con su recibo y su condición de retorno.
- **Consume:** quien opera y quien vigila.

## Cómo se aplica

1. **Declarar la condición.** Qué tiene que pasar para que el despliegue siga y qué para detenerlo.
2. **Desplegar gradual.** Primero una parte, no todo.
3. **Medir contra la condición.** Con el criterio de `../evaluacion/evaluar.md`.
4. **Retornar si falla.** El retorno se declara antes, no se improvisa.
5. **Registrar.** Qué entró, qué salió y qué se revirtió.

`Despliegue: [qué] | Condición de seguir: [qué] | Condición de parar: [qué] | Retorno: [mecanismo]`

## Prueba

¿Las condiciones se declararon antes? ¿Hay retorno?

**Falsificador:** despliegue sin condición de parada; sin retorno; se mide después de que ya está todo puesto.

## Transiciones

- Si falla → se retorna y se declara.
- Si pasa → `../versionado/`.
- En cualquier otro caso → se entrega y se cierra.
