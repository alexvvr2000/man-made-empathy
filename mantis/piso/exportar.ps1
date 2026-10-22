# exportar.ps1 — unidad del piso de esta instancia
# Decide: si el export publicado coincide con lo que hay en la base.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# La base es el acelerador; el export es la fuente. Rige ../mantis/mantenimiento/notas/notas-tesis.md.
# Base: .sesion-continua/tesis.db (oculta). Publicado: notas/actuales.md
#
# No se aplica a: lo que vive solo en la sesion (continuas.md), ni a las generaciones.
#
# Uso: pwsh -File mantis/piso/exportar.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Base = Join-Path $Root '.sesion-continua\tesis.db'
$Salida = Join-Path $Root 'notas\actuales.md'

if (-not (Test-Path $Base)) {
  Write-Output "EXPORTAR"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no existe .db/notas.db"
  exit 0
}

function Q($sql) { & sqlite3 -separator ' | ' $Base $sql }

$cabecera = @'
# Notas

**Unidad:** registro.
**Aplica a:** recordar.
**Tipo:** memoria de la conversación. No decide, no ejecuta: guarda lo que se dijo, para que no se pierda con el contexto.
**Lector:** quien va a compilar la tesis, y quien va a defenderla mañana.
**Dueño:** la autoridad.
**Estado:** vigente.
**Base:** `.db/notas.db`, tabla `fila`. **Este archivo es su export, no se edita a mano.**
'@

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine($cabecera)

# El bloque de la sesión.
$s = Q "SELECT fecha,vista,estado,roto,abierto,siguiente,decidido,rige FROM sesion WHERE id = 1;"
if ($s) {
  $f = $s -split ' \| '
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('## La sesión')
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('```')
  [void]$sb.AppendLine("Sesión: $($f[0]) | Vista: $($f[1])")
  [void]$sb.AppendLine("Estado: $($f[2]) | Roto: $($f[3])")
  [void]$sb.AppendLine("Abierto: $($f[4])")
  [void]$sb.AppendLine("Siguiente: $($f[5])")
  [void]$sb.AppendLine("Decidido: $($f[6])")
  [void]$sb.AppendLine("Rige: $($f[7])")
  [void]$sb.AppendLine('```')
}

# Las secciones, en orden, con sus filas.
$secciones = Q "SELECT nombre FROM seccion ORDER BY orden;"
$total = 0
foreach ($sec in $secciones) {
  $filas = & sqlite3 -separator ' | ' $Base "SELECT dicho,pieza,tipo,usa,sostenido,estado,vista FROM fila WHERE seccion = '$(($sec -replace "'","''"))' ORDER BY id;"
  if (-not $filas) { continue }
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine("## $sec")
  [void]$sb.AppendLine('')
  [void]$sb.AppendLine('| Dicho | De | Tipo | Usa | Sostenido | Estado | Vista |')
  [void]$sb.AppendLine('|---|---|---|---|---|---|---|')
  foreach ($f in $filas) { [void]$sb.AppendLine("| $f |"); $total++ }
}

$g = & sqlite3 $Base "SELECT COUNT(*) FROM generacion;"
[void]$sb.AppendLine('')
[void]$sb.AppendLine('## Prueba')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('¿Cada fila de la base aparece en el export? ¿Cada fila nombra su pieza y su vista? ¿El bloque de la sesión es el último medido?')
[void]$sb.AppendLine('')
[void]$sb.AppendLine('**Falsificador:** una fila en la base que no está en el export; un export editado a mano; un bloque de sesión escrito de memoria.')

[System.IO.File]::WriteAllText($Salida, $sb.ToString())

# Verificar: el export tiene tantas filas como la base.
$enBase = [int](& sqlite3 $Base "SELECT COUNT(*) FROM fila;")
Write-Output "EXPORTAR"
Write-Output "Base: $Base"
Write-Output "Salida: notas/actuales.md"
Write-Output "Filas: $total exportadas | $enBase en la base | generaciones: $g"
Write-Output ""
Write-Output "VEREDICTO: $(if ($total -eq $enBase -and $enBase -gt 0) { 'pasa' } else { 'falla' })"
Write-Output ""
Write-Output "INDETERMINADO"
Write-Output "(exportar no juzga si lo anotado es válido: eso es criterio)"
