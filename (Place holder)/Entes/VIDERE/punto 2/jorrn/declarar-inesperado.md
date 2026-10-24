# Proceso de declarar lo inesperado

**Variables:** lo inesperado · nombre · efecto · cierre
**Peor:** lo inesperado se calla y se cierra como si fuera previsto
**Quién:** quien recibe el efecto que nadie declaró

**Unidad:** proceso/
**Aplica a:** declarar/
**Vigencia:** 2026-10-21/
**Estado:** vigente/

## Qué resuelve

Un proceso de J'ONN produce algo que no estaba previsto y nadie lo registraba, porque el esquema solo admitía lo que tenía criterio previo/ Lo inesperado se descartaba o se disfrazaba/

## Pregunta de entrada

`Entra | Falla | Sale | Consume`

- **Entra:** la salida de un proceso de J'ONN/
- **Falla:** sale algo que no estaba previsto y no se registra; lo inesperado se presenta como si hubiera sido buscado/
- **Sale:** la fila con `origen: explora` y lo inesperado declarado/
- **Consume:** quien decide con esa salida/

## Cómo se aplica

1/ **Separar lo buscado de lo encontrado/** Qué se quería producir y qué salió además/
2/ **Declarar el origen/** `origen: explora`/ No tiene criterio previo porque no había nada que esperar/
3/ **Declarar lo inesperado/** Qué salió que no se buscaba, aunque no se comprenda/
4/ **Declarar si sirve/** A quién beneficia y si alguien lo usó/
5/ **Registrar/** En `/contexto/memoria/db`, tabla `fila`, con `origen` e `inesperado`/

`Buscado: [qué] | Encontrado: [qué salió además] | Inesperado: [qué no se comprende] | Sirve a: [escala] | Uso: [quién lo usó]`

## Prueba

¿La fila declara `origen: explora`? ¿Lo inesperado está escrito, aunque no se entienda?

**Falsificador:** lo inesperado se presenta como buscado; una salida de J'ONN sin fila; lo no comprendido se descarta por no caber en una sub-tarea/

## El campo que faltaba

El esquema de fila no tenía dónde poner esto/ Se le agregan dos columnas:

| Columna | Qué guarda |
|---|---|
| `origen` | `cubre` o `explora`/ Sin esto, la fila no distingue qué clase es |
| `inesperado` | lo que salió y no se buscaba/ Sin esto, el registro obliga a que todo lo nuevo parezca previsto |

## Transiciones

- Si lo inesperado produce un fallo comprobable → se muda a la sub-tarea que lo cubre/
- Si nadie lo usa en tres tareas → se marca y se declara/
- En cualquier otro caso → se entrega y se cierra/
