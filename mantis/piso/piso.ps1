# piso.ps1 — el tren de esta instancia
# Decide: si una unidad EXISTE, y solo despues si pasa su propia medicion.
#
# Una unidad sin friccion no existe: aparece. Y lo que aparece sin resistencia es un
# script que se ejecuta por costumbre. Por eso el tren pregunta primero que se le
# resiste a cada unidad, y solo despues corre su check.
#
# Rige ../../Ouroboros/procesos/friccion como fundamento del piso.md, "Las cuatro pruebas de existencia".
# Rige ../../Ouroboros/piso.md, "El tren".
#
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
# Uso: pwsh -File mantis/piso/piso.ps1 [-Root <ruta>] [-Solo <unidad>]

param(
  [string]$Root = (Join-Path $PSScriptRoot "..\.."),
  [string]$Solo
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Las ocho que deciden. Cada una declara las cuatro pruebas de existencia:
#   SeLeResiste  — que la contradice, con nombre
#   Contesta     — quien puede contestarla, y no es el que la produjo
#   SiDeja       — que se pierde si deja de correr, y el sintoma
#   DejaDeValer  — el limite: No se aplica a que
$unidades = @(
  @{ Archivo='inventario.ps1'; SeLeResiste='un proceso que se escribe sin los campos del formato y nadie lo nota';
     Contesta='quien escribe procesos, y quien los lee despues'; SiDeja='73 procesos con forma pero sin campos: el error aparece en la tercera mutacion';
     DejaDeValer='lo que no es proceso: un indice, un borrador, una nota' },
  @{ Archivo='rutas.ps1'; SeLeResiste='una ruta relativa que apunta a un archivo que se movio';
     Contesta='quien mueve el archivo, y quien lo cita'; SiDeja='abre el archivo, resuelve a nada, y nadie sabe desde cuando';
     DejaDeValer='rutas externas, plantillas con [corchete] y enlaces de era' },
  @{ Archivo='fantasmas.ps1'; SeLeResiste='un ente al que le falta rastro, ruta o carga';
     Contesta='quien carga el ente, y quien lo hereda'; SiDeja='un ente sin cuerpo se lee como ente completo';
     DejaDeValer='carpetas sin ninguna de las tres: no son entes' },
  @{ Archivo='notas.ps1'; SeLeResiste='una decision tomada que no dejo fila en la memoria';
     Contesta='quien retoma el turno sin poder preguntar'; SiDeja='la memoria se llena por reclamo y no por proceso';
     DejaDeValer='el contenido de la fila: eso lo decide el aplanado' },
  @{ Archivo='turno.ps1'; SeLeResiste='un turno que cierra sin dejar entrada';
     Contesta='quien abre el turno siguiente'; SiDeja='el turno se cierra sin rastro y la siguiente instancia arranca a ciegas';
     DejaDeValer='abrir el turno: eso lo decide quien lo empieza' },
  @{ Archivo='privacidad.ps1'; SeLeResiste='un archivo del repo que expone la maquina de una persona';
     Contesta='quien va a publicar el repo'; SiDeja='una ruta personal sale a la luz en el primer push';
     DejaDeValer='archivos ignorados por git, y la firma de autor de CITATION.cff' },
  @{ Archivo='trazabilidad.ps1'; SeLeResiste='una referencia nombrada sin su archivo, o con un campo vacio';
     Contesta='quien lee la tesis y quiere saber de donde viene'; SiDeja='una idea discutida en conversacion se pierde cuando el contexto se llena';
     DejaDeValer='los momentos, que son prosa sin forma fija; y los archivos que empiezan con _' },
  @{ Archivo='quien.ps1'; SeLeResiste='un cambio que toca una zona y no la que la sostiene';
     Contesta='la autoridad, que sabe de quien es cada cosa'; SiDeja='nadie sabe de quien es el cambio ni que zona se movio';
     DejaDeValer='la intencion; se declara en el pase' }
)

if ($Solo) { $unidades = @($unidades | Where-Object { $_.Archivo -eq $Solo }); if ($unidades.Count -eq 0) { throw "No hay unidad con archivo $Solo." } }

$filas = @()
foreach ($u in $unidades) {
  $script = Join-Path $PSScriptRoot $u.Archivo

  # 1. Las cuatro pruebas de existencia. Sin ellas no se corre: aparece.
  $faltan = @()
  foreach ($k in @('SeLeResiste','Contesta','SiDeja','DejaDeValer')) {
    if ([string]::IsNullOrWhiteSpace($u[$k])) { $faltan += $k }
  }
  if ($faltan.Count -gt 0) {
    $filas += [pscustomobject]@{ Unidad=$u.Archivo; Existe='no'; Veredicto='aparece'; PruebaFalta=($faltan -join ',') }
    continue
  }

  if (-not (Test-Path $script)) {
    $filas += [pscustomobject]@{ Unidad=$u.Archivo; Existe='si'; Veredicto='no corre'; PruebaFalta='-' }
    continue
  }

  # 2. Solo si existe, se corre su medicion.
  $lineas = & pwsh -NoProfile -File $script -Root $Root 2>&1
  $veredicto = 'indeterminado'
  foreach ($l in $lineas) { if ($l -match '^VEREDICTO:\s*(\w+)') { $veredicto = $Matches[1]; break } }
  $filas += [pscustomobject]@{ Unidad=$u.Archivo; Existe='si'; Veredicto=$veredicto; PruebaFalta='-' }
}

$aparecen = @($filas | Where-Object { $_.Existe -ne 'si' })
$existen = @($filas | Where-Object { $_.Existe -eq 'si' })
$falla = @($existen | Where-Object { $_.Veredicto -ne 'pasa' })
$enPasa = @($existen | Where-Object { $_.Veredicto -eq 'pasa' }).Count

Write-Output "PISO"
Write-Output "Root: $Root"
Write-Output ""
Write-Output "UNIDAD | EXISTE | VEREDICTO"
foreach ($f in $filas) {
  $ex = if ($f.Existe -eq 'si') { 'si' } else { 'no' }
  Write-Output "$($f.Unidad) | $ex | $($f.Veredicto)"
}
Write-Output ""
Write-Output "Existen: $($existen.Count) de $($filas.Count) | pasan: $enPasa"
if ($aparecen.Count -gt 0) { Write-Output "Aparecen sin existir: $($aparecen.Count) ($(($aparecen | ForEach-Object { $_.Unidad }) -join ', '))" }
Write-Output ""

# El piso falla si una unidad no existe, o si existe y no pasa.
$veredicto = if ($aparecen.Count -eq 0 -and $falla.Count -eq 0) { 'pasa' } else { 'falla' }
Write-Output "VEREDICTO: $veredicto"
Write-Output ""

if ($falla.Count -gt 0) {
  Write-Output "FALLA EN"
  foreach ($f in $falla) { Write-Output "$($f.Unidad) | $($f.Veredicto)" }
  Write-Output ""
}
if ($aparecen.Count -gt 0) {
  Write-Output "APARECE SIN EXISTIR"
  foreach ($f in $aparecen) { Write-Output "$($f.Unidad) | falta: $($f.PruebaFalta)" }
  Write-Output ""
}

# El reporte de resistencia: que se le resiste a cada unidad que si existe.
Write-Output "SE LE RESISTE"
foreach ($f in $filas) {
  $u = $unidades | Where-Object { $_.Archivo -eq $f.Unidad } | Select-Object -First 1
  if ($u -and $f.Existe -eq 'si') {
    Write-Output "$($u.Archivo) | se le resiste: $($u.SeLeResiste) | contesta: $($u.Contesta)"
  }
}
Write-Output ""

Write-Output "INDETERMINADO"
Write-Output "(el tren no decide si lo medido sirve: eso es criterio)"
