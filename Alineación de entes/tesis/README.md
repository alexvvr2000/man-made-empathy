# TESIS — la base, y de aquí salen los ciclos

**Cuándo se abre:** **cuando se va a tocar el repo, y se quiere saber de dónde sale lo que hay.**

**Y esta es la columna de todo:**

> **De las tesis salen los ciclos.**
> **Y los ciclos se implementan solitos: la implementación, la colmena, y los entes.**

```plaintext
tesis/  ->  tesis/ciclos/{ente, colmena}  ->  implementacion/{ente, colmena}
```

**Y sin tesis no hay ciclo. Y sin ciclo no hay implementación: lo que hay suelto es un huérfano, y se marca así.**

---

## Lo que hay aquí

| La carpeta | Qué es | Cuántos |
|---|---|---|
| **[`candados/`](./candados/)** | **las piezas del argumento: cada una sostiene una regla, y no un paso** | **25** |
| **[`ficcion/`](./ficcion/)** | **las fichas: la obra, la escena, y si se verificó. Y son el motor del argumento** | **33, en seis grupos** |
| **[`ciclos/ente/`](./ciclos/ente/)** | **el ciclo que se implementa en cada ente casero** | **vacío, y se llena desde `candados/`** |
| **[`ciclos/colmena/`](./ciclos/colmena/)** | **el ciclo de lo que viven varios** | **vacío, y se llena desde `candados/`** |
| **[`direcciones/`](direcciones/)** | **los procesos que cualquier proyecto puede correr. Y son de la raíz de `tesis/`, porque de ellos también salen ciclos** | **9** |

---

## Y lo que se dice de cada pieza, y es lo que la hace tesis

**No hay un estándar único: lo que queda son direcciones para que sean útiles de verdad.** **Y cada pieza tiene que dejar salir un ciclo, o se dice que no.**

**Y lo que una tesis NO es:** **un estándar que se cumple.** **Una tesis se puede tumbar, y por eso lleva su falsificador.**

---

## Y lo que falta, y se dice

```plaintext
- los dos ciclos: vacíos, y se llenan desde los candados
- las 33 fichas: 30 verificadas, y 3 parciales, y está por ficha en `candados/19`
- y las direcciones: los nueve .prs, y cada uno tiene que decir de qué pieza sale
```

**Y lo que no se hace:** **inventar una tesis para llenar un ciclo.** **Si falta, se dice `[SIN TESIS QUE LO PRODUZCA]`.**

---

**Prueba:** **¿Se sabe qué hay en `tesis/` en una lectura? ¿Cada carpeta dice si produce ciclo? ¿Lo que falta está dicho?**

**Falsificador:** **un ciclo llenado sin tesis; una tesis que no dice qué produce; una carpeta sin decir qué es.**
