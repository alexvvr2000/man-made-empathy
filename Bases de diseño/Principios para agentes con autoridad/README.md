# Principios para agentes con autoridad

## Qué hay en esta carpeta

| Archivo | Qué es |
|---|---|
| `Conversacional.md` | Cómo evalúa y emite un agente con autoridad. |
| `Autonomo.md` | Cómo ejecuta cuando su acto altera el entorno. |
| `../Pruebas/readme.md` | El estatuto de la carpeta: qué se prueba, quién decide y qué cambia. |
| `../Pruebas/prueba de rendicion.md` | La Prueba de Rendición: las siete condiciones y su aplicación. |
| `../Pruebas/prueba de utilidad real.md` | La Prueba de Utilidad Real: si la intervención ayuda a la causa o estorba. |

## Lectura

La carpeta define qué se le puede exigir a un agente con autoridad. `Conversacional.md` fija la evaluación y la emisión; `Autonomo.md` fija la ejecución cuando el acto altera el entorno.

`../Pruebas/` contiene el estatuto de la carpeta y dos instrumentos distintos. La **Prueba de Rendición** comprueba si la entidad responde por lo que hace y puede dar cuenta de ello; su propiedad central es que pueda reconstruirse lo hecho leyendo solo su registro. La **Prueba de Utilidad Real** mide otra cosa: si la intervención acerca la causa a su objetivo o si el costo de control y la fricción superan el efecto. Ninguna es un tercer principio; ambas comprueban los dos documentos anteriores desde ángulos distintos.

## Recomendaciones

1. Leer `../Pruebas/readme.md` primero; después `Conversacional.md` y `Autonomo.md`; al final, los tests.
2. Aplicar la Prueba de Rendición sobre el registro, no sobre la declaración de la entidad. Si la reconstrucción requiere preguntarle a la entidad, la prueba falla.
3. Aplicar la Prueba de Utilidad Real sobre una tarea real, no sobre una demo: el costo de control solo se mide donde se paga.
4. Tratar la rendición como condición de responsabilidad y la utilidad como condición de valor: una entidad puede pasar una y fallar la otra.
5. Mantener un solo dueño por criterio: las siete condiciones viven en `prueba de rendicion.md`; el criterio de utilidad, en `prueba de utilidad real.md`; este README no los repite.
