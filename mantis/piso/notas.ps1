# notas.ps1 — unidad del piso de esta instancia
# Decide: si la memoria de la conversacion se esta escribiendo como manda la carta.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# NOTAS: notas/actuales.md es la memoria. Un turno con decision y sin fila no esta entregado.
# Columna: Dicho | De | Tipo | Usa | Sostenido | Estado
# Rige ../../AGENTS.md, "Escribir notas".
#
# Uso: pwsh -File mantis/piso/notas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Notas = Join-Path $Root 'notas\actuales.md'

if (-not (Test-Path $Notas)) {
  Write-Output "NOTAS"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe notas/actuales.md"
  exit 0
}

$tipos = @('analogía', 'referencia', 'cita', 'frase', 'decisión', 'descarte')
$sinPieza = @(); $sinTipo = @(); $estados = @{}
$filas = 0

foreach ($l in (Select-String -Path $Notas -Pattern '^\|\s+[«A-Za-zÁÉÍÓÚ]' | Where-Object { $_.Line -notmatch '^\|\s*Dicho\s*\|' }).Line) {
  $cols = ($l.Trim() -replace '^\||\|$', '') -split '\|'
  foreach ($i in 0..($cols.Count - 1)) { $cols[$i] = ($cols[$i] -replace '`', '').Trim() }
  if ($cols.Count -lt 7) { continue }
  $filas++
  if ([string]::IsNullOrWhiteSpace($cols[1]) -or $cols[1] -eq '—') { $sinPieza += $l }
  if ($tipos -notcontains $cols[2]) { $sinTipo += $l }
  $estados[$cols[5]] = 1 + [int]$estados[$cols[5]]
}

$mod = (Get-Item $Notas).LastWriteTime.ToString('yyyy-MM-dd HH:mm')
$genDir = Join-Path $Root 'notas\generaciones'
$gens = @(Get-ChildItem $genDir -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -notmatch '^\.' })
$gensSinRegistro = @($gens | Where-Object { -not (Test-Path (Join-Path $_.FullName 'registro.md')) })

# El bloque de continuas no puede ser mas viejo que el ultimo archivo cambiado.
$cont = Join-Path $Root 'notas\continuas.md'
$contViejo = $false
if (Test-Path $cont) {
  $bloque = (Get-Item $cont).LastWriteTime
  $ultimo = Get-ChildItem $Root -Recurse -File -Include *.md,*.ps1 -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.FullName -notmatch '\\notas\\' -and $_.Name -ne 'continuas.md' } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
  if ($ultimo -and $bloque -lt $ultimo.LastWriteTime) { $contViejo = $true }
}
$resumen = ($estados.Keys | Sort-Object | ForEach-Object { "$_ : $($estados[$_])" }) -join ' | '
$pasa = ($sinPieza.Count -eq 0 -and $sinTipo.Count -eq 0 -and $filas -gt 0 -and -not $contViejo)

Write-Output "NOTAS"
Write-Output "Archivo: notas/actuales.md"
Write-Output "Filas: $filas | Ultima escritura: $mod"
Write-Output "Estados: $resumen"
Write-Output "Sin pieza: $($sinPieza.Count) | Con tipo fuera de la lista: $($sinTipo.Count)"
Write-Output "Generaciones: $($gens.Count) | sin registro: $($gensSinRegistro.Count)"
Write-Output "Continuas: $(if ($contViejo) { 'VIEJO: hay archivos cambiados despues del bloque' } else { 'al dia' })"
Write-Output ""
Write-Output "VEREDICTO: $(if ($pasa -and $gensSinRegistro.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if (-not $pasa) {
  Write-Output "PROBLEMA | FILA"
  foreach ($f in $sinPieza) { Write-Output "sin pieza | $f" }
  foreach ($f in $sinTipo) { Write-Output "tipo invalido | $f" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(notas no juzga si lo anotado es valido: eso lo decide el aplanado)"