# Registro de la tarea

**Unidad:** tarea.
**Aplica a:** registrar
**Tipo:** leyes y reglas de registro; mecanismos de fila.
**Alcance:** toda tarea que conserva estado, fuentes o continuidad.
**Lector:** autoridad y ejecutor. El registro declara su lector al emitir.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

La tarea no depende de la conversación: depende del registro. Lo que no se conserva no existe; lo que se lee entero se paga dos veces. El registro no es un diario ni una base de datos: es la forma mínima que permite a otra instancia reconstruir la tarea sin preguntar.

`Agente` se lee como `ejecutor`; la unidad es la tarea.

## Qué no es

- No es un diario: no registra actividad.
- No es una base de datos: el medio es un parámetro, no el contrato.
- No es la conversación: la comprime en cierres.

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
- **Sin centro.** El `Registro` es el tablero; el `A.R.E.S.` mapa es la vista.
- **Con costo.** Cada subproceso tiene `Cierra en`; el `A.R.E.S.` mapa declara `Costo`/`Beneficio`; la `Prueba de Utilidad Real` juzga el equipo.

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

## Falsificadores

- Se cita la sesión como fuente.
- Se edita una fila del permanente.
- Se lee el registro entero.
- Se registra actividad en el permanente.
- Se habla por la fuente sin Testimonio.
- La continuidad exige la conversación.
- Un patrón sin refuta.
- Un precedente sin condición.
- Un descarte sin motivo.
- Una fila sin disparador ni reemplaza.

## Transiciones

- Falta un hecho del entorno → `indagacion-instrumental`.
- Dos o más caminos con fricción → `deliberacion-estructurada`.
- El siguiente paso altera estado persistente → `entrega-operacion`.
- En cualquier otro caso → se entrega y se cierra.
