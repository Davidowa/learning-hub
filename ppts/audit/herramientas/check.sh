#!/usr/bin/env bash
# Construye uno o varios decks y corre preflight, lint y sizes sobre cada uno.
# La última línea dice CLEAN solo si todo quedó en cero.
#
#   ppts/audit/herramientas/check.sh ppts/cpp/programacion-avanzada/es/w03.es.yaml [otro.yaml ...]
#
# Las rutas pueden ser relativas a la raíz del repositorio o absolutas. Usa el Python de .venv
# si existe. Las fuentes las encuentra kit/fonts.py en Windows, macOS o Linux.
RAIZ="$(cd "$(dirname "$0")/../../.." && pwd)"
PY="$RAIZ/.venv/bin/python"; [ -x "$PY" ] || PY=python3
cd "$RAIZ/ppts" || exit 2
bad=0
for y in "$@"; do
  case "$y" in /*) abs="$y" ;; *) abs="$RAIZ/$y" ;; esac
  rel="${abs#$RAIZ/ppts/}"
  p="${rel%.yaml}.pptx"
  echo "### $rel"
  out=$("$PY" -m kit.build "$rel" 2>&1); rc=$?
  echo "$out" | grep -E '^\s*!|Error|Traceback' && bad=1
  [ $rc -ne 0 ] && { echo "$out" | tail -5; bad=1; continue; }
  pf=$("$PY" -m kit.preflight "$rel" 2>&1); echo "$pf" | grep -vE ' clean$|^$'; echo "$pf" | grep -q '^0 issue' || bad=1
  li=$("$PY" -m kit.lint "$p" 2>&1);    echo "$li" | grep -vE ' clean$|^$'; echo "$li" | grep -q '^0 issue' || bad=1
  sz=$("$PY" -m kit.sizes "$p" 2>&1);   echo "$sz" | tail -1; echo "$sz" | grep -q '^0 run' || bad=1
done
[ $bad -eq 0 ] && echo CLEAN || echo NOT-CLEAN
