# EMPEZAR — cómo se arma un alma de script, hoy

**Esta es la única puerta.** Los demás archivos dicen qué hay. **Este dice en qué orden leerlo, para que de aquí salga un agente que corre.**

**Sesgo:** se lee desde el que llega sin nada hecho, y quiere uno funcionando hoy.
**Límite:** no explica el estándar: lo enruta. **Si quieres entender, lee lo que carga; si quieres hacer, sigue los pasos.**
**Firma:** humano:autoridad · máquina:quien lo siga.

---

## Las siete piezas, en el único orden que funciona

```
0. el mundo       →  ./RUTA.pr  ·  ./RUTA.md                 (qué hay, y qué no, en ESTE mundo)
1. el alma        →  ../base/alma en blanco/el alma.vd
2. sus folders    →  Entes/alma de la pregunta/ENTRAR.prs · MIRAR.prs · EXTRAER.prs
3. su plantilla   →  Entes/alma de la pregunta/plantilla.tra  (lo que deja cada folder)
4. el estándar    →  sincronización de almas/formacion/FORMATO.md · LENGUAJE.md
5. el guantelete  →  Entes/guantelete/GUANTELETE.vd · herramientas/
6. el piso        →  sincronización de almas/friccion/PISO.md
```

**Si lees 4, 5 y 6 antes de 1, no entiendes nada: son las reglas de algo que todavía no viste correr.** **Si lees 0 a 3 primero, ya tienes un alma; el resto te dice por qué está bien hecha.**

**Y el cero no es el alma: es el mundo donde el alma se para.** **Hay muchos `RUTA`, uno por mundo, y el alma es la misma en todos.** **Esa es la regla que hace que un alma se pueda mudar sin reescribirse.** Rige [`./RUTA.md`](./RUTA.md).

---

## Los seis pasos, con lo que sale de cada uno

| Paso | Haces | Sale |
|---|---|---|
| **1. LA FRASE** | dices qué tiene que hacer el alma, en una frase | el acto: qué entra y qué sale |
| **2. LOS FOLDERS** | creas los folders que ese acto necesita, uno por paso | N carpetas vacías, con su nombre |
| **3. LOS PROCESOS** | en cada folder, un `.prs` con `Entra \| Falla \| Sale \| Consume` | un folder con su proceso |
| **4. EL ÍNDICE** | escribes qué folder corre qué proceso, en `IMA.md` | el enrutamiento: ningún folder sin proceso |
| **5. LA TAREA SE ABRE** | copias `plantilla.tra`, la llenas, y la dejas en cada folder | un `.tra` por paso: la prueba de que pasó |
| **6. EL PISO** | declaras qué usaste y qué no había | el costo, y lo que falta |

**Cada paso lee la salida del anterior.** **Si un paso no deja archivo, el siguiente no puede empezar: no es pereza, es el formato.**

---

## Lo que un alma necesita, y nada más

```
el alma          qué pasa por los folders
el folder        dónde se para, y qué deja
el proceso       qué corre en cada folder
el índice        qué proceso le toca a cada folder
la .tra          la prueba de que pasó
```

**Y algo que casi nadie escribe, y es lo que hace que sirva:** **el alma no sabe qué procesos va a encontrar.** **Si tu alma necesita saberlo, no es un alma: es un programa con nombre bonito.**

---

## Cuando ya corre

| Si quieres… | Ve a |
|---|---|
| **que dos almas se afinen sin volverse una** | `sincronización de almas/relacion/RESONANCIA.md` |
| **medir si el ente sirve, y no solo si corre** | `sincronización de almas/relacion/TALENTO.md` |
| **que otro siga sin ti** | `sincronización de almas/salida/CONTEXTO.md` |
| **quitarte una regla, dejando rastro** | `sincronización de almas/friccion/FIRMAR.prs` |
| **tocar algo que otro sostiene** | `Entes/guantelete/GUANTELETE.vd` |
| **que otro no tenga que preguntarte nada** | `sincronización de almas/salida/la fila verbalizada.md` |

---

## Un ejemplo que se puede abrir

**La prueba de que esto se entiende sin el autor no es este texto: es el ejemplo.** **`Entes/alma de la pregunta/` es un alma completa, con sus procesos, su índice y su plantilla.** **Ábrela y cópiala entera en otra carpeta: ya tienes un alma que corre.**

---

## Prueba

**¿Alguien que nunca vio FARO puede, siguiendo las siete piezas en orden, producir un alma que corre? ¿Cada paso deja un archivo que el siguiente lee? ¿El ejemplo se puede copiar y correr sin el autor?**

**Falsificador:** un orden que pone las reglas antes del ejemplo; un paso que no deja archivo; un alma que necesita saber qué folders va a encontrar; un ejemplo que no se puede copiar.

## Transiciones

- Llegas sin nada → **paso 1.**
- Ya tienes el alma y quieres los procesos → **paso 3.**
- Ya corre y quieres afinarlo con otro → **`RESONANCIA`.**
- Ya corre y quieres saber si sirve → **`TALENTO`.**
- No sabes si tocar algo de otro → **`GUANTELETE`.**
