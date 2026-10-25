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

**Un piso sin `Falta` está mintiendo.** **Rige `./PISO.md`.**

## Prueba

¿Cada capacidad declara qué devuelve, cuánto cuesta y qué riesgo? ¿Lo que falta está escrito? ¿La capacidad probada entró al piso?

**Falsificador:** una capacidad sin costo; un piso sin `Falta`; una capacidad usada sin declararse; un piso que crece sin prueba.

## Transiciones

- Una capacidad se prueba → **entra aquí con su costo y su riesgo.**
- Una capacidad se cae → se marca, y los `.prs` que la usan se declaran en riesgo.

## La regla dura: nada de FARO nombra una era

**Todo lo que es FARO es atemporal: el estándar, los conceptos, y los entes base.**

**Nada de esto nombra un lenguaje, una herramienta, una version, una plataforma, ni el nombre que hoy leen las maquinas.** **Porque todo eso caduca, y la forma no.**

**Y el corte, para no confundirse:**

| Dónde | Qué dice |
|---|---|
| **FARO** | **la forma: qué entra, qué sale, qué se cumple** |
| **la era** | **con qué se hace hoy, y cómo se lee hoy** |

**Lo de la era vive en quien es de la era.** **Y por eso un ente de FARO se puede copiar en cien años y empezar a trabajar: no le debe nada a esta decada.**

**Y la prueba, que es una sola pregunta:**

> **¿Este ente se podria leer dentro de cien años sin saber nada de esta era?**

**Si la respuesta es si, el ente es atemporal.** **Si necesita saber como se llamaba una herramienta en 2026, no es un ente: es una version de un ente.**



**El estándar es atemporal. Por eso no nombra lenguajes, ni librerías, ni versiones, ni plataformas.**

**Y el corte es uno, y es fácil de aplicar:**

| Dónde | Qué dice |
|---|---|
| **el estándar** | **la forma: qué entra, qué sale, qué se cumple** |
| **la implementación** | **con qué se hace: el lenguaje, la herramienta, la versión** |

**Una regla que dice «se escribe en tal lenguaje» no es un estándar: es una decisión de implementación con fecha de caducidad.** **Y un estándar con fecha de caducidad se vuelve un museo.**

**Lo que el estándar sí puede decir es lo que la forma exige:** **que se pueda correr donde el que lo lee, que no dependa de una sola plataforma, que lo ajeno se declare.** **Eso no envejece; el nombre de una herramienta, sí.**

### Prueba de la regla

**¿El estándar nombra un lenguaje, una librería, una versión o una plataforma? ¿La forma se puede cumplir con otra herramienta sin cambiar el estándar?**

**Falsificador:** un estándar que dice con qué lenguaje se implementa; una regla que caduca cuando cambia una versión; una herramienta nombrada como si fuera parte de la forma.
## La regla dura: primero el estándar, después la implementación

**Y esto rige todo lo que se escriba bajo este lenguaje.**

**Se escribe la forma en el estándar —con su `Prueba` y su `Falsificador`— y solo después se escribe el esquema, el script o el archivo que la implementa.**

**Y si el estándar cambia después, la implementación queda desfasada hasta que se reimplemente.** **No se ajusta el estándar para que quepa la implementación.**

**Y la razón, que es la misma de todo el repo:** **una implementación que arrastra al estándar deja de ser estándar y pasa a ser costumbre con nombre.** **Y una costumbre no se puede contestar.**

### Prueba de la regla

**¿El estándar existía antes que el esquema? ¿La implementación cita el estándar que la manda? ¿Cuando el estándar cambió, la implementación se declaró desfasada?**

**Falsificador:** un esquema escrito antes que su estándar; un estándar ajustado para que quepa lo ya escrito; una implementación que dice cumplir un estándar que ya cambió.





