# direccion.ps1 — mide si MANTIS esta enrutado contra el estandar vigente
# Forma: Libre albedrio/piso.md, La direccion y El rastro.
# Sale: 0 = pasa | 1 = falla | 2 = indeterminado. Siempre imprime el porque.
#
# Limite declarado: mide citas y fechas, no el sentido de las secciones.
# Mutacion que detecta: un ente de Ouroboros muto y la carta de MANTIS no lo refleja.

$ErrorActionPreference = 'Stop'
$raiz = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$estandar = Join-Path $raiz 'Libre albedrio'
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
    foreach ($m in [regex]::Matches((Get-Content $c.FullName -Raw), 'Libre albedrio/([^`"\)\s]+\.md)')) {
        $citas[$m.Groups[1].Value] = $true
    }
}
if ($citas.Count -eq 0) { $fallas += 'MANTIS no cita ningun estandar: no hay enrutamiento que medir' }
$rotas = 0
foreach ($cit in ($citas.Keys | Sort-Object)) {
    $p = Join-Path $estandar $cit
    if (Test-Path $p) { Diag 'ok' "cita resuelve: Libre albedrio/$cit" }
    else { $fallas += "cita rota: Libre albedrio/$cit no existe"; Diag 'falla' "cita rota: Libre albedrio/$cit" }
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
    if ($firma) { $fallas += "Libre albedrio/$($e.Name) declara que MANTIS muta hacia arriba"; Diag 'falla' "mutacion hacia arriba: $($e.Name)" }
}
Diag 'ok' 'nadie de abajo declara mutar hacia arriba'

# --- 5. El estandar no nombra su propia carpeta ---------------------------
# Rige Libre albedrio/piso.md, `El estandar no nombra su propia carpeta`.
# Un estandar que cita su propia ubicacion se rompe en la siguiente mudanza.
# Se excluye la forma historica: `Libre albedrio/` y `Libre albedrio/` sueltos en
# prosa narran una mudanza; lo prohibido es la ruta que se resuelve al leer.
$sueltos = 0
foreach ($e in (Get-ChildItem $estandar -File -Filter *.md)) {
    $txt = Get-Content $e.FullName -Raw
    $porCarpeta = [regex]::Matches($txt, '\.\./Libre albedrio/|`\./Libre albedrio/').Count
    if ($porCarpeta -gt 0) {
        $sueltos += $porCarpeta
        Diag 'aviso' "nombra su carpeta: $($e.Name) ($porCarpeta citas)"
    }
}
if ($sueltos -eq 0) { Diag 'ok' 'ningun estandar resuelve una ruta a su propia carpeta' }
else { $indet += "$sueltos cita(s) de carpeta en los estandares: se rompen en la proxima mudanza" }

# --- 6. Los estandares no citan archivos que ya no existen -----------------
# Una cita a la tesis o a un estandar que no resuelve es una mentira por ruta:
# el nombre se dice, y el acto que promete no esta. Rige Libre albedrio/verbalizar.md.
$rotasEstandar = 0
foreach ($e in (Get-ChildItem $estandar -File -Filter *.md)) {
    foreach ($m in [regex]::Matches((Get-Content $e.FullName -Raw), '`(\.\./[^`]+\.md)`')) {
        $rel = $m.Groups[1].Value
        $p = [System.IO.Path]::GetFullPath((Join-Path $e.DirectoryName $rel))
        if (-not (Test-Path $p)) {
            $rotasEstandar++
            $fallas += "cita muerta en Libre albedrio/$($e.Name): $rel"
            Diag 'falla' "cita muerta: $($e.Name) -> $rel"
        }
    }
}
if ($rotasEstandar -eq 0) { Diag 'ok' 'ningun estandar cita un archivo que no existe' }

# --- 7. Todo el repo: ninguna cita relativa muerta -------------------------
# El fallo de la mudanza no estaba solo en los estandares: MANTIS citaba rutas
# con un nivel de menos y nadie lo veia. Se mide lo mismo sobre el ente.
$rotasEnte = 0
foreach ($c in (Get-ChildItem $raiz -Recurse -File -Filter *.md | Where-Object {
        $_.FullName -notmatch '\\\.memoria continua\\|\\\.git\\' })) {
    foreach ($m in [regex]::Matches((Get-Content $c.FullName -Raw), '`(\.\.?/[^`]+\.md)`')) {
        $p = [System.IO.Path]::GetFullPath((Join-Path $c.DirectoryName $m.Groups[1].Value))
        if (-not (Test-Path $p)) {
            $rotasEnte++
            $fallas += "cita muerta en $($c.Name): $($m.Groups[1].Value)"
            Diag 'falla' "cita muerta: $($c.Name) -> $($m.Groups[1].Value)"
        }
    }
}
if ($rotasEnte -eq 0) { Diag 'ok' 'ningun documento del repo cita un archivo relativo que no existe' }

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
