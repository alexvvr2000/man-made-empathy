# Implementaciones de la era

**Unidad:** era.
**Aplica a:** implementar.
**Tipo:** instancia de la era. No es estándar ni instancia del corpus: es **lo que caduca cuando la era cambia.**
**Lector:** quien va a implementar sobre este repo.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué es esta carpeta

Una **era**. No una instancia: una instancia se corrige, una era **se reemplaza.**

| Nivel | Qué es | Si desaparece |
|---|---|---|
| Estándar (`Ouroboros/`) | la forma | no se sabe cuándo algo está bien |
| Instancia (`Tesis/`, `mantis/`) | qué se hace hoy | el estándar queda sin efecto |
| **Era (`Implementaciones de la era/`)** | **con qué se hace** | **el estándar sigue intacto** |

## La forma de un agente

Todo agente declara cuatro cosas. Sin las cuatro, no es un agente: es un archivo.

```
Agente: [nombre] | Lenguaje: ../Ouroboros/ (el de esta base, sin variantes)
Mutaciones: [qué aplica de S.A.R.A/, o NINGUNA]
Piso: [qué corpus/ cumple, y dónde corre]
Era: [qué tecnología, lenguaje o modelo; y qué lo reemplaza]
```

| Campo | Qué declara | Sin él |
|---|---|---|
| **Lenguaje** | de dónde nacen sus procesos | inventa un lenguaje y deja de ser comparable |
| **Mutaciones** | qué parte de S.A.R.A aplica | se convierte en una copia de S.A.R.A con otro nombre |
| **Piso** | qué estándar cumple, y dónde corre | no se puede comparar con otro agente |
| **Era** | con qué está hecho, y qué lo reemplazaría | se queda cuando la era ya cambió |

## La regla que evita la deriva

> **Un agente puede cambiar todo menos el lenguaje con el que declara el cambio.** Si para funcionar necesita otro Ouroboros, ya no estás implementando: estás creando otro sistema.

Y la consecuencia, que es la que importa a largo plazo:

> **Cuatro generaciones de mutaciones siguen siendo legibles mientras el lenguaje no cambie.** Si cada generación crea su propio lenguaje, la cuarta no la lee nadie — no por diseño, por deriva.

## Lo que hay aquí

| Agente | Qué implementa | Era |
|---|---|---|
| `A.P.R.I.L/` | `corpus/ATLAS/`: intención a forma legible | palabra escrita y voz |
| `Expedicion/` | una familia de agentes que levantan proyectos de código | hoy: lectura y cartografía |

Cada agente declara los cuatro campos.

## Prueba

¿Cada agente declara lenguaje, mutaciones, piso y era? ¿Ninguno trae su propio Ouroboros? ¿Lo que caduca está separado de lo que se corrige?

**Falsificador:** un agente con primitivos propios; un agente sin `Era` declarada; una implementación dentro de una instancia; un agente que es una copia de S.A.R.A con otro nombre.

## Transiciones

- El agente necesita un primitivo que no existe → no es era: es `../Ouroboros/primitivos/`, y se declara.
- El agente aplica parte de S.A.R.A → `../S.A.R.A/README.md`, como mutación.
- El agente no cumple el piso → `../corpus/piso.md`.
- En cualquier otro caso → se entrega y se cierra.
