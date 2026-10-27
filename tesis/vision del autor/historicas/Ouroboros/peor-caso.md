# peor-caso

**Variables:** corridas · dispersión · peor resultado · costo del peor caso · reporte
**Peor:** se reporta la media y el desastre queda escondido/ El sistema entra en producción con un promedio excelente y un fallo que nadie vio, porque **el promedio lo tapó**/
**Quién:** quien decide con el reporte/ **Si no ve el peor caso, no puede decidir/**

## Entra | Falla | Sale | Consume

- **Entra:** una serie de corridas del mismo proceso, y el costo de equivocarse en ese uso/
- **Falla:** se reporta el promedio y nada más; se mezclan corridas de costo barato con irreversibles; el peor caso se cuenta una vez y no por costo; se presenta la media como si fuera el resultado típico/
- **Sale:** la media, la dispersión y **el peor caso, separado por costo/**
- **Consume:** quien decide desplegar o confiar/ **Sin el peor caso, el reporte no sirve para eso/**

## Tesis

**La media esconde lo que importa/** Un sistema con un promedio alto puede tener un peor caso equivalente a cero/ Y en el uso donde el costo es irreversible, **el peor caso es el único número que cuenta/**

El caso documentado: un modelo quedó **quinto por media** y con **peor caso 0/00**/ Otro, más chico, **nunca bajó de 0/787**/ El primero gana el reporte y pierde la confianza/

## Proceso

### 1/ Correr más de una vez

**Una sola corrida no tiene peor caso: tiene un resultado/** El peor caso exige repetición, y la repetición exige que la diferencia entre corridas se pueda ver/

```
Corridas: [n] | Mismo proceso: [sí] | Misma entrada: [sí]
```

### 2/ Reportar la dispersión antes que la media

**La media sin dispersión no dice si el sistema es estable o impredecible/** Primero cuánto varía; después dónde cae/

```
Media: [n] | Dispersión: [n] | Estable: [sí|no]
```

**Si `Estable: no`, el peor caso es el número principal** y la media es un dato de color/

### 3/ Separar el peor caso por costo

**El peor caso global no sirve/** Un desastre en lo barato no importa; uno en lo irreversible cambia la decisión/

```
Peor caso global: [n] | Peor caso en caro: [n] | Peor caso en irreversible: [n]
```

**Regla:** se decide con el peor caso **del costo del uso**, no con el global ni con la media/

### 4/ Reportarlo primero

**El peor caso va primero en el reporte, no al final/** Si la decisión se toma con el primer número que se ve, **el primer número tiene que ser el que importa/**

## Prueba

¿Hay más de una corrida? ¿Se reporta la dispersión? ¿El peor caso está separado por costo? ¿El peor caso aparece antes que la media en el reporte?

**Falsificador:** una sola corrida presentada como resultado; media sin dispersión; peor caso global usado para decidir un uso irreversible; el peor caso al final del reporte; corridas de costo distinto mezcladas en el mismo promedio/

## Modos de falla

- **Media como titular/** El promedio encabeza y el desastre queda en una nota al pie/
- **Una corrida/** Se presenta como si tuviera peor caso/
- **Peor caso global/** Se usa para decidir un uso irreversible/
- **Dispersión escondida/** Se sabe que varía y no se dice/
- **Mezcla de costos/** Lo barato y lo irreversible en el mismo promedio/

## Transiciones

- No hay corridas suficientes → se declara `Vacío:` con la fecha, y no se reporta peor caso/
- El costo del uso no está declarado → `//costo-del-error/md`/
- La dispersión viene de dos ejecutores distintos → `////////////1 Tesis/Pruebas/prueba de talento utilizable/md`/
- En cualquier otro caso → se entrega y se cierra/
