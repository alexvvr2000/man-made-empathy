# retiro

**Variables:** proceso · fin que cubría · lo que deja · quién lo retira · qué queda en su lugar
**Peor:** un proceso que ya no cubre nada se queda porque nadie decidió sacarlo. Ocupa su lugar, se mantiene, se lee, y **su fin quedó descubierto por otro lado sin que nadie lo note.**
**Quién:** quien depende de lo que el proceso producía. **Si nadie lo nota, nadie lo usa.**

## Entra | Falla | Sale | Consume

- **Entra:** un proceso, el fin que cubría, y la prueba de que ese fin ya no existe o ya lo cubre otro.
- **Falla:** se borra sin declarar qué fin quedó descubierto; se retira sin dejar rastro de que existió; se retira porque estorba y no porque su fin desapareció; el retiro no se distingue de un reemplazo.
- **Sale:** el proceso retirado, con su fin, su prueba de retiro y el `Vacío:` de lo que queda sin cubrir — o la decisión de no retirarlo.
- **Consume:** quien usaba el proceso. **Sabe qué se perdió y qué no.**

## Tesis

**Quitar es una mutación**, y la más peligrosa: **el reemplazo se nota, el hueco no.** Un proceso que se retira sin declarar qué fin cubría deja un agujero con la forma exacta de lo que hacía — y nadie lo busca porque nadie sabe que estaba.

> **Un proceso no se retira porque estorba. Se retira porque el fin que cubría dejó de existir.**

Si el fin existe y el proceso no lo cubre, **no se retira: se muta.** Rige `./mutacion.md`.

## Las tres clases de retiro

| Clase | Cuándo | Qué se declara |
|---|---|---|
| **Absorbido** | otro proceso cubre el mismo fin | a quién pasa el fin, y la prueba de que lo cubre |
| **Vencido** | el fin dejó de existir | por qué dejó de existir, y desde cuándo |
| **Vacío** | el fin sigue existiendo y nadie lo cubre | **se retira igual**, y el `Vacío:` queda con fecha |

**La tercera es la que se hace mal siempre.** Se retira porque estorba, y el fin queda descubierto sin que nadie lo declare. **Se puede retirar — pero el `Vacío:` se escribe antes, no después.**

```
Retiro: [proceso] | Clase: [absorbido|vencido|vacío] | Fin: [el que cubría]
Pasa a: [proceso|nadie] | Prueba: [qué muestra que el fin ya no existe o ya está cubierto]
Vacío: [qué queda sin cubrir, desde cuándo] | Quién: [tipo:nombre]
```

## Proceso

### 1. Nombrar el fin, no el proceso

**El retiro se justifica por el fin, nunca por el proceso.** "Este proceso estorba" no es razón: es una preferencia.

```
Fin: [qué se perseguía] | Sigue existiendo: [sí|no] | Lo cubre otro: [cuál|nadie]
```

### 2. Elegir la clase

| Si el fin... | La clase es |
|---|---|
| lo cubre otro proceso | **absorbido** |
| dejó de existir | **vencido** |
| sigue existiendo y nadie lo cubre | **vacío** |

**No hay cuarta.** Un proceso que se retira sin que el fin caiga en una de las tres no se retira: se muta.

### 3. Escribir el `Vacío:` antes de retirar

**Si la clase es `vacío`, el `Vacío:` se escribe en el mismo acto, no después.** Un vacío que se anota después se olvida, y el olvido es lo que el retiro debía evitar.

```
Vacío: [qué queda sin cubrir] | Se buscó: [dónde] | Cierra: [cuándo se revisa]
```

### 4. Dejar el rastro

**El proceso retirado no se borra: se reemplaza por su registro.** Un proceso que desaparece sin dejar rastro hace imposible saber que existió, y **lo que no se sabe que existió no se puede echar de menos.**

```
Registro: [proceso] | Retirado: [fecha] | Clase | Fin | Vacío | Reemplaza a: [NINGUNA - es un retiro]
```

### 5. Separar retiro de reemplazo

| Reemplazo | Retiro |
|---|---|
| entra uno nuevo | **no entra nada** |
| el fin sigue cubierto | el fin se declara |
| `Reemplaza:` apunta al anterior | `Reemplaza: NINGUNA` |

**Un retiro no es un reemplazo sin nombre.** Si entra algo, es mutación.

## Lo que el retiro no hace

**No juzga si el proceso servía.** Un proceso puede ser inútil y su fin seguir existiendo: **entonces no se retira, se muta.**

**No reescribe.** Retirar es sacar; lo que entra después es de `./mutacion.md` o de `./manipulacion.md`.

**No permite el borrado limpio.** Siempre queda el registro y el `Vacío:`.

## Prueba

**Prueba:** ¿El fin está nombrado? ¿La clase es una de las tres? ¿El `Vacío:` se escribió **antes** de retirar? ¿Queda el rastro del proceso retirado? ¿El retiro se distingue de un reemplazo?

**Falsificador:** se retira porque estorba y no porque el fin desapareció; se borra sin dejar rastro; un vacío anotado después del retiro; un retiro con algo nuevo adentro sin declararlo; un retiro sin `Vacío:` cuando el fin sigue existiendo.

## Modos de falla

- **Retiro por fastidio.** Se retira porque molesta, y el fin queda descubierto.
- **Borrado limpio.** Desaparece sin rastro y después nadie sabe que existió.
- **Vacío tardío.** Se anota después, y se olvida.
- **Retiro disfrazado.** Entra algo nuevo y se llama retiro.
- **Fin sin nombre.** Se retira sin decir qué se perseguía.

## Transiciones

- El fin sigue existiendo y el proceso no lo cubre → `./mutacion.md`, no se retira.
- Entra un proceso nuevo → `./manipulacion.md`.
- El vacío hay que cubrirlo → se declara y se abre la tarea que lo cubra.
- El proceso estaba en una sub-tarea → se retira con su registro, y la sub-tarea se declara.
- En cualquier otro caso → se entrega y se cierra.
