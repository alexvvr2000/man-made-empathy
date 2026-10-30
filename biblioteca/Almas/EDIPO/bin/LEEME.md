# bin/ — las seis herramientas de EDIPO

**Cuándo se abre:** **cuando EDIPO atiende, y necesita saber qué puede correr.**

## Las seis, y qué hace cada una

| Lo que | Qué hace |
|---|---|
| **`buscar`** | **busca en el catálogo antes de decir que no hay** |
| **`decir-quien`** | **dada una pieza, dice de quién es, y en qué estado está** |
| **`que-falta`** | **qué está pendiente, sin cerrar, o sin verificar** |
| **`no-se`** | **anota la pregunta que no pudo contestar** |
| **`historia`** | **qué hubo: los días, los commits, y de dónde vino cada pieza** |

**Y son cinco, y son seis las cosas que hace:** **recibir es la puerta, y no un comando.**

## Y por qué `historia` no es un extra

> **Sin `historia`, la biblioteca es un índice.**
> **Con `historia`, es memoria: lo que se intentó, y no aguantó.**

## Cómo se corre

```powershell
cd EDIPO
.\bin\historia
.\bin\historia --dia 2026-10-26
.\bin\historia --pieza BUSCAR
.\bin\buscar "cuando se corre el guantelete"
.\bin\decir-quien BUSCAR
.\bin\que-falta
.\bin\no-se "¿cuándo nació la primera idea?"
```

**Y corre sin pedirle nada a nadie: si no hay catálogo o historial, lo dice.**

## Prueba

**¿Corren solos? ¿Dicen lo que hay, lo que falta, y lo que pasó? ¿Lo que no pueden, lo dicen?**

**Falsificador:** una herramienta que declara lo que no hace; una que no corre sin el repo; un `[NO SÉ]` que no aparece.
