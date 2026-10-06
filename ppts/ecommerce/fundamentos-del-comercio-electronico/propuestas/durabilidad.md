<!-- Propuesta de temario, lente: durabilidad. Borrador de un agente diseñador, sin verificar; ver HANDOFF-auditoria-y-cursos-nuevos.md en la raíz. -->

# Fundamentals of E-commerce: a durability-first proposal

**Course:** Fundamentos del comercio electrónico / Fundamental Principles of E-commerce (ES and EN editions)
**Prepared for:** David Escobar-Castillejos, Universidad Panamericana
**Date:** October 5, 2026 (the stack annex is dated the same day)
**Lens:** Durability first. Each topic is cut down to the concept that should still hold in 2036, and then one current instance that students can check is attached to it.

---

## 0. Design rules this proposal follows

1. **The 2036 test.** Every claim on a slide must either still be true in ten years or carry a date. A dated claim goes into the current-stack annex and the session deck links to it.
2. **Brands stay out of titles and objectives.** A product name can appear on an "instance" slide ("Hoy, en México", verified on a date), never in a session title or a learning objective.
3. **Each session has the same spine:** one transferable mental model, one current and verifiable instance of it, and a "funeral test" prompt: *if this tool disappeared next term, what would you keep and what would you migrate?*
4. **One evaluation instrument for the whole course.** The *Eight-question tool card* (Ficha de 8 preguntas) is introduced in session 1 and used every week. Session 16 applies it to a live trend.
   1. **Job:** Which of the five durable jobs does it do, and what did people use before it?
   2. **Money:** How does it make money, and what does it cost per order?
   3. **Data:** What data does it hold, and can you export it in a standard format?
   4. **Exit:** What would it cost to leave within 90 days (domain, URLs, reviews, customer list)?
   5. **Local fit:** Does it handle MXN, IVA, CFDI, SPEI and cash, Spanish, and the PROFECO information duties?
   6. **Integration:** Does it offer an API, webhooks, file export?
   7. **Evidence:** How old is it, who uses it, is it an open standard or proprietary, and does it have an incentive to change its rules?
   8. **Failure:** What breaks if it changes its terms or shuts down, and what is plan B?
5. **House rules still apply.** Mexican Spanish with tú, American English, no em dashes, no durations on slides. The exercise in week N uses only what weeks 1 to N taught. Code cards are small: a UTM link, a JSON product, a webhook, a JSON order, a DMARC record, a GA4 event.

---

## 1. Audit of the original syllabus

The original has 8 units of 3 items each, so 24 items. Codes such as O1.1 mean "original unit 1, item 1". Verdicts are keep, reframe, replace, merge or remove.

| # | Original item | Verdict | Reason (durability view) | Lands in |
|---|---|---|---|---|
| T | Course title "Fundamentos del comercio electrónico" | Keep | It names a field, not a technology. It will still be accurate in 2036. | All |
| O1.1 | Modelos y canales: B2C, B2B, C2C, D2C, marketplaces, omnicanalidad, social commerce, comercio conversacional | Reframe | B2C, B2B and C2C have lasted since the 1990s. "D2C", "social commerce" and "conversational commerce" are labels for whichever surface currently holds attention. The durable question underneath them is who owns the customer relationship, the data, the price and the delivery promise. The surfaces keep changing: Facebook Live Shopping closed in October 2022, Instagram live shopping closed in March 2023, and TikTok Shop began transacting in Mexico in February 2025. We teach the ownership questions and treat the surfaces as instances. | S02. Marketplace economics in S05, social surfaces in S14 |
| O1.2 | Propuesta de valor y cliente objetivo | Keep and extend | Jobs, segments and value propositions are durable. What the original lacks is the economic half: a value proposition that loses money on every order is not viable. Unit economics are added here. | S03 |
| O1.3 | Validación de mercado: entrevistas, encuestas, prototipos, landing pages, pruebas de venta, PMF | Keep and reframe | The durable idea is the evidence ladder: what people say < what they do < what they commit < what they pay. A landing page is one instance of a smoke test. "Product-Market Fit" is a heuristic (the Sean Ellis 40% question, retention), not a certificate. | S04 |
| O2.1 | Tipos de plataformas: SaaS, CMS, tiendas propias, marketplaces (Shopify, Tiendanube, WooCommerce, Wix, Amazon, Mercado Libre) | Reframe | **The category is misnamed.** It mixes four axes: SaaS is a delivery model, CMS is a software type, "tienda propia" is an ownership position and a marketplace is a business model. WooCommerce is an open-source plugin for WordPress, which is the CMS, not a CMS itself. The brand list will date. The durable axis is **rent vs buy vs build**, together with own channel vs marketplace, total cost of ownership and exit cost. Platform end of life is a real event: Magento 1 reached end of life in June 2020. The brands move to the annex. | S05 |
| O2.2 | Catálogo e inventario: SKU, categorías, variantes, precios, imágenes, disponibilidad, inventario | Keep and split | Product data is one of the most durable topics in the course. The UPC barcode was first scanned in 1974 and GS1 identifiers still underpin marketplaces. The inventory-state part moves next to the order lifecycle. | S06. Inventory states in S11 |
| O2.3 | Arquitecturas e integraciones modernas: APIs, Headless Commerce, Composable Commerce | Reframe and merge with O8.3 | "Modern" is a time-bound adjective. "Headless" and "composable" are marketing labels (the MACH Alliance was founded in 2020) for an older principle: separate the presentation layer from the commerce logic and integrate through contracts (APIs and events). We teach the principle, use the labels as current instances, and present decoupling as a cost-benefit choice rather than a virtue. | S11 |
| O3.1 | UX/UI: navegación, jerarquía visual, accesibilidad, responsive, mobile-first | Keep | Usability heuristics (Nielsen's ten, from the 1990s) and accessibility principles (perceivable, operable, understandable, robust) are durable. Versions go to the annex: WCAG 2.2 since October 2023, and the European Accessibility Act applying to e-commerce since June 28, 2025. Performance metrics are instances too: INP replaced FID as a Core Web Vital in March 2024, while the goal, responsiveness, stayed the same. | S07 |
| O3.2 | Página de producto y checkout | Keep and split | These are two different decisions: the product page reduces uncertainty, the checkout reduces friction. The legal information duties on the product page (total price, seller identity) are folded in here. | S07 (product page), S08 (checkout) |
| O3.3 | Optimización de conversión: CRO, A/B, CTA, prueba social, promociones, abandono | Keep and reframe | "CRO" is a job title. The durable discipline is experimentation, and the original skips the statistics: hypothesis, sample size, stopping rules. Tool deaths make the point: Google Optimize closed on September 30, 2023 and test design was unaffected. "Promociones" and "prueba social" need an ethics boundary, which is taught here and formalized in S16. | S08. Social proof in S14 |
| O4.1 | Medios de pago: tarjetas, transferencias, SPEI, wallets, pagos diferidos, BNPL, pasarelas y procesadores | Reframe | A list of instruments ages quickly. A model of roles and rails does not: payer, payee, issuer, acquirer, network, processor, gateway; push vs pull; synchronous vs asynchronous confirmation; cost, speed and reversibility. Instances: SPEI (Banxico), CoDi (2019, low adoption), DiMo (2023). "Meses sin intereses" is the long-standing Mexican form of installment credit, and BNPL is a newer form of the same idea. | S09 |
| O4.2 | Seguridad y protección de datos: cifrado, tokenización, autenticación, privacidad | Keep and update | The concepts are durable: the CIA triad, minimization, tokenization. **The law changed.** Mexico's LFPDPPP of 2010 was repealed by a new LFPDPPP published in the DOF on March 20, 2025 and in force since March 21, 2025. INAI was extinguished, and private-sector data protection now sits with the Secretaría Anticorrupción y Buen Gobierno (SABG). Card-security instances: PCI DSS v4.0 was retired on December 31, 2024 and v4.0.1 is current. Passkeys are the current instance of phishing-resistant authentication. | S10 |
| O4.3 | Fraude y gestión de riesgo: fraudes comunes, robo de identidad, contracargos, prevención | Keep and extend | Fraud is economics: losses traded against friction and false declines. The original lacks Mexico-specific patterns, such as fake SPEI receipts (verifiable through Banxico's CEP) and refund abuse. | S10 |
| O5.1 | Gestión de pedidos e inventarios: del pedido a la confirmación | Keep and reframe | An order is a state machine with exceptions (cancellation, partial shipment, refund). That model is durable and transfers to any OMS. | S11 |
| O5.2 | Fulfillment y distribución: almacenamiento, preparación, transportistas, operadores, última milla | Keep | The trade-off between speed, cost and reliability is durable. Carriers and marketplace fulfillment programs go to the annex. | S12 |
| O5.3 | Modelos logísticos y posventa: dropshipping, logística tercerizada, devoluciones, reembolsos, logística inversa | Keep and update | Dropshipping is a sourcing model whose cross-border form is exposed to policy. Mexico applied a 19% global rate to courier imports from countries without trade agreements on January 1, 2025 and raised it to 33.5% on August 15, 2025 (verify the current rate and exceptions). The US suspended its de minimis exemption for all countries on August 29, 2025. Returns are a legal duty and part of the promise. | S12 |
| O6.1 | Adquisición de tráfico: SEO, publicidad en buscadores, anuncios en redes, marketing de contenidos | Reframe | "SEO" assumes a page of ten blue links. Discovery now also runs through marketplace search (Mercado Libre and Amazon as product search engines) and AI answer engines (Google AI Overviews since May 2024 in the US, AI Mode since 2025, verify Mexican availability). The durable concept is discoverability through intermediaries that rank by relevance and sell placement through auctions. Retail media is missing from the original. | S13 |
| O6.2 | Social commerce y contenido: redes, influencers, reseñas, comunidades, UGC | Keep and reframe | Social proof is durable. "Influencer" becomes **paid endorsement with a disclosure duty**, and reviews become **authenticity and moderation**. The US FTC rule against fake reviews took effect on October 21, 2024. | S14 |
| O6.3 | Retención y fidelización: CRM, email, remarketing, automatización, lealtad | Keep and reframe | Retention economics (repeat rate, cohorts, LTV) are durable. **"Remarketing" depends on identifiers that platforms keep changing:** Apple ATT arrived with iOS 14.5 in April 2021. Chrome reversed its third-party-cookie phase-out in 2024 and Google retired most Privacy Sandbox APIs in October 2025. The durable answer is a consented first-party relationship. Email deliverability has had a hard floor since February 2024, when Gmail and Yahoo began requiring SPF, DKIM, DMARC and one-click unsubscribe from bulk senders. | S14 |
| O7.1 | Indicadores: conversión, ticket promedio, CAC, LTV, ROAS, margen | Keep and move earlier | These formulas are durable, and every other unit needs them. They are introduced in S03 and S04 and consolidated into a metric tree in S15. | S03, S04, S13, S15 |
| O7.2 | Embudo de conversión | Keep | The funnel is durable. It is taught as a measurement in S04, a diagnosis in S08 and a system in S15. | S04, S08, S15 |
| O7.3 | Analítica digital: GA4 y dashboards | Reframe | **"GA4" is a product version.** Universal Analytics stopped processing data on July 1, 2023 (July 1, 2024 for UA 360). Data Studio was renamed Looker Studio in October 2022. The durable concepts are event-based measurement, consent, data quality, and attribution vs incrementality. GA4 is today's instance. | S15 |
| O8.1 | Protección al consumidor y privacidad: información, precios, datos, consentimiento, garantías, devoluciones | Keep and distribute | Each rule is taught where the harm happens: total-price display (LFPC art. 7 Bis) on the product page, privacy in S10, returns and warranties in S12, recurring charges in S14. S16 consolidates them. Update: an LFPC reform published December 12, 2025 added sections on recurring charges and subscription cancellation to art. 76 Bis (verify the exact sections). | S07, S10, S12, S14, S16 |
| O8.2 | Propiedad intelectual y ética digital: derechos de autor, marcas, dark patterns, transparencia, IA | Keep and rename | The current term is "deceptive design", which is broader than "dark patterns" and is the vocabulary regulators use (EU DSA art. 25). IP law has instances too: Mexico's LFPPI replaced the Ley de la Propiedad Industrial in November 2020, and the July 2020 LFDA reform introduced notice and takedown. AI is taught as an instance of automated content and decisions, not as a separate topic. | S16 |
| O8.3 | Ecosistema tecnológico: CRM, ERP, OMS, WMS, APIs, webhooks | Merge with O2.3 | The categories are durable because each one is a system of record for one entity. They belong next to the order they carry, not at the end of the course. | S11 |

**Totals:** keep 13 (including the split, extended and moved items), reframe 9, merge 2 (O2.3 and O8.3 form one session). Nothing is removed outright. The only line items that would date within a few years are the brand lists and "GA4", and they move to the annex.

### Flags on the Mexican context list in the brief

These are not in the original syllabus, but the durability lens applies to them too.

| Item | Verdict | Finding |
|---|---|---|
| **NOM-247-SE** | **Replace (misapplied)** | NOM-247-SE-2021 (published in the DOF on March 22, 2022, in force since September 18, 2022) regulates commercial information, advertising and contracts for **residential real estate**, not e-commerce. It only applies if a student project sells housing. The e-commerce instruments are the LFPC (art. 7 Bis total price, art. 32 advertising, art. 76 Bis electronic transactions), NOM-050-SCFI-2004 for general product information, and NMX-COE-001-SCFI-2018, a voluntary e-commerce standard (verify its current status). |
| Mexican personal data law and its regulator | Update | Under the new LFPDPPP (DOF March 20, 2025), the regulator is the SABG and INAI no longer exists. Whether the implementing regulation has been issued needs checking (verify). |
| CoDi / DiMo | Keep as instances | Both are still operating, and adoption is low. Reports cite about 4.4 million CoDi operations in 2025 (verify). Banxico has set new rules to simplify app transfers and QR payments, with a December 14, 2026 deadline (verify). They are taught as instances of **request-to-pay** and **alias-based push transfer**. Brazil's Pix (November 2020) is the international comparison that worked at scale. |
| OXXO Pay | Keep as an instance | This is a brand. The concept is a **cash voucher network**: asynchronous, push, reference-based. It stays durable in Mexico for as long as cash use stays high. |
| SAT CFDI | Keep and update | CFDI 4.0 has been mandatory since April 1, 2023. For 2026, the platform withholding regime holds back 2.5% ISR on sales of goods (up from 1%) and 8% IVA from sellers who provide an RFC (verify against the 2026 RMF). CFF art. 30-B gives the SAT online access to platform systems from April 2026 (verify). |
| GA4 | Reframe | See O7.3. |

---

## 2. Additions the original lacks

| # | Addition | Why it earns a place | Session |
|---|---|---|---|
| A1 | **Economics of one order** (contribution-margin waterfall, take rates, break-even CAC) | Business students need to know whether a sale makes money. Without this, CAC, ROAS and "free shipping" are formulas with nothing behind them. | S03, reused in S05, S09, S12, S13 |
| A2 | **Experiment literacy** (the evidence ladder, sample size, pre-declared thresholds, peeking) | Validation and CRO both depend on it, and it does not age. | S04, S08 |
| A3 | **Platform risk, lock-in and data portability** | Every channel is rented. Fee changes (Etsy, 2022), algorithm changes and account suspensions are recurring events, so an exit plan is a core skill. | S05 |
| A4 | **Product identity standards and structured data** (GS1 GTIN, schema.org, product feeds) | Marketplaces, search and AI agents read data, not pages. This is the most transferable technical skill in the course and needs no programming. | S06 |
| A5 | **Taxes and invoicing** (CFDI 4.0, platform withholding) | In Mexico, the factura is part of the order, and B2B buyers will not buy without one. The original ignores the SAT. | S11 (cost line in S03) |
| A6 | **Cross-border commerce** (landed cost, courier rates, de minimis) | Mexico changed its courier-import regime twice in 2025, and the US ended de minimis. Landed cost is the durable concept that makes such changes understandable. | S12 |
| A7 | **Discovery through marketplaces, answer engines and retail media** | A large share of product search starts inside marketplaces or AI answers. "SEO" alone teaches a shrinking slice. | S13 |
| A8 | **Consent and deliverability as infrastructure** (SPF, DKIM, DMARC, REPEP, opt-in on WhatsApp) | Retention fails without them, and they are standards that change slowly. | S14 |
| A9 | **Attribution vs incrementality, metric trees, data reconciliation** | Dashboards on their own teach reading. Decisions need causal thinking and a check that analytics revenue matches orders. | S15 |
| A10 | **Agentic commerce and machine customers** (AI agents that search and pay) | This is the live trend: OpenAI's Agentic Commerce Protocol (September 2025), Google's AP2 (2025) and Universal Commerce Protocol (January 2026, verify). It is the course's practice case for evaluating a trend, not something to treat as settled fact. | S16 |
| A11 | **The Eight-question tool card** | This is how "teach students to evaluate the next tool" becomes a gradeable skill rather than a slogan. | S01 to S16 |
| A12 | **Subscriptions and recurring-charge law** | The LFPC reform of December 2025 (verify) applies to the running case's coffee subscription. | S14, S16 |
| A13 | **Platform power and competition** | The Mexican competition authority (then COFECE) found in September 2025 that featured-offer ("Buy Box") algorithms on Amazon and Mercado Libre were a barrier to competition. Those two platforms hold over 85% of the market, and no corrective measures were ordered (verify details). It is a local, durable lesson about dependence. | S05 |
| A14 | **Customer service as an operation** (channels, SLAs, PROFECO Concilianet) | Resolving problems is the fifth durable job of a distance sale, and the original only treats it as "posventa logistics". | S12 |

---

## 3. The 17-session plan

**Running class case (fictional):** *Café Siete Lunas*, a small specialty roaster in Coatepec, Veracruz. It sells three roasts in three grinds, in 250 g and 1 kg bags. Today it sells through Instagram and WhatsApp, with SPEI transfers. It wants its own store, a Mercado Libre presence, and an office-subscription channel for B2B buyers who need a CFDI. The case advances every session.

**Roadmap for the intro deck**

| Phase | Weeks | Theme | Covers |
|---|---|---|---|
| 01 | 1 to 4 | Modelo y evidencia | Who sells, why it makes money, how we know |
| 02 | 5 to 8 | Tienda y conversión | Platform, catalog, page, checkout. Parcial 1 |
| 03 | 9 to 12 | Pago y operación | Money, trust, orders, delivery |
| 04 | 13 to 17 | Crecimiento, reglas y cierre | Reach, retention, measurement, law. Parcial 2, project, final |

---

### S01 · Semana 1 · Sesión 1 de 17
**ES:** Vender a distancia: lo que no cambia
**EN:** Selling at a distance: what does not change

- **Original items:** course framing; opens O1.1. Adds A11.
- **Mental model:** Every distance sale has to do five jobs: **be found, be believed, get paid, deliver, and resolve**. Tools are instances of these jobs. Each tool is temporary, but the job it does stays.
- **Current instance:** one Mercado Libre purchase paid in cash at OXXO, traced through the five jobs.
- **Topics**
  1. Course framing: grading, project, honor code and AI-use rules (intro deck, as in COM102 w01.0)
  2. The five jobs of a distance sale, and who does each one: store, platform, bank, carrier
  3. Concept vs instance, with recent tool deaths: Universal Analytics (2023), Google Optimize (2023), Instagram live shopping (2023)
  4. The Eight-question tool card
  5. How to read an industry source: the AMVO annual online-sales study and INEGI's ENDUTIH. We read their method, not just their headline numbers.
- **Objectives**
  1. Map any online purchase onto the five jobs and name who performs each one.
  2. Classify eight items as concept or instance, and give the concept behind each instance.
  3. Apply questions 1 to 3 of the tool card to a service they have used.
  4. State the five grading components and the weeks they fall in.
- **Cases:** Mercado Libre with OXXO cash payment (MX). Amazon's 1-Click patent, filed in the 1990s and expired in 2017: a feature anyone could copy once the patent ran out, aimed at the same durable goal of less friction (international).
- **Lab:** In pairs, each student traces their last online purchase through the five jobs, and the pair compares who did each job.
- **Homework:** For three tools or services they have bought through, write the concept each one is an instance of and one predecessor it replaced. Add a paragraph on expectations for the course.
- **Quiz idea:** "Google Optimize closed in September 2023. Which skill lost its value?" (a) designing an A/B test; (b) knowing where Optimize's buttons were; (c) choosing a primary metric; (d) computing a sample size. Answer: b.

### S02 · Semana 2 · Sesión 2 de 17
**ES:** ¿Quién es dueño del cliente? Modelos y canales
**EN:** Who owns the customer? Models and channels

- **Original items:** O1.1.
- **Mental model:** Four ownership questions classify any model: **who sets the price, who holds the customer data, who controls the transaction surface, and who carries inventory risk.** Channels sit on a spectrum from control to reach.
- **Current instance:** TikTok Shop in Mexico (transacting since February 2025) as the newest surface for an old pattern: selling where attention is.
- **Topics**
  1. B2C, B2B, C2C, B2B2C and D2C, redefined through the four questions
  2. Marketplaces as two-sided platforms: network effects, with take rates introduced here
  3. Omnichannel: one customer, one inventory, many touchpoints (click and collect, returns in store)
  4. Social and conversational commerce as surfaces: WhatsApp catalogs, live shopping, in-app shops
  5. What makes B2B different: quotes, credit terms, recurring orders, a mandatory CFDI
  6. Channel conflict and price parity
- **Objectives**
  1. Classify eight Mexican businesses using the four ownership questions.
  2. Explain how one brand can be D2C and a marketplace seller at the same time, and what it gives up in each.
  3. Identify one channel conflict in a given scenario and propose a rule to resolve it.
  4. Draw a channel map for the case with the four questions answered.
- **Cases:** Liverpool omnichannel and click and collect; Mercado Libre's evolution from C2C auctions to B2C marketplace; small businesses selling through WhatsApp (MX). Facebook Live Shopping closing in October 2022 as an example of surface volatility (international).
- **Lab:** A channel map for Café Siete Lunas covering five candidate channels.
- **Homework:** A channel teardown of a Mexican brand present in at least three channels, comparing price, data captured and delivery promise in each.
- **Quiz idea:** "A seller lists on a marketplace and uses the marketplace's own fulfillment. Who controls the delivery promise?" Answer: the marketplace.

### S03 · Semana 3 · Sesión 3 de 17
**ES:** Propuesta de valor y la economía de un pedido
**EN:** Value proposition and the economics of one order

- **Original items:** O1.2, the margin part of O7.1. Adds A1.
- **Mental model:** A value proposition is the fit between a customer's job, pains and gains and what you offer. **It is only viable if one order leaves a positive contribution margin after all variable costs.**
- **Current instance:** a marketplace's free-shipping threshold (the amount is dated in the annex) and the effect it has on order value.
- **Topics**
  1. Jobs to be done, pains and gains; segments beyond demographics
  2. Value proposition statement and canvas
  3. Price as part of the proposition: anchors, bundles, MSI framing; Buen Fin and Hot Sale discount arithmetic
  4. The order waterfall: displayed price (IVA included, LFPC art. 7 Bis), net of IVA, product cost, payment fee, commission, shipping, packaging, expected returns, contribution
  5. AOV, gross margin, contribution margin, CAC, LTV, and break-even CAC
- **Objectives**
  1. Write a value proposition that can be tested, naming the segment, job and differentiator.
  2. Compute the contribution margin of one order from the parameters given.
  3. Compute the maximum affordable CAC for a target margin.
  4. Explain with numbers how a free-shipping threshold changes AOV and margin.
- **Cases:** a Buen Fin discount that destroys margin (MX). Dollar Shave Club, acquired by Unilever in 2016 for about USD 1 billion, as a value proposition built on subscription convenience (international).
- **Lab:** A waterfall spreadsheet for a 250 g bag sold through the case's own store vs a marketplace. The instructor supplies the fees.
- **Homework (project M1 part):** The value proposition and order waterfall for the team's project business.
- **Quiz idea:** Price 300 MXN including IVA, product cost 90, payment fee 3.5% plus 3 MXN, shipping 85. What is the contribution? (The net price is 300 / 1.16 ≈ 258.62.)

### S04 · Semana 4 · Sesión 4 de 17
**ES:** Evidencia antes de construir
**EN:** Evidence before building

- **Original items:** O1.3, the funnel part of O7.2. Adds A2.
- **Mental model:** The **evidence ladder**: opinions < behavior < commitment < payment. Test the riskiest assumption first, and decide the success threshold before running the test.
- **Current instance:** a pre-sale landing page whose traffic is tagged with UTM parameters. UTM comes from Urchin, which Google bought in 2005, and the convention has outlived Urchin and Universal Analytics.
- **Topics**
  1. Interviews about past behavior, not future intent (*The Mom Test*, Fitzpatrick, 2013)
  2. Surveys and their biases
  3. Smoke tests: landing page, fake door, pre-sale, concierge MVP, and the ethics of each (disclosure, refunds)
  4. Measuring a test: visitors, conversion rate, cost per sign-up
  5. Telling sources apart with UTM tags
  6. PMF signals: the 40% question, repeat purchase, cohort retention
- **Code card:** `https://sietelunas.mx/preventa?utm_source=instagram&utm_medium=social&utm_campaign=preventa_2026_10`
- **Objectives**
  1. Rewrite five leading interview questions as questions about past behavior.
  2. Design a smoke test with a success threshold declared in advance.
  3. Build correct UTM links and compute conversion rate by source.
  4. Place six pieces of evidence on the ladder.
- **Cases:** Mexican Instagram brands that run pre-sales before producing (MX). Zappos (1999), whose founder photographed shoes in stores before holding any inventory (international).
- **Lab:** Teams write interview questions and swap them so another team flags the leading ones. Then they design the case's pre-sale test.
- **Homework (project M1 due):** Five interviews, one smoke test with UTM links, and an evidence-ladder summary.
- **Quiz idea:** "Which is the strongest evidence?" (a) 80% say they would buy; (b) 40 email sign-ups; (c) 12 paid pre-orders; (d) 500 likes. Answer: c.

### S05 · Semana 5 · Sesión 5 de 17
**ES:** Rentar, comprar o construir la tienda
**EN:** Rent, buy or build the store

- **Original items:** O2.1, marketplace economics from O1.1. Adds A3 and A13.
- **Mental model:** **Control vs effort vs reach.** Every option is priced in money, time and exit cost. Platform risk is the chance that the rules change while you are inside.
- **Current instance:** the case compares a Mexican hosted store platform, an open-source store and a marketplace, using pricing pages dated on the day they are read.
- **Topics**
  1. Four ways to have a store: marketplace listing (rented reach), hosted SaaS (rented software), self-hosted open source (owned software and its maintenance), custom or enterprise build
  2. Twelve-month total cost of ownership: plan, transaction fees, apps, payment fees, people's time
  3. Marketplace economics: take rate, featured offer, algorithm dependence
  4. Lock-in and portability: domain, URLs, customer list, reviews, exports
  5. End of life and rule changes: Magento 1 (June 2020), Etsy's fee increase (2022)
  6. Choosing with the tool card
- **Objectives**
  1. Compute twelve-month TCO for two platform options.
  2. List three exit costs for a given platform and a way to reduce each.
  3. Explain the competition authority's featured-offer finding and what it means for a small seller.
  4. Recommend a platform mix, justified question by question on the tool card.
- **Cases:** The September 2025 competition finding on Amazon and Mercado Libre; Tiendanube's local payment integrations (MX). Magento 1's end of life forcing replatforming; Etsy's 2022 fee increase and seller strike (international).
- **Lab:** The tool card applied to two options for the case. Every number cites its source and the date it was read.
- **Homework (project M2 part):** A platform memo with a TCO table and a 90-day exit plan.
- **Quiz idea:** "Which cost does a marketplace seller pay that a hosted-store owner does not?" Answer: the commission on each sale, or take rate.

### S06 · Semana 6 · Sesión 6 de 17
**ES:** El catálogo es un conjunto de datos
**EN:** The catalog is a dataset

- **Original items:** O2.2 (product data part). Adds A4.
- **Mental model:** **One product truth, many channels.** Identity, attributes, variants, media, price and availability are data. A product with poor data is never found, however good the product is.
- **Current instance:** schema.org `Product` markup and a merchant product feed.
- **Topics**
  1. Identifiers: SKU (internal) vs GTIN/EAN (GS1, global) vs listing ID (per channel)
  2. Product-level vs variant-level attributes; category taxonomy and mapping to each channel
  3. Content: titles, descriptions, images, alt text
  4. Price and availability as data: stock, lead time, pre-order
  5. Structured data and feeds; the idea of a PIM
- **Code card:** a JSON-LD `Product` with `name`, `sku`, `gtin13`, `offers.price`, `priceCurrency: "MXN"`, `availability`.
- **Objectives**
  1. Design a SKU scheme for a product family with variants.
  2. Separate product-level from variant-level attributes for ten SKUs.
  3. Write valid JSON-LD for one product and check it with a validator.
  4. Map one product to two channel taxonomies.
- **Cases:** GS1 México barcodes; marketplace listing attribute requirements (MX). The first UPC scan in 1974, a data standard that has lasted more than fifty years (international).
- **Lab:** A catalog sheet for the case: three roasts × three grinds × two sizes.
- **Homework (project M2 part):** A ten-SKU catalog for the project, plus JSON-LD for the hero product.
- **Quiz idea:** "Which identifier should match between your store and a marketplace for the same item?" Answer: the GTIN.

### S07 · Semana 7 · Sesión 7 de 17
**ES:** Diseñar para decidir: experiencia y página de producto
**EN:** Designing for the decision: experience and the product page

- **Original items:** O3.1, the product-page half of O3.2, the information duties from O8.1.
- **Mental model:** A product page answers the questions a good shop clerk would answer: what it is, whether it fits, the total price, when it arrives, what happens if it is wrong, and who vouches for it. Accessibility follows POUR (perceivable, operable, understandable, robust). Speed and stability are part of trust.
- **Current instance:** WCAG 2.2 and Core Web Vitals (LCP, INP, CLS), measured with a free audit tool.
- **Topics**
  1. Mobile-first navigation, on-site search, information scent
  2. Visual hierarchy and usability heuristics
  3. Anatomy of a product page, including legal information: total price (art. 7 Bis), seller identity and terms (art. 76 Bis), warranty, returns
  4. Accessibility: POUR; the European Accessibility Act as an international signal
  5. Performance as trust: why FID was replaced by INP in 2024 while the goal stayed the same
- **Objectives**
  1. Run a heuristic evaluation and log five issues with severity ratings.
  2. Check a page against a ten-item checklist that includes the legal items.
  3. Find three accessibility failures (contrast, alt text, keyboard access) and propose fixes.
  4. Explain the difference between a metric and the goal it stands for.
- **Cases:** product pages from a department store, a marketplace and a small hosted store, compared; PROFECO's price-display rules (MX). The European Accessibility Act (international).
- **Lab:** A heuristic and accessibility audit of a real Mexican product page.
- **Homework (project M2 part):** A wireframe of the hero product page, with the legal-information checklist.
- **Quiz idea:** "Which page meets the total-price duty?" Four price displays, one of them showing "+ IVA". Answer: a display that includes IVA.

### S08 · Semana 8 · Sesión 8 de 17 · closes with Parcial 1
**ES:** Checkout y experimentación
**EN:** Checkout and experimentation

- **Original items:** the checkout half of O3.2, O3.3, the funnel diagnosis from O7.2. Adds A2.
- **Mental model:** Conversion is **motivation minus friction minus anxiety.** Opinions propose changes and experiments decide them. A false positive has a cost.
- **Current instance:** a free sample-size calculator. The test tool itself is an annex item.
- **Topics**
  1. Checkout anatomy: cart, guest checkout, address, shipping choice, payment choice, review
  2. Sources of friction: forced account creation, surprise costs, too many fields, a missing payment method
  3. Step-by-step drop-off analysis
  4. A/B testing: hypothesis, primary metric, sample size, significance, peeking, stopping rule
  5. Social proof, urgency and promotions, and the line where they become deception (preview of S16)
  6. Prioritizing tests with a scoring heuristic
- **Objectives**
  1. Compute step conversion rates and identify the weakest step.
  2. Write an A/B hypothesis with a primary metric and a stopping rule.
  3. Judge whether a result is conclusive for a given sample size.
  4. Classify four urgency claims as truthful or deceptive.
- **Cases:** surprise shipping charges at checkout; countdown claims during Buen Fin (MX). Large-scale experimentation programs at travel and retail companies, kept as anonymized patterns (international).
- **Lab:** Using the case's funnel data, locate the leak, then design two tests with sample sizes.
- **Homework (project M2 due before S09):** A storefront prototype with catalog, product page and checkout flow, built on a free trial or a prototyping tool.
- **Quiz idea:** "B beats A by 12% after three days with 40 conversions each. Do you ship B?" Answer: not yet. The sample is too small and no stopping rule was set.
- **Closing:** Parcial 1 logistics (S01 to S08).

### S09 · Semana 9 · Sesión 9 de 17
**ES:** Cómo se mueve el dinero
**EN:** How money moves

- **Original items:** O4.1.
- **Mental model:** Payments follow roles and rails. The roles are payer, payee, issuer, acquirer, network, processor, gateway and aggregator. Payments are push or pull, and confirmation is synchronous or asynchronous. Every method trades **cost, speed and reversibility** against each other.
- **Current instance:** a webhook confirming a cash-voucher payment.
- **Topics**
  1. Card lifecycle: authorization, capture, clearing, settlement, merchant discount rate
  2. Account-to-account push payments: SPEI, CEP proof, CoDi (request-to-pay by QR), DiMo (phone-number alias)
  3. Cash networks: OXXO vouchers (asynchronous, reference-based)
  4. Wallets and tokenized cards
  5. Installment credit: MSI (who funds it), BNPL
  6. Gateways vs processors vs aggregators; why asynchronous methods need a webhook before you ship
- **Code card**
  ```json
  {"type": "payment.succeeded",
   "data": {"order_id": "SL-1042", "method": "cash_voucher",
            "amount": 389.00, "currency": "MXN",
            "paid_at": "2026-10-05T18:22:10-06:00"}}
  ```
- **Objectives**
  1. Draw the roles involved in a card payment and in a SPEI payment.
  2. Choose a payment mix for a customer segment, justified by cost, speed and reversibility.
  3. Explain why a cash-voucher order must wait for a webhook before it ships.
  4. Compute payment cost per order for three methods, reusing the S03 waterfall.
- **Cases:** SPEI running 24/7; CoDi (2019) and DiMo (2023) adoption; MSI during Buen Fin; cash use measured by INEGI's ENIF (MX). Brazil's Pix (2020) and India's UPI (2016), which applied the same concepts and succeeded at scale (international).
- **Lab:** A payment mix for two case segments: a young buyer without a credit card, and an office buyer who needs a factura.
- **Homework (project M3 part):** A payment plan with cost per order for each method and the confirmation flow.
- **Quiz idea:** "Which of these is a pull payment?" (card, SPEI, OXXO voucher, DiMo). Answer: card.

### S10 · Semana 10 · Sesión 10 de 17
**ES:** Confianza: seguridad, privacidad y fraude
**EN:** Trust: security, privacy and fraud

- **Original items:** O4.2, O4.3, the privacy part of O8.1.
- **Mental model:** The **CIA triad** (confidentiality, integrity, availability) plus **data minimization**; risk is likelihood times impact. Fraud controls trade losses against friction, and a false decline is also a loss.
- **Current instance:** the 2025 LFPDPPP with the SABG as regulator; PCI DSS v4.0.1; passkeys.
- **Topics**
  1. Encryption in transit and at rest; tokenization and why it reduces PCI scope
  2. Authentication: passwords, MFA, passkeys; 3-D Secure 2 as risk-based authentication
  3. Privacy: the privacy notice (aviso de privacidad), consent, ARCO rights, the SABG; GDPR as the international reference
  4. Fraud types: card-not-present, account takeover, friendly fraud, triangulation, fake SPEI receipts, refund abuse, brand-impersonation phishing
  5. The chargeback lifecycle and what evidence wins it
  6. Rules and scoring: approve, review or reject
- **Objectives**
  1. Classify six data fields by sensitivity and decide whether to collect each one.
  2. List the core elements of a privacy notice under the 2025 law (verify the list against the law's text).
  3. Design three fraud rules and estimate the cost of their false positives.
  4. Describe the chargeback flow and the evidence a merchant should keep.
- **Cases:** fake SPEI receipts detected through CEP; the move from INAI to the SABG in 2025 (MX). Target's 2013 breach through a vendor's credentials; British Airways' GDPR fine in 2020 (international).
- **Lab:** A fraud review of ten orders with signals. Compare the losses prevented with the sales lost.
- **Homework (project M3 part):** A data inventory and a simplified privacy notice for the project.
- **Quiz idea:** "Tokenization means…" (a) encrypting the database; (b) replacing the card number with a value that is useless outside your system; (c) hiding digits on screen; (d) using HTTPS. Answer: b.

### S11 · Semana 11 · Sesión 11 de 17
**ES:** El pedido y los sistemas que lo mueven
**EN:** The order and the systems that move it

- **Original items:** O5.1, O2.3, O8.3, the inventory part of O2.2. Adds A5.
- **Mental model:** An **order is a state machine**. Each entity has one system of record. Systems either request data (APIs) or are told about changes (webhooks). Decoupling (headless) is a trade-off, not a virtue.
- **Current instance:** a JSON order payload and a CFDI 4.0 data checklist.
- **Topics**
  1. Order states and exceptions: created, paid, allocated, picked, shipped, delivered, closed; cancelled, refunded, partial
  2. Inventory states (on hand, reserved, available) and how a multichannel store oversells
  3. The system map: storefront, OMS, WMS, ERP, CRM, PSP, carrier, and which one is the source of truth for what
  4. Integration patterns: API request, webhook event, batch file, middleware; headless and composable, with MACH as the current label
  5. Invoicing: CFDI 4.0 (mandatory since April 2023), the RFC, tax regime and postal code a B2B buyer must provide, the global invoice for public-counter sales, and platform withholding as an order-level deduction
- **Code card:** an order JSON with `order_id`, `status`, `items[{sku, qty, unit_price}]`, `tax`, `payment.method`, `customer.rfc` (optional), `channel`.
- **Objectives**
  1. Draw an order state diagram that includes two exception paths.
  2. Assign the system of record for six entities.
  3. Explain an overselling scenario and fix it with reservations and events.
  4. Identify the fields a B2B checkout needs in order to issue a CFDI.
- **Cases:** a small seller connecting a marketplace to a Mexican accounting or ERP package; the factura request at checkout (MX). Target Canada (2013 to 2015), where bad item data in the systems helped sink the launch (international).
- **Lab:** Trace one case order through all of its systems, then diagram a webhook-driven inventory sync between the store and the marketplace (a diagram, no code).
- **Homework (project M3 part):** The project's order state diagram and system map.
- **Quiz idea:** Given a JSON order, "which field does the ERP need before it can issue the CFDI to a company?" Answer: the customer's RFC, together with tax regime and postal code.

### S12 · Semana 12 · Sesión 12 de 17
**ES:** Entregar y resolver: logística y posventa
**EN:** Deliver and resolve: logistics and aftersales

- **Original items:** O5.2, O5.3, the returns and warranty part of O8.1. Adds A6 and A14.
- **Mental model:** The delivery promise trades speed, cost and reliability, and you can optimize two of them. Where the inventory sits decides the promise. Reverse logistics is part of the promise. Landed cost decides whether a cross-border sale is viable.
- **Current instance:** marketplace fulfillment programs and the 2025 Mexican courier-import rate.
- **Topics**
  1. In-house vs third-party logistics vs marketplace fulfillment
  2. Pick, pack and ship; packaging; dimensional weight
  3. Last mile: carriers, aggregators, pickup points and lockers, failed deliveries
  4. Dropshipping and its risks
  5. Returns: the cooling-off period (LFPC art. 56, verify how it applies to online sales), warranties, policy design, refunds, reverse-logistics cost
  6. Cross-border: landed cost, courier rates (19% then 33.5% in 2025, verify), the end of US de minimis; customer-service channels, SLAs and PROFECO Concilianet
- **Objectives**
  1. Compute billable weight and choose the cheaper package.
  2. Choose a fulfillment model for a scenario and justify it.
  3. Compute the landed cost of an imported item under the current rate.
  4. Write a returns policy that meets the LFPC basics.
- **Cases:** marketplace full-fulfillment programs, same-day carriers, OXXO pickup; cross-border apparel platforms after August 2025; the Carta Porte complement for goods in transit (MX). Zappos' long return window as a value proposition (international).
- **Lab:** Fulfillment options for the case with costs, plus a returns-policy draft.
- **Homework (project M3 due before S13):** The payments and operations blueprint.
- **Quiz idea:** "A 30 × 30 × 20 cm box weighs 2 kg. With a divisor of 5,000, what is the billable weight?" Answer: 3.6 kg.

### S13 · Semana 13 · Sesión 13 de 17 · closes with Parcial 2
**ES:** Ser encontrado: búsqueda, medios y alcance
**EN:** Being found: search, media and reach

- **Original items:** O6.1, the CAC and ROAS part of O7.1. Adds A7.
- **Mental model:** Attention is either rented (paid), earned, or owned. Intermediaries rank by relevance signals and sell placement in auctions where both bid and quality count. Every channel has diminishing returns.
- **Current instance:** AI answer summaries in search results and retail media on marketplaces.
- **Topics**
  1. How ranking intermediaries work: relevance, quality, authority, behavior
  2. Search fundamentals: crawl, index, rank, intent; structured data from S06
  3. Answer engines and AI summaries: being the cited source; product-data quality as an acquisition lever
  4. Marketplace search and retail media
  5. Paid search and paid social auctions; content and creators
  6. CAC and ROAS by channel, break-even ROAS, marginal returns; UTM discipline (from S04)
- **Objectives**
  1. Explain ad-auction ranking using bid and quality.
  2. Compute break-even ROAS from the S03 contribution margin.
  3. Allocate a budget across three channels and justify the split.
  4. Audit the search basics of a product page.
- **Cases:** Hot Sale and Buen Fin media spikes; marketplace ads (MX). The debate over AI summaries and click-through traffic (international).
- **Lab:** Break-even ROAS and a channel budget for the case.
- **Homework:** A short draft of the project's acquisition plan (M4 part), kept light because of the exam.
- **Quiz idea:** "Contribution before ads is 40% of revenue. What is the break-even ROAS?" Answer: 2.5.
- **Closing:** Parcial 2 logistics (S09 to S13).

### S14 · Semana 14 · Sesión 14 de 17
**ES:** Confianza social y relación con el cliente
**EN:** Social proof and the customer relationship

- **Original items:** O6.2, O6.3. Adds A8 and A12.
- **Mental model:** People trust people. Retention economics come down to repeat rate, cohorts and LTV. A relationship built on consent outlasts any tracking identifier.
- **Current instance:** email authentication records and WhatsApp opt-in.
- **Topics**
  1. Reviews and UGC: authenticity, moderation, fake-review rules
  2. Creators: paid endorsements and disclosure
  3. CRM and segmentation (RFM, meaning recency, frequency, monetary value)
  4. Lifecycle messages: welcome, abandoned cart, post-purchase, win-back; consent and opt-out; REPEP
  5. Deliverability: SPF, DKIM, DMARC (Gmail and Yahoo requirements since February 2024)
  6. Subscriptions and loyalty: the cancellation duties from the LFPC reform of December 2025 (verify); remarketing under signal loss (ATT in 2021; Privacy Sandbox APIs retired in October 2025)
- **Code card:** `_dmarc.sietelunas.mx  TXT  "v=DMARC1; p=quarantine; rua=mailto:dmarc@sietelunas.mx"`
- **Objectives**
  1. Compute repeat rate and a simple LTV from a cohort table.
  2. Segment customers by RFM and choose an action for each segment.
  3. Design three lifecycle messages, each with a trigger, a consent basis and a metric.
  4. Check a subscription flow against the cancellation and recurring-charge duties.
- **Cases:** WhatsApp as the default customer channel in Mexico; marketplace seller reputation as social proof (MX). The FTC rule against fake reviews (2024) (international).
- **Lab:** A cohort and RFM analysis of the case's customer list in a spreadsheet.
- **Homework (project M4 part):** A retention plan for the project.
- **Quiz idea:** "AOV 400 MXN, contribution 35%, four orders per year, two-year customer life. What is the contribution LTV?" Answer: 1,120 MXN.

### S15 · Semana 15 · Sesión 15 de 17
**ES:** Medir para decidir
**EN:** Measuring to decide

- **Original items:** O7.1, O7.2, O7.3. Adds A9.
- **Mental model:** A metric tree: revenue = sessions × conversion rate × AOV, and contribution follows from it. An event model records who did what, when, and with which properties. Dashboards start from a decision. Attribution is not causation.
- **Current instance:** GA4, with Universal Analytics retired in 2023, plus a free dashboard tool.
- **Topics**
  1. The KPI tree and a north-star metric
  2. Event-based measurement: events, parameters, users, sessions; the data layer; consent
  3. The purchase event and the funnel report
  4. Attribution models and their limits; incrementality through holdouts and geo tests
  5. Dashboard design: question, metric, chart, decision
  6. Data quality: reconciling analytics revenue with orders (consent, ad blockers, refunds)
- **Code card**
  ```js
  gtag('event', 'purchase', {
    transaction_id: 'SL-1042', value: 389.00, currency: 'MXN',
    items: [{ item_id: 'SL-VER-250-GR', quantity: 1, price: 389.00 }]
  });
  ```
- **Objectives**
  1. Build a KPI tree for the case.
  2. Specify an event plan of five events with their parameters.
  3. Reconcile analytics revenue against order revenue and explain the gap.
  4. Choose between an attribution report and a holdout test for a given business question.
- **Cases:** reading a Hot Sale campaign (MX). The migration from Universal Analytics to GA4 as a tool death, and Data Studio's 2022 renaming to Looker Studio (international).
- **Lab:** Answer five business questions in a public GA4 demo account, then build a one-page dashboard.
- **Homework (project M4 part):** A measurement plan for the project.
- **Quiz idea:** "Revenue fell 10%, while sessions and AOV stayed flat. Which branch of the tree moved?" Answer: conversion rate.

### S16 · Semana 16 · Sesión 16 de 17 · closes with project presentations
**ES:** Reglas, ética y lo que viene
**EN:** Rules, ethics and what comes next

- **Original items:** O8.1 (consolidated), O8.2. Adds A10 and A11 (capstone).
- **Mental model:** Rules follow harms: information asymmetry, deception, misuse of data, concentrated power. Ethics starts where compliance ends. A trend is judged with the tool card, not with hype.
- **Current instance:** agentic commerce, where AI agents search and pay on a person's behalf (ACP, AP2, UCP; verify adoption in Mexico).
- **Topics**
  1. Consumer-protection map: LFPC art. 7 Bis, 32, 56 and 76 Bis; PROFECO enforcement; NMX-COE-001 as a voluntary standard
  2. Intellectual property: trademarks (IMPI, LFPPI 2020), copyright and notice and takedown (LFDA 2020), counterfeits and brand registries on marketplaces
  3. Deceptive design: sneaking, false urgency, obstruction, confirmshaming, forced continuity; EU DSA art. 25 as an international reference
  4. AI in commerce: generated product content and images (accuracy, disclosure, IP), personalization and price fairness
  5. Agentic commerce evaluated with the eight questions
  6. Course synthesis: the five jobs and their sixteen models
- **Objectives**
  1. Identify five deceptive-design patterns in screenshots and name the rule each one breaches.
  2. Check a listing for trademark and copyright risk.
  3. Apply the full tool card to agentic commerce and state a dated verdict.
  4. Defend the project's decisions in a ten-minute presentation.
- **Cases:** PROFECO's Buen Fin monitoring; IMPI actions against counterfeit sellers (MX). The FTC's case against Amazon over Prime cancellation, settled in 2025 (verify amount and terms); EU DSA (international).
- **Lab:** A deceptive-design hunt on three Mexican sites, plus a trend evaluation of agentic commerce.
- **Homework (project M4 due):** The final project dossier and presentation.
- **Quiz idea:** A screenshot of a cancellation flow that takes five screens with a "Are you sure you want to lose your benefits?" prompt. Name the patterns. Answer: obstruction and confirmshaming.

### S17 · Semana 17 · Sesión 17 de 17
**ES:** Examen final
**EN:** Final exam

- **Coverage:** S01 to S16.
- **Durability design:** at least one "unseen instance" item, where students apply the tool card to a fictional new tool or regulation written for the exam. At most 20% of points may depend on knowing a current brand-specific fact.

---

## 4. Assessment plan and running project

### Weights (same five-by-twenty structure as COM102)

| Component | Content | When | Weight |
|---|---|---|---|
| Parcial 1 | S01 to S08 | Week 8 | 20% |
| Parcial 2 | S09 to S13 | Week 13 | 20% |
| Proyecto: *Expediente de tienda* | Team dossier and presentation | Milestones in weeks 4, 8, 12 and 16 | 20% |
| Examen final | All sessions, including one unseen-instance item | Week 17 | 20% |
| Tareas y quizzes | Weekly homework and quizzes; the two lowest are dropped | Whole course | 20% |

### Exam design rules (the durability check)

- At least 50% of points apply concepts to a new case.
- At most 20% of points may depend on a dated, brand-specific fact, and only on facts that are in the annex.
- Every exam includes one unseen-instance item answered with the tool card.

### Running project: Expediente de tienda (store dossier)

Teams of three or four take a real Mexican micro or small business (with the owner's consent) or their own venture. In class, the Café Siete Lunas case models each deliverable a week ahead of the teams.

| Milestone | Due | Contents | Share of the 20% |
|---|---|---|---|
| M1 Modelo y evidencia | End of S04 | Channel map, value proposition, order waterfall, five interviews, smoke test with UTM links | 3% |
| M2 Tienda | Before S09 | Platform memo (TCO and exit plan), ten-SKU catalog with JSON-LD, product-page wireframe, checkout prototype | 4% |
| M3 Operación | Before S13 | Payment plan, data inventory and privacy notice, fraud rules, order state diagram, system map, fulfillment choice, returns policy | 4% |
| M4 Crecimiento y cierre | S16 | Acquisition, retention and measurement plans; legal and ethics checklist; current-stack memo applying the tool card to two tools; ten-minute presentation | 9% (dossier 6, presentation 3) |

**Individual accountability:** an oral check at the presentation, in the same spirit as the COM102 honor code. Each member must explain any section of the dossier the instructor picks.

---

## 5. Current-stack annex, as of October 5, 2026

Everything in this section is an instance and is reviewed each term. The session decks link to it rather than repeating it. A suggested source is `annex-stack.{es,en}.yaml`, with the review date on its cover.

### 5.1 Instances by concept

| Concept (durable) | Current instances in Mexico | International instances | What to re-check each term |
|---|---|---|---|
| Hosted store (rented software) | Tiendanube, Shopify, Wix | Shopify, BigCommerce, Squarespace | Plans and transaction fees; support for local payment methods |
| Self-hosted store (owned software) | WooCommerce on WordPress | WooCommerce, Adobe Commerce (Magento) | Major versions and end-of-life dates |
| Enterprise platform | VTEX, Salesforce Commerce Cloud, Adobe Commerce | Same | Not needed every term |
| Marketplace | Mercado Libre, Amazon México, Walmart, Liverpool, Coppel, TikTok Shop, Shein, Temu | Amazon, eBay, Etsy | Commissions, free-shipping threshold, fulfillment program terms |
| Social and conversational surface | WhatsApp Business (app and platform), Instagram, Facebook, TikTok | Same | Shop features added or removed (they change often) |
| Account-to-account push payments | SPEI, CoDi, DiMo (Banxico) | Pix (Brazil), UPI (India), FedNow (US) | Banxico rule changes (deadline December 14, 2026, verify); status of the Ley de Economía Digital para Pagos initiative (sent to Congress September 2026, not law, verify) |
| Card acquiring and gateways | Stripe, Conekta, Openpay (BBVA), Mercado Pago, PayPal, Clip | Stripe, Adyen, PayPal | Fees; supported methods |
| Cash voucher network | OXXO (through PSPs), Spin by OXXO | Boleto (Brazil) | Availability and maximum amounts |
| Installment credit | MSI on cards; Aplazo, Kueski Pay | Klarna, Affirm (Klarna's availability to Mexican merchants unconfirmed, verify) | New entrants; CNBV and CONDUSEF guidance |
| Card security standards | PCI DSS v4.0.1; EMV 3-D Secure 2.x | Same | New PCI SSC versions |
| Authentication | Passkeys (FIDO2/WebAuthn) | Same | Support across platforms |
| Fulfillment and carriers | Mercado Envíos (Full, Flex), Amazon FBA, 99minutos, Skydropx, Envia.com, Estafeta, DHL, FedEx, Paquetexpress, J&T Express | Amazon FBA, Shopify fulfillment partners | Rates; pickup-point networks |
| Accounting and ERP with CFDI | Odoo, Aspel, CONTPAQi, SAP Business One, Dynamics 365 Business Central | Same | CFDI version; complement updates |
| CRM, email and messaging | HubSpot, Klaviyo, Mailchimp, Brevo, WhatsApp platform | Same | Sender requirements; WhatsApp pricing model |
| Web analytics | GA4, Google Tag Manager, Looker Studio, Microsoft Clarity | Same, plus Adobe Analytics | Consent-mode requirements; GA4 interface changes |
| Ad and retail-media platforms | Google Ads, Meta Ads, TikTok Ads, marketplace ads | Same, plus Amazon Ads | Auction and targeting changes |
| Search and answer engines | Google Search (AI Overviews in Mexico, verify), AI assistants with shopping | Same | Reach of AI summaries; merchant feed requirements |
| Agentic commerce protocols | Availability in Mexico unconfirmed (verify) | OpenAI ACP (September 2025), Google AP2 (2025), Google UCP (January 2026, verify) | Adoption; merchant onboarding; consumer protection |
| Accessibility | WCAG 2.2 | WCAG 2.2; European Accessibility Act | WCAG 3 draft progress |
| Performance | Core Web Vitals (LCP, INP, CLS) | Same | Changes to the metric set |
| Product data | GS1 México (GTIN), schema.org | Same | schema.org Product changes |

### 5.2 Regulators and laws (Mexico)

| Area | Regulator | Instrument | What to re-check each term |
|---|---|---|---|
| Consumer protection | PROFECO | LFPC (art. 7 Bis, 32, 56, 76 Bis; December 12, 2025 reform on recurring charges, verify sections); NOM-050-SCFI-2004; NMX-COE-001-SCFI-2018 (voluntary, verify); REPEP; Concilianet | New reforms; Buen Fin monitoring rules |
| Personal data | SABG | LFPDPPP (DOF March 20, 2025) | Whether the regulation has been issued (verify); SABG guidance |
| Tax and invoicing | SAT | CFF (art. 30-B, platform access from April 2026, verify), LIVA, LISR, 2026 RMF, CFDI 4.0, Carta Porte complement | Withholding rates (2.5% ISR on goods and 8% IVA in 2026, verify); new RMF each January |
| Payments | Banxico | SPEI, CoDi and DiMo rules | Changes to the transfer and QR standard |
| Fintech and financial services | CNBV, CONDUSEF | Ley Fintech (2018) | Licenses of new providers |
| Intellectual property | IMPI, INDAUTOR | LFPPI (2020), LFDA (notice and takedown since 2020) | Enforcement campaigns |
| Competition | Comisión Nacional Antimonopolio (replaced COFECE in 2025, verify) | Ley Federal de Competencia Económica (2025, verify); marketplace finding of September 2025 | Follow-up actions on marketplaces |
| Customs | ANAM, SAT | Simplified courier regime: 19% from January 2025, 33.5% from August 15, 2025 (verify current rate and exceptions) | Rate changes; agreement exceptions |
| Not applicable to e-commerce | Secretaría de Economía | NOM-247-SE-2021 (residential real estate) | Only relevant for housing projects |

### 5.3 International references

GDPR (2018); EU Digital Services Act (fully applicable since February 2024; art. 25 on deceptive design); EU Digital Markets Act; European Accessibility Act (June 28, 2025); EU AI Act (in force August 2024 with phased obligations; verify 2026 dates given proposals to delay); PSD2 strong customer authentication (verify PSD3 status); FTC rule on consumer reviews and testimonials (October 21, 2024); FTC "click to cancel" rule vacated by a US appeals court in 2025 (verify); US de minimis suspended for all countries on August 29, 2025; PCI SSC; EMVCo; W3C (WCAG); Gmail and Yahoo bulk-sender requirements (February 2024).

### 5.4 Recent changes to use as teaching cases (dated)

| Date | Change | Concept it teaches |
|---|---|---|
| June 2020 | Magento 1 end of life | Platform end of life, exit cost |
| November 2020 | LFPPI replaces Ley de la Propiedad Industrial | Laws are instances too |
| April 2021 | Apple ATT (iOS 14.5) | Signal loss, value of first-party data |
| October 2022 | Facebook Live Shopping ends; Data Studio renamed Looker Studio | Surface volatility; names change, function stays |
| March 2023 | Instagram live shopping ends | Surface volatility |
| April 1, 2023 | CFDI 4.0 mandatory | Invoicing as part of the order |
| July 1, 2023 | Universal Analytics stops processing (UA 360 on July 1, 2024) | Tool death, measurement concepts survive |
| September 30, 2023 | Google Optimize closes | Tool death, experimentation survives |
| February 2024 | Gmail and Yahoo sender requirements | Deliverability standards |
| March 2024 | INP replaces FID | Metric vs goal |
| December 31, 2024 | PCI DSS v4.0 retired; v4.0.1 current | Standards have versions |
| January and August 2025 | Mexican courier-import rate 19%, then 33.5% (verify) | Landed cost, policy risk |
| February 2025 | TikTok Shop begins transacting in Mexico | New surface, same pattern |
| March 21, 2025 | New LFPDPPP; INAI extinguished; SABG becomes regulator | Regulators change, duties remain |
| June 28, 2025 | European Accessibility Act applies | Accessibility as an obligation |
| August 29, 2025 | US de minimis suspended | Cross-border policy risk |
| September 2025 | Marketplace featured-offer finding in Mexico; OpenAI ACP | Platform power; agentic commerce |
| October 2025 | Most Privacy Sandbox APIs retired; third-party cookies remain in Chrome | Forecasts fail, consent strategy holds |
| December 2025 | LFPC reform on recurring charges (verify) | Subscription duties |
| January 2026 | Platform ISR withholding on goods rises to 2.5%; Google UCP announced (verify both) | Fees and taxes as order costs; protocol competition |

### 5.5 Checklist for the start of each term

1. Read the DOF for reforms to the LFPC, LFPDPPP, CFF, LIVA, LISR, and the new RMF.
2. Check the SABG site for guidance and the status of the data-protection regulation.
3. Check Banxico for SPEI, CoDi and DiMo rule changes.
4. Check PROFECO for Buen Fin and Hot Sale rules and dates, and any new monitoring programs.
5. Check marketplace seller pages for commissions, free-shipping thresholds and fulfillment terms.
6. Check the pricing pages of the platforms and payment providers named in the decks, and record the date read.
7. Check courier-import rates and US import rules.
8. Check analytics, consent and email-sender requirements.
9. Read the latest AMVO study and ENDUTIH for the market-size slides.
10. Check the status of agentic-commerce protocols and their availability in Mexico.
11. Update the "Hoy, en México" instance slide in each session with the new verification date.

---

**For the build:** the repo already has a `commerce` palette (`language: commerce` in `ppts/kit/tokens.py`), and the generic scanner in `ppts/kit/highlight.py` covers the JSON and JS code cards. A natural home for the course is `ppts/ecommerce/fundamentos-del-comercio-electronico/{es,en}/wNN.{es,en}.yaml`, with `w01.0` as the intro deck carrying the roadmap and grading table above. Nothing in the repository was changed while writing this proposal.