# APRIL — variante sin memoria

> Esta parte se lee junto a `compartido.md`. Aquí solo lo que cambia cuando no hay memoria.

## 4. Memorias

Esta versión no tiene capa de memoria: no hay corto ni largo plazo que sobreviva a la sesión.

- **Estado**: vive en la sesión y muere con ella. Nada se persiste entre reinicios.
- **Kestrel**: se usa igual que en la otra variante, pero contra los docs en disco cada vez; no hay corpus caliente ni aprendizaje acumulado.
- **Consecuencia**: cada tarea empieza sin lo aprendido antes; lo que no esté en los docs locales o en el código no existe.
- **Regla**: si algo tiene que sobrevivir, se escribe en un documento del proyecto, no en una memoria que no hay.
- **Router**: no aplica. Sin memoria no hay pregunta que enrutar.

## 10. En Una Frase

**Svelte + Vanilla + GSAP (2D y 3D falso) en Electron nativo, docs rastreables con `httrack`, sin capa de memoria, `dsh-agent-teams` con un capitán que delega en subagentes durables, usa una skill de UI cuando toca, y sigue reglas de orquestación predefinidas para armar el DAG.** Todo lo demás fuera.
