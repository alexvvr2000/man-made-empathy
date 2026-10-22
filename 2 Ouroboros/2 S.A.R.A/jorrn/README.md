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
