# Courses — source code

Each subfolder holds the **runnable code, notebooks, and assets** for a course.
The corresponding **lesson docs** live under `docs/{en,es}/courses/<course>/` and
are published via MkDocs Material to GitHub Pages.

## Layout

```
courses/
├── python-course/         # Python — basics → advanced
├── programacion-i/        # intro programming
└── computacion-grafica/   # OpenGL / shaders
```

## Add a new course

1. Create `courses/<slug>/` for code.
2. Create `docs/en/courses/<slug>/index.md` and `docs/es/courses/<slug>/index.md`.
3. Add nav entry in [`mkdocs.yml`](../mkdocs.yml).
