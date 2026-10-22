# Deterrente de S/A/R/A

**Unidad:** nivel/
**Aplica a:** sostener/
**Tipo:** deterrente de la tarea/ No produce, no ejecuta, no chequea: dice qué pasa si el nivel se viola/
**Lector:** quien va a usar S/A/R/A, y quien va a mutarla/
**Dueño:** la autoridad/
**Estado:** vigente/

## Entra | Falla | Sale | Consume

**Variables:** procesos sueltos · cuerpo · fin · quién decide
**Peor:** S.A.R.A deja de ser una instancia y nadie lo nota: sus cuerpos siguen existiendo sin que se pueda justificar ninguno.
**Quién:** quien usa los cuerpos, y quien muta la fábrica.

- **Entra:** S.A.R.A en uso.
- **Falla si:** no dice qué se pierde si deja de ser instancia; no declara qué conservó del guantelete.
- **Sale:** la tabla Si pasa esto | Se pierde | Y el síntoma es, y el límite de la fábrica.
- **Consume:** quien decide si el paso 2 se sostiene.

**Prueba:** ¿la pérdida se puede señalar? ¿se declara qué conserva del paso 1?

**Falsificador:** un deterrente sin tabla; una mutación que no declara qué conserva de su original.

## Qué es

S/A/R/A es una **instancia que cruzó la puerta de `mutación`** para tareas estándar/ **No es la mutación: es lo primero que la cruza/** Este archivo dice **qué se pierde si deja de ser eso/**

Sin deterrente, S/A/R/A es un fantasma: una carpeta que se mantiene porque está, y que nadie puede justificar cuando deja de servir/

## Lo que se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| una sub-tarea crece sin un fallo que la justifique | deja de ser una abstracción | trabajo que nadie pidió y nadie puede retirar |
| S/A/R/A crea un primitivo propio | **deja de ser mutación** | sus procesos ya no se comparan ni se mueven entre agentes |
| dos sub-tareas se contradicen | el cuerpo no puede decidir | cada mitad parece correcta y juntas no caben |
| una sub-tarea no tiene deterrente | no puede justificarse | es una carpeta con procesos adentro |
| la mutación no declara qué conserva | no se reconstruye el cambio | S/A/R/A parece nueva cada generación y no lo es |

## Lo que S/A/R/A no es

**No es un lenguaje/** Usa el de `//////1 Guantelete — primitivo/`; si necesitara primitivos propios, sería otro sistema/

**No es una era/** No caduca cuando cambia la tecnología: caduca si deja de tener un fallo que la justifique/

**No es una mutación/** Una mutación nace de una gema y declara qué conserva/ S/A/R/A nace de **todas**, y por eso es instancia: rige `//////1 Tesis/SARA 1/md`, `S/A/R/A nace de Ouroboros, y no es una pieza suya`/

**No es un catálogo/** Sus sub-tareas no son una lista de temas: cada una cubre **un fallo comprobado/** Una que no lo cubre no entra/

## Prueba

¿S/A/R/A sigue sin primitivos propios? ¿Cada sub-tarea declara su deterrente? ¿Cada proceso tiene `Falsificador`? ¿Alguna sub-tarea cubre un fallo que ya no existe?

**Falsificador:** S/A/R/A con primitivos propios; una sub-tarea sin deterrente; una sub-tarea cuyo fallo ya no existe y no se retiró; un proceso sin quién lo refute/

## Transiciones

- S/A/R/A necesita una gema que no tiene → se declara en `///1 Guantelete — primitivo/primitivos/`, y deja de ser instancia/
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira/
- La conjunción se cierra → la tarea siguiente arranca de `//README/md`/
- En cualquier otro caso → se entrega y se cierra/
