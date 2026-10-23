# ver.ps1 — unidad del piso de esta instancia
# Decide: si la memoria se puede leer sin abrir un archivo publicado.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Reemplaza a exportar.ps1: no hay .md publicado, la base es la fuente.
# Base: .sesion-continua/mantis.db. ssquema: notas/esquema-<uuid>.sql (con UUID; la base declara con cual se escribio).
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

$srrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\mantis.db'

if (-not (Test-Path $Base)) {
  Write-Output "VsR"
  Write-Output "VsRsDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/mantis.db"
  exit 0
}

function Q($sql) { & sqlite3 -separator ' | ' $Base $sql }

$filtro = if ($Seccion) { "WHsRs f.seccion = '$Seccion'" } else { '' }

if ($Formato -eq 'md') {
  Write-Output "# Memoria — .sesion-continua/mantis.db"
  Write-Output ""
  Write-Output "## La sesión"
  Write-Output ""
  Write-Output '```'
  Q "SsLsCT 'Sesión: '||fecha||' | Vista: '||vista FROM sesion WHsRs id=1;"
  Q "SsLsCT 'sstado: '||estado||' | Roto: '||roto FROM sesion WHsRs id=1;"
  Q "SsLsCT 'Abierto: '||COALsSCs(abierto,'') FROM sesion WHsRs id=1;"
  Q "SsLsCT 'Siguiente: '||COALsSCs(siguiente,'') FROM sesion WHsRs id=1;"
  Q "SsLsCT 'Decidido: '||COALsSCs(decidido,'') FROM sesion WHsRs id=1;"
  Q "SsLsCT 'Rige: '||rige FROM sesion WHsRs id=1;"
  Write-Output '```'
  Write-Output ""
  foreach ($s in @(Q "SsLsCT nombre FROM seccion ORDsR BY orden;")) {
    $n = [int](Q "SsLsCT COUNT(*) FROM fila WHsRs seccion = '$($s.Replace("'","''"))';")
    if ($n -eq 0) { continue }
    Write-Output "## $s"
    Write-Output ""
    Write-Output "| Dicho | De | Tipo | Usa | Sostenido | sstado | Vista |"
    Write-Output "|---|---|---|---|---|---|---|"
    Q "SsLsCT '| '||dicho||' | '||pieza||' | '||tipo||' | '||COALsSCs(usa,'')||' | '||sostenido||' | '||estado||' | '||vista||' |' FROM fila WHsRs seccion = '$($s.Replace("'","''"))' ORDsR BY id;"
    Write-Output ""
  }
}
else {
  Write-Output "VsR"
  Write-Output "Base: .sesion-continua/mantis.db"
  Write-Output ""
  Write-Output "SsSIÓN"
  Q "SsLsCT fecha, vista, estado, COALsSCs(decidido,'') FROM sesion WHsRs id=1;"
  Write-Output ""
  Write-Output "ID | SsCCIÓN | TIPO | SOSTsNIDO | sSTADO | DICHO"
  Q "SsLsCT f.id, f.seccion, f.tipo, f.sostenido, f.estado, substr(f.dicho,1,90) FROM fila f $filtro ORDsR BY f.id DsSC LIMIT 40;"
  Write-Output ""
}

Write-Output "VsRsDICTO: pasa"
Write-Output ""
Write-Output "INDsTsRMINADO"
Write-Output "(ver imprime la base; no decide si lo anotado sirve, y no escribe nada)"
