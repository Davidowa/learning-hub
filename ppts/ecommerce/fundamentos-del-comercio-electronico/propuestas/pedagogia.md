<!-- Propuesta de temario, lente: pedagogia. Borrador de un agente diseñador, sin verificar; ver HANDOFF-auditoria-y-cursos-nuevos.md en la raíz. -->

# Fundamentos del comercio electrónico / Fundamentals of E-commerce
## Course redesign proposal: pedagogy-first edition

Prepared for David Escobar-Castillejos, Universidad Panamericana. Facts checked on 5 October 2026. Anything I could not confirm is marked (verify).

**How it fits the repo**
- **Location.** `ppts/commerce/fundamentos-del-comercio-electronico/{es,en}/wNN.{es,en}.yaml`, with 17 decks per language (34 in total). Session 1 is a single `w01` deck. Its first block is the course framing (roadmap, grading table, project, AI rules), so the course keeps the 17-deck count of the other 17-session courses. Split it into `w01.0` and `w01.1` only if the framing outgrows one block.
- **Palette and code cards.** Use `meta.language: commerce`. That palette already exists in `kit/tokens.py`: raspberry `9D174D` on an aubergine `2A0E1F` canvas with an amber accent. Its comment already expects JSON cards through the generic scanner. Code cards use `lang: json` for payloads, `lang: javascript` for the GA4 event and `lang: text` for the UTM link.
- **Cover.** Covers read `[Sesión, N de 17]` and `[Session, N of 17]`. The course code and the faculty kicker are still pending.
- **Annex-tagged slides.** In every session, one slide shows the current instance of that session's concept. Its `notes` start with `[Anexo 2026-10]`, so the term review finds all of them with one grep. These are the only slides that change when the annex changes.

---

## 0. Pedagogical design

### Course learning outcomes (CLOs)

By the end of the course the student can:

| CLO | Outcome |
|---|---|
| CLO1 Model | Classify commerce models and channels, and explain who controls price, customer data, payment, delivery and complaints in each one. |
| CLO2 Economics | Calculate and interpret order-level economics and core KPIs (margin, contribution, AOV, CR, CAC, ROAS, return rate, LTV) to choose between options. |
| CLO3 Design | Design a catalog, product page, payment mix and checkout that reduce uncertainty and friction, and justify each choice with evidence. |
| CLO4 Operate | Trace an order from payment through delivery, return and invoice, naming each risk (fraud, oversell, chargeback, failed delivery) and its control. |
| CLO5 Grow and measure | Plan acquisition and retention with a measurement plan, and explain why data sources disagree. |
| CLO6 Govern | Apply Mexican consumer, data-protection, tax and IP rules and ethical criteria to concrete store decisions, and compare one rule with an international counterpart. |
| CLO7 Evaluate | Evaluate a new tool or trend with an evidence-based rubric that separates the durable concept from the current instance. |

### Seven design rules

1. **Concept first, then a current instance.** Each session teaches one mental model that transfers to other tools. It then shows one current instance that students check live: a public fee page, a demo account or a government portal. No exam item asks for a brand, version, fee or date from memory. When a number matters, the question gives it.
2. **One running case and one running order.** The case is **Molienda**, a fictitious specialty coffee roaster from Coatepec, Veracruz.
   - It sells beans in 250 g and 1 kg, whole or ground, plus a monthly subscription and grinders as its high-ticket line.
   - Today it sells only through WhatsApp and Instagram.
   - Its **order #1001** (two 250 g bags at $289 and one grinder at $1,490, total $2,068 MXN) appears in every session. It is priced (S3), listed (S5), paid (S7), checked out (S8), sent as JSON (S9), shipped (S10), returned and invoiced (S11), attributed (S12 and S13), repeated (S14), audited (S15) and mapped (S16).
   - Keeping one familiar context lowers the background load, so students spend their attention on the new idea.
   - Coffee was chosen because it brings real complications: it is perishable (roast date, first-expired-first-out), shipping cost depends on weight, the subscription triggers the December 2025 consumer-law reform, the grinder makes interest-free installments (MSI) relevant, and selling to cafeterías gives a B2B side that needs CFDI invoices.
3. **Prerequisites before the topics that need them.** The original syllabus has four ordering problems, and the plan fixes each one:
   - It teaches the funnel and KPIs (unit 7) after conversion optimization (unit 3) and marketing (unit 6). Fix: a set of metrics starts in S3 and grows through the course.
   - It teaches checkout (unit 3) before payment methods (unit 4). Fix: payments come first.
   - It teaches the order and warehouse systems, OMS and WMS (unit 8), after order management and fulfillment (unit 5). Fix: each system appears in the session where its job appears.
   - It teaches the law (unit 8) after every decision the law governs. Fix: a short legal "compliance card" appears wherever a rule applies, and S15 pulls them together.
4. **Spaced retrieval.** Every session opens with three ungraded questions. One comes from the previous session, one from two or three sessions back and one from five or more back (schedule in 3.3). Every homework includes one mixed-in item from an earlier phase.
5. **Worked example, then completion, then independent work.** Block 1 works through an example on Molienda. The lab hands out a partly completed version. The homework applies the same skill alone to the team's own business.
6. **A limit on new material.** Each session introduces about 12 new terms and at most two new formulas. S3 is the exception: it has four arithmetic formulas, spread across the worked example, the lab and the homework. A bilingual glossary fixes each term once.
7. **Exams and checkpoints never fall in the same week.** Partials come at the end of S8 and S13. Project checkpoints are due at the start of S5, S10 and S15. The two exam weeks teach a topic that pulls earlier sessions together, so the class doubles as review: checkout in S8, measurement in S13.

---

## 1. Audit of the original syllabus

Verdicts: **keep**, **reframe** (keep the idea, change how it is taught), **replace**, **merge** or **remove**.

| # | Original item | Verdict | Reason | Lands in |
|---|---|---|---|---|
| 1.1 | Models and channels: B2C, B2B, C2C, D2C, marketplaces, omnichannel, social commerce, conversational commerce | **Keep models, reframe channels** | The models are durable. The channels are fast-changing instances of one question: who controls price, data, payment, delivery and the complaint. "Conversational commerce" has moved toward purchases made by an assistant, and its instances keep changing. Meta made in-app Shops checkout mandatory for new US shops in 2023 and discontinued it on 4 Sep 2025 (verify). OpenAI launched ChatGPT Instant Checkout on 29 Sep 2025 and scaled it back in March 2026. Social commerce appears again in 6.2, so the two are merged. | S1, S12, S16 |
| 1.2 | Value proposition and target customer | **Keep** | Durable. The original lists the "elements" but no method. The plan adds job-to-be-done and customer-profile tools and ties the proposition to evidence. | S2 |
| 1.3 | Market validation: interviews, surveys, prototypes, landing pages, test sales, PMF, viability | **Keep, reframe** | Taught as an "evidence ladder" (what people say, what they do, what they commit to). Product-market fit stays as a signal, not a milestone. "Viability" cannot be judged without order economics, which the original never teaches (addition A1). | S2, S3 |
| 2.1 | Platform types: SaaS, CMS, own stores, marketplaces (Shopify, Tiendanube, WooCommerce, Wix, Amazon, Mercado Libre) | **Reframe; remove brand names from the syllabus body** | The list mixes three different axes: SaaS is a delivery model, a CMS is a kind of software (WooCommerce is a plugin for WordPress), and a marketplace is a business model. The syllabus should name the rent-buy-build continuum and its decision criteria. Brand names move to the dated annex. Mercado Shops, Mercado Libre's own store builder, was itself discontinued in 2025 (verify date): a ready-made lesson on platform risk. | S4, annex |
| 2.2 | Catalog and inventory: SKU, categories, variants, prices, images, descriptions, availability | **Keep, split** | Product data (identifiers, attributes, feeds) goes to S5. Inventory as a live number shared across channels goes to S9, next to the order lifecycle where overselling happens. Adds GTIN/GS1 barcodes, structured data and AI-written descriptions. | S5, S9 |
| 2.3 | Modern architectures and integrations: APIs, headless, composable | **Reframe, merge with 8.3** | "Headless" and "composable" are vendor-era labels (the MACH Alliance dates from 2020). The durable concepts are how tightly storefront, commerce logic and data are coupled, plus a few integration patterns (API, webhook, feed). Taught where they first matter, then assembled into one systems map. | S4, S9, S16 |
| 3.1 | UX/UI: navigation, visual hierarchy, accessibility, responsive, mobile-first | **Keep** | Adds measurable standards as current instances: WCAG 2.2 (W3C, Oct 2023) and Core Web Vitals (INP replaced FID on 12 Mar 2024). | S6 |
| 3.2 | Product page and checkout | **Keep, split** | Product page goes to S6. Checkout moves to S8, after payments (S7), which fixes the original's inverted order. | S6, S8 |
| 3.3 | Conversion optimization: CRO, A/B tests, CTAs, social proof, promotions, drop-off analysis | **Keep, reframe** | "Drop-off analysis" needs the funnel, which the original only teaches in unit 7. The plan adds the logic of experiments and their traffic limits, since most small and mid-size stores cannot detect small effects. Google Optimize, a common free testing tool, shut down on 30 Sep 2023. The method outlived the tool. Promotions are tied to Buen Fin and Hot Sale and to honest reference prices. | S6, S8 |
| 4.1 | Payment methods: cards, transfers, SPEI, wallets, deferred payments, BNPL, gateways, processors | **Keep, expand** | Missing items that matter in Mexico: cash vouchers (OXXO Pay and similar), CoDi (2019), DiMo (since early 2023), and MSI as its own item ("deferred payments" in the original is ambiguous). Banxico Circular 9/2026 requires banks to standardize mobile, DiMo, CoDi and QR transfer flows by 14 Dec 2026. Adds the economics: fees, settlement times and net amount received. | S7 |
| 4.2 | Security and data protection: encryption, tokenization, authentication, privacy, good practices | **Reframe, split** | "Good practices" with no merchant decision attached cannot be assessed. The merchant's real decision is how to keep card data out of its own systems: tokenization, hosted payment fields, PCI DSS scope (v4.0.1 is current) and 3-D Secure. That goes to S7. Login methods such as passkeys go to S8. Privacy law goes to S15. | S7, S8, S15 |
| 4.3 | Fraud and risk management | **Keep, move** | Fraud review is a step in the order lifecycle, and a chargeback is a payment state, so the topic sits with orders. | S9 |
| 5.1 | Order and inventory management | **Keep, reframe** | Taught as an order with two separate status tracks (payment and fulfillment) plus inventory arithmetic. Brings the OMS forward from 8.3. | S9 |
| 5.2 | Fulfillment and distribution: storage, picking, carriers, logistics operators, last mile | **Keep** | Adds the delivery promise as a feature with a cost, dimensional (volumetric) weight, the platform-worker labor reform (verify how it applies) and cross-border shipping. | S10 |
| 5.3 | Logistics models and after-sales: dropshipping, 3PL, returns, refunds, reverse logistics | **Split, reframe** | Dropshipping and 3PL go to S10. Dropshipping is reframed as a sourcing model in which legal responsibility to the consumer stays with the seller. Returns, refunds and reverse logistics go to S11, next to warranty law and CFDI invoicing. | S10, S11 |
| 6.1 | Traffic acquisition: SEO, search ads, social ads, content | **Keep, reframe** | Reframed from "traffic" to "customers bought at a CAC", split into capturing existing demand and creating new demand. AI-generated answers in search and assistants are taught as the current change in how products get found. | S12 |
| 6.2 | Social commerce and content: networks, influencers, reviews, communities, UGC | **Merge with 1.1's social commerce** | Adds influencer disclosure duties, fake-review rules (the US FTC rule has been in force since Oct 2024) and TikTok Shop México (opened Feb 2025). | S12, S8 |
| 6.3 | Retention: CRM, email, remarketing, automation, loyalty | **Keep, reframe** | The measurable core is cohort retention and LTV. Remarketing is taught under consent and the loss of tracking identifiers: Apple ATT (Apr 2021) and Safari blocking third-party cookies by default since 2020. Chrome kept third-party cookies and Google retired its Privacy Sandbox APIs in Oct 2025 (verify). Adds subscriptions under the Dec 2025 consumer-law reform. | S14 |
| 7.1 | Core KPIs: conversion, AOV, CAC, LTV, ROAS, margin | **Keep, redistribute** | Taught in unit 7 they arrive too late to judge CRO or marketing. They now build up over the course: margin and AOV (S3), conversion rate (S6), CAC and ROAS (S12), the full KPI tree (S13), LTV (S14). | S3, S6, S12, S13, S14 |
| 7.2 | Conversion funnel | **Keep, move earlier** | Built with UX in S6, used for CRO in S8, measured with events in S13. | S6, S8, S13 |
| 7.3 | Digital analytics: GA4 and dashboards | **Reframe** | The syllabus should name event-based measurement and measurement plans. GA4 is the current instance; it replaced Universal Analytics, which stopped processing standard-property data on 1 Jul 2023. | S13, annex |
| 8.1 | Consumer protection and privacy: product info, prices, personal data, consent, warranties, returns | **Keep, spread out, update** | Each rule is taught where the decision happens (price display S3, product info S5, pre-payment info S8, warranty and returns S11, tracking consent S13, subscriptions S14) and consolidated in S15. Updates: a new personal data law (LFPDPPP) was published in the DOF on 20 Mar 2025. INAI was dissolved and the Secretaría Anticorrupción y Buen Gobierno now supervises private-sector data protection. LFPC art. 76 Bis gained fractions VIII and IX on recurring charges (DOF 12 Dec 2025). | S3, S5, S8, S11, S13, S14, S15 |
| 8.2 | Intellectual property and digital ethics: copyright, trademarks, dark patterns, transparency, data and AI | **Keep** | Adds a named taxonomy of dark patterns, the FTC v. Amazon Prime settlement ($2.5 billion, 25 Sep 2025) and EU AI Act art. 50 transparency duties (applicable from 2 Aug 2026). | S15, S8, S16 |
| 8.3 | Enterprise tech ecosystem: CRM, ERP, OMS, WMS, APIs, webhooks | **Merge, introduce each system where its job appears** | Introduced just in time: OMS (S9), WMS (S10), ERP and CFDI (S11), analytics (S13), CRM (S14), then assembled into one map (S16). | S9 to S16 |

**Nothing is removed outright**, because every item names a lasting concept. What does leave the syllabus body is the brand names (they move to the annex) and "CMS" as a platform category.

**One fact in the brief needs correcting.** The brief lists **NOM-247-SE** as e-commerce context. NOM-247-SE-2021 actually covers commercial information, advertising and contracts for **residential real estate** (DOF 22 Mar 2022). The instruments that apply to e-commerce in general are:
- LFPC Chapter VIII Bis (art. 76 Bis);
- the voluntary standard **NMX-COE-001-SCFI-2018** (in force since 1 May 2019);
- PROFECO's voluntary **Distintivo Digital** with its e-commerce code of ethics.

NOM-247 can still appear, but only as an example of a sector-specific norm that also applies to websites.

---

## 2. Additions the original lacks

| # | Addition | Why it earns a place | Where |
|---|---|---|---|
| A1 | **Order economics** (contribution margin per order) | It is the common measure for every decision in the course (platform, payment, shipping, returns, ads). Without it students cannot compare options, and it is the anchor for the business students. | S3, then in every session |
| A2 | **Mexican payment specifics**: cash vouchers, CoDi/DiMo, MSI, cash on delivery | In Mexico, cash use and installment habits decide which customers can buy at all. Brazil's Pix and India's UPI give the international comparison. | S7 |
| A3 | **Tax and invoicing**: CFDI 4.0, marketplace withholding, SAT access to platforms | Every Mexican store invoices. CFDI 4.0 has been mandatory since 1 Apr 2023. Marketplaces have withheld ISR and IVA from sellers since Jun 2020, with rates changed in the 2026 reform (verify). CFF art. 30-B has given SAT online access to platforms since 1 Apr 2026. | S11 |
| A4 | **Product data standards**: GTIN/GS1 barcodes, structured data, feeds | One product record feeds the store, marketplaces, search engines and AI assistants. Errors in it multiply across every channel. | S5 |
| A5 | **Delivery promise economics and cross-border shipping** | Dimensional weight and delivery-date promises decide both margin and conversion. Courier imports from countries without a trade agreement with Mexico have paid a 33.5% global rate since 15 Aug 2025 (verify current rate), which changed Shein's and Temu's price advantage. | S10 |
| A6 | **How experiments work** | Prevents false conclusions from A/B tests. Most small and mid-size stores lack the traffic to detect small effects. | S8 |
| A7 | **Subscriptions and recurring charges** | The LFPC reform of 12 Dec 2025 changed how sign-up, renewal and cancellation must work. | S14 |
| A8 | **Accessibility and speed as measurable UX** | WCAG 2.2 and Core Web Vitals turn "good UX" into something checkable. The EU European Accessibility Act has applied since 28 Jun 2025. | S6 |
| A9 | **Reconciling measurements, and consent** | Ad platforms, analytics and the order system always report different numbers. Students must know which source to trust for which question. | S13 |
| A10 | **Platform risk and competition** | Fee changes, account suspension and closed products (Mercado Shops). COFECE's 2024 preliminary finding was that the Amazon and Mercado Libre marketplaces lacked effective competition; the case closed in 2025 without remedies (verify). The Comisión Nacional Antimonopolio replaced COFECE in Oct 2025. | S4, S16 |
| A11 | **Responsible use of AI in commerce** | AI-generated content still has to be true, AI answers are changing how products are found, and the EU AI Act sets an international reference. | S5, S12, S15, S16 |
| A12 | **Tool-and-trend evaluation rubric (the "tool card")** | This is the course's "time-transcendent" skill. Students practice it six times rather than meet it once. | S4, S7, S10, S12, S13, S16 |
| A13 | **Spreadsheet data skills** (cohorts, RFM) | Analysis without code that every graduate can repeat on their own data. | S3, S14 |

---

## 3. The 17-session plan

### 3.1 Roadmap (for the `roadmap` slide)

| Phase | Weeks | Title (es / en) | Content |
|---|---|---|---|
| 01 | 1 to 4 | El negocio detrás de la tienda / The business behind the store | Models, evidence, order economics, platforms |
| 02 | 5 to 8 | La compra / The purchase | Catalog, UX and funnel, payments, checkout. **Partial 1** at the end of week 8 |
| 03 | 9 to 13 | Cumplir y crecer / Deliver and grow | Orders, fulfillment, after-sales, acquisition, measurement. **Partial 2** at the end of week 13 |
| 04 | 14 to 17 | Relación, reglas y lo que sigue / Loyalty, rules and what comes next | Retention, law and ethics, evaluating tools, **project** (week 16), **final exam** (week 17) |

### 3.2 Session template, about 3 hours

Minutes live in the speaker notes only, never on slides.

| Segment | Time | Typical slides |
|---|---|---|
| Opening and retrieval | 15 | `cover`, `agenda` (4 cards, no durations), `objectives`, `roadmap`, a `steps` slide with three retrieval questions, a `table` slide with the answers and the session each came from |
| Block 1: the mental model plus a worked Molienda example | 35 | `divider`, `concept`, `figure` or `diagram`, `table`, or `code` where it applies |
| Block 2: the second concept plus the live current instance | 35 | `divider`, `compare`, a `tiers` slide tagged `[Anexo]`, `pitfalls` |
| Break | 10 | |
| Block 3: team lab (a completion problem) | 55 | `divider`, `lab` |
| Close | 15 | `quiz` plus an answer slide (`trace` or `table`), `takeaways`, `homework`, `closing` |

That is about 24 to 28 slides, the same size as the existing teaching decks. In exam weeks the lab drops to 30 minutes, and 20 minutes go to exam scope, rules and two practice items (as in COM102 `w08`). In S16, blocks 1 and 2 take 60 minutes, a short lab 25, and pitches about 70 (up to 8 teams at 6 minutes plus 2 minutes of questions).

### 3.3 Course-long threads and the retrieval schedule

| Thread | What it is | Sessions |
|---|---|---|
| Order P&L | The cost sheet of order #1001; each session fills in one line | Built in S3. Commission S4, payment fee S7, shipping S10, returns S11, CAC S12, LTV S14 |
| Funnel | Sessions through purchases | Built S6, used for CRO S8, measured with events S13 |
| Tool card | The six-question evaluation (below) | Platform S4, payment provider S7, logistics provider S10, ad channel S12, analytics tool S13, emerging trend S16 |
| Five control questions | Who sets the price, holds the data, takes the payment, delivers, answers the complaint | S1, S4, S12, S16 |
| Compliance card | One legal rule, shown where it applies | S3, S5, S8, S11, S13, S14, then consolidated in S15 |
| Systems map | One system added when its job appears | Commerce engine S4, OMS S9, WMS S10, ERP/CFDI S11, analytics S13, CRM S14, assembled S16 |

**The tool card**, in Spanish "Ficha de evaluación". Each tool or trend is checked against six questions, then given a verdict:
1. **Job and concept.** What durable job does it do? What is it an instance of? What did it replace?
2. **Evidence.** What independent, checkable evidence exists for a business like ours?
3. **Economics.** Which lines of the order P&L does it change, and by how much?
4. **Control.** What are the answers to the five control questions?
5. **Exit.** How do we leave? What data can we export? What breaks if it disappears tomorrow?
6. **Risk and compliance.** What are the legal, security and dependency risks?

Verdict: adopt, pilot (with a metric and a stop rule), watch or reject, plus a date to check it again.

**Retrieval openers** (Q1 from the previous session, Q2 from two or three back, Q3 from five or more back):

| Session | Q1 | Q2 | Q3 | | Session | Q1 | Q2 | Q3 |
|---|---|---|---|---|---|---|---|---|
| S2 | S1 | S1 | diagnostic | | S10 | S9 | S7 | S4 |
| S3 | S2 | S1 | diagnostic | | S11 | S10 | S8 | S3 |
| S4 | S3 | S2 | S1 | | S12 | S11 | S9 | S5 |
| S5 | S4 | S3 | S1 | | S13 | S12 | S10 | S6 |
| S6 | S5 | S3 | S1 | | S14 | S13 and Partial 2 most-missed | S12 | S3 |
| S7 | S6 | S4 | S2 | | S15 | S14 | S11 | S8 |
| S8 | S7 | S5 | S3 | | S16 | S15 | S12 | S4 |
| S9 | S8 and Partial 1 most-missed | S7 | S3 | | S17 | one item per phase, mixed | | |

**Code cards in the whole course:** a product JSON (S5), an order JSON and a webhook (S9), a UTM link (S12) and a GA4 purchase event (S13). None is longer than 12 lines.

---

### S1 · Comercio digital: modelos, canales y quién controla qué / Digital commerce: models, channels and who controls what
- **Original items:** 1.1. **Deck:** `w01` (block 1 is the course framing).
- **Mental model:** The five control questions. A *model* says who sells to whom. A *channel* says where the sale happens. The five questions say who holds the power.
- **Current instance (verifiable):** TikTok Shop México (opened Feb 2025), a social marketplace with its own checkout. Contrast it with Facebook and Instagram Shops, whose in-app checkout ended on 4 Sep 2025 (verify) and which now send buyers to the merchant's own site.
- **Topics:**
  1. Course framing: roadmap, grading, project, AI rules, and the concept-versus-instance rule with its annex.
  2. What counts as e-commerce: the order is placed digitally, however the customer pays or receives it. E-commerce's share of retail (latest INEGI or AMVO figure, verify).
  3. Models: B2C, B2B, C2C, D2C, B2B2C; own store versus marketplace.
  4. Channels: own site or app, marketplace, social, conversational (WhatsApp Business catalog), omnichannel (click and collect, ship from store), and purchases made by an assistant as the newest form.
  5. The five control questions, applied.
- **Objectives:** the student can
  - distinguish model from channel in five given businesses;
  - classify ten businesses by model and channel, answering the five questions for each;
  - explain who owns the customer relationship in a marketplace and in an own store, and what follows for the seller;
  - state the grading components, the checkpoint dates and the AI rules.
- **Cases.** Mexico: Mercado Libre (C2C auctions in its origins, now marketplace, payments and logistics), Amazon México, Liverpool (click and collect), a D2C mezcal brand selling through WhatsApp, Facebook Marketplace (C2C), TikTok Shop México. International: Alibaba (B2B), Etsy, Warby Parker (D2C that later opened stores), the Meta Shops checkout reversal.
- **Lab, "Mapa de 10 negocios":** Teams place ten business cards on a model-by-channel grid and answer the five questions for each. They then propose two channel positions for Molienda and state what control each one costs.
- **Homework:** Form the team and choose the project business: a real micro or small business with an owner willing to answer questions, or one of three backup cases supplied by the instructor. One page covering its current channels and the five questions for each.
- **Quiz:** "Una marca de tenis vende en su tienda propia y en Mercado Libre. ¿Qué cambia entre los dos?"
  - A) The model goes from B2C to C2C.
  - **B) The channel: in the marketplace the platform controls ranking, payment and part of the customer data. ✔**
  - C) Nothing; it is the same customer.
  - D) On Mercado Libre the brand no longer answers for the warranty.
  - Why the distractors: A confuses model with channel. D is a legal misconception that S11 corrects.

### S2 · Cliente, propuesta de valor y evidencia / Customer, value proposition and evidence
- **Original items:** 1.2, 1.3.
- **Mental model:** The evidence ladder. What people *say* (opinions, surveys) ranks below what people *do* (searches, clicks, sign-ups), which ranks below what people *commit* (deposits, pre-orders, purchases). Test the riskiest assumption with the cheapest test that reaches the "commit" rung, and set the pass threshold before you run it.
- **Current instance:** Google Trends for Mexico and Mercado Libre's search autocomplete as free demand signals (verify each term that both still show these data).
- **Topics:**
  1. Segment, job to be done, pains and gains (the customer profile).
  2. The digital value proposition: why buy online, and why from you (assortment, price, convenience, trust, speed).
  3. Assumptions about desirability, viability and feasibility, ranked by risk.
  4. The evidence ladder and its tests: interviews about past behavior, surveys and their biases, landing-page smoke tests, concierge pre-sales on WhatsApp, a single marketplace listing.
  5. Product-market fit as a signal (repeat purchases, unprompted referrals), and the ethics of testing: never charge for what you cannot deliver; advertising must be truthful (LFPC art. 32).
- **Objectives:** the student can
  - write a one-sentence value proposition naming the segment, the job and the alternative it beats;
  - rank five assumptions by risk and pick a test for the riskiest;
  - place six pieces of evidence on the ladder and justify which of them validate demand;
  - rewrite five hypothetical interview questions so they ask about past behavior.
- **Cases.** Mexico: the Molienda subscription idea, a Mercado Libre listing as a demand test, Google Trends for "café de especialidad". International: Zappos' founder photographing shoes in stores before holding any stock (1999); Dropbox's explainer-video waitlist (2008, verify); Buffer's pricing-page smoke test (2010, verify).
- **Lab:** An interview clinic in pairs (turn a bad question into a good one). Then design a one-week test of the Molienda subscription with a pass threshold set in advance, for example "at least 20 refundable deposits from 400 visits".
- **Homework:** Three real interviews for the project business, findings placed on the ladder, and one test proposal with its threshold.
- **Quiz:** "¿Qué evidencia es más fuerte de que la gente pagará una suscripción de café?"
  - A) 80% of 200 survey respondents say they would subscribe.
  - B) 300 likes on the announcement post.
  - **C) 25 people pay a $100 MXN refundable deposit. ✔**
  - D) Three cafetería owners say it is a great idea.
  - Why the distractors: A and D are "say" evidence; B is "do" evidence, but cheap. Only C is a commitment.

### S3 · La economía de un pedido / The economics of an order
- **Original items:** 7.1 (AOV, margin), 1.3 (viability). **Addition:** A1.
- **Mental model:** The order P&L. Start from the price, subtract the cost of goods to get gross margin, then subtract the order's variable costs (payment fee, packaging, any shipping you absorb, marketplace commission, expected returns) to get the **contribution margin per order**. Every later decision in the course moves one line of this P&L.
- **Current instance:** The cost sheet for order #1001 in a spreadsheet. The fee lines are left blank; S4, S7 and S10 fill them from the annex.
- **Topics:**
  1. Consumer prices are total prices, taxes included (LFPC art. 7 Bis). The IVA rate for each product is given in the case.
  2. Gross margin versus markup.
  3. Variable costs per order.
  4. Contribution margin per order and average order value (AOV, "ticket promedio").
  5. Raising AOV without destroying margin: bundles, free-shipping thresholds, volume tiers.
- **Objectives:** the student can
  - calculate gross margin and markup and convert one into the other;
  - build a contribution-per-order statement for three baskets;
  - calculate AOV from an order list;
  - find the lowest free-shipping threshold that keeps contribution positive;
  - show with numbers why an order with positive gross margin can still lose money.
- **Cases.** Mexico: free-shipping thresholds on Mercado Libre and Amazon México (current values in the annex); Buen Fin bundles. International: Webvan's 2001 bankruptcy as a cost-per-order failure; Amazon Prime's shipping logic.
- **Lab:** In a spreadsheet, build the P&L for three Molienda baskets: one 250 g bag; order #1001; one subscription month. Find the basket that loses money, propose one fix (threshold, bundle or price) and test it.
- **Homework:** A cost sheet for three products of the project business, with a source for every number, and the contribution per order.
- **Quiz:** "Compras en $100 y vendes en $150, sin impuestos. ¿Margen bruto y markup?"
  - A) 50% and 50%.
  - **B) 33% and 50%. ✔**
  - C) 50% and 33%.
  - D) 33% and 33%.
  - Why the distractors: swapping margin and markup is the classic error.

### S4 · Plataformas: rentar, comprar o construir / Platforms: rent, buy or build
- **Original items:** 2.1, 2.3 (part). **Additions:** A10, A12.
- **Mental model:** The rent-buy-build continuum.
  - **Marketplace:** you rent traffic and accept its rules.
  - **Hosted SaaS store:** you rent the software.
  - **Self-hosted open source:** you own the software and its upkeep.
  - **Custom, headless or composable:** you build.

  Six axes decide the choice: control, time to launch, cost structure (fixed versus a percentage of sales), ownership of customer data, cost of leaving, and skills needed. Headless means separating the storefront from the commerce engine through APIs. It pays off when several storefronts or teams must change independently, and not before.
- **Current instance:** Each platform's public pricing page and Mercado Libre's seller-fee calculator, recorded with today's date on a tool card (verify the calculator's address each term).
- **Topics:**
  1. The continuum and the six axes.
  2. Marketplace economics and power: commission, fixed fees, fulfillment programs, ranking and reputation, account suspension. Competition context: COFECE's 2024 preliminary finding on marketplaces; the Comisión Nacional Antimonopolio, operating since Oct 2025.
  3. Store economics: subscription plus payment fees plus apps (SaaS) versus hosting, updates and security patches (open source).
  4. The architecture in one picture: storefront, commerce engine, back office and the APIs between them. Headless and composable as decisions about decoupling.
  5. The tool card, introduced here and reused five more times.
- **Objectives:** the student can
  - compare three platform options on the six axes and recommend one in writing;
  - calculate the monthly cost of a marketplace and of a SaaS store at three order volumes and find the crossover point;
  - explain what headless decouples, with one case where it pays and one where it does not;
  - fill in a tool card that names the concept, the instance, the evidence and the exit plan.
- **Cases.** Mexico: Mercado Libre, Amazon México, Tiendanube, Shopify, WooCommerce, Wix; Mercado Shops' closure (the store lived inside someone else's platform). International: Magento 1's end of life (30 Jun 2020) forcing migrations; the MACH Alliance.
- **Lab, "Tres caminos para Molienda":** With an illustrative fee table, teams compute the monthly cost at 50, 300 and 2,000 orders for marketplace-only, a SaaS store and open source. They chart the crossover and fill in a tool card for the option they choose.
- **Homework:** Put together Checkpoint 1, due at the start of S5.
- **Quiz:** "Marketplace: 15% de comisión con ticket de $500. Tienda SaaS: $1,500 al mes más 3% por pago. ¿Desde cuántos pedidos al mes conviene la tienda?"
  - A) 10.
  - **B) 25 ✔**, because 75n = 1,500 + 15n.
  - C) 60.
  - D) 100.
  - Open follow-up: why might the seller stay on the marketplace anyway? (It supplies traffic the store would have to buy; this sets up CAC in S12.)

### S5 · Catálogo y datos de producto / Catalog and product data
- **Original items:** 2.2 (catalog). **Additions:** A4, A11.
- **Mental model:** Online, the product data *is* the product. Keep one record per sellable unit (SKU), with identifiers, attributes and variants, in a single source of truth that publishes to every channel. An error in the record shows up in every channel.
- **Current instance:** Google's Rich Results Test on a live product page, and a GS1 México barcode lookup (verify tool names each term).
- **Topics:**
  1. Product, variant, SKU and bundle; option matrices (grind by size).
  2. Identifiers: the SKU is yours; the GTIN (EAN-13) is global and issued through GS1 (Mexico's prefix is 750); why marketplaces ask for a GTIN.
  3. Attributes and taxonomy. Mandatory commercial information must also appear online: price with taxes, specifications, warranty terms. Labeling norms such as NOM-050-SCFI follow the product, not the medium (verify sector-specific norms).
  4. Content: titles, descriptions, images. AI-written drafts are fact-checked by a person, because the seller answers for every claim.
  5. One record, many outputs: feeds (Google Merchant Center), schema.org `Product` markup, marketplace listings. Code card: a product JSON, `sku`, `variant`, `gtin`, `price {amount, currency: MXN, taxes_included}`, `available`.
- **Objectives:** the student can
  - turn a two-option product into a complete SKU table with a naming convention;
  - distinguish SKU from GTIN and say who assigns each;
  - audit a listing against a required-information checklist;
  - fact-check an AI-written description against a spec sheet;
  - identify which JSON fields a store, a marketplace and a feed each read.
- **Cases.** Mexico: Mercado Libre's required attributes per category, Amazon México matching offers by GTIN. International: Amazon's ASIN; schema.org in search results.
- **Lab:** Build Molienda's six products into a SKU table, then fact-check one AI-written description line by line.
- **Homework:** The project catalog of 10 SKUs, plus one product JSON filled in from the template.
- **Quiz:** "Café en grano o molido, en 250 g o 1 kg. ¿Cuántos SKU?"
  - A) 1.
  - B) 2.
  - **C) 4. ✔**
  - D) 6.
  - Why the distractors: B counts options instead of combinations; A confuses a product with a SKU.

### S6 · Experiencia de usuario, página de producto y embudo / UX, the product page and the funnel
- **Original items:** 3.1, 3.2 (product page), 7.2. **Addition:** A8.
- **Mental model:** Each step must answer the shopper's questions with certainty: is this what I need, can I trust it, what will it cost in total, when will it arrive. The funnel shows where those answers fail. Revenue = sessions × conversion rate × AOV.
- **Current instance:** PageSpeed Insights (LCP, INP and CLS; INP replaced FID on 12 Mar 2024) and an accessibility checker (WAVE or Lighthouse), run on a live Mexican store.
- **Topics:**
  1. Mobile first: navigation, search and filters built on S5's taxonomy.
  2. Anatomy of a product page: images, total price, delivery estimate, variant selector, reviews, returns and warranty, trust signals.
  3. Accessibility: the POUR principles, WCAG 2.2 as the current standard, and what automated checkers miss.
  4. Speed as part of UX: the Core Web Vitals vocabulary.
  5. The funnel: conversion at each step, the largest relative drop, the revenue identity.
  6. Heuristic evaluation (Nielsen's ten heuristics, 1994).
- **Objectives:** the student can
  - calculate each step's conversion and overall CR from funnel counts and find the largest relative drop;
  - rank a product page's three worst issues using the heuristics;
  - find four accessibility failures by combining a checker with a manual keyboard pass;
  - split a change in revenue into sessions, CR and AOV.
- **Cases.** Mexico: the same product compared on Amazon México, Mercado Libre and a small Tiendanube or Shopify store. International: Baymard Institute research; the European Accessibility Act.
- **Lab:** Take apart Molienda's mobile product page using the given funnel data, and decide which step to fix first.
- **Homework:** Audit the team's product page (or prototype) and one competitor's, and write one funnel hypothesis.
- **Quiz:** The funnel is 10,000 sessions, 4,000 product views, 600 add-to-carts, 300 checkouts, 150 purchases. "¿Dónde está la mayor fuga relativa?"
  - A) From session to product view.
  - **B) From product view to cart (85% lost). ✔**
  - C) From cart to checkout.
  - D) From checkout to purchase.
  - Why the distractors: A has the largest *absolute* drop, which is exactly the relative-versus-absolute confusion the question targets.

### S7 · Pagos: cómo se mueve el dinero / Payments: how money moves
- **Original items:** 4.1, 4.2 (payment security). **Addition:** A2.
- **Mental model:** Every payment method trades off four things: who bears the risk, how fast the money settles, what it costs and how many customers can use it. Card payments follow one model: cardholder, issuer, card network, acquirer and merchant, with gateways and payment aggregators (PSPs) in between.
- **Current instance:** Banxico's CEP lookup used on a real SPEI transfer, plus two payment providers' public fee pages recorded in the annex.
- **Topics:**
  1. The card flow: authorization, capture, settlement, payout. Aggregator versus own merchant account.
  2. Mexican payment rails:
     - SPEI: real-time interbank transfers, each with an electronic receipt called a CEP;
     - CoDi (2019): QR codes and payment requests running on SPEI;
     - DiMo (early 2023): transfers to a phone number;
     - Circular 9/2026: standardized mobile transfer flows required by 14 Dec 2026;
     - cash vouchers (OXXO Pay and similar) and cash on delivery.
  3. Credit at checkout: MSI (the merchant pays an extra fee for each installment term), BNPL, wallets.
  4. Cost and settlement: percentage plus fixed fees, MSI surcharges, payout times and the net amount received, carried back into the order P&L.
  5. Payment security as a merchant decision: tokenization and hosted payment fields keep card data out of your systems and shrink your PCI DSS scope; 3-D Secure adds authentication and shifts fraud liability.
  6. International comparison: Pix (Brazil, Nov 2020) and UPI (India, 2016) as public instant-payment rails with mass adoption, and the case of CoDi's low adoption (verify the figures).
- **Objectives:** the student can
  - diagram a card payment from click to payout;
  - compare five methods on risk, speed, cost and reach for a given segment;
  - calculate the net received from the same order paid by card, by MSI 6, by SPEI and by cash voucher;
  - explain what tokenization and 3DS protect against and what they do not;
  - recommend a payment mix from given data on cash and card use (ENIF style).
- **Cases.** Mexico: the SPEI receipt (CEP), DiMo, OXXO Pay, MSI during Buen Fin, Mercado Pago, Kueski Pay, Aplazo. International: Pix, UPI, Klarna, PCI DSS v4.0.1, EMV 3DS.
- **Lab:** Molienda's payment mix. From a segment table and a fee table, choose methods, compute the weighted payment cost per order, and decide whether to offer MSI only on grinders.
- **Homework:** The project's payment mix with a net-received table, plus a tool card for one payment provider.
- **Quiz:** "¿Quién paga los meses sin intereses?"
  - A) The issuing bank, at no cost to anyone.
  - B) The buyer, through hidden interest.
  - **C) The merchant, through a higher fee for each term, which it may build into the price. ✔**
  - D) Banxico.

### S8 · Checkout, confianza y optimización de conversión / Checkout, trust and conversion optimization (Partial 1 week)
- **Original items:** 3.2 (cart, checkout), 3.3, 4.2 (login methods), 8.1 (information required before payment). **Addition:** A6.
- **Mental model:** Friction is any step that reduces neither the shopper's uncertainty nor the merchant's risk. Conversion optimization (CRO) applies the scientific method to friction: diagnose, form a hypothesis, change one thing against a control, and decide with a metric chosen in advance.
- **Current instance:** A free online sample-size calculator. Plus the fact that Google Optimize shut down on 30 Sep 2023 while the testing method stayed the same.
- **Topics:**
  1. Anatomy of a checkout: cart; guest checkout versus account (passkeys and social login as current instances); address; shipping with a delivery date; payment; review. The total price must be visible before payment.
  2. Trust and required information: who the seller is and how to contact them, returns and warranty terms, reviews; PROFECO's Distintivo Digital and NMX-COE-001-SCFI-2018 (both voluntary).
  3. The CRO loop: research, hypothesis (change, metric, direction, reason), prioritization (ICE), test, learn.
  4. A/B testing logic and limits: random assignment, one primary metric, no peeking at results early, sample size. What low-traffic stores do instead: usability tests with five users, or bolder changes.
  5. Honest promotions and social proof: real reference prices, real scarcity. Mexican peak seasons: Buen Fin (13 to 17 Nov 2026) and Hot Sale. Block 3 closes with Partial 1's scope and rules.
- **Objectives:** the student can
  - remove at least three non-essential steps or fields from a checkout, justifying each removal;
  - list the information a Mexican online store must show before payment;
  - write a testable hypothesis from a funnel diagnosis;
  - decide, from a sample-size table, whether an uplift is detectable at a store's traffic;
  - classify six promotions as honest or manipulative.
- **Cases.** Mexico: PROFECO price monitoring during Buen Fin (verify the current program); Mercado Libre's purchase with saved payment details. International: Amazon's 1-Click patent (expired 2017); Booking.com's experimentation culture.
- **Lab:** Molienda's seven-step checkout mockup with about 6,000 sessions a month. Redesign it, write two hypotheses, and check whether an A/B test is feasible. The expected finding is that only large effects are detectable, so a usability test should come first.
- **Homework:** A Partial 1 practice set (20 mixed items drawn from the S1 to S8 quizzes, self-scored), plus the team's checkout redesign for Checkpoint 2.
- **Quiz:** "3,000 sesiones al mes, conversión de 1.5%, se espera +5% relativo con un botón nuevo. ¿Qué haces?"
  - A) Run an A/B test for a week.
  - B) Run an A/B test and check daily until it turns significant.
  - **C) The effect cannot be detected at this traffic in a reasonable time; do qualitative research or test a bolder change. ✔**
  - D) Launch it to everyone and compare with last month.
  - Why the distractors: B is peeking; D mixes the change up with seasonality.

### S9 · Pedidos, inventario y riesgo / Orders, inventory and risk
- **Original items:** 5.1, 4.3, 2.2 (inventory), 8.3 (OMS, APIs, webhooks).
- **Mental model:** An order moves through two independent status tracks. The payment track runs pending, authorized, paid, refunded, disputed. The fulfillment track runs unfulfilled, allocated, shipped, delivered, returned. Every status change is an event that other systems listen for. Inventory: available to sell = on hand minus reserved, and there is one stock for all channels.
- **Current instance:** The webhook event log in a payment sandbox (Mercado Pago or Stripe test mode), shown by the instructor (verify sandbox access each term).
- **Topics:**
  1. The order's statuses on both tracks, and who triggers each change.
  2. Inventory arithmetic, safety stock, overselling across channels during sync delays, and first-expired-first-out for perishables.
  3. APIs versus webhooks (pulling versus being notified); duplicate events and the idea of handling the same event only once; the OMS as the system of record for orders. Code cards: an order JSON (`order_id: "1001"`, `payment_status`, `fulfillment_status`, `items` with SKUs, `total` in MXN) and a webhook (`event_id`, `type: "order.paid"`, `created_at: "2026-11-14T10:32:05-06:00"`).
  4. Fraud patterns: stolen cards in online purchases, account takeover, "friendly fraud" (a real buyer who disputes a legitimate charge), promo abuse, triangulation. Warning signals and rules; approve, review or reject.
  5. Chargebacks: the process, the evidence that wins (proof of delivery, the 3DS result) and the cost. In Mexico, the cardholder disputes an unrecognized charge with the issuing bank (verify the current deadlines in CONDUSEF guidance).
- **Objectives:** the student can
  - trace both status tracks of an order through three scenarios (normal, cancelled before shipping, charged back after delivery);
  - calculate available stock across two channels and identify the window in which overselling can happen;
  - read an order JSON and a webhook and name the system that should react;
  - score three orders against a given fraud rule set and justify each decision;
  - list the evidence needed to contest a chargeback.
- **Cases.** Mexico: Mercado Libre and Mercado Pago notifications (verify naming); cash-voucher orders that wait as "pending until paid or expired". International: Shopify's separate financial and fulfillment statuses; rule-based fraud screening of the Stripe Radar kind.
- **Lab, "El viaje del pedido #1001":** A shuffled event log containing a duplicated webhook and a stock conflict between the store and Mercado Libre. Teams rebuild the order's history in a `trace` table, find the oversell and decide on three suspicious orders.
- **Homework:** The project's order lifecycle diagram, inventory policy and five fraud rules (part of Checkpoint 2).
- **Quiz:** "El webhook `order.paid` del pedido 1001 llega dos veces con el mismo `event_id`. ¿Qué debe pasar?"
  - A) Two shipments.
  - **B) The system recognizes the event and ignores the repeat. ✔**
  - C) The order is cancelled.
  - D) One payment is refunded.

### S10 · Fulfillment y última milla / Fulfillment and the last mile
- **Original items:** 5.2, 5.3 (dropshipping, 3PL), 8.3 (WMS). **Addition:** A5.
- **Mental model:** The delivery promise is a product feature that costs money. The promise (date, speed, price) depends on where the stock is, the order cutoff time, the carrier and the service level. Fulfillment options range from most control to least effort: in-house, third-party logistics (3PL), marketplace fulfillment, dropshipping.
- **Current instance:** Live quotes from a multi-carrier platform for the same parcel from CDMX to Mérida, recorded and compared.
- **Topics:**
  1. The warehouse flow (receive, store, pick, pack, ship), the WMS and packaging.
  2. Fulfillment models, including marketplace programs (Mercado Envíos Full, Logística de Amazon) and dropshipping, where legal responsibility to the consumer stays with the seller.
  3. Carriers and the last mile: parcel carriers, aggregators, same-day couriers, pickup points, failed deliveries. The December 2024 platform-worker labor reform (IMSS pilot from 1 Jul 2025, in full effect Jan 2026) as a cost driver for app-based delivery (verify how it applies to each courier model).
  4. Shipping economics: billable weight (actual versus volumetric), zones, who pays, and the S3 free-shipping threshold revisited.
  5. Cross-border: the 33.5% courier rate for imports from countries without a trade agreement with Mexico (verify), and export basics.
- **Objectives:** the student can
  - calculate billable weight for three box sizes and its effect on shipping cost;
  - compare four fulfillment models on control, cost, speed and risk and recommend one;
  - design a delivery promise consistent with stock location and carrier capacity;
  - explain who answers to the consumer when a dropshipped product fails.
- **Cases.** Mexico: Mercado Envíos Full, Logística de Amazon, Estafeta, DHL, FedEx, Paquetexpress, 99minutos, Liverpool click and collect, Shein and Temu after the courier rate change. International: Zara's ship-from-store; Amazon's 2023 regionalization of its US network.
- **Lab:** For Molienda, choose a fulfillment model at three volumes, compute billable weight for three boxes, write delivery promises for CDMX, Guadalajara, Monterrey and Mérida, and fill in a tool card for one logistics provider.
- **Homework:** The project's fulfillment plan and delivery promise, with shipping cost carried into the order P&L.
- **Quiz:** "Caja de 40 × 30 × 20 cm, pesa 3 kg, divisor volumétrico 5,000. ¿Peso facturable?"
  - A) 3 kg.
  - **B) 4.8 kg. ✔**
  - C) 24 kg.
  - D) 7.8 kg.
  - Why the distractors: C forgets the divisor; D adds the two weights.

### S11 · Devoluciones, posventa y facturación / Returns, after-sales and invoicing
- **Original items:** 5.3 (returns, refunds, reverse logistics), 8.1 (warranties and returns). **Addition:** A3.
- **Mental model:** After-sales is where the promise is kept or broken, and it has four parts. The **legal floor** is what the store cannot take away. The **policy** is what it chooses to add. The **economics** is return rate times cost per return. The **paper trail** is that every invoiced sale and every refund leaves a CFDI.
- **Current instance:** SAT's CFDI verification portal, used on a real invoice the student has received.
- **Topics:**
  1. The consumer's legal rights:
     - a warranty of no less than 90 days (LFPC art. 77);
     - five business days to revoke consent (LFPC art. 56; PROFECO applies it to online purchases, verify the scope case by case);
     - PROFECO's Concilianet and Buró Comercial.
  2. Designing the returns policy (window, condition, who pays return shipping, exchange or refund or store credit) and customer service (channels, response times, public replies to reviews). Return reasons feed back into the catalog (S5).
  3. Reverse logistics and its cost: return label, inspection, restock, refurbish, liquidate or destroy.
  4. Refunds by payment method: card reversal, SPEI, and cash vouchers, which require the customer's bank details. Revisits S7.
  5. CFDI for e-commerce:
     - what CFDI 4.0 needs from the customer: RFC, name, tax regime, postal code and invoice use;
     - self-invoicing portals, and the global invoice for sales to the general public;
     - a CFDI de egreso (credit note) when an invoiced sale is refunded;
     - marketplace withholding of ISR and IVA from sellers, and SAT's online access to platforms (CFF art. 30-B).
- **Objectives:** the student can
  - separate legal entitlement from store policy in four after-sales cases;
  - calculate returns cost per 100 orders and its effect on contribution;
  - list the data a CFDI 4.0 needs and the document issued when an invoiced sale is refunded;
  - design a returns policy that is compliant, clear and viable for a given product category.
- **Cases.** Mexico: Concilianet, the SAT verification portal, Mercado Libre's buyer protection (verify the current name), Amazon México returns. International: the EU's 14-day withdrawal right; "bracketing" in fashion (buying several sizes to return most).
- **Lab:** Molienda's after-sales desk handles six cases: a damaged grinder, the wrong grind, a change of mind on day 3, an invoice requested a month later, a refund of an invoiced order, and a review complaining of late delivery. For each: the customer's right, the action, the cost and the CFDI document.
- **Homework:** The project's returns and warranty policy, after-sales cost estimate and invoicing flow (part of Checkpoint 3).
- **Quiz:** "El cliente pidió factura y luego devolvió el producto. ¿Qué corresponde?"
  - A) Nothing; the original CFDI stands.
  - B) Delete the original from the system.
  - **C) Issue a CFDI de egreso related to the original, or cancel the original if SAT's rules allow it. ✔**
  - D) Issue a new income CFDI with a negative amount.

### S12 · Adquisición: llegar al cliente correcto / Acquisition: reaching the right customer
- **Original items:** 6.1, 6.2, 1.1 (social commerce).
- **Mental model:** Media is owned, earned or paid. Channels either **capture** demand that already exists (search, marketplaces) or **create** it (social media, creators). Every channel buys customers at a cost per acquisition (CAC). A campaign pays for itself only when its return on ad spend (ROAS) beats the **break-even ROAS**, which is 1 ÷ contribution margin %.
- **Current instance:** The Meta Ad Library and Google Ads Transparency Center, used to read a competitor's live ads (both are public).
- **Topics:**
  1. Owned, earned and paid media; capturing versus creating demand.
  2. Search: SEO fundamentals (crawling, indexing, relevance, authority, S5's structured data), search ads and shopping ads. AI-generated answers in search and in chat assistants as the current change in what "being found" means.
  3. Social and creator commerce: UGC, reviews, influencers with clear disclosure, live shopping, TikTok Shop México.
  4. Ads sold by retailers and marketplaces: Mercado Ads, Amazon Ads.
  5. Campaign tagging: UTM parameters and naming conventions. Code card: `https://molienda.mx/suscripcion?utm_source=instagram&utm_medium=social&utm_campaign=buenfin2026_suscripcion&utm_content=reel_tueste`. Then the economics: CPC, CTR, CR, CAC, ROAS and break-even ROAS.
- **Objectives:** the student can
  - classify a business's channels as capture or creation and as owned, earned or paid;
  - calculate CAC and ROAS and compare ROAS with the break-even ROAS;
  - build UTM links for three campaigns following a convention;
  - assess an influencer post for disclosure and expected CAC;
  - explain which fundamentals still decide visibility when AI answers replace a list of links.
- **Cases.** Mexico: TikTok Shop México, Mercado Ads, Hot Sale and Buen Fin campaigns. International: the FTC's endorsement guides and fake-review rule; Glossier's community-led growth.
- **Lab:** Molienda's campaign table (Meta, Google, Mercado Ads and one creator). Compute CAC, ROAS and break-even ROAS, reallocate the budget and tag three links. It closes with a puzzle left open on purpose: Meta reports 40 purchases, analytics 25 and the store 32. Why? S13 answers it.
- **Homework:** The project's acquisition plan: budget, expected CAC, break-even ROAS, UTM convention, and an analysis of a competitor's ads.
- **Quiz:** "Margen de contribución de 25%. ¿ROAS mínimo para no perder dinero en la campaña?"
  - A) 1.25.
  - B) 2.5.
  - **C) 4. ✔**
  - D) 25.

### S13 · Medición y decisiones / Measurement and decisions (Partial 2 week)
- **Original items:** 7.1, 7.2, 7.3, 8.1 (consent for tracking). **Addition:** A9.
- **Mental model:** Measure decisions, not data. A KPI tree runs from contribution profit down to its drivers. Event-based analytics records each thing that happened, with its parameters. Every number has a source, a definition and a known bias.
- **Current instance:** The GA4 demo account (the Google Merchandise Store), free and read-only (verify access each term). GA4 replaced Universal Analytics, which stopped processing data on 1 Jul 2023.
- **Topics:**
  1. The KPI tree: contribution profit = orders × contribution per order − marketing − fixed costs, and orders = sessions × CR. Guardrail metrics (return rate, margin) keep a gain in one number from hiding a loss in another.
  2. Events and parameters: `view_item`, `add_to_cart`, `begin_checkout`, `purchase`. Code card: a `gtag("event", "purchase", {...})` call with `transaction_id: "1001"`, `value: 2068.00`, `currency: "MXN"` and two items.
  3. The measurement plan: business question, metric, event, parameters, owner.
  4. Why the numbers disagree: attribution models and windows; consent and blocked cookies; ad blockers; switching devices; ad platforms crediting themselves.
     - Which source answers what: the order system is the truth for orders, analytics for behavior, ad platforms for ad delivery.
     - Consent: non-essential cookies need consent, declared in the privacy notice.
     - Context: Chrome kept third-party cookies, Safari blocks them by default, and Apple's ATT limits mobile identifiers.
  5. Dashboards that change decisions: few metrics, comparisons, segments, no vanity metrics. Block 3 closes with Partial 2's scope and rules.
- **Objectives:** the student can
  - build a KPI tree linking contribution profit to at least six drivers;
  - map three business questions to events and parameters;
  - find missing or wrong parameters in a purchase event;
  - explain three reasons the three data sources disagree, and which source answers which question.
- **Cases.** Mexico: Molienda's Buen Fin dashboard; Mercado Libre's seller metrics. International: the Universal Analytics shutdown, ATT, the retirement of Privacy Sandbox.
- **Lab:** Explore the GA4 demo account (funnel; traffic acquisition by UTM). Write Molienda's measurement plan and build the reconciliation table that resolves the S12 puzzle.
- **Homework:** A Partial 2 practice set (mixed items from S9 to S13 plus S3), and the team's measurement plan and KPI tree for Checkpoint 3.
- **Quiz:** "El evento `purchase` llega sin `transaction_id`. ¿Cuál es el riesgo?"
  - A) None.
  - **B) Reloading the thank-you page counts the purchase twice and inflates revenue. ✔**
  - C) GA4 rejects every event.
  - D) The customer is not charged.

### S14 · Retención y valor del cliente / Retention and customer value
- **Original items:** 6.3, 7.1 (LTV), 8.3 (CRM). **Addition:** A7.
- **Mental model:** A customer is a member of a cohort (the group who first bought in the same period), not a single transaction. The chain runs from the retention curve to the repeat rate, to contribution-based LTV, to LTV:CAC and payback. Message customers by behavioral segment, and only with their consent.
- **Current instance:** Reading the SPF, DKIM and DMARC results of a brand's email through Gmail's "Show original". Gmail and Yahoo have required these from bulk senders since Feb 2024.
- **Topics:**
  1. Cohorts, retention curves and repeat-purchase rate.
  2. Contribution-based LTV, LTV:CAC and the payback period (revisits S12).
  3. RFM segmentation (recency, frequency, monetary value) in a spreadsheet; the CRM as the system of record for customers.
  4. Lifecycle messages (welcome, post-purchase, replenishment, win-back) by email, WhatsApp Business with opt-in, and SMS. Consent and opt-out under the 2025 data law; REPEP, PROFECO's do-not-contact registry for phone marketing.
  5. Loyalty programs, subscriptions and remarketing:
     - The December 2025 LFPC reform (art. 76 Bis, fractions VIII and IX) requires clear disclosure of recurring charges, express consent, notice at least five calendar days before an automatic renewal, and cancellation without penalty (verify operating details against PROFECO guidance).
     - First-party versus third-party data, and why remarketing audiences have shrunk.
- **Objectives:** the student can
  - build a cohort table and read its retention curve;
  - calculate LTV and LTV:CAC and judge whether a channel's CAC can be sustained;
  - segment customers with RFM and propose one message per segment;
  - design a subscription sign-up and cancellation flow that meets the December 2025 requirements;
  - distinguish first-party from third-party data and the consent each requires.
- **Cases.** Mexico: Molienda's subscription; Mercado Libre's loyalty program (current name in the annex). International: the FTC v. Amazon Prime settlement (Sep 2025, $2.5 billion, over enrollment and cancellation); Starbucks Rewards; the FTC's "click to cancel" rule, vacated by a US appeals court on 8 Jul 2025 (regulations can disappear too).
- **Lab:** From a 12-month order export (a CSV of about 500 rows), build a cohort table, RFM segments and LTV. Then design a compliant subscription flow on paper.
- **Homework:** The project's retention plan: LTV, segments and consent mechanism. This completes Checkpoint 3, due at the start of S15.
- **Quiz:** "La suscripción se renueva sola cada mes. Con la reforma de diciembre de 2025, ¿qué debe hacer el proveedor?"
  - A) Nothing beyond the terms and conditions.
  - **B) Disclose the recurring charge clearly, obtain express consent, notify before automatic renewal and allow cancellation without penalty. ✔**
  - C) Email a receipt after each charge.
  - D) Ask PROFECO for permission.

### S15 · Ley, privacidad y ética / Law, privacy and ethics
- **Original items:** 8.1, 8.2, 4.2 (privacy).
- **Mental model:** There are three layers: the law (the floor), the platform's rules (a contract) and what you ought to do (ethics). Add data minimization: collect only what has a stated purpose, and keep it only while that purpose lasts.
- **Current instance:** The DOF text of the 2025 LFPDPPP read side by side with a real Mexican store's privacy notice.
- **Topics:**
  1. Consumer protection, consolidated: the compliance cards from S3, S5, S8, S11, S13 and S14 become one checklist (LFPC arts. 7 Bis, 32, 56, 76 Bis and 77; NMX-COE-001-SCFI-2018; the Distintivo Digital; electronic contracts under the Código de Comercio).
  2. Personal data:
     - the 2025 LFPDPPP (DOF 20 Mar 2025, in force 21 Mar 2025), now supervised by the Secretaría Anticorrupción y Buen Gobierno;
     - the privacy notice, consent and ARCO rights (access, rectification, cancellation, opposition);
     - the third parties that process data for the store (payment provider, carriers, email tools), and security incidents;
     - GDPR as the comparison for stores selling into the EU.
  3. Intellectual property: trademarks (IMPI), copyright over photos and text (INDAUTOR), counterfeits and marketplace brand-protection programs, licenses for images, fonts and AI outputs.
  4. Dark patterns: false urgency, drip pricing, confirmshaming, hard-to-cancel flows, preselected add-ons, nagging. International instances: FTC v. Amazon and EU DSA art. 25.
  5. Responsible AI in commerce: truthful AI-generated content, disclosing chatbots (EU AI Act art. 50 transparency duties apply from 2 Aug 2026), fairness in personalized pricing. Responsibility stays with the seller.
- **Objectives:** the student can
  - audit a store against the Mexican checklist and rank the findings by risk;
  - write the core elements of a privacy notice for a given data flow;
  - name the dark pattern in five screens and propose a compliant alternative for each;
  - decide whether a given image, text or AI output may be used, citing the rule;
  - compare one Mexican obligation with its EU or US counterpart and say which applies to a Mexican store selling abroad.
- **Cases.** Mexico: the Secretaría Anticorrupción y Buen Gobierno, PROFECO, IMPI. International: FTC v. Amazon, the EU DSA, the EU AI Act.
- **Lab, "Auditoría legal de Molienda":** Fifteen screenshots (checkout, cookie banner, subscription flow, product page, privacy notice). Find the violations and dark patterns, rewrite each, and draft the elements of a privacy notice.
- **Homework:** For the final project report: a compliance checklist, a draft privacy notice and a dark-pattern self-audit.
- **Quiz:** "La tienda muestra 'Solo quedan 2' en todos los productos, sin importar el inventario. ¿Qué es?"
  - A) Social proof.
  - B) Legitimate scarcity marketing.
  - **C) False scarcity: a dark pattern and misleading advertising. ✔**
  - D) Personalization.

### S16 · Evaluar la siguiente herramienta / Evaluating the next tool (project week)
- **Original items:** 2.3, 8.3 (consolidated), 1.1 (conversational commerce, now led by assistants), 8.2 (AI). **Addition:** A12.
- **Mental model:** Concept, instance, half-life. Every tool is an instance of a durable job. Evaluate it with the tool card and the five control questions. Adopt it in a way you can undo, with a metric and a stop rule decided beforehand.
- **Current instance:** The checkout-inside-the-platform case, with dates:
  - Meta's in-app Shops checkout, made mandatory for new US shops in 2023 and discontinued on 4 Sep 2025 (verify);
  - OpenAI's Instant Checkout, launched 29 Sep 2025 with its Agentic Commerce Protocol and scaled back in March 2026 toward product discovery that sends buyers to the merchant's own checkout;
  - Google's Universal Commerce Protocol, announced Jan 2026;
  - TikTok Shop's in-app checkout in Mexico, live since Feb 2025.
- **Topics:**
  1. The systems map assembled from S9 to S14: storefront, commerce engine, payment provider, OMS, WMS or 3PL, ERP and CFDI, CRM, analytics. Integration patterns (API, webhook, file or feed, middleware) and one system of record per type of data.
  2. Headless and composable revisited on the map: when decoupling pays.
  3. Hype versus evidence. The course's "instance graveyard": Universal Analytics, Google Optimize, FID, Magento 1, Mercado Shops, INAI, COFECE, Privacy Sandbox, Meta's Shops checkout.
  4. The checkout-inside-the-platform case worked through the five control questions.
  5. A pilot plan you can undo: hypothesis, metric, duration, stop rule, exit. Block 3: project pitches and logistics.
- **Objectives:** the student can
  - draw a systems map naming the system of record for orders, stock, customers and invoices, and how each pair connects;
  - evaluate an emerging tool with the tool card, naming the gaps in its evidence;
  - write a pilot plan with a decision metric and a stop rule;
  - explain with the checkout case why control of the customer relationship decides whether a channel gets adopted.
- **Lab (25 minutes):** Each team draws one trend card (assistant-led checkout, live shopping, ads sold by retailers, passkeys, social marketplaces) and produces a tool card and a pilot plan for Molienda. Pitches follow.
- **Homework:** Deliver the final project report. For the final exam, a 300-word reflection: choose one retired instance and explain what replaced it and which concept survived.
- **Quiz:** "Un proveedor asegura que su agente de IA 'sube las ventas 40%'. ¿Qué evidencia basta para adoptarlo?"
  - A) The vendor's case study.
  - B) Three testimonials.
  - **C) A test on our own traffic, with a metric and a stop rule set beforehand. ✔**
  - D) The number of companies using it.

### S17 · Evaluación final / Final assessment
- **Original items:** all of them.
- **Content:** The exam's scope by phase; the four costliest errors from the two partials, with corrections; one practice item per phase; the instance graveyard as review; exam rules (format, materials, how to submit). Built on the COM102 `w17` pattern.
- **Objectives:** the student can
  - locate each exam topic in the session and lab that practiced it;
  - recognize the frequent errors;
  - practice with mixed items rather than rereading slides;
  - sit the exam with no doubts about its format.
- **Lab:** A practice round in pairs: eight items, two from each phase.
- **Homework:** None. The final exam takes place this week.
- **Quiz:** "En Buen Fin la conversión de Molienda subió, el ticket bajó y la contribución por pedido cayó. ¿Qué revisas primero?"
  - A) The design of the home page.
  - **B) Contribution by order and by payment method, because discounts and MSI may have pulled in low-margin orders. ✔**
  - C) The number of sessions.
  - D) The SEO ranking.

---

## 4. Assessment plan

### 4.1 Weights

| Component (es / en) | Covers | When | Weight |
|---|---|---|---|
| Parcial 1 / Midterm 1 | S1 to S8 | End of week 8 | 20 % |
| Parcial 2 / Midterm 2 | S9 to S13, plus S3's economics | End of week 13 | 20 % |
| Proyecto integrador / Capstone project | Everything, in three checkpoints and a final delivery | Checkpoints due at the start of S5, S10 and S15; final in S16 | 25 % |
| Examen final / Final exam | Cumulative, weighted toward S14 to S16 and integration | Week 17 | 20 % |
| Tareas y laboratorios / Homework and labs | Weekly work | All term | 15 % |

**Project 25 %:** three checkpoints at 3 % each, the final project report at 10 %, and the pitch plus an individual oral defense at 6 %. A peer-evaluation factor (0.8 to 1.1) adjusts the team-graded parts for each student.

**Homework and labs 15 %:** homework counts 10 % (the best 10 of 12 graded items: S1 to S7, S9 to S12, S14). Lab sheets count 5 %, graded complete or incomplete at the end of class. Retrieval openers and the practice sets in exam weeks are not graded.

**Why 25/15 rather than the house 5 × 20:** the project is the most authentic assessment and the only one that touches all seven learning outcomes. **If the academy requires five components at 20 % each:** the project takes 20 % (report 10, pitch and defense 5, checkpoints 5) and homework and labs take 20 %.

### 4.2 Exam design rules
- Each exam is about 60 % a case with given data (calculate, decide, justify) and 40 % short items written like the session quizzes, whose wrong options are built from the common misconceptions.
- No item needs a brand, version, fee or date from memory. When a figure is needed, the question gives it. For legal content, students must know the principle ("the total price includes taxes"), not the article number.
- Calculators are allowed. No formula sheet: the course's eight formulas are practiced in the openers all term.
- One item bank serves both languages, with identical answer options in identical order.
- Feedback loop: the most-missed items of each partial come back in the S9 and S14 openers.

### 4.3 Running project: "Plan de comercio electrónico para un negocio real"

Teams of three or four work on a real micro or small business, or on one of three backup cases. Molienda is not allowed, because it is the in-class case. No real customer personal data may appear in any deliverable.

| Checkpoint | Due | Contents | Built from |
|---|---|---|---|
| CP1 | Start of S5 | The business and the five control questions; segment and value proposition; validation evidence placed on the ladder; order P&L for three products; platform decision with a tool card | S1 to S4 |
| CP2 | Start of S10 | A 10-SKU catalog and a product JSON; product page audit and redesign; payment mix with net-received table; checkout redesign; order lifecycle diagram, inventory policy and fraud rules | S5 to S9 |
| CP3 | Start of S15 | Fulfillment plan and delivery promise; returns, warranty and invoicing flow; acquisition plan with CAC and break-even ROAS; KPI tree and measurement plan; retention plan with LTV and consent | S10 to S14 |
| Final | S16 | All of the above revised, with a log of changes made after feedback; compliance checklist and privacy notice (S15); systems map; one emerging tool evaluated with the tool card plus a pilot plan; 6-minute pitch | S1 to S16 |

**Check that the project never runs ahead of the course:** the final report needs nothing that is first taught in S16.
- The tool card comes from S4.
- The pilot logic (hypothesis, metric, stop rule) comes from S8.
- Each piece of the systems map was introduced between S9 and S14.

Students may build a working prototype on any platform's free trial, using the payment sandbox only, or a clickable prototype. The grade is for decisions, not for the tool.

**Rubric for the final report and pitch:**

| Criterion | Weight | Meets the standard when |
|---|---|---|
| Evidence | 15 % | Every number has a source, and the validation reaches at least the "do" rung |
| Economics | 20 % | The order P&L is complete and consistent with the payment, shipping, returns and CAC choices |
| Experience design | 15 % | Catalog, product page and checkout pass the session checklists, and accessibility was checked |
| Operations | 15 % | Order lifecycle, fraud rules, delivery promise and returns policy fit the business |
| Growth and measurement | 15 % | CAC compared with break-even ROAS; KPI tree; measurement plan; LTV-based retention plan |
| Compliance and ethics | 10 % | Checklist passed, privacy notice drafted, no dark patterns |
| Tool evaluation | 10 % | One emerging tool evaluated on the tool card, with a pilot plan that can be undone |

**AI policy** (the same as in the COM102 approach): AI may be used for drafting and brainstorming. Every number needs a source, and every AI-generated claim is fact-checked (the S5 skill). In the oral defense, any member can be asked to explain any number in the report.

### 4.4 Alignment of outcomes, practice and assessment

| CLO | Taught | Practiced in | Assessed in |
|---|---|---|---|
| CLO1 Model | S1, S4, S12, S16 | S1 and S4 labs | P1, CP1, Final |
| CLO2 Economics | S3, S4, S6, S7, S10 to S14 | S3, S4, S7, S10, S12 and S14 labs | P1, P2, every checkpoint, Final |
| CLO3 Design | S5 to S8 | S5 to S8 labs | P1, CP2 |
| CLO4 Operate | S9 to S11 | S9 to S11 labs | P2, CP2, CP3 |
| CLO5 Grow and measure | S12 to S14 | S12 to S14 labs | P2, CP3, Final |
| CLO6 Govern | Compliance cards in S3, S5, S8, S11, S13, S14; S15 | S11, S14 and S15 labs | P1 (S8 required information), P2 (S11), project report, Final |
| CLO7 Evaluate | S4, S7, S10, S12, S13, S16 | Tool cards in labs and homework; S16 lab | Project report, Final |

---

## 5. Current-stack annex, as of 5 October 2026

Rule: the syllabus names the concept; this annex names today's instance. Lab numbers are labeled "illustrative" so that fee changes do not invalidate them.

### 5.1 Platforms and channels

| Instance | Concept | Status, Oct 2026 | Re-check each term |
|---|---|---|---|
| Mercado Libre (with Mercado Pago, Mercado Envíos, Mercado Ads) | Marketplace with its own payments, logistics and ads | Market leader in Mexico | Fees by category, free-shipping threshold, reputation rules, loyalty program name |
| Amazon México (Logística de Amazon, Amazon Ads) | Marketplace | Active | Seller fees, fulfillment program fees |
| TikTok Shop México | Social marketplace with in-app checkout | Open since 13 Feb 2025 | Allowed categories, fees |
| Walmart, Liverpool and Coppel marketplaces | Retailer-run marketplaces | (verify each seller program) | Whether each program is still open to sellers |
| Facebook and Instagram Shops; WhatsApp Business catalog | Social catalog plus ads; conversational selling | In-app checkout ended 4 Sep 2025 (verify) | Checkout model, WhatsApp pricing |
| Shopify, Tiendanube, WooCommerce, Wix | Hosted SaaS and open-source store software | Active | Plans, transaction fees; **whether Shopify Payments is available in Mexico (sources conflict, verify)** |
| VTEX, Adobe Commerce, Salesforce Commerce Cloud, commercetools | Enterprise and composable commerce | Active | Only as examples of the upper end of the continuum |
| Mercado Shops | Store builder inside a marketplace | **Discontinued** in 2025 (verify date) | Graveyard |

### 5.2 Payments

| Instance | Concept | Status | Re-check |
|---|---|---|---|
| SPEI with its CEP receipt; CoDi; DiMo | Public instant-payment rails | Circular 9/2026: banks must standardize mobile, DiMo, CoDi and QR flows by **14 Dec 2026** | Whether banks complied; any new transfer experience |
| Mercado Pago, Stripe, Conekta, Openpay (BBVA), Clip, PayPal, Kushki (verify) | Payment gateways and aggregators | Active | Fees, MSI surcharges, payout times, supported methods |
| OXXO Pay and other cash-voucher networks | Cash payments for online orders | Active | Supported providers, voucher expiry |
| Kueski Pay, Aplazo; Mercado Pago's credit without a card (verify name) | BNPL and installments | Active (verify each provider's regulatory status) | Availability, fees |
| Apple Pay, Google Wallet, Mercado Pago and PayPal wallets | Stored-credential wallets | (verify bank coverage) | Coverage |
| PCI DSS v4.0.1; EMV 3-D Secure 2.x; passkeys (FIDO2/WebAuthn) | Payment and login security standards | v4.0 retired 31 Dec 2024; future-dated requirements binding since 31 Mar 2025 | Any new PCI DSS version |

### 5.3 Logistics
- **Instances:** Mercado Envíos Full; Logística de Amazon; Estafeta, DHL Express, FedEx, Paquetexpress, 99minutos; multi-carrier aggregators such as Skydropx and Envia.com (verify); pickup-point networks.
- **Re-check each term:** rates, each carrier's volumetric divisor, coverage, the courier import rate for countries without a trade agreement (33.5% since 15 Aug 2025, verify), and how the platform-worker labor rules apply to delivery apps.

### 5.4 Marketing, CRM and AI-driven discovery
- **Ads:** Google Ads, Meta Ads, TikTok Ads, Mercado Ads, Amazon Ads.
- **Transparency tools:** Meta Ad Library, Google Ads Transparency Center.
- **Email and CRM:** Klaviyo, Mailchimp, HubSpot, Brevo.
- **WhatsApp Business Platform:** re-check its pricing model.
- **Email authentication:** SPF, DKIM and DMARC (bulk-sender requirements since Feb 2024).
- **AI-driven discovery:** Google AI Overviews and AI Mode; ChatGPT product discovery after Instant Checkout was scaled back (Mar 2026). OpenAI's Agentic Commerce Protocol (Sep 2025) and Google's Universal Commerce Protocol (Jan 2026).
- **Re-check each term:** availability in Mexico, and which protocols merchants actually use.

### 5.5 Analytics and experimentation
- **Instances:** GA4 and its demo account, Google Tag Manager, Looker Studio, Microsoft Clarity, Hotjar, Meta Conversions API, PageSpeed Insights (Core Web Vitals: LCP, INP, CLS), WAVE and Lighthouse, Google Trends, free sample-size calculators, A/B tools (platform-native, VWO, Optimizely, AB Tasty; verify).
- **Re-check each term:** GA4's recommended ecommerce events, Core Web Vitals thresholds, demo-account access, tracking-cookie policies in Chrome and Safari.

### 5.6 Mexican regulators and laws

| Body or instrument | What it governs | Status, Oct 2026 | Re-check |
|---|---|---|---|
| PROFECO; LFPC | Consumer rights online: art. 7 Bis total price, art. 32 truthful advertising, art. 56 revocation, art. 76 Bis electronic transactions, art. 77 minimum 90-day warranty | Art. 76 Bis fractions VIII and IX (recurring charges) published in the DOF on 12 Dec 2025, in force since 13 Dec 2025 | New reforms; Buen Fin and Hot Sale guidance |
| NMX-COE-001-SCFI-2018; Distintivo Digital PROFECO and its e-commerce code of ethics | Voluntary e-commerce standard and badge | In force since 1 May 2019 | Requirements for the badge |
| Secretaría Anticorrupción y Buen Gobierno; LFPDPPP 2025 | Private-sector personal data | Law published in the DOF 20 Mar 2025; INAI dissolved | Whether a new reglamento or guidelines have been issued (verify) |
| SAT | CFDI 4.0 (mandatory since 1 Apr 2023); withholding from marketplace sellers (since Jun 2020, rates changed in 2026, verify); CFF art. 30-B, online access to platforms (since 1 Apr 2026) | Active | The annual Resolución Miscelánea, CFDI catalogs, withholding rates |
| Banxico | SPEI, CoDi, DiMo; Circular 9/2026 | Deadline 14 Dec 2026 | Whether banks complied |
| CNBV and CONDUSEF; Ley Fintech (2018) | Payment institutions; cardholder disputes | Active | Dispute deadlines; how BNPL is regulated (verify) |
| IMPI (LFPPI 2020); INDAUTOR (LFDA) | Trademarks; copyright | Stable | |
| Comisión Nacional Antimonopolio | Competition, including the marketplace market | Replaced COFECE (reform DOF 16 Jul 2025; operating since 17 Oct 2025) | Any new marketplace investigation |
| STPS and IMSS; Ley Federal del Trabajo, platform-worker chapter | Delivery and ride app workers | Reform Dec 2024; IMSS pilot Jul to Dec 2025; full effect Jan 2026 | Rules for delivery couriers |
| Customs regime for courier imports | Low-value imports | 33.5% global rate for countries without a trade agreement, since 15 Aug 2025 (verify current) | Rate changes |
| Código de Comercio (electronic commerce provisions); NOM-151-SCFI-2016 | Electronic contracts; preserving data messages | Stable | |
| NOM-050-SCFI-2004 and sector norms | Commercial product information | (verify how each applies to online display) | |
| **NOM-247-SE-2021** | **Residential real-estate** information, advertising and contracts (DOF 22 Mar 2022) | In force; **not a general e-commerce norm** | Use only as an example of a sector norm that reaches websites |

### 5.7 International references
- **EU, data and platforms:** GDPR (2018); DSA (applies to all platforms since 17 Feb 2024; art. 25 on dark patterns); DMA.
- **EU, consumers and accessibility:** Consumer Rights Directive (14-day withdrawal right); Omnibus Directive (since 28 May 2022: price reductions, reviews); European Accessibility Act (28 Jun 2025).
- **EU, AI:** AI Act art. 50 transparency duties apply from 2 Aug 2026. The Digital Omnibus delayed the high-risk duties, not these (verify the exact date for watermarking).
- **United States, FTC:** endorsement guides (2023); fake-review rule (in force Oct 2024); the "click to cancel" rule, vacated on 8 Jul 2025; FTC v. Amazon settlement of $2.5 billion (25 Sep 2025).
- **Standards and public rails:** WCAG 2.2; PCI DSS v4.0.1; Pix (Brazil); UPI (India).

### 5.8 Data sources and calendar
- **Data:** INEGI's ENDUTIH survey (internet use); ENIF, the national financial inclusion survey (INEGI and CNBV); AMVO's annual online sales study; Banxico's SPEI statistics. Each term, re-check that the latest edition is the one cited.
- **Calendar:** Buen Fin 2026 runs 13 to 17 Nov 2026. In a fall term it falls around S12 and S13, so it becomes the live case. Hot Sale (run by AMVO) is in late May or early June (verify the dates each year) and serves as the live case in a spring term.

### 5.9 Instance graveyard (material for S16)

| Retired instance | Replaced by, or what survived | When |
|---|---|---|
| Universal Analytics | GA4; event-based measurement | 1 Jul 2023 |
| Google Optimize | No free Google successor; the method of controlled experiments | 30 Sep 2023 |
| FID | INP; measuring responsiveness | 12 Mar 2024 |
| Magento 1 | Migrations; lesson about upkeep and the cost of leaving | 30 Jun 2020 |
| CFDI 3.3 | CFDI 4.0 | 1 Apr 2023 |
| PCI DSS 3.2.1, then 4.0 | 4.0.1 | 31 Mar 2024; 31 Dec 2024 |
| Mercado Shops | A seller page inside the marketplace; lesson about platform risk | 2025 (verify) |
| INAI | Secretaría Anticorrupción y Buen Gobierno | Mar 2025 |
| COFECE | Comisión Nacional Antimonopolio | Oct 2025 |
| Privacy Sandbox APIs | Third-party cookies stay in Chrome; consent rules unchanged | Oct 2025 (verify) |
| In-app checkout in Meta Shops | Checkout on the merchant's own site | Sep 2025 (verify) |
| ChatGPT Instant Checkout | Discovery in the assistant, checkout at the merchant | Sep 2025 to Mar 2026 |
| FTC "click to cancel" rule | General FTC powers; Mexico's own reform in Dec 2025 | Vacated 8 Jul 2025 |

### 5.10 Term review protocol
1. Two weeks before the term, the owner checks every annex row against its primary source (DOF, Banxico, SAT, PROFECO, vendor documentation) and updates its "verified on" date.
2. Run `grep -rn "\[Anexo" ppts/commerce/` across the 34 YAML files, update only those slides, then rebuild and run `kit.lint`.
3. When an instance has died, replace it with its successor, or with the bare concept if there is none, and add a row to the graveyard.
4. Lab data is labeled "illustrative" and is updated only when it claims to be current.
5. Update both language editions in the same commit and add one changelog line to the course `HANDOFF.md`.

---

## 6. Keeping the Spanish and English editions equal
- **Same structure.** The same 17 decks per language, with the same slide order, layouts and counts. Add a preflight check that compares slide counts between `es/` and `en/`.
- **Same content.** Molienda, order #1001, MXN amounts and the Mexican cases stay in the English edition, glossed on first use in each deck:
  - SPEI: Mexico's real-time interbank transfer system;
  - MSI: interest-free installments;
  - CFDI: Mexico's electronic invoice;
  - PROFECO: Mexico's federal consumer protection agency.

  Law names stay in Spanish with an English gloss, for example "Ley Federal de Protección al Consumidor (Federal Consumer Protection Law, LFPC)".
- **Fixed glossary.** A bilingual glossary of about 80 terms, in the style of `office/.../GLOSARIO-DOC.es.md`, fixes each pair once. Examples:

  | Español | English |
  |---|---|
  | ticket promedio | average order value (AOV) |
  | margen de contribución | contribution margin |
  | contracargo | chargeback |
  | aclaración por cargo no reconocido | cardholder dispute |
  | logística inversa | reverse logistics |
  | última milla | last mile |
  | peso volumétrico | dimensional weight |
  | pago referenciado en efectivo | cash voucher payment |
  | aviso de privacidad | privacy notice |
  | derechos ARCO | ARCO rights |
  | CFDI de egreso | credit note (CFDI type E) |
  | embudo | funnel |
  | tienda propia | own store |

- **Language and typography.** Mexican Spanish with tú, and American English (catalog, fulfillment, behavior). Both editions follow the house style "20 %" and Mexican number formatting ("$2,068.00 MXN"). Labels follow the existing English decks: "Midterm 1", "Final exam", "Homework", "Session N of 17".
- **Same items and data.** Quizzes and exams use the same options in the same order with the same correct letter. Lab datasets are the same files with the column headers translated.
- **No em dashes on slides; durations only in speaker notes.**

---

## 7. Decisions still open for the professor
1. Course code, faculty kicker, credits and hours (needed for the intro deck's `stat` slide).
2. The project weight: 25/15 or the house 5 × 20 (both versions are specified in 4.1).
3. Whether teams may open free platform trials and use payment sandboxes, or work only with clickable prototypes.
4. The rules for projects with real businesses: owner consent and no real customer data.
5. Fall term (Buen Fin as the live case) or spring term (Hot Sale).
6. **NOM-247-SE in the brief:** confirm whether another instrument was meant, most likely NMX-COE-001-SCFI-2018 or LFPC art. 76 Bis.
7. Team size and the number of teams, which set the length of the S16 pitch block.

## 8. Sources checked on 5 October 2026 (for the dated and "(verify)" items)
- LFPC reform, DOF 12 Dec 2025: https://www.diputados.gob.mx/LeyesBiblio/ref/lfpc/LFPC_ref33_12dic25.pdf
- 2025 LFPDPPP and its regulator: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf and https://basham.com.mx/en/nueva-ley-federal-de-proteccion-de-datos-personales-en-posesion-de-los-particulares-publicada-en-el-diario-oficial-de-la-federacion/
- Banxico Circular 9/2026: https://www.informador.mx/economia/esta-es-la-fecha-limite-de-los-bancos-para-aplicar-cambios-de-banxico-sobre-reglas-en-transferencias-20260919-0079.html
- NMX-COE-001-SCFI-2018: https://www.dof.gob.mx/nota_detalle.php?codigo=5559015&fecha=30/04/2019
- NOM-247-SE-2021 (real estate): https://sidof.segob.gob.mx/notas/docFuente/5646251
- Distintivo Digital PROFECO: https://sidof.segob.gob.mx/notas/docFuente/5612350
- Buen Fin 2026 dates: https://www.elimparcial.com/mexico/2026/10/01/el-buen-fin-2026-sera-del-13-al-17-de-noviembre-y-cambiara-su-calendario-estas-son-las-fechas-requisitos-para-comercios-y-recomendaciones-para-consumidores/
- Comisión Nacional Antimonopolio: https://www.cuatrecasas.com/es/latam/competencia-derecho-ue/art/entra-en-funciones-la-comision-nacional-antimonopolio-de-mexico
- COFECE marketplace finding: https://forbes.com.mx/amazon-y-mercado-libre-senaladas-en-mexico-por-posibles-practicas-anticompetitivas/
- TikTok Shop México launch: https://roastbrief.com.mx/2026/02/tiktok-shop-celebra-su-primer-aniversario-en-mexico-con-un-crecimiento-acelerado-de-25-veces-en-vendedores-activos/
- Meta Shops checkout: https://ppc.land/meta-phases-out-facebook-and-instagram-shops-checkout-by-august-2025/
- OpenAI Instant Checkout and ACP: https://openai.com/index/buy-it-in-chatgpt/ and https://www.forbes.com/sites/jasongoldberg/2026/03/10/why-openais-checkout-retreat-spells-trouble-for-its-commerce-strategy/
- Google UCP: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/
- Privacy Sandbox retirement: https://www.emarketer.com/content/google-s-privacy-sandbox-elimination-ends-quest-cookieless-chrome
- SAT CFF art. 30-B and platform withholding: https://sovos.com/mx/blog/iva/sat-acceso-informacion-plataformas-digitales/
- Courier import rate: https://www.xataka.com.mx/comercio-electronico/malas-noticias-para-tus-compras-shein-temu-mexico-este-impuesto-33-5-se-cobrara-a-partir-agosto-2025
- Platform-worker labor reform: https://www.infobae.com/mexico/2025/06/28/nuevas-reglas-del-imss-para-repartidores-de-plataformas-digitales-entran-en-vigor/
- DiMo launch: https://expansion.mx/finanzas-personales/2023/04/28/dimo-de-banxico-ya-esta-disponible-como-funciona
- LFPC arts. 56 and 77: https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf
- EU AI Act art. 50 timing: https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon
- FTC v. Amazon settlement: https://www.dglaw.com/an-amazonian-sized-settlement-ftc-secures-2-5-billion-against-amazon-for-use-of-dark-patterns-in-prime-enrollment-scheme/
- "Click to cancel" vacated: https://www.cooley.com/news/insight/2025/2025-07-11-click-to-cancel-just-got-cancelled-eighth-circuit-vacates-entirety-of-ftcs-negative-option-rule
- Mercado Shops closure: https://www.orbis.agency/blog/mercado-shops-cierra-en-2025/
- Shopify Payments in Mexico (sources conflict): https://atempora.studio/blog/shopify-payments-mexico

Repo files read: `/tmp/claude-0/newcourses/ecommerce-original.es.txt`, `/home/user/learning-hub/ppts/README.md`, `/home/user/learning-hub/ppts/python/programacion-orientada-a-objetos/es/w01.0.es.yaml`, `/home/user/learning-hub/ppts/cpp/programacion-avanzada/es/w05.es.yaml`, `/home/user/learning-hub/ppts/kit/tokens.py` (the existing `commerce` palette).