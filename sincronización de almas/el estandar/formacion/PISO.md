# el piso — qué declara un mundo, y cómo se comprueba

**Nombre.** EL PISO. **El nombre dice el acto:** **un mundo no dice lo que puede: dice lo que puede, y se le mide antes de creerle.**
**Reemplaza:** la prosa de `RUTA.md`. **Conserva lo que decía, y le quita lo que no se puede comprobar.**

**Unidad:** pieza.
**Aplica a:** declarar y comprobar.
**Tipo:** se ejecuta. **Una capacidad no declarada no existe; una declarada sin prueba tampoco.**
**Lector:** quien llega a un mundo nuevo, y el ente antes de tocar nada.
**Dueño:** humano:autoridad.
**Estado:** vigente.

**Sesgo:** se lee desde lo que el mundo **puede**, no desde lo que el mundo **tiene**.
**Límite:** **no dice cómo se hace.** **Dice qué se puede, y con qué se comprueba.** **El cómo es del mundo.**
**Firma:** humano:autoridad · máquina:quien lo mida.

**Peor:** el piso declara una capacidad que no tiene, **y el ente produce resultados que nadie puede reproducir porque nunca existió con qué.**
**Quién:** quien reciba el resultado y no pueda volver a correrlo.

---

## La regla, y son seis

**Un mundo declara sus capacidades. No las describe: las enumera, y cada una lleva su prueba.**

| # | Capacidad | Qué significa, sin decir cómo | Prueba mínima |
|---|---|---|---|
| **1** | **`leer`** | traer el contenido de algo que ya existía | leer el propio `RUTA.md`, y que coincida con lo que se declaró |
| **2** | **`escribir`** | dejar algo que otro pueda leer después | escribir un archivo, y volver a leerlo igual |
| **3** | **`ejecutar`** | que algo corra, y que devuelva si salió bien | correr un paso que diga `ok`, y recibir `ok` |
| **4** | **`medir`** | contar el tiempo, lo que cuesta, o cuántas veces | medir la prueba de arriba, y que dé un número |
| **5** | **`fuera`** | traer algo que no estaba en el mundo | **puede faltar.** Si no hay, se declara `no`, y el ente no lo usa |
| **6** | **`entre_turnos`** | que algo siga corriendo cuando el ente no lo está mirando | **puede faltar.** Si no hay, se declara `no`, y nada se promete para después |

**Y son seis porque seis alcanzan para todo lo que se ha probado aquí.** **Un mundo que necesite una séptima la pide, y se justifica: una capacidad no entra porque el mundo la tenga, entra porque un corte no se cumple sin ella.**

## Lo que un mundo NO declara

**No declara su lenguaje, su marca, su sistema, ni su dominio.** **Python no es una capacidad: es con qué se cumple `ejecutar`.** **HTTP no es una capacidad: es cómo se cumple `fuera`.** **Un motor no es una capacidad: es cómo se cumple `ejecutar`, con consecuencias.**

**Y esa es la prueba del piso:** **si la capacidad nombra cómo, no es capacidad: es una pieza del mundo, y va en `bin/`.**

## La forma

```plaintext
mundo:            [cuál es, y qué lo distingue de otro]
capacidades:      leer · escribir · ejecutar · medir · fuera · entre_turnos
con:              [con qué se cumple cada una. Sí puede nombrar lenguaje: eso es del mundo]
prueba:           [la prueba de cada una, y cómo se comprueba]
no_puede:         [lo que falta, y qué se pierde por eso]
se_gasta:         [qué cambio del mundo lo deja viejo]
```

**`no_puede` no es una derrota: es la mitad del piso.** **Un mundo que no puede `entre_turnos` y lo dice no está roto: está declarado, y el ente no promete nada para después.**

---

## La regla del nacimiento: no nace nada con el piso a medias

**Y esto es lo que impide que una opinión se vuelva un ente.**

> **Un ente no nace hasta que el piso de su mundo está listo.** **Y el piso no está listo porque se escribió: está listo cuando se midió, y salió completo.**

**"Completo" tiene dos condiciones, y las dos se corren, no se opinan:**

| Condición | Qué significa |
|---|---|
| **todo lo que declara, lo puede** | cada capacidad declarada pasó su prueba |
| **todo lo que no puede, lo declaró** | `no_puede` no está vacío si le falta algo, y **nombra qué** |

**Y lo que no declara, no existe.** **Si el ente pide una capacidad que el piso no declara, es `[FALTA EN EL PISO]`, y no corre.** **No se supone: se dice.**

**Por qué esto importa, y es la misma razón de `NEGARSE` en [`EJECUTOR`](./EJECUTOR.md):** **un piso a medias no falla cuando algo sale mal: falla cuando algo sale bien, y entonces nadie lo puede volver a producir porque el mundo no tenía con qué.**

**Un mundo con el piso a medias admite opiniones. No admite entes.**

## La prueba del nacimiento

```
1. se llena el piso
2. se corre su prueba, capacidad por capacidad
3. lo que falló se corrige, o se declara no_puede
4. solo entonces se llena la carta del ente: Nombre, Falta, Contesta
5. el primer corte que se corre es el que nace
```

**Prohibido el paso 4 sin el 3.** **Un ente con los tres corchetes llenos y el piso a medias es un ente con opinión: parece que corre, y no se puede reproducir.**

## La prueba

**¿Cada capacidad declarada tiene su prueba, y se corrió? ¿Alguna capacidad nombra cómo en vez de qué? ¿Lo que falta está declarado, y qué se pierde? ¿Se dice cuándo el mundo se gasta? ¿Se midió el piso ANTES de llenar la carta del ente?**

**Falsificador:** una capacidad sin prueba, o con prueba que no se corrió; una capacidad que nombra su herramienta en vez de su acto; un `no_puede` vacío; un mundo que declara `entre_turnos` y no lo tiene; un piso escrito para un dominio y no para lo que corre; **un ente que nace con el piso sin medir.**

## Transiciones

- Se llega a un mundo nuevo → **se lee su piso, y se corre la prueba de cada capacidad antes de usarla.**
- Una capacidad se declara y falla su prueba → **no tiene la capacidad: se declara `no_puede`, y lo que dependía de ella no corre.**
- El mundo cambia → **se vuelve a medir. Un piso que no se mide es una promesa.**
- Se quiere una capacidad nueva → **se nombra la falta que la pide, y se refuta: ¿un corte se cumple sin ella? Si sí, no entra.**
- Se quiere que nazca un ente → **primero el piso listo; después la carta.** **Al revés no se nace: se opina.**

