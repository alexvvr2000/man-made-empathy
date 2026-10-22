# Piso de esta instancia

**Unidad:** instancia.
**Aplica a:** ejecutar.
**Tipo:** instancia del estándar. No es estándar: dice **qué se usa hoy aquí.**
**Lector:** quien corre una unidad en este repo.
**Dueño:** la autoridad.
**Estado:** vigente.

## Qué declara

> **Este repo sigue el formato de `../../corpus/piso/formato-de-proceso.md`.**

Y lo sigue **sin excepción**: un archivo nuevo que no cumpla las formas legítimas de allí no entra. Un archivo viejo se acepta como esté — las dos formas de `Prueba` valen, y ninguna se convierte a la otra.

## Lo que corre aquí

El estándar dice **qué** tiene que decidir una unidad. Aquí se declara **con qué se ejecuta**, y eso puede cambiar sin tocar el estándar.

| Unidad | Qué decide | Dónde corre | Cómo se nombra |
|---|---|---|---|
| `inventario` | qué procesos hay, dónde cuelgan, qué campo les falta | `./inventario.ps1` | por lo que decide, no por el lenguaje |

**PowerShell no es un estándar: es la era.** El archivo vive aquí, en la instancia, y no en `../../../corpus/piso/`, porque lo que cambia de era no puede vivir donde vive la forma.

**Si mañana se reescribe en otro lenguaje, el nombre no cambia y el estándar no se toca.** Solo cambia esta tabla.

## Qué hace una unidad con lo que no puede leer

Escribe `indeterminado` **y por qué**. No adivina, y no marca como incompleto lo que no pudo abrir: **incompleto es un veredicto, no una excusa.**

Rige `../../../corpus/piso/README.md`: si el veredicto cambia entre dos corridas del mismo repo, no es piso.

## Prueba

¿La unidad corrió sobre el repo y emitió veredicto? ¿Lo que no pudo leer quedó como `indeterminado` y no como fallo? ¿El formato vigente es el de `corpus/piso/`?

**Falsificador:** un `.md` de la instancia presentado como estándar; un ejecutable dentro de `corpus/piso/`; un `indeterminado` contado como incompleto; un formato propio que contradice al de `corpus/`.
