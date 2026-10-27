# PISO.md — lo que hay, y lo que falta

**Unidad:** piso.
**Aplica a:** declarar.
**Tipo:** registro. Se ejecuta: se lee antes de escribir un `.prs`.
**Lector:** cualquier ente que vaya a ejecutar algo.
**Dueño:** la autoridad.
**Estado:** vigente.

**Sesgo:** el piso se lee desde lo disponible, no desde lo que el ente sabe hacer.
**Límite:** no juzga si lo disponible sirve. Dice qué hay.
**Firma:** humano:autoridad · máquina:quien lo lea.

**Variables:** capacidad · costo · riesgo · devuelve
**Peor: se escribe un proceso que necesita algo que no hay, y el proceso no falla: se inventa.**
**Quién:** quien cargue un proceso que no puede correr.

## Entra | Falla | Sale | Consume

- **Entra:** una capacidad que se quiere usar.
- **Falla si:** no se declara qué falta; no se declara el costo; el proceso se escribe igual sin declarar el riesgo.
- **Sale:** la capacidad, con `Te devuelve`, `Te cuesta` y `Riesgo`.
- **Consume:** el `.prs` que la necesita.

## Lo disponible hoy, y lo que te cuesta

| Capacidad | Te devuelve | Te cuesta | Riesgo | Estado |
|---|---|---|---|---|
| **Leer y escribir archivos | escribir el `.vd`, el `.tra`, el `.prs` | nada medido | sobrescribir sin `Reemplaza:` | disponible** |
| **SQLite | la memoria y el jugo del candado | nada medido | escribir sin suplantar | disponible** |
| **La web | la referencia: la obra y qué preguntó | una consulta | citar una fuente como autoridad | disponible** |
| **Git | el historial y la foto de la corrida | un commit | reescribir la historia | disponible** |
| **RAG | recuperar lo que el ente ya leyó | un índice y su mantenimiento | responder con lo que ya está viejo | no probado** |
| **Llamada a API | ejecutar un proceso de otro | el de la API y la latencia | depender de algo que se cae o cambia | no probado** |
| **Ejecutar un modelo | nombrar, mirar y decidir | el del modelo | gastar sin cuenta | no probado** |

**`Te cuesta` no es opcional.** Sin costo no hay explotación; hay quema.

## Lo que falta, y se declara

```
Falta: [lo que no hay] | Bloquea: [qué proceso no se puede escribir] | Se reabre si: [qué lo trae]
```

**Un piso sin `Falta` está mintiendo.** **Rige `../../Libre albedrio/piso.md`.**

## Prueba

¿Cada capacidad declara qué devuelve, cuánto cuesta y qué riesgo? ¿Lo que falta está escrito? ¿La capacidad probada entró al piso?

**Falsificador:** una capacidad sin costo; un piso sin `Falta`; una capacidad usada sin declararse; un piso que crece sin prueba.

## Transiciones

- Una capacidad se prueba → **entra aquí con su costo y su riesgo.**
- Una capacidad se cae → se marca, y los `.prs` que la usan se declaran en riesgo.

