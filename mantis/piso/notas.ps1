# notas.ps1 — unidad del piso de esta instancia
# Decide: si la memoria de la conversacion se esta escribiendo como manda la carta.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# NOTAS: 1 Tesis/notas.md es la memoria. Un turno con decision y sin fila no esta entregado.
# Columna: Dicho | De | Tipo | Usa | Sostenido | Estado
# Rige ../../AGENTS.md, "Escribir notas".
#
# Uso: pwsh -File mantis/piso/notas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Notas = Join-Path $Root '1 Tesis\notas.md'

if (-not (Test-Path $Notas)) {
  Write-Output "NOTAS"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe 1 Tesis/notas.md"
  exit 0
}

$tipos = @('analogía', 'referencia', 'cita', 'frase', 'decisión', 'descarte')
$sinPieza = @(); $sinTipo = @(); $estados = @{}
$filas = 0

foreach ($l in (Select-String -Path $Notas -Pattern '^\|\s+[«A-Za-zÁÉÍÓÚ]' | Where-Object { $_.Line -notmatch '^\|\s*Dicho\s*\|' }).Line) {
  $cols = ($l.Trim() -replace '^\||\|$', '') -split '\|'
  foreach ($i in 0..($cols.Count - 1)) { $cols[$i] = ($cols[$i] -replace '`', '').Trim() }
  if ($cols.Count -lt 6) { $sinPieza += $l; continue }
  $filas++
  if ([string]::IsNullOrWhiteSpace($cols[1]) -or $cols[1] -eq '—') { $sinPieza += $l }
  if ($tipos -notcontains $cols[2]) { $sinTipo += $l }
  $estados[$cols[5]] = 1 + [int]$estados[$cols[5]]
}

$mod = (Get-Item $Notas).LastWriteTime.ToString('yyyy-MM-dd HH:mm')
$resumen = ($estados.Keys | Sort-Object | ForEach-Object { "$_ : $($estados[$_])" }) -join ' | '
$pasa = ($sinPieza.Count -eq 0 -and $sinTipo.Count -eq 0 -and $filas -gt 0)

Write-Output "NOTAS"
Write-Output "Archivo: 1 Tesis/notas.md"
Write-Output "Filas: $filas | Ultima escritura: $mod"
Write-Output "Estados: $resumen"
Write-Output "Sin pieza: $($sinPieza.Count) | Con tipo fuera de la lista: $($sinTipo.Count)"
Write-Output ""
Write-Output "VEREDICTO: $(if ($pasa) { 'pasa' } else { 'falla' })"
Write-Output ""

if (-not $pasa) {
  Write-Output "PROBLEMA | FILA"
  foreach ($f in $sinPieza) { Write-Output "sin pieza | $f" }
  foreach ($f in $sinTipo) { Write-Output "tipo invalido | $f" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(notas no juzga si lo anotado es valido: eso lo decide el aplanado)"