# Excel for Mac captures

The verified batch contains 30 native Excel and VBA captures from Excel for Mac 16.112.3, with an English interface. Files live in `ppts/img/en/mac/`; the Windows set remains in `ppts/img/en/`.

Run the installed capturist doctor before a batch. The Mac backend compatibility patch in this folder records the changes verified on this Mac: Screen Recording preflight binding, layer-8 dialog selection, carriage-return-separated accessibility windows, direct tab controls, workbook-specific ribbon selection, the VBA Insert Module toolbar control, clipboard paste through the VBA toolbar, and dismissal of the parent Manage Rules dialog.

The patch applies to the installed skill copy. It does not modify the Skills source repository. Review with `patch --dry-run -p1` from the installed skill directory before applying on another machine.

Run from the repository root:

```bash
~/.agents/skills/capturist-core/.venv/bin/python ~/.agents/skills/the-office-capturist/scripts/office_capture.py doctor --apps excel
~/.agents/skills/capturist-core/.venv/bin/python ~/.agents/skills/the-office-capturist/scripts/office_capture.py run capture-plans/excel-mac-en.yaml --out ppts/img/en --lang en
~/.agents/skills/capturist-core/.venv/bin/python ~/.agents/skills/the-office-capturist/scripts/office_capture.py check ppts/img/en/mac --plan capture-plans/excel-mac-en.yaml --sheet /tmp/excel-mac-sheet.png
```

Open the contact sheet and inspect every capture. The plan contains the supported, verified surfaces. Windows-only dialogs and unverified routes are excluded. Dark-appearance overrides address the native dialog colors; blank, duplicate, size and instance checks remain active.

Build the Mac lessons from `ppts/` with `python -m kit.mac`, then run preflight, build, lint, sizes and PDF export on `mac/`. A full `kit.build .` regenerates these derived editions when the Mac capture set is available. The generated `ppts/mac/` folder is ignored by Git.
