# HISTÓRICAS

**Cada era que existió, ordenada por fecha.** **No hay un número: hay 51 hoy, y mañana las que sean.**

**Y no se cargan: se piden.**

## El índice, por corte de fecha

| Fecha | Eras | Archivos |
|---|---|---|
| **2026-10-02** | `Principios` · `Puntos de inicio` | **11** |
| **2026-10-17** | `prompts iniciales` | **6** |
| **2026-10-18** | `Entornos de desarrollo` · `Principios Agentes` · `dsh` | **39** |
| **2026-10-19** | `A.R.E.S` | **15** |
| **2026-10-20** | `Bases de diseño` · `faber` | **34** |
| **2026-10-21** | `Alineacion de tareas` · `Instrucciones` · `Sistemas Compilables` · `Sondas de comportamiento` · `scripts` | **56** |
| **2026-10-22** | `1 Introduccion` · `1 Tesis` · `2 Ouroboros` · `2 Place holder` · `3 Era` · `Agentes` · `Implementaciones de la era` · `S.A.R.A` · `corpus` | **409** |
| **2026-10-23** | `VIDERE` · `notas` | **15** |
| **2026-10-24** | `(Place holder)` · `(Placeholder)` · `Era` · `Libre albedrio` · `Ouroboros` | **367** |
| **2026-10-25** | `futuro` · `mantis_nuevo` | **72** |
| **2026-10-26** | `sincronizacion de almas` | **80** |
| **2026-10-27** | **las de hoy: lo que hubo mientras se ordenaba** | **1 378** |

**Doce fechas, veintiséis días, 2 482 archivos.**

**Y el índice completo, con cada era y su conteo exacto, está en [`indice.json`](./indice.json).** **Ese archivo lo pone la máquina: se rehace con un comando, y no se escribe a mano.**

## Cómo se pide una era

```powershell
python mantis/bin/historicas.py                        las eras, con su fecha
python mantis/bin/historicas.py --sacar "S.A.R.A"      trae una, aquí
python mantis/bin/historicas.py --desde 2026-10-22     las que se fueron en esa fecha, o después
```

**Y cuando llegue, se lee, y se borra si ya no hace falta.** **Git la sigue teniendo.**

## Y lo que hay que saber antes de abrir una

**Estos archivos son de su era.** **Sus enlaces apuntan a rutas de cuando se escribieron, y muchas ya no existen.**

**No se arreglan: son historia.** **Un archivo histórico que se actualiza deja de decir lo que decía.** **Se leen por lo que dicen, no por lo que enlazan.**

## Y por qué no hay folders aquí

**Porque un folder por era es un límite disfrazado: el que se crea después no tiene folder.** **El índice sí aguanta: una era nueva es una línea, y se rehace solo.**

**Lo único que se guarda en esta carpeta es el índice y esta puerta.**
