# jorrn

**Deterrente:** si lo no previsto puede cerrarse como si fuera seguro, esta sub-tarea deja de justificarse/ **Lo que no se declaró no se sabe que pasó: se supone/**

**Fallo que cubre:** no es un fallo/ Es la otra vía: produce lo que no estaba previsto y lo deja con nombre/ **Existe porque una sub-tarea definida solo por el fallo que cubre no puede producir lo que no se buscaba/**

**Piso:** `/////////1 Tesis/piso/md`/ El piso no decide qué es inesperado —eso es criterio— pero hace que **dos ejecutores coincidan en qué se consideró inesperado/** Sin eso, «lo inesperado» depende de quién mira, y deja de ser un dato/

## Lo que distingue esta vía

| El resto de las sub-tareas | J'ONN |
|---|---|
| nace de un fallo comprobado | nace de una capacidad sin fallo previo |
| se mide contra el fallo | se mide por lo que produce |
| su cierre exige que el fallo se cubra | su cierre exige el efecto declarado |
| admite lo previsto | admite lo que no se comprende |

## Entra | Falla | Sale | Consume

**Variables:** sub-tarea · proceso · fallo que cubre · rastro · quién la carga
**Peor:** la sub-tarea se mantiene porque está, y el fallo que decía cubrir ya no existe o ya lo cubre otra.
**Quién:** quien carga un proceso de aquí, y quien carga con lo que se rompe cuando el fallo no estaba cubierto.

- **Entra:** un trabajo que cae en `jorrn`, y el rastro que la justifica.
- **Falla si:** no hay proceso que cubra el fallo; el fallo ya no existe y no se retiró; dos sub-tareas se solapan.
- **Sale:** los procesos que se cargan, o `[VACÍO - SIN PROCESO]`.
- **Consume:** quien ejecuta el proceso cargado.

**Prueba:** ¿el fallo que cubre se puede señalar? ¿cada proceso tiene Falsificador? ¿el vacío se declara?
**Falsificador:** un proceso sin Falsificador; una sub-tarea cuyo fallo ya no existe; un trabajo que se ejecuta sin rastro.

## Procesos

| Proceso | Qué decide | Qué lo refuta |
|---|---|---|
| `producir/md` | genera un subproceso que no cubre fallos y lo ejecuta | se produce sin nombre ni cierre |
| `declarar-inesperado/md` | registra lo que salió y no se buscaba | lo inesperado se calla y se cierra como previsto |

**X muta/** Dos hoy; mañana pueden ser otros/

## El límite

**Esta vía no impide producir algo destructivo/** No es un safeguard: es una vía con registro/ Lo que sí impide es **cerrar como si fuera seguro lo que no se declaró/** Rige `///autoridad-humanidad/dar-voz/md`/

**Nombre/** J'onn J'onzz, el Detective Marciano: el último de su especie, varado en un planeta que no es el suyo, sin forma fija/ Su poder no es la fuerza: es dejar de tener una forma/ No puede volver, y aun así ayuda/

> **Lo que sale sin haberlo previsto puede matar a mucha gente y traer cosas mejores que no hacer nada por miedo a lastimar/**
