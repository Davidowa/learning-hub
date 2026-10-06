export const meta = {
  name: 'deck-audit',
  description: 'Audit and fix one course slice of slide decks: per week pair, audit+fix then adversarial review+fix',
  whenToUse: 'Pass args {course, dir, items:[{week, es, en, check_issues}], known}',
  phases: [
    { title: 'Audit', detail: 'auditor runs every code example, checks claims, parity, wording; fixes confirmed defects' },
    { title: 'Review', detail: 'independent reviewer refutes/verifies the fixes and does a fresh pass' },
  ],
}

const A = args
// args: {course, dir, weeks: ["w01", "track|w02", ...]}; paths derive from dir
A.known = '(Read the full list from the file ppts/audit/herramientas/defectos-conocidos-al-iniciar.txt before starting; it is the instructor list of content errors per course.)'
A.items = A.weeks.map(w => {
  const [sub, wk] = w.includes('|') ? w.split('|') : [null, w]
  const base = A.dir + '/' + (sub ? sub + '/' : '')
  return { week: (sub ? sub + '-' : '') + wk, es: `${base}es/${wk}.es.yaml`, en: `${base}en/${wk}.en.yaml` }
})
const COMMON = `
You are working in the git repository /home/user/learning-hub. Course slide decks are written as YAML lessons under ppts/ and built into .pptx by the kit in ppts/kit (layout catalogue and conventions: ppts/README.md, read the "Writing a lesson", "Layouts" and "What the kit enforces" parts). Each slide is a single-key mapping naming a layout (cover, agenda, objectives, roadmap, divider, concept, diagram, code, code_output, figure, table, trace, steps, stat, pitfalls, method, lab, quiz, tiers, quote, takeaways, homework, closing) with that layout's arguments, plus optional speaker 'notes'.

HOUSE RULES (from the instructor; breaking one silently is worse than asking):
- Spanish is Mexican Spanish (tú, computadora, archivo, celular; never vosotros, ordenador, fichero, vale as filler), with ¿ ¡ and accents. English is American English (percent, color, behavior; "you").
- No em dash (U+2014) or U+2015 anywhere, no double hyphen as a dash, no spaced hyphen used as a dash. Preflight rejects them.
- Never shrink type to make text fit. Fix overflow by shortening the YAML text or splitting an example across two slides. Code cards stop at 18 pt; a build line starting with "!" is a failure.
- accent: true only on a code annotation whose label already says it is the risk; at most one per slide.
- YAML traps: quote any flow-list cell containing a comma; quote numeric labels like '01'.
- The exercise of week N only uses what weeks 1 to N taught.
- No durations on slides (minutes belong in speaker notes).
- The cover names the subject; the session topic goes in the subtitle.

CONCURRENCY: many other agents are editing OTHER decks in this same working tree right now. Edit ONLY the YAML files assigned to you. Never edit ppts/kit/*, ppts/img/*, other decks, or any other file. Never run git commands that change state (no add, commit, stash, checkout, reset, restore, clean). Read-only git (git diff -- <your files>) is fine. If a defect can only be fixed outside your files (a figure in ppts/kit/figures.py or ppts/img, another week's deck), do NOT fix it; report it with fixed=false and where it must be fixed.

TOOLCHAINS available for actually running the slide code (use a private scratch folder /tmp/claude-0/audit/scratch/<course>-<week>/, create it):
- Python 3.11 with pandas, matplotlib, seaborn, PyQt6 (set QT_QPA_PLATFORM=offscreen), sqlite3 module.
- C++: g++ 13 / clang++ (use -std=c++20 -Wall -Wextra).
- C#: .NET 10 SDK. Copy the prewarmed template: dotnet new console -o <scratch>/cs, put the code in Program.cs && cd there && DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1 dotnet run. Multiple classes can go in extra .cs files.
- SQL: MariaDB 10.11 running locally (the course teaches MySQL 8; note real dialect differences instead of flagging them as slide errors). Connect with: mariadb -uaudit -paudit. Create and drop your own database named audit_<course>_<week> with dots replaced by underscores; never touch other databases.
- VBA, Excel formulas and Unity C# (UnityEngine) cannot be executed here. Check them by careful reading against the official Microsoft / Unity documentation semantics you know; trace them by hand. List anything you could not verify.
- Slide checks: ppts/audit/herramientas/check.sh <yaml> [<yaml>] builds the given decks with the real fonts and runs preflight, lint and sizes on them; the last line is CLEAN or NOT-CLEAN. Always use this script (kit/fonts.py finds the real Arial, Georgia and Courier New on Windows, macOS or Linux).

KNOWN DEFECTS reported by the instructor's earlier visual review (Spanish; "w07.es s9" means week 07 Spanish deck, slide 9, counting slides from 1 in the order they appear in the YAML). Those that fall in your files are confirmed defects: fix them (unless the fix lives in kit/figures.py, which another agent handles; then just report). Also, VBA w01 and w02 have a different slide count in es and en.
---
${A.known}
---`

const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          slide: { type: 'string', description: 'slide number (1-based, YAML order) and layout, e.g. "12 code"' },
          category: { type: 'string', enum: ['code-wrong', 'output-mismatch', 'line-reference', 'quiz-key', 'trace', 'technical-claim', 'description-mismatch', 'parity', 'language', 'consistency', 'pedagogy-order', 'overflow', 'figure', 'other'] },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          description: { type: 'string' },
          evidence: { type: 'string', description: 'what you ran or checked, and the actual result' },
          fixed: { type: 'boolean' },
          fix_summary: { type: 'string' },
        },
        required: ['file', 'slide', 'category', 'severity', 'description', 'evidence', 'fixed', 'fix_summary'],
      },
    },
    code_examples_run: { type: 'integer', description: 'how many code/code_output/quiz/trace snippets you actually executed or compiled' },
    unverifiable: { type: 'array', items: { type: 'string' } },
    checks_clean: { type: 'boolean', description: 'last line of check.sh on both files is CLEAN' },
    slide_counts: { type: 'string', description: 'es N slides / en M slides after your edits' },
  },
  required: ['findings', 'code_examples_run', 'unverifiable', 'checks_clean', 'slide_counts'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      description: 'one per auditor finding',
      items: {
        type: 'object',
        properties: {
          finding: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed-and-fix-correct', 'confirmed-fix-corrected-by-me', 'not-a-defect-reverted', 'not-a-defect-no-change', 'confirmed-left-unfixed-out-of-scope'] },
          note: { type: 'string' },
        },
        required: ['finding', 'verdict', 'note'],
      },
    },
    new_findings: AUDIT_SCHEMA.properties.findings,
    code_examples_run: { type: 'integer' },
    checks_clean: { type: 'boolean' },
    slide_counts: { type: 'string' },
  },
  required: ['verdicts', 'new_findings', 'code_examples_run', 'checks_clean', 'slide_counts'],
}

const files = it => [it.es, it.en].filter(Boolean)

function auditPrompt(it) {
  return `${COMMON}

YOUR ASSIGNMENT: course "${A.course}" (${A.dir}), session ${it.week}. Files:
${files(it).map(f => '- ' + f).join('\n')}
Run ppts/audit/herramientas/check.sh on your two files before editing; fix every mechanical issue it reports.

Audit EVERY slide of both files, including speaker notes, then fix the defects you confirm. Specifically:
1. Code that works: extract every code, code_output, quiz (source) and trace example and actually run or compile it with the toolchains above (add only the minimum scaffolding a fragment needs, and say so). A code_output panel must equal the real output. A trace table must match a hand or real execution step by step. Compiler warnings the slide denies (or errors it claims) must be real.
2. Line references: every annotation "Línea N" / "Line N" / "Líneas N a M" must point at the line of the displayed source (1-based) that it describes.
3. Quiz: exactly one defensible correct option; the answer stated in the notes matches; each distractor represents the confusion the notes say it represents.
4. Technical claims: definitions, numbers, API and menu names, keyboard paths, version facts. Flag anything false or outdated for the stated tool version.
5. Describing properly: each title, eyebrow, lead, caption and takeaway says what the slide actually shows (e.g. "three words" over a table of five is a defect). Agenda cards and objectives match what the deck teaches. Cover session counter "N de M" / "N of M" and the roadmap 'now' state agree with this session's position (glance at the neighbouring weeks' covers in the same folder to confirm the numbering scheme, read-only).
6. es/en parity: same slide count, same layouts in the same order, same facts, numbers and code behavior. When they disagree, decide which side is right and fix the other.
7. Language and register per house rules; one register across the deck (Spanish tú throughout, English "you" not "the student").
8. Pedagogy order: labs, quizzes and homework only use what this or earlier sessions taught (grep earlier decks in the same folder if unsure).

Fix rules: make the smallest edit that corrects the defect; keep the author's voice and structure; do not rewrite slides that are correct; do not invent content. After editing, run ppts/audit/herramientas/check.sh on both files and iterate until the last line is CLEAN (shorten text, never shrink type). Report every finding, including ones you decided were not defects only if they look suspicious to a reader (mark fixed=false and explain in evidence). Be exhaustive: an audit that reports nothing on a 25-slide deck with code must show in code_examples_run that it actually ran the code.`
}

function reviewPrompt(it, report) {
  return `${COMMON}

YOUR ASSIGNMENT: independent adversarial review of an audit that another agent just did on course "${A.course}" (${A.dir}), session ${it.week}. Files:
${files(it).map(f => '- ' + f).join('\n')}

The auditor's report (JSON):
${JSON.stringify(report)}

See exactly what the auditor changed with: cd /home/user/learning-hub && git diff -- ${files(it).join(' ')}

Do three things:
A. For each auditor finding, try to REFUTE it. Re-run the code yourself, recount line numbers yourself, re-derive the quiz answer yourself. If the finding was not a real defect and the auditor changed the file, revert that change (edit the YAML back by hand; never use git checkout/restore). If the defect is real but the fix is wrong, incomplete or introduced a new problem (broken parity, changed facts, worse wording, YAML trap, text now overflowing), correct it.
B. Fresh pass: audit both files yourself, slide by slide, for anything the auditor missed, with the same checklist: run every code example and compare outputs, line references, quiz keys, traces, technical claims, titles that do not describe their slide, es/en parity, Mexican Spanish / American English, no em dashes, pedagogy order. Fix what you confirm.
C. Run ppts/audit/herramientas/check.sh on both files and iterate until CLEAN.`
}

phase('Audit')
const results = await pipeline(
  A.items,
  it => agent(auditPrompt(it), { label: `audit:${A.course}:${it.week}`, phase: 'Audit', schema: AUDIT_SCHEMA }),
  (report, it) => report
    ? agent(reviewPrompt(it, report), { label: `review:${A.course}:${it.week}`, phase: 'Review', schema: REVIEW_SCHEMA })
        .then(rev => ({ week: it.week, files: files(it), audit: report, review: rev }))
    : { week: it.week, files: files(it), audit: null, review: null },
)
const out = results.filter(Boolean)
const nAudit = out.reduce((n, r) => n + (r.audit ? r.audit.findings.length : 0), 0)
const nNew = out.reduce((n, r) => n + (r.review ? r.review.new_findings.length : 0), 0)
const unclean = out.filter(r => !(r.review && r.review.checks_clean)).map(r => r.week)
log(`${A.course}: ${out.length} sessions, ${nAudit} audit findings, ${nNew} reviewer findings, not clean: ${unclean.join(', ') || 'none'}`)
return { course: A.course, dir: A.dir, sessions: out }
