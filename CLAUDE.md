<!-- davidowa-skills:project:start -->
- Slides here are built only with ppts/kit: python -m kit.preflight <folder>, then kit.build, kit.lint, kit.sizes and kit.preview.
- Do not use up-academic-slides or pptx.
- Office and Unity screenshots come from the capturists: Windows captures in ppts/img/<lang>/, macOS captures in ppts/img/<lang>/mac/, each folder with its own captures.json. They must pass check before a build.
- Captions and alt text go through the-writer.
- Here, 'captura' or 'capturar' without 'de pantalla' means data entry.
<!-- davidowa-skills:project:end -->

## Python runtime

Use Python 3.14. On Windows, run Python with `py -3.14`. Recreate the project environment with `py -3.14 -m venv .venv` before installing dependencies. Use the committed lock file when a Pipfile is present. Do not select Python 3.13 or 3.15 for this project.
