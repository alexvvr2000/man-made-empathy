# EL RASTRO — cómo se prueba que esto es de Alejandro, y cuándo

**Qué es:** lo que un tercero necesita para verificar la historia del repositorio. **No pide confianza: pide una corrida.**

---

## Lo que se puede probar, y con qué

| Lo que se prueba | Y con qué |
|---|---|
| **que los commits son de Alejandro** | **firma `OpenPGP` dentro del commit, con la llave pública de [`./llave-publica.asc`](llave-publica.asc)** |
| **que el contenido de un commit no se tocó** | **la firma cubre el árbol y el mensaje: si cambia un byte, no verifica** |
| **que existió antes de esta fecha** | **el sello de tiempo lo pondría un tercero (`Zenodo`); la fecha del commit la pone la máquina que lo hizo, y no se toma como fecha absoluta** |

## Cómo se verifica, y son dos comandos

```plaintext
gpg --import legal/llave-publica.asc
git log --format="%h %G? %GK" --reverse main
```

**Y el resultado que hay que buscar es `G`.** **Los estados posibles, y qué significa cada uno:**

| La letra | Qué es |
|---|---|
| **`G`** | **firma buena, y verificada contra la llave pública** |
| **`U`** | **firma válida, y la llave no está declarada de confianza en esa máquina** |
| **`E`** | **la firma existe, pero no hay llave pública importada en esa máquina** |
| **`N`** | **no hay firma** |

**Y `E` o `U` no son fraude: son ausencia de llave, o de confianza.**

## Lo que hay hoy, medido el `2026-11-02`

```plaintext
commits en main:        711
con firma válida:       52
sin firma:              659
llave que firma:        5EE02079A7F9061386033BA5A49A5FB4B1ACB80B
```

**Y lo que no se afirma:** **que los commits sin firma sean de otra persona.** **Son commits del mismo historial, sin firma.** **Lo que se afirma es sólo lo que la firma prueba.**

---

**Prueba:** ¿importa la pública, y sale `G`? ¿Se distingue la firma buena de la que no se pudo verificar, y del commit sin firma?

**Falsificador:** un commit presentado como firmado cuando da `N`; una fecha de commit presentada como fecha de existencia absoluta; una verificación que no se puede rehacer con la llave de `legal/`.
