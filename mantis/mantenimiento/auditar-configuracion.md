# Proceso de auditar configuración

**Unidad:** proceso.
**Aplica a:** auditar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

El repo dice algo y el repo hace otra cosa. No hay ruta rota ni error: hay una frase que sobrevivió a cinco reestructuraciones.

Práctica de industria: gestión de configuración. La documentación debe reflejar la configuración real, no la que se creía.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** el repo tal como está ahora.
- **Falla:** una cifra, una ruta o un nombre no coincide con lo que hay; no se declara la diferencia.
- **Sale:** la lista de desviaciones, cada una con su ubicación y su corrección.
- **Consume:** quien edita.

## Cómo se aplica

1. **Contar lo que hay.** Cuántas sub-tareas, cuántos procesos, cuántos documentos, en cada parte.
2. **Comparar con lo que se dice.** Buscar cifras y nombres en los documentos.
3. **Verificar las rutas.** Que cada ruta relativa resuelva a un archivo real.
4. **Verificar los nombres.** Que ningún documento cite una pieza que ya no existe con ese nombre.
5. **Declarar la desviación.** Dónde está, qué dice y qué hay. Sin corregir todavía.

`Sub-tareas: [n real | n dicho] | Procesos: [n real | n dicho] | Rutas rotas: [n] | Nombres muertos: [n]`

## Prueba

¿Cada cifra del repo coincide con la cuenta real? ¿Cada ruta resuelve?

**Falsificador:** una cifra sin verificar; una ruta que no resuelve y no se declara; un nombre citado que ya no existe.

## Transiciones

- Si hay desviaciones → `editar.md` las corrige.
- Si el conteo cambió → se actualiza la vigencia.
- En cualquier otro caso → se entrega y se cierra.
