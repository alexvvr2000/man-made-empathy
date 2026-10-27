# Deterrente de S.A.R.A

**Unidad:** nivel.
**Aplica a:** sostener.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: dice qué pasa si el nivel se viola.
**Lector:** quien va a usar S.A.R.A, y quien va a mutarla.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es

S.A.R.A es una **mutación de Ouroboros** para tareas estándar. Este archivo dice **qué se pierde si deja de ser eso.**

Sin deterrente, S.A.R.A es un fantasma: una carpeta que se mantiene porque está, y que nadie puede justificar cuando deja de servir.

## Lo que se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| una sub-tarea crece sin un fallo que la justifique | deja de ser una abstracción | trabajo que nadie pidió y nadie puede retirar |
| S.A.R.A crea un primitivo propio | **deja de ser mutación** | sus procesos ya no se comparan ni se mueven entre agentes |
| dos sub-tareas se contradicen | el cuerpo no puede decidir | cada mitad parece correcta y juntas no caben |
| una sub-tarea no tiene deterrente | no puede justificarse | es una carpeta con procesos adentro |
| la mutación no declara qué conserva | no se reconstruye el cambio | S.A.R.A parece nueva cada generación y no lo es |

## La estructura

```
S.A.R.A              ← la tarea. Este deterrente.
  └── punto-de-partida     el cuerpo: 16 sub-tareas, 27 procesos
        ├── sub-tarea      declara su deterrente en su README
        │     └── proceso  declara su Falsificador
        └── ...
```

**Un nivel, un deterrente.** La tarea tiene el suyo; cada sub-tarea el suyo, dentro de su `README` como campo; cada proceso su `Falsificador`. **No se hereda hacia abajo ni se suma hacia arriba:** cada nivel responde por sí mismo.

## Lo que S.A.R.A no es

**No es un lenguaje.** Usa el de `../Ouroboros/`; si necesitara primitivos propios, sería otro sistema.

**No es una era.** No caduca cuando cambia la tecnología: caduca si deja de tener un fallo que la justifique.

**No es un catálogo.** Sus sub-tareas no son una lista de temas: cada una cubre **un fallo comprobado.** Una que no lo cubre no entra.

## Prueba

¿S.A.R.A sigue sin primitivos propios? ¿Cada sub-tarea declara su deterrente? ¿Cada proceso tiene `Falsificador`? ¿Alguna sub-tarea cubre un fallo que ya no existe?

**Falsificador:** S.A.R.A con primitivos propios; una sub-tarea sin deterrente; una sub-tarea cuyo fallo ya no existe y no se retiró; un proceso sin quién lo refute.

## Transiciones

- S.A.R.A necesita un primitivo que no tiene → se declara en `../Ouroboros/primitivos/`, y deja de ser mutación.
- Una sub-tarea no puede declarar su deterrente → se declara fantasma y se retira.
- La conjunción se cierra → la tarea siguiente arranca de `./README.md`.
- En cualquier otro caso → se entrega y se cierra.
