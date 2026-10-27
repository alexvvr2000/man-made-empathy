# Implementación — verificación

> Cómo se comprueba una cita en el sistema real. El protocolo solo exige la verificación; este documento describe el instrumento.

## Kestrel — verificación de citas

Las dos variantes usan Kestrel; lo que cambia es cuánto provecho sacan de él.

- **Qué hace:** antes de admitir una cita, comprueba que el texto citado existe literalmente en la fuente guardada (`String.indexOf`). Si la cita tiene menos de **24 caracteres**, se rechaza.
- **Integridad:** los documentos se hashean con **SHA-256** al obtenerlos; si el texto ya no coincide con su hash, todas las citas que descansan en él se rechazan.
- **Coste:** cero tokens de modelo en la verificación; la hace código determinista.
- **`npm run rag:index`:** descartado; Kestrel no indexa, verifica por subcadena y hash.
