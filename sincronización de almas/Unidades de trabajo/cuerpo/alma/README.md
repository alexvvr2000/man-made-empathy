# ALMA — el socket: aquí se monta un alma

**Clase:** carta de carpeta. **Estado:** ocupada por el alma que corre hoy, o vacía.

**Sesgo:** se lee desde el que va a cambiar de alma sin cambiar de cuerpo.
**Límite:** **no guarda el alma.** **Es el lugar donde se pone: lo que está montado, y desde cuándo.**

---

## Qué es

**El socket.** **Aquí se monta un `../alma/`, o una `../colmena/`.** **Los dos son lo mismo en dos tamaños: los dos tienen memoria y criterio.**

**Y por eso el alma se puede cambiar sin tocar el cuerpo:** **se saca una, se pone otra, y el cuerpo sigue sabiendo qué puede.**

---

## La montura

**Y no se llena a mano: la deja `../conectar.prs`.**

```plaintext
Alma:        [cuál está montada]
Desde:       [cuándo]
Piso:        [qué capacidades de este cuerpo se probaron con ella]
En proceso:  [qué .prs de ../procesos/ la enlazan]
```

**Y cuando no hay nada montado, se dice:**

```plaintext
Alma: ninguna | Desde: — | Piso: [lo que este cuerpo declara igual] | En proceso: ninguno
```

**Un socket vacío no es un cuerpo roto: es un cuerpo que está esperando, y lo dice.**

---

## Lo que NO va aquí

**El alma.** **Se enlaza, no se copia.** **Una copia se desincroniza en la siguiente mutación.**
**El criterio.** **Es del alma, y se va con ella.**
**Los procesos.** **Los del alma viajan con ella; los que enlazan `bin/` viven en `../procesos/`, y los pone el alma que llega.**

---

## Prueba

**¿Dice qué alma está montada, y desde cuándo? ¿Se puede cambiar sin tocar el cuerpo? ¿Lo que se montó trae su propio registro? ¿El socket vacío se declara como vacío, y no como avería?**

**Falsificador:** un alma copiada dentro del socket; una montura sin fecha; un socket que dice tener alma y no la tiene; un criterio guardado en el cuerpo.
