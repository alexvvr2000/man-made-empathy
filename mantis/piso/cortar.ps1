# cortar.ps1 — corta lo que no es estándar de 2 Ouroboros/
#
# Pregunta única, y es la que decide: si quito esto, ¿la gente sabrá qué hacer con Ouroboros?
#
# Se queda en el estándar:
#   - la cabecera del archivo (Unidad · Aplica a · Tipo · Estado · Variables · Peor · Quién)
#   - el bloque Entra | Falla | Sale | Consume
#   - Cómo se aplica   (cómo se usa)
#   - Ancla            (forma de salida)
#   - Prueba / Falsificador / Modos de falla / Transiciones
#   - tablas que se ejecutan: gemas, procesos, puertas, clases, rutas, estructura
#   - El fantasma (integridad) y La acaloración del nombre (mutación)
#
# Se va a 1 Tesis/desechos del estandar.md:
#   - ## Tesis y Lo que resuelve
#   - ## Lo que ... no hace / no es
#   - ## De dónde nacen / De dónde salen los principios / Lo que absorbió
#   - ## El molde de cera, analogías, Piso y techo, Cerca, Admisión
#   - cualquier caso de la era

param(
  [string]$Root = (Join-Path $PSScriptRoot ".."),
  [string]$Desechos = (Join-Path $PSScriptRoot "..\..\1 Tesis\desechos del estandar.md")
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Secciones que SÍ son estándar: se quedan siempre.
$seQuedan = @(
  'Cómo se aplica','Cómo se crea','Cómo se lee','Cómo se produce','Cómo entra',
  'Ancla','Anclas','Prueba','Pruebas','Falsificador','Modos de falla','Transiciones',
  'Proceso','Las tres clases de retiro','La escala','La distinción','Las tres dimensiones',
  'El fantasma','El nombre muta con la cosa','La regla que impide el absoluto',
  'Las tres piezas de cada paso','El sesgo, en tres archivos',
  'Qué se pierde si se viola','Qué vuelve piso a una herramienta','Se nombra por lo que decide',
  'El piso no decide. El criterio decide.','El tren','Cómo entra una herramienta al piso',
  'Qué hay aquí','Qué hay aquí y qué no','Los tres archivos','La estructura','Las gemas',
  'Las puertas que no se abren solas','Mutación es la puerta','Vacío','Lectura','Reglas',
  'Franjas','Estado','De qué se compone','Cuándo se usa','Compuertas','Lenguaje','Entregable',
  'Admisión','La secuencia mínima','Las variables','La forma de un proceso','La costura entre Ouroboros y S.A.R.A',
  'Lo que todo subproceso declara','La tabla','La tabla: si se va a...','Las cuatro reglas del nivel de arriba',
  'Mutar la serie','Lo que no cambia','1. Origen','2. Cambio declarado','3. Trazabilidad',
  '4. Libertad controlada','5. Retorno','6. Prueba','7. Creación','Acta de creación',
  'Cómo se lee una fila','Registro de formas','Qué es','Los tres niveles','1. Qué es',
  '1.1 La carta y el derrotero son dos piezas','2. Identidad','3. Declaración','4. Rutas',
  '5. Vacío','6. Lectura','7. Invariantes','8. Conformidad','9. Falsificadores',
  'Qué hay','Cómo se verifica','Composición','Encadenar','Piso','Techo','Canal','Modo del mensaje',
  'Retórica','Situación','Participantes','Atención conjunta','Acomodación','Cuerpo','Sesgo declarado',
  'Registros','Índice','Crecimiento'
)

$mudar = @(
  'Tesis','Qué resuelve','Lo que este proceso hace, y lo que no','Lo que impide crecer por crecer',
  'Lo que el guantelete no es','Lo que S.A.R.A no es','Lo que ATLAS no es','Lo que la fricción no hace',
  'Lo que esto no hace','Lo que no hace','Lo que el retiro no hace','Lo que este proceso no hace',
  'Lo que el chequeo no hace','De dónde nacen','De dónde salen los principios','Lo que absorbió',
  'El molde de cera','Fabricar es mutar','Por qué esto mantiene un sistema del AM',
  'Lo que hace útil a un proceso incompleto','Cerca','Cerca del nivel de arriba','Piso y techo',
  'Por qué la industria no lo tiene','El cuerpo','Cómo crece','De aquí a un fantasma en un cascarón',
  'Continuidad','La semilla','Sin propósito','Integridad es que no tenga agujeros',
  'El agujero tiene nombre','La regla que decide si agregar o rehacer','La prueba de que quedó íntegro',
  'La medición a un proceso','Lo que distingue esta vía','El límite','La trampa del buen cómputo',
  'Cómo se sabe si se aprendió',"La condición de cierre de J'ONN",'El campo que faltaba',
  'Lo que previene','Lo que no se declara','La escala de la intervención','P24 — Nivel por defecto',
  'Lo que distingue esto de pensar'
)

$blockRe = [regex]'(?ms)^(#{2,3})\s+(.+?)\s*\r?\n(.*?)(?=^#{1,3}\s|\z)'

$global:desechos = Get-Content $Desechos -Raw -Encoding utf8
$mudadas = 0; $archivos = 0

foreach ($f in (Get-ChildItem $Root -Recurse -Filter *.md)) {
  $rel = $f.FullName.Substring($Root.Length + 1).Replace('\','/')
  $txt = Get-Content $f.FullName -Raw -Encoding utf8
  $nuevo = $txt

  foreach ($m in $blockRe.Matches($txt)) {
    $titulo = $m.Groups[2].Value.Trim()
    if ($seQuedan -contains $titulo) { continue }
    if (-not ($mudar -contains $titulo)) { continue }
    $global:desechos += "`n`n## $rel — $titulo`n`n### $titulo`n`n" + $m.Groups[3].Value.Trim() + "`n"
    $nuevo = $nuevo.Replace($m.Value, '')
    $mudadas++
  }

  if ($nuevo -ne $txt) {
    $nuevo = [regex]::Replace($nuevo, '(?m)^\r?\n[ \t]*\r?\n[ \t]*\r?\n+', "`n`n")
    Set-Content $f.FullName $nuevo -NoNewline -Encoding utf8
    $archivos++
  }
}

[System.IO.File]::WriteAllText((Resolve-Path $Desechos).Path, ($global:desechos.TrimEnd() + "`n"))

Write-Output "CORTAR"
Write-Output "Archivos tocados: $archivos | Secciones mudadas: $mudadas"
Write-Output "Desechos: $Desechos"
