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
$zonas = @('Tesis', 'Ouroboros', 'mantis')

# |archivo md| enlace (ruta|texto)  ·  ``ruta.md``  ·  [texto](ruta)
$patrones = @(
  [regex]'`(\.\.?/[^`\n]+)`',
  [regex]'\]\(([^)\s]+)\)'
)

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
        if ($visto[$p]) { continue }
        $visto[$p] = $true
        $limpia = ($p -split '#')[0].TrimEnd('/')
        $destino = Join-Path $dir $limpia
        if (-not (Test-Path -LiteralPath $destino)) {
          $filas += [pscustomobject]@{ Archivo = $rel; Ruta = $p }
        }
      }
    }
  }
}

Write-Output "RUTAS"
Write-Output "Root: $Root"
Write-Output "Archivos con ruta: $(($filas | Select-Object -ExpandProperty Archivo -Unique | Measure-Object).Count) | rutas rotas: $($filas.Count)"
Write-Output ""
Write-Output "VEREDICTO: $(if ($filas.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($filas.Count -gt 0) {
  Write-Output "ARCHIVO | RUTA"
  foreach ($f in ($filas | Sort-Object Archivo, Ruta)) { Write-Output "$($f.Archivo) | $($f.Ruta)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(rutas no juzga si el destino dice lo que debe: eso es integridad)"
