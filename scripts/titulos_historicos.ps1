#!/usr/bin/env pwsh
#Requires -Version 7.0
[CmdletBinding()]
param(
    [Parameter(Mandatory, Position=0)][string]$File,
    [Parameter(Mandatory, Position=1)][string]$RepoPath,
    [Parameter(Mandatory, Position=2)][string]$OutputFolder,
    [ValidateRange(1,10)][int]$MinLevel = 1,
    [ValidateRange(1,10)][int]$MaxLevel = 10
)

$ErrorActionPreference = 'Stop'

# repo check
$RepoPath = (Resolve-Path -LiteralPath $RepoPath).Path
if (-not (Test-Path -LiteralPath (Join-Path $RepoPath '.git'))) {
    throw "No es un repo git: $RepoPath"
}

# normalizar y resolver archivo
$gitPath = ($File -replace '\\','/') -replace '^\./',''
$git = { & git -C $RepoPath -c core.quotepath=false @args }

if ($gitPath -notmatch '/') {
    $hits = @(& $git ls-files -- "*$gitPath*")
    if ($hits.Count -eq 0) { throw "Archivo no encontrado: $gitPath" }
    if ($hits.Count -gt 1) { throw "Ambiguo, sé específico: $($hits -join ', ')" }
    $gitPath = $hits[0]
    Write-Host "▸ $gitPath" -ForegroundColor DarkGray
}

# carpeta destino + nombre con auto-incremento
$null = New-Item -ItemType Directory -Path $OutputFolder -Force
$base = [System.IO.Path]::GetFileNameWithoutExtension($gitPath)
if (-not $base) { $base = 'titulos' }
$outPath = Join-Path $OutputFolder "${base}_titulos_${MinLevel}-${MaxLevel}.md"

if (Test-Path -LiteralPath $outPath) {
    $n = 1
    do {
        $outPath = Join-Path $OutputFolder "${base}_titulos_${MinLevel}-${MaxLevel}_${n}.md"
        $n++
    } while (Test-Path -LiteralPath $outPath)
}

# git log
$fmt = '--pretty=format:%x00%H%x1f%an%x1f%aI'
$logArgs = @('log','--no-merges','-w','--unified=0',$fmt,'-p','--follow','--',$gitPath)

$raw = & $git @logArgs 2>&1 | Out-String
if ([string]::IsNullOrWhiteSpace($raw)) { throw "Sin commits para '$gitPath'" }

# parse
$maxPart = if ($MaxLevel -ge 7) { '' } else { [string]$MaxLevel }
$headRegex = '^\s{0,3}#{' + $MinLevel + ',' + $maxPart + '}\s+\S'

$sb = [System.Text.StringBuilder]::new()
$curHash = ''; $curAutor = ''; $curFecha = ''
$headings = [System.Collections.Generic.List[string]]::new()
$inDiff = $false

function Flush {
    if ($headings.Count -gt 0) {
        [void]$sb.AppendLine("=== $curHash | $curFecha | $curAutor ===")
        foreach ($h in $headings) { [void]$sb.AppendLine($h) }
        [void]$sb.AppendLine()
    }
}

foreach ($line in ($raw -split "`n")) {
    if ($line.Length -eq 0) { continue }
    if ($line[0] -eq [char]0) {
        Flush
        $p = $line.Substring(1) -split [char]0x1f
        $curHash  = if ($p.Count -gt 0) { $p[0] } else { '' }
        $curAutor = if ($p.Count -gt 1) { $p[1] } else { '' }
        $curFecha = if ($p.Count -gt 2) { $p[2] } else { '' }
        $headings.Clear(); $inDiff = $false
    }
    elseif ($line.StartsWith('diff --git')) { $inDiff = $true }
    elseif ($line.StartsWith('+++') -or $line.StartsWith('---') -or $line.StartsWith('@@')) { continue }
    elseif ($inDiff -and $line.Length -gt 1 -and ($line[0] -eq '+' -or $line[0] -eq '-')) {
        $text = $line.Substring(1)
        if ($text -match $headRegex) { $headings.Add("$($line[0]) $($text.Trim())") }
    }
}
Flush

[System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

$s = $sb.ToString()
Write-Host "✓ $outPath" -ForegroundColor Green
Write-Host "  $(([regex]::Matches($s,'(?m)^=== ')).Count) commits, $(([regex]::Matches($s,'(?m)^[+-] #')).Count) títulos" -ForegroundColor DarkGray