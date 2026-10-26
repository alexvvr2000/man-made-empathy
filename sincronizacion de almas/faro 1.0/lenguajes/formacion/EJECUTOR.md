# EJECUTOR — lo que corre un `.prs`, y por qué el estándar no lo nombra

**Nombre.** EJECUTOR. **Y el nombre dice el acto:** **lo que lee un proceso y lo corre.** **No sabe qué hace el proceso: sabe leer su corte.**

**Origen.** **Del hueco que quedó abierto: el estándar dice que un `.prs` declara lo que entra y lo que sale, y no dice quién lo corre.** **Por eso cada ente acababa poniendo su propio script en su raíz, y el estándar no tenía dónde declararlo.** **Esto lo declara.**

**Unidad:** primitivo.
**Aplica a:** correr.
**Tipo:** se declara. **No es un archivo del estándar: es lo que el mundo tiene que dar para que un `.prs` corra.**
**Lector:** quien vaya a correr un ente, y quien vaya a escribir un mundo.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** el ejecutor se lee desde lo que el proceso declara, no desde lo que el ejecutor supone.
**Límite:** **no juzga si el proceso sirve.** **No sabe qué hace ningún proceso.** **No traduce: si la entrada no es la que el proceso pide, para.**
**Firma:** humano:autoridad · máquina:quien lo corra.

**Variables:** proceso · corte · entrada · salida · mundo
**Peor:** cada ente pone su propio ejecutor, **y entonces el estándar tiene tantos ejecutores como entes: ninguno se puede contestar.**
**Quién:** quien tenga que correr un ente y no sepa con qué.

---

## La regla que faltaba

> **Un `.prs` no corre solo: lo corre el mundo.** **Y el mundo declara con qué.**

**El estándar no nombra el lenguaje del ejecutor, y no tiene por qué.** **Lo que el estándar exige es que el ejecutor sea uno, que se declare, y que no sepa qué hacen los procesos.**

**Y por eso no vive en el estándar: vive en el `RUTA` del mundo, como una capacidad más.**

```plaintext
Ejecutor:   [cómo se llama en este mundo]
Corre:      [qué lee: el corte de un .prs]
No sabe:    [qué hace el proceso]
Falta:      [qué no puede correr este mundo, y qué lo traería]
```

**Un mundo sin ejecutor declarado no puede correr un ente: se declara `[SIN EJECUTOR]`, y no se improvisa.**

---

## Lo que el ejecutor sabe, y lo que no

| Sabe | No sabe |
|---|---|
| **leer los cuatro campos de un proceso** | **qué hace ese proceso** |
| **correr lo que el proceso declara** | **juzgar lo que salió** |
| **dejar la `.tra` del paso** | **decidir si el paso era el que tocaba** |

**Y por eso sirve para todos los procesos: un proceso nuevo no lo toca.**

**Y por eso se puede contestar: cualquiera puede leer qué corrió, sin preguntarle al ejecutor qué quería decir.**

---

## Cómo se declara en un mundo

**En su `RUTA.po`, y con la misma forma que todo lo demás:**

```plaintext
msgid "ejecutor"
msgstr "[cómo se llama en este mundo], y corre el corte de un .prs"
```

**Y el ente lo cita; no lo copia.** **Un ente con su propio ejecutor no es transportable: al mudarse de mundo se lleva algo que su mundo nuevo no necesita y que puede no correr.**

---

## Lo que el ejecutor no hace

**No es estándar.** **No decide qué procesos existen.** **No crea tareas.** **No sabe el nombre de ninguno.**

**Y si un ejecutor conoce el nombre de sus procesos, no es un ejecutor: es un programa con procesos adentro.**

---

## Prueba

**¿El mundo declara su ejecutor? ¿El ejecutor corre un proceso sin saber qué hace? ¿Deja la `.tra` del paso? ¿Un proceso nuevo no lo toca? ¿El ente lo cita en vez de copiarlo?**

**Falsificador:** un ente con su propio ejecutor copiado; un mundo que corre `.prs` sin declarar con qué; un ejecutor que conoce el nombre de sus procesos; un ejecutor que no deja `.tra`; un `[SIN EJECUTOR]` que se resuelve improvisando.

## Transiciones

- El mundo declara su ejecutor → **el ente lo cita, y corre.**
- El mundo no lo declara → **`[SIN EJECUTOR]`, y no se corre.**
- El ejecutor cambia → **cambia el `RUTA` del mundo, y el ente no se toca.**
- El ente se muda de mundo → **lee el ejecutor del mundo nuevo, y sigue.**
- En cualquier otro caso → **se corre, y se deja la `.tra`.**
