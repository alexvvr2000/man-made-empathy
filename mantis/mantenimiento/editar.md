# Editar

**Tipo:** proceso de mantenimiento. Once pasos, en orden. Vuelve sobre Ouroboros y sobre las abstracciones.
**Alcance:** `../Ouroboros/`, `../S.A.R.A/`, `../Agentes/` y `../.contexto/`. La implementación de una era no entra salvo que el cambio la produzca.
**Dueño:** la autoridad. El cambio se propone; la autoridad lo autoriza.
**Claridad:** `../Ouroboros/Proceso de claridad.md`.
**Creación de procesos:** `../Ouroboros/Proceso de creación de procesos.md`.

## Parámetros del repo

Tres valores. Si el proceso se muda a otro repositorio, cambian estos y los pasos no.

`Archivo: [documento o base] | Caso: [lo que la norma prohíbe o exige] | Invariantes: [par Prueba/Falsificador · rutas resuelven · numeración continua · referencias apuntan · cifras cuadran]`

## 1. Leer

**Entra:** la petición.
**Sale:** el archivo leído entero y la lista de documentos que lo citan.
**Falla si:** se edita un archivo que no se leyó; se toca una sección sin saber quién la cita.

## 2. Localizar

**Entra:** la obligación.
**Sale:** la parte, el destino y la declaración `qué cambia | qué conserva | qué elimina`, o la decisión de que no entra.
**Falla si:** ya existía y se escribió otra vez; no encaja en la tabla y se escribió igual; el uso era «una vez» y se escribió como proceso.

**Si ya existe:** se calibra en la sección que lo posee; no se crea una segunda.

**Clasificación.** `cambio=[puede|debe] | uso=[una vez|recurrente]`. Lo recurrente entra a la base; lo que ocurre una vez se ejecuta y se informa; un efecto se registra y se mide, y no se escribe como proceso hasta que una decisión dependa de él.

Rutas relativas a la raíz. Tres partes, y el destino es una sola.

| Parte | Documento | Gobierna | Entra el proceso que... |
|---|---|---|---|
| **Ouroboros** | `Ouroboros/Proceso de creación de procesos.md` | produce procesos | produce o reemplaza un proceso |
| **Ouroboros** | `Ouroboros/Proceso de ingeniería inversa.md` | deduce procesos | saca un proceso de lo observable |
| **Ouroboros** | `Ouroboros/Proceso de aplicar.md` | la aplicación | ejecuta un proceso o compone dos |
| **Ouroboros** | `Ouroboros/Proceso de mutación.md` | la transformación | gobierna origen, cambio o retorno |
| **Ouroboros** | `Ouroboros/Proceso de claridad.md` | la forma | gobierna la forma de lo que se lee o ejecuta |
| **Ouroboros** | `Ouroboros/Proceso ATLAS.md` | la comunicación | gobierna piso, techo, sesgo o registro |
| **Abstracción** | `S.A.R.A/punto-de-partida/` | N sub-tareas, N procesos | entra el proceso que cubre un fallo comprobado |
| **Abstracción** | `S.A.R.A/Conceptos.md` | el origen de los nombres | da alta un término |
| **Abstracción** | `S.A.R.A/Proceso PROMETEA.md` | crea subprocesos | crea un subproceso del agente |
| **Abstracción** | `S.A.R.A/Pruebas/` | la evaluación | mide rendición, utilidad o cruce |
| **Abstracción** | `S.A.R.A/Derrotero.md` | el enrutamiento | declara condición, proceso y consecuencia |
| **Implementación** | `Agentes/` | una era | traduce un proceso a su era |
| **Registro** | `.contexto/memoria.sql` | los datos | registra una fila o un concepto |

**Destino.** Antes de escribir, se declara la parte: Ouroboros, abstracción, implementación o registro. Si toca Ouroboros, se ejecuta antes `../Ouroboros/Proceso de creación de procesos.md` y se mide su efecto en los que componen con él.

**Destino único.** El proceso va al documento cuyo `Aplica a` coincide con su tarea; si no coincide con ninguno, no es proceso de la base y se pregunta.

**Tarea sin clase.** La tarea se describe por su entrada, su falla, su salida y su consumidor. Prohibido clasificarla por quién la ejecuta: esa ambigüedad se deja abierta a propósito.

**Pertenencia.** Un documento de la base se sostiene sin nombrar implementaciones: si las quitas y el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Prueba:** ¿la obligación estaba ya? ¿el destino es uno y su `Aplica a` coincide?
**Falsificador:** se crea una segunda norma para la misma obligación; entra en el documento que la menciona y no en el que lo gobierna; se toca más de una parte sin declararlo.

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

## 6. Revisar por cambio

**Entra:** el cambio, no el archivo.
**Sale:** el cambio leído con su alcance declarado: qué tocó y qué dejó intacto.
**Falla si:** se revisa el archivo entero por inercia; el cambio no declara su alcance; el cambio pasa de 400 líneas y no se parte en etapas.

**Límite de revisión.** Un cambio mayor a 400 líneas se parte. La investigación es consistente: más rápido no encuentra errores.

`Cambio: [n líneas] | Etapas: [n] | Alcance: [qué toca] | Intacto: [qué no]`

## 7. Revisor distinto

**Entra:** el cambio revisado.
**Sale:** la verificación por quien no lo produjo, o la declaración de que no hay revisor.
**Falla si:** el que edita se certifica a sí mismo y no lo declara.

**Sin revisor.** Si no hay una instancia distinta del que editó, se declara `Sin revisor independiente` y el cambio se entrega marcado. No se simula la independencia.

`Revisor: [id] | Produjo: [id] | Separados: [sí|no] | Si no: [Sin revisor independiente]`

## 8. Contrastar configuración

**Entra:** el repo después del cambio.
**Sale:** las cifras y nombres que el cambio dejó desactualizados, o la declaración de que ninguna.
**Falla si:** el cambio altera un conteo y no lo actualiza donde se dice; queda una ruta o un nombre muerto.

Se ejecuta `./auditar-configuracion.md` cuando el cambio altera conteos, nombres o estructura.

## 9. Cascada

**Entra:** el cambio verificado en su parte.
**Sale:** los dependientes revisados o declarados fuera de alcance.
**Falla si:** se cambia una pieza y se deja un documento que la cita con otro significado.

**Dependientes.** Si el cambio toca una sub-tarea o un proceso, se revisan las referencias de `S.A.R.A/punto-de-partida/README.md` y el mapa de sub-tareas. Si toca la base, se ejecuta `./verificar-esquema.md`. Si cambia una tarea o un campo del disparador, se enruta en `../../AGENTS.md` en el mismo cambio.

**Reemplazo.** Si el cambio reemplaza un proceso, se declara qué conserva del anterior: un reemplazo que pierde el servicio no entra, rige `../Ouroboros/Proceso de creación de procesos.md`, `Lo que funciona ya está viejo`.

## 10. Verificar

**Entra:** el cambio y sus dependientes.
**Sale:** seis líneas: rutas que resuelven, pares que cuadran, numeración sin huecos, referencias que apuntan, cifras que cuadran, esquema que corresponde.
**Falla si:** una ruta no resuelve; un par falta; la numeración salta; una referencia apunta a una sección que se movió; una cifra no coincide; el esquema y la base divergen.

## 11. Entregar y declarar

**Entra:** el cambio verificado, o la serie verificada.
**Sale:** los archivos en el árbol, git intacto, y una de dos declaraciones. **Cambio suelto:** qué archivo, qué líneas, qué cambió, en tres líneas. **Serie:** una fila por cambio —`archivo | líneas | qué`— y el total; se aprueba la tabla, no el diff.
**Falla si:** se toca git; la serie no declara cuántos cambios trae; una fila no dice qué cambió.

## Serie

**Enunciado:** una serie es un mandato con varios cambios del mismo intento. Se entrega por etapas: cada etapa deja el repo completo y verificado, y declara qué sigue.
**Prueba:** ¿la etapa se verifica sola? ¿se declaró qué sigue?
**Falsificador:** se entrega todo junto y la primera revisión es al final; una etapa deja el repo a medias; una etapa no dice qué sigue.

**Etapa.** Se corta donde el repo queda coherente: un archivo, un grupo de procesos, una sección. Nunca por cantidad.

## Orden

Los pasos no se saltan y el 3 no se cambia por el 4. Un mandato a la vez: dentro del mandato van varios cambios en serie; entre mandatos, se espera. El commit, el push y la corrección son de la autoridad; corregida una fila, se re-declara esa fila y no la serie entera. Un turno sin archivo cambiado no es una edición: se declara el vacío.
