# Fundamentals of E-commerce

This course organizes concepts, implementation and evidence across 17 sessions. Each lab uses only the current and earlier session concepts.

## Assessment

| Component | Weight | Due |
|---|---:|---|
| Midterm 1 | 20 % | w08 |
| Midterm 2 | 20 % | w13 |
| Capstone project | 20 % | w16 |
| Final exam | 20 % | w17 |
| Homework and labs | 20 % | w01-w16 |

## Sessions

### 01. Digital commerce: models, channels and who controls what

- Business model: A model identifies who sells to whom. A channel identifies where the transaction is initiated.
- Channel control: Price, customer data, payment, delivery and support can belong to different participants. Assign each responsibility before choosing a channel.
- Order flow: Trace discovery, trust, payment, delivery and resolution for one order. A handoff needs an owner and evidence.

Lab: Ten-business map: teams place ten business cards on a model-by-channel grid and answer the five control questions for each. They close by proposing two channel positions for Molienda and writing, in one line each, what control each one costs.

### 02. Customer, value proposition and evidence

- Customer evidence: Describe past customer behavior before proposing a solution. Distinguish an observation from an assumption.
- Value proposition: Link a customer need to a specific benefit and a reason to trust the seller. Test the uncertain part first.
- Validation: A statement of interest, an observed action and a payment represent different commitments. Define the decision threshold before collecting evidence.

Lab: Interview clinic in pairs: turn bad questions into good ones and swap with another pair to flag the leading ones. Then design a one-week test of the Molienda subscription with the threshold set in advance, for example at least 20 refundable deposits from 400 visits, and write what you would do if it is not met.

### 03. The economics of an order

- Revenue basis: Separate the customer total from revenue net of taxes. The exercise supplies tax assumptions for each product.
- Margin and markup: Gross margin divides gross profit by revenue. Markup divides the same gross profit by cost. Their denominators differ.
- Order contribution: Subtract product cost and all variable order costs from net revenue. A positive gross margin can coexist with a negative order contribution.

Lab: In a spreadsheet, the P&L of three Molienda baskets: one 250 g bag, order #1001 (two 250 g bags at $289 and one grinder at $1,490, total $2,068 MXN) and one subscription month. The commission, payment and shipping lines are flagged to be filled in w04, w07 and w10, using today's illustrative values for now. Find the basket that loses money, propose one fix (threshold, bundle or price) and test it with numbers.

### 04. Platforms: rent, buy or build

- Total ownership cost: Include subscription, hosting, integration, support, updates and exit costs over a defined period. A low entry price can hide later work.
- Platform control: Compare control over data, prices, policies and customer relationships. Renting software and renting an audience solve different needs.
- Integration and exit: Define how product, order and customer records enter and leave the platform. Test an export before depending on a vendor.

Lab: Three paths for Molienda: with an illustrative fee table, compute the monthly cost at 50, 300 and 2,000 orders for marketplace only, a SaaS store and open source. Chart the crossover, fill in the commission line of order #1001's P&L and complete the tool card for the chosen option, with a 90-day exit plan.

### 05. Catalog and product data

- Product and SKU: A product can have several sellable variants. Each SKU identifies a stockkeeping unit, while a bundle combines units.
- Attributes and taxonomy: Attributes describe the item. Categories organize discovery. Use consistent values so filters and comparisons work.
- Publishing product data: Keep one reviewed specification as the source for descriptions, images and feeds. Check every generated claim against that specification.

Lab: Build Molienda's catalog (three roasts, whole bean or ground, in 250 g or 1 kg, plus the grinder and the subscription) as a SKU table with a naming convention and sample GTINs; map one product to two channel taxonomies and fact-check, line by line, an AI-written description with three planted errors.

### 06. The shopping experience, the product page and the funnel

- Purchase uncertainty: A product page should explain the item, total price, delivery promise and resolution terms. The customer needs these details before payment.
- Funnel denominators: A step conversion uses entrants to that step as its denominator. Compare relative drop and absolute lost orders separately.
- Access and usability: Check keyboard operation, labels, readable text and error recovery. An automated check covers only part of the experience.

Lab: Take apart Molienda's mobile product page (a mock with planted defects) using the given funnel data: heuristic evaluation, an accessibility pass with a checker and the keyboard, and a written decision on which step to fix first and why.

### 07. Payments: how money moves

- Payment lifecycle: Authorization, capture, settlement and merchant payout are distinct events. Fulfillment should depend on the required confirmation state.
- Fees and timing: Compare a percentage fee, a fixed fee and the payout delay. Use the provider agreement and the exercise fee sheet.
- Payment evidence: A screenshot is a claim of payment. Reconcile the provider notification and the credited movement before releasing an order.

Lab: Molienda's payment mix: from a segment table (a young buyer without a credit card, an office buyer who needs an invoice, a grinder customer) and an illustrative fee table, choose methods, compute the weighted payment cost per order, fill in the payment line of order #1001, decide whether to offer MSI only on grinders and complete a tool card for one payment provider.

### 08. Checkout, trust and conversion optimization

- Checkout disclosure: Show the complete charge, delivery conditions and seller contact before the customer confirms. Explain errors without discarding valid input.
- Experiment design: Define random assignment, the primary metric and stopping rule before an A/B test. Estimate the data needed for the effect of interest.
- Trust and persuasion: Use truthful reviews, inventory and offers. A measured conversion gain must also preserve margin and customer outcomes.

Lab: Molienda's seven-step checkout, with about 6,000 sessions a month: redesign it, write two hypotheses and check with the sample-size table whether an A/B test is feasible. The expected finding is that only large effects are detectable, so a usability test comes first. A short lab because of the exam week.

### 09. Orders, inventory and risk

- Order states: Track payment and fulfillment separately. A refunded payment and a returned parcel describe different parts of the same order.
- Available inventory: Available stock equals on-hand stock minus reservations and safety stock. Delayed synchronization can expose the same stock in several channels.
- Duplicate events: Store a stable event identifier and handle a repeated notification without repeating its business effect. Confirm processing before acknowledging it.

Lab: The history of order #1001: a shuffled event log with a duplicate webhook and a stock conflict between the store and Mercado Libre. Rebuild the order's history in a trace table, find the oversell and decide what to do with three suspicious orders.

### 10. Fulfillment and the last mile

- Fulfillment flow: Receive, store, pick, pack and ship with a check at each handoff. A delivery promise depends on capacity and cutoff times.
- Billable weight: Compare physical weight with dimensional weight under the carrier agreement. The exercise supplies dimensions, divisor and rounding rules.
- Delivery recovery: Define who handles a failed delivery, damaged parcel and missing tracking update. Include these costs in the order calculation.

Lab: For Molienda: choose a fulfillment model at three volumes, compute the billable weight of three boxes, write delivery promises from Coatepec to Mexico City, Guadalajara, Monterrey and Mérida, carry shipping into order #1001's P&L and complete a tool card for one logistics provider.

### 11. Returns, after-sales and invoicing

- Returns operation: Separate the customer decision, return transport, inspection and refund. Record a reason that can improve the catalog or fulfillment process.
- Refund reconciliation: Reconcile the refunded amount with the original payment and order. A returned parcel alone does not prove that the money was refunded.
- Invoicing evidence: Link the invoice, order, payment and any refund document. Determine the applicable fiscal treatment from current rules and transaction facts.

Lab: Molienda's after-sales desk handles six cases: a damaged grinder, the wrong grind, a change of mind on day 3, an invoice requested a month later, a refund of an invoiced order and a review complaining of late delivery. For each: the customer's right, the action, the cost and the CFDI document.

### 12. Acquisition: reaching the right customer

- Acquisition channels: Separate channels controlled by the business, earned exposure and paid distribution. Record the audience and purpose of each campaign.
- CAC and ROAS: CAC divides acquisition spending by acquired customers. ROAS divides attributed revenue by advertising spending. Neither is contribution profit.
- Break-even advertising: With a contribution ratio of m before advertising, the simple break-even ROAS is 1/m. State the included costs and attribution assumptions.

Lab: Molienda's campaign table (Meta, Google, Mercado Ads and one creator): compute CAC, ROAS and break-even ROAS, reallocate the budget, tag three links and complete a tool card for one ad channel. It closes with a puzzle left open on purpose: Meta reports 40 purchases, analytics 25 and the store 32. Why? Answered in w13.

### 13. Measurement and decisions

- Metric definitions: State population, unit of observation, period and denominator. A session, customer, order and item are different units.
- Reconciliation: Compare order records, payment records and behavioral events by stable identifiers. Investigate missing and duplicated events before deciding.
- Attribution and cause: Attribution assigns credit under a rule. A holdout experiment can estimate incremental impact. Different questions require different evidence.

Lab: Explore the GA4 demo account (funnel and traffic acquisition by UTM). Write Molienda's measurement plan and build the reconciliation table that solves the w12 puzzle, including a duplicate purchase event planted in the data. A short lab because of the exam week.

### 14. Retention and customer value

- Cohort retention: Compare customers who began in the same period and have equal opportunity to return. A young cohort has less observation time.
- Customer contribution: Estimate value from contribution over observed or modeled purchases. Disclose the horizon, costs and uncertainty before comparing it with CAC.
- Lifecycle messages: Match each message to a customer need and an allowed contact purpose. Provide a working way to stop promotional messages.

Lab: From a 12-month export of Molienda orders (about 500 rows), build the cohort table, RFM segments and LTV. Then design, on paper, a subscription flow that complies with the law.

### 15. Law, privacy and ethics

- Consumer information: Map product information, complete price, contact and resolution terms to the point where the customer decides. Review the current applicable consumer law.
- Personal data: Define purpose, necessary data, access, retention and rights handling. In Mexico, check the current private-sector data-protection law and its competent authority.
- Law, policy and ethics: A platform rule and a legal obligation have different sources. Also evaluate harm to the customer, even when a pattern is technically allowed.

Lab: Molienda legal audit: fifteen screenshots (checkout, cookie banner, subscription flow, product page, privacy notice). Find the violations and deceptive patterns, rewrite each one and draft the elements of the privacy notice.

### 16. Evaluating the next tool

- System responsibilities: Assign a system of record for products, orders, inventory and customers. Define how changes cross each boundary.
- Tool evidence: Compare a vendor claim with a test in the relevant context. State integration cost, maintenance cost and an exit path.
- Reversible pilot: Define the hypothesis, metric, observation period and stop rule. Preserve the previous workflow until the new one meets the criteria.

Lab: Short lab: each team draws a trend card (checkout inside an assistant, live shopping, marketplace advertising, passkeys, social marketplaces) and produces a tool card and a pilot plan for Molienda. Project presentations follow.

### 17. Final assessment

- Integrated diagnosis: Explain a business outcome using the order calculation, funnel and operating evidence. Check that the proposed action addresses the diagnosed cause.
- Decision under uncertainty: Identify what the data supports and what remains unknown. Propose the next measurement when uncertainty changes the decision.
- Individual defense: Reproduce a calculation, explain a tradeoff and identify a limit without relying on a brand name. Every team member should understand the submitted work.

Lab: Practice round in pairs: eight items, two from each phase.

## Submission rules

Disclose assistance tools and keep reproducible evidence. Each member must explain the work. Each exam specifies the permitted materials.
