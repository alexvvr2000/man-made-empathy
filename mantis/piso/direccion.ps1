# direccion.ps1 — mide si MANTIS esta enrutado contra el estandar vigente
# Forma: Ouroboros/Estandar/piso.md, La direccion y El rastro.
# Sale: 0 = pasa | 1 = falla | 2 = indeterminado. Siempre imprime el porque.
#
# Limite declarado: mide citas y fechas, no el sentido de las secciones.
# Mutacion que detecta: un ente de Ouroboros muto y la carta de MANTIS no lo refleja.

$ErrorActionPreference = 'Stop'
$raiz = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$estandar = Join-Path $raiz 'Ouroboros/Estandar'
$mantis   = Join-Path $raiz 'mantis'

$fallas = @()
$indet  = @()

function Diag($tipo, $msg) {
    Write-Host ("[{0}] {1}" -f $tipo, $msg)
}

# --- 1. Ouroboros limpio en git -------------------------------------------
$gitSeguro = $false
if (Test-Path (Join-Path $raiz '.git')) {
    Push-Location $raiz
    try {
        $sucio = @(git status --porcelain -- 'Ouroboros' 2>$null | Where-Object { $_ -match '^\s*[MADRCU]' })
        $cambios = @(Get-ChildItem 'Ouroboros' -Recurse -File -Filter *.md |
                     Where-Object { $_.LastWriteTime -gt (Get-Item 'mantis/mantis.md').LastWriteTime })
        if ($sucio.Count -gt 0) {
            $indet += "Ouroboros/ tiene $($sucio.Count) archivo(s) modificado(s) sin commitear: se compara contra un estado inestable"
        } elseif ($cambios.Count -gt 0) {
            $indet += "Ouroboros/ tiene $($cambios.Count) archivo(s) mas nuevos que la carta de MANTIS: posible atraso sin commitear"
        } else {
            $gitSeguro = $true
        }
    } catch { $indet += "git no respondio: $($_.Exception.Message)" }
    Pop-Location
} else {
    $indet += "no hay .git: no hay con que comparar"
}
if ($gitSeguro) { Diag 'ok' 'Ouroboros/ limpio y sin archivos mas nuevos que la carta' }

# --- 2. Cada estandar que MANTIS cita, existe ------------------------------
$cartas = @(Get-ChildItem $mantis -Recurse -File -Filter *.md)
$citas = @{}
foreach ($c in $cartas) {
    foreach ($m in [regex]::Matches((Get-Content $c.FullName -Raw), 'Estandar/([^`"\)\s]+\.md)')) {
        $citas[$m.Groups[1].Value] = $true
    }
}
if ($citas.Count -eq 0) { $fallas += 'MANTIS no cita ningun estandar: no hay enrutamiento que medir' }
$rotas = 0
foreach ($cit in ($citas.Keys | Sort-Object)) {
    $p = Join-Path $estandar $cit
    if (Test-Path $p) { Diag 'ok' "cita resuelve: Estandar/$cit" }
    else { $fallas += "cita rota: Estandar/$cit no existe"; Diag 'falla' "cita rota: Estandar/$cit" }
    if (-not (Test-Path $p)) { $rotas++ }
}

# --- 3. La carta cubre los estandares -------------------------------------
$todos = @(Get-ChildItem $estandar -File -Filter *.md | Select-Object -ExpandProperty Name)
foreach ($t in $todos) {
    $n = 0
    foreach ($c in $cartas) {
        if ((Get-Content $c.FullName -Raw) -match [regex]::Escape($t)) { $n++ }
    }
    if ($n -eq 0) { $fallas += "la carta no menciona el estandar $t"; Diag 'falla' "no cubierto: $t" }
}
if ($fallas.Count -eq 0) { Diag 'ok' "carta cubre los $($todos.Count) estandares" }

# --- 4. Nadie de abajo muto hacia arriba ----------------------------------
foreach ($e in (Get-ChildItem $estandar -File -Filter *.md)) {
    $firma = Select-String -Path $e.FullName -Pattern 'mantuvo MANTIS|MANTIS muta' -SimpleMatch
    if ($firma) { $fallas += "Ouroboros/Estandar/$($e.Name) declara que MANTIS muta hacia arriba"; Diag 'falla' "mutacion hacia arriba: $($e.Name)" }
}
Diag 'ok' 'nadie de abajo declara mutar hacia arriba'

# --- Veredicto -------------------------------------------------------------
# Lo roto manda sobre lo indeterminado: una cita muerta es una falla cierta,
# aunque ademas haya atraso. Ocultar la falla detras de `indeterminado` es
# el error que el piso pide no cometer.
Write-Host ''
if ($fallas.Count -gt 0) {
    Write-Host 'falla'
    $fallas | ForEach-Object { Write-Host "  - $_" }
    if ($indet.Count -gt 0) {
        Write-Host '  (ademas, indeterminado en lo que sigue)'
        $indet | ForEach-Object { Write-Host "  - $_" }
    }
    exit 1
}
if ($indet.Count -gt 0) {
    Write-Host 'indeterminado'
    $indet | ForEach-Object { Write-Host "  - $_" }
    exit 2
}
Write-Host 'pasa: MANTIS esta enrutado contra el estandar vigente'
exit 0
