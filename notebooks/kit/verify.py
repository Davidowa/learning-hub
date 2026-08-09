"""Execute a notebook from scratch in an empty working directory.

Mirrors what a fresh Colab session does: new kernel, empty /content, nothing
uploaded. Any traceback that is not inside a cell marked as a deliberate failure
is reported.
"""
import shutil
import sys
import tempfile
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

MARKERS = ("FALLA A PROPÓSITO", "FAILS ON PURPOSE")


def run(path):
    nb = nbformat.read(path, as_version=4)
    work = Path(tempfile.mkdtemp(prefix="nbrun-"))
    client = NotebookClient(nb, timeout=600, kernel_name="python3",
                            resources={"metadata": {"path": str(work)}},
                            allow_errors=True)
    try:
        client.execute()
    except CellExecutionError as e:
        print(f"  KERNEL ERROR: {e}")
        return 1

    problems = 0
    code_cells = 0
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        code_cells += 1
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                problems += 1
                print(f"  CELL {i} RAISED {out['ename']}: {out['evalue']}")
                print("   source:", cell.source.splitlines()[0][:80])
    print(f"  {code_cells} code cells, {problems} uncaught errors")
    shutil.rmtree(work, ignore_errors=True)
    return problems


if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:
        print(f"== {arg}")
        total += run(arg)
    print("TOTAL PROBLEMS:", total)
    sys.exit(1 if total else 0)
