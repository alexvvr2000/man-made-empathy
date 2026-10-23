# notas.ps1 — unidad del piso de esta instancia
# Decide: si la memoria se escribe como manda la carta, en la base única.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Una sola base, y ningún export: la base es la fuente.
# Base: .sesion-continua/mantis.db (oculta, en gitignore). Esquema: notas/esquema.sql.
# Rige ../mantenimiento/notas/notas-tesis.md.
#
# No se aplica a: el contenido de la fila (eso lo decide el aplanado), ni al corte de una
# generación (eso vive en notas/generaciones/, y es archivo porque se lee como documento).
#
# Uso: pwsh -File mantis/piso/notas.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\mantis.db'

if (-not (Test-Path $Base)) {
  Write-Output "NOTAS"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/mantis.db"
  exit 0
}

function Q($sql) { & sqlite3 $Base $sql }

$tablas = @(Q "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;" | Where-Object { $_ })
$necesarias = @('fila','generacion','prueba','seccion','sesion','trabajo')
$errores = @()
foreach ($n in $necesarias) { if ($tablas -notcontains $n) { $errores += "falta la tabla: $n" } }

if ($errores.Count -gt 0) {
  Write-Output "NOTAS"
  Write-Output "Base: .sesion-continua/mantis.db"
  Write-Output "VEREDICTO: falla"
  Write-Output "PROBLEMA"
  foreach ($e in $errores) { Write-Output "  - $e" }
  exit 0
}

$filas = [int](Q "SELECT COUNT(*) FROM fila;")
$vivas = [int](Q "SELECT COUNT(*) FROM fila WHERE estado = 'vivo';")
$sinPieza = [int](Q "SELECT COUNT(*) FROM fila WHERE pieza IS NULL OR TRIM(pieza) = '';")
$sinVista = [int](Q "SELECT COUNT(*) FROM fila WHERE vista IS NULL OR TRIM(vista) = '';")
$sinCompilar = [int](Q "SELECT COUNT(*) FROM fila WHERE estado = 'cubierto' AND (compilado IS NULL OR TRIM(compilado) = '');")
$gens = [int](Q "SELECT COUNT(*) FROM generacion;")
$gensSinVista = [int](Q "SELECT COUNT(*) FROM generacion WHERE vista IS NULL OR TRIM(vista) = '';")
$sesion = Q "SELECT COUNT(*) FROM sesion WHERE id = 1;"
$orfanas = [int](Q "SELECT COUNT(*) FROM fila WHERE seccion NOT IN (SELECT nombre FROM seccion);")
$trabajo = [int](Q "SELECT COUNT(*) FROM trabajo;")

# El diff de hoy: cuántos archivos cambiaron desde el último commit, y cuántos tienen nota.
# Es la medida de cuánto se dijo sin anotar. Un archivo cambiado sin fila es una decisión sin rastro.
$ultimo = @(& git -C $Root log -1 --format='%H' 2>$null)
$cambios = @()
if ($ultimo) {
  $cambios += @(& git -C $Root diff --name-only $ultimo[0] 2>$null | Where-Object { $_ })
}
$cambios += @(& git -C $Root status --porcelain 2>$null | Where-Object { $_ } | ForEach-Object { $_.Substring(3).Trim() })
$cambios = @($cambios | Where-Object { $_ -and (Test-Path (Join-Path $Root $_)) } | Sort-Object -Unique)
$conNota = 0
foreach ($c in $cambios) {
  $corto = Split-Path $c -Leaf
  $hit = Q "SELECT COUNT(*) FROM fila WHERE pieza LIKE '%$corto%' OR usa LIKE '%$corto%' OR pieza LIKE '%$c%';"
  if ([int]$hit -gt 0) { $conNota++ }
}
$sinNota = $cambios.Count - $conNota

if ($filas -eq 0) { $errores += 'la base no tiene filas' }
if ($sinPieza -gt 0) { $errores += "filas sin pieza: $sinPieza" }
if ($sinVista -gt 0) { $errores += "filas sin vista: $sinVista" }
if ($sinCompilar -gt 0) { $errores += "filas cubiertas sin Compilado en: $sinCompilar" }
if ($gensSinVista -gt 0) { $errores += "generaciones sin vista: $gensSinVista" }
if ($orfanas -gt 0) { $errores += "filas en secciones que el esquema no declara: $orfanas" }
if (-not $sesion) { $errores += 'no hay bloque de sesion en la base' }
if ($sinNota -gt 0) { $errores += "archivos cambiados sin nota: $sinNota de $($cambios.Count)" }

Write-Output "NOTAS"
Write-Output "Base: .sesion-continua/mantis.db (una sola, sin export)"
Write-Output "Filas: $filas | vivas: $vivas | generaciones: $gens | trabajo: $trabajo"
Write-Output "Sin pieza: $sinPieza | sin vista: $sinVista | cubiertas sin compilar: $sinCompilar"
Write-Output "Cambios sin nota: $sinNota de $($cambios.Count)"
Write-Output ""
Write-Output "VEREDICTO: $(if ($errores.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($errores.Count -gt 0) {
  Write-Output "PROBLEMA"
  foreach ($e in $errores) { Write-Output "  - $e" }
  Write-Output ""
}

if ($cambios.Count -gt 0 -and $sinNota -gt 0) {
  Write-Output "SIN NOTA"
  foreach ($c in $cambios) {
    $corto = Split-Path $c -Leaf
    $hit = Q "SELECT COUNT(*) FROM fila WHERE pieza LIKE '%$corto%' OR usa LIKE '%$corto%' OR pieza LIKE '%$c%';"
    if ([int]$hit -eq 0) { Write-Output $c }
  }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(notas no juzga si lo anotado es valido: eso lo decide el aplanado)"
