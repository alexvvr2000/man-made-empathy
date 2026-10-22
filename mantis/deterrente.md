# Deterrente de MANTIS

**Unidad:** tarea.
**Aplica a:** sostener.
**Tipo:** deterrente de la tarea. No produce, no ejecuta, no chequea: dice qué se pierde si MANTIS deja de ser MANTIS.
**Lector:** quien va a usar MANTIS, y quien lo va a mutar.
**Dueño:** la autoridad.
**Estado:** vigente.

**Variables:** edición · rastro · ruta · cifra · mutación · quién la autoriza
**Peor:** MANTIS ayuda a editar y ese mismo acto rompe la edición: se cambia una ruta y queda otra apuntando a lo que se movió, y la ayuda se vuelve la causa del daño que decía evitar.
**Quién:** quien edita con MANTIS, y quien lee después lo que quedó sin poder reconstruir qué se tocó.

## Qué es

**MANTIS es una tarea.** Tiene sub-tareas y cada una resuelve una cosa: editar, auditar, medir, verificar. Este archivo dice **qué se pierde si deja de ser eso.**

A diferencia de un derrotero de proyecto —que enruta tareas a un agente— **este enruta la operación de editar sobre el propio repo.** Es la puerta de la edición, y ninguna se abre sola.

## Muta

**MANTIS es un proceso vivo, y se muta igual que lo que vigila.**

Todo cambio al derrotero, a `./mantenimiento/` o a `./piso/` **declara qué conserva antes de entrar**, y se acuña con `Reemplaza:`. Rige `../Ouroboros/1 Guantelete — primitivo/primitivos/mutar.md`, `Sin herencia`.

**Un MANTIS que no muta es una costumbre con nombre de norma.** Si la herramienta que vigila se defiende por antigüedad, hereda la tendencia que existía para corregir, y desde adentro ya no se ve: **el editor se vuelve el estándar.**

**La mutación de MANTIS se prueba igual que la de cualquier proceso:** el cambio declara `Origen`, `Cambia`, `Conserva` y `Reemplaza`, y otro lee el rastro y reconstruye el cambio sin preguntar al que mutó. Rige `../Ouroboros/1 Guantelete — primitivo/primitivos/mutar.md`, `Ancla`.

```
Mantiene: [qué conserva] | Muta: [qué cambia] | Reemplaza: [nombre anterior o NINGUNA] | Prueba: [corrida|no corrida]
```

## La estructura

```
mantis/                          ← la tarea. Este archivo.
├── Derrotero.md                   la puerta: qué se carga y cuándo
├── deterrente.md                  este archivo: qué se pierde si MANTIS deja de servir
├── mantenimiento/                 editar, auditar, medir, verificar
└── piso/                          lo que corre hoy y emite veredicto
```

**Un nivel, un deterrente.** La tarea tiene el suyo; cada proceso de `./mantenimiento/` declara su `Falsificador`; cada unidad del piso declara qué decide y qué no puede ver. **No se hereda hacia abajo ni se suma hacia arriba.**

**La carta lo lee.** `../AGENTS.md` dice qué hay, qué no se toca y cómo se verifica; **este deterrente dice qué se pierde si MANTIS deja de servir**, y su `Muta:` dice cómo se acuña cuando cambia. **La carta ayuda a leer lo que muta; no muta por él.** Rige `../Ouroboros/formato de ente.md`, `La carta y el derrotero son dos piezas`.

**Un deterrente que no muta ya no es IA: es un archivo.** Lo que mantiene viva una tarea no es que sus archivos cambien de sitio: es que **cada cambio declare qué conserva.** Rige `../Ouroboros/1 Guantelete — primitivo/primitivos/mutar.md`, `Sin herencia`.

## Lo que se pierde si se viola

| Si pasa esto | Se pierde | Y el síntoma es |
|---|---|---|
| se edita sin leer el archivo entero | el rastro | se corrige lo que no se entendió, y el error se muda a la siguiente línea |
| se cambia una ruta y no las que la citan | la cadena | abre el archivo, resuelve a nada, y nadie sabe desde cuándo |
| el cambio se defiende por ser de MANTIS | el estándar | el editor se vuelve la norma y nadie lo nota |
| MANTIS no se muta | la vigencia | la herramienta vigila lo viejo con criterios que ya no aplican |
| el chequeo no corre y se declara pasado | la prueba | un check que no corrió pasa igual |
| el que edita se certifica a sí mismo | la independencia | no hay revisor: hay una firma |

## Lo que MANTIS no es

**No es una persona.** Es el nombre del derrotero, y lo implementa cualquier agente que lo cargue.

**No es un estándar.** Aplica la forma de `../Ouroboros/`; no la define. Si la contradice, gana el estándar y MANTIS se corrige.

**No es una era.** No caduca cuando cambia la herramienta: caduca si deja de decir qué se pierde sin él.

## Prueba

¿Cada edición declara qué conserva? ¿Cada ruta movida arrastra a quien la cita? ¿Toda mutación de MANTIS trae `Reemplaza:` y prueba? ¿Los checks que se declaran corridos corrieron?

**Falsificador:** una edición sin lectura previa; una ruta rota que no se declara; MANTIS defendido por antigüedad; una mutación de MANTIS sin `Reemplaza:`; un check declarado pasado sin haber corrido; el que edita certificándose a sí mismo sin declararlo.

## Transiciones

- Una ruta dejó de resolver → `./mantenimiento/editar/editar.md`, paso 8.
- El conteo cambió → `./mantenimiento/chequear/auditar-configuracion.md`.
- Se muta MANTIS → se declara `Mantiene`, `Muta`, `Reemplaza` y `Prueba` antes de entrar.
- En cualquier otro caso → se entrega y se cierra.
