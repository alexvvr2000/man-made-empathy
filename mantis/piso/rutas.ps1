# rutas.ps1 — unidad del piso de esta instancia
# Decide: que ruta relativa del repo no resuelve a un archivo real.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# FORMA: no se inventa aqui. Se lee de ../../Ouroboros/piso.md, "Se nombra por lo que decide".
# Uso: pwsh -File mantis/piso/rutas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Zonas que se revisan. La raiz no: sus enlaces son de era.
$zonas = @('Tesis', 'Ouroboros', 'mantis', 'VIDERE')

# |archivo md| enlace (ruta|texto)  ·  `ruta.md`  ·  [texto](ruta)  ·  [texto]: ruta
$patrones = @(
  [regex]'`(\.\.?/[^`\n]+)`',
  [regex]'\]\(([^)\s]+)\)',
  [regex]'(?m)^\s*\[[^\]]+\]:\s*(\S+)'
)

# Una ruta con espacios se escribe entre <>. El destino sin <> no se adivina:
# la unidad lo declara en vez de resolverlo con una heuristica.
# Y se cuentan las rutas que se miran: cero rutas no es un repo sano.
$sinDelimitar = @()
$miradas = 0

$filas = @()
foreach ($z in $zonas) {
  $base = Join-Path $Root $z
  if (-not (Test-Path $base)) { continue }
  foreach ($f in (Get-ChildItem $base -Recurse -Filter *.md)) {
    $rel = $f.FullName.Replace($Root + '\', '/').Replace('\', '/')
    $dir = Split-Path $f.FullName
    $txt = Get-Content $f.FullName -Raw -Encoding utf8
    $visto = @{}
    foreach ($pat in $patrones) {
      foreach ($m in $pat.Matches($txt)) {
        $p = $m.Groups[1].Value
        if ($p -match '^(https?:|mailto:|#)') { continue }
        if ($p -notmatch '\.(md|ps1)$') { continue }
        $miradas++
        if ($visto[$p]) { continue }
        $visto[$p] = $true
        $limpia = ($p -split '#')[0].TrimEnd('/')
        $delimitado = $false
        if ($limpia -match '^<(.*)>$') { $limpia = $Matches[1]; $delimitado = $true }
        $destino = Join-Path $dir $limpia
        if (-not (Test-Path -LiteralPath $destino)) {
          if ($limpia -match '\s' -and -not $delimitado) {
            $sinDelimitar += [pscustomobject]@{ Archivo = $rel; Ruta = $p }
          } else {
            $filas += [pscustomobject]@{ Archivo = $rel; Ruta = $p }
          }
        }
      }
    }
  }
}

Write-Output "RUTAS"
Write-Output "Root: $Root"
Write-Output "Rutas revisadas: $miradas | rutas rotas: $($filas.Count) | rutas con espacios sin <>: $($sinDelimitar.Count)"
Write-Output ""
if ($miradas -eq 0) {
  Write-Output "VEREDICTO: indeterminado"
  Write-Output ""
  Write-Output "MOTIVO: la unidad no encontro ninguna ruta que revisar"
  exit 0
}
Write-Output "VEREDICTO: $(if ($filas.Count -eq 0 -and $sinDelimitar.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($filas.Count -gt 0) {
  Write-Output "ARCHIVO | RUTA"
  foreach ($f in ($filas | Sort-Object Archivo, Ruta)) { Write-Output "$($f.Archivo) | $($f.Ruta)" }
  Write-Output ""
}

if ($sinDelimitar.Count -gt 0) {
  Write-Output "ARCHIVO | RUTA SIN <>"
  foreach ($f in ($sinDelimitar | Sort-Object Archivo, Ruta)) { Write-Output "$($f.Archivo) | $($f.Ruta)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(rutas no juzga si el destino dice lo que debe: eso es integridad)"
