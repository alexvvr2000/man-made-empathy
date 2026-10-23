# ver.ps1 — unidad del piso de esta instancia
# Decide: si la memoria se puede leer sin abrir un archivo publicado.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Reemplaza a exportar.ps1: no hay .md publicado, la base es la fuente.
# Base: .sesion-continua/mantis.db. Esquema: notas/esquema.sql.
# Rige ../mantenimiento/notas/notas-tesis.md.
#
# No se aplica a: escribir la base (eso es anotar.ps1), ni al corte de una generación
# (eso va a notas/generaciones/ y se lee como documento).
#
# Uso: pwsh -File mantis/piso/ver.ps1 [-Root <ruta>] [-Seccion <nombre>] [-Formato <tabla|md>]

param(
  [string]$Root = (Join-Path $PSScriptRoot "..\.."),
  [string]$Seccion = '',
  [string]$Formato = 'tabla'
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\mantis.db'

if (-not (Test-Path $Base)) {
  Write-Output "VER"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/mantis.db"
  exit 0
}

function Q($sql) { & sqlite3 -separator ' | ' $Base $sql }

$filtro = if ($Seccion) { "WHERE f.seccion = '$Seccion'" } else { '' }

if ($Formato -eq 'md') {
  Write-Output "# Memoria — .sesion-continua/mantis.db"
  Write-Output ""
  Write-Output "## La sesión"
  Write-Output ""
  Write-Output '```'
  Q "SELECT 'Sesión: '||fecha||' | Vista: '||vista FROM sesion WHERE id=1;"
  Q "SELECT 'Estado: '||estado||' | Roto: '||roto FROM sesion WHERE id=1;"
  Q "SELECT 'Abierto: '||COALESCE(abierto,'') FROM sesion WHERE id=1;"
  Q "SELECT 'Siguiente: '||COALESCE(siguiente,'') FROM sesion WHERE id=1;"
  Q "SELECT 'Decidido: '||COALESCE(decidido,'') FROM sesion WHERE id=1;"
  Q "SELECT 'Rige: '||rige FROM sesion WHERE id=1;"
  Write-Output '```'
  Write-Output ""
  foreach ($s in @(Q "SELECT nombre FROM seccion ORDER BY orden;")) {
    $n = [int](Q "SELECT COUNT(*) FROM fila WHERE seccion = '$($s.Replace("'","''"))';")
    if ($n -eq 0) { continue }
    Write-Output "## $s"
    Write-Output ""
    Write-Output "| Dicho | De | Tipo | Usa | Sostenido | Estado | Vista |"
    Write-Output "|---|---|---|---|---|---|---|"
    Q "SELECT '| '||dicho||' | '||pieza||' | '||tipo||' | '||COALESCE(usa,'')||' | '||sostenido||' | '||estado||' | '||vista||' |' FROM fila WHERE seccion = '$($s.Replace("'","''"))' ORDER BY id;"
    Write-Output ""
  }
}
else {
  Write-Output "VER"
  Write-Output "Base: .sesion-continua/mantis.db"
  Write-Output ""
  Write-Output "SESIÓN"
  Q "SELECT fecha, vista, estado, COALESCE(decidido,'') FROM sesion WHERE id=1;"
  Write-Output ""
  Write-Output "ID | SECCIÓN | TIPO | SOSTENIDO | ESTADO | DICHO"
  Q "SELECT f.id, f.seccion, f.tipo, f.sostenido, f.estado, substr(f.dicho,1,90) FROM fila f $filtro ORDER BY f.id DESC LIMIT 40;"
  Write-Output ""
}

Write-Output "VEREDICTO: pasa"
Write-Output ""
Write-Output "INDETERMINADO"
Write-Output "(ver imprime la base; no decide si lo anotado sirve, y no escribe nada)"
