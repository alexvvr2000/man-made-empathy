# fantasmas.ps1 — unidad del piso de esta instancia
# Decide: que ente no tiene sus tres piezas.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# FANTASMA: ente sin rastro.md, sin ruta.md o sin carga.md.
# Rige ../../Ouroboros/procesos/integridad.md, "El fantasma".
#
# Uso: pwsh -File mantis/piso/fantasmas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

$piezas = @('rastro.md', 'ruta.md', 'carga.md')
$hallazgos = @()
$entes = 0; $entesOk = 0

foreach ($d in (Get-ChildItem $Root -Directory -Recurse -Depth 3 | Where-Object { $_.FullName -notmatch '\\\.git\\' })) {
  $tiene = @($piezas | Where-Object { Test-Path (Join-Path $d.FullName $_) })
  if ($tiene.Count -eq 0) { continue }
  $entes++
  $rel = $d.FullName.Replace($Root + '\', '').Replace('\', '/')
  $faltan = @($piezas | Where-Object { -not (Test-Path (Join-Path $d.FullName $_)) })
  if ($faltan.Count -eq 0) { $entesOk++; continue }
  $hallazgos += [pscustomobject]@{ Ente = $rel; Falta = ($faltan -join ', ') }
}

Write-Output "FANTASMAS"
Write-Output "Root: $Root"
Write-Output "Entes: $entes | con las tres piezas: $entesOk"
Write-Output ""
Write-Output "VEREDICTO: $(if ($hallazgos.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($hallazgos.Count -gt 0) {
  Write-Output "ENTE | FALTA"
  foreach ($h in ($hallazgos | Sort-Object Ente)) { Write-Output "$($h.Ente) | $($h.Falta)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(fantasmas no juzga si el fallo que cubre cada ente sigue existiendo: eso es integridad)"