# Memoria — configuración sin capa de memoria

> Se lee junto a `ares-protocolo.md`. Solo incluye lo que cambia cuando no hay memoria.

## 4. Memorias

Esta versión no tiene capa de memoria: no hay corto ni largo plazo que sobreviva a la sesión.

- **Estado:** existe solo en la sesión y termina con ella. Nada se persiste entre reinicios.
- **Kestrel:** se usa igual que en la otra variante, pero contra los docs en disco cada vez; no hay corpus caliente ni aprendizaje acumulado.
- **Consecuencia:** cada tarea empieza sin lo aprendido antes; lo que no esté en los docs locales o en el código no existe.
- **Regla:** si algo tiene que sobrevivir, se escribe en un documento del proyecto, no en una memoria que no hay.
- **Router:** no aplica. Sin memoria no hay pregunta que enrutar.

## 10. Resumen

La implementación usa Svelte + Vanilla + GSAP (2D y 3D falso) en Electron nativo y docs rastreables con `httrack`. No tiene capa de memoria. La orquestación usa `dsh-agent-teams` con un capitán que delega en subagentes durables, una skill de UI cuando corresponde y reglas predefinidas para armar el DAG.
