# trazabilidad.ps1 — unidad del piso de esta instancia
# Decide: si lo que Tesis/referencias nombra tiene su archivo, y si cada archivo tiene su forma.
#
# Que no es: no decide si una referencia vale, ni si provoca algo. Eso lo decide quien lee.
# No se aplica a: los momentos, que son prosa y no llevan forma fija; y los archivos que
#                 empiezan con "_", que son plantilla, no referencia.
# No usa modelo. Corre igual en cualquier ejecutor.
#
# FORMA: no se inventa aqui. Se lee de ../../Ouroboros/piso.md, "Se nombra por lo que decide".
# El porque: una referencia que se discute y no se guarda se pierde con el contexto, y la que
# mas respalda un punto es la que mas se olvida. Esta unidad convierte eso en un numero.
#
# Uso: pwsh -File mantis/piso/trazabilidad.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

$dir = Join-Path $Root 'Tesis\referencias'
$index = Join-Path $dir 'index.md'

if (-not (Test-Path -LiteralPath $index)) {
  Write-Output "TRAZABILIDAD"
  Write-Output "Root: $Root"
  Write-Output ""
  Write-Output "VEREDICTO: indeterminado"
  Write-Output ""
  Write-Output "MOTIVO: no existe Tesis/referencias/index.md"
  exit 0
}

# Los campos que toda entrada de referencia declara. Sin los cuatro no es una entrada: es un titulo.
# El valor tiene que tener contenido despues del campo. Se acepta cursiva o negrita al inicio del
# valor —una obra en italica es normal—, pero no un campo que termina justo despues de los dos puntos:
# un campo sin valor es un campo que falta.
$campos = @(
  @{ Nombre = 'De quién';           Regex = '(?m)^\*\*De quién:\*\*[ \t]+\S' },
  @{ Nombre = 'Qué dice';           Regex = '(?m)^\*\*Qué dice:\*\*[ \t]+\S' },
  @{ Nombre = 'Qué pieza sostiene'; Regex = '(?m)^\*\*Qué pieza sostiene:\*\*[ \t]+\S' },
  @{ Nombre = 'Qué la contestaría'; Regex = '(?m)^\*\*Qué la contestaría:\*\*[ \t]+\S' }
)

$txtIndex = Get-Content -LiteralPath $index -Raw -Encoding utf8

# Una referencia esta declarada en el indice si aparece como negrita al principio de una fila de tabla.
# Solo las filas: la prosa habla de las referencias con negrita, y no es una declaracion.
$nombradas = @()
$visto = @{}
foreach ($m in [regex]::Matches($txtIndex, '(?m)^\|\s*\*\*([^*]+)\*\*')) {
  $n = $m.Groups[1].Value.Trim()
  if ($n -match '^(Referencia|Proceso)$') { continue }
  if (-not $visto[$n]) { $visto[$n] = $true; $nombradas += $n }
}

$archivos = @(Get-ChildItem -LiteralPath $dir -File -Filter *.md | Where-Object { $_.Name -notlike '_*' -and $_.Name -ne 'README.md' -and $_.Name -ne 'index.md' })

$sinArchivo = @()
$sinForma = @()
$miradas = 0

# 1. Cada nombre del indice: tiene archivo, o esta declarado [SIN ENTRADA].
foreach ($n in $nombradas) {
  $miradas++
  $base = ($n -replace '[^A-Za-z0-9 ]', '') -replace '\s+', '-' | ForEach-Object { $_.ToLower() }
  $candidatos = @($archivos | Where-Object {
    $ti = (Get-Content -LiteralPath $_.FullName -Raw -Encoding utf8) -split "`r?`n" | Select-Object -First 3 | Out-String
    $ti -match [regex]::Escape($n)
  })
  if ($candidatos.Count -eq 0) {
    # Declarado como pendiente solo si [SIN ENTRADA] esta en LA MISMA LINEA que el nombre.
    # Buscarlo en cualquier parte del archivo lo da por declarado con el [SIN ENTRADA] de otra fila,
    # y entonces el chequeo nunca falla: se corre por cumplir y no detecta nada.
    $declarado = $false
    foreach ($linea in ($txtIndex -split "`r?`n")) {
      if ($linea -match [regex]::Escape($n) -and $linea -match '\[SIN ENTRADA\]') { $declarado = $true }
    }
    if (-not $declarado) {
      $sinArchivo += [pscustomobject]@{ Referencia = $n; Falta = 'sin archivo y sin [SIN ENTRADA]' }
    }
  }
}

# 2. Cada archivo de referencia: tiene los cuatro campos.
foreach ($f in $archivos) {
  $t = Get-Content -LiteralPath $f.FullName -Raw -Encoding utf8
  foreach ($c in $campos) {
    if ($t -notmatch $c.Regex) {
      $sinForma += [pscustomobject]@{ Archivo = $f.Name; Falta = $c.Nombre }
    }
  }
}

Write-Output "TRAZABILIDAD"
Write-Output "Root: $Root"
Write-Output "Referencias nombradas: $miradas | archivos de referencia: $($archivos.Count) | sin archivo: $($sinArchivo.Count) | sin campo: $($sinForma.Count)"
Write-Output ""

if ($miradas -eq 0) {
  Write-Output "VEREDICTO: indeterminado"
  Write-Output ""
  Write-Output "MOTIVO: la unidad no encontro ninguna referencia nombrada en el indice"
  exit 0
}

Write-Output "VEREDICTO: $(if ($sinArchivo.Count -eq 0 -and $sinForma.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($sinArchivo.Count -gt 0) {
  Write-Output "REFERENCIA | FALTA"
  foreach ($s in ($sinArchivo | Sort-Object Referencia)) { Write-Output "$($s.Referencia) | $($s.Falta)" }
  Write-Output ""
}

if ($sinForma.Count -gt 0) {
  Write-Output "ARCHIVO | CAMPO FALTANTE"
  foreach ($s in ($sinForma | Sort-Object Archivo, Falta)) { Write-Output "$($s.Archivo) | $($s.Falta)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(trazabilidad no juzga si una referencia vale o provoca algo: eso lo decide quien lee)"
