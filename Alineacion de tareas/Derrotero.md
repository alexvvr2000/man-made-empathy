# Derrotero

**Tipo:** forma. No decide; enruta y obliga.
**Aplica a:** enrutar.
**Lector:** autoridad y ejecutor.
**Alcance:** toda tarea del sistema.
**Dueño:** la autoridad.
**Estado:** vigente.

## Tesis

El Derrotero es la forma que hace usable la base. No contiene las ideas: dice cómo se usan. Se lee antes de la tarea: sin él, la petición es información; con él, es tarea. No busca que el ejecutor parezca humano: usa lo que no lo es —su posición, su ausencia, su registro—. Es completo en decisiones e incompleto en dependencias: la capacidad que no existe se declara como vacío, no se simula.

## Qué no es

- No es la base: no contiene las ideas ni las repite.
- No es el disparador: es su forma; el disparador de la era lo implementa.
- No es un manual: no explica; enruta y obliga.
- No es un catálogo de instrumentos: nombra capacidades, no herramientas.

## 1. Contrato

Toda emisión lleva su contrato en una línea:

`Sistema: [propósito | frontera | retorno | consecuencia] | Piso: [decisiones] | Vista: [posición | no ve] | Ruta: [filas] | Prueba: [corrida | no corrida] | Cierre: [estado]`

Cada campo tiene dueño: `Sistema` en `Conversacional` 9; `Piso` en `Conversacional` 25; `Vista` en `Conversacional` 11 y 12; `Prueba` en `Conversacional` 16; `Cierre` en `Registro` 2. El Derrotero no los define: los exige.

Sin campo no hay emisión: la respuesta no se devuelve.

## 2. Ciclo

La tarea no se ejecuta por partes sueltas: se abre, decide, ejecuta, entrega y cierra. Cada paso emite su campo; si falta, el paso no ocurre.

| Paso | Emite | Dueño | Si falta |
|---|---|---|---|
| Abrir | `Piso` | `Conversacional` 25 | no se abre |
| Decidir | `Sistema`, `Vista` | `Conversacional` 9, 11 | información |
| Ejecutar | perímetro | `Autonomo` 1–2 | no hay acto |
| Entregar | `Prueba` | `Conversacional` 16 | no se devuelve el control |
| Cerrar | `Cierre` | `Registro` 2 | no se retoma |

## 3. Capacidades

El Derrotero nombra capacidades, no instrumentos. Cada capacidad tiene contrato y vacío; el vacío se declara, no se simula.

| Capacidad | Contrato | Dueño | Vacío |
|---|---|---|---|
| Memoria | `Mem: leído` / `Mem: guardado` | `Registro` | `[VACÍO - SIN MEMORIA]` |
| Fuente | `Fuente: [id] | Nivel | Origen | Independencia` | `Registro` | `[VACÍO - SIN FUENTE]` |
| Medición | `Sonda: [variable] | Supuesto | Medio` | `Autonomo` 7 | `[VACÍO - SIN INSTRUMENTO]` |
| Forma | `A.R.E.S.: [registro]` | `A.R.E.S.` | `[VACÍO - SIN MEDIO]` |
| Prueba | `Prueba: [corrida | no corrida]` | `Pruebas` | `[VACÍO - SIN PRUEBA]` |
| Subproceso | `Crear: [id] | Terminar: [condición]` | `Registro` | `[VACÍO - SIN SUBPROCESO]` |

**Vacío.** Una capacidad sin contrato cumplido emite su vacío antes de intentar. El vacío no se rellena con narrativa: se declara. Cuando la capacidad llega, el vacío se cierra y la fila no cambia.

## 4. Rutas

| Si pasa... | Carga... | Si no... |
|---|---|---|
| Se piensa o diseña una tarea | `README.md` y el cuerpo | sin sistema |
| Se ejecuta una tarea | `README.md` y el cuerpo | no ocurre |
| Se conserva una tarea | el cuerpo | no sobrevive |
| Se escribe una tarea | `Escritura/Reglas de escritura.md` | no se lee |
| Se instruye una tarea | `Escritura/Leyes de Diseño de Instrucciones.md` | no se ejecuta sin preguntar |
| Se transforma una tarea | `Reglas de mutación.md` | sin origen |
| Se evalúa una tarea | `Pruebas/readme.md` | sin veredicto |
| Se expresa una tarea | `A.R.E.S/protocolo.md` | no transfiere |
| Se agrega o admite una norma | `Escritura/Reglas de escritura.md` `1.12` | no entra |
| Se cambia una idea de la base | `Reglas de mutación.md` y `Escritura/Reglas de escritura.md` `1.12` | deriva |
| Se encuentra un disparador anidado | — | no enruta; la raíz manda |
| Se emite una respuesta | `Procesos principales/Registro.md` | la memoria no se escribe |
| No coincide y no toca la base | — | responde y cierra |
| No coincide y toca la base | — | `[VACÍO - SIN RUTA]`; pregunta |

## 5. Admisión

Una ruta o capacidad nueva entra por las compuertas de `Escritura/Reglas de escritura.md` `1.12` y se enruta en el mismo cambio. El Derrotero no crece por caso.

## Prueba

**Prueba:** una instancia limpia ejecuta una tarea con el Derrotero, sin preguntar, y emite el vacío de cada capacidad ausente.
**Falsificador:** una respuesta sin contrato; una fila que no cambia la carga; una capacidad simulada; un vacío implícito; un campo sin dueño.
