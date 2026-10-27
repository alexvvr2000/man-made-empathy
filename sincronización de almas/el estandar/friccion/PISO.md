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
| **la memoria | guardar la posición y lo que se sostuvo | nada medido | escribir sin suplantar | disponible** |
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

## El piso perpetuo, y por qué no es un reloj

**El piso se corre en cada paso, no una vez al día.** **Y lo que lo hace perpetuo no es que corra solo: es que cada paso decide si sigue.**

**Un reloj corre cada hora y dice «pasa». Eso no es criterio: es costumbre, y la costumbre tiene dueño.** **El criterio es esto:**

```
1. leer el estándar   → ¿cambió desde la última .tra?
2. si cambió          → se declara desfasado, y se para. No se sigue con criterio viejo.
3. correr el piso     → y escribir el veredicto en la .tra de ese paso
4. no hay .tra        → [SIN TRA - NO PASÓ]. No se adivina, no se continúa.
```

**La diferencia con la industria, en una línea:** **un servicio corre siempre y no puede parar por su cuenta; un criterio corre solo mientras cumple, y se detiene cuando el estándar cambia.**

| Un reloj | El criterio |
|---|---|
| corre cada hora | **corre en cada paso** |
| repite la misma comprobación | **lee el piso de la `.tra` anterior y decide** |
| no puede parar | **para cuando el estándar cambió** |
| nunca dice «no sé» | **dice `[SIN TRA - NO PASÓ]`** |

**Y el cerrojo que lo sostiene:** **el piso no se termina; se ponen cerrojos.** **Un piso perpetuo sin criterio es un cerrojo sin llave: se cierra y no deja pasar a nadie que el estándar no previó.**

### Prueba del piso perpetuo

**¿El piso corrió en este paso, o se corrió ayer? ¿Si el estándar cambió, se paró y lo declaró? ¿Si no hay `.tra`, se adivinó o se declaró?**

**Falsificador:** un piso que corre en horario; un paso que sigue después de que el estándar cambió; un piso que no puede parar; un paso sin `.tra` que continúa igual.

---

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

---

# (de PISO.md)

# PISO.md — el piso, en la forma que la ruta nueva carga sin interpretar
#
# Un `.po` traduce entre dos lenguajes. Aquí traduce entre dos rutas: lo que una
# dejó, en la forma en que la otra lo entiende.
#
# La ruta nueva no lee este archivo entero ni adivina: abre la clave y la tiene.
# Si no hay `.tra` de donde cargarlo, no hay pase: se dice `[SIN TRA - NO PASÓ]`.

msgid ""
msgstr ""
"version: 1\n"
"fecha: 2026-10-26\n"
"deja: la ruta que escribió este piso\n"
"pasa: el alma que pasó\n"
"lee: la ruta que lo carga\n"
"rige: PISO.md, seccion «La forma portable del piso»\n"

msgid "piso"
msgstr "el veredicto del piso: pasa | falla | indeterminado"

msgid "fallas"
msgstr "lo que falló, una por línea, o vacío si pasó"

msgid "se_abre"
msgstr "qué vuelve a abrir el piso: un caso, una fuente, o un contra"

msgid "proceso"
msgstr "a qué proceso entró el alma en esta ruta"

msgid "alma"
msgstr "qué alma pasó: su nombre, no su forma"

msgid "ruta"
msgstr "por qué ruta pasó, y de dónde venía"

msgid "huella"
msgstr "sha256 de lo anterior; una .tra editada es una .tra falsa"

msgid "sin_tra"
msgstr "[SIN TRA - NO PASÓ]: la ruta no adivina, para y lo declara"

msgid "quien_guarda"
msgstr "la .tra guarda; RUTA enruta; ninguna hace el trabajo de la otra"
