# Course notebooks

Google Colab notebooks for COM102 (Programación Orientada a Objetos) and TIA502 (Análisis
de Datos), one per teaching week, in Spanish and English.

They are generated rather than hand-edited. Seventy-eight notebooks that all need the same
setup cell, the same metadata and the same verification is how a format drifts, so the
shared parts live in `kit/nbkit.py` and each week lives in its own module under
`kit/lessons/`.

```bash
cd notebooks
python -m kit.build                    # every lesson
python -m kit.build da_w15_1           # just one
python kit/verify.py analisis-de-datos/es/w15.1.ipynb
```

## Layout

```
notebooks/
  kit/
    nbkit.py        markdown/code cell helpers, the data bootstrap, the writer
    build.py        lessons -> .ipynb
    verify.py       runs a notebook from an empty directory and reports uncaught errors
    lessons/        one module per week per language
  analisis-de-datos/{es,en}/wNN.ipynb
  programacion-orientada-a-objetos/{es,en}/wNN.ipynb
```

## Which weeks get a notebook

Data Analysis gets every week except `w01.0`, which is course framing. Twenty per language.

Object Oriented Programming gets every week except `w01.0`, `w14` and `w15`. Weeks 14 and 15
are PyQt6 and Colab has no display, so those two stay in the deck. Nineteen per language.

The source is always the `.yaml` under `ppts/`, never the built `.pptx`, and the Python
examples come from `docs/en/courses/python-course/` so that what a student runs matches what
they can clone.

## What a notebook is

Not the slide pasted into cells. A slide has to fit on a screen, so its code is trimmed; a
notebook has no such limit, and that is its reason to exist. For every block the deck shows,
the notebook gives the complete version, runs it, and adds the variants that did not fit.

Roughly: a cover cell naming the week and what the reader will be able to do, then one
markdown cell of explanation per code cell, quizzes turned into predict-before-you-run pairs,
and exercises at the end with the solutions in a separate markdown cell so they are not
visible out of the corner of the eye.

## Where the data comes from

No `files.upload()`, no `drive.mount()`, no dialog boxes. The first cell of every Data
Analysis notebook fetches `sales.csv`, `regions.csv` and `employees.csv` from the public
repository over a URL and, if that does not answer, rebuilds them in the session from the
fixed seed in `docs/en/courses/python-course/06 - Advanced/data/make_datasets.py`. Both
routes produce byte-identical files, which is checked by sha256.

Notebooks that write files, such as the weeks on paths and SQLite, create them with `open()`
in `/content` in a cell that runs before the one reading them.

## The verification bar

A notebook that does not run start to finish is not finished.

```bash
python kit/verify.py analisis-de-datos/es/w15.2.ipynb
```

That runs it with a fresh kernel in an empty working directory, the way a new Colab session
starts, and reports any traceback. Cells that fail on purpose catch their exception and
print it, because an uncaught raise stops Colab's "Run all" and the notebook then does not
run end to end.

Colab's pandas may be 2.x or 3.x, so every Data Analysis notebook prints `pd.__version__` in
its first cell and says what to expect from each. Verify against both before calling a week
done. Note that pandas 2.2 has no wheels for Python 3.14; build that environment on 3.13 or
older or `to_datetime` will segfault.

Notebooks are stored without outputs, which keeps them small and makes the student run them.
