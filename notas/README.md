# notas

**Lector:** el agente que retoma la sesión.
**Dueño:** el agente. Es memoria operativa, no base ni autoridad.
**Regla:** este chat se borra sin aviso. Lo que no esté en `./notas/` no existe después.
**Escritura:** la línea se corrige, no se apila.

No se lleva contador ni se planifica la sesión. El índice se lee al retomar.

**Al retomar:** se abre `estado.md`.

## Cuándo

- Cambió el objetivo, una decisión, una acción irreversible, un error abierto o un dato durable → una línea.
- Se cierra una operación con estado nuevo → una línea.
- Nada de eso → ninguna nota.

## Recibo

Cuando se escribe una nota, la respuesta cierra con `Notas=[archivo]`. Cuando no, no se añade nada: el archivo es la evidencia, no el recibo.

## Dónde

Un archivo por tema. Nombre y formato libres. Al crear uno, se añade su línea al índice.

## Índice

| Archivo | Qué guarda |
|---|---|
| `estado.md` | Estado del proyecto, operación, entorno y autoridad. |
