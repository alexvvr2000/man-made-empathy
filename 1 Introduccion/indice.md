# Indice

**Unidad:** nivel.
**Aplica a:** ubicar.
**Tipo:** registro generado. No se edita a mano: se regenera.
**Generado por:** `../mantis/piso/indice.ps1`.
**Fecha:** 2026-10-22.

## Que es

Este archivo existe porque **todo muta y nadie se acuerda donde quedo cada cosa.** Es el indice del repo: que hay, en que zona, y que clase es cada archivo.

**Un indice escrito a mano se desactualiza en la siguiente mutacion.** Por eso lo genera el piso: si cambio algo y el indice no cambio, el indice miente.

## Las zonas

| Zona | Rol | Que es |
|---|---|---|
| `corpus/` | estandar | el estandar: la forma |
| `Ouroboros/` | instancia | instancia: el lenguaje de procesos |
| `S.A.R.A/` | instancia | instancia: las abstracciones |
| `mantis/` | instancia | instancia: la operacion |
| `Agentes/` | era | la era |

## Las clases

| Clase | Que es |
|---|---|
| `proceso` | se ejecuta: declara entrada, falla, salida y consumidor |
| `estandar` | dice como tiene que ser algo |
| `deterrente` | dice que pasa si el nivel se viola |
| `formato` | dice que forma tiene lo que un ejecutor lee |
| `puerta` | `README`: abre una zona o una sub-tarea |
| `indice` | este archivo y sus semejantes |

## El arbol

### corpus/

| Carpeta | Archivo | Clase | Lineas |
|---|---|---|---|
| `corpus` | `Conceptos.md` | estandar | 106 |
| `corpus` | `Derrotero y Carta.md` | estandar | 125 |
| `corpus` | `esquema-de-fila.md` | estandar | 67 |
| `corpus` | `formato.md` | formato | 160 |
| `corpus` | `indice.md` | indice | 164 |
| `corpus` | `integridad.md` | estandar | 181 |
| `corpus` | `piso.md` | estandar | 88 |
| `corpus` | `problemas-abiertos.md` | estandar | 95 |
| `corpus` | `README.md` | puerta | 104 |
| `corpus/ATLAS` | `indice de formas.md` | indice | 65 |
| `corpus/ATLAS` | `Proceso ATLAS.md` | estandar | 344 |
| `corpus/ATLAS` | `README.md` | puerta | 50 |

### Ouroboros/

| Carpeta | Archivo | Clase | Lineas |
|---|---|---|---|
| `Ouroboros` | `deterrente.md` | deterrente | 83 |
| `Ouroboros` | `README.md` | puerta | 74 |
| `Ouroboros/mutaciones` | `friccion.md` | proceso | 136 |
| `Ouroboros/mutaciones` | `README.md` | puerta | 27 |
| `Ouroboros/mutaciones` | `sesgo-declarado.md` | proceso | 137 |
| `Ouroboros/primitivos` | `aplicar.md` | proceso | 87 |
| `Ouroboros/primitivos` | `claridad.md` | proceso | 226 |
| `Ouroboros/primitivos` | `ingenieria-inversa.md` | proceso | 76 |
| `Ouroboros/primitivos` | `manipulacion.md` | proceso | 188 |
| `Ouroboros/primitivos` | `mutacion.md` | proceso | 155 |
| `Ouroboros/primitivos` | `README.md` | puerta | 21 |

### mantis/

| Carpeta | Archivo | Clase | Lineas |
|---|---|---|---|
| `mantis` | `Derrotero.md` | proceso | 48 |
| `mantis/mantenimiento` | `auditar-configuracion.md` | proceso | 81 |
| `mantis/mantenimiento` | `editar.md` | proceso | 150 |
| `mantis/mantenimiento` | `medir-acero.md` | proceso | 59 |
| `mantis/mantenimiento` | `verificar-esquema.md` | proceso | 45 |

### Agentes/

| Carpeta | Archivo | Clase | Lineas |
|---|---|---|---|
| `Agentes` | `README.md` | puerta | 68 |
| `Agentes/A.P.R.I.L` | `README.md` | puerta | 73 |
| `Agentes/Expedicion` | `README.md` | puerta | 46 |

## Totales

`Archivos: 31 | procesos: 12 | estandares: 7`

## Prueba

¿Cada archivo del repo aparece? ¿Su clase es la que dice su forma? ¿El indice se regenero despues del ultimo cambio?

**Falsificador:** un archivo sin clase; un indice que no se regenera tras una mutacion; una zona sin rol.
