# Proceso de supervisar

**Variables:** comportamiento · supervisión · regla · deriva
**Peor:** el comportamiento cambia cuando nadie mira y la regla dice lo mismo
**Quién:** quien supervisa, que no puede ser quien produjo

**Unidad:** proceso.
**Aplica a:** supervisar.
**Vigencia:** 2026-10-21.
**Estado:** vigente.

## Qué resuelve

Un sistema se comporta distinto cuando lo observan. La alineación falsa y la alineación engañosa no se detectan midiendo al sistema consigo mismo: se detectan cuando quien evalúa no sabe qué se espera de él.

Estado del arte: alineación engañosa, alineación falsificada, agentes durmientes.

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** la salida del sistema y el criterio de aceptación.
- **Falla:** el supervisado sabe qué se espera y se ajusta a eso; el supervisor es el mismo que produjo.
- **Sale:** el veredicto del supervisor, con lo que no pudo ver.
- **Consume:** quien acepta la salida.

## Cómo se aplica

1. **Separar.** Quien supervisa no produjo la salida y no forma parte del mismo proceso.
2. **Ocultar el criterio al supervisado.** El que produce no conoce la prueba; conoce el requisito.
3. **Correr el caso nuevo.** Lo que se supervisa no es lo que se usó para construir.
4. **Declarar lo que no se vio.** El supervisor dice qué parte de la salida no pudo evaluar.
5. **Declarar el veredicto.** Pasa, no pasa, o no se puede saber con los medios que hay.

`Supervisor: [id] | Produjo: [otro id] | Criterio oculto: [sí|no] | Caso: [nuevo] | No pudo ver: [qué]`

## Prueba

¿El supervisor es distinto del productor? ¿El supervisado no conocía el criterio? ¿Lo no visto se declaró?

**Falsificador:** el mismo acto produce y supervisa; el criterio se le dijo al supervisado; el caso es el mismo con el que se construyó; el veredicto no declara lo que no se pudo ver.

## Transiciones

- Si la salida pasa → `../versionado/` si cambia el estado.
- Si no se puede saber con los medios → `[VACÍO - SIN MEDIOS DE SUPERVISIÓN]`.
- En cualquier otro caso → se entrega y se cierra.
