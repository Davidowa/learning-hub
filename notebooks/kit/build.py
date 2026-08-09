"""Build every notebook, or the ones named on the command line.

    python -m kit.build                 # everything under lessons/
    python -m kit.build da_w15_1        # one lesson module
"""
import importlib.util
import sys
from pathlib import Path

LESSONS = Path(__file__).resolve().parent / "lessons"


def run(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def main(names):
    files = sorted(LESSONS.glob("*.py"))
    if names:
        wanted = set(names)
        files = [f for f in files if f.stem in wanted]
        missing = wanted - {f.stem for f in files}
        for name in sorted(missing):
            print(f"no lesson called {name}")
    for path in files:
        run(path)
    print(f"\n{len(files)} lesson module(s) built")


if __name__ == "__main__":
    main(sys.argv[1:])
