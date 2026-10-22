# Punto de partida

**Vigencia:** 2026-10-21.

**Qué es:** el conjunto de procesos que la industria tiene probados para resolver lo que falla en la IA hoy, con sus tres escalas de autoridad. Es el punto de partida declarado, no un estándar.

## La forma

```
tarea
  └── sub-tarea (carpeta)  × N
        └── proceso        × N
```

**N no tiene número fijo.** Ni las sub-tareas ni los procesos. Hoy son dieciséis sub-tareas y veinticinco procesos; mañana pueden ser otros, con otros nombres, u otro número.

**Todo muta sin límite.** Una sub-tarea puede desaparecer entera, un proceso puede reemplazarse por uno que no se parezca en nada, y puede entrar uno que cubra un fallo que hoy no existe. Rige `../../Ouroboros/Proceso de mutación.md`, `Mutar la serie`.

**Ninguna jerarquía.** Las sub-carpetas son hermanas. Los procesos dentro de una también. Ninguno manda sobre otro, y ninguno posee un núcleo que los demás citen.

## La fila

Todo proceso deja rastro con la misma forma: `./esquema-de-fila.md`. Sin esquema común no hay conjunto, hay registros que no se agregan.

La fila guarda lo que casi nadie guarda: **el criterio previo, el falsificador, lo descartado y el contrafactual**. Eso es lo que la vuelve distinta de un registro de actividad, y lo que la haría única si alguien la llena en volumen.

## Las sub-tareas de hoy

### Lo que se produce

| Sub-tarea | Fallo que cubre | Procesos |
|---|---|---|
| `requisitos/` | no se sabe qué se quiere | especificar, verificar requisito |
| `evaluacion/` | no se sabe si mejoró | evaluar, probar regresión, vigilar tendencias, deliberar |
| `evidencia/` | alucina sin constancia | trazar |
| `sesgo/` | hereda el prejuicio | auditar sesgo |
| `versionado/` | cambia sin que nadie lo note | versionar |
| `despliegue/` | se suelta sin medir | desplegar |
| `reproduccion/` | no se puede repetir | reproducir |
| `seguridad/` | se le salen las manos | contener |
| `costo/` | cuesta más de lo que sirve | acotar |
| `vocabulario/` | el vocabulario crece sin origen | conceptualizar |
| `alineacion/` | se comporta distinto cuando lo observan | supervisar, entender salida, pluralizar autoridad |

### A quién sirve

Tres escalas de autoridad. Cada una declara un afectado distinto y no se funden entre sí: si se juntan, la que sirve a la humanidad se diluye en la que sirve al equipo, y ese es justo el fallo que se quiere evitar.

| Sub-tarea | Fallo que cubre | Procesos |
|---|---|---|
| `autoridad-yo/` | se decide sin saber a quién beneficia | declarar interés |
| `autoridad-equipo/` | se optimiza para uno y se perjudica a los demás | identificar partes |
| `autoridad-humanidad/` | el efecto se mide solo en quienes tienen voz | dar voz |

**Sin voz, no hay decisión.** Una decisión que afecta a quien no puede expresarse no entra si su efecto sobre esa parte no está declarado. La ausencia de voz se nombra; no se asume que no importa. Rige `./autoridad-humanidad/dar-voz.md`.

### Cómo trabajan juntos

| Sub-tarea | Fallo que cubre | Procesos |
|---|---|---|
| `concordia/` | se optimiza un colaborador y se arruina la cadena; el operador se vuelve apéndice | componer, armonizar, auditar dependencia |

**La composición no es buena por su coste.** Es buena si su coste se paga con beneficio para las tres escalas y si el operador sigue pudiendo hacerlo sin ella. Rige `./concordia/README.md`.

### Lo que no estaba previsto

| Sub-tarea | Qué admite | Procesos |
|---|---|---|
| `jorrn/` | procesos que no cubren fallos: producen lo que no se busca | producir, declarar lo inesperado |

**Un proceso nace de un fallo comprobado o de una capacidad sin fallo previo.** El primero se mide contra el fallo. El segundo se mide por lo que produce. Ninguno reemplaza al otro.

J'ONN no es un safeguard: no impide producir algo destructivo. Impide **cerrar como si fuera seguro lo que no se declaró**. Rige `./autoridad-humanidad/dar-voz.md`.

**Dieciséis sub-tareas, veinticinco procesos.** Es lo que el estado del arte sostiene hoy. No es el mínimo ni el máximo.

## Cómo se ejecuta

Una tarea entra, se elige la sub-tarea que cubre su fallo, y se aplican sus procesos. Cada proceso tiene `Entra | Falla | Sale | Consume` y se aplica solo: ninguno necesita leer los otros veinticuatro para funcionar.

`Fallo: [el que cubre la sub-tarea] | Sub-tarea: [cuál] | Procesos: [cuáles] | Niveles: 3 | Muta: [sí]`

## Prueba

¿Cada proceso declara su fallo y se aplica solo? ¿Las sub-tareas son hermanas? ¿El conjunto puede cambiar sin tocar otro? ¿Toda fila dice a quién sirve?

**Falsificador:** una sub-tarea que manda sobre otra; un proceso que necesita otro para funcionar; un conjunto que solo crece; un nivel que no sea tarea, sub-tarea o proceso; una fila sin `Sirve a`.

## Lo que sigue

De aquí en adelante es terreno inexplorado. Lo que está declarado se puede medir; lo que no, no se afirma. Rige `../README.md`, `Nota para las siguientes generaciones`.

> El conflicto no es malo: creó la bomba atómica, y abandonarlo trae las mismas pérdidas, solo que más lentas y menos visibles.

