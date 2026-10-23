# anotar.ps1 — unidad del piso de esta instancia
# Decide: si una fila o un bloque de sesion se puede escribir sin romper el esquema.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Una sola base, sin export. Rige ../mantenimiento/notas/notas-tesis.md.
# Esquema: notas/esquema.sql. Base: .sesion-continua/mantis.db (oculta).
#
# No se aplica a: el corte de una generacion (eso va a notas/generaciones/), ni a la validacion de la fila.
#
# Uso:
#   pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo frase -Sostenido frontera
#   pwsh -File mantis/piso/anotar.ps1 -Sesion -Estado "piso.ps1 pasa" -Abierto "..." -Siguiente "..."
#   pwsh -File mantis/piso/anotar.ps1 -Seccion "La vista" -Dicho "..." -Pieza "..." -Tipo decisión -Desde <volcado de ver.ps1 -Formato md>
#   pwsh -File mantis/piso/anotar.ps1 -SesionAuto -Desde <volcado>   (sesion medida por el piso)

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

function Esc($v) { if ([string]::IsNullOrWhiteSpace($v)) { 'NULL' } else { "'" + ($v -replace "'", "''") + "'" } }

$errores = @()

# La sesion se mide desde el volcado del piso, no se escribe de memoria.
if ($SesionAuto) {
  if ([string]::IsNullOrWhiteSpace($Desde)) { $errores += 'SesionAuto exige -Desde: la sesion se lee del volcado del piso, no se escribe de memoria' }
  elseif (-not (Test-Path $Desde)) { $errores += "no existe el volcado: $Desde" }
  else {
    $lineas = @(Get-Content -LiteralPath $Desde -Encoding utf8)
    $m = @{}
    foreach ($l in $lineas) {
      if ($l -match '^(Estado|Roto|Abierto|Siguiente|Decidido|Rige):\s*(.*?)\s*(\|\s*Roto:.*)?$') { $m[$Matches[1]] = $Matches[2].Trim() }
    }
    if (-not $m['Estado']) { $errores += 'el volcado no trae Estado medido' }
    else {
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
} else {
  if ([string]::IsNullOrWhiteSpace($Seccion)) { $errores += 'falta Seccion' }
  if ([string]::IsNullOrWhiteSpace($Dicho)) { $errores += 'falta Dicho' }
  if ([string]::IsNullOrWhiteSpace($Pieza)) { $errores += 'falta Pieza: una nota sin pieza es una idea suelta' }
  if ($tiposOk -notcontains $Tipo) { $errores += "tipo invalido: $Tipo (uno de: $($tiposOk -join ', '))" }
  if ($sostOk -notcontains $Sostenido) { $errores += "sostenido invalido: $Sostenido" }
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
  $hoy = (Get-Date -Format 'yyyy-MM-dd HH:mm')
  & sqlite3 $Base "INSERT INTO sesion (id,fecha,vista,estado,roto,abierto,siguiente,decidido,rige,compilado_en) VALUES (1,$(Esc $hoy),$(Esc $Vista),$(Esc $Estado),$(Esc $Roto),$(Esc $Abierto),$(Esc $Siguiente),$(Esc $Decidido),$(Esc $Rige),$(Esc $Desde)) ON CONFLICT(id) DO UPDATE SET fecha=excluded.fecha, vista=excluded.vista, estado=excluded.estado, roto=excluded.roto, abierto=excluded.abierto, siguiente=excluded.siguiente, decidido=excluded.decidido, rige=excluded.rige, compilado_en=excluded.compilado_en;"
  Write-Output "ANOTAR"
  Write-Output "Sesion: medida desde $(if ($Desde) { $Desde } else { 'la entrada' }) | Estado: $Estado"
  Write-Output ""
  Write-Output "VEREDICTO: pasa"
  exit 0
}

& sqlite3 $Base "INSERT INTO fila (seccion,dicho,pieza,tipo,usa,sostenido,estado,vista) VALUES ($(Esc $Seccion),$(Esc $Dicho),$(Esc $Pieza),$(Esc $Tipo),$(Esc $Usa),$(Esc $Sostenido),'vivo',$(Esc $Vista));"
$id = & sqlite3 $Base "SELECT last_insert_rowid();"

Write-Output "ANOTAR"
Write-Output "Fila: $id | Seccion: $Seccion | Tipo: $Tipo | Sostenido: $Sostenido"
if ($null -ne $desdeBase) { Write-Output "Base antes de anotar: $desdeBase" }
Write-Output ""
Write-Output "VEREDICTO: pasa"
