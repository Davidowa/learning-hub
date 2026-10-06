<!-- Propuesta de temario, lente: practica. Borrador de un agente diseñador, sin verificar; ver HANDOFF-auditoria-y-cursos-nuevos.md en la raíz. -->

# Fundamentos del comercio electrónico / Fundamentals of E-commerce
## Practice-first redesign proposal, as of October 5, 2026

**Lens.** By 2027-2030, a junior e-commerce analyst or manager has to do eight things on the job. They run the weekly numbers and turn them into a decision. They keep the catalog and listings clean across channels. They read the funnel and propose tests. They choose and run payment methods and handle fraud and disputes. They coordinate orders, stock, shipping and returns. They plan campaigns against a cost ceiling. They keep the operation compliant with PROFECO, privacy and SAT rules. And they decide whether a new tool or trend deserves a pilot. Every session below trains one or more of these tasks on a real artifact.

**Design spine**
- **Four blocks** cover the 16 teaching weeks: Discover (S1-S4), Build (S5-S8, Parcial 1), Operate (S9-S13, Parcial 2) and Grow (S14-S16, project). The final exam is S17.
- **One running case** is used in every lab: *Calzado Andar*, a fictional D2C footwear brand from León, Guanajuato, with a data pack the professor provides.
- **One team project** grows every week: the *Playbook de operación* for a real micro or small business, or for the team's own product.
- **Every session** teaches one transferable mental model plus one current, verifiable instance, and names one "metric of the week".
- **Tools live in the dated annex (Section 5).** Sessions swap the instance, never the concept.
- **The dependency rule is checked.** The lab of week N only uses what weeks 1 to N taught. For example, GA4 waits until S14, and the privacy-notice template in S4 is a given form, with the full treatment in S11.

---

## 1. Audit of the original syllabus

Numbering follows the original: unit.item.

| # | Original item | Verdict | Reason (obsolescence facts dated; uncertain ones marked) | Lands in |
|---|---|---|---|---|
| Title | Fundamentos del comercio electrónico / "Fundamental principles of e-commerce" | Keep (ES), rename (EN) | The Spanish title is fine. "Fundamentals of E-commerce" is the natural American English form. | Covers, footer |
| 1.1 | Modelos y canales (B2C, B2B, C2C, D2C, marketplaces, omnicanalidad, social commerce, comercio conversacional) | Keep + reframe | The taxonomy has been stable since the 1990s, but the channel labels keep changing. Teach it through a **control matrix**: who owns the customer, the data, the price, fulfillment and risk. That matrix still works for the next channel. Feature churn shows why: Facebook Live Shopping ended Oct 1, 2022, and TikTok Shop opened in Mexico in February 2025. | S2; conversational part in S16 |
| 1.2 | Propuesta de valor y cliente objetivo | Keep + extend | Jobs-to-be-done and the value proposition canvas are enduring. The original has no per-order economics, so a proposition cannot be judged as viable. Add contribution margin and break-even CAC. | S3 |
| 1.3 | Validación de mercado (entrevistas, encuestas, prototipos, landing pages, pruebas de venta, PMF) | Keep + reframe | Add an **evidence ladder** (opinion < stated intent < behavior < payment) and pass/fail thresholds written before the test runs. Treat PMF as a set of signals, not one number. Add the legal and ethical limits of tests: a privacy notice on any form, and no charging for something you cannot ship. | S4 |
| 2.1 | Tipos de plataformas (SaaS, CMS, tiendas propias, marketplaces; Shopify, Tiendanube, WooCommerce, Wix, Amazon, Mercado Libre) | Reframe | Product names are instances and move to the annex. The enduring skill is choosing by TCO, control, local fit and **exit cost**. Real churn: Magento 1 reached end of life on June 30, 2020. Mercado Libre closed Mercado Shops on Dec 31, 2025 (sellers moved to an in-marketplace page). Shopify Payments became available in Mexico in 2025 (verify), which changed the comparison. "Tiendas propias" is ambiguous; split it into self-hosted open source and custom-built. | S5 |
| 2.2 | Catálogo e inventario digital (SKU, categorías, variantes, precios, imágenes, disponibilidad, inventario) | Keep + split | The catalog becomes "product data as infrastructure". The same rows now feed the store, marketplaces, ads and AI shopping surfaces, so identifiers, feeds and structured data are essential. Inventory moves to S12 and merges with 5.1. | S6 (catalog), S12 (inventory) |
| 2.3 | Arquitecturas e integraciones (APIs, Headless, Composable) | Reframe + merge | "Headless" and "composable" are vendor-era labels; the MACH Alliance was founded in 2020. The durable concepts are coupling vs. decoupling, system of record, API vs. webhook, and build/buy/rent. Keep the labels only as current vocabulary. The integration practice merges with 8.3. | S5 (concept), S12 (practice) |
| 3.1 | UX/UI (navegación, jerarquía, accesibilidad, responsive, mobile-first) | Keep + update | Anchor accessibility to WCAG 2.2 (W3C Recommendation, Oct 2023). The European Accessibility Act has applied since June 28, 2025 to e-commerce sold into the EU. Add speed: INP replaced FID as a Core Web Vital in March 2024. "Responsive" and "mobile-first" are now baseline, so treat mobile as the default context rather than a separate topic. | S7 |
| 3.2 | Página de producto y checkout | Keep + localize | Add the Mexican specifics: total price including taxes and shipping, address entry by código postal and colonia, MSI/OXXO/SPEI shown before checkout, and a delivery promise by CP. | S7 |
| 3.3 | Optimización de conversión (CRO, A/B, CTA, prueba social, promociones, abandono) | Keep + reframe | Add experiment rigor: hypothesis, sample size, one primary metric, guardrails, no peeking. Add the ethical line between persuasion and dark patterns. Tool churn: Google Optimize closed Sept 30, 2023, and the method survived. Social proof must be genuine: the FTC rule on fake reviews took effect Oct 21, 2024. | S8; seasonal promotions in S15 |
| 4.1 | Medios de pago (tarjetas, transferencias, SPEI, wallets, diferidos, BNPL, pasarelas, procesadores) | Keep + expand | Separate rails, methods and providers. Mexico-specific items: MSI, cash vouchers at OXXO, SPEI with a reference per order, CoDi (2019) and DiMo (2023). Banxico Circular 9/2026 requires banks to standardize SPEI/CoDi/DiMo/QR transfers in their apps by Dec 14, 2026 (verify). Add BNPL (Kueski Pay, Aplazo), fees and settlement. | S9 |
| 4.2 | Seguridad y protección de datos (cifrado, tokenización, autenticación, privacidad) | Split + update | **Security** goes to S10. Cover scope reduction under PCI DSS v4.0.1 (v3.2.1 retired Mar 31, 2024; the future-dated requirements became mandatory Mar 31, 2025), tokenization, EMV 3-D Secure 2 (3DS 1.0 was retired in October 2022) and passkeys. **Privacy** goes to S11 under the new LFPDPPP. | S10, S11 |
| 4.3 | Fraude y gestión de riesgo (fraudes comunes, robo de identidad, contracargos, prevención) | Keep + extend | Add the economics of fraud loss vs. false declines and the chargeback evidence pack. Add Mexican patterns, such as fake SPEI receipts, which can be checked through Banxico's CEP. Add card-network monitoring programs (verify current program names and thresholds, e.g., Visa VAMP). | S10 |
| 5.1 | Gestión de pedidos e inventarios | Merge (with 2.2 inventory, 2.3, 8.3) | Teach the order as a state machine that crosses systems. Add available-to-promise, overselling across channels, and CFDI 4.0 in order-to-cash (mandatory since April 1, 2023). | S12 |
| 5.2 | Fulfillment y distribución (almacenamiento, preparación, transportistas, última milla) | Keep + extend | Add marketplace fulfillment programs (Mercado Libre Full, Amazon FBA), shipping aggregators, cost-to-serve, dimensional weight and peak-season capacity. | S13 |
| 5.3 | Modelos logísticos y posventa (dropshipping, 3PL, devoluciones, reembolsos, logística inversa) | Keep + reframe dropshipping | Dropshipping is a fulfillment model, and its cross-border economics changed in Mexico. Courier imports from countries without a trade agreement went from 19% (Jan 2025) to 33.5% from Aug 15, 2025 (verify thresholds). Tariffs of 5% to 50% on 1,463 tariff lines from non-FTA countries apply since Jan 1, 2026. Teach landed cost. Returns become a designed flow: policy, reason codes, disposition, refund. | S13 |
| 6.1 | Adquisición de tráfico (SEO, SEM, redes, contenidos) | Keep + reframe | SEO now includes AI answers: Google AI Overviews (2024), and AI Mode in Spanish, including Mexico, since September 2025. Add retail media (Mercado Ads, Amazon Ads). Measure under signal loss: Apple ATT (April 2021). Chrome kept third-party cookies and Google retired the Privacy Sandbox APIs in October 2025, so plan around consent and first-party data, not a cookie deadline. Spend is bounded by the CAC ceiling. | S15 |
| 6.2 | Social Commerce y contenido (redes, influencers, reseñas, comunidades, UGC) | Merge | On its own this item is a list of platforms whose features churn. Channel economics go to S2, creators and UGC as acquisition to S15, reviews on the product page to S7, and review authenticity and influencer disclosure to S11. | S2, S7, S11, S15 |
| 6.3 | Retención y fidelización (CRM, email, remarketing, automatización, lealtad) | Keep + extend | Add cohorts and margin-based LTV. WhatsApp is the default Mexican channel; the Business Platform moved to per-message pricing on July 1, 2025. Add marketing consent, and subscriptions under the Dec 2025 LFPC reform. "Remarketing" becomes consented audiences. | S16 |
| 7.1 | Indicadores (conversión, ticket, CAC, LTV, ROAS, margen) | Keep, move earlier, thread | Introduce the revenue equation in S1, unit economics in S3, one "metric of the week" every session, and the full KPI tree in S14. Add contribution margin after marketing, plus MER alongside ROAS. LTV must be margin-based and read by cohort. | S1, S3, S14 (thread) |
| 7.2 | Embudo de conversión | Keep + split | Diagnosis goes to S8 (from a provided table); instrumentation goes to S14 (GA4 funnel exploration). | S8, S14 |
| 7.3 | Analítica digital (GA4, dashboards) | Reframe | GA4 is the current instance of event-based analytics. Universal Analytics stopped processing standard properties on July 1, 2023, and GA4 renamed "conversions" to "key events" in March 2024. The durable skills are the measurement plan, the event schema, consent and data quality, and the decision memo. | S14 |
| 8.1 | Protección al consumidor y privacidad | Keep + update | **LFPC** Art. 76 Bis (e-commerce) as reformed in the DOF on Dec 12, 2025 (recurring charges and cancellation). **NMX-COE-001-SCFI-2018**, a voluntary e-commerce standard in force since 2019, and the Código de Ética de Comercio Electrónico (DOF Feb 26, 2021). **LFPDPPP** published March 20, 2025, which repealed the 2010 law; INAI no longer exists and the regulator is the **Secretaría Anticorrupción y Buen Gobierno (SABG)**. Its implementing reglamento was still pending more than a year later (verify). **Note:** NOM-247-SE-2021 regulates commercial information for *residential real estate*, not e-commerce. Cite it only as an example of a sector NOM that reaches online portals. | S11 |
| 8.2 | Propiedad intelectual y ética digital (derechos de autor, marcas, dark patterns, transparencia, IA) | Keep + split | IP: IMPI and the LFPPI (in force Nov 5, 2020), the LFDA, counterfeits and marketplace brand programs. Dark patterns: S8 and S11. AI: disclose AI-generated content, and state automated processing in the privacy notice (the new LFPDPPP requires it per legal commentary, verify). EU AI Act as the international benchmark: GPAI duties since Aug 2, 2025, and Annex III high-risk duties moved to Dec 2, 2027 by the Digital Omnibus (verify). | S11, S15 |
| 8.3 | Ecosistema tecnológico (CRM, ERP, OMS, WMS, APIs, webhooks) | Merge | The acronyms do not transfer; data ownership and event flow do. Teach it as "one order, five systems", adding the PSP, the carrier and the PAC that issues the CFDI. | S12 |

**Structural verdict.** The original's 8 units of 3 items are reorganized into 4 blocks that follow the lifecycle of a real operation (discover, build, operate, grow). Legal moves from the last unit to S11, before launch, because compliance is a launch requirement and not an epilogue.

---

## 2. Additions the original lacks

| # | Addition | Why it earns a place | Lands in |
|---|---|---|---|
| A1 | Unit economics and pricing: contribution margin per order, break-even CAC and ROAS, marketplace fee stack, MSI cost | Most small e-commerce failures are margin failures, and computing these numbers is the junior analyst's first daily task. | S3, threaded through all sessions |
| A2 | Product data and feeds: identifiers (GTIN via GS1 México), Merchant Center and marketplace listings, schema.org | One catalog now feeds store search, marketplaces, shopping ads and AI assistants. Bad data cannot be found anywhere. | S6 |
| A3 | Experiment design and statistical literacy | Without sample size and a no-peeking rule, "A/B testing" produces false wins. | S8 |
| A4 | Mexican tax in operations: CFDI 4.0, factura global, platform withholding regime (since June 1, 2020), CFF Art. 30-B real-time platform access (from April 1, 2026, verify) | Every Mexican order touches SAT. Students who ignore it design checkouts that cannot invoice. | S2, S12 |
| A5 | Cross-border trade and landed cost | Mexican courier and tariff rules changed in 2025-2026 and broke dropshipping economics. The concept outlives any rate. | S13 |
| A6 | Marketplace operations: listing quality, reputation, fulfillment programs, retail media | Most Mexican online retail flows through marketplaces, yet the original treats them only as a platform type. | S2, S6, S13, S15 |
| A7 | Measurement under privacy constraints: consent, first-party data, server-side conversions, incrementality | Attribution keeps degrading, so a junior analyst must know what the numbers can and cannot say. | S14, S15 |
| A8 | Customer service and reputation operations: "where is my order" contacts, SLAs, PROFECO's online complaint system (Concilianet), replies to reviews | Service failures drive returns, complaints and churn more than marketing does. | S13, S16 |
| A9 | Peak-season operations: Hot Sale, Buen Fin, December, Día de las Madres | Peaks stress every system at once and anchor real deadlines. | S13, S15 |
| A10 | AI in e-commerce work and agentic commerce, evaluated rather than hyped | AI already writes listings and answers shopping queries. In 2025-2026 agentic checkout showed both promise and a fast retreat (see the annex). | S6, S11, S15; course AI-use rule from S1 |
| A11 | Tool and trend evaluation method (RADAR) | This is what makes the course time-transcendent: students practice judging the next tool themselves. | S5, S15, final exam |
| A12 | Business communication with data: decision memo, weekly business review (WBR), quarterly business review (QBR) deck | Analysis that does not end in a decision is not done. Every assessment mirrors these formats. | S5, S14, S16, all exams |

**RADAR**, the course's evaluation rubric for any tool or trend:
- **R**esuelve un problema real / **R**eal problem
- **A**dopción comprobable / **A**doption evidence
- **D**atos y salida / **D**ata and exit
- **A**juste local (MXN, SPEI, OXXO, CFDI, Spanish, Mexican law) / **A**lignment with the local market
- **R**etorno y riesgo / **R**eturn and risk

Each RADAR evaluation ends in **wait / pilot / adopt**, plus the one piece of evidence that would change the verdict.

---

## 3. The 17-session plan

### Roadmap

| Block | Sessions | Focus | Assessment |
|---|---|---|---|
| 01 · Descubrir / Discover | S1-S4 | System view, models and channels, customer and economics, validation | Weekly artifacts |
| 02 · Construir / Build | S5-S8 | Platform, catalog, shopping experience, conversion | **Parcial 1** closes S8 |
| 03 · Operar / Operate | S9-S13 | Payments, risk, compliance, orders and systems, fulfillment | **Parcial 2** closes S13 |
| 04 · Crecer / Grow | S14-S16 | Measurement, acquisition, retention | **Proyecto** closes S16 |
| Cierre | S17 | Final exam | **Examen final** |

Each session gives: original items covered, mental model and current instance, topics, objectives ("the student will be able to..."), examples, metric of the week, lab (in class, on the Calzado Andar case), homework (the team applies the lab to its own operation), and a quiz idea (multiple choice; the correct answer is marked ✔).

---

### S1 · Encuadre y el comercio electrónico como sistema / Course framing and e-commerce as a system
Two decks: `w01.0` (course framing: roadmap, grading table, tools, AI-use rule, diagnostic) and `w01` (teaching).
- **Original items:** 7.1 (first pass); preview of all units.
- **Mental model:** three flows (information, money, goods) and the revenue equation (sessions × conversion rate × AOV), minus a cost stack. **Current instance:** one Mercado Libre order paid in cash at OXXO and delivered by Mercado Envíos, traced end to end.
- **Topics:**
  1. How the course works: running case, team project, five graded components, AI-use rule (disclose, verify, defend).
  2. E-commerce defined by its three flows, and the actors on each: customer, merchant, platform, PSP, bank, carrier, regulator.
  3. The revenue equation and the cost stack: COGS, platform and payment fees, shipping, packaging, returns, marketing.
  4. Mexico in context: AMVO Estudio de Venta Online 2026 puts retail e-commerce at MXN 941 billion in 2025, +19.2%, 17.7% of retail (verify before putting on a slide). Cash and installments are local traits. International comparison.
  5. Concepts vs. instances: why tools live in an annex, with a first look at the retirement log.
- **Objectives:**
  - Map one real order across the three flows, naming at least six actors and the data each one holds.
  - Split a month-over-month revenue change into sessions, conversion and AOV effects.
  - Classify ten course terms as enduring concept or current instance.
  - State the five graded components, their weeks and the AI-use rule.
- **Examples:** MX: the Mercado Libre + OXXO + Mercado Envíos order; Hot Sale and Buen Fin as national peaks. International: Amazon's "virtuous cycle" sketch; Brazil's Pix as a contrast in how money moves.
- **Metric of the week:** conversion rate and AOV.
- **Lab, "Disecciona un pedido":** pairs map a purchase they made in the last three months onto a three-flow template, then decompose Calzado Andar's August vs. September revenue.
- **Homework:** team charter; route choice (A: a real small business, with an owner consent letter; B: the team's own product); one-page "system map today" of that business.
- **Quiz:** "Sessions rose 20% and revenue stayed flat, with the same AOV. What happened?" A) Conversion fell about 17% ✔ B) Returns rose C) Ad spend rose D) Shipping costs rose.

### S2 · Modelos de negocio y canales: quién controla qué / Business models and channels: who controls what
- **Original items:** 1.1, 6.2 (social as a channel), 2.1 (marketplace as a channel).
- **Mental model:** a control matrix (customer relationship, data, price, assortment, fulfillment, risk) plus the take rate; any new channel gets scored the same way. **Current instance:** TikTok Shop México (open since February 2025) vs. Mercado Libre vs. an own store.
- **Topics:**
  1. Who sells to whom: B2C, B2B, C2C, D2C, B2B2C; 1P vs. 3P on marketplaces.
  2. Marketplaces: what they give (traffic, trust) and what they keep (data, customer, rules); the fee stack and the platform ISR/IVA withholding regime.
  3. Omnichannel: click and collect, ship from store, return in store; stock visibility as the prerequisite.
  4. Social and creator commerce: in-app checkout vs. link-out; feature churn (Facebook Live Shopping ended Oct 1, 2022).
  5. Conversational commerce: WhatsApp catalogs and chat-to-pay as the Mexican default for small sellers.
  6. Platform risk: changes in rules or fees, and closures (Mercado Shops, Dec 31, 2025).
- **Objectives:**
  - Classify eight businesses by model and primary channel.
  - Fill a control matrix for four channels and name the data the merchant loses in each.
  - Compute net revenue per order after commission, fixed fee, shipping subsidy and withholding for two channels.
  - Recommend a launch channel mix and name two risks with their mitigations.
- **Examples:** MX: Mercado Libre (3P, Full), Amazon México (1P/3P), Liverpool (click and collect), Walmart México marketplace, TikTok Shop, a distributor taking orders from corner stores (tienditas) by WhatsApp. International: Shein and Temu cross-border models; Amazon's 3P share.
- **Metric of the week:** take rate; net revenue per order.
- **Lab:** control matrix and net-per-order for Calzado Andar in its own store, Mercado Libre, Amazon and TikTok Shop, using a dated fee sheet. Each pair checks one live fee page and records any difference.
- **Homework:** team channel map, control matrix and launch-channel recommendation (one page).
- **Quiz:** "A brand sells only as a 3P seller on a marketplace. What does it usually NOT get?" A) Payouts B) The buyer's email for its own campaigns ✔ C) Sales reports D) Ratings.

### S3 · Cliente, propuesta de valor y economía unitaria / Customer, value proposition and unit economics
- **Original items:** 1.2; 7.1 (margin, CAC, LTV first pass).
- **Mental model:** job to be done → value proposition → price; contribution margin per order is the most you can pay to acquire a customer. **Current instance:** the fee, MSI and shipping lines of a real Mexican checkout.
- **Topics:**
  1. Segments and customer profiles: jobs, pains, gains; evidence vs. assumptions.
  2. Value proposition canvas and positioning statement.
  3. Pricing basics: cost-plus, value-based, anchoring, bundles, free-shipping thresholds, total-price display.
  4. Unit economics: AOV, COGS, payment fees, MSI cost, shipping, packaging, returns allowance, contribution margin.
  5. Break-even CAC, break-even ROAS, and a first margin-based LTV.
- **Objectives:**
  - Write a positioning statement that names the segment, the job, the current alternative and the differentiator.
  - Build a one-order unit-economics sheet and compute contribution margin.
  - Compute break-even CAC and break-even ROAS.
  - Identify the two largest cost lines and propose one lever for each.
- **Examples:** MX: a Veracruz specialty-coffee roaster selling D2C vs. through supermarkets; a 6-month MSI promotion paid for by the merchant; marketplace free-shipping thresholds (verify current amounts). International: Warby Parker home try-on; Dollar Shave Club's subscription proposition.
- **Metric of the week:** contribution margin per order; break-even CAC.
- **Lab:** unit-economics sheet for Calzado Andar's best seller in its own store vs. Mercado Libre; free shipping vs. a free-shipping threshold scenario.
- **Homework:** team customer profile, value proposition canvas, positioning statement and unit-economics sheet.
- **Quiz:** "Net price $750, COGS $300, payment fees $30, shipping $110, packaging $20, returns allowance $40. What is the contribution margin before marketing?" A) $250 ✔ B) $450 C) $340 D) $290.

### S4 · Validación de mercado con experimentos baratos / Market validation with cheap experiments
- **Original items:** 1.3.
- **Mental model:** the evidence ladder (opinion < stated intent < behavior < payment), with pass/fail thresholds written before the test runs. **Current instance:** a landing page or preorder on a trial store, reached through UTM-tagged links.
- **Topics:**
  1. Assumption mapping (desirability, viability, feasibility), riskiest first.
  2. Interviews about past behavior, not opinions; what surveys can and cannot tell you.
  3. Behavioral tests: smoke test, honest fake door, preorder, concierge, marketplace test listing.
  4. Tagging traffic with UTM parameters and a naming convention.
  5. Reading results: thresholds, sample-size intuition, PMF signals (retention; the "very disappointed" 40% survey).
  6. Minimum legal and ethics for tests: privacy-notice template on every form, no charging for what cannot ship, honest preorder dates.
- **Code card (UTM link):**
  `https://tienda.example/sandalia-tule?utm_source=instagram&utm_medium=social&utm_campaign=valida_tule_2027_02&utm_content=reel_a`
- **Objectives:**
  - Rank six assumptions by risk and existing evidence.
  - Design a test card with metric, threshold, sample and stop date.
  - Build UTM links for three sources that follow a convention.
  - Decide to persevere, pivot or stop from a results table, and justify the decision.
- **Examples:** MX: an Instagram/WhatsApp preorder by a small fashion brand; a Mercado Libre test listing. International: Zappos (1999, photos of shoes taken in local stores); Dropbox's demo video; Buffer's two-page test.
- **Metric of the week:** visitor-to-signup or visitor-to-preorder rate; cost per validated lead.
- **Lab:** test card, landing page (from a template) and UTM set for a new Calzado Andar product, with thresholds written down first.
- **Homework:** a 7-day real validation with at least 5 interviews and one behavioral test, reported as a one-page evidence report ending in a decision.
- **Quiz:** "Which is the strongest evidence of demand?" A) 80% of respondents say they would buy B) 300 likes C) 40 people paid a $100 deposit ✔ D) An influencer said she loves it.

### S5 · Plataformas y arquitectura: elegir sin casarte / Platforms and architecture: choosing without lock-in
- **Original items:** 2.1, 2.3 (concept).
- **Mental model:** the build/buy/rent spectrum; coupling (monolith → headless → composable); 12-month TCO plus exit cost; RADAR for any tool. **Current instance:** Shopify vs. Tiendanube vs. WooCommerce for a Mexican small business, priced from live pages.
- **Topics:**
  1. What a platform does: catalog, cart, checkout, payments, orders, apps, themes.
  2. Hosting models: SaaS, self-hosted open source, marketplace storefronts, enterprise suites.
  3. APIs without code: request, response, limits, app ecosystems.
  4. Headless and composable: what decoupling buys, what it costs, and when a small business should not do it.
  5. TCO and exit cost; platform lifecycle (Magento 1 end of life June 30, 2020; Mercado Shops closure).
  6. RADAR, introduced and practiced.
- **Objectives:**
  - Compare three platforms with a weighted matrix whose weights come from the team's S2-S3 artifacts.
  - Compute a 12-month TCO at projected volume, including transaction fees and apps.
  - Draw monolithic vs. headless and name two conditions under which headless is not worth it.
  - Apply RADAR to one tool and state one evidence gap.
- **Examples:** MX: Tiendanube (LATAM focus), Shopify (Shopify Payments in Mexico since 2025, verify), WooCommerce with a local PSP plugin, VTEX (LATAM enterprise), Mercado Shops' closure. International: MACH Alliance (2020) and composable vendors.
- **Metric of the week:** platform TCO as a percentage of revenue.
- **Lab:** platform decision memo for Calzado Andar (matrix, TCO, RADAR, recommendation).
- **Homework:** open a development or trial store on the chosen platform (admin screenshot), plus the team's one-page decision memo.
- **Quiz:** "Which line is most often missing from a platform TCO?" A) Monthly plan B) App subscriptions and transaction fees ✔ C) Domain D) Theme.

### S6 · Catálogo y datos de producto / Catalog and product data
- **Original items:** 2.2 (catalog).
- **Mental model:** one source of truth, many outputs; data quality decides whether a product can be found in store search, marketplaces, ads and AI assistants. **Current instance:** one set of rows exported as a Merchant Center feed and as a Mercado Libre listing.
- **Topics:**
  1. SKU design: product vs. variant vs. bundle; option dimensions.
  2. Attributes and taxonomy: filters, marketplace category trees, Google product taxonomy.
  3. Identifiers: GTIN (GS1 México), MPN, brand.
  4. Content: titles, descriptions, images, size guides, mandatory commercial information.
  5. Feeds and sync: CSV vs. API, update frequency, error handling.
  6. Machine-readable products: schema.org `Product`, and why AI shopping surfaces depend on structured data.
- **Code card:** a 12-line JSON-LD `Product` (name, sku, gtin13, brand, offers.price, priceCurrency "MXN", availability).
- **Objectives:**
  - Design a SKU convention for a line with two option dimensions.
  - Build a catalog CSV of at least 15 rows that passes a 12-point checklist.
  - Rewrite a listing title to a marketplace's guidelines.
  - Diagnose and fix five feed errors.
- **Examples:** MX: GS1 México barcodes; Mercado Libre listing-quality guidance; Amazon México detail pages. International: Google Merchant Center; schema.org; shopping in AI search.
- **Metric of the week:** catalog completeness; feed error rate.
- **Lab:** build the Calzado Andar catalog (15 to 20 SKUs), import it into the dev store, and validate the feed.
- **Homework:** team catalog in its store, a feed export, and three optimized listings (store, marketplace, social).
- **Quiz:** "Following the course convention, a sandal in 8 sizes and 3 colors is..." A) 24 SKUs, 1 product ✔ B) 1 SKU, 24 products C) 11 SKUs, 3 products D) 24 SKUs, 24 products.

### S7 · Experiencia de compra: navegación, ficha de producto y checkout / Shopping experience: navigation, product page and checkout
- **Original items:** 3.1, 3.2.
- **Mental model:** each step answers the buyer's current question and removes one reason to doubt; mobile is the default; accessibility and speed are part of UX. **Current instance:** WCAG 2.2 AA checks with WAVE, and Core Web Vitals in PageSpeed Insights, on a Mexican store.
- **Topics:**
  1. Navigation, search and filters.
  2. Product page anatomy: images, total price, delivery promise by CP, returns, reviews, size guide, MSI/OXXO/SPEI visible early.
  3. Checkout: guest checkout, Mexican address form (CP → colonia), error messages, total-cost transparency.
  4. Trust: contact data, policies, genuine reviews.
  5. Accessibility: contrast, labels, focus order, alt text, target size.
  6. Performance: LCP, INP, CLS.
- **Objectives:**
  - Audit a mobile store against 10 heuristics and rank 10 issues by severity and effort.
  - Wireframe a product page that includes every trust element.
  - Run WAVE and Lighthouse and explain three findings in business terms.
  - Specify a Mexican checkout address form.
- **Examples:** MX: product pages from Liverpool, Mercado Libre and a Tiendanube store compared. International: Baymard Institute's checkout research (documented average abandonment around 70%, verify the current figure); the European Accessibility Act (June 28, 2025).
- **Metric of the week:** mobile checkout completion rate.
- **Lab:** heuristic and accessibility audit of the Calzado Andar mock store, which has defects planted in it.
- **Homework:** store v1 (home, one collection, three product pages, checkout configured) plus a before/after self-audit.
- **Quiz:** "Which product-page element most reduces 'where is my order?' contacts?" A) More photos B) A delivery date promised by CP ✔ C) A countdown timer D) A chat bubble.

### S8 · Conversión y experimentos / Conversion and experimentation, closing with Parcial 1
- **Original items:** 3.3, 7.2 (diagnosis).
- **Mental model:** the funnel is a product of step rates, so fix the largest absolute leak first; an experiment is a hypothesis, a primary metric, guardrails and a sample size set in advance; persuasion informs, manipulation hides. **Current instance:** a free sample-size calculator and Microsoft Clarity recordings on the dev store.
- **Topics:**
  1. Funnel math by device and source.
  2. Qualitative evidence: recordings, heatmaps, on-site surveys.
  3. Writing and prioritizing hypotheses (ICE).
  4. A/B basics: randomization, sample size, significance, peeking, novelty effect.
  5. Levers (CTA, social proof, promotions, urgency) vs. dark patterns (fake scarcity, drip pricing, confirmshaming, sneaking items into the basket).
  6. Parcial 1 logistics.
- **Objectives:**
  - Compute step rates and absolute losses, and name the largest leak.
  - Write three hypotheses in the format "we saw X, we believe Y, we will know by Z".
  - Judge whether a test result is conclusive given its sample size and p-value.
  - Classify six tactics as persuasion or dark pattern, with the reason.
- **Examples:** MX: Hot Sale and Buen Fin promotions, and PROFECO's price monitoring during Buen Fin. International: Booking.com's experimentation culture; the FTC fake-reviews rule (Oct 21, 2024); Google Optimize's closure (Sept 30, 2023), where the tool disappeared and the method stayed.
- **Metric of the week:** step conversion rates; revenue per session.
- **Lab:** funnel diagnosis on Calzado Andar data (device × step), then a written A/B test spec.
- **Homework:** team CRO backlog (five prioritized hypotheses) and one full test spec.
- **Quiz:** "You check a test daily and see p = 0.04 on day 3. Best action?" A) Ship it B) Keep running to the planned sample size ✔ C) Restart with a new variant D) Lower the significance threshold.

### S9 · Medios de pago / Payments
- **Original items:** 4.1.
- **Mental model:** methods run on rails, and providers sell access to the rails; each method trades off cost, speed, reach, risk and reversibility; the payment mix follows the customer. **Current instance:** test-mode checkout with a card and an OXXO cash voucher through a Mexican PSP.
- **Topics:**
  1. The four-party card model (issuer, acquirer, network, gateway, PSP/aggregator); authorization, capture, settlement, refund.
  2. Mexican methods: debit and credit, MSI, SPEI with a reference per order, CoDi/DiMo (Circular 9/2026 standardization, verify), cash vouchers, wallets, BNPL.
  3. Cost and cash flow: discount rate, fixed fees, MSI surcharges, settlement times, reserves.
  4. Approval rate; soft vs. hard declines.
  5. Payment events (pending, approved, expired), webhooks and idempotency.
  6. International benchmarks: Pix, UPI, PSD2 strong customer authentication.
- **Code card:** a 10-line JSON payment notification (`"status": "pending"`, `"payment_method": "oxxo"`, `"external_reference": "AND-10452"`).
- **Objectives:**
  - Draw a card payment flow naming five actors.
  - Design a payment mix for a segment and justify at least three methods.
  - Compute the effective cost per order for three methods, including 6-month MSI.
  - Decide from a webhook payload whether an order can ship.
- **Examples:** MX: OXXO cash for underbanked buyers; SPEI with CLABE reference; Mercado Pago; Kueski Pay and Aplazo. International: Pix (Nov 2020), UPI, Klarna.
- **Metric of the week:** approval rate; payment cost as a percentage of GMV.
- **Lab:** configure test-mode payments in the dev store and run an approved, a declined and a pending transaction; fill in the fee model.
- **Homework:** team payment mix, fee and settlement model, and evidence of the three test transactions.
- **Quiz:** "A customer chose OXXO and received the voucher. When do you ship?" A) Immediately B) When the provider notifies the payment as approved ✔ C) When the customer sends a photo of the ticket D) After 72 hours.

### S10 · Seguridad, fraude y contracargos / Security, fraud and chargebacks
- **Original items:** 4.2 (security), 4.3.
- **Mental model:** hold less (scope), verify more (authentication), price the risk (fraud loss vs. false declines), and defend with evidence. **Current instance:** PCI DSS v4.0.1 and EMV 3-D Secure 2.
- **Topics:**
  1. TLS; hashing vs. encryption vs. tokenization.
  2. PCI scope: hosted fields or redirect, never storing the CVV, scripts on payment pages.
  3. Authentication: 3DS2, MFA, passkeys, account takeover.
  4. Fraud patterns: card testing, stolen cards, friendly fraud, triangulation, fake SPEI receipts (checked through Banxico's CEP), refund abuse, phishing aimed at sellers.
  5. Rules, scores, manual review; fraud rate, chargeback ratio, false-decline rate.
  6. Chargeback lifecycle and the evidence pack.
- **Objectives:**
  - Explain how tokenization shrinks PCI scope.
  - Write five risk rules and measure their effect on a labeled dataset (fraud caught vs. good orders blocked).
  - Assemble a chargeback evidence pack for an "item not received" dispute.
  - Compute the chargeback ratio and compare it with the provider's threshold.
- **Examples:** MX: fake SPEI screenshots in marketplace and social sales. International: the 2018 British Airways card-skimming breach (UK ICO fine of GBP 20 million, 2020); the retirement of 3DS 1.0 (2022).
- **Metric of the week:** chargeback ratio; false-decline rate.
- **Lab:** rules lab on 500 labeled Calzado Andar orders.
- **Homework:** team risk policy covering rules, review criteria, chargeback kit, and staff account security (MFA, roles).
- **Quiz:** "Which data must never be stored after authorization?" A) Last four digits B) CVV/CVC ✔ C) Expiry date D) Cardholder name.

### S11 · Cumplimiento y ética: consumidor, datos personales y propiedad intelectual / Compliance and ethics: consumers, personal data and IP
- **Original items:** 8.1, 8.2, 4.2 (privacy).
- **Mental model:** obligations follow the journey. Before the purchase: information and advertising. At the purchase: total price, terms, consent. After it: delivery, warranty, returns, data rights. The frame works in any jurisdiction. **Current instance:** LFPC Art. 76 Bis as reformed Dec 12, 2025, and the LFPDPPP of March 20, 2025, supervised by SABG.
- **Topics:**
  1. Consumer law: LFPC e-commerce duties, advertising and promotions, warranties, recurring charges and cancellation (Dec 2025 reform); PROFECO tools (Concilianet); NMX-COE-001-SCFI-2018 and the 2021 Code of Ethics.
  2. Personal data: privacy notice, purposes that need consent, ARCO rights, cookies and tracking, disclosure of automated processing.
  3. IP: trademark registration at IMPI, copyright on photos and texts, counterfeits and marketplace brand protection.
  4. Dark patterns and honest design (follows from S8).
  5. AI: disclosure of AI-generated content and reviews; the EU AI Act as an international benchmark.
  6. International frame: GDPR, the EU 14-day withdrawal right, DSA, FTC.
- **Objectives:**
  - Audit a store against a 20-item checklist and assign each finding to an authority.
  - Draft a privacy notice that matches the store's real data flows.
  - Identify three dark patterns on real sites and rewrite them compliantly.
  - Route five complaint scenarios to the right authority.
- **Examples:** MX: PROFECO's Buen Fin monitoring; the move from INAI to SABG; the LFPC reform on subscriptions. Correct the NOM-247-SE-2021 misattribution here (it covers real estate). International: FTC v. Amazon on Prime cancellation (settled September 2025, verify amount); the EU withdrawal right.
- **Metric of the week:** compliance checklist score.
- **Lab:** compliance audit of the Calzado Andar mock store, which has planted issues.
- **Homework:** legal pack: privacy notice (full and short versions), terms, returns and warranty policy, cookie and tracking inventory, IP check. This is an academic exercise, not legal advice.
- **Quiz:** "A customer asks you to delete their data. Which right, and which authority?" A) ARCO cancellation; SABG ✔ B) Revocation; PROFECO C) ARCO cancellation; INAI D) Opposition; SAT.

### S12 · Pedidos, inventario e integraciones: una orden, cinco sistemas / Orders, inventory and integrations: one order, five systems
- **Original items:** 5.1, 2.2 (inventory), 2.3 (integration practice), 8.3.
- **Mental model:** the order is a state machine; each data entity has one system of record; events move state between systems; available-to-promise = on hand − committed − safety stock. **Current instance:** an `orders/create` webhook captured at webhook.site from the dev store, and a CFDI 4.0 issued through a PAC.
- **Topics:**
  1. Order states (created, paid, invoiced, picked, packed, shipped, delivered, returned, refunded, cancelled) and the system that owns each.
  2. Systems: storefront, OMS, ERP, WMS, CRM, PSP, carrier, PAC.
  3. Integration patterns: API, webhook, file, iPaaS; retries, idempotency, reconciliation.
  4. Inventory: ATP, safety stock, multichannel sync, overselling.
  5. Order-to-cash: CFDI 4.0 (mandatory since April 1, 2023), invoicing on request vs. factura global, matching the customer's Constancia de Situación Fiscal, cancellations, payment complement.
  6. Platform tax data flows (withholdings; CFF Art. 30-B, verify).
- **Code card:** a 12-line JSON order payload (id, channel, line items with SKU, payment status, shipping CP, `requires_invoice: true`).
- **Objectives:**
  - Draw an order state diagram with at least eight states and their owning systems.
  - Build an integration map that marks the system of record for each entity.
  - Compute ATP and decide which channel to throttle.
  - Specify the CFDI data to capture at checkout and when the invoice is issued.
- **Examples:** MX: overselling during Hot Sale when Mercado Libre and the own store share stock. International: Target Canada (2013-2015), undone in part by bad product and inventory data.
- **Metric of the week:** oversell rate; order cycle time.
- **Lab:** trace a Calzado Andar order across the systems, capture a test webhook, find three failure points, and run the ATP exercise.
- **Homework:** team order-to-cash map and integration plan, including the CFDI process and a reconciliation routine.
- **Quiz:** "The same order webhook arrives twice. What prevents a double shipment?" A) A faster server B) Checking whether that order ID was already processed ✔ C) Turning webhooks off D) An email confirmation.

### S13 · Fulfillment, última milla y logística inversa / Fulfillment, last mile and reverse logistics, closing with Parcial 2
- **Original items:** 5.2, 5.3.
- **Mental model:** cost-to-serve vs. delivery promise; choose the model by volume, SKU count and channel; returns are a designed flow (policy → reason codes → disposition → refund). **Current instance:** Mercado Libre Full vs. own warehouse plus a shipping aggregator, and the courier import rate for cross-border goods.
- **Topics:**
  1. Fulfillment models: in-house, 3PL, marketplace fulfillment, dropshipping, cross-border landed cost (33.5% courier rate since Aug 15, 2025; 2026 tariffs).
  2. Pick, pack, ship: packaging, dimensional weight, SLAs.
  3. Carriers, aggregators, zones, pickup points, tracking.
  4. Returns and reverse logistics: refunds by payment method, warranty.
  5. Peak operations and capacity planning.
  6. Parcial 2 logistics.
- **Objectives:**
  - Compute cost per order for two models at two volumes.
  - Compute dimensional weight and choose a box.
  - Build a shipping matrix by zone with a delivery promise.
  - Design a returns flow consistent with the S11 policy.
  - Compute the landed cost of a cross-border SKU and compare it with local sourcing.
- **Examples:** MX: Mercado Libre Full, 99minutos, Envia.com and Skydropx, and Temu/Shein under the new courier rate. International: Zappos free returns; Amazon FBA.
- **Metric of the week:** on-time delivery; cost per order; return rate.
- **Lab:** fulfillment decision and shipping matrix from Calzado Andar's destination data, plus a returns flow for size-related returns.
- **Homework:** team fulfillment and returns plan, plus a peak-season capacity plan.
- **Quiz:** "Box 40×30×20 cm, divisor 5,000, actual weight 2 kg. Billable weight?" A) 2 kg B) 4.8 kg ✔ C) 6.8 kg D) 2.4 kg.

### S14 · Analítica y medición / Analytics and measurement
- **Original items:** 7.1, 7.2 (instrumentation), 7.3.
- **Mental model:** question → KPI → event → parameter; the KPI tree; consent and data quality set the limits of what you can know; a dashboard exists to trigger a decision. **Current instance:** GA4 ecommerce events and funnel exploration, and a Looker Studio dashboard.
- **Topics:**
  1. KPI tree: revenue, conversion, AOV, contribution margin after marketing, CAC, ROAS, MER, repeat rate.
  2. Event-based analytics: events, parameters, users, sessions; the recommended ecommerce events.
  3. GA4 in practice: reports vs. explorations, funnel exploration, key events, DebugView.
  4. Data quality: consent mode, ad blockers, duplicate purchases, cross-domain checkout, gaps in marketplace data.
  5. Dashboards and the WBR: from chart to decision memo.
- **Code card:** a 10-line `gtag('event', 'purchase', {...})` with transaction_id, value, currency "MXN" and items.
- **Objectives:**
  - Write a measurement plan for five business questions.
  - Verify the ecommerce events on the dev store with DebugView.
  - Build a one-page dashboard with six KPIs, targets and owners.
  - Write a 200-word WBR memo that ends in one decision.
- **Examples:** International: the GA4 demo account (Google Merchandise Store); Universal Analytics' shutdown (July 1, 2023); "conversions" renamed "key events" (March 2024). MX: analyzing a Hot Sale traffic spike; marketplace seller dashboards vs. GA4.
- **Metric of the week:** the share of orders with an attributed source; GA4 vs. platform order-count reconciliation.
- **Lab:** GA4 demo funnel exploration, then a Looker Studio dashboard built from the Calzado Andar CSVs, which contain a planted duplication.
- **Homework:** team measurement plan, GA4 configured, dashboard v1 and the first WBR memo.
- **Quiz:** "Contribution margin before marketing is 30% of revenue and a campaign has ROAS 3.0. Is it profitable?" A) Yes B) No, break-even ROAS is 3.33 ✔ C) Yes, ROAS > 1 D) Cannot tell.

### S15 · Adquisición: búsqueda, pauta, creadores y descubrimiento con IA / Acquisition: search, paid media, creators and AI discovery
- **Original items:** 6.1, 6.2 (creators, UGC).
- **Mental model:** capturing demand (search, marketplaces) vs. creating it (social, creators, content); spend is bounded by the CAC ceiling; attribution is an estimate and incrementality is the test. **Current instance:** shopping ads fed by the S6 feed, and Google AI Mode in Spanish (since September 2025) as a new discovery surface.
- **Topics:**
  1. SEO (technical, content, product data) and AI answers.
  2. Paid search and shopping; retail media (Mercado Ads, Amazon Ads).
  3. Paid social, creators, affiliates and UGC, with disclosure.
  4. UTM taxonomy, attribution models, signal loss, server-side conversions, holdout tests.
  5. Budget allocation and the seasonal calendar.
  6. Trend radar on agentic commerce: OpenAI's Instant Checkout (built on the Agentic Commerce Protocol, launched September 2025, retired March 2026, verify) and Google's Universal Commerce Protocol (January 2026), evaluated with RADAR.
- **Objectives:**
  - Build a 30-day acquisition plan whose budget split is justified by the CAC ceiling.
  - Define a UTM taxonomy and tag ten links consistently.
  - Compare last-click and data-driven attribution for a dataset and explain the gap.
  - Write a creator brief that includes disclosure.
  - Produce a RADAR memo with a wait/pilot/adopt verdict on one agentic-commerce option.
- **Examples:** MX: a Buen Fin plan; TikTok Shop creators; Mercado Ads. International: Apple ATT (2021); the Privacy Sandbox retirement (2025); the rise and retreat of Instant Checkout; UCP.
- **Metric of the week:** CAC; ROAS vs. break-even ROAS; share of new customers.
- **Lab:** Buen Fin acquisition plan for Calzado Andar, plus a RADAR evaluation of agentic checkout.
- **Homework:** team 30-day plan, UTM sheet, creator brief and a RADAR memo on one emerging tool.
- **Quiz:** "Which is demand capture rather than demand creation?" A) A TikTok creator video B) A search ad on the brand's own name ✔ C) An Instagram reel D) A podcast sponsorship.

### S16 · Retención, relación con el cliente y comercio conversacional / Retention, customer relationships and conversational commerce, closing with the project
- **Original items:** 6.3, 1.1 (conversational), 7.1 (LTV).
- **Mental model:** customer value = margin × repeat purchases over time, read as cohort curves; the right message at the right moment, with consent; loyalty is earned by operations before points. **Current instance:** WhatsApp Business Platform flows (per-message pricing since July 1, 2025) and an email-flow tool.
- **Topics:**
  1. CRM data and RFM segmentation.
  2. Lifecycle flows (welcome, abandoned checkout, post-purchase, review request, win-back), channel choice, consent and opt-out.
  3. Service and reputation: SLAs, review replies, PROFECO complaints.
  4. Loyalty, subscriptions (Dec 2025 LFPC reform: clear disclosure of recurring charges and cancellation) and referrals.
  5. Cohorts, margin-based LTV, LTV:CAC.
  6. Project delivery logistics.
- **Objectives:**
  - Segment customers with RFM and choose an action per segment.
  - Design three flows, each with trigger, channel, message, KPI and consent basis.
  - Build a cohort table and compute the 6-month margin LTV.
  - Judge whether the current CAC is sustainable.
- **Examples:** MX: WhatsApp as the default service channel; Mercado Libre's Meli+ membership (verify current terms). International: Amazon Prime; Chewy Autoship.
- **Metric of the week:** repeat purchase rate; 6-month margin LTV; LTV:CAC.
- **Lab:** RFM and cohort analysis on 18 months of Calzado Andar orders; flow design.
- **Homework:** the final project delivery (Section 4).
- **Quiz:** "Margin per order $250; cumulative orders per customer at 6 months 1.4. What is the 6-month margin LTV?" A) $250 B) $350 ✔ C) $1,400 D) $175.

### S17 · Examen final / Final exam
- A short deck in the style of COM102's w17: course map review, exam rules, a solved sample item. The hour goes to questions and the exam.

---

## 4. Assessment plan and the running project/case

### Weights
The plan keeps the house structure of five components at 20% each, so covers and grading tables match the other courses. Each component is redesigned to mirror real work.

| Component | Week | What it is | Real-work equivalent | Weight |
|---|---|---|---|---|
| **Tareas (Playbook artifacts)** | S1-S15 | One team artifact per week (the homework above), graded on a 3-criterion rubric: correct concept, evidence, explicit decision. Lowest one dropped. Each student keeps an individual contribution log. | A weekly deliverable to a manager | 20% |
| **Parcial 1** | End of S8 | **Store diagnosis memo**, individual and in class. Students get a store pack (screenshots, funnel table, fee sheet, unit economics) and write a one-page memo: diagnosis, three prioritized fixes with expected impact, and one A/B test spec. Plus 10 concept items. | A "look at this store and tell me what to fix" request | 20% |
| **Parcial 2** | End of S13 | **Incident triage**, individual. A Buen Fin-style incident pack: spike in declines, oversold SKUs, chargebacks, carrier delay, fake SPEI receipts, a PROFECO complaint. Students produce a triage table (severity, owner, action, customer message) and an impact calculation. Plus 10 concept items. | A peak-day war room | 20% |
| **Proyecto** | S16 | **Launch-readiness review + QBR**: the store working in test mode, the complete Playbook, the dashboard and a 30-day growth plan. 12-minute presentation, 8-minute defense. Rubric: business logic 25, store and operations readiness 25, data and measurement 20, compliance 15, communication 15. Individual grades adjust (±) through peer evaluation and the defense. | A launch review with leadership | 20% |
| **Examen final** | S17 | **"Tus primeros 30 días / Your first 30 days"**, individual, with a data pack. A) KPIs, unit economics, funnel and cohort analysis. B) A prioritized 30-day plan memo. C) A **RADAR evaluation of an unseen tool or trend** (vendor one-pager plus evidence). D) Concepts. | Onboarding into a new job | 20% |

**AI-use rule (stated in S1, applied in every assessment):** use AI as you would at work. Disclose it, verify it, and be able to defend every number and sentence. Data packs are seeded per team or per student, so answers cannot be copied across.

*If the program sheet allows changing weights, the practice-first option is to move 10 points from the final exam to the project (30/20/20/10/20). The default keeps the house standard.*

### The running case: Calzado Andar (fictional)
- **Profile:** a D2C footwear brand from León, Guanajuato. About 40 SKUs (sizes 22-29 cm × colors, plus a care-kit add-on). It sells through its own store, Mercado Libre, Amazon México and TikTok Shop, and ships nationwide from León.
- **Data pack (built once, re-seeded each term):** products.csv, orders.csv (18 months, with channel, payment method, CP, shipping cost, return and chargeback flags), funnel_daily.csv (by device and source), ad_spend.csv, returns.csv, a dated fee sheet, and a mock store.
- **Planted problems, one per block, so labs have something real to find:** a mobile checkout leak, an oversold SKU during Buen Fin, a card-testing burst, size-driven returns, untagged campaigns, a non-compliant privacy notice, and duplicate purchase events.

### The team project: *Playbook de operación*
- **Route A:** a real micro or small business, with a signed consent letter from the owner. Students never take money themselves; any live sale runs through the business's own accounts and RFC.
- **Route B:** the team's own product, run in test mode.
- **Chapters are the weekly homework:**

| Week | Chapter |
|---|---|
| 1 | System map |
| 2 | Channel strategy |
| 3 | Value proposition and unit economics |
| 4 | Evidence report |
| 5 | Platform decision |
| 6 | Catalog |
| 7 | Store v1 and audit |
| 8 | CRO backlog |
| 9 | Payments |
| 10 | Risk policy |
| 11 | Legal pack |
| 12 | Order-to-cash |
| 13 | Fulfillment and returns |
| 14 | Measurement and dashboard |
| 15 | Acquisition plan |
| 16 | Retention flows and QBR |

---

## 5. Current-stack annex, as of October 2026

Concepts are fixed; this annex is reviewed every term. Slides cite instances as "as of <month year>". Each row is written as *concept: current instances* (status note) → what to re-check.

### 5.1 Platforms, channels and discovery

**Hosted SaaS storefront:** Shopify, Tiendanube, Wix, BigCommerce.
- Status: Shopify Payments has been available in Mexico since 2025 (verify).
- Re-check: plan prices, transaction fees, Mexican payment and CFDI apps, free dev/trial terms for classroom use.

**Open source:** WooCommerce, Magento Open Source / Adobe Commerce.
- Status: Magento 1 reached end of life June 30, 2020.
- Re-check: hosting cost, plugins for local PSPs.

**Enterprise / composable:** VTEX, Salesforce Commerce Cloud, commercetools.
- Status: MACH Alliance (2020).
- Re-check: used only as examples.

**Marketplaces (MX):** Mercado Libre, Amazon México, Walmart México, Liverpool, TikTok Shop (Feb 2025), Temu, Shein.
- Status: Mercado Shops closed Dec 31, 2025.
- Re-check: commission tables, free-shipping thresholds, fulfillment programs, seller requirements.

**Social and conversational:** Instagram, Facebook, TikTok, YouTube, WhatsApp Business app and Platform.
- Status: WhatsApp moved to per-message pricing July 1, 2025.
- Re-check: in-app checkout availability in Mexico, message prices.

**AI discovery and agentic commerce:** Google AI Overviews and AI Mode (Spanish since September 2025), ChatGPT shopping; protocols ACP (OpenAI and Stripe, September 2025), AP2 (Google, September 2025), UCP (Google, January 2026); card-network agent programs (2025, verify).
- Status: Instant Checkout retired March 2026 (verify).
- Re-check: availability in Mexico, merchant onboarding, which protocols the teams' platforms support.

### 5.2 Payments and risk

**Rails:** cards (Visa, Mastercard, Amex, Carnet), SPEI (since 2004), CoDi (2019), DiMo (2023), cash networks (OXXO and others).
- Status: Banxico Circular 9/2026 sets a Dec 14, 2026 deadline for standardized transfers in bank apps (verify).
- Re-check: new rules and adoption.

**PSPs and gateways:** Mercado Pago, Stripe, Conekta, Openpay (BBVA), Clip, PayPal, Getnet, platform-native payments.
- Status: Mercado Pago's banking license application was still in process (verify).
- Re-check: fees, settlement times, supported methods, MSI terms.

**Installments and BNPL:** MSI on cards, Kueski Pay, Aplazo, marketplace credit.
- Re-check: fees, cost disclosures (CONDUSEF).

**Wallets:** Apple Pay, Google Pay, Mercado Pago, PayPal.
- Re-check: Mexican acceptance.

**Security standards:** PCI DSS v4.0.1, EMV 3DS 2.x, FIDO passkeys.
- Status: PCI DSS v3.2.1 retired Mar 31, 2024; the future-dated requirements became mandatory Mar 31, 2025.
- Re-check: new versions, eligibility for the simplest self-assessment questionnaire (SAQ A).

**Dispute monitoring:** card-network programs (e.g., Visa VAMP, verify).
- Re-check: thresholds and fees.

### 5.3 Operations and back office

**Fulfillment:** Mercado Envíos (Full, Flex), Logística de Amazon (FBA), 3PLs.
- Re-check: fees, inbound rules.

**Carriers and aggregators:** Estafeta, DHL Express, FedEx, Paquetexpress, 99minutos, J&T Express, Envia.com, Skydropx.
- Re-check: rates and coverage.

**ERP, accounting and integration:** Odoo, SAP Business One, NetSuite, Dynamics 365 BC, CONTPAQi, Aspel; PACs for CFDI; Zapier, Make, n8n; webhook.site for class.
- Status: CFDI 4.0 mandatory since April 1, 2023.
- Re-check: CFDI complements, Carta Porte, PAC list.

**Cross-border trade:** courier regime (RGCE) and tariff schedule.
- Status: 19% from January 2025, then 33.5% from Aug 15, 2025 for non-FTA courier imports (verify thresholds); 5% to 50% tariffs on 1,463 lines from non-FTA countries since Jan 1, 2026.
- Re-check: current rates, thresholds for USMCA origins.

### 5.4 Analytics, marketing and CRM

**Event analytics:** GA4, with BigQuery export.
- Status: Universal Analytics stopped processing July 1, 2023; "key events" naming since March 2024.
- Re-check: interface changes, demo account availability.

**Tags and server-side:** Google Tag Manager (web and server), Meta Conversions API, Google enhanced conversions, Consent Mode v2 (required for EEA traffic since March 2024).
- Re-check: consent requirements.

**Dashboards:** Looker Studio, Google Sheets, Excel.

**Behavior and experimentation:** Microsoft Clarity, Hotjar, VWO, Optimizely, AB Tasty.
- Status: Google Optimize closed Sept 30, 2023.
- Re-check: free tiers.

**Speed and accessibility:** PageSpeed Insights, Lighthouse, CrUX, WAVE, axe.
- Status: INP replaced FID in March 2024; WCAG 2.2 (October 2023).
- Re-check: status of WCAG 3 (verify).

**Advertising:** Google Ads (Search, Shopping, Performance Max), Meta Ads, TikTok Ads, Mercado Ads, Amazon Ads, Merchant Center, Search Console.
- Re-check: campaign-type names, feed specs.

**CRM and messaging:** HubSpot, Klaviyo, Mailchimp, Brevo; WhatsApp Platform through business solution providers (BSPs).
- Re-check: message pricing, consent features.

**Privacy signals:** Apple ATT (April 2021); Chrome keeps third-party cookies; Privacy Sandbox APIs retired October 2025.
- Re-check: browser and operating-system changes.

**Market data:** AMVO Estudio de Venta Online (published around March); INEGI ENDUTIH; event calendar (Hot Sale 2026: May 25 to June 2; Buen Fin 2026: Nov 13 to 17).
- Re-check: new figures and next-term dates.

### 5.5 Regulators and laws

**Mexico**

**PROFECO: consumer protection.**
- Instruments: LFPC, Art. 76 Bis (reform DOF Dec 12, 2025); Concilianet; Buen Fin monitoring.
- Re-check: new reforms; whether the mandatory e-commerce NOM announced in 2021 has been published (verify).

**Secretaría de Economía: standards.**
- Instruments: NMX-COE-001-SCFI-2018 (voluntary); Código de Ética (DOF Feb 26, 2021); labeling NOMs (e.g., NOM-050-SCFI-2004).
- Note: NOM-247-SE-2021 covers residential real estate only.
- Re-check: new NOMs and NMX.

**SABG: personal data held by private parties.**
- Instruments: LFPDPPP (DOF March 20, 2025). INAI no longer exists.
- Re-check: publication of the reglamento, guidelines, sanctions.

**SAT: tax and invoicing.**
- Instruments: CFDI 4.0; platform regime (LISR 113-A, LIVA 18-J, since June 2020); CFF Art. 30-B (April 1, 2026, verify); RESICO.
- Re-check: the Miscelánea Fiscal every January; withholding rates.

**Banxico: payment systems.**
- Instruments: SPEI rules, CoDi, DiMo, CEP; Circular 9/2026 (verify).
- Re-check: deadlines and new features.

**CNBV and CONDUSEF: fintech and financial consumers.**
- Instruments: Ley Fintech (2018).
- Re-check: licenses granted to payment players.

**IMPI and INDAUTOR: intellectual property.**
- Instruments: LFPPI (in force Nov 5, 2020); LFDA.
- Re-check: marketplace enforcement practice.

**Comisión Nacional Antimonopolio (replaced COFECE): competition, including digital markets.**
- Instruments: LFCE reform (July 2025, verify date).
- Re-check: investigations into marketplaces or payments.

**ANAM and SHCP: customs and tariffs.**
- Instruments: RGCE courier rule; tariff decree of January 2026.
- Re-check: rates.

**International**
- **OECD** Recommendation on Consumer Protection in E-commerce (2016).
- **UNCITRAL** Model Law on Electronic Commerce (1996).
- **EU:** GDPR (2018); 14-day withdrawal right; DSA (all platforms since Feb 17, 2024); DMA; AI Act (in force Aug 1, 2024; GPAI duties Aug 2, 2025; Annex III high-risk moved to Dec 2, 2027, verify); European Accessibility Act (June 28, 2025); PSD2/SCA (PSD3/PSR status, verify).
- **US FTC:** reviews and testimonials rule (Oct 21, 2024); Endorsement Guides (2023); its click-to-cancel rule was vacated by a federal appeals court in July 2025.
- **Brazil:** LGPD and Pix. **India:** UPI.
- **Standards bodies:** PCI SSC, EMVCo, W3C, FIDO Alliance, GS1, schema.org.

### 5.6 Retirement log: obsolete instance → concept that stays

| Was | What happened | Concept kept | Session |
|---|---|---|---|
| Universal Analytics | Stopped July 1, 2023 | Event-based measurement | S14 |
| Google Optimize | Closed Sept 30, 2023 | Experiment method | S8 |
| Magento 1 | End of life June 30, 2020 | Platform lifecycle, migration cost | S5 |
| Mercado Shops | Closed Dec 31, 2025 | Platform risk, exit plan | S2, S5 |
| Facebook Live Shopping | Ended Oct 1, 2022 | Social feature churn; own the relationship | S2 |
| 3-D Secure 1.0 | Retired October 2022 | Risk-based authentication | S10 |
| PCI DSS 3.2.1 | Retired Mar 31, 2024 | Scope reduction | S10 |
| FID metric | Replaced by INP, March 2024 | Responsiveness | S7 |
| INAI; LFPDPPP 2010 | Extinct; repealed March 20, 2025 | Privacy notice, consent, ARCO | S11 |
| "Cookieless Chrome" | Abandoned; Privacy Sandbox retired October 2025 | Consent and first-party data | S15 |
| ChatGPT Instant Checkout | Launched September 2025, retired March 2026 (verify) | Evaluate agentic commerce with RADAR | S15 |
| Courier dropshipping from Asia | 33.5% rate (2025) and 2026 tariffs | Landed cost | S13 |

### 5.7 Review protocol, every term
1. **Two weeks before classes:** walk every "Re-check" item using official sources first (DOF, regulator sites, vendor docs), and log the date checked.
2. **Update the dated fee sheet, the annex and the Calzado Andar seed;** run every lab once on the new data.
3. **Move anything retired to the log, with its replacement concept.** Slides swap the instance; sessions do not change.
4. **Admit new tools or trends only after a written RADAR evaluation,** and add at most one new instance per session per term.
5. **Calendar checks:** January (Miscelánea Fiscal, tariffs), March (AMVO study), mid-year (Banxico, PROFECO reforms), and before Hot Sale and Buen Fin (dates and rules).

---

### Repo fit (for building the decks)
- **Path:** `ppts/commerce/fundamentos-del-comercio-electronico/{es,en}/` with `w01.0`, `w01` … `w17`.
- **Palette:** `meta.language: commerce`. This palette already exists in `ppts/kit/tokens.py`, and its comment anticipates a few JSON code cards (generic scanner).
- **Covers and slides:** covers say "Sesión N de 17"; S8, S13 and S16 teach their full topic and close with exam or project logistics; no durations on slides; dates appear as "as of" and sources go in speaker notes.
- **Archetypes:** `concept` (mental model), `diagram` (flows, order states), `table` (control matrix, annex rows), `code` (JSON/UTM/gtag only), `pitfalls` (dark patterns, fraud), `quiz` + `trace` (worked numeric answers), `lab`, `homework`, `tiers` (RADAR).
- **Course code:** to be assigned.

### Sources checked for dated claims
- NOM-247-SE-2021 scope: [DOF](https://dof.gob.mx/nota_detalle_popup.php?codigo=5646251), [SE](https://platiica.economia.gob.mx/normalizacion/nom-247-se-2021/)
- NMX-COE-001-SCFI-2018: [DOF](https://www.dof.gob.mx/nota_detalle.php?codigo=5559015&fecha=30/04/2019); Código de Ética: [gob.mx](https://www.gob.mx/cms/uploads/attachment/file/621262/Acuerdo_por_el_que_se_emite_el_Codigo_de_Etica_en_materia_de_Comercio_Electronico.pdf)
- LFPDPPP 2025 and SABG: [IDC](https://idconline.mx/corporativo/2025/03/21/publican-nuevas-leyes-sobre-acceso-a-informacion-publica-y-proteccion-de-datos-personales), [Hogan Lovells](https://www.hlc.com/es/publications/mexicos-new-federal-data-protection-law-what-it-means-for-companies), [reglamento pending](https://sharkit.mx/nueva-lfpdppp-reglamento-pendiente/)
- LFPC reform Dec 2025: [Greenberg Traurig](https://www.gtlaw.com/en/insights/2025/12/reformas-a-la-ley-federal-de-proteccion-al-consumidor)
- DiMo/CoDi and Circular 9/2026: [Infobae](https://www.infobae.com/mexico/2023/08/08/pago-digital-en-mexico-cuales-son-y-de-que-trata-spei-codi-y-dimo/), [El Imparcial](https://www.elimparcial.com/dinero/2026/06/19/banxico-reforma-las-reglas-del-spei-para-obligar-a-los-bancos-a-unificar-el-diseno-de-sus-aplicaciones-moviles-pero-como-funcionara-este-nuevo-sistema-simplificado-y-que-cambia-al-hacer-transferencias/)
- Courier rate and 2026 tariffs: [Merca2.0](https://www.merca20.com/mexico-impone-aranceles-de-33-5-a-paquetes-de-temu-y-shein/), [El Imparcial](https://www.elimparcial.com/dinero/2025/12/30/a-partir-del-1-de-enero-del-2026-mexico-aplicara-aranceles-a-china-de-hasta-el-50/)
- SAT Art. 30-B: [Sovos](https://sovos.com/mx/blog/iva/sat-acceso-informacion-plataformas-digitales/)
- TikTok Shop MX: [TikTok Newsroom](https://newsroom.tiktok.com/es-latam/tiktok-shop-evento-cdmx); Mercado Shops: [Enviame](https://enviame.io/mercado-shops/); Shopify Payments MX: [Doose Studio](https://doosestudio.com/en/blogs/ecommerce/shopify-payments-ya-esta-disponible-en-mexico)
- Agentic commerce: [CNBC on UCP](https://www.cnbc.com/2026/01/11/google-launches-universal-commerce-protocol-bets-on-ai-powered-retail.html), [Instant Checkout retired](https://www.agenticcommercefeed.com/blog/2026-03-16-openai-kills-instant-checkout)
- Privacy Sandbox: [eMarketer](https://www.emarketer.com/content/google-s-privacy-sandbox-elimination-ends-quest-cookieless-chrome); Google AI Mode in Spanish: [Fast Company MX](https://fastcompany.mx/2025/09/23/modo-ia-de-google-disponible-en-espanol-para-region-latinoamerica/)
- WhatsApp pricing: [Meta docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- CNA replacing COFECE: [Proceso](https://www.proceso.com.mx/nacional/politica/2025/7/1/el-oficialismo-sepulta-definitivamente-la-cofece-crea-la-comision-nacional-antimonopolio-354051.html); Mercado Pago license: [El Universal](https://www.eluniversal.com.mx/cartera/bancos-digitales-aprietan-la-competencia-en-mexico-mercado-pago-solicita-licencia-bancaria-ante-la-cnbv/)
- AMVO 2026: [La Jornada](https://www.jornada.com.mx/noticia/2026/03/11/economia/comercio-electronico-no-se-detiene-amvo-ventas-en-linea-crecieron-19-en-2025); Hot Sale 2026: [AMVO](https://blog.amvo.org.mx/blog/confirmado-fechas-oficiales-y-datos-clave-del-hot-sale-2026); Buen Fin 2026: [calendariodemexico](https://calendariodemexico.com/buen-fin-2026-mexico-fechas-ofertas/)
- EU AI Act omnibus: [Orrick](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)