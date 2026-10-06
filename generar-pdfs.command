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

set -euo pipefail
cd "$(dirname "$0")"
RAIZ="$(pwd)"
CARPETA="${1:-.}"
MOTOR="${2:-auto}"
NARGS=$#

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

# 1. Python 3.10 o más nuevo
PY=""
for c in python3.13 python3.12 python3.11 python3.10 python3; do
  if command -v "$c" >/dev/null 2>&1 &&
     "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then
    PY="$c"
    break
  fi
done
[ -n "$PY" ] || falla "No encontré Python 3.10 o más nuevo." \
  "Instálalo desde https://www.python.org/downloads/ o con Homebrew: brew install python"
echo "Python: $(command -v "$PY") ($("$PY" -c 'import platform; print(platform.python_version())'))"

# 2. LibreOffice, que convierte cada .pptx a PDF
SOFFICE=""
if command -v soffice >/dev/null 2>&1; then
  SOFFICE="$(command -v soffice)"
elif command -v libreoffice >/dev/null 2>&1; then
  SOFFICE="$(command -v libreoffice)"
elif [ -x "/Applications/LibreOffice.app/Contents/MacOS/soffice" ]; then
  SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
fi
[ -n "$SOFFICE" ] || falla "No encontré LibreOffice." \
  "Instálalo desde https://www.libreoffice.org/download/ o con Homebrew: brew install --cask libreoffice"
echo "LibreOffice: $SOFFICE"

# 3. Entorno virtual con lo que el kit necesita
if [ ! -x ".venv/bin/python" ]; then
  echo "Creando .venv/ (solo la primera vez)..."
  "$PY" -m venv .venv || falla "No pude crear .venv/."
fi
VPY="$RAIZ/.venv/bin/python"
echo "Instalando dependencias del kit..."
"$VPY" -m pip install --quiet --disable-pip-version-check -r ppts/requirements.txt ||
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
