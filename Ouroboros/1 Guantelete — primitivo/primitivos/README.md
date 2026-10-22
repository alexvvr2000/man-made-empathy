# primitivos

**Deterrente:** si un primitivo deja de ser primitivo —se deriva de otro, o depende de uno para funcionar— esta sub-tarea deja de justificarse. **El lenguaje se vuelve un catálogo, y un catálogo no compone: lista.**

**Fallo que cubre:** sin piezas que no se deriven de nada, todo proceso necesita otro para explicarse y no hay dónde parar. Los primitivos son **el punto donde se para.**

**Piso:** `../../../Ouroboros/piso.md`. Dos ejecutores que aplican el mismo primitivo tienen que tender al mismo resultado; si no, no era primitivo: era preferencia.

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · piso · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `primitivos`.
- **Falla si:** no hay proceso que cubra el fallo; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `manipulacion.md` | crear, calibrar, reemplazar y retirar procesos, en ese orden | se crea sin variables o sin fricción |
| `aplicar.md` | ejecutar un proceso sobre una entrada y comprobar la composición | se aplica con una entrada que no le corresponde |
| `mutacion.md` | transformar declarando qué conserva, y acuñar nombre y lugar nuevos | se muta sin declarar qué se conserva |
| `claridad.md` | la forma de lo que se lee o se ejecuta | la forma no llega al lector |
| `ingenieria-inversa.md` | deducir un proceso de lo observable, por tendencia | el proceso deducido no reproduce nada observable |
| `retiro.md` | cuándo un proceso se retira, y qué fin queda descubierto | se retira sin declarar el fin que cubría |

**X muta.** Seis hoy; mañana pueden ser otros.

> **Seis primitivos, y ninguno se deriva de otro.** Es más de lo mínimo, y es a propósito: se recuerdan y se usan. Un lenguaje de tres piezas elegante no lo usa nadie; uno de veinte no se recuerda.
