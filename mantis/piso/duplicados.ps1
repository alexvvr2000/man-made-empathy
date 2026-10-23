# duplicados.ps1 — unidad del piso de esta instancia
# Decide: donde hay dos piezas para el mismo nombre.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# DUPLICADO: el mismo nombre de archivo en dos entes, o el mismo titulo H1 en dos archivos.
# Un nombre que sirve para dos cosas no nombra nada. Rige ../../Ouroboros/mutacion.md.
#
# Uso: pwsh -File mantis/piso/duplicados.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

$zonas = @('Tesis', 'Ouroboros', 'mantis')
$archivos = @()
foreach ($z in $zonas) {
  $base = Join-Path $Root $z
  if (-not (Test-Path $base)) { continue }
  $archivos += Get-ChildItem $base -Recurse -Filter *.md
}

# 1. Nombres de archivo que se repiten fuera de su ente.
# Un README.md por sub-tarea es legitimo; una carta.md en dos pasos no.
$porNombre = $archivos | Group-Object Name | Where-Object { $_.Count -gt 1 }
$nombres = @()
foreach ($g in $porNombre) {
  $padres = $g.Group | ForEach-Object { (Split-Path (Split-Path $_.FullName -Parent) -Leaf) } | Sort-Object -Unique
  # Las tres piezas del ente se repiten a proposito: rastro, ruta y carga son el mismo nombre en cada ente.
  # El README de sub-tarea tambien: es la puerta de cada una.
  if ($g.Name -in @('README.md','rastro.md','ruta.md','carga.md')) { continue }
  # Dos carpetas hermanas de la misma parte son dos lectores del mismo texto:
  # la fuente de la tesis y su corte publicable comparten nombre a proposito.
  $padre = @($g.Group | ForEach-Object { Split-Path (Split-Path $_.FullName -Parent) -Leaf } | Sort-Object -Unique)
  if ($padre.Count -le 1) { continue }
  # Un nombre en la tesis y en el estandar es explicacion contra forma: se declara, no se corrige.
  $zonas = @($g.Group | ForEach-Object { ($_.FullName.Replace($Root + '\', '') -split '\\')[0] } | Sort-Object -Unique)
  if ($zonas -contains 'Tesis' -and $zonas -contains 'Ouroboros') { continue }
  $nombres += [pscustomobject]@{ Tipo = 'nombre'; Nombre = $g.Name; Veces = $g.Count; Donde = (($g.Group | ForEach-Object { $_.FullName.Replace($Root + '\', '').Replace('\', '/') }) -join ' · ') }
}

# 2. Titulo H1 que se repite: dos archivos que dicen ser la misma pieza.
$titulos = @()
foreach ($f in $archivos) {
  $txt = Get-Content $f.FullName -Raw -Encoding utf8
  $m = [regex]::Match($txt, '(?m)^#\s+(.+?)\s*$')
  if (-not $m.Success) { continue }
  $titulos += [pscustomobject]@{ Titulo = $m.Groups[1].Value.Trim(); Ruta = $f.FullName.Replace($Root + '\', '').Replace('\', '/') }
}
$porTitulo = $titulos | Group-Object Titulo | Where-Object { $_.Count -gt 1 }
  $porTitulo = @($porTitulo | Where-Object { $g2 = $_; -not (($g2.Group | Where-Object { $_.Ruta -match '^1 Tesis/' }) -and ($g2.Group | Where-Object { $_.Ruta -match '^Ouroboros/' })) })
  # Dos carpetas hermanas de la misma parte: la fuente y su corte declaran el mismo titulo.
  $porTitulo = @($porTitulo | Where-Object { $g3 = $_; $dirs = @($g3.Group | ForEach-Object { $_.Ruta.Substring(0, $_.Ruta.LastIndexOf('/')) } | Sort-Object -Unique); $dirs.Count -gt 1 })
  # Un titulo repetido entre la tesis y el estandar camina el mismo puente: el estandar ejecuta, la tesis explica.
  $porTitulo = @($porTitulo | Where-Object { -not (($_.Group.FullName -match '\\Tesis\\') -and ($_.Group.FullName -match '\\Ouroboros\\')) })
foreach ($g in $porTitulo) {
  $nombres += [pscustomobject]@{ Tipo = 'titulo'; Nombre = $g.Name; Veces = $g.Count; Donde = (($g.Group | ForEach-Object { $_.Ruta }) -join ' · ') }
}

Write-Output "DUPLICADOS"
Write-Output "Root: $Root"
Write-Output "Archivos: $($archivos.Count) | duplicados: $($nombres.Count)"
Write-Output ""
Write-Output "VEREDICTO: $(if ($nombres.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($nombres.Count -gt 0) {
  Write-Output "TIPO | NOMBRE | VECES | DÓNDE"
  foreach ($n in ($nombres | Sort-Object Tipo, Nombre)) { Write-Output "$($n.Tipo) | $($n.Nombre) | $($n.Veces) | $($n.Donde)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(duplicados no juzga si el nombre repetido es legitimo: eso lo declara Reemplaza:)"