# privacidad.ps1 — unidad del piso de esta instancia
# Decide: si un archivo versionado del repositorio expone la maquina de una persona.
#
# Que no es: no decide si un ejemplo didactico es peligroso. Eso lo decide quien lee.
# No se aplica a: archivos ignorados por git (viven solo en la maquina del autor), y a
#                 rutas relativas del repo, que no dicen nada de una maquina personal.
# No usa modelo. Corre igual en cualquier ejecutor.
#
# FORMA: no se inventa aqui. Se lee de ../../Ouroboros/piso.md, "Se nombra por lo que decide".
# Uso: pwsh -File mantis/piso/privacidad.ps1 [-Root <ruta>]

param([string]$Root = (Join-Path $PSScriptRoot "..\.."))

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path

# Solo lo versionado. Una ruta personal en un archivo ignorado no sale del repo.
$versionados = @()
try {
  $null = & git -C $Root rev-parse --is-inside-work-tree 2>$null
  if ($LASTEXITCODE -eq 0) {
    $versionados = & git -C $Root ls-files 2>$null
  }
} catch { }

if (-not $versionados -or $versionados.Count -eq 0) {
  Write-Output "PRIVACIDAD"
  Write-Output "Root: $Root"
  Write-Output ""
  Write-Output "VEREDICTO: indeterminado"
  Write-Output ""
  Write-Output "MOTIVO: la unidad no pudo leer la lista de archivos versionados (no hay git o no hay repo)"
  exit 0
}

# Lo que dice donde vive una persona. Un patron, un caso.
$patrones = @(
  @{ Nombre = 'ruta de usuario';   Regex = '(?i)([A-Za-z]:[\\/]+)?Users[\\/]+[A-Za-z0-9._-]+' },
  @{ Nombre = 'directorio temporal'; Regex = '(?i)AppData[\\/]+(Local|Roaming)' },
  @{ Nombre = 'ruta de disco';     Regex = '(?i)\b[A-Za-z]:\\(Users|Documents|Desktop|Downloads)\b' },
  @{ Nombre = 'correo';            Regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' }
)

# Falsos positivos aceptados y declarados: el correo del git config de un ejemplo,
# y la direccion de ejemplo de una documentacion. Se listan, no se adivinan.
$permitidos = @(
  'example@example.com',
  'someone@example.com',
  'user@example.com',
  'mailto:'
)

# AUTORIA DECLARADA: la autoridad decide que su firma de autor es publica a proposito.
# Un CITATION.cff dice quien escribio el trabajo y como se le contacta: eso es el trabajo,
# no el disco. Lo que sigue protegido en el es la maquina: rutas, temporales y cuentas.
# Cualquier otro archivo queda sujeto a todos los patrones sin excepcion.
$autoriaPublica = @('CITATION.cff')

$hallazgos = @()
$mirados = 0

foreach ($rel in $versionados) {
  $rel = $rel.Trim()
  if (-not $rel) { continue }
  # Solo texto: un binario no se escanea con regex.
  if ($rel -match '\.(png|jpe?g|gif|webp|ico|pdf|zip|gz|exe|dll|woff2?|ttf|otf|db|sqlite)$') { continue }
  $abs = Join-Path $Root $rel
  if (-not (Test-Path -LiteralPath $abs)) { continue }
  $mirados++
  $relNorm = $rel.Replace('\', '/')
  # En un archivo de autoria publica, el correo y el nombre son la firma: no se busca rutas de otra persona ahi,
  # pero la maquina sigue sujeta. El correo se deja pasar; las rutas y los temporales no.
  $esAutoria = $false
  foreach ($a in $autoriaPublica) { if ($relNorm -eq $a) { $esAutoria = $true } }
  try {
    $txt = Get-Content -LiteralPath $abs -Raw -Encoding utf8 -ErrorAction Stop
  } catch { continue }
  if (-not $txt) { continue }
  $lineas = $txt -split "`r?`n"
  for ($i = 0; $i -lt $lineas.Count; $i++) {
    $linea = $lineas[$i]
    foreach ($pat in $patrones) {
      if ($esAutoria -and $pat.Nombre -eq 'correo') { continue }
      foreach ($m in ([regex]::Matches($linea, $pat.Regex))) {
        $valor = $m.Value
        $skip = $false
        foreach ($p in $permitidos) { if ($valor -like "*$p*" -or $linea -like "*$p*") { $skip = $true } }
        if ($skip) { continue }
        $hallazgos += [pscustomobject]@{
          Archivo = $relNorm
          Linea   = $i + 1
          Que     = $pat.Nombre
          Valor   = $valor
        }
      }
    }
  }
}

Write-Output "PRIVACIDAD"
Write-Output "Root: $Root"
Write-Output "Archivos versionados leidos: $mirados | hallazgos: $($hallazgos.Count)"
Write-Output ""

$unico = @($hallazgos | Sort-Object Archivo, Linea, Que -Unique)

if ($unico.Count -eq 0) {
  Write-Output "VEREDICTO: pasa"
} else {
  Write-Output "VEREDICTO: falla"
}
Write-Output ""

if ($unico.Count -gt 0) {
  Write-Output "ARCHIVO | LINEA | QUE | VALOR"
  foreach ($h in $unico) { Write-Output "$($h.Archivo) | $($h.Linea) | $($h.Que) | $($h.Valor)" }
  Write-Output ""
}

Write-Output "INDETERMINADO"
Write-Output "(privacidad no juzga si un ejemplo publicado expone a alguien: eso lo decide quien lo publica)"
