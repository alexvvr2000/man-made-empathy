# Notas continuas — el proceso

**Unidad:** tarea.
**Aplica a:** continuar.
**Tipo:** tarea de mantenimiento. Guarda dónde se quedó el trabajo para que la próxima sesión —otra IA, otro día— levante el contexto sin preguntar lo ya dicho.
**Lector:** quien abre una sesión nueva, y quien cierra la actual.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** sesión · estado medido · lo abierto · lo siguiente · vista
**Peor:** el chat se borra y lo que se había decidido se pierde; la sesión siguiente pregunta lo ya contestado, o peor, inventa el estado y cree recordar lo que no midió.
**Quién:** quien abre la sesión siguiente, y quien carga con lo que se perdió.

## Entra | Falla | Sale | Consume

- **Entra:** el trabajo hecho en la sesión y el veredicto del piso.
- **Falla si:** la sesión cierra sin bloque; el `Estado:` se escribe de memoria y no se midió; lo abierto se omite.
- **Sale:** un bloque nuevo al principio de `../../../.sesion-continua/continuas.db`, y los bloques ya cumplidos purgados.
- **Consume:** quien abre la sesión siguiente. **Lee el primer bloque y sabe dónde quedamos.**

## No espera aviso

**El bloque se actualiza al cerrar cada turno que entregó algo.** No hay un momento de cierre que el autor tenga que anunciar: **si el turno cambió un archivo, el bloque se movió antes de contestar.**

**Si dependiera de que alguien diga «acabé la sesión», no se resolvería nada:** se cambiaría una molestia por otra, y lo que no se anuncie se pierde.

**Y no queda en la voluntad de quien escribe:** ../../mantis/piso/notas.ps1 compara el bloque con el archivo cambiado más reciente. **Si el bloque es más viejo, falla.** El piso corre solo, y ahí no hace falta que nadie se acuerde.

**Prueba:** ¿el bloque es más nuevo que el último archivo cambiado? ¿un turno que entregó dejó el bloque movido?

**Falsificador:** un bloque que espera aviso; un turno con archivos cambiados y el bloque quieto; un bloque escrito como recuerdo y no como estado medido.

## Vive fuera del piso

**La sesión es lo más mutable de todo, y por eso no tiene la forma de la tesis.** Su base, su esquema y su export viven **juntos, en .sesion-continua/**, y **no los comparte nadie.**

| Dónde | Qué | Se publica |
|---|---|---|
| .sesion-continua/continuas.db | la base de la sesión | **no** |
| .sesion-continua/esquema.sql | su esquema, que **cambia cuando cambia la sesión** | **no** |
| .sesion-continua/continuas.md | su export | **no** |

**Y el piso no la valida.** Un piso le exige forma a lo que tiene que dar el mismo veredicto en cualquier ejecutor; **la sesión existe justamente porque no tiene forma fija.** Pedirle CHECK y NOT NULL es pedirle que sea otra cosa. Rige ../../../Ouroboros/CRITERIO.md, Unidad y tiro.

**El esquema de la tesis vive en 
otas/esquema.sql; este no se mezcla con él.** Si se mezclaran, **cada cambio de la sesión arrastraría al esquema que no tiene por qué moverse.**

## La forma muta, no crece

**Esto no se agrega: se sustituye.** `continuas.md` tiene **un solo bloque vivo**, el de la sesión actual, **arriba del archivo.** Cuando cierra la sesión siguiente, el bloque viejo **se purga** y el nuevo lo reemplaza.

**Un archivo que solo crece se vuelve un cementerio:** lo importante se hunde bajo lo viejo, y quien llega lo lee entero o no lo lee.

| Lo que pasó | Qué se hace |
|---|---|
| la sesión cierra | el bloque se actualiza en el sitio: **no se agrega otro** |
| el bloque anterior ya se cumplió | **se purga**; su vista ya quedó en el corte de `../notas/generaciones/` |
| algo de lo abierto cambió de dirección | **se sustituye la línea**, no se acumula |

**Y lo que no cabe aquí no se pierde:** lo que valga para la tesis va a `../../../notas/actuales.md`. **La continua es un puntero, no la memoria.**

## El bloque

```
Sesión: [fecha hora] | Repo: [rama, último commit] | Vista: [la de hoy]
Estado: [veredicto de piso.ps1, pegado] | Roto: [qué falla, o ninguno]
Abierto: [lo que se preguntó y no se contestó]
Siguiente: [lo primero que la próxima sesión carga]
Decidido: [solo lo que cambió de dirección, con su porqué]
Rige: claridad | sesgo declarado
```

**`Estado:` no se escribe de memoria: se corre `../../../mantis/piso/piso.ps1` y se pega el veredicto.** Un estado recordado es una alucinación; **uno medido no.** Rige `./notas-tesis.md`, `Notas de tesis`.

**`Siguiente:` es la única línea que inventa, y es una intención, no un hecho.** Se declara como intención.

## Las dos referencias

**No se copian: se citan.**

- **`claridad`** — `../../../Ouroboros/1 Guantelete — primitivo/primitivos/claridad.md`. **El bloque se lee igual en cualquier IA:** sin ambigüedad, sin glosario, sin vocabulario de esta conversación.
- **`sesgo declarado`** — `../../../Ouroboros/1 Guantelete — primitivo/mutaciones/sesgo-declarado.md`. **Cada bloque declara su `Vista`.** Lo que hoy se cree no se presenta como lo que siempre fue; **un cambio de vista se escribe, no se esconde.**

## Vacío

**Si la sesión no dejó bloque, la siguiente sesión no sabe dónde quedamos y lo declara `[VACÍO - SIN BLOQUE]`.** No se improvisa el estado.

## Prueba

¿Hay un solo bloque vivo? ¿El `Estado:` es el de una corrida y no un recuerdo? ¿Lo abierto está? ¿El bloque viejo se purgó? ¿Cada bloque declara «Vista»?

**Falsificador:** un archivo que solo crece; un `Estado:` escrito de memoria; un bloque sin `Siguiente:`; una sesión que cierra sin actualizar el bloque; un cambio de vista que no se declara.

## Transiciones

- Algo de lo abierto se cierra → se sustituye la línea, no se acumula.
- Algo de lo abierto gana peso para la tesis → se anota en `../../../notas/actuales.md`.
- La sesión cerró → el bloque se actualizó en el sitio.
- En cualquier otro caso → se entrega y se cierra.