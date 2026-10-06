export const meta = {
  name: 'syllabus-design',
  description: 'Design a time-durable 17-session syllabus: 3 independent designers, judge-synthesizer, fact-check, bilingual syllabus writers',
  whenToUse: 'args {course: "mobile" | "ecommerce"}',
  phases: [
    { title: 'Design', detail: 'three independent proposals with distinct lenses' },
    { title: 'Synthesize', detail: 'judge scores and merges into one plan JSON' },
    { title: 'Fact-check', detail: 'verify currency of every technical, legal and market claim' },
    { title: 'Write', detail: 'syllabus and audit documents in Spanish and English' },
  ],
}

const C = args.course
const MOBILE = C === 'mobile'
const ORIG = MOBILE ? 'ppts/react-native/desarrollo-de-aplicaciones-moviles/temario-original.es.txt' : 'ppts/ecommerce/fundamentos-del-comercio-electronico/temario-original.es.txt'
const PLAN = (MOBILE ? 'ppts/react-native/desarrollo-de-aplicaciones-moviles/plan.json' : 'ppts/ecommerce/fundamentos-del-comercio-electronico/plan.json')

const CONTEXT = `
Context: you are helping David Escobar-Castillejos, a professor at Universidad Panamericana (Mexico), design a new course for the repository /home/user/learning-hub. Today is 2026-10-05. Read the original syllabus the professor gave at ${ORIG} first.

How courses are built in this repo: every session is a slide deck written as YAML under ppts/<language>/<subject>/{es,en}/wNN.{es,en}.yaml and built by ppts/kit (see ppts/README.md). Existing courses run 17 sessions: 16 teaching weeks plus a final-exam session (covers say "Sesión N de 17"). Two partial exams sit at the end of weeks 8 and 13 and a project at week 16, and those weeks still teach their full topic before closing with exam or project logistics. Look at ppts/python/programacion-orientada-a-objetos/es/w01.0.es.yaml (the course-intro deck with roadmap and grading table) and one teaching week such as ppts/cpp/programacion-avanzada/es/w05.es.yaml to see the style, depth per session and slide archetypes available. House rules: Mexican Spanish (tú), American English, no em dashes, the exercise of week N only uses what weeks 1 to N taught, no durations on slides.

${MOBILE ? `This syllabus becomes TWO courses with the same syllabus: (A) React Native for iOS and Android, (B) SwiftUI for iOS only. Same session titles, objectives and assessment; each session has a track realization (what is built and coded in RN, what in SwiftUI). The original syllabus has an Android-native unit and an iOS-native unit: decide how both tracks honor them (e.g. the Android unit in the SwiftUI course can become the platform-concepts unit taught as Android-to-iOS counterparts; in the RN course both platforms are first-class). Students: engineering undergraduates who already know programming fundamentals and OOP (they took C#, Python OOP and C++ courses in this repo), but not JavaScript/TypeScript or Swift necessarily, so the language ramp must be planned. Hardware reality: SwiftUI needs a Mac with Xcode; RN with Expo can run on any laptop plus a phone.` :
`The course is for business/engineering undergraduates in Mexico (Spanish and English editions). Use Mexican context where relevant (SPEI, CoDi/DiMo, OXXO Pay, Mercado Libre, Tiendanube, Amazon México, PROFECO, NOM-247-SE, Ley Federal de Protección al Consumidor, the Mexican personal data law and its current regulator, SAT CFDI invoicing) but keep principles international. Little or no programming; any code cards are small (a JSON order payload, a webhook, a UTM link, a GA4 event).`}

"Time-transcendent" (trascendente en el tiempo) means: the syllabus names enduring concepts and skills, not product versions; tools appear as current examples of a concept and live in a dated "current stack" annex reviewed every term; obsolete items are replaced by the concept they were an instance of; each session teaches a transferable mental model plus one current, verifiable instance of it; and the course teaches students how to evaluate the next tool or trend themselves.`

const LENSES = [
  ['durability', 'DURABILITY-FIRST: strip everything to the concepts that will still be true in 10 years, then attach current instances. Flag every original item that is obsolete, version-bound or misnamed, and say what concept it was an instance of.'],
  ['practice', 'PRACTICE-FIRST: what a junior ' + (MOBILE ? 'mobile developer' : 'e-commerce analyst/manager') + ' must be able to do in their first job in 2027 to 2030. One running project or case that grows every week, labs that produce real artifacts, assessments that mirror real work.'],
  ['pedagogy', 'PEDAGOGY-FIRST: cognitive load, prerequisite order, spaced retrieval, constructive alignment between objectives, labs and assessment, a believable pace for 17 sessions of about 3 hours, and parity between the Spanish and English editions.'],
]

phase('Design')
const proposals = await parallel(LENSES.map(([key, lens]) => () => agent(`${CONTEXT}

Your lens: ${lens}

Produce a complete proposal in markdown:
1. Audit of the original syllabus: a table with every original line item, a verdict (keep / reframe / replace / merge / remove), the reason, and where it lands in your plan. Be concrete about obsolescence (for example, what replaced what, and since when) and only state facts you are sure of; mark uncertain ones "(verify)".
2. Additions the original lacks, with the reason each one earns a place.
3. The 17-session plan: for each session, title, the original items it covers, 4 to 6 topics, 3 to 5 measurable objectives, ${MOBILE ? 'the React Native realization and the SwiftUI realization (what is built, which APIs or components, one or two code examples worth putting on slides),' : 'the Mexican and international examples or cases used,'} a lab, a homework, and a quiz idea.
4. Assessment plan with weights, and the running project or case.
5. The current-stack annex as of October 2026 (${MOBILE ? 'React Native, Expo, navigation, state, storage, testing, release tooling; Swift, SwiftUI, Xcode, iOS versions, SwiftData, testing, release' : 'platforms, payment providers, analytics tools, regulators and laws'}) with what to re-check each term.
Return the markdown as your final answer.`, { label: `design:${C}:${key}`, phase: 'Design' })))

phase('Synthesize')
const synth = await agent(`${CONTEXT}

Three independent designers produced proposals for this course with different lenses (durability, practice, pedagogy). Here they are:

${proposals.map((p, i) => `===== PROPOSAL ${i + 1} (${LENSES[i][0]}) =====\n${p}`).join('\n\n')}

Act as the judge and the synthesizer. First score each proposal 1 to 10 on: coverage of every original item, time-durability, practicality, pedagogical soundness, feasibility in 17 sessions${MOBILE ? ', and fairness to both tracks' : ', and fit for Mexico'}. Then build ONE plan that starts from the strongest proposal and grafts the best ideas of the others. Every original syllabus item must be mapped (kept, reframed, merged or replaced with a reason).

Write the plan as JSON to ${PLAN} (create the directory if needed) with this shape:
{
  "course": "${C}",
  "title_es": "...", "title_en": "...",
  ${MOBILE ? '"tracks": {"rn": {"title_es": "...", "title_en": "...", "footer_es": "...", "footer_en": "..."}, "swiftui": {...same keys}},' : '"footer_es": "...", "footer_en": "...",'}
  "principles_es": [...], "principles_en": [...],
  "audit": [{"original": "...", "original_unit": "...", "verdict": "keep|reframe|replace|merge|remove", "reason_es": "...", "reason_en": "...", "lands_in": "w03, w07"}],
  "additions": [{"topic_es": "...", "topic_en": "...", "reason_es": "...", "reason_en": "...", "lands_in": "..."}],
  "units": [{"n": 1, "title_es": "...", "title_en": "...", "sessions": ["w01", "w02"]}],
  "assessment": [{"name_es": "...", "name_en": "...", "scope_es": "...", "scope_en": "...", "week": "w08", "weight": 20}],
  "running_${MOBILE ? 'project' : 'case'}": {"name": "...", "description_es": "...", "description_en": "...", "milestones": [{"week": "w03", "what_es": "...", "what_en": "..."}]},
  "sessions": [{
    "label": "w01", "n": 1, "unit": 1,
    "title_es": "...", "title_en": "...", "subtitle_es": "...", "subtitle_en": "...",
    "original_items": ["..."],
    "topics_es": [...], "topics_en": [...],
    "objectives_es": [...], "objectives_en": [...],
    ${MOBILE ? '"rn": {"build_es": "...", "build_en": "...", "apis": [...], "code_examples": ["short description of each code card"], "lab_es": "...", "lab_en": "...", "homework_es": "...", "homework_en": "..."},\n    "swiftui": {same keys},' : '"examples": ["Mexican and international examples or cases"], "lab_es": "...", "lab_en": "...", "homework_es": "...", "homework_en": "...",'}
    "quiz_idea_es": "...", "quiz_idea_en": "...",
    "builds_on": ["w00"], "exam_or_project_note": "",
    "verify": ["claims in this session that must be checked against official documentation before slides are written"]
  }],
  "stack_annex": {"as_of": "2026-10", ${MOBILE ? '"rn": [{"item": "...", "current": "...", "recheck": "..."}], "swiftui": [...]' : '"items": [{"item": "...", "current": "...", "recheck": "..."}]'}}
}
Exactly 17 sessions, w01 to w17, w17 being the final-exam session. Assessment weights sum to 100. Return a short summary of your scores and of the decisions you made as your final answer.`, { label: `synthesize:${C}`, phase: 'Synthesize' })

phase('Fact-check')
const fc = await agent(`${CONTEXT}

A course plan was synthesized at ${PLAN}. Fact-check it. For every technical, legal, product, market or version claim in it (stack annex, verify lists, topics, audit reasons), confirm it against authoritative sources. Use the tools available to you: ToolSearch can load WebSearch, WebFetch and the Context7 documentation tools (mcp__Context7__resolve-library-id and mcp__Context7__query-docs); try them, and if one is blocked, use what works. ${MOBILE ? 'Pay special attention to: React Native New Architecture status, Hermes, Expo SDK and Expo Router, React Navigation, the current minimum Android and iOS versions, Android components (activities, services, broadcast receiver restrictions since Android 8, content providers, intents, the manifest), ART vs Dalvik, Swift 6 concurrency, SwiftUI APIs (NavigationStack, Observation/@Observable, SwiftData), Xcode Previews and Playgrounds, storyboards status, App Store and Google Play distribution requirements.' : 'Pay special attention to: the Mexican personal-data law and regulator after the 2025 reform, PROFECO rules for online sales, NOM-247-SE, CFDI, SPEI/CoDi/DiMo, BNPL providers in Mexico, PCI DSS version, 3-D Secure, GA4 metrics and events, Shopify/Tiendanube/WooCommerce capabilities, headless and composable commerce definitions (MACH), marketplace fee models.'}
Correct the JSON in place where a claim is wrong or outdated, and phrase anything that changes often as a dated annex item rather than inside a session. Check also that the plan covers every original syllabus item, that each session's lab only uses what that and earlier sessions taught, that the 17-session pace is realistic, and that the Spanish and English fields say the same thing. Keep the JSON valid (verify with python3 -c "import json; json.load(open('${PLAN}'))"). Return a list of every correction you made and every claim you could not verify.`, { label: `factcheck:${C}`, phase: 'Fact-check' })

phase('Write')
const DOCS = MOBILE ? [
  ['es', 'ppts/react-native/desarrollo-de-aplicaciones-moviles/syllabus.es.md', 'the React Native course, in Spanish'],
  ['en', 'ppts/react-native/desarrollo-de-aplicaciones-moviles/syllabus.en.md', 'the React Native course, in English'],
  ['es', 'ppts/swift/desarrollo-de-aplicaciones-moviles/syllabus.es.md', 'the SwiftUI course, in Spanish'],
  ['en', 'ppts/swift/desarrollo-de-aplicaciones-moviles/syllabus.en.md', 'the SwiftUI course, in English'],
  ['es', 'ppts/react-native/desarrollo-de-aplicaciones-moviles/auditoria-del-temario.es.md', 'the audit of the original syllabus (shared by both mobile courses), in Spanish: why each item was kept, reframed, merged, replaced or removed, the principles of time-durability, and the current-stack annex for both tracks'],
  ['en', 'ppts/react-native/desarrollo-de-aplicaciones-moviles/syllabus-audit.en.md', 'the audit of the original syllabus (shared by both mobile courses), in English, same content as the Spanish one'],
] : [
  ['es', 'ppts/ecommerce/fundamentos-del-comercio-electronico/syllabus.es.md', 'the e-commerce course, in Spanish'],
  ['en', 'ppts/ecommerce/fundamentos-del-comercio-electronico/syllabus.en.md', 'the e-commerce course, in English'],
  ['es', 'ppts/ecommerce/fundamentos-del-comercio-electronico/auditoria-del-temario.es.md', 'the audit of the original syllabus, in Spanish: the time-durability principles, what changed and why, and the dated current-stack annex'],
  ['en', 'ppts/ecommerce/fundamentos-del-comercio-electronico/syllabus-audit.en.md', 'the same audit, in English'],
]
const written = await parallel(DOCS.map(([lang, path, what]) => () => agent(`${CONTEXT}

Write ${what} as a markdown document at /home/user/learning-hub/${path} from the plan at ${PLAN} (read it fully; do not invent content beyond it; if you see an error in it, write the corrected version and say so in your answer). Create the directory if needed. Structure for a syllabus: course title, description, who it is for and prerequisites, durability principles in two or three sentences, learning outcomes, units with sessions in a table (session, title, topics, ${MOBILE ? 'what is built in this track, ' : ''}lab), the running ${MOBILE ? 'project' : 'case'} and its milestones, assessment table, required hardware and software (as the dated annex), and policies only if the plan states them. Write in the language of the document only: Mexican Spanish with tú and no peninsular forms, or American English. Never use em dashes. Plain, specific prose: a number, a name, a tool rather than adjectives; no hype words. Edit only that one file. Return the path and a three-line summary.`, { label: `write:${path.split('/').pop()}:${path.split('/')[1]}`, phase: 'Write' })))

return { course: C, plan: PLAN, synth, factcheck: fc, written }
