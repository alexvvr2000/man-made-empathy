# Proceso de producir

**Variables:** subproceso · origen · perímetro · término
**Peor:** se produce sin nombre, sin perímetro y sin término, y después nadie lo puede retirar
**Quién:** quien tiene que sostener lo producido

**Unidad:** proceso/
**Aplica a:** producir/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un sistema que exige que toda pieza cubra un fallo comprobado filtra las ideas nuevas antes de escucharlas/ La idea llega sin fallo previo y se descarta, o se disfraza de arreglo/

Esta vía produce lo que no estaba previsto, sin pedir permiso previo/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** una capacidad que alguien ve posible, sin fallo que la justifique/
- **Falla:** se exige un fallo comprobado antes de producir; se descarta por no caber en una sub-tarea existente/
- **Sale:** un subproceso ejecutable, con lo que produce declarado/
- **Consume:** quien va a usarlo, y la autoridad que responde/

## Cómo se aplica

1/ **Declarar la capacidad/** Qué se ve posible, sin decir qué fallo cubre/ Si se puede nombrar el fallo, no es J'ONN: es una sub-tarea de cobertura/
2/ **Escribir el subproceso/** Con `Entra | Falla | Sale | Consume`, aunque el fallo sea "no produce lo que se espera"/
3/ **Ejecutarlo/** Unas veces será simple; otras llamará a otra API/ La forma la dicta lo que produce/
4/ **Declarar qué salió/** Lo esperado y lo que no se buscaba: rige `declarar-inesperado/md`/
5/ **Cerrar con efecto/** Rige `///autoridad-humanidad/dar-voz/md`, condición de cierre de J'ONN/

`Capacidad: [qué se ve posible] | Subproceso: [qué produce] | Ejecuta: [simple | llama a API] | Efecto: [qué se déclaró]`

## Prueba

¿La capacidad no tiene fallo previo? ¿El subproceso se ejecutó? ¿El cierre declara el efecto?

**Falsificador:** se exige fallo comprobado antes de producir; se descarta una idea por no encajar en una sub-tarea; se produce sin ejecutar; se cierra sin efecto declarado/

## Lo que este proceso no hace

No impide producir algo destructivo/ No hay lista de lo que no se produce/ Lo que hay es registro: qué se hizo, con qué efecto y quién responde/

Si esa ausencia no basta, la contención tiene que vivir fuera de este proceso/ Aquí no se simula/

## Transiciones

- Si aparece un fallo comprobado → se muda a la sub-tarea que lo cubre/
- Si la salida llama a otra API → se declara el colaborador y su coste/
- Si sale algo no comprendido → `declarar-inesperado/md`/
- En cualquier otro caso → se entrega y se cierra/
