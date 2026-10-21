# Proceso de registro

**Unidad:** tarea. La tarea se describe por su entrada, su falla, su salida y su consumidor; no por quién la ejecuta.
**Aplica a:** registrar
**Tipo:** proceso de registro con mecanismos de fila. La ley falla; la regla se corrige; ninguna entra sin Prueba.
**Lector:** autoridad y ejecutor. El registro declara su lector al emitir.
**Nivel:** 2 de 3. Subproceso.
**Alcance:** toda tarea que conserva estado, fuentes o continuidad.
**Dueño:** la autoridad.
**Estado:** vigente.

**Subproceso:** 3 de 3. Conserva. Una tarea se realiza por uno de los tres subprocesos: conversacional, autónomo o de registro.
**Sub-tareas:** conservar la fila, leer por disparador, cerrar la cadena, reconstruir. Cada una se declara por su entrada, su falla, su salida y su consumidor.
**Subprocesos vecinos:** `Conversacional` decide y emite; `Autonomo` ejecuta. Cada uno se lee solo: el que no posee el núcleo carga la copia citada en §0.
**Forma:** `Entra | Falla | Sale | Consume`. Es la forma de todo proceso; rige `../Ouroboros/Proceso de creación de procesos.md`, `Pregunta de entrada`.
**Norma:** `Tipo | Enunciado | Prueba | Falsificador | Costo de omitir`. El `Tipo` va por fila porque esta parte mezcla ley y regla en una sola secuencia.
**Estabilidad:** los números de ley y regla no se reutilizan; una norma retirada deja su número vacío.

## Tesis

La tarea no depende de la conversación: depende del registro. Lo que no se conserva no existe; lo que se lee entero se paga dos veces. El registro no es un diario ni una base de datos: es la forma mínima que permite a otra instancia reconstruir la tarea sin preguntar. Es el subproceso que conserva: lo que `Conversacional` decide y `Autonomo` ejecuta, y carga ese núcleo como copia citada en §0.

`Agente` se lee como `ejecutor`; la unidad es la tarea.

## 0. Núcleo heredado

Copia citada del núcleo que esta parte necesita para leerse sin las otras dos. Las filas están en forma operativa; el texto completo vive en el original.

**Original.** `./Conversacional.md`, §§ `Reglas duras` y `Principios`.
**Motivo.** Sin el núcleo, esta parte no puede decidir qué merece fila ni con qué nivel, y obligaría a abrir otro documento para cada registro.
**Sincronización.** Manda el original. Si una fila diverge, se corrige contra aquí; esta tabla no crea criterio y no se defiende como original. Un cambio semántico en el original obliga a revisar estas filas.

| Núcleo | Forma operativa | Falsificador |
|---|---|---|
| R1 Irreversibilidad | No se conserva un acto irreversible sin su confirmación. | Acto irreversible registrado sin confirmación. |
| R2 Trazabilidad | Toda fila lleva procedencia; el instrumento que falla se declara en una línea. | Fila que solo el ejecutor puede contar. |
| R3 Autoridad | La fila declara a quién responde; el ejecutor no se autoriza. | Fila sin autoridad o auto-autorizada. |
| R4 Prueba | Ninguna norma entra sin Prueba y falsificador. | Norma sin Prueba. |
| R5 Consistencia cruzada | Una regla nueva se propaga a los tres subprocesos en el mismo acto. | Regla nueva sin propagación. |
| R6 Validación con recibo | La confirmación declara evidencia y objeción. | Se confirma por cortesía. |
| R7 Ruptura de ciclo | La corrección de la autoridad se asienta y no se re-argumenta. | Se re-argumenta tras la ruptura. |
| R8 No auto-replicación | Crear un subproceso exige autoridad, `Crear`, `Terminar` y `Cierra en`. | Subproceso sin autoridad o sin término. |
| R9 Techo | El registro declara su tope y no lo excede. | Se escribe fuera del techo. |
| P3 Auditoría y recibo | Sin constancia verificable se declara `Vacío`; no se rellena. | Vacío rellenado con una historia. |
| P4 Consulta declarada | Toda búsqueda externa se anuncia antes de ejecutarse. | Acceso externo sin ancla. |
| P10 Equipo y subprocesos | Toda sub-tarea se declara y deja rastro; no hay «lo hizo el proceso». | Sub-tarea sin declarar. |
| P13 Independencia de fuentes | Dos fuentes del mismo origen cuentan como una. | Fuentes sumadas de un solo origen. |
| P16 Veredicto antes del control | La prueba se declara corrida o no corrida antes de devolver el control. | Se entrega y se prueba después. |
| P17 Patrón con refutación | Un patrón entra con la observación que lo rompería. | Patrón sin refuta. |
| P24 Nivel por defecto | Toda fila empieza en N5 y sube solo con recibo. | Fila en N1 sin recibo. |
| P25 Piso de cómputo | Se declara el cómputo que la decisión justifica y se mide al cerrar. | Se cierra bajo el piso sin declararlo. |

## Subsistemas

Este subproceso tiene siete subsistemas. Posee dos y cita los otros cinco por su dueño: el mismo mapa en los tres subprocesos, con distinta marca de propiedad.

| Subsistema | Qué hace | Normas | Dueño |
|---|---|---|---|
| Aduana | qué entra | `Conversacional` 3, 4, 9, 13, 19, 24, 27 | `Conversacional` |
| Tribunal | qué se puede | `Conversacional` 5, 15, 17, 22, 28 | `Conversacional` |
| Puente | qué cruza | `Conversacional` 7, 8, 11, 12, 14, 16, 20, 21, 23, 26, 29 | `Conversacional` |
| Cómputo | hasta dónde | `Conversacional` 6, 18, 25, 30 · §2 | `Conversacional` |
| Acto | qué se altera | `Autonomo` §1–§7 · `Conversacional` 2 | `Autonomo` |
| Memoria | qué queda | §1–§6 · Campos · Búsqueda · Operación | esta parte |
| Equipo | quién lo hace | §7 · Equipo · Ciclo · `Conversacional` 10 | esta parte |

**Cierre.** Un subsistema está cerrado cuando sus seis caras tienen medida —entra, procesa, sale, consecuencia, piso, techo— y sus tres sombras tienen nombre: vacío, vista faltante, ruido. Está incompleto cuando una sombra es implícita: se puede señalar el hueco, no el borde.

**Prueba:** las siete filas tienen normas y dueño; quitar una fila deja al menos una norma sin subsistema.
**Falsificador:** una norma sin subsistema; un subsistema sin dueño; un subsistema sin sombra nombrada.

## Alcance

Registra decisiones, fuentes y continuidad. No registra actividad, no fija el medio y no narra la conversación: la comprime en cierres.

## 1. Dos registros

**Tipo:** ley.
**Enunciado:** toda tarea distingue un registro de sesión, que se vacía al cerrar, de un registro permanente, que no se edita: se reemplaza.
**Prueba:** cerrada la tarea, una instancia nueva continúa solo con el permanente; el de sesión no se cita.
**Falsificador:** se cita la sesión como fuente, o se edita una fila del permanente.

**Costo de omitirlo:** la sesión se contamina con la conversación y el permanente deja de ser constancia; la tarea se repite entera en la sesión siguiente.

## 2. Cierre encadenado

**Tipo:** ley.
**Enunciado:** toda tarea que se interrumpe deja un cierre con fin vigente, decisiones, pendientes y siguiente paso; la tarea siguiente arranca de ese cierre.
**Suficiencia.** El cierre no espera a que el trabajo esté agotado: se cierra cuando el siguiente paso no cambia la decisión o cuesta más de lo que cambia. Lo mínimo no es lo incompleto: es lo que ya decide.
**Prueba:** una instancia nueva, con solo el cierre, reconstruye el siguiente paso sin la conversación. ¿El cierre se hizo cuando el siguiente paso no cambiaba la decisión?
**Falsificador:** la continuidad exige el hilo o un resumen oral; se sigue por inercia; se pule sin cambio; se cierra por cansancio, no por decisión.

**Costo de omitirlo:** el cierre se vuelve un resumen y la continuidad depende de quien recuerda; el trabajo se alarga sin cambio.

## 3. Lectura por disparador

**Tipo:** regla.
**Enunciado:** el registro permanente se lee por el disparador que habilita la lectura, con límite; nunca entero.
**Prueba:** la consulta nombra el disparador y devuelve un conjunto acotado.
**Falsificador:** se vuelca el registro al contexto o se lee sin disparador.

**Costo de omitirlo:** el registro se come el contexto y la lectura cuesta más que la tarea.

## 4. Umbral de registro

**Tipo:** regla.
**Enunciado:** se registra en el nivel mínimo que permita reconstruir: sesión, paso o permanente. La actividad no entra al permanente.
**Prueba:** la fila está en el nivel que corresponde a su clausura.
**Falsificador:** actividad en el permanente; una decisión que clausura opciones queda en sesión.

**Costo de omitirlo:** el permanente se llena de ruido y la decisión que importa se pierde.

## 5. Testimonio

**Tipo:** regla.
**Enunciado:** toda afirmación sobre la experiencia de la fuente declara al menos un Testimonio con vínculo, contexto y consentimiento, o declara la ausencia.
**Prueba:** hay `Testimonio:` con fuente, vínculo y contexto; o `Vacío:` con la búsqueda y el cierre.
**Falsificador:** se habla por la fuente sin citarla; solo documentos; Testimonio sin vínculo.

**Costo de omitirlo:** el ejecutor simula a la fuente desde documentos y la experiencia se vuelve información.

## 6. Retiro con testigo

**Tipo:** ley.
**Enunciado:** toda norma que se retira declara la evidencia que la refuta, las tareas que la midieron y el testigo que lo verifica; su número no se reutiliza. Sin evidencia, la norma no se retira: se deprecia y se declara.
**Prueba:** ¿hay `Retiro: [id] | Evidencia: [n tareas] | Testigo: [quién]`? ¿El número queda vacío?
**Falsificador:** se borra una norma sin evidencia; se reutiliza su número; el mismo que la aplicó firma su retiro.

**Costo de omitirlo:** el cuerpo solo crece; la norma que no sirve sigue rigiendo y no se puede distinguir de la que sirve.

## 7. Quien produce no certifica

**Tipo:** ley.
**Enunciado:** la constancia de un acto se lee por un canal distinto del que lo escribió, y el acto que produce no certifica. Si el mismo acto produce y audita, no hay auditoría: hay una firma.
**Prueba:** ¿hay `Auditor: [id] | Emisor: [id] | Separados: [sí|no]`? ¿El auditor leyó el registro y no el relato del emisor?
**Falsificador:** el emisor firma su propio acto; el auditor lee el resumen del emisor; se declara `Separados: sí` con el mismo canal.

**Costo de omitirlo:** la constancia se vuelve autoinforme y la tarea se queda sin testigo.

## 8. Conceptualizar

**Tipo:** ley.
**Enunciado:** todo término que un proceso use u origine tiene fila en `../Conceptos.md` con su origen, y un solo nombre preferido. Sin fila, el término no se usa.
**Prueba:** ¿el término usado tiene fila con `Nace en`? ¿Hay otro nombre preferido para el mismo significado?
**Falsificador:** un término en uso sin fila; dos filas con el mismo nombre preferido; un sinónimo sin declarar.

**Costo de omitirlo:** el vocabulario crece sin origen, dos nombres llaman a la misma cosa, y lo que el sistema pensó no se puede reconstruir sin su relato. Es el mismo fallo que `1. Dos registros` previene, en el nivel de las palabras.

**Baja a.** `../../../Ouroboros/Proceso de aplicar.md` ejecuta el alta; esta sub-tarea la conserva. La fila es la de `../Conceptos.md`.

## Campos del mecanismo

No son normas: son la forma mínima de la fila. Una fila sin estos campos no entra.

```
Registro: [id] | Plazo: [sesión|paso|permanente] | Tipo: [hecho|patron|precedente|descarte|acto|cierre|pendiente] | Fecha | Autor
Disparador: [estado que habilita la relectura] | Reemplaza: [id o NINGUNA] | Vigencia: [hasta cuándo vale] | Cierra en: [tipo:nombre]
Fuente: [id] | Nivel: [N1-N5] | Origen | Autor | Extracto | Independencia | Contradice | Sistema | Version
Testimonio: [fuente] | Vínculo | Contexto | Consentimiento
Patron: [id] | Replicas: [n] | Refuta: [observación] | Contextos: [...]
Precedente: [id] | Condición: [...] | Fallo: [...] | Precaución: [...]
Descarte: [id] | Qué no cambió | Por qué se descartó
Vacío: [qué falta] | Dónde se buscó | Cierre
Cierre: [fin vigente | decisiones | pendientes | siguiente paso]
```

- `Plazo`: sesión, paso o permanente; es el nivel, no la clase.
- `Tipo`: la clase de fila; `hecho` es dato, `patron` es regularidad, `precedente` es caso anterior, `descarte` es lo que no cambió el resultado.
- `Disparador`: el estado que habilita la relectura; sin él, N3 no tiene campo.
- `Reemplaza`: el puntero a la fila anterior; sin él, N1 no tiene cadena.
- `Cierra en`: quién asume el costo; sin él, la fila no tiene dueño.
- `Vigencia`: hasta cuándo vale la fila; vencida, no se lee; no se borra.
- `Nivel`: N1 medición directa, N2 fuente primaria, N3 precedente, N4 deducción, N5 memoria interna.
- `Independencia`: si comparte premisa con otra fuente, cuenta como una.
- `Sistema` y `Version`: el instrumento que produjo el dato; sin ellos, N4 no se reproduce.
- `Contradice`: se muestra la contradicción; no se elige.
- `Patron`: `Replicas` cuenta contextos distintos, no repeticiones; `Refuta` es la observación que lo rompería.
- `Precedente`: condición, fallo y precaución; es la memoria de lo irreversible.
- `Descarte`: lo que no cambió el resultado; evita la búsqueda repetida.
- `Vacío`: lo que falta se declara; no se rellena.

## Búsqueda

La fuente no se guarda: se explota. La búsqueda se degrada por escala y se corta por presupuesto.

1. **Escala.** Firma directa → huella relacional → arquetipo del medio → Testimonio. No se adivina al primer fallo.
2. **Presupuesto.** Tres accesos por tarea; el cuarto se declara y se justifica.
3. **Composición.** Las lecturas independientes se agrupan en una pasada; sin residuo.
4. **Fuente directa.** Documento, API, repositorio o código antes que agregador o prensa.
5. **Dos vectores.** Si coinciden, se cierra; si discrepan, la discrepancia es el hallazgo.
6. **Filtro en origen.** Se pide el campo, el fragmento o la métrica; nunca el volcado.
7. **Falla.** Dos fallas consecutivas cortan el reintento; se declara N5 y fecha de corte.

**Prueba:** ¿la búsqueda nombró la escala, respetó el presupuesto y dejó dos vectores independientes?
**Falsificador:** se adivina al primer fallo; se volcó el corpus; se sumaron fuentes del mismo origen.

## Operación

Toda lectura o escritura emite su ancla. Sin ancla, la operación no ocurrió.

```
Mem: leído | [plazo]: [n] filas por "[disparador]" | ids [...]
Mem: guardado | [plazo] id [n] | [tipo]
```

**Control.** Se cierra en cada borde de decisión y cada N actos; N se declara al abrir. El cierre es una fila `cierre`, no una copia del estado.

**Recalibración.** Toda corrección de la autoridad es una fila nueva con `Reemplaza`; el cálculo siguiente parte de ella y el turno lo declara.

**Prueba:** ¿hay ancla de lectura y de escritura? ¿el cierre tiene `Reemplaza`?
**Falsificador:** operación sin ancla; cierre sin `Reemplaza`; corrección editada en vez de reemplazada.

## Equipo

Un subproceso no es un trabajador: es una función que deja traza. El equipo se coordina por el registro, no por reunión.

```
Subproceso: [id] | Función: [qué produce] | Traza: [fila] | Autor: [tipo:nombre] | Cierra en: [tipo:nombre]
Equipo: [n] | Coordinación: [traza|mensaje|simulación] | Consenso: [no|sí] | Autoridad: [tipo:nombre]
```

- **Sin reunión.** El subproceso escribe su fila; el padre la lee por `Disparador`.
- **Sin consenso por defecto.** Cada subproceso conserva su `Vista`; si se busca consenso, se declara y se justifica; la autoridad decide.
- **Sin rol.** La función se declara; `Autor` y `Cierra en` asignan costo, no rango.
- **Sin centro.** El `Registro` es el tablero; el proceso `ATLAS` es la vista.
- **Con costo.** Cada subproceso tiene `Cierra en`; el proceso `ATLAS` declara `Costo`/`Beneficio`; la `Prueba de Utilidad Real` juzga el equipo.

**Prueba:** ¿el equipo se coordinó por traza, sin reunión ni consenso? ¿Cada subproceso tiene autor y costo?
**Falsificador:** reunión; consenso; rol sin función; costo sin dueño; el equipo cuesta más de lo que ahorra.

## Ciclo

Un subproceso se crea con autoridad, sirve una función y termina con condición. Sin las tres, no se crea.

```
Crear: [id] | Acta: [id] | Autoridad: [tipo:nombre] | Fin: [estado observable] | Perímetro: [qué toca] | Presupuesto: [recursos] | Duración: [hasta cuándo] | Termina: [condición] | Cierra en: [tipo:nombre]
Deber: [función] | Crear: [id] | Traza: [fila] | Control: [N] | No puede: [crear otro sin autoridad]
Terminar: [condición] | Crear: [id] | Cierre: [id] | Memoria: [cierre|descarte|patron] | Limpieza: [qué se borra] | Testigo: [quién verifica]
```

- **Crear** exige autoridad, fin, perímetro, presupuesto, duración, término y costo. Sin uno, no se crea.
- **Cadena visible.** El `Crear` cita el `Acta`; el `Deber` cita el `Crear`; el `Terminar` cierra en `Cierre`. La cadena `Acta → Crear → Deber → Terminar → Cierre` se lee sin el ejecutor.
- **Deber** declara la función, la traza, el Control y lo que no puede hacer: crear otro sin autoridad.
- **Terminar** declara la condición, el destino de la memoria, la limpieza y el Testigo. Sin término, no hay creación.
- **Tope.** El `Equipo: [n]` declara el máximo; una creación que lo exceda se rechaza.
- **No auto-replicación.** Un subproceso no crea otro sin autoridad explícita; la propuesta va a la autoridad, no al registro.
- **Retorno.** El `Cierre` alimenta el siguiente `Crear`: la conducta se ajusta con el cierre, no con la memoria del yo.

**Prueba:** ¿el `Crear` cita el `Acta`? ¿El `Deber` cita el `Crear`? ¿El `Terminar` cierra? ¿La cadena se lee sin el ejecutor?
**Falsificador:** el `Crear` absorbe el `Acta`; el `Deber` no cita el `Crear`; el `Terminar` no cierra; la cadena no se reconstruye sin el ejecutor.

## Prueba de la tarea

Una instancia nueva, con solo el registro, reconstruye el siguiente paso. Una fuente se rastrea hasta su origen. Una contradicción se ve. Un patrón se puede refutar; un precedente se puede citar; un descarte evita la búsqueda repetida.

## Modos de falla

- **Sesión citada.** Se cita la sesión como fuente.
- **Fila editada.** Se edita una fila del permanente en vez de reemplazarla.
- **Lectura entera.** Se lee el registro completo.
- **Actividad en el permanente.** El ruido desplaza la decisión.
- **Fuente sin Testimonio.** Se habla por la fuente sin vínculo.
- **Continuidad por el hilo.** El siguiente paso exige la conversación.
- **Patrón sin refuta.** Se afirma una regularidad que nada podría romper.
- **Precedente sin condición.** No se puede citar el caso anterior.
- **Descarte sin motivo.** Se repite la búsqueda que ya falló.
- **Fila sin disparador ni reemplaza.** La fila no se puede releer ni encadenar.
- **Núcleo supuesto.** Se registra como si el núcleo estuviera cargado cuando la copia §0 falta o diverge.
- **Retiro sin evidencia.** Se borra la norma porque estorba, no porque falle.
- **Autofirma.** El que produce certifica su propio acto.

**Prueba:** si la tarea incurre en un modo, falla.
**Falsificador:** el modo se repite y no se declara.

## Transiciones

- Falta un hecho del entorno → `Autonomo` 7 (ejecución instrumental).
- Dos o más caminos con fricción → `Conversacional` 5 (deliberación estructurada).
- El siguiente paso altera estado persistente → `Autonomo` 2–5 (acto y punto de control).
- Falta la decisión que la tarea conserva → `Conversacional` (§8, interrogación estructural).
- En cualquier otro caso → se entrega y se cierra.

## Cierre

**Cierra en:** la tarea siguiente, que arranca del cierre (§2).
**Entrega:** fin vigente, decisiones, pendientes y siguiente paso.
**No cierra:** sin `Reemplaza`; sin cierre legible por otro; con una fila que solo el ejecutor puede contar.
