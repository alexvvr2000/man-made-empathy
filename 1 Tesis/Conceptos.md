# Conceptos

**Unidad:** concepto.
**Aplica a:** conceptualizar.
**Tipo:** registro. Se consulta y se conserva; no se ejecuta.
**Nivel:** dato del subproceso de registro. Lo da de alta la sub-tarea `conceptualizar`.
**Lector:** autoridad y ejecutor.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

El origen de cada nombre que usa el sistema. Un concepto sin origen es una palabra que nadie puede reconstruir; dos nombres para el mismo concepto son una lengua sucia.

La regla, y es la que cierra el problema: **un concepto, un nombre preferido**. Los demás se declaran como sinónimos; ninguno manda dos veces.

## La fila

`Concepto: [nombre preferido] | Nace en: [proceso] | Bajó de: [concepto o proceso] | Nuevo: [sí|no] | Sinónimos: [los admitidos] | Calificador: [si el nombre es ambiguo] | Más amplio: [concepto] | Más estrecho: [concepto] | Se usa en: [dónde] | Estado: [vigente|retirado|hipótesis]`

- **Nace en:** el proceso donde apareció. Sin esto, no se puede preguntar de dónde viene.
- **Bajó de:** el concepto o proceso del que se deriva. Si no bajó de nada, `Nuevo: sí` y se declara por qué no existía.
- **Sinónimos:** los nombres que se admiten para el mismo concepto. Uno manda; los demás se escriben, no se inventan.
- **Calificador:** si el nombre es ambiguo, se desambigua con un calificador en vez de renombrarlo.
- **Más amplio / más estrecho:** la relación con otros conceptos. Sin esto, el registro es una lista y no un mapa.
- **Estado:** un concepto retirado no se borra; se marca y se declara su reemplazo.

## Los tres casos

| Caso | Qué se escribe | Qué evita |
|---|---|---|
| **Concepto nuevo** | `Nuevo: sí` + proceso + por qué no existía | que aparezca sin acta |
| **Concepto derivado** | `Bajó de:` + el concepto o proceso que lo origina | que parezca nuevo cuando no lo es |
| **Concepto duplicado** | no se crea fila: se cita la existente y se declara la equivalencia | dos nombres para la misma cosa |

## Cómo se da de alta

1. **Buscar.** ¿Ya existe un concepto con ese nombre, o con otro nombre y el mismo significado?
2. **Clasificar.** Nuevo, derivado o duplicado.
3. **Escribir la fila.** Con su calificador si el nombre es ambiguo.
4. **Verificar la colisión.** Ningún otro concepto usa ese nombre como preferido.
5. **Declarar el uso.** En qué proceso se usa.

**Prohibido** usar un concepto antes de tener su fila.

## Lo que el registro previene

Tres problemas, y tienen nombre en bibliotecología:

| Problema | Qué es | Cómo se resuelve |
|---|---|---|
| **Homógrafo** | mismo nombre, distinto concepto | calificador: "cruce físico" y "cruce de visión" no son lo mismo |
| **Sinónimo** | distinto nombre, mismo concepto | sinónimos declarados; uno manda |
| **Polisemia** | un nombre, varios significados | se separa en filas distintas con calificador |

## Registro

| Concepto | Nace en | Bajó de | Nuevo | Sinónimos | Calificador | Más amplio | Más estrecho | Se usa en | Estado |
|---|---|---|---|---|---|---|---|---|---|
| proceso | Ouroboros | — | sí | — | — | — | abstracción | Ouroboros | vigente |
| guantelete | Guantelete | proceso | sí | Placeholder | — | — | gema | `2 Ouroboros/1 Guantelete/README.md` | vigente |
| gema | Guantelete | guantelete | sí | — | — | guantelete | — | `2 Ouroboros/1 Guantelete/README.md` | vigente |
| abstracción | Ouroboros | proceso | sí | nombre puesto | — | — | primitivo de convención | `README` de Ouroboros | vigente |
| primitivo de convención | S.A.R.A | abstracción | sí | — | — | abstracción | agente | `README` de S.A.R.A | vigente |
| subproceso | S.A.R.A | abstracción | sí | subproceso autónomo, conversacional, de registro | — | proceso | sub-tarea | `punto-de-partida/` | vigente |
| sub-tarea | `punto-de-partida/` | subproceso | sí | — | — | subproceso | — | `punto-de-partida/` | vigente |
| agente | S.A.R.A | abstracción | sí | ejecutor | — | primitivo de convención | subproceso | `README` de S.A.R.A | vigente |
| piso | ATLAS | — | sí | — | — | proceso | — | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| techo | ATLAS | — | sí | — | — | proceso | — | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| cruce | `Pruebas/` | — | sí | — | — | prueba | cruce físico, cruce de visión | `S.A.R.A/Pruebas/prueba de cruce.md` | vigente |
| cruce físico | `Pruebas/` | cruce | sí | — | — | cruce | — | `S.A.R.A/Pruebas/prueba de cruce.md` | vigente |
| cruce de visión | `Pruebas/` | cruce | sí | — | — | cruce | — | `S.A.R.A/Pruebas/prueba de cruce.md` | vigente |
| tendencia | ingeniería inversa | — | sí | — | — | — | — | `Ouroboros/primitivos/ingenieria-inversa.md` | vigente |
| fantasma | S.A.R.A | — | sí | — | — | tarea | — | `README` de S.A.R.A | vigente |
| ACERO | S.A.R.A | — | sí | — | — | propiedad | — | `mantis/mantenimiento/medir-acero.md` | vigente |
| J'ONN | `punto-de-partida/jorrn/` | — | sí | — | — | sub-tarea | producir, declarar lo inesperado | `README` de S.A.R.A | vigente |
| ARDOR | S.A.R.A | alineación, registro, discernimiento, objetivo, responsabilidad | sí | — | — | sistema | S.A.R.A | `README` de S.A.R.A | vigente |
| semilla | `aprendizaje/aprender` | — | sí | condiciones de partida | — | — | — | `aprendizaje/aprender.md` | vigente |
| continuidad | `aprendizaje/aprender` | — | sí | — | — | — | — | `aprendizaje/aprender.md` | vigente |
| situación | `ATLAS` | — | sí | — | — | — | percepción, comprensión, proyección | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| participantes | `ATLAS` | — | sí | — | — | — | — | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| atención conjunta | `ATLAS` | — | sí | foco | — | — | compartido, diádico, triádico | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| acomodación | `ATLAS` | — | sí | acomodo | — | — | converger, divergir | `corpus/ATLAS/Proceso ATLAS.md` | vigente |
| nivel de fuente | `punto-de-partida/evidencia` | — | sí | nivel, N0–N5 | — | — | testigo, medición directa, fuente primaria, precedente, deducción, memoria interna | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| testigo | `punto-de-partida/evidencia` | nivel de fuente | sí | — | — | nivel de fuente (N0) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| medición directa | `punto-de-partida/evidencia` | nivel de fuente | sí | — | — | nivel de fuente (N1) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| fuente primaria | `punto-de-partida/evidencia` | nivel de fuente | sí | — | — | nivel de fuente (N2) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| precedente | `punto-de-partida/evidencia` | nivel de fuente | sí | — | — | nivel de fuente (N3) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| deducción | `punto-de-partida/evidencia` | nivel de fuente | sí | — | — | nivel de fuente (N4) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| memoria interna | `punto-de-partida/evidencia` | nivel de fuente | sí | N5 | — | nivel de fuente (N5) | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| fecha de corte | `punto-de-partida/evidencia` | memoria interna | sí | — | — | — | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| consentimiento | `punto-de-partida/evidencia` | testigo | — | — | — | — | — | `punto-de-partida/evidencia/nivel-de-fuente.md` | vigente |
| ayuda no pedida | `punto-de-partida/evidencia` | — | sí | ayuda no solicitada, ayuda directa | — | — | impedimento | `punto-de-partida/evidencia/ayuda-no-pedida.md` | vigente |
| impedimento | `punto-de-partida/evidencia` | ayuda no pedida | — | — | — | — | — | `punto-de-partida/evidencia/ayuda-no-pedida.md` | vigente |

Treinta y cuatro filas. Doce conceptos estaban en uso sin origen cuando se abrió este registro.

## Prueba

¿Cada concepto que usa el sistema tiene fila con origen? ¿Cada fila tiene un solo nombre preferido?

**Falsificador:** un concepto usado sin fila; dos filas con el mismo nombre preferido; un concepto nuevo sin `Nace en`; un sinónimo que no se declara.

## Lo que no es

- No es un glosario de definiciones: no explica qué significa, registra de dónde viene y cómo se relaciona.
- No es un diccionario de la lengua: solo cubre los nombres del sistema.
- No decide: registra. La autoridad decide cuál nombre manda.
