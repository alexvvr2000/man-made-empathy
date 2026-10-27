# mutaciones

**Deterrente:** si una mutación deja de declarar qué conserva, esta sub-tarea deja de justificarse. **Un proceso nuevo que no dice qué conserva no reemplaza: borra sin decirlo.**

**Fallo que cubre:** cada primitivo resuelve una cosa y ninguna resuelve **el momento de decidir** ni **el de mirar**. Los dos fallos son distintos y no se cubren mutando un primitivo entero: se cubren **mudando uno de ellos hacia ese momento.**

**Piso:** `../../../1 Tesis/piso.md`. Una mutación que dos ejecutores no reproducen no es una pieza del lenguaje: es una costumbre.

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · piso · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `mutaciones`.
- **Falla si:** no hay proceso que cubra el fallo; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `friccion.md` | que la decisión pase por quien la toma, antes de mover algo | la decisión se ejecuta sin haber pasado por quien la toma |
| `sesgo-declarado.md` | desde dónde se mira, y quién puede ver lo que no se ve | la idea se descarta por no caber, sin nombrar la regla que rompe |

**X muta.** Dos hoy; mañana pueden ser otros.

## De dónde nacen

Las dos nacieron de la misma pregunta —*¿el otro puede reconstruir esto?*— y nacen de `../primitivos/claridad.md`.

| Mutación | Qué conserva de `claridad` |
|---|---|
| `friccion` | que el otro pueda reconstruir **la decisión** |
| `sesgo-declarado` | que el otro pueda reconstruir **desde dónde se mira** |

> **Una mutación nueva puede nacer de n primitivos, no de uno.** Las piezas se combinan, no se escalan.
