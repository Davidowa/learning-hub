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
# -LiteralPath en todo: si la ruta trae [ o ], PowerShell la leeria como comodin.
Set-Location -LiteralPath $Raiz

function Falla([string]$Mensaje, [string]$Ayuda = '') {
    Write-Host ''
    Write-Host "ERROR: $Mensaje" -ForegroundColor Red
    if ($Ayuda) { Write-Host $Ayuda }
    exit 1
}

function Corre-Callado([string]$Exe, [string[]]$Argumentos) {
    # Corre un programa sin mostrar nada y devuelve su codigo de salida. Con
    # ErrorActionPreference en Stop, Windows PowerShell 5.1 vuelve error cualquier linea
    # que el programa escriba en stderr; aqui solo importa el codigo de salida.
    $ErrorActionPreference = 'Continue'
    try {
        & $Exe @Argumentos 2>&1 | Out-Null
        return $LASTEXITCODE
    } catch {
        return -1
    }
}

function Probar-Python([string[]]$Comando) {
    # $true si el comando corre Python 3.10 o mas nuevo. El alias "python" de la Microsoft
    # Store, sin Python instalado, no corre nada: avisa en stderr y sale con 9009.
    # No se le pide la ruta del interprete: PowerShell lee lo que imprime con la pagina de
    # codigos de la consola, y una ruta con acentos o enes (un usuario de Windows llamado
    # asi) llegaria cambiada y no se podria correr.
    $resto = @($Comando | Select-Object -Skip 1)
    $codigo = Corre-Callado $Comando[0] ($resto + @('-c', 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'))
    return ($codigo -eq 0)
}

Write-Host "== Generar PDFs - $Raiz"

# La carpeta va relativa a ppts\; con ppts\ adelante (autocompletado) tambien sirve.
$Carpeta = $Carpeta -replace '^(\.[\\/])?ppts([\\/]+|$)', ''
if (-not $Carpeta) { $Carpeta = '.' }
$Destino = if (Split-Path -Path $Carpeta -IsAbsolute) { $Carpeta } else { Join-Path $Raiz "ppts\$Carpeta" }
if (-not (Test-Path -LiteralPath $Destino)) {
    Falla "No existe la carpeta ppts\$Carpeta." `
        'Escribela relativa a ppts\, por ejemplo: python  o  cpp\programacion-avanzada'
}

# 1. Python 3.10 o mas nuevo
$PyCmd = $null
foreach ($c in @(@('py', '-3'), @('python'), @('python3'))) {
    if ((Get-Command $c[0] -ErrorAction SilentlyContinue) -and (Probar-Python $c)) {
        $PyCmd = $c
        break
    }
}
if (-not $PyCmd) {
    Falla 'No encontre Python 3.10 o mas nuevo.' `
        'Instalalo desde https://www.python.org/downloads/ y marca "Add python.exe to PATH".'
}
$PyExe = $PyCmd[0]
$PyArgs = @($PyCmd | Select-Object -Skip 1)
$PyVer = & $PyExe @PyArgs -c 'import platform; print(platform.python_version())'
Write-Host "Python: $($PyCmd -join ' ') ($PyVer)"

# 2. Entorno virtual con lo que el kit necesita
$Venv = Join-Path $Raiz '.venv'
$VenvPy = Join-Path $Venv 'Scripts\python.exe'
# Un .venv\ deja de servir si se desinstala o actualiza el Python con que se creo, o si
# vino de una Mac (alli no hay Scripts\python.exe): entonces se rehace.
$VenvSirve = (Test-Path -LiteralPath $VenvPy) -and ((Corre-Callado $VenvPy @('-c', 'import sys')) -eq 0)
if (-not $VenvSirve) {
    if (Test-Path -LiteralPath $Venv) {
        Write-Host '.venv\ no sirve con el Python de esta computadora; lo vuelvo a crear...'
    } else {
        Write-Host 'Creando .venv\ (solo la primera vez)...'
    }
    & $PyExe @PyArgs -m venv --clear $Venv
    if ($LASTEXITCODE -ne 0) { Falla 'No pude crear .venv\.' }
}
Write-Host 'Instalando dependencias del kit...'
# Si PyYAML no trae version compilada para este Python (uno muy nuevo, de 32 bits o ARM),
# pip la compila, y sin Visual C++ eso falla. Asi instala la version en Python puro.
$env:PYYAML_FORCE_LIBYAML = '0'
& $VenvPy -m pip install --quiet --disable-pip-version-check -r (Join-Path $Raiz 'ppts\requirements.txt') comtypes
$CodigoPip = $LASTEXITCODE
Remove-Item Env:PYYAML_FORCE_LIBYAML -ErrorAction SilentlyContinue
if ($CodigoPip -ne 0) { Falla 'pip no pudo instalar ppts\requirements.txt.' 'Revisa tu conexion a internet.' }

Push-Location -LiteralPath (Join-Path $Raiz 'ppts')
try {
    # 3. Con que se exportan los PDFs. Se revisa antes de construir, que tarda.
    $Motores = & $VenvPy -c "from kit.pdf import find_soffice, powerpoint_installed as pp; print(('powerpoint ' if pp() else '') + ('libreoffice' if find_soffice() else ''))"
    if ($LASTEXITCODE -eq 0) {
        $HayPowerPoint = "$Motores" -match 'powerpoint'
        $HayLibreOffice = "$Motores" -match 'libreoffice'
        if ($Motor -eq 'powerpoint' -and -not $HayPowerPoint) {
            Falla 'No encontre PowerPoint en esta computadora.' 'Corre el script sin "powerpoint" para usar LibreOffice.'
        }
        if (-not $HayLibreOffice -and ($Motor -eq 'libreoffice' -or ($Motor -eq 'auto' -and -not $HayPowerPoint))) {
            $Que = 'No encontre ni PowerPoint ni LibreOffice, y se necesita uno de los dos para exportar a PDF.'
            if ($Motor -eq 'libreoffice') { $Que = 'No encontre LibreOffice.' }
            Falla $Que 'Instala LibreOffice (es gratis) desde https://www.libreoffice.org/download/ y vuelve a correr este script.'
        }
    }

    # 4. Construir los decks desde el YAML y exportarlos
    Write-Host ''
    Write-Host "== Construyendo presentaciones ($Carpeta)..."
    & $VenvPy -m kit.build $Carpeta
    if ($LASTEXITCODE -ne 0) {
        Falla 'Fallo la construccion de los decks.' `
            'Si tienes abierta en PowerPoint alguna presentacion de ppts\, cierrala y vuelve a correr este script.'
    }

    Write-Host ''
    Write-Host '== Exportando a PDF...'
    & $VenvPy -m kit.pdf $Carpeta -o (Join-Path $Raiz 'pdf') --engine $Motor
    if ($LASTEXITCODE -ne 0) {
        Falla 'Fallo la exportacion a PDF.' `
            ("Si tienes abierto algun PDF de pdf\ (en Acrobat, por ejemplo), cierralo y vuelve a correr este script.`n" +
             "Si lo que falla es PowerPoint, prueba con LibreOffice:  generar-pdfs.bat $Carpeta libreoffice")
    }
} finally {
    Pop-Location
}

$Salida = Join-Path $Raiz 'pdf'
Write-Host ''
Write-Host "Listo. Los PDFs estan en: $Salida" -ForegroundColor Green
if (Test-Path -LiteralPath $Salida) { try { Invoke-Item -LiteralPath $Salida } catch { } }
