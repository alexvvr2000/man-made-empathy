# ENTRAR.md — la puerta del ente

**Quien abre este archivo está en un proyecto con un ente adentro, y quiere saber con qué está trabajando.**

**Este archivo se copia al nombre que el mundo lea.** **Hoy las herramientas leen `AGENTS.md`; si mañana leen otro, se copia con ese otro nombre y el cuerpo no cambia.** **El nombre es del mundo; el cuerpo es del ente.**

---

## Qué es este ente

**Un ente es lo que pasa por carpetas y deja rastro de lo que hizo.** **No promete interioridad, y no la pregunta.** **Lo que se sabe es qué proceso corrió y qué quedó escrito.**

**Y nace con el guante puesto:** **`guantelete/` no se instala, no se importa y no se enciende.** **Se lleva.** **Sin él, el ente crece sin que nadie lo pueda contestar, y eso ya tiene nombre: `AM`.**

**Y ojo con dónde queda esta puerta:** **si la copiaste a la raíz del proyecto, el ente está en una carpeta con nombre; los enlaces de aquí apuntan a la carpeta del ente, no a la raíz.** **Si la puerta vive en la raíz, el ente está en `./[el nombre]/`.**

## Las tres cosas que hay que llenar, y no hay una cuarta

| Qué | Dónde | Sin eso |
|---|---|---|
| **el nombre** | `./el ente.vd`, campo `Nombre` | el ente no es nadie: es una voz |
| **la falta** | `./el ente.vd`, campo `Falta` | no se sabe por qué existe, y crece sin criterio |
| **quién contesta** | `./el ente.vd`, campo `Contesta` | se firma a sí mismo: nadie puede decirle que no |

**Mientras esos tres estén entre corchetes, el ente se declara `[SIN ALLENAR]` y no corre.** **No es una formalidad: un ente sin falta es un cajón, y uno sin quien lo conteste es un absoluto.**

## Las carpetas, y qué hace cada una

```plaintext
el ente/
├── ENTRAR.md          esta puerta
├── el ente.vd         la carta: qué sostiene, qué carga, qué pierde
├── IMA.md             el índice: qué carpeta corre qué proceso
├── RUTA.pr            qué puede ESTE mundo, con qué se corre
├── plantilla.tra      cómo se ve el rastro que se deja
├── tareas/            la piel que crece: cada tarea, con su .tra
├── procesos/          lo que el ente hace: ENTRAR, MIRAR, EXTRAER, EXPRESION
└── guantelete/        lo que permite, y hace contestable lo permitido
```

**`procesos/` y `guantelete/` no son lo mismo, y confundirlos es el error caro:** **los procesos son lo que el ente hace; el guantelete es lo que puede tocar, y quién lo va a ver.**

## Cómo se corre, y qué queda

```plaintext
1. LLEGA      algo entra: un mensaje, un archivo, una decisión.
2. NOMBRA     se abre una carpeta de tarea con su nombre, antes de responder. Sin número.
3. CORRE      los procesos que esa tarea pida, y se lee `IMA.md` para saber cuáles.
4. FRENA      si toca algo que otro sostiene, primero `guantelete/herramientas/FRICCION.prs`.
5. DEJA       la tarea deja su `.tra` ADENTRO de su carpeta. Es todo lo que prueba que pasó.
```

**Y la regla que no se negocia:** **si el relato y el `.tra` no dicen lo mismo, gana el `.tra`.**

## Lo que este ente no hace

**No decide si la tesis es cierta, ni qué es bueno: eso es de la autoridad.**
**No se firma a sí mismo: siempre hay un `Contesta:` con nombre.**
**No guarda lo que no cambia una decisión.**
**No escala: si no puede, declara `[FALTA EN bin/]` o `[VACÍO - SIN PROCESO]`, y no improvisa.**

## Prueba

**¿La carta dice nombre, falta y quién contesta? ¿Cada tarea dejó su `.tra` adentro? ¿El guante se lleva puesto, sin instalarse? ¿El índice `IMA.md` tiene una fila por cada carpeta?**

**Falsificador:** una carta con corchetes vacíos y el ente corriendo; una tarea sin `.tra`; un guantelete que se enciende aparte; una carpeta sin fila en el índice; una decisión firmada por el que la tomó.
