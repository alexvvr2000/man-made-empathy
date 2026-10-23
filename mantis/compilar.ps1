# compilar.ps1 — compila la tesis a LaTeX, y a PDF si hay motor
# Decide: si cada paper de Tesis/ se puede emitir como documento formal.
# No juzga contenido. No usa modelo. Corre igual en cualquier ejecutor.
#
# Genera el .tex SIN depender de pandoc: el conversor vive aqui y trata el
# subconjunto de Markdown que usa la tesis. Si hay motor LaTeX, ademas compila
# a PDF; si no lo hay, lo declara y no lo finge.
#
# Dos fuentes de documentos:
#   Tesis/<parte>/paper.md                    el paper y sus fuentes
#   Tesis/publicable/manifiesto.txt           la carpeta publicable: una fila por
#                                             documento (archivo | titulo). El
#                                             manifiesto manda: lo que no esta en
#                                             el no se compila; lo que esta y no
#                                             resuelve se declara y falla.
#
# Rige ./mantenimiento/editar/editar.md, paso 11.
# Uso:
#   pwsh -File mantis/compilar.ps1
#   pwsh -File mantis/compilar.ps1 -Solo Tesis/idea
#   pwsh -File mantis/compilar.ps1 -Solo Tesis/publicable
#   pwsh -File mantis/compilar.ps1 -Salida dist

param(
  [string]$Root = (Join-Path $PSScriptRoot ".."),
  [string]$Solo = '',
  [string]$Salida = 'dist'
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path $Root).Path
$Destino = Join-Path $Root $Salida

# ---------------------------------------------------------------
# 1. Buscar los papers: Tesis/<parte>/paper.md y el manifiesto publicable
# ---------------------------------------------------------------
$papers = @()
$manifiesto = ''
if ($Solo) {
  $base = Join-Path $Root $Solo
  if (Test-Path (Join-Path $base 'paper.md')) { $papers += (Join-Path $base 'paper.md') }
  if (Test-Path (Join-Path $base 'manifiesto.txt')) { $manifiesto = Join-Path $base 'manifiesto.txt' }
} else {
  $papers = @(Get-ChildItem (Join-Path $Root 'Tesis') -Recurse -Filter 'paper.md' -File | Select-Object -ExpandProperty FullName)
  $m = Join-Path $Root 'Tesis\publicable\manifiesto.txt'
  if (Test-Path $m) { $manifiesto = $m }
}

if ($papers.Count -eq 0 -and -not $manifiesto) {
  Write-Output "COMPILAR"
  Write-Output "VEREDICTO: indeterminado"
  Write-Output "MOTIVO: no hay Tesis/*/paper.md ni Tesis/publicable/manifiesto.txt que compilar"
  exit 0
}

# ---------------------------------------------------------------
# 2. El conversor. Subconjunto de Markdown -> LaTeX.
# ---------------------------------------------------------------
function Esc-Tex($s) {
  if ($null -eq $s) { return '' }
  $s = $s -replace '\\', '\textbackslash{}'
  $s = $s -replace '&', '\&'
  $s = $s -replace '%', '\%'
  $s = $s -replace '\$', '\$'
  $s = $s -replace '#', '\#'
  $s = $s -replace '_', '\_'
  $s = $s -replace '\{', '\{'
  $s = $s -replace '\}', '\}'
  $s = $s -replace '~', '\textasciitilde{}'
  $s = $s -replace '\^', '\textasciicircum{}'
  # fuera de T1: se pasan a matematicas, despues del escape para que el $ no se escape
  $s = $s.Replace([string][char]0x2260, '$\neq$').Replace([string][char]0x2192, '$\rightarrow$')
  $s = $s.Replace([string][char]0x2265, '$\geq$').Replace([string][char]0x2264, '$\leq$')
  return $s
}

function Convert-Inline($s) {
  $code = @{}
  $links = @{}
  $i = 0
  # 1. codigo en linea, a marcador
  $s = [regex]::Replace($s, '`([^`]+)`', {
    param($m)
    $script:ci++
    $key = [char]1 + $script:ci.ToString() + [char]2
    $script:codes[$key] = $m.Groups[1].Value
    return $key
  })
  # 2. enlaces, a marcador
  $s = [regex]::Replace($s, '\[([^\]]+)\]\(([^)]+)\)', {
    param($m)
    $script:li++
    $key = [char]1 + 'L' + $script:li.ToString() + [char]2
    $script:lnks[$key] = @($m.Groups[1].Value, $m.Groups[2].Value)
    return $key
  })
  # 3. escapar el resto
  $s = Esc-Tex $s
  # 4. negrita y cursiva
  $s = [regex]::Replace($s, '\*\*([^*]+)\*\*', '\textbf{$1}')
  $s = [regex]::Replace($s, '(?<!\*)\*([^*]+)\*(?!\*)', '\emph{$1}')
  # 5. restaurar codigo y enlaces
  foreach ($k in $script:codes.Keys) {
    $s = $s.Replace($k, '\texttt{' + (Esc-Tex $script:codes[$k]) + '}')
  }
  foreach ($k in $script:lnks.Keys) {
    $t = Esc-Tex $script:lnks[$k][0]
    $u = $script:lnks[$k][1] -replace '\\', '/'
    $s = $s.Replace($k, '\href{' + $u + '}{' + $t + '}')
  }
  return $s
}

function Convert-Md($texto) {
  $script:ci = 0; $script:li = 0
  $script:codes = @{}; $script:lnks = @{}
  $script:sb = New-Object System.Text.StringBuilder
  $script:lista = ''
  $script:enCita = $false

  $lineas = ($texto -replace "`r`n", "`n").Split("`n")
  # la cabecera del repo no va al documento: se empieza en el primer '##'
  $ini = 0
  for ($j = 0; $j -lt $lineas.Count; $j++) { if ($lineas[$j] -match '^##\s') { $ini = $j; break } }
  if ($ini -gt 0) { $lineas = $lineas[$ini..($lineas.Count - 1)] }
  $enCodigo = $false
  $enTabla = $false
  $nCols = 0
  $primerH1 = $true

  function Cerrar-Lista {
    if ($script:lista -ne '') {
      Add-Linea ("\end{$($script:lista)}")
      $script:lista = ''
    }
  }
  function Cerrar-Cita {
    if ($script:enCita) {
      Add-Linea ('\end{quote}')
      $script:enCita = $false
    }
  }
  function Add-Linea($x) { [void]$script:sb.AppendLine($x) }

  for ($i = 0; $i -lt $lineas.Count; $i++) {
    $l = $lineas[$i].TrimEnd()

    # bloque de codigo
    if ($l -match '^\s*```') {
      if (-not $enCodigo) {
        Cerrar-Lista; Cerrar-Cita
        Add-Linea ('\begin{verbatim}')
        $enCodigo = $true
      } else {
        Add-Linea ('\end{verbatim}')
        $enCodigo = $false
      }
      continue
    }
    if ($enCodigo) { Add-Linea ($l); continue }

    # tabla
    if ($l -match '^\s*\|') {
      $celdas = @(($l.Trim().Trim('|') -replace '\\\|', [char]3).Split('|') | ForEach-Object { ($_ -replace [char]3, '\|').Trim() })
      if (-not $enTabla) {
        Cerrar-Lista; Cerrar-Cita
        $nCols = $celdas.Count
        $espec = '@{}' + ('*{' + $nCols + '}{>{\raggedright\arraybackslash}p{\dimexpr(\textwidth-\tabcolsep*2*' + $nCols + ')/' + $nCols + '\relax}}') + '@{}'
        Add-Linea ('\begin{longtable}{' + $espec + '}')
        Add-Linea ('\toprule')
        Add-Linea ((($celdas | ForEach-Object { Convert-Inline $_ }) -join ' & ') + ' \\')
        Add-Linea ('\midrule')
        Add-Linea ('\endhead')
        $enTabla = $true
        continue
      }
      # fila separadora
      if ($l -match '^\s*\|[\s\-:|]+\|\s*$') { continue }
      if ($celdas.Count -eq 0) { continue }
      Add-Linea ((($celdas | ForEach-Object { Convert-Inline $_ }) -join ' & ') + ' \\')
      continue
    } elseif ($enTabla) {
      Add-Linea ('\bottomrule')
      Add-Linea ('\end{longtable}')
      Add-Linea ('')
      $enTabla = $false
    }

    # titulos
    if ($l -match '^(#{1,4})\s+(.*)$') {
      Cerrar-Lista; Cerrar-Cita
      $nivel = $Matches[1].Length
      $t = Convert-Inline ($Matches[2] -replace '^\d+(\.\d+)*\.?\s+', '')
      if ($nivel -eq 1) {
        if ($primerH1) { $primerH1 = $false; continue }  # el H1 es el titulo del documento
        Add-Linea ('\section*{' + $t + '}')
      } elseif ($nivel -eq 2) {
        # los titulos que no son cuerpo numerado no gastan numero: el texto cita 'seccion 6'
        if ($t -match '^(Resumen|Abstract|Palabras clave|Keywords|Declaracion de aporte|Declaración de aporte|Referencias|Prueba|Falsificador|Cómo se lee|Como se lee)$') {
          Add-Linea ('\section*{' + $t + '}')
        } else { Add-Linea ('\section{' + $t + '}') }
      }
      elseif ($nivel -eq 3) { Add-Linea ('\subsection{' + $t + '}') }
      else { Add-Linea ('\subsubsection{' + $t + '}') }
      continue
    }

    # linea vacia
    if ($l -eq '') {
      Cerrar-Lista; Cerrar-Cita
      Add-Linea ('')
      continue
    }

    # cita
    if ($l -match '^\s*>\s?(.*)$') {
      Cerrar-Lista
      if (-not $enCita) { Add-Linea ('\begin{quote}'); $script:enCita = $true }
      Add-Linea ((Convert-Inline $Matches[1]) + '\par')
      continue
    } elseif ($enCita) { Cerrar-Cita }

    # regla
    if ($l -match '^\s*---+\s*$') {
      Cerrar-Lista; Cerrar-Cita
      Add-Linea ('\par\noindent\rule{\textwidth}{0.4pt}\par')
      continue
    }

    # listas
    if ($l -match '^\s*[-*]\s+(.*)$') {
      Cerrar-Cita
      if ($script:lista -ne 'itemize') { Cerrar-Lista; Add-Linea ('\begin{itemize}'); $script:lista = 'itemize' }
      Add-Linea ('\item ' + (Convert-Inline $Matches[1]))
      continue
    }
    if ($l -match '^\s*\d+[.)]\s+(.*)$') {
      Cerrar-Cita
      if ($script:lista -ne 'enumerate') { Cerrar-Lista; Add-Linea ('\begin{enumerate}'); $script:lista = 'enumerate' }
      Add-Linea ('\item ' + (Convert-Inline $Matches[1]))
      continue
    }

    # parrafo
    Cerrar-Lista; Cerrar-Cita
    Add-Linea ((Convert-Inline $l) + ' ')
    Add-Linea ('')
  }

  if ($enTabla) { Add-Linea ('\bottomrule'); Add-Linea ('\end{longtable}') }
  if ($enCodigo) { Add-Linea ('\end{verbatim}') }
  Cerrar-Lista; Cerrar-Cita
  return $sb.ToString()
}

function Get-Titulo($texto, $porDefecto) {
  $m = [regex]::Match($texto, '(?m)^#\s+(.+?)\s*$')
  if ($m.Success) { return $m.Groups[1].Value }
  if ($porDefecto) { return $porDefecto }
  return 'Documento'
}
function Get-Campo($texto, $campo) {
  $m = [regex]::Match($texto, '(?m)\*\*' + $campo + ':\*\*\s*([^|\r\n]+)')
  if ($m.Success) { return $m.Groups[1].Value.Trim() }
  return ''
}

$plantilla = @'
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage[margin=2.5cm]{geometry}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=black}
\usepackage{longtable,booktabs,array}
\usepackage{microtype}
\usepackage{csquotes}
\usepackage{enumitem}
\setlist{nosep,leftmargin=*}
\title{__TITULO__}
\newcommand{\fuente}{__FUENTE__}
\author{__AUTOR__}
\date{__FECHA__}
\begin{document}
\maketitle
__CUERPO__
\end{document}
'@

# ---------------------------------------------------------------
# 3. El manifiesto, y si sus filas resuelven
# ---------------------------------------------------------------
$declarados = @()
if ($manifiesto) {
  foreach ($l in (Get-Content -LiteralPath $manifiesto -Encoding utf8)) {
    $l = $l.Trim()
    if ($l -eq '' -or $l.StartsWith('#')) { continue }
    $partes = $l.Split('|')
    $archivo = $partes[0].Trim()
    $titulo = if ($partes.Count -gt 1) { $partes[1].Trim() } else { '' }
    $declarados += [pscustomobject]@{ Destino = $archivo; Titulo = $titulo }
  }
}
$faltan = @()
foreach ($d in $declarados) {
  if (-not (Test-Path (Join-Path $Root $d.Destino))) { $faltan += $d.Destino }
}

# ---------------------------------------------------------------
# 4. Compilar cada documento, con la ruta relativa de la fuente
# ---------------------------------------------------------------
$motor = $null
foreach ($c in @('xelatex', 'lualatex', 'pdflatex', 'tectonic')) {
  $g = Get-Command $c -ErrorAction SilentlyContinue
  if ($g) { $motor = $c; break }
}

New-Item -ItemType Directory -Path $Destino -Force | Out-Null
$filas = @()

function Convertir-Uno($src, $titulo, $carpetaSalida, $relativo) {
  $texto = Get-Content -LiteralPath $src -Raw -Encoding utf8
  $nombre = [System.IO.Path]::GetFileNameWithoutExtension($src)
  $autor = (Get-Campo $texto 'Autor') -replace '^\[.*\]$', ''
  $fecha = Get-Campo $texto 'Fecha'
  $tex = $plantilla.Replace('__TITULO__', (Get-Titulo $texto $titulo)).
    Replace('__AUTOR__', $autor).
    Replace('__FECHA__', $fecha).
    Replace('__CUERPO__', (Convert-Md $texto))
  # El .tex guarda la ruta relativa de su fuente: los enlaces del documento resuelven,
  # y quien lee el .tex sabe de donde salio.
  $tex = $tex.Replace('__FUENTE__', $relativo)
  $rutaTex = Join-Path $carpetaSalida ($nombre + '.tex')
  Set-Content -LiteralPath $rutaTex -Value $tex -Encoding utf8 -NoNewline

  $pdf = 'sin motor'
  if ($motor) {
    Push-Location $carpetaSalida
    try {
      & $motor -interaction=nonstopmode -halt-on-error ($nombre + '.tex') *> $null
      & $motor -interaction=nonstopmode -halt-on-error ($nombre + '.tex') *> $null
    } catch { }
    finally { Pop-Location }
    if (Test-Path (Join-Path $carpetaSalida ($nombre + '.pdf'))) { $pdf = 'pdf' } else { $pdf = 'motor fallo' }
  }
  return [pscustomobject]@{
    Nombre = $nombre
    Ruta   = $rutaTex
    Tex    = if (Test-Path $rutaTex) { 'sí' } else { 'no' }
    Pdf    = $pdf
    Lineas = (Get-Content -LiteralPath $rutaTex).Count
  }
}

# La ruta de cada .tex: dist/<parte>/<archivo>.tex, siempre relativa a la raiz.
function Ruta-Relativa($ruta) { return ($ruta.Replace($Root + '\', '')).Replace('\', '/') }

# Primero el manifiesto, con la carpeta de su parte; despues los paper.md.
foreach ($d in $declarados) {
  $src = Join-Path $Root $d.Destino
  if (-not (Test-Path $src)) { continue }
  $parte = (($d.Destino -split '[\\/]')[1])
  $carpetaSalida = Join-Path $Destino $parte
  New-Item -ItemType Directory -Path $carpetaSalida -Force | Out-Null
  $r = Convertir-Uno $src $d.Titulo $carpetaSalida $d.Destino
  $filas += [pscustomobject]@{
    Documento = "$parte/$($r.Nombre)"
    Ruta      = (Ruta-Relativa $r.Ruta)
    Tex       = $r.Tex
    Pdf       = $r.Pdf
    Lineas    = $r.Lineas
  }
}

# Los paper.md que el manifiesto no declara: si ya esta emitido, no se repite.
$declaradas = @($declarados | ForEach-Object { [System.IO.Path]::GetFullPath((Join-Path $Root $_.Destino)) })
foreach ($p in $papers) {
  if ($declaradas -contains [System.IO.Path]::GetFullPath($p)) { continue }
  $carpeta = Split-Path $p -Parent
  $slug = (Split-Path $carpeta -Leaf) -replace '[^\w\-]', '-'
  $carpetaSalida = Join-Path $Destino $slug
  New-Item -ItemType Directory -Path $carpetaSalida -Force | Out-Null
  foreach ($src in @($p, (Join-Path $carpeta 'fuentes.md'))) {
    if (-not (Test-Path $src)) { continue }
    $rel = (Ruta-Relativa $src)
    $r = Convertir-Uno $src '' $carpetaSalida $rel
    $filas += [pscustomobject]@{ Documento = "$slug/$($r.Nombre)"; Ruta = (Ruta-Relativa $r.Ruta); Tex = $r.Tex; Pdf = $r.Pdf; Lineas = $r.Lineas }
  }
}

Write-Output "COMPILAR"
Write-Output "Root: $Root | Salida: $Salida"
Write-Output "Motor LaTeX: $(if ($motor) { $motor } else { 'ninguno' })"
Write-Output ""
Write-Output "DOCUMENTO | TEX | PDF | LINEAS TEX"
foreach ($f in $filas) { Write-Output "$($f.Documento) | $($f.Tex) | $($f.Pdf) | $($f.Lineas)" }
Write-Output ""
Write-Output "RUTA DEL TEX"
foreach ($f in $filas) { Write-Output $f.Ruta }
Write-Output ""
Write-Output "Manifiesto: $(if ($manifiesto) { 'sí' } else { 'ninguno' }) | declarados: $($declarados.Count) | no resuelven: $($faltan.Count)"
Write-Output ""
# Emitir algo es emitir algo: cero documentos no es un exito.
Write-Output "VEREDICTO: $(if ($filas.Count -gt 0 -and @($filas | Where-Object { $_.Tex -ne 'sí' }).Count -eq 0 -and $faltan.Count -eq 0) { 'pasa' } else { 'falla' })"
Write-Output ""

if ($faltan.Count -gt 0) {
  Write-Output "NO RESUELVEN"
  foreach ($f in $faltan) { Write-Output $f }
  Write-Output ""
}

Write-Output "INDETERMINADO"
if (-not $motor) {
  Write-Output "(no hay motor LaTeX: se emite el .tex y el PDF se declara sin motor)"
  Write-Output "(instalar uno de: xelatex, lualatex, pdflatex, tectonic — y volver a correr)"
} else {
  Write-Output "(compilar no juzga si el paper sirve: eso es criterio)"
}
