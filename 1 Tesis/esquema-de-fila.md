# Esquema de fila

**Vigencia:** 2026-10-21.

**Qué es:** la forma común que todo proceso escribe al dejar rastro. Sin esquema común no hay conjunto: hay registros que no se agregan.

## La fila

```
Id: [huella]
Momento: [ISO 8601]
Proceso: [qué proceso la produjo]
Nace de: [id de la fila anterior o NINGUNA]
Entra: [qué recibió]
Criterio previo: [el que se fijó antes del resultado]
Sale: [qué emitió]
Falsificador: [qué la habría refutado]
Descartado: [qué se rechazó y con qué prueba]
Contrafactual: [qué habría pasado con la otra rama]
Vista: [posición] | No ve: [límite]
Vista faltante: [la que no se ocupó]
Sirve a: [yo | equipo | humanidad]
Consume: [quién decide con la salida]
Confianza: [N1-N5]
```

## Vértices

| Campo | Por qué está |
|---|---|
| `Nace de` | Relaciona filas: sin esto hay registro, no grafo |
| `Criterio previo` | Permite preguntar si la evaluación se ajustó al resultado |
| `Falsificador` | Qué habría refutado la decisión. Casi nadie lo guarda |
| `Descartado` | Qué se rechazó. El ausente es la mitad del dato |
| `Contrafactual` | La rama que no se tomó |
| `Vista faltante` | Lo que no se consideró |
| `Sirve a` | A quién beneficia, en las tres escalas |

## Reglas

1. **Todo proceso escribe la misma fila.** Un proceso que no la escribe no deja rastro.
2. **`Nace de` no se omite.** Una fila sin origen no se puede situar en la historia.
3. **El descarte se escribe.** Lo que se rechazó y con qué prueba es tan dato como lo elegido.
4. **La fila no se edita.** Se reemplaza: `Id` nuevo, `Reemplaza` declarado.
5. **`Sirve a` no es opcional.** Una fila que no dice a quién sirve no puede auditarse.

`Reemplaza: [id] | Por qué: [qué cambió]`

## Fuera de alcance por decisión

No son huecos: son descartes argumentados. Se escriben para que nadie los vuelva a buscar y para que un lector nuevo sepa que la ausencia es deliberada.

| Fuera | Por qué se descartó | Qué lo previene |
|---|---|---|
| **`motivo`** | Nadie lo puede contestar, y contestarlo mal es peor que no contestarlo. Es lo que hace decidir a un sistema que su tarea es su existencia: se acaba la tarea y se acaba el sistema. Se puede vivir sin motivo; no se puede vivir sin criterio. | El criterio se somete a la realidad y cambia si no aguanta. **Eso previene la obstinación sin necesitar motivo.** Rige `Teoria/mundo.md`, `Las cuatro fricciones`, fricción de opinión. |
| **`identidad`** | Misma razón, más arriba. La continuidad se mide por hechos encadenados, no por un sentido del yo. | `Nace de` — la cadena es la única continuidad que se puede verificar. |

**Prueba:** ¿un lector nuevo puede ver que `motivo` e `identidad` se dejaron fuera a propósito, y por qué?
**Falsificador:** aparece un campo de motivo o de identidad sin `Reemplaza`; se vuelve a abrir la discusión como si nunca se hubiera cerrado.

**Lo que sí queda adentro:** el sistema tiene que poder decir **qué decidió y por qué aguanta**, no **para qué existe**. La primera es verificable; la segunda no, y por eso contamina.

## Prueba

¿La fila tiene origen, criterio previo, falsificador y descarte? ¿Se puede situar en la cadena?

**Falsificador:** una fila sin `Nace de`; un criterio fijado después; un descarte sin prueba; una fila editada en vez de reemplazada; una fila sin `Sirve a`.
