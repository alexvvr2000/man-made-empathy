# inventario.ps1 — unidad del piso de esta instancia
# Decide: que procesos hay, donde cuelgan, y que campo les falta.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# FORMATO: no se inventa aqui. Se lee de ../../1 Tesis/formato.md
# Si el estandar cambia, esta unidad no se toca: se vuelve a correr.
#
# Uso: pwsh -File mantis/piso/inventario.ps1 [-Root <ruta>] [-Formato <ruta>]

param(
  [string]$Root   = (Join-Path $PSScriptRoot "..\.."),
  [string]$Formato = (Join-Path $PSScriptRoot "..\..\1 Tesis\formato.md")
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Formato = (Resolve-Path $Formato).Path

# ---------------------------------------------------------------
# 1. Leer el estandar. Si no se puede leer, se declara y no se adivina.
# ---------------------------------------------------------------
if (-not (Test-Path $Formato)) {
  Write-Output "INVENTARIO"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no se encontro el formato en $Formato"
  Write-Output "Se declara indeterminado: la unidad no completa el estandar por su cuenta."
  exit 0
}

$estandar = Get-Content $Formato -Raw -Encoding utf8

# La tabla de campos del estandar: | `Campo` | ... | `forma` |
# Se extraen los nombres de campo de la primera columna de la seccion "La forma del proceso":
# Variables, Peor, Quien, y el bloque Entra | Falla | Sale | Consume.
$seccion = ($estandar -split '(?m)^## ' | Where-Object { $_ -match '^La forma del proceso' -or $_ -match '^Los campos' })
if (-not $seccion) {
  Write-Output "INVENTARIO"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: el formato no tiene la seccion de campos"
  exit 0
}

# 'Campo' es el encabezado de la tabla, no un campo: se excluye.
$nombres = @()
foreach ($linea in ($seccion -split "`n")) {
  $m = [regex]::Match($linea, '^\|\s*`?([A-Za-zÁÉÍÓÚáéíóúñÑ]+)`?\s*\|')
  if ($m.Success -and $m.Groups[1].Value -ine 'Campo') { $nombres += $m.Groups[1].Value }
}
if ($nombres.Count -eq 0) {
  Write-Output "INVENTARIO"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: la seccion 'La forma del proceso' no declara campos"
  exit 0
}

# ---------------------------------------------------------------
# 2. Las formas legitimas, transcritas del estandar.
#    El estandar acepta linea (**Campo:**) o seccion (## Campo).
#    Se generan desde el nombre, no se escriben a mano por campo.
# ---------------------------------------------------------------
function Get-Patron($campo) {
  $c = [regex]::Escape($campo)
  $variantes = @(
    "^\*\*$c( de la jerga)?:\*\*"
    "^\s*-\s*\*\*$c( de la jerga)?:\*\*"
    "^\*\*$c si:\*\*"
    "^\s*-\s*\*\*$c si:\*\*"
    "^$c( si)?:"
    "^##+\s+$c"
  )
  return '(?m)(' + ($variantes -join '|') + ')'
}

$campos = [ordered]@{}
foreach ($n in $nombres) { $campos[$n] = Get-Patron $n }

# ---------------------------------------------------------------
# 3. Lo que NO es proceso, segun el estandar.
# ---------------------------------------------------------------
function Test-EsProceso($nombre) {
  if ($nombre -ieq 'README.md') { return $false }
  if ($nombre -match '(?i)indice') { return $false }
  if ($nombre -match '(?i)formato') { return $false }
  if ($nombre -match '(?i)deterrente') { return $false }
  return $true
}

# ---------------------------------------------------------------
# 4. Donde se busca. 1 Tesis/ NO se inventaria: contiene estandares.
# ---------------------------------------------------------------
$carpetas = @('2 Ouroboros\2 S.A.R.A','2 Ouroboros\1 Guantelete','2 Ouroboros\3 ATLAS')

$filas = @()
$nCompleto = 0; $nIncompleto = 0; $nIndeterminado = 0; $nExcluido = 0

function Medir-Archivo($archivo, $sub) {
  $rel = $archivo.FullName.Replace($Root + '\','').Replace('\','/')
  try { $txt = Get-Content $archivo.FullName -Raw -Encoding utf8 }
  catch {
    $script:filas += [pscustomobject]@{ Proceso=$rel; Sub=$sub; Veredicto='indeterminado'; Falta='no se pudo leer' }
    $script:nIndeterminado++; return
  }
  $falta = @()
  foreach ($k in $campos.Keys) { if ($txt -notmatch $campos[$k]) { $falta += $k } }
  if ($falta.Count -eq 0) {
    $script:filas += [pscustomobject]@{ Proceso=$rel; Sub=$sub; Veredicto='completo'; Falta='-' }
    $script:nCompleto++
  } else {
    $script:filas += [pscustomobject]@{ Proceso=$rel; Sub=$sub; Veredicto='incompleto'; Falta=($falta -join ',') }
    $script:nIncompleto++
  }
}

foreach ($c in $carpetas) {
  $base = Join-Path $Root $c
  if (-not (Test-Path $base)) { continue }
  foreach ($a in (Get-ChildItem $base -Filter *.md -File -ErrorAction SilentlyContinue)) {
    if (Test-EsProceso $a.Name) { Medir-Archivo $a '(raiz)' } else { $nExcluido++ }
  }
  foreach ($s in (Get-ChildItem $base -Directory -ErrorAction SilentlyContinue)) {
    foreach ($a in (Get-ChildItem $s.FullName -Filter *.md -File -Recurse -ErrorAction SilentlyContinue)) {
      if (Test-EsProceso $a.Name) { Medir-Archivo $a $s.Name } else { $nExcluido++ }
    }
  }
}

# ---------------------------------------------------------------
# 5. Salida: veredicto, no datos crudos.
# ---------------------------------------------------------------
Write-Output "INVENTARIO"
Write-Output "Root: $Root"
Write-Output "Formato: $Formato"
Write-Output "Campos leidos del estandar: $($nombres -join ', ')"
Write-Output "Procesos: $($filas.Count) | completos: $nCompleto | incompletos: $nIncompleto | indeterminados: $nIndeterminado | excluidos: $nExcluido"
Write-Output ""
Write-Output "VEREDICTO: $(if ($nIncompleto -eq 0 -and $nIndeterminado -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($nIncompleto -gt 0 -or $nIndeterminado -gt 0) {
  Write-Output "PROCESO | SUB-TAREA | VEREDICTO | FALTA"
  foreach ($f in ($filas | Where-Object { $_.Veredicto -ne 'completo' } | Sort-Object Proceso)) {
    Write-Output "$($f.Proceso) | $($f.Sub) | $($f.Veredicto) | $($f.Falta)"
  }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(inventario no juzga si el proceso sirve: eso es integridad)"
