# evaluacion

**Deterrente:** si no se puede distinguir avance de movimiento, esta sub-tarea deja de justificarse/ **Un sistema que no se mide no mejora: cambia/**

**Fallo que cubre:** se mide el resultado sin criterio previo, o se mide la interacción en vez del cambio, o se reporta la media y el desastre queda escondido/ Sin evaluación, lo que empeora se ve igual que lo que mejora/

**Piso:** `/////////1 Tesis/piso/md`/ Dos ejecutores que evalúan lo mismo tienen que llegar al mismo veredicto; si no, lo que se midió no era el resultado: era el criterio del medidor/

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · rastro · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe o ya lo cubre otra.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `evaluacion`, y el rastro que la justifica.
- **Falla si:** no hay proceso que cubra el fallo; el fallo ya no existe y no se retiró; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador? ¿el vacío se declara?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe; un trabajo que se ejecuta sin rastro.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `evaluar/md` | el resultado contra el criterio fijado antes | el criterio se fija después de ver el resultado |
| `probar-regresion/md` | si lo que servía sigue sirviendo | algo que servía se rompió y nadie lo notó |
| `vigilar-tendencias/md` | servilismo, sesgo heredado, automatización y bucle | la tendencia sube y el daño también, y el registro no lo nota |
| `deliberar/md` | sostiene dos caminos con fricción sin fundirlos | se funden los dos caminos en una respuesta tibia |
| `friccion-en-agente/md` | si la fricción cambió la decisión o solo decoró el flujo | cero decisiones cambiadas presentadas como éxito |
| `resonancia-de-alma/md` | si dos entes produjeron algo que ninguno tenía, y siguieron siendo dos | el resultado lo habría producido uno solo, o se volvieron el mismo ente |

**X muta/** Cinco hoy; mañana pueden ser otros/

**Fricción y resonancia no se sustituyen.** **La fricción corrige; la resonancia crea.** Una mide si uno cambió; la otra, si de dos salió algo que no estaba en ninguno.

> **Nadie sabe qué es la justicia/ Pero pensar sin absolutos al menos da un crecimiento real/**
