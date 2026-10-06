"""Where the kit finds its fonts on Windows, macOS and Linux.

The kit measures every line of text with the real Arial, Georgia and Courier New
before it places it (see ``deck.measure``). It used to look only in
``%WINDIR%\\Fonts``, so on a Mac the files were never found, the measurement fell
back to a character-count ratio, and a deck built there wrapped and placed text
differently from the same deck built on Windows. The fonts are on a Mac, under
other file names: ``Arial Bold.ttf`` rather than ``arialbd.ttf``.

``find('arialbd.ttf')`` takes the Windows file name the rest of the kit uses and
returns the first matching file in the usual font folders of the three systems.
When nothing matches it returns the Windows path anyway, so the caller's own
fallback (``measure`` uses a ratio, ``preview`` the PIL default font) still runs.
"""
from __future__ import annotations

import os

# Windows file name -> other names the same face ships under (macOS, Office for
# Mac, Linux packages). Compared case-insensitively.
_ALIASES = {
    'arial.ttf': ['Arial.ttf'],
    'arialbd.ttf': ['Arial Bold.ttf', 'Arial_Bold.ttf', 'Arialbd.ttf'],
    'ariali.ttf': ['Arial Italic.ttf', 'Arial_Italic.ttf', 'Ariali.ttf'],
    'arialbi.ttf': ['Arial Bold Italic.ttf', 'Arial_Bold_Italic.ttf', 'Arialbi.ttf'],
    'georgia.ttf': ['Georgia.ttf'],
    'georgiab.ttf': ['Georgia Bold.ttf', 'Georgia_Bold.ttf', 'Georgiab.ttf'],
    'georgiai.ttf': ['Georgia Italic.ttf', 'Georgia_Italic.ttf', 'Georgiai.ttf'],
    'georgiaz.ttf': ['Georgia Bold Italic.ttf', 'Georgia_Bold_Italic.ttf', 'Georgiaz.ttf'],
    'cour.ttf': ['Courier New.ttf', 'Courier_New.ttf'],
    'courbd.ttf': ['Courier New Bold.ttf', 'Courier_New_Bold.ttf'],
    'couri.ttf': ['Courier New Italic.ttf', 'Courier_New_Italic.ttf'],
    'courbi.ttf': ['Courier New Bold Italic.ttf', 'Courier_New_Bold_Italic.ttf'],
    'consola.ttf': ['Consolas.ttf'],
    'inkfree.ttf': ['Ink Free.ttf', 'InkFree.ttf'],
}


def _dirs() -> list[str]:
    home = os.path.expanduser('~')
    windir = os.environ.get('WINDIR', r'C:\Windows')
    local = os.environ.get('LOCALAPPDATA', os.path.join(home, 'AppData', 'Local'))
    return [
        os.path.join(windir, 'Fonts'),                          # Windows, and WINDIR overrides
        os.path.join(local, 'Microsoft', 'Windows', 'Fonts'),   # Windows per-user installs
        '/System/Library/Fonts/Supplemental',                   # macOS: Arial, Georgia, Courier New
        '/System/Library/Fonts',
        '/Library/Fonts',
        os.path.join(home, 'Library', 'Fonts'),
        # Office for Mac carries Consolas and other Windows faces inside the app
        '/Applications/Microsoft PowerPoint.app/Contents/Resources/DFonts',
        '/Applications/Microsoft Word.app/Contents/Resources/DFonts',
        '/usr/share/fonts/truetype/msttcorefonts',              # Debian/Ubuntu ttf-mscorefonts
        '/usr/share/fonts/truetype/mscore',
        '/usr/share/fonts/msttcore',
        os.path.join(home, '.local', 'share', 'fonts'),
        os.path.join(home, '.fonts'),
    ]


_cache: dict[str, str] = {}


def find(win_name: str) -> str:
    """Path to the font Windows calls ``win_name``, wherever this system keeps it."""
    if win_name in _cache:
        return _cache[win_name]
    wanted = {n.lower() for n in [win_name] + _ALIASES.get(win_name.lower(), [])}
    found = None
    for d in _dirs():
        try:
            names = os.listdir(d)
        except OSError:
            continue
        for n in names:
            if n.lower() in wanted:
                found = os.path.join(d, n)
                break
        if found:
            break
    _cache[win_name] = found or os.path.join(os.environ.get('WINDIR', r'C:\Windows'),
                                             'Fonts', win_name)
    return _cache[win_name]


def missing(names=('arial.ttf', 'arialbd.ttf', 'georgia.ttf', 'georgiab.ttf',
                   'cour.ttf', 'courbd.ttf')) -> list[str]:
    """The fonts a build needs that this system does not have."""
    return [n for n in names if not os.path.exists(find(n))]


if __name__ == '__main__':
    for n in sorted(_ALIASES):
        p = find(n)
        print(f'{n:14s} {"ok  " if os.path.exists(p) else "MISSING"} {p}')
