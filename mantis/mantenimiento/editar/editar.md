# Editar — el proceso

**Tipo:** proceso de mantenimiento. Once pasos, en orden. Vuelve sobre el estándar y sobre la tesis.
**Alcance:** `../../../Ouroboros/`, `../../../Tesis/`, `../../Era/` y `../../../mantis/`. La implementación de una era no entra salvo que el cambio la produzca.
**Dueño:** la autoridad. El cambio se propone; la autoridad lo autoriza.
**Claridad:** `../../../Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md`.
**Integridad:** `../../../Ouroboros/procesos/integridad.md`. **Corre siempre antes de mutar.**
**Notas:** `../../../AGENTS.md`, `Escribir notas`. Un turno con decisión y sin fila no está entregado.
**Manipulación de procesos:** `../../../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md`.

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

Rutas relativas a la raíz. Cuatro niveles, y el destino es una sola.

| Nivel | Parte | Documento | Gobierna | Entra el proceso que... |
|---|---|---|---|---|
| **Estándar** | Ouroboros | `Ouroboros/formato de proceso.md` | la forma del proceso | dice cómo tiene que ser un proceso |
| **Estándar** | Ouroboros | `Ouroboros/formato de ente.md` | la forma del ente | dice cómo se lee un ente |
| **Estándar** | Ouroboros | `Ouroboros/CRITERIO.md` | la puerta | impide que el criterio se vuelva absoluto |
| **Estándar** | Ouroboros | `Ouroboros/piso.md` | la ejecución | dice qué corre igual en cualquier ejecutor |
| **Estándar** | Ouroboros | `Ouroboros/mutacion.md` | la transformación | dice qué nombre y lugar tiene un cambio |
| **Estándar** | Tesis | `Tesis/README.md` | el porqué de los niveles | explica; no rige |
| **Tesis** | Tesis | `Tesis/Conceptos.md` | el origen de los nombres | da alta un término; lo cita la mutación |
| **Tesis** | Tesis | `Tesis/esquema-de-fila.md` | la forma del rastro | cambia lo que todo proceso escribe al actuar |
| **Instancia** | Ouroboros | `Ouroboros/3 ATLAS — mutación/Proceso ATLAS.md` | la comunicación | gobierna piso, techo, sesgo o registro |
| **Instancia** | Ouroboros | `Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md` | produce procesos | produce o reemplaza un proceso |
| **Instancia** | Ouroboros | `Ouroboros/1 Guantelete — primitivo/herramientas/ingenieria-inversa.md` | deduce procesos | saca un proceso de lo observable |
| **Instancia** | Ouroboros | `Ouroboros/1 Guantelete — primitivo/herramientas/aplicar.md` | la aplicación | ejecuta un proceso o compone dos |
| **Instancia** | Ouroboros | `Ouroboros/1 Guantelete — primitivo/herramientas/mutar.md` | la transformación | gobierna origen, cambio o retorno |
| **Instancia** | Ouroboros | `Ouroboros/1 Guantelete — primitivo/herramientas/claridad.md` | la forma | gobierna la forma de lo que se lee o ejecuta |
| **Instancia** | Ouroboros | `Ouroboros/2 S.A.R.A — mutación/` | N sub-tareas, N procesos | entra el proceso que cubre un fallo comprobado |
| **Instancia** | Ouroboros | `Ouroboros/2 S.A.R.A — mutación/Proceso PROMETEA.md` | crea subprocesos | crea un subproceso, con integridad antes |
| **Tesis** | Tesis | `Tesis/Pruebas/` | la evaluación | mide rendición, utilidad o cruce |
| **Tesis** | Tesis | `.sesion-continua/mantis.db` | la memoria | guarda lo que se dijo y el porqué |
| **Implementación** | Era | `Era/` | una era | traduce un proceso a su era |
| **Registro** | Memoria | `.sesion-continua/mantis.db` | la memoria de la conversación | anota la decisión, la frase o el descarte en el mismo turno |

**Cómo se clasifica.** Un archivo que dice **cómo tiene que ser** algo es estándar. Uno que dice **qué se hace hoy** es instancia. Uno que dice **con qué** es implementación. Uno que dice **qué pasó una vez** es caso, y un caso no entra en `Tesis/`.

**Destino.** Antes de escribir, se declara el nivel y la parte: estándar, instancia, implementación o registro. Si es estándar, se ejecuta el paso 9 completo: **un estándar sin sus instancias revisadas no entra.** Si toca el estándar de `Ouroboros/`, se ejecuta antes `../../../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md` y se mide su efecto en los que componen con él.

**Gana el estándar.** Una instancia no puede contradecir su estándar. Si lo contradice, la instancia se corrige, y si la instancia tenía razón, primero se corrige el estándar y después se propaga.

**Destino único.** El proceso va al documento cuyo `Aplica a` coincide con su tarea; si no coincide con ninguno, no es proceso de la base y se pregunta.

**Tarea sin clase.** La tarea se describe por su entrada, su falla, su salida y su consumidor. Prohibido clasificarla por quién la ejecuta: esa ambigüedad se deja abierta a propósito.

**Pertenencia.** Un documento de la base se sostiene sin nombrar implementaciones: si las quitas y el documento sigue teniendo sentido, es idea; si se queda vacío, es implementación.

**Jerga.** Un nombre interno se usa en el documento que lo gobierna. Fuera de ahí entra con glosa, o no entra. Un nombre interno no sostiene un argumento: si la frase pierde sentido al quitárselo, el argumento era el nombre. Rige `../chequear/auditar-configuracion.md`, `La jerga`.

`Origen: [raíz|Tesis|Ouroboros|Era|mantis] | Nivel: [estándar|instancia|implementación|caso] | Ruta: [la del archivo] | El lector sabe: [sí|con glosa|no]`

**Prueba:** ¿la obligación estaba ya? ¿el destino es uno y su `Aplica a` coincide? ¿el nivel se declaró? ¿la frase se entiende sin conocer el repo?
**Falsificador:** se crea una segunda norma para la misma obligación; entra en el documento que la menciona y no en el que lo gobierna; se toca más de una parte sin declararlo; una frase que pierde sentido al quitarle un nombre interno o una ruta; un estándar sin sus instancias revisadas; un caso presentado como estándar.

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

Se ejecuta `../chequear/auditar-configuracion.md` cuando el cambio altera conteos, nombres o estructura.

## 9. Cascada

**Entra:** el cambio verificado en su parte.
**Sale:** los dependientes revisados o declarados fuera de alcance.
**Falla si:** se cambia una pieza y se deja un documento que la cita con otro significado.

**Dependientes.** Si el cambio toca una sub-tarea o un proceso, se revisan las referencias de `Ouroboros/2 S.A.R.A — mutación/decisión.md` y el mapa de sub-tareas. Si produce una decisión, se anota en `.sesion-continua/mantis.db`. Si cambia una tarea o un campo del disparador, se enruta en `../../../AGENTS.md` en el mismo cambio.

**Reemplazo.** Si el cambio reemplaza un proceso, se declara qué conserva del anterior: un reemplazo que pierde el servicio no entra, rige `../../../Ouroboros/1 Guantelete — primitivo/herramientas/manipulacion.md`, `Lo que funciona ya está viejo`.

## 10. Verificar

**Entra:** el cambio y sus dependientes.
**Sale:** siete líneas: rutas que resuelven, pares que cuadran, numeración sin huecos, referencias que apuntan, cifras que cuadran, esquema que corresponde, jerga con glosa.
**Falla si:** una ruta no resuelve; un par falta; la numeración salta; una referencia apunta a una sección que se movió; una cifra no coincide; el esquema y la base divergen; un nombre interno aparece fuera de su documento sin glosa.

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
