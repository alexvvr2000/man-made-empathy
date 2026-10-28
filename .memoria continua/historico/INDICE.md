# ÍNDICE DEL HISTÓRICO — qué se guardó, y cuándo

**Hecho:** 2026-10-28. **Clase:** índice. **Estado:** vigente.
**Lector:** quien quiere reconstruir qué pasó, y con qué se trabajó.

**Sesgo:** se lee desde la transparencia: **lo que se movió, se anota; lo que se guardó, dice de cuándo.**
**Límite:** **no es la memoria viva.** **Nada de aquí se usa para decidir.**
**Firma:** humano:autoridad.

---

## La regla, y es la que hace la transparencia

> **Cada vez que se barre, se mueve o se guarda algo, se anota aquí, con fecha y con qué.**
> **Y si algo se borró, se dice que se borró, y dónde quedó.**

**Porque transparencia no es guardar: es poder reconstruir qué pasó, y cuándo.**

---

## Lo que hay hoy

| Lo que | Dónde | De cuándo | Para qué |
|---|---|---|---|
| **el esquema de MANTIS** | **[`./esquema.sql`](./esquema.sql)** | **2026-10-24** | **cómo se pensaba la memoria vieja: seis partes por entrada, suplantar en vez de editar** |
| **el rastro crudo de MANTIS** | **[`./rastro-respaldo/`](./rastro-respaldo/)** | **2026-10-24 a 2026-10-26** | **279 entradas, 261 pases, 355 piezas, y `mantis.db`** |

---

## La bitácora, y cada línea es un movimiento

| Fecha | Qué se hizo | Qué se movió | Dónde quedó |
|---|---|---|---|
| **2026-10-28** | **se sacó el rastro crudo de `.memoria continua/rastro/`** | **`mantis.db` y los ocho `.jsonl`** | **[`./rastro-respaldo/`](./rastro-respaldo/)** |
| **2026-10-28** | **se guardó el esquema viejo** | **`esquema.sql`** | **[`./esquema.sql`](./esquema.sql)** |
| **2026-10-28** | **el histórico entró al repo, por decisión del autor** | **`.gitignore`: `historico/` exento, `ciclo.db` excluido** | **commits `8733c6c` y `f953106`** |

**Y las tres son de hoy, y son las que hay.** **Lo que se añada, se añade aquí, y con su renglón.**

---

## Qué NO está aquí, y hay que saberlo

**La tesis vieja no está aquí.** **Está en [`../../Sincronización de almas/ideas/tesis vieja/`](../../Sincronización%20de%20almas/ideas/tesis%20vieja/), porque es argumento y no rastro.**

**Las notas de `.memoria continua/notas/` no están aquí.** **Son fuente viva, no histórico.**

**El chat gigante no está aquí.** **Se lee de `C:\Users\Alex\.dsh\sessions`, y su volcado es el ciclo 1.**

**Y la base viva, `ciclo.db`, no está en el repo:** **se rehace desde `bin/esquema.sql`.**

---

## Lo que este índice NO permite

**No permite reconstruir una decisión de hoy.** **Para eso está `bin/ciclo.py ver`, y el `pase` del día.**

**No permite afirmar nada sobre nadie.** **El rastro crudo dice lo que se escribió, y quién lo escribió entonces.**

**No es prueba de nada.** **Es el histórico del método, y se cita como historia.**

---

## Prueba

**¿Cada cosa guardada tiene su fecha y su para qué? ¿La bitácora dice qué se movió y dónde quedó? ¿Se dice qué NO está aquí?**

**Falsificador:** un archivo guardado sin fecha; un movimiento sin renglón; un borrado que no se dice; un histórico que se presenta como prueba.
