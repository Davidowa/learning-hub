# Learning Hub

Slides, code, and resources for Computer Science courses at **Universidad Panamericana**.

Live site: <https://davidowa.github.io/learning-hub/>

## Courses

- [`computational-thinking-course`](courses/computational-thinking-course/) — Computational Thinking · [EN](docs/en/courses/computational-thinking-course/index.md) · [ES](docs/es/courses/computational-thinking-course/index.md)
  - 01 · Problem Solving — four CT pillars, 7-step process, worked end-to-end example
  - 02 · Flowcharts — shape grammar + 6 Mermaid-rendered worked examples
  - 03 · Pseudocode — conventions, keyword table, side-by-side examples with flowcharts, functions
  - 04 · Programming Foundations — what programming is, languages, CPU/RAM/GPU, compilers, paradigms
- [`cs-course`](courses/cs-course/) — CS in C# · [EN](docs/en/courses/cs-course/index.md) · [ES](docs/es/courses/cs-course/index.md) *(under construction)*
- [`python-course`](courses/python-course/) — Python (basics → advanced) · [EN](docs/en/courses/python-course/index.md) · [ES](docs/es/courses/python-course/index.md)
  - 01 · Basics · 02 · OOP · 03 · Paths & Files · 04 · SQLite · 05 · GUI · 06 · Advanced · 07 · Activities

**Suggested path:** Computational Thinking → CS (C#) → Python.

## Repo layout

```text
learning-hub/
├── docs/                     # markdown source (rendered by MkDocs)
│   ├── en/                   # English content
│   └── es/                   # Spanish content
├── courses/                  # runnable code per course
├── resources/                # shared supplementary material
├── assets/                   # shared media
├── templates/                # assignment/project templates
├── mkdocs.yml                # site config
├── requirements.txt          # Python deps for docs
└── .github/workflows/docs.yml  # auto-deploy to GitHub Pages
```

## Build docs locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix:    source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000/>.

## Deploy

Push to `main` → GitHub Actions builds + publishes to Pages.

One-time setup in repo Settings → Pages:

- **Source:** GitHub Actions

## Contributing

- Add lesson markdown under `docs/{en,es}/courses/<slug>/`.
- Keep parallel structure between languages (missing pages fall back to English).
- Code samples go under `courses/<slug>/`.

## License

See [LICENSE](LICENSE).
