# herramientas

**Deterrente:** si una herramienta deja de declarar desde dónde se aplica, esta sub-tarea deja de justificarse. **Una herramienta sin posición se aplica igual, y su resultado se lee como si no tuviera sitio.**

**Fallo que cubre:** una pieza de base dice desde dónde se sostiene una regla; no dice cómo se ejecuta. Sin las herramientas, cada tarea inventa su propio modo de aplicar, mutar o retirar, y dos ejecutores no llegan al mismo sitio.

**Piso:** .../../../piso.md.. Dos ejecutores que aplican la misma herramienta tienen que tender al mismo resultado; si no, no era herramienta: era preferencia.

## Entra | Falla | Sale | Consume

**Variables:** pieza · herramienta · fallo que cubre · piso · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y la herramienta que decía cubrir un fallo ya no lo cubre.
**Quién:** quien carga una herramienta, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en .herramientas..
- **Falla si:** no hay herramienta que cubra el fallo; una herramienta se usa sin la pieza de base que la sostiene.
- **Sale:** las herramientas que se cargan, o .[VACÍO - SIN HERRAMIENTA]..
- **Consume:** quien ejecuta la herramienta cargada.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada herramienta tiene .Falsificador.?
**Falsificador:** una herramienta sin .Falsificador.; una herramienta que se aplica sin sesgo declarado.

## Procesos

| Herramienta | Qué decide | Qué lo refuta |
|---|---|---|
| .manipulacion.md. | crear, calibrar, reemplazar y retirar procesos, en ese orden | se crea sin variables o sin fricción |
| .aplicar.md. | ejecutar un proceso sobre una entrada y comprobar la composición | se aplica con una entrada que no le corresponde |
| .mutar.md. | transformar declarando qué conserva, y acuñar nombre y lugar nuevos | se muta sin declarar qué se conserva |
| .retiro.md. | cuándo un proceso se retira, y qué fin queda descubierto | se retira sin declarar el fin que cubría |
| .ingenieria-inversa.md. | deducir un proceso de lo observable, por tendencia | el proceso deducido no reproduce nada observable |
| .claridad.md. | la forma de lo que se lee o se ejecuta | la forma no llega al lector |

**.X. muta.** Seis hoy; mañana pueden ser otras.

> **Seis herramientas, y ninguna es fundamento.** Se aplican sobre lo que ya tiene sesgo declarado. Una herramienta que se defiende por ser la de siempre es la que no se vuelve a correr cuando el criterio cambió.
