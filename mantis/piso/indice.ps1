# indice.ps1 — unidad del piso de esta instancia
# Decide: que hay en el repo, donde esta, y que forma tiene.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
# Genera 1 Tesis/indice.md: un indice a mano se desactualiza en la siguiente mutacion.
# Uso: pwsh -File mantis/piso/indice.ps1 [-Root <ruta>] [-Salida <ruta>]

param(
  [string]$Root   = (Join-Path $PSScriptRoot "..\.."),
  [string]$Salida = (Join-Path $PSScriptRoot "..\..\1 Tesis\indice.md")
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

$zonas = [ordered]@{
  '1 Tesis' = 'la tesis: la forma, aun por aplanar en archivos'
  '2 Ouroboros' = 'la tarea: paso 1, paso 2 y paso 3'
  'Era' = 'la era'
  'mantis' = 'instancia: la operacion'
}

function Get-Rol($rel) {
  if ($rel -match '^1 Tesis') { return 'estandar' }
  if ($rel -match '^Era') { return 'era' }
  return 'instancia'
}

function Get-Clase($nombre, $rel) {
  if ($nombre -ieq 'README.md') { return 'puerta' }
  if ($nombre -match '(?i)indice') { return 'indice' }
  if ($nombre -match '(?i)deterrente') { return 'deterrente' }
  if ($nombre -match '(?i)formato') { return 'formato' }
  if ($rel -match '^1 Tesis') { return 'estandar' }
  return 'proceso'
}

$filas = @()
foreach ($z in $zonas.Keys) {
  $base = Join-Path $Root $z
  if (-not (Test-Path $base)) { continue }
  foreach ($a in (Get-ChildItem $base -Filter *.md -File -Recurse -ErrorAction SilentlyContinue | Sort-Object FullName)) {
    $rel = $a.FullName.Replace($Root + '\','').Replace('\','/')
    $dir = ($rel -split '/')[0..(($rel -split '/').Count - 2)] -join '/'
    if ($dir -eq '') { $dir = '(raiz)' }
    $filas += [pscustomobject]@{
      Zona   = $z
      Rol    = Get-Rol $rel
      Carpeta= $dir
      Archivo= $a.Name
      Clase  = Get-Clase $a.Name $rel
      Lineas = (Get-Content $a.FullName -ErrorAction SilentlyContinue).Count
    }
  }
}

$hoy = Get-Date -Format 'yyyy-MM-dd'
$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine('# Indice')
[void]$sb.AppendLine()
[void]$sb.AppendLine('**Unidad:** nivel.')
[void]$sb.AppendLine('**Aplica a:** ubicar.')
[void]$sb.AppendLine('**Tipo:** registro generado. No se edita a mano: se regenera.')
[void]$sb.AppendLine('**Generado por:** `../mantis/piso/indice.ps1`.')
[void]$sb.AppendLine("**Fecha:** $hoy.")
[void]$sb.AppendLine()
[void]$sb.AppendLine('## Que es')
[void]$sb.AppendLine()
[void]$sb.AppendLine('Este archivo existe porque **todo muta y nadie se acuerda donde quedo cada cosa.** Es el indice del repo: que hay, en que zona, y que clase es cada archivo.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('**Un indice escrito a mano se desactualiza en la siguiente mutacion.** Por eso lo genera el piso: si cambio algo y el indice no cambio, el indice miente.')
[void]$sb.AppendLine()
[void]$sb.AppendLine('## Las zonas')
[void]$sb.AppendLine()
[void]$sb.AppendLine('| Zona | Rol | Que es |')
[void]$sb.AppendLine('|---|---|---|')
foreach ($z in $zonas.Keys) {
  $rol = if ($z -eq '1 Tesis') { 'estandar' } elseif ($z -eq 'Era') { 'era' } else { 'instancia' }
  [void]$sb.AppendLine("| ``$z/`` | $rol | $($zonas[$z]) |")
}
[void]$sb.AppendLine()
[void]$sb.AppendLine('## Las clases')
[void]$sb.AppendLine()
[void]$sb.AppendLine('| Clase | Que es |')
[void]$sb.AppendLine('|---|---|')
[void]$sb.AppendLine('| `proceso` | se ejecuta: declara entrada, falla, salida y consumidor |')
[void]$sb.AppendLine('| `estandar` | dice como tiene que ser algo |')
[void]$sb.AppendLine('| `deterrente` | dice que pasa si el nivel se viola |')
[void]$sb.AppendLine('| `formato` | dice que forma tiene lo que un ejecutor lee |')
[void]$sb.AppendLine('| `puerta` | `README`: abre una zona o una sub-tarea |')
[void]$sb.AppendLine('| `indice` | este archivo y sus semejantes |')
[void]$sb.AppendLine()
[void]$sb.AppendLine('## El arbol')
[void]$sb.AppendLine()

foreach ($z in $zonas.Keys) {
  $del = $filas | Where-Object { $_.Zona -eq $z }
  if (-not $del) { continue }
  [void]$sb.AppendLine("### $z/")
  [void]$sb.AppendLine()
  [void]$sb.AppendLine('| Carpeta | Archivo | Clase | Lineas |')
  [void]$sb.AppendLine('|---|---|---|---|')
  foreach ($f in ($del | Sort-Object Carpeta, Archivo)) {
    [void]$sb.AppendLine("| ``$($f.Carpeta)`` | ``$($f.Archivo)`` | $($f.Clase) | $($f.Lineas) |")
  }
  [void]$sb.AppendLine()
}

$tot = $filas.Count
$pro = ($filas | Where-Object { $_.Clase -eq 'proceso' }).Count
$est = ($filas | Where-Object { $_.Clase -eq 'estandar' }).Count
[void]$sb.AppendLine('## Totales')
[void]$sb.AppendLine()
[void]$sb.AppendLine("``Archivos: $tot | procesos: $pro | estandares: $est``")
[void]$sb.AppendLine()
[void]$sb.AppendLine('## Prueba')
[void]$sb.AppendLine()
[void]$sb.AppendLine('¿Cada archivo del repo aparece? ¿Su clase es la que dice su forma? ¿El indice se regenero despues del ultimo cambio?')
[void]$sb.AppendLine()
[void]$sb.AppendLine('**Falsificador:** un archivo sin clase; un indice que no se regenera tras una mutacion; una zona sin rol.')

Set-Content $Salida $sb.ToString() -NoNewline -Encoding utf8

$sinClase = ($filas | Where-Object { -not $_.Clase }).Count
Write-Output "INDICE"
Write-Output "Salida: $Salida"
Write-Output "Archivos: $tot | procesos: $pro | estandares: $est | sin clase: $sinClase"
Write-Output ""
Write-Output "VEREDICTO: $(if ($sinClase -eq 0) { 'pasa' } else { 'falla' })"
