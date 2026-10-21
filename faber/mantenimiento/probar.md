# Probar el cambio

**Tarea:** probar.
**Carga:** `../../Alineacion de tareas/Pruebas/readme.md`.
**Produce:** el veredicto `Prueba: corrida | no corrida`.
**Cierra en:** `cerrar.md` si pasa; `editar.md` si falla.

## 5. Validación

Toda norma y todo documento se validan con el mismo esquema:

- Toda fila del mapa tiene tareas, mecanismo, invariante y Prueba.
- Toda norma tiene Prueba y falsificador.
- No hay duplicados que fallen igual.
- No hay huérfanos: toda implementación cita su fila del núcleo.
- No hay copias sin cita.
- Toda referencia resuelve dentro de la base.

**Prueba:** si una fila no tiene Prueba, no es norma; es una idea. Si una implementación no cita su núcleo, es una bifurcación.

**Falsificador:** una norma sin Prueba, una fila sin tareas, una implementación sin núcleo.

