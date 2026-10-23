# anotar.ps1 — la unidad que escribe la memoria
# Decide: si una fila o un bloque de sesion se escribe sin romper el esquema.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Rige ../../Ouroboros/procesos/memoria continua.md, paso 8:
#   "Guardar en cada interacción, no al final. La memoria no vive en el ejecutor:
#    vive en este proceso."
# Base: .sesion-continua/mantis.db. Esquema: notas/corrida-<uuid>/esquema.sql.
#
# No se aplica a: la cobertura del repo (eso es notas.ps1), ni al turno (eso es turno.ps1).
#
# Uso:
#   pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo decisión
#   pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "piso.ps1 pasa (7 de 7)"
#   pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "(lo que mide el piso)"
#   pwsh -File mantis/piso/anotar.ps1 -Chequear

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
  [string]$Desde = '',
  [switch]$SesionAuto,
  [switch]$Chequear
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\mantis.db'

if (-not (Test-Path $Base)) {
  Write-Output "ANOTAR"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/mantis.db"
  exit 0
}

$tiposOk = @('analogía', 'referencia', 'cita', 'frase', 'decisión', 'descarte')
$sostOk = @('prueba', 'frontera', 'nada')
if ([string]::IsNullOrWhiteSpace($Vista)) { $Vista = 'vista ' + (Get-Date -Format 'yyyy-MM-dd') }

function Q($sql) { & sqlite3 $Base $sql }
function Esc($v) { if ([string]::IsNullOrWhiteSpace($v)) { 'NULL' } else { "'" + ($v -replace "'", "''") + "'" } }

$errores = @()

if ($SesionAuto) {
  if ([string]::IsNullOrWhiteSpace($Desde)) {
    $errores += 'SesionAuto exige -Desde: la sesion se lee del volcado del piso, no se escribe de memoria'
  } elseif (-not (Test-Path $Desde)) {
    $errores += "no existe el volcado: $Desde"
  } else {
    $m = @{}
    foreach ($linea in (Get-Content -LiteralPath $Desde -Encoding utf8)) {
      if ($linea -match '^(Estado|Roto|Abierto|Siguiente|Decidido|Rige):\s*(.*?)\s*(\|\s*Roto:.*)?$') {
        $m[$Matches[1]] = $Matches[2].Trim()
      }
    }
    if (-not $m['Estado']) {
      $errores += 'el volcado no trae Estado medido'
    } else {
      $Sesion = $true
      $Estado = $m['Estado']
      if ($m['Roto']) { $Roto = $m['Roto'] }
      if ($m['Abierto']) { $Abierto = $m['Abierto'] }
      if ($m['Siguiente']) { $Siguiente = $m['Siguiente'] }
      if ($m['Decidido']) { $Decidido = $m['Decidido'] }
      if ($m['Rige']) { $Rige = $m['Rige'] }
    }
  }
}

$desdeBase = $null
if (-not [string]::IsNullOrWhiteSpace($Desde) -and (Test-Path $Desde) -and -not $SesionAuto) {
  $desdeBase = @(Get-Content -LiteralPath $Desde -Encoding utf8 | Where-Object { $_ -match '^\|' -and $_ -notmatch '^\|[-: ]+\|$' }).Count
}

if ($Sesion) {
  if ([string]::IsNullOrWhiteSpace($Estado)) { $errores += 'la sesion no trae Estado medido' }
} elseif (-not $SesionAuto) {
  if ([string]::IsNullOrWhiteSpace($Seccion)) { $errores += 'falta Seccion' }
  if ([string]::IsNullOrWhiteSpace($Dicho)) { $errores += 'falta Dicho' }
  if ([string]::IsNullOrWhiteSpace($Pieza)) { $errores += 'falta Pieza: una nota sin pieza es una idea suelta' }
  if ($tiposOk -notcontains $Tipo) { $errores += "tipo invalido: $Tipo" }
  if ($sostOk -notcontains $Sostenido) { $errores += "sostenido invalido: $Sostenido" }
  $existe = Q "SELECT 1 FROM seccion WHERE nombre = $(Esc $Seccion);"
  if (-not $existe) { $errores += "seccion desconocida: $Seccion" }
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
  $hoy = Get-Date -Format 'yyyy-MM-dd HH:mm'
  Q "INSERT INTO sesion (id,fecha,vista,estado,roto,abierto,siguiente,decidido,rige,compilado_en) VALUES (1,$(Esc $hoy),$(Esc $Vista),$(Esc $Estado),$(Esc $Roto),$(Esc $Abierto),$(Esc $Siguiente),$(Esc $Decidido),$(Esc $Rige),$(Esc $Desde)) ON CONFLICT(id) DO UPDATE SET fecha=excluded.fecha, vista=excluded.vista, estado=excluded.estado, roto=excluded.roto, abierto=excluded.abierto, siguiente=excluded.siguiente, decidido=excluded.decidido, rige=excluded.rige, compilado_en=excluded.compilado_en;" | Out-Null
  Write-Output "ANOTAR"
  Write-Output "Sesion: actualizada | Estado: $Estado"
  Write-Output ""
  Write-Output "VEREDICTO: pasa"
  exit 0
}

Q "INSERT INTO fila (seccion,dicho,pieza,tipo,usa,sostenido,estado,vista) VALUES ($(Esc $Seccion),$(Esc $Dicho),$(Esc $Pieza),$(Esc $Tipo),$(Esc $Usa),$(Esc $Sostenido),'vivo',$(Esc $Vista));" | Out-Null
$id = Q "SELECT MAX(id) FROM fila;"

Write-Output "ANOTAR"
Write-Output "Fila: $id | Seccion: $Seccion | Tipo: $Tipo | Sostenido: $Sostenido"
if ($null -ne $desdeBase) { Write-Output "Base antes de anotar: $desdeBase" }
Write-Output ""
Write-Output "VEREDICTO: pasa"
