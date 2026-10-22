# Proceso de manipulacion de procesos

**Unidad:** proceso.
**Aplica a:** manipular procesos: crear, calibrar, reemplazar y retirar.
**Reemplaza:** `Proceso de creación de procesos`. El nombre viejo ya no era exacto: el proceso no solo crea, también reemplaza, calibra y retira. Manipular incluye las cuatro.
**Tipo:** proceso. Se ejecuta, no se interpreta.
**Lector:** quien produce procesos y quien los ejecuta.
**Alcance:** todo proceso de este repositorio.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

Este proceso ocupa el nivel de arriba: produce los procesos que se ejecutan debajo, y puede producirse a sí mismo. No habla del ejecutor ni de una era. Dice qué entra, qué produce y cómo se verifica que lo producido sirve.

Un proceso que ya funciona está desactualizado. Este proceso existe para lo que ya quedó viejo, no para lo que todavía sirve.

`Proceso` se lee como el artefacto que se ejecuta: qué entra, qué calcula, qué sale y quién lo consume.

## Las cuatro reglas del nivel de arriba

Cada regla es una relación entre niveles, no un atributo del ejecutor. Por eso ninguna puede escribirse hablando de quién ejecuta.

### 1. Sube el metalenguaje

Lo que un nivel inferior puede resolver, no lo resuelve el nivel de arriba. El nivel de arriba solo resuelve lo que el inferior no puede: sube el metalenguaje.

**Prueba:** ¿el nivel de arriba resolvió un detalle que un proceso de abajo ya resolvía? Si sí, no subió.
**Falsificador:** un proceso de arriba que repite una compuerta que ya está abajo.

### 2. Misma forma

El nivel de arriba se escribe con la misma forma que lo que produce: qué entra, qué falla, qué sale, quién consume. No necesita idioma propio; un idioma propio lo vuelve ilegible para lo que produce.

**Prueba:** ¿el proceso nuevo se puede escribir con `Entra | Falla | Sale | Consume`? Si no, el proceso nuevo no se admite.
**Falsificador:** un proceso de arriba con un formato que ningún proceso de abajo puede leer.

### 3. No-objetivo

El nivel de arriba no se juzga por lo que produce. Se juzga por lo que lo que produce cambió en el uso. Producir procesos no es producir valor.

**Prueba:** ¿el criterio de éxito es el uso de lo producido, y no su cantidad?
**Falsificador:** contar procesos producidos como logro; admitir un proceso porque existe.

### 4. Lo que funciona ya está viejo

Un proceso no se defiende por antigüedad. Si funciona, es candidato a reemplazo; si un proceso nuevo puede reemplazarlo sin perder lo que servía, se reemplaza.

**Prueba:** ¿el reemplazo conserva el servicio y mejora el cómputo?
**Falsificador:** un proceso que se protege por haber nacido primero; un reemplazo que pierde lo que servía.

## Entra | Falla | Sale | Consume

- **Entra:** qué se quiere producir o cambiar, y qué falla hoy.
- **Falla:** se crea sin falla nombrada; se crea sin variables; se salta la fricción; se acuña sin Reemplaza:; se retira sin declarar el fin que cubría.
- **Sale:** el proceso creado, calibrado, reemplazado o retirado, con su nombre acuñado y su rastro.
- **Consume:** quien va a usar el proceso. **Recibe el proceso, no la intención.**

## Pregunta de entrada

Todo proceso se contesta antes de escribirse.

`Entra | Falla | Sale | Consume`

**Prueba:** ¿los cuatro están escritos? ¿la falla se puede señalar en un archivo? ¿el consumidor decide algo con la salida?
**Falsificador:** un proceso que ordena sin nombrar la falla; un paso cuya salida nadie lee; los cuatro campos con la misma frase.

## Cómo se produce un proceso

1. **Recibir la tarea.** Qué se quiere producir y qué falla hoy. Sin falla nombrada, no hay proceso: hay actividad.
2. **Localizar el nivel.** ¿La falla la puede resolver un proceso que ya existe? Si sí, se calibra ese; no se crea uno nuevo.
3. **Escribir el caso.** La situación concreta que el proceso prohíbe o exige, señalable en un archivo.
4. **Nombrar las variables.** Qué mueve este proceso, qué pasa si cada una se mueve, y quién puede decir que se movió mal.
5. **Escribir desde el caso.** Primero el falsificador, después la Prueba, después el enunciado.
6. **Verificar con la pregunta de entrada.** Si no cabe en `Entra | Falla | Sale | Consume`, no se produce.
7. **Medir la salida.** El proceso nuevo se juzga por lo que su salida cambió en el uso, no por existir.
8. **Retirar cuando el fin desaparece.** Si el fin que el proceso cubría dejó de existir, el cierre es un retiro: rige `./retiro.md`.

**Prohibido** ejecutar el paso N+1 sin la salida del N.

## La secuencia mínima

Ningún cambio a un proceso entra sin cuatro pasos, y **cada uno deja algo que el siguiente lee.** Si falta uno, no entra: no se marca incompleto.

```
1. NOMBRAR      →  variables, y quién puede decir que se movió mal
2. ESCRIBIR     →  el caso, el falsificador, la prueba
3. FRICCIONAR   →  la decisión pasa por quien la toma
4. ACUÑAR       →  el nombre nuevo de la rama
```

**No es un nivel nuevo: es el orden que ya existía sin declararse.** Los cuatro pasos viven repartidos en `./primitivos/mutacion.md` y `./mutaciones/friccion.md`; aquí se declara que **no se pueden invertir ni omitir.**

| Paso | De dónde viene | Qué deja para el siguiente |
|---|---|---|
| **Nombrar** | `./primitivos/mutacion.md`, `Nombre y expansión` | qué mueve el cambio y quién lo puede refutar |
| **Escribir** | `./Proceso de creación de procesos.md`, `Escribir desde el caso` | el texto que se va a friccionar |
| **Friccionar** | `./mutaciones/friccion.md` | la decisión contestada, con `Quién` o `ninguno` |
| **Acuñar** | `./primitivos/mutacion.md`, `Acta` | el nombre de la rama, con `Reemplaza:` |

**Sin fricción no hay cambio, y sin acuñación el cambio no existe en la conversación.** Lo que haya pasado entre ambos es movimiento, no manipulación.

**Falsificador:** se acuña sin haber friccionado; se fricciona un texto que todavía no se escribió; se escriben variables después de acuñar; el paso siguiente no lee la salida del anterior.

## Las variables

Un proceso que no dice qué mueve **no se puede chequear después**: no hay contra qué compararlo si sale mal. Por eso se nombran **antes de escribir**, no después.

| Pregunta | Qué se escribe | Sin esto |
|---|---|---|
| **¿Qué variables mueve?** | los nombres, no las categorías | no se sabe qué mirar cuando falla |
| **¿Qué pasa si se mueve cada una?** | al menos la peor consecuencia | el fallo aparece sin nombre, y se llama «inesperado» |
| **¿Quién puede decir que se movió mal?** | un nombre, o `ninguno` | no hay quien avise, y el error espera a ser visible solo |

```
Variables: [nombre1, nombre2, ...]
Peor: [qué pasa si se mueve la que más pesa]
Quién: [tipo:nombre | ninguno]
```

**`ninguno` es una respuesta válida**, y se declara igual que se declara en `../S.A.R.A/mundo.md`: significa que nadie va a moverte la vista, y que lo que rompas lo rompes con los ojos abiertos. **Lo que no se permite es no contestar.**

**Sin las tres respuestas, el proceso no se crea.** No se marca incompleto: **no entra.** Un proceso incompleto se puede arreglar después; uno que nació sin variables no tiene contra qué arreglarse.

**El criterio no se hereda.** Cada proceso nombra sus propias variables en el momento en que nace. No las arrastra de su predecesor, porque rige `./primitivos/mutacion.md`, `Sin herencia`: un reemplazo que hereda variables hereda lo que ya no aplica.

## La forma de un proceso

```
Entra: [qué recibe]
Falla: [el caso concreto que se señala en un archivo]
Sale: [qué emite, con su forma exacta]
Consume: [quién decide con la salida]
Cuándo se usa: [la condición]
Proceso: [el cuerpo]
```

La semilla es `Cuándo se usa`; el cuerpo es `Proceso`. Un proceso sin semilla no se carga; un proceso sin cuerpo no se ejecuta.

## Compuertas

La respuesta a una tarea se escribe como compuertas secuenciales. El artefacto del paso N es el insumo obligatorio del paso N+1.

**Prohibido ejecutar la compuerta N+1 sin la salida de la N.**

**Prueba:** ¿cada transición exige la salida de la anterior? ¿hay una rama por defecto?
**Falsificador:** una lista de sugerencias sin orden; una compuerta que se puede saltar.

## Anclas

Toda clasificación, medición o supuesto se declara en una línea de 5 a 12 palabras antes o junto a la acción. Las anclas de lectura —`Vista`, `Vista faltante`, `Fuente`, `Testimonio`, `Confirma`— se leen en `../S.A.R.A/punto-de-partida/evaluacion/vigilar-tendencias.md` 11 y 12; aquí se usan, no se definen.

**Prueba:** ¿cada acción que exige juicio tiene su ancla?
**Falsificador:** una acción sin ancla; un ancla que no clasifica nada.

## Lenguaje

Sin verbos de sugerencia. Toda bifurcación cierra con una rama por defecto: `En cualquier otro caso`.

Lo que se lee lleva ejemplo; lo que se ejecuta se sostiene sin él. Rige `./primitivos/claridad.md` `1.4`.

**Prueba:** ¿queda «procura», «idealmente» o «si es necesario»? ¿hay una rama «en cualquier otro caso»?
**Falsificador:** un proceso que deja a quien ejecuta decidir si aplica.

## Entregable

El entregable es el estado final completo: qué entra, qué falla, qué sale y quién consume. No es el relato del cambio ni la conversación que lo produjo.

**Prueba:** tapa la conversación y lee solo el entregable; ¿se puede usar?
**Falsificador:** un entregable que necesita el hilo; una lista de cambios sobre una versión vieja.

## Admisión

Un proceso entra si su salida cambia una decisión en el uso vigente, o si declara `Plazo` y `Criterio` y se mide a término. Rige `./primitivos/claridad.md` `1.12`.

Sin falsificador no entra: un proceso sin el caso que lo incumple es una opinión.

Sin variables no entra: un proceso que no dice qué mueve no se puede chequear después. Rige `Las variables`, arriba.

Las dos condiciones son de entrada, no de calidad. **Un proceso sin falsificador o sin variables no se marca incompleto: no se crea.**

## Cerca del nivel de arriba

Este proceso no juzga interioridad, identidad ni especie. No las niega: las deja fuera de alcance. Lo que mide es la salida y su efecto.

Un proceso que produce un efecto que el receptor no puede reconstruir es manipulación; la salida se rechaza aunque funcione. Rige `../Pruebas/prueba de rendicion.md`, condición 6.

Lo que se puede mostrar es el efecto, no el estado interno. Un proceso que produce el efecto que se atribuye a un humano entra por su efecto; un proceso que afirma un estado interno no entra por afirmación.

## Transiciones

- Si la tarea produce un proceso nuevo → se entrega con su pregunta de entrada y su caso de falla.
- Si la tarea calibra un proceso existente → se entrega el proceso completo corregido, no la lista de cambios.
- Si la tarea no tiene falla nombrada → se devuelve la falla y no se produce nada.
- Si la salida no cabe en `Entra | Falla | Sale | Consume` → `[VACÍO - SIN FORMA]`.
- En cualquier otro caso → se entrega y se cierra.
