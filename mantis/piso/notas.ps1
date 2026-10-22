# notas.ps1 — unidad del piso de esta instancia
# Decide: si la memoria de la tesis se escribe como manda la carta.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# La base es el acelerador; el export es la fuente.
# Base: .sesion-continua/tesis.db (oculta). Esquema: notas/esquema.sql. Publicado: notas/actuales.md
# Rige ../mantis/mantenimiento/notas/notas-tesis.md. Las continuas NO se validan aqui: son mutables.
#
# No se aplica a: lo que no va a la tesis (eso es .sesion-continua/), ni a las generaciones.

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\tesis.db'


if (-not (Test-Path $Base)) {
  Write-Output "NOTAS"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/tesis.db"
  exit 0
}

function Q($sql) { & sqlite3 $Base $sql }

$filas = [int](Q "SELECT COUNT(*) FROM fila;")
$vivas = [int](Q "SELECT COUNT(*) FROM fila WHERE estado = 'vivo';")
$sinPieza = [int](Q "SELECT COUNT(*) FROM fila WHERE pieza IS NULL OR TRIM(pieza) = '';")
$sinVista = [int](Q "SELECT COUNT(*) FROM fila WHERE vista IS NULL OR TRIM(vista) = '';")
$sinCompilar = [int](Q "SELECT COUNT(*) FROM fila WHERE estado = 'cubierto' AND (compilado IS NULL OR TRIM(compilado) = '');")
$gens = [int](Q "SELECT COUNT(*) FROM generacion;")
$gensSinVista = [int](Q "SELECT COUNT(*) FROM generacion WHERE vista IS NULL OR TRIM(vista) = '';")
$sesion = Q "SELECT COUNT(*) FROM sesion WHERE id = 1;"
$orfanas = [int](Q "SELECT COUNT(*) FROM fila WHERE seccion NOT IN (SELECT nombre FROM seccion);")

$errores = @()
if ($filas -eq 0) { $errores += 'la base no tiene filas' }
if ($sinPieza -gt 0) { $errores += "filas sin pieza: $sinPieza" }
if ($sinVista -gt 0) { $errores += "filas sin vista: $sinVista" }
if ($sinCompilar -gt 0) { $errores += "filas cubiertas sin Compilado en: $sinCompilar" }
if ($gensSinVista -gt 0) { $errores += "generaciones sin vista: $gensSinVista" }
if ($orfanas -gt 0) { $errores += "filas en secciones que el esquema no declara: $orfanas" }
if (-not $sesion) { $errores += 'no hay bloque de sesion en la base' }

Write-Output "NOTAS"
Write-Output "Base: .sesion-continua/tesis.db"
Write-Output "Filas: $filas | vivas: $vivas | generaciones: $gens"
Write-Output "Sin pieza: $sinPieza | sin vista: $sinVista | cubiertas sin compilar: $sinCompilar"
Write-Output ""
Write-Output "VEREDICTO: $(if ($errores.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($errores.Count -gt 0) {
  Write-Output "PROBLEMA"
  foreach ($e in $errores) { Write-Output "$e" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(notas no juzga si lo anotado es valido: eso lo decide el aplanado)"