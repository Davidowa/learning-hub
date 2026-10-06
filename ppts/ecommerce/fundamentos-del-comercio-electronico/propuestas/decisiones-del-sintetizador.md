# Decisiones del sintetizador

<!-- Resumen que dejó el agente juez al combinar las tres propuestas en plan.json. -->

Plan written to `/tmp/claude-0/newcourses/ecommerce-plan.json`. It has 17 sessions (w01 to w17, with w17 as the final exam), all 24 original items audited and mapped to sessions, 18 additions, 4 units, 5 assessment components that add up to 100 and 36 annex rows dated 2026-10. A script checked the file: it parses, has no em or en dashes, each audit row's sessions list that item, and no session builds on a later week.

**Scores** (coverage / durability / practicality / pedagogy / feasibility / Mexico fit):
| Proposal | Scores | Total |
|---|---|---|
| P1, durability | 9 / 10 / 7 / 7 / 7 / 9 | 49 |
| P2, practice | 9 / 8 / 10 / 7 / 6 / 10 | 50 |
| P3, pedagogy | 10 / 9 / 8 / 10 / 8 / 9 | 54 |

- **P1, durability:** it has the best durability framework: the ten-year test, no brand names in titles, an eight-question tool card and a cap on brand facts in exams. But it teaches checkout before payments, packs law, the AI-agent trend and project presentations into S16, and a quiz assumes 16 % IVA on coffee.
- **P2, practice:** it is the most like real work and the richest on Mexican operations (store-diagnosis and incident-triage exams, test datasets with planted problems, postal-code address forms). But it has the same checkout-before-payments order, depends heavily on trial stores and payment sandboxes, asks for 16 weekly team chapters, and squeezes retention into the project week.
- **P3, pedagogy:** it fixes the original's four ordering problems, aligns outcomes with assessment, uses spaced retrieval, keeps one running order all term, places each legal rule where the decision happens, and bans memory-only facts in exams. Its weaknesses are a 25/15 weighting that departs from the house rule and an overloaded S16.

**Decisions:**
1. **Base:** P3's sequence and its case: Molienda, a fictional coffee roaster in Coatepec, and its order #1001 ($2,068). Payments come in w07, before checkout in w08. Metrics start in w03. Each system (OMS, WMS, ERP, CRM) appears in the week its job appears, and the full systems map is put together in w16.
2. **From P1:**
   - The five jobs of a distance sale (be found, earn trust, get paid, deliver, resolve), combined with P3's five control questions.
   - Tool-card questions on local fit and on integration and exit. The card has seven questions in total and a verdict, is practiced six times, and is applied to an unseen tool in the final exam.
   - The critique that the platform list mixes axes (WooCommerce is a WordPress plugin, not a CMS).
   - Mexican fraud patterns such as fake SPEI receipts, plus landed cost, email deliverability, the "deceptive design" term and customer service treated as an operation.
3. **From P2:**
   - Exam formats: Parcial 1 as a store-diagnosis memo, Parcial 2 as a Buen Fin incident triage, and the final as "Your first 30 days" with an unseen-tool card.
   - A dataset with planted problems.
   - Mexican checkout details: the postal code fills in the colonia, and the delivery date is promised by postal code.
   - The AI-use rule: disclose, verify, defend.
   - Every lab ends in a written decision.
   - Students never handle money or real customer data.
4. **Assessment:** I kept the house 5 × 20 split instead of P3's 25/15. Project checkpoints fall at the start of w05, w10 and w15, so they never share a week with an exam. Partials close w08 and w13, the project closes w16, and each of those weeks still teaches its full topic.
5. **w01** is built as two decks, w01.0 (course framing) and w01.1 (teaching), following COM102 and COM101.

**Corrections and items to verify:**
- **NOM-247-SE-2021 is the wrong norm.** It covers residential real estate. The plan uses LFPC art. 76 Bis and the voluntary standard NMX-COE-001-SCFI-2018 instead, and the professor should confirm which instrument the brief meant.
- **Coffee is probably taxed at 0 % IVA, while the grinder is at 16 %.** The case states each product's rate, and this is flagged for checking against LIVA art. 2-A.
- **The case URLs use `molienda.example`,** so no real site is implied.
- **Two facts where the proposals contradict each other are marked "verify":**
  - the outcome of the competition case on the Amazon and Mercado Libre marketplaces;
  - whether Shopify Payments is available in Mexico.
- **Other recent dated claims carry "verify" in each session and in the annex,** for example the December 2025 LFPC reform, Banxico Circular 9/2026, CFF art. 30-B, the 33.5 % courier rate and the AI-checkout launch and retreat.
- **Open items:**
  - The footer still needs a course code once one is assigned.
  - Pitches in w16 are about 6 minutes plus 2 of questions per team, so that block depends on the number of teams.