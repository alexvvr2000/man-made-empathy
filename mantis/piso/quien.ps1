#!/usr/bin/env pwsh
# quien.ps1 — unidad del piso de esta instancia
# Decide: a quien pertenece un cambio, y si cambio algo que deberia haber cambiado.
#
# Que no es: no decide si el cambio sirve. Eso lo decide quien lee.
# No se aplica a: archivos que no estan en ninguna zona declarada (son raiz, no son de nadie).
# No usa modelo. Corre igual en cualquier ejecutor.
#
# FORMA: no se inventa aqui. Se lee de Ouroboros/piso.md, "Se nombra por lo que decide".
# Uso: pwsh -File mantis/piso/quien.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Las zonas, y a quien pertenece cada una. Es la diferencia que la autoridad pidio ver.
$zonas = [ordered]@{
  'futuro'     = 'repo — el instrumento que se comparte'
  'mantis'     = 'MANTIS — la tarea que decide y edita'
  'VIDERE'     = 'VIDERE — el ente que testifica'
  'Tesis'      = 'autoridad — lo que la autoridad trae y firma'
  'Ouroboros'  = 'estandar — fuera del repo, vive en MEGA/mme'
  'Pruebas'    = 'prueba — lo que mide si sirve'
  'notas'      = 'memoria — la corrida de la base'
}

# Un cambio es de una zona si su ruta empieza por ella.
function Get-Zona($rel) {
  foreach ($z in $zonas.Keys) { if ($rel -like "$z/*" -or $rel -like "$z\*") { return $z } }
  return 'raiz'
}

$versionados = @()
try {
  $null = & git -C $Root rev-parse --is-inside-work-tree 2>$null
  if ($LASTEXITCODE -eq 0) { $versionados = & git -C $Root ls-files 2>$null }
} catch { }
if (-not $versionados -or $versionados.Count -eq 0) {
  Write-Output "QUIEN"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no se pudo leer git ls-files"
  exit 0
}

# Lo que cambio: working tree contra HEAD, mas lo no versionado.
$cambiados = @()
try { $cambiados = & git -C $Root status --porcelain 2>$null } catch { }

$porZona = @{}
foreach ($z in $zonas.Keys) { $porZona[$z] = 0 }
$porZona['raiz'] = 0
foreach ($v in $versionados) { $z = Get-Zona $v.Replace('\','/'); $porZona[$z]++ }

$tocados = @{}
foreach ($c in $cambiados) {
  if (-not $c -or $c.Length -lt 4) { continue }
  $ruta = $c.Substring(3).Trim().Trim('"').Replace('\','/')
  if ($ruta -match ' -> ') { $ruta = ($ruta -split ' -> ')[1] }
  $z = Get-Zona $ruta
  if (-not $tocados[$z]) { $tocados[$z] = @() }
  $tocados[$z] += $ruta
}

Write-Output "QUIEN"
Write-Output "Root: $Root"
Write-Output ""
Write-Output "ZONA | DE QUIEN ES | ARCHIVOS | TOCADOS EN ESTE TURNO"
foreach ($z in $zonas.Keys) {
  $n = $porZona[$z]
  $t = if ($tocados[$z]) { $tocados[$z].Count } else { 0 }
  Write-Output "$z | $($zonas[$z]) | $n | $t"
}
Write-Output "raiz | nadie — la carta, la licencia y el readme | $($porZona['raiz']) | $(if ($tocados['raiz']) { $tocados['raiz'].Count } else { 0 })"
Write-Output ""

# La regla: un cambio que toca una zona y no la que la sostiene, se declara.
$hechos = @()
foreach ($z in $tocados.Keys) { $hechos += "$z" }
Write-Output "TOCADO: $(if ($hechos.Count -eq 0) { 'nada' } else { ($hechos -join ', ') })"
Write-Output ""
Write-Output "VEREDICTO: pasa"
Write-Output ""
Write-Output "INDETERMINADO"
Write-Output "(quien no juzga si el cambio sirve: eso lo decide quien lee el pase)"
