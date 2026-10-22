# fantasmas.ps1 — unidad del piso de esta instancia
# Decide: que existe sin deterrente que lo sostenga.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
# Tres preguntas, y valen igual para 5 sub-tareas que para 500.
# Uso: pwsh -File mantis/piso/fantasmas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

$hallazgos = @()
$subs = 0; $subsOk = 0; $procs = 0; $procsOk = 0

function Anotar($nivel, $ruta, $que) {
  $script:hallazgos += [pscustomobject]@{ Nivel = $nivel; Ruta = $ruta; Falta = $que }
}

# ---- P1: la tarea tiene deterrente? ----
$tareaDet = Join-Path $Root 'S.A.R.A\deterrente.md'
if (-not (Test-Path $tareaDet)) { Anotar 'tarea' 'S.A.R.A/' 'sin deterrente' }

# ---- P2: cada sub-tarea declara su deterrente? ----
$base = Join-Path $Root 'S.A.R.A\punto-de-partida'
if (Test-Path $base) {
  foreach ($s in (Get-ChildItem $base -Directory | Sort-Object Name)) {
    $subs++
    $r = Join-Path $s.FullName 'README.md'
    $rel = "S.A.R.A/punto-de-partida/$($s.Name)"
    if (-not (Test-Path $r)) { Anotar 'sub-tarea' $rel 'sin README (no puede declarar deterrente)'; continue }
    $t = Get-Content $r -Raw -Encoding utf8
    if ($t -match '(?m)^\*\*Deterrente:\*\*') { $subsOk++ } else { Anotar 'sub-tarea' $rel 'sin deterrente declarado' }

    # ---- P3: cada proceso tiene quien lo refute? ----
    foreach ($a in (Get-ChildItem $s.FullName -Filter *.md -File -Recurse | Where-Object { $_.Name -ne 'README.md' })) {
      $procs++
      $txt = Get-Content $a.FullName -Raw -Encoding utf8
      if ($txt -match '(?m)^\*\*Falsificador|\*\*Falsificador:\*\*|^##+\s+Falsificador') { $procsOk++ }
      else { Anotar 'proceso' ($a.FullName.Replace($Root + '\','').Replace('\','/')) 'sin falsificador' }
    }
  }
}

Write-Output "FANTASMAS"
Write-Output "Root: $Root"
Write-Output "Sub-tareas: $subs | con deterrente: $subsOk"
Write-Output "Procesos: $procs | con falsificador: $procsOk"
Write-Output ""
$veredicto = if ($hallazgos.Count -eq 0) { 'pasa' } else { 'falla' }
Write-Output "VEREDICTO: $veredicto"
Write-Output ""

if ($hallazgos.Count -gt 0) {
  Write-Output "NIVEL | RUTA | FALTA"
  foreach ($h in ($hallazgos | Sort-Object Nivel, Ruta)) { Write-Output "$($h.Nivel) | $($h.Ruta) | $($h.Falta)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(fantasmas no juzga si el fallo que cubre una sub-tarea sigue existiendo: eso es integridad)"
