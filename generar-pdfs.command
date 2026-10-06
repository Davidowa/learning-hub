#!/bin/bash
# Genera los PDFs de todas las presentaciones en esta computadora (macOS o Linux).
#
#   Doble clic en Finder, o desde la terminal:
#     ./generar-pdfs.command                   todos los cursos
#     ./generar-pdfs.command python            solo los cursos bajo ppts/python
#     ./generar-pdfs.command cpp/programacion-avanzada/es
#
# Construye cada deck desde su .yaml y lo exporta a PDF con LibreOffice. Los PDFs
# quedan en pdf/ (un PDF por presentación en pdf/decks/, y uno por curso e idioma
# con un marcador por sesión). pdf/ no se sube al repositorio.
#
# Necesita Python 3.10 o más nuevo y LibreOffice. La primera vez crea .venv/ en la
# raíz del repositorio e instala lo que el kit necesita (ppts/requirements.txt).
#
# Si macOS no te deja abrirlo con doble clic ("no se puede abrir", "Apple no pudo
# verificar...", "no tienes los permisos adecuados"), casi siempre es porque bajaste
# el ZIP en vez de clonar. Córrelo desde la Terminal, en la carpeta del repositorio:
#     bash generar-pdfs.command

set -euo pipefail
cd "$(dirname "$0")"
RAIZ="$(pwd)"
CARPETA="${1:-.}"
MOTOR="${2:-auto}"
NARGS=$#

# La carpeta va relativa a ppts/; con ppts/ adelante (autocompletado) también sirve.
case "$CARPETA" in
  ppts | ppts/ | ./ppts | ./ppts/) CARPETA=. ;;
  ppts/*) CARPETA="${CARPETA#ppts/}" ;;
  ./ppts/*) CARPETA="${CARPETA#./ppts/}" ;;
esac

MAC=""
if [ "$(uname)" = "Darwin" ]; then
  MAC=1
  # Si Homebrew no quedó en el PATH de la terminal, igual buscamos Python y LibreOffice ahí.
  PATH="$PATH:/opt/homebrew/bin:/usr/local/bin"
fi

pausa() {
  # Doble clic en Finder: sin argumentos y con una terminal. Deja leer el resultado.
  if [ "$NARGS" -eq 0 ] && [ -t 0 ]; then
    echo
    read -r -p "Presiona Enter para cerrar esta ventana... " _ || true
  fi
}

falla() {
  echo
  echo "ERROR: $1"
  [ -n "${2:-}" ] && echo "$2"
  pausa
  exit 1
}

echo "== Generar PDFs · $RAIZ"
case "$CARPETA" in /*) DIR="$CARPETA" ;; *) DIR="ppts/$CARPETA" ;; esac
[ -d "$DIR" ] || falla "No existe la carpeta $DIR." \
  "Pasa una carpeta relativa a ppts/, por ejemplo: python o cpp/programacion-avanzada/es"

# 1. Python 3.10 o más nuevo
PY=""
for c in python3.14 python3.13 python3.12 python3.11 python3.10 python3; do
  p="$(command -v "$c" 2>/dev/null)" || continue
  # Sin las herramientas de línea de comandos de Xcode, el /usr/bin/python3 de macOS no
  # corre: abre un diálogo para instalarlas (y lo que instala es Python 3.9). Se salta.
  if [ -n "$MAC" ] && [ "$p" = "/usr/bin/python3" ]; then
    dev="$(xcode-select -p 2>/dev/null)" || dev=""
    { [ -n "$dev" ] && [ -x "$dev/usr/bin/python3" ]; } || continue
  fi
  if "$p" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then
    PY="$p"
    break
  fi
done
[ -n "$PY" ] || falla "No encontré Python 3.10 o más nuevo${MAC:+ (el python3 que trae macOS es 3.9)}." \
  "Instálalo desde https://www.python.org/downloads/ o con Homebrew: brew install python"
echo "Python: $PY ($("$PY" -c 'import platform; print(platform.python_version())'))"

# 2. LibreOffice, que convierte cada .pptx a PDF
SOFFICE=""
if command -v soffice >/dev/null 2>&1; then
  SOFFICE="$(command -v soffice)"
elif command -v libreoffice >/dev/null 2>&1; then
  SOFFICE="$(command -v libreoffice)"
elif [ -x "/Applications/LibreOffice.app/Contents/MacOS/soffice" ]; then
  SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
elif [ -x "${HOME:-}/Applications/LibreOffice.app/Contents/MacOS/soffice" ]; then
  SOFFICE="$HOME/Applications/LibreOffice.app/Contents/MacOS/soffice"
fi
[ -n "$SOFFICE" ] || falla "No encontré LibreOffice." \
  "Instálalo desde https://www.libreoffice.org/download/ o con Homebrew: brew install --cask libreoffice"
# Que arranque de verdad antes de construir nada: la versión para Intel en una Mac con
# Apple Silicon sin Rosetta, o una copia dañada, si no fallaría en cada conversión.
"$SOFFICE" --version >/dev/null 2>&1 || falla "LibreOffice no arranca ($SOFFICE)." \
  "Ábrelo una vez desde Aplicaciones para ver qué pasa. En una Mac con Apple Silicon instala la
versión para Apple Silicon de https://www.libreoffice.org/download/ (o Rosetta: softwareupdate --install-rosetta)."
echo "LibreOffice: $SOFFICE"

# 3. Entorno virtual con lo que el kit necesita. Si ya hay una .venv/ cuyo Python no corre
#    (se desinstaló o lo cambió Homebrew), es anterior a 3.10 o no tiene pip, se rehace.
if ! .venv/bin/python -c 'import sys, pip; sys.exit(0 if sys.version_info >= (3, 10) else 1)' \
     >/dev/null 2>&1; then
  if [ -e .venv ] || [ -L .venv ]; then
    echo "Rehaciendo .venv/ (la que había no le sirve al kit)..."
  else
    echo "Creando .venv/ (solo la primera vez)..."
  fi
  "$PY" -m venv --clear .venv || falla "No pude crear .venv/." \
    "Si usas Debian o Ubuntu, instala el módulo venv: sudo apt install python3-venv"
fi
VPY="$RAIZ/.venv/bin/python"
echo "Instalando dependencias del kit..."
# PyYAML no publica rueda precompilada para el Python más nuevo; con esta variable se instala
# en Python puro en lugar de pedir un compilador.
PYYAML_FORCE_LIBYAML=0 "$VPY" -m pip install --quiet --disable-pip-version-check -r ppts/requirements.txt ||
  falla "pip no pudo instalar ppts/requirements.txt." "Revisa tu conexión a internet."

# 4. Las fuentes con las que el kit mide el texto
cd ppts
FALTAN="$("$VPY" -c 'from kit import fonts; print(" ".join(fonts.missing()))')"
if [ -n "$FALTAN" ]; then
  echo "AVISO: faltan fuentes ($FALTAN). Los decks se construyen igual, pero el texto"
  echo "       puede acomodarse distinto. macOS las trae en /System/Library/Fonts/Supplemental."
fi

# 5. Construir los decks desde el YAML y exportarlos
echo
echo "== Construyendo presentaciones ($CARPETA)..."
"$VPY" -m kit.build "$CARPETA" || falla "Falló la construcción de los decks."
echo
echo "== Exportando a PDF..."
"$VPY" -m kit.pdf "$CARPETA" -o ../pdf --engine "$MOTOR" || falla "Falló la exportación a PDF."
cd "$RAIZ"

echo
echo "Listo. Los PDFs están en: $RAIZ/pdf"
if command -v open >/dev/null 2>&1 && [ "$(uname)" = "Darwin" ]; then
  open "$RAIZ/pdf" || true
elif command -v xdg-open >/dev/null 2>&1 && [ -n "${DISPLAY:-}" ]; then
  xdg-open "$RAIZ/pdf" >/dev/null 2>&1 || true
fi
pausa
