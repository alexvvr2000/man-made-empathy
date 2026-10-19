# agents.md — Índice bajo demanda

**Tipo:** índice. No carga instrucciones por sí solo.
**Alcance:** todo artefacto de este repositorio.
**Uso:** se carga solo la fila que coincide; el resto no se carga.
**Cada turno:** si hubo un cambio nuevo aprobado, se anota un candidato en el almacén que corresponda (`novedad.md`); no se crea ley.
**Seguridad:** automático solo en meta-repos; lectura por defecto; aplicar solo con autorización; sin segundo plano de aplicación.

| Quiero... | Cargo... |
|---|---|
| Escribir o editar | `./Bases de diseño/Reglas de escritura de este repositorio.md` |
| Revisar consistencia | `./Instrucciones/consistencia.md` |
| Crear una instrucción | `./Instrucciones/instruccion-de-autoridad.md` |
| Analizar novedades | `./Instrucciones/novedad.md` |
| En cualquier otro caso | no se carga instrucción; se responde y se cierra |