<#
.SYNOPSIS
  Genera los PDFs de todas las presentaciones en esta computadora (Windows).

.DESCRIPTION
  Construye cada deck desde su .yaml y lo exporta a PDF. Si PowerPoint esta
  instalado lo usa a el, que es el programa para el que se disenaron los decks;
  si no, usa LibreOffice. Los PDFs quedan en pdf\ (uno por presentacion en
  pdf\decks\, y uno por curso e idioma con un marcador por sesion). pdf\ no se
  sube al repositorio.

  La primera vez crea .venv\ en la raiz del repositorio e instala lo que el kit
  necesita (ppts\requirements.txt mas comtypes, para hablar con PowerPoint).

.PARAMETER Carpeta
  Que construir, relativo a ppts\. Por omision, todo. Ejemplos: python,
  cpp\programacion-avanzada, office\manejo-y-analisis-de-la-informacion\es

.PARAMETER Motor
  auto (PowerPoint si esta, si no LibreOffice), powerpoint o libreoffice.

.EXAMPLE
  .\generar-pdfs.ps1
  .\generar-pdfs.ps1 python
  .\generar-pdfs.ps1 cpp\programacion-avanzada -Motor libreoffice
#>
param(
    [Parameter(Position = 0)][string]$Carpeta = '.',
    [Parameter(Position = 1)][ValidateSet('auto', 'powerpoint', 'libreoffice')][string]$Motor = 'auto'
)

$ErrorActionPreference = 'Stop'
$Raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Raiz

function Falla([string]$Mensaje, [string]$Ayuda = '') {
    Write-Host ''
    Write-Host "ERROR: $Mensaje" -ForegroundColor Red
    if ($Ayuda) { Write-Host $Ayuda }
    exit 1
}

function Probar-Python([string[]]$Comando) {
    # Devuelve la ruta del interprete si es Python 3.10 o mas nuevo, o $null.
    # El alias "python" de la Microsoft Store abre la tienda en vez de correr: se descarta solo,
    # porque no imprime nada.
    try {
        $exe = $Comando[0]
        $args0 = @()
        if ($Comando.Length -gt 1) { $args0 = $Comando[1..($Comando.Length - 1)] }
        $salida = & $exe @args0 -c "import sys; print(sys.executable if sys.version_info >= (3, 10) else '')" 2>$null
        if ($LASTEXITCODE -eq 0 -and $salida) { return ($salida | Select-Object -First 1).Trim() }
    } catch { }
    return $null
}

Write-Host "== Generar PDFs - $Raiz"

# 1. Python 3.10 o mas nuevo
$Python = $null
foreach ($c in @(@('py', '-3'), @('python'), @('python3'))) {
    if (Get-Command $c[0] -ErrorAction SilentlyContinue) {
        $Python = Probar-Python $c
        if ($Python) { break }
    }
}
if (-not $Python) {
    Falla 'No encontre Python 3.10 o mas nuevo.' `
        'Instalalo desde https://www.python.org/downloads/ y marca "Add python.exe to PATH".'
}
Write-Host "Python: $Python"

# 2. Entorno virtual con lo que el kit necesita
$VenvPy = Join-Path $Raiz '.venv\Scripts\python.exe'
if (-not (Test-Path $VenvPy)) {
    Write-Host 'Creando .venv\ (solo la primera vez)...'
    & $Python -m venv (Join-Path $Raiz '.venv')
    if ($LASTEXITCODE -ne 0) { Falla 'No pude crear .venv\.' }
}
Write-Host 'Instalando dependencias del kit...'
& $VenvPy -m pip install --quiet --disable-pip-version-check -r (Join-Path $Raiz 'ppts\requirements.txt') comtypes
if ($LASTEXITCODE -ne 0) { Falla 'pip no pudo instalar ppts\requirements.txt.' 'Revisa tu conexion a internet.' }

# 3. Construir los decks desde el YAML y exportarlos
Push-Location (Join-Path $Raiz 'ppts')
try {
    Write-Host ''
    Write-Host "== Construyendo presentaciones ($Carpeta)..."
    & $VenvPy -m kit.build $Carpeta
    if ($LASTEXITCODE -ne 0) { Falla 'Fallo la construccion de los decks.' }

    Write-Host ''
    Write-Host '== Exportando a PDF...'
    & $VenvPy -m kit.pdf $Carpeta -o (Join-Path $Raiz 'pdf') --engine $Motor
    if ($LASTEXITCODE -ne 0) {
        Falla 'Fallo la exportacion a PDF.' `
            ('Si no tienes PowerPoint, instala LibreOffice desde https://www.libreoffice.org/download/ ' +
             'y vuelve a correr este script.')
    }
} finally {
    Pop-Location
}

$Salida = Join-Path $Raiz 'pdf'
Write-Host ''
Write-Host "Listo. Los PDFs estan en: $Salida" -ForegroundColor Green
if (Test-Path $Salida) { try { Invoke-Item $Salida } catch { } }
