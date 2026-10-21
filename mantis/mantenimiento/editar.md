# Editar

**Tipo:** proceso de mantenimiento. Ocho pasos, en orden. Vuelve sobre Ouroboros y sobre las abstracciones.
**Alcance:** los archivos de `../../Alineacion de tareas/` y de `../`. Las implementaciones no entran.
**Dueño:** la autoridad. El cambio se propone; la autoridad lo autoriza.
**Claridad:** `../../Alineacion de tareas/Ouroboros/Proceso de claridad.md`.
**Creación de procesos:** `../../Alineacion de tareas/Ouroboros/Proceso de creación de procesos.md`.

## Parámetros del repo

Tres valores. Si el proceso se muda a otro repositorio, cambian estos y los pasos no.

`Archivo: [documento de la base o de este derrotero] | Caso: [lo que la norma prohíbe o exige] | Invariantes: [par Prueba/Falsificador · rutas resuelven · numeración continua · referencias apuntan]`

## 1. Leer

**Entra:** la petición.
**Sale:** el archivo leído entero y la lista de documentos que lo citan.
**Falla si:** se edita un archivo que no se leyó; se toca una sección sin saber quién la cita.

## 2. Localizar

**Entra:** la obligación.
**Sale:** el destino y la declaración `qué cambia | qué conserva | qué elimina`, o la decisión de que no entra.
**Falla si:** ya existía y se escribió otra vez; no encaja en la tabla y se escribió igual; el uso era «una vez» y se escribió como norma.

**Si ya existe:** se calibra en la sección que la posee; no se crea una segunda.

**Clasificación.** `cambio=[puede|debe] | uso=[una vez|recurrente]`. Lo recurrente entra a la base; lo que ocurre una vez se ejecuta y se informa; un efecto se registra y se mide, y no se escribe como norma hasta que una decisión dependa de él.

Rutas relativas a `../../Alineacion de tareas/`.

| Documento | Parte | Gobierna | Entra el proceso que... |
|---|---|---|---|
| `Ouroboros/Proceso de creación de procesos.md` | Ouroboros | produce procesos | produce o reemplaza un proceso |
| `Ouroboros/Proceso de ingeniería inversa.md` | Ouroboros | deduce procesos | saca un proceso de lo observable |
| `Ouroboros/Proceso de aplicar.md` | Ouroboros | la aplicación | ejecuta un proceso o compone dos |
| `Ouroboros/Proceso de mutación.md` | Ouroboros | la transformación de un proceso | gobierna origen, cambio o retorno |
| `Ouroboros/Proceso de claridad.md` | Ouroboros | la claridad de un artefacto | gobierna la forma de lo que se lee o ejecuta |
| `Ouroboros/Proceso ATLAS.md` | Ouroboros | la comunicación | gobierna piso, techo, sesgo o registro |
| `Ouroboros/indice de formas.md` | Ouroboros | el índice de formas | registra una forma que pasó su prueba |
| `S.A.R.A/punto-de-partida/` | sub-tareas | N sub-tareas, cada una con N procesos | entra el proceso que cubre un fallo comprobado |


| `punto-de-partida/README.md` | abstracción | el índice de abstracciones | ninguna: solo apunta |
| `Derrotero.md` | abstracción | el enrutamiento | declara condición, proceso y consecuencia |
| `Pruebas/` | abstracción | la evaluación | mide rendición, utilidad o cruce |

**Destino.** El proceso va al documento cuyo `Aplica a` coincide con su tarea; si no coincide con ninguno, no es proceso de la base y se pregunta.

**Destino.** Antes de escribir, se declara si el cambio va a Ouroboros (un primitivo) o a una abstracción. Si toca un primitivo, se ejecuta antes `Ouroboros/Proceso de creación de procesos.md` y se mide su efecto en los que componen con él.

**Tarea sin clase.** La tarea se describe por su entrada, su falla, su salida y su consumidor. Prohibido clasificarla por quién la ejecuta: esa ambigüedad se deja abierta a propósito.

**Pertenencia.** Un documento de la base se sostiene sin nombrar implementaciones: si las quitas y el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Disparador.** El disparador apunta, no contiene: una regla, un ejemplo o una explicación en él lo descalifica.

**Prueba:** ¿la obligación estaba ya? ¿el destino es uno y su `Aplica a` coincide?
**Falsificador:** se crea una segunda norma para la misma obligación; entra en el documento que la menciona y no en el que la gobierna.

## 3. Escribir el caso

**Entra:** el destino.
**Sale:** una frase con sujeto y acto: la situación concreta que la norma prohíbe o exige.
**Falla si:** el caso no se puede señalar en un archivo; el caso es la norma repetida con otras palabras.

## 4. Escribir desde el caso

**Entra:** el caso.
**Sale:** el falsificador, luego la Prueba, luego el enunciado, en ese orden.
**Falla si:** el enunciado se escribió antes del falsificador; el falsificador no se puede cumplir.

## 5. Partir y podar

**Entra:** el bloque escrito.
**Sale:** el bloque con una obligación por enunciado y sin lo que no cambia una decisión.
**Falla si:** quedan dos obligaciones unidas por «y», «o» o una enumeración; sobrevive un párrafo que no cambia ninguna decisión.

**Poda.** Una fila sin tarea se elimina; una copia sin cita se elimina; un huérfano se reporta y se corrige.

## 6. Releer

**Entra:** el archivo editado.
**Sale:** el archivo leído de arriba abajo, con sus dependientes revisados o declarados fuera de alcance.
**Falla si:** se revisa el diff y no el archivo; queda una sección que ya no encaja con la de arriba.

**Dependientes.** Si el cambio toca una sub-tarea o un proceso, se revisan las referencias de `S.A.R.A/punto-de-partida/README.md` y el mapa de sub-tareas. Si mueve o renumera, se revisan las rutas. Si cambia una tarea o un campo del disparador, se enruta en `../../AGENTS.md` en el mismo cambio.

**Cascada.** Si el cambio produce o toca un primitivo de Ouroboros, se revisa el mapa de `README.md` y el `Aplica a` de las abstracciones que lo carguen. Si el cambio reemplaza un proceso, se declara qué conserva del anterior: un reemplazo que pierde el servicio no entra, rige `Ouroboros/Proceso de creación de procesos.md`, `Lo que funciona ya está viejo`.

## 7. Verificar

**Entra:** el cambio.
**Sale:** tres líneas: rutas que resuelven, pares que cuadran, numeración sin huecos, referencias que apuntan.
**Falla si:** una ruta no resuelve; un par falta; la numeración salta; una referencia apunta a una sección que se movió.

## 8. Entregar y declarar

**Entra:** el cambio verificado, o la serie verificada.
**Sale:** los archivos en el árbol, git intacto, y una de dos declaraciones. **Cambio suelto:** qué archivo, qué líneas, qué cambió, en tres líneas. **Serie:** una fila por cambio —`archivo | líneas | qué`— y el total; se aprueba la tabla, no el diff.
**Falla si:** se toca git; la serie no declara cuántos cambios trae; una fila no dice qué cambió.

## Serie

**Enunciado:** una serie es un mandato con varios cambios del mismo intento. Se entrega por etapas: cada etapa deja el repo completo y verificado, y declara qué sigue.
**Prueba:** ¿la etapa se verifica sola? ¿se declaró qué sigue?
**Falsificador:** se entrega todo junto y la primera revisión es al final; una etapa deja el repo a medias; una etapa no dice qué sigue.

**Etapa.** Se corta donde el repo queda coherente: un archivo, un grupo de normas, una sección. Nunca por cantidad.

## Orden

Los pasos no se saltan y el 3 no se cambia por el 4. Un mandato a la vez: dentro del mandato van varios cambios en serie; entre mandatos, se espera. El commit, el push y la corrección son de la autoridad; corregida una fila, se re-declara esa fila y no la serie entera. Un turno sin archivo cambiado no es una edición: se declara el vacío.
