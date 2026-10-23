# piso.ps1 — el tren de esta instancia
# Decide: si el repo pasa todas las unidades del piso, y con un solo veredicto.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Un tren no es una tuberia: cada unidad se puede correr suelta y su salida se lee sola.
# Rige ../../Ouroboros/piso.md, "El tren".
#
# El piso son las unidades que DECIDEN: emiten pasa o falla sobre el repo.
# Las herramientas NO votan: se corren, su salida se lee, y no cambian el veredicto.
# Una herramienta contada como unidad infla el marcador sin decidir nada.
#
# Uso: pwsh -File mantis/piso/piso.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Las cinco que deciden.
$unidades = @(
  'inventario.ps1',
  'rutas.ps1',
  'fantasmas.ps1',
  'notas.ps1',
  'turno.ps1'
)


$filas = @()
foreach ($u in $unidades) {
  $script = Join-Path $PSScriptRoot $u
  if (-not (Test-Path $script)) { $filas += [pscustomobject]@{ Unidad = $u; Veredicto = 'no corre' }; continue }
  $lineas = & pwsh -NoProfile -File $script -Root $Root 2>&1
  $veredicto = 'indeterminado'
  foreach ($l in $lineas) { if ($l -match '^VEREDICTO:\s*(\w+)') { $veredicto = $Matches[1]; break } }
  $filas += [pscustomobject]@{ Unidad = $u; Veredicto = $veredicto }
}

$falla = @($filas | Where-Object { $_.Veredicto -ne 'pasa' })
$enPasa = @($filas | Where-Object { $_.Veredicto -eq 'pasa' }).Count

Write-Output "PISO"
Write-Output "Root: $Root"
Write-Output ""
Write-Output "UNIDAD | VEREDICTO"
foreach ($f in $filas) { Write-Output "$($f.Unidad) | $($f.Veredicto)" }
Write-Output ""
Write-Output "Unidades en pasa: $enPasa de $($filas.Count)"
Write-Output ""
Write-Output "VEREDICTO: $(if ($falla.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($falla.Count -gt 0) {
  Write-Output "FALLA EN"
  foreach ($f in $falla) { Write-Output "$($f.Unidad) | $($f.Veredicto)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(el tren no decide si lo medido sirve: eso es criterio)"
