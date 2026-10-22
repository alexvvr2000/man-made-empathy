# anotar.ps1 — unidad del piso de esta instancia
# Decide: si una fila o un bloque de sesion se puede escribir sin romper el esquema.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# La base es el acelerador; el export es la fuente. Rige ../mantis/mantenimiento/notas/notas-tesis.md.
# Esquema: notas/esquema.sql. Base: .sesion-continua/tesis.db (oculta).
#
# No se aplica a: lo que no va a la tesis (eso es continuas.md), ni a las generaciones.
#
# Uso:
#   pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo frase -Sostenido frontera
#   pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "piso.ps1 pasa" -Abierto "..." -Siguiente "..."
#   pwsh -File mantis/piso/anotar.ps1 -Chequear        (solo valida, no escribe)

param(
  [string]$Root = (Join-Path $PSScriptRoot "..\.."),
  [string]$Seccion,
  [string]$Dicho,
  [string]$Pieza,
  [string]$Tipo = 'frase',
  [string]$Usa = 'Tesis',
  [string]$Sostenido = 'frontera',
  [string]$Vista = '',
  [switch]$Sesion,
  [string]$Estado,
  [string]$Roto = 'ninguno',
  [string]$Abierto,
  [string]$Siguiente,
  [string]$Decidido,
  [string]$Rige = 'claridad | sesgo declarado',
  [switch]$Chequear
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\tesis.db'

if (-not (Test-Path $Base)) {
  Write-Output "ANOTAR"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .db/notas.db"
  exit 0
}

$tiposOk = @('analogía', 'referencia', 'cita', 'frase', 'decisión', 'descarte')
$sostOk = @('prueba', 'frontera', 'nada')
if ([string]::IsNullOrWhiteSpace($Vista)) { $Vista = 'vista ' + (Get-Date -Format 'yyyy-MM-dd') }

function Esc($v) { if ([string]::IsNullOrWhiteSpace($v)) { 'NULL' } else { "'" + ($v -replace "'", "''") + "'" } }

$errores = @()
if ($Sesion) {
  if ([string]::IsNullOrWhiteSpace($Estado)) { $errores += 'la sesion no trae Estado medido' }
} else {
  if ([string]::IsNullOrWhiteSpace($Seccion)) { $errores += 'falta Seccion' }
  if ([string]::IsNullOrWhiteSpace($Dicho)) { $errores += 'falta Dicho' }
  if ([string]::IsNullOrWhiteSpace($Pieza)) { $errores += 'falta Pieza: una nota sin pieza es una idea suelta' }
  if ($tiposOk -notcontains $Tipo) { $errores += "tipo invalido: $Tipo (uno de: $($tiposOk -join ', '))" }
  if ($sostOk -notcontains $Sostenido) { $errores += "sostenido invalido: $Sostenido" }
  # La seccion debe existir en el esquema.
  $existe = & sqlite3 $Base "SELECT 1 FROM seccion WHERE nombre = $(Esc $Seccion);"
  if (-not $existe) { $errores += "seccion desconocida: $Seccion (ver notas/esquema.sql, tabla seccion)" }
}

if ($errores.Count -gt 0 -or $Chequear) {
  Write-Output "ANOTAR"
  Write-Output "Errores: $($errores.Count)"
  foreach ($e in $errores) { Write-Output "  - $e" }
  Write-Output ""
  Write-Output "VEREDICTO: $(if ($errores.Count -eq 0) { 'pasa' } else { 'falla' })"
  exit 0
}

if ($Sesion) {
  & sqlite3 $Base "INSERT INTO sesion (id,fecha,vista,estado,roto,abierto,siguiente,decidido,rige) VALUES (1,$(Esc (Get-Date -Format 'yyyy-MM-dd HH:mm')),$(Esc $Vista),$(Esc $Estado),$(Esc $Roto),$(Esc $Abierto),$(Esc $Siguiente),$(Esc $Decidido),$(Esc $Rige)) ON CONFLICT(id) DO UPDATE SET fecha=excluded.fecha, vista=excluded.vista, estado=excluded.estado, roto=excluded.roto, abierto=excluded.abierto, siguiente=excluded.siguiente, decidido=excluded.decidido, rige=excluded.rige;"
  Write-Output "ANOTAR"
  Write-Output "Sesion: actualizada en el sitio"
  Write-Output ""
  Write-Output "VEREDICTO: pasa"
  exit 0
}

& sqlite3 $Base "INSERT INTO fila (seccion,dicho,pieza,tipo,usa,sostenido,estado,vista) VALUES ($(Esc $Seccion),$(Esc $Dicho),$(Esc $Pieza),$(Esc $Tipo),$(Esc $Usa),$(Esc $Sostenido),'vivo',$(Esc $Vista));"
$id = & sqlite3 $Base "SELECT last_insert_rowid();"

Write-Output "ANOTAR"
Write-Output "Fila: $id | Seccion: $Seccion | Tipo: $Tipo | Sostenido: $Sostenido"
Write-Output ""
Write-Output "VEREDICTO: pasa"
