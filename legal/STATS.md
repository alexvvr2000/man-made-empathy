# LAS ESTADÍSTICAS — el uso real de DSH, y el costo triangulado

**Qué es:** lo que se corrió en este equipo, del `2026-10-24` al `2026-11-02`, y cuánto cuesta según la tarifa pública del proveedor.
**Qué no es:** no es el conteo de un paper: es el registro de la máquina, y se da tal cual, con la fuente de cada número.

---

## Lo que el motor guardó, medido el `2026-11-02`

**Fuente:** cada mensaje del ente, en los registros de sesión de `DSH`, con su `usage`. **Y esos registros están en [`./TRANSCRIPTS/`](TRANSCRIPTS/), y de ahí salen.**

| Lo que | Cuánto |
|---|---|
| **mensajes del ente** | **9 565** |
| **tokens de entrada** | **26 753 421** |
| **tokens de salida** | **5 007 043** |
| **tokens de caché leída** | **4 293 493 888** |
| **el modelo** | **`deepseek-v4.1-flash`, y no otro: 9 556 de 9 565** |

**Y por sesión, para quien quiera ver de dónde viene el volumen:**

| La sesión | Mensajes | Entrada | Salida |
|---|---|---|---|
| `4a569f10` Libre albedrío | 4 085 | 11 558 369 | 2 254 090 |
| `861cd72a` Recordar discusión | 1 687 | 5 387 033 | 949 661 |
| `0fb4082e` Continuación | 1 524 | 4 722 618 | 738 260 |
| `0da15a04` Alma de niño | 1 656 | 3 341 600 | 793 357 |
| `7c5bbecd` despegarte | 448 | 1 464 971 | 204 802 |
| `9e94ea69` CV | 163 | 265 208 | 66 703 |
| `4031abeb` saludo | 2 | 13 622 | 170 |

## Y la tarifa, triangulada

**Fuente abierta:** `OpenCode`, la página del modelo, abierta el `2026-11-02` ([opencode.ai/data/deepseek/deepseek-v4-1-flash](https://opencode.ai/data/deepseek/deepseek-v4-1-flash)).
**Y lo que dice, textualmente en sus cifras:** `Cost input $0.30 / 1M` · `Cost output $1.20 / 1M` · `缓存比例 97% 输入 token` (el 97 % de los tokens de entrada son caché).

**Y la cuenta, con esas cifras y **sin** inventar una tarifa de caché:**

```plaintext
entrada:  26 753 421 / 1 000 000 * $0.30  =  $ 8.03
salida:    5 007 043 / 1 000 000 * $1.20  =  $ 6.01
                                          ----------
                                          $ 14.04
```

**Y el aviso, que importa más que la cifra:** **la tarifa de los tokens de caché de esa misma página **no** está clara, y por eso no se calcula.** **Y el plan `Go` cuesta `$10` al mes** ([opencode.ai/go](https://opencode.ai/go), abierto el `2026-11-02`), **así que la cifra de `$14.04` es el costo **al precio por token**, y no lo que se pagó de la tarjeta.**

## Lo que estas estadísticas no dicen

```plaintext
- no dicen si la idea es buena
- no dicen si el ente piensa
- y no dicen el costo real del mes: dicen lo que se gastó EN ESTE EQUIPO,
  a la tarifa pública, y sin la parte de caché
```

---

**Prueba:** ¿Los números salen de un registro con huella? ¿La tarifa tiene su enlace y su fecha? ¿Se dice lo que no se midió?

**Falsificador:** una cifra sin registro que la sostenga; una tarifa sin fuente; un costo presentado como lo que se pagó sin serlo.
