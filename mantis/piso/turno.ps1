# turno.ps1 — la unidad que no deja cerrar un turno sin su entrada
# Decide: si el turno deja rastro en la memoria, por interacción y no al final del repo.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Rige ../../Ouroboros/procesos/memoria continua.md, paso 8:
#   "Guardar en cada interacción, no al final. La memoria no vive en el ejecutor:
#    vive en este proceso. Un turno que no deja entrada no está entregado."
#
# Base: .sesion-continua/mantis.db. Tabla: turno.
# No se aplica a: lo que se anota (eso es anotar.ps1), ni a la cobertura del repo
# (eso es notas.ps1, que mide el diff completo, no la interacción).
#
# Uso:
#   pwsh -File mantis/piso/turno.ps1 -Abrir "lo que se va a hacer en este turno"
#   pwsh -File mantis/piso/turno.ps1 -Anotar "la fila se escribe en este turno"
#   pwsh -File mantis/piso/turno.ps1 -Cerrar -Entradas 3
#   pwsh -File mantis/piso/turno.ps1            (veredicto del turno abierto)

param(
  [string]$Root = (Join-Path $PSScriptRoot "..\.."),
  [string]$Abrir,
  [string]$Anotar,
  [switch]$Cerrar,
  [int]$Entradas = -1
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\mantis.db'

if (-not (Test-Path $Base)) {
  Write-Output "TURNO"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .sesion-continua/mantis.db"
  exit 0
}

function Q($sql) { & sqlite3 $Base $sql }
function Esc($v) { if ([string]::IsNullOrWhiteSpace($v)) { 'NULL' } else { "'" + ($v -replace "'", "''") + "'" } }

& sqlite3 $Base "CREATE TABLE IF NOT EXISTS turno (id INTEGER PRIMARY KEY, abierto TEXT NOT NULL, cerrado TEXT, dijo TEXT, entradas INTEGER NOT NULL DEFAULT 0, filas_antes INTEGER NOT NULL DEFAULT 0, filas_despues INTEGER NOT NULL DEFAULT 0);" | Out-Null

$filas = [int](Q "SELECT COUNT(*) FROM fila;")
$vivo = Q "SELECT id FROM turno WHERE cerrado IS NULL ORDER BY id DESC LIMIT 1;"

if ($Abrir) {
  if ($vivo) { Q "UPDATE turno SET cerrado = 'reemplazado' WHERE id = $vivo;" | Out-Null }
  Q "INSERT INTO turno (abierto, dijo, filas_antes) VALUES (datetime('now','localtime'), $(Esc $Abrir), $filas);" | Out-Null
  $id = Q "SELECT id FROM turno ORDER BY id DESC LIMIT 1;"
  Write-Output "TURNO"
  Write-Output "Abierto: $id | Dijo: $Abrir | Filas antes: $filas"
  Write-Output ""
  Write-Output "VEREDICTO: pasa"
  exit 0
}

if ($Anotar) {
  if (-not $vivo) { $vivo = & sqlite3 $Base "SELECT id FROM turno ORDER BY id DESC LIMIT 1;" }
  if (-not $vivo) {
    Write-Output "TURNO"
    Write-Output "VEREDICTO: falla"
    Write-Output "MOTIVO: no hay turno abierto; se abre con -Abrir antes de anotar"
    exit 0
  }
  Q "UPDATE turno SET dijo = COALESCE(dijo,'') || ' | ' || $(Esc $Anotar), entradas = entradas + 1, filas_despues = $filas WHERE id = $vivo;" | Out-Null
  Write-Output "TURNO"
  Write-Output "Anotado en turno $vivo | Entradas: $(Q "SELECT entradas FROM turno WHERE id = $vivo;")"
  Write-Output ""
  Write-Output "VEREDICTO: pasa"
  exit 0
}

if ($Cerrar) {
  if (-not $vivo) {
    Write-Output "TURNO"
    Write-Output "VEREDICTO: indeterminado"
    Write-Output "MOTIVO: no hay turno abierto"
    exit 0
  }
  $antes = [int](Q "SELECT filas_antes FROM turno WHERE id = $vivo;")
  $crecio = $filas - $antes
  if ($Entradas -ge 0) { Q "UPDATE turno SET entradas = $Entradas WHERE id = $vivo;" | Out-Null }
  Q "UPDATE turno SET cerrado = datetime('now','localtime'), filas_despues = $filas WHERE id = $vivo;" | Out-Null
  Write-Output "TURNO"
  Write-Output "Cerrado: $vivo | Filas crecidas: $crecio"
  Write-Output ""
  Write-Output "VEREDICTO: $(if ($crecio -gt 0) { 'pasa' } else { 'falla' })"
  Write-Output ""
  if ($crecio -le 0) {
    Write-Output "MOTIVO: el turno cerró sin dejar entrada en la memoria"
  }
  Write-Output "INDETERMINADO"
  Write-Output "(turno no juzga si lo anotado es valido: eso lo decide el aplanado)"
  exit 0
}

# veredicto del turno abierto, o del último cerrado
if ($vivo) {
  $antes = [int](Q "SELECT filas_antes FROM turno WHERE id = $vivo;")
  $ent = [int](Q "SELECT entradas FROM turno WHERE id = $vivo;")
  $crecio = $filas - $antes
  Write-Output "TURNO"
  Write-Output "Abierto: $vivo | Entradas: $ent | Filas crecidas: $crecio"
  Write-Output ""
  Write-Output "VEREDICTO: $(if ($crecio -gt 0) { 'pasa' } else { 'falla' })"
  Write-Output ""
  if ($crecio -le 0) { Write-Output "MOTIVO: el turno esta abierto y no ha dejado entrada" }
} else {
  $ult = Q "SELECT id FROM turno WHERE cerrado IS NOT NULL ORDER BY id DESC LIMIT 1;"
  if (-not $ult) {
    Write-Output "TURNO"
    Write-Output "VEREDICTO: indeterminado"
    Write-Output "MOTIVO: no hay turno abierto ni cerrado"
    exit 0
  }
  $crecio = [int](Q "SELECT filas_despues - filas_antes FROM turno WHERE id = $ult;")
  Write-Output "TURNO"
  Write-Output "Ultimo cerrado: $ult | Filas crecidas: $crecio"
  Write-Output ""
  Write-Output "VEREDICTO: $(if ($crecio -gt 0) { 'pasa' } else { 'falla' })"
}

Write-Output ""
Write-Output "INDETERMINADO"
Write-Output "(turno no juzga si lo anotado es valido: eso lo decide el aplanado)"
