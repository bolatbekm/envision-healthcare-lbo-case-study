# Sources

Every figure used in this repo traces to one of the documents below. Pulled
2026-10-21. Envision Healthcare Corporation (NYSE: EVHC until 2018, CIK
**0001678531**) was a public company before its 2018 KKR buyout, filed a
Form 15-12B (SEC deregistration) immediately after the deal closed, and
had **no further SEC reporting obligation** afterward — similar to Red
Lobster's data shape, not Toys "R" Us's. Unlike Red Lobster, however, the
2023 Chapter 11 declaration here is extraordinarily detailed about the
post-LBO period, including two rounds of pre-bankruptcy "liability
management" transactions — so the post-2018 story is actually very well
documented, just not via continuous annual filings.

## 1. Pre-2018: a recently-merged, margin-collapsing company

**Source**: Envision Healthcare Corporation's FY2017 10-K, filed 2018-03-01
([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1678531/000167853118000033/evhc10k20171231.htm),
CIK 1678531). Saved at `data/raw/evhc_fy2017_10k.htm`.

- Envision Healthcare Corporation was formed by a **"merger of equals"**
  between Envision Healthcare Holdings, Inc. and AmSurg Corp. in December
  2016 (per the 2023 bankruptcy declaration, ¶26). This means FY2016 and
  earlier figures reported in the FY2017 10-K reflect a different
  corporate perimeter than FY2017 and are not cleanly comparable
  year-over-year.
- **FY2017 (first full year as the combined company)**: Net revenue
  **$7,819.3 million**, Operating income **$189.2 million** (a thin **2.4%**
  margin).
- The 10-K's own common-size (% of revenue) presentation shows operating
  margin falling sharply even before the sale process began: **24.1%
  (FY2015) → 10.6% (FY2016) → 2.4% (FY2017)** — though this comparison
  spans the 2016 merger, so part of the decline reflects a different,
  larger company, not pure like-for-like deterioration.
- The **Physician Services** segment specifically reported an operating
  **loss of $221.3 million** in FY2017 (vs. a $176.8M operating *gain* in
  FY2015), on $6,542.4M of segment revenue — a segment already in trouble
  before KKR bought the company.
- **Corporate prehistory** (2023 declaration, ¶29-31): the Physician
  Services business traces to EmCare, founded 1972; taken private by
  Clayton, Dubilier & Rice in 2011 for ~$3 billion (**Envision's first
  LBO** — it had been through this before); went public again in 2013 as
  Envision Healthcare; merged with AmSurg in 2016.

## 2. The 2018 KKR transaction

**Source**: Envision's DEFM14A merger proxy, filed 2018-08-13
([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001678531/000095012318008376/d608534ddefm14a.htm)).

- Merger consideration: **$46.00 per share, cash** — a 32% premium to the
  volume-weighted average share price since November 1, 2017.
- **Total transaction value: ~$9.9 billion** (widely reported, including
  assumption/repayment of existing debt).
- **KKR's equity commitment: $3.5 billion** ("an aggregate amount in cash
  equal to $3.5 billion," the proxy's own wording).
- **Debt financing commitments: up to $8.05 billion**, from a lender group
  including Credit Suisse, Citigroup, Morgan Stanley, Barclays, and
  Goldman Sachs (commitment letters are customarily sized with headroom
  above what's actually drawn at close).
- Fairness opinions delivered by three separate advisors: **J.P. Morgan
  Securities, Evercore, and Guggenheim Securities**.
- Deal closed **October 11, 2018**. Envision filed Form 15-12B
  (deregistration from SEC reporting) on **October 22, 2018** — eleven
  days later. On the closing date, Envision also issued **$1.225 billion**
  of Senior Notes (per the 2023 declaration, ¶76) — the one piece of the
  acquisition debt that was itself a registered/public instrument.

## 3. 2023: the bankruptcy, in detail

**Primary source**: *Declaration of Paul Keglevic, Chief Restructuring
Officer of Envision Healthcare Corporation, in Support of the Debtors'
Chapter 11 Petitions*, filed May 15, 2023, Case No. 23-90342 (CML), U.S.
Bankruptcy Court for the Southern District of Texas, Houston Division —
Document 2, 177 pages. Saved at
`data/raw/keglevic_first_day_declaration.pdf` (text extract:
`data/raw/keglevic_first_day_declaration.txt`). Paul Keglevic was Chief
Restructuring Officer at filing.

### What went wrong (¶-numbered references are to the declaration)

- **COVID-19 impact**: approximately **$1.1 billion** of lost revenue and
  **$415 million** of lost EBITDA in 2020; a further **$380 million**
  revenue impact in 2021.
- **A specific payor dispute** (the declaration doesn't name the payor in
  the passages extracted, but separate press reporting and the
  declaration's own later reference to "an arbitration case against
  United Healthcare" identify it as **UnitedHealthcare**): cumulative
  revenue impact **>$400 million**, via (a) unilaterally changing contract
  terms by ~$100M (2018), (b) extracting ~$100M in additional rate
  reductions, (c) ~$50M/year in denied payments since 2021, and (d)
  underpaying on paid claims by >$200M. Envision won a **$91 million**
  arbitration award against the payor over this conduct.
- **Inflation**: ~$330 million in increased costs since 2019 versus 2019
  spend levels.
- **Two rounds of pre-bankruptcy "liability management" (debt-exchange)
  transactions** that delayed but did not resolve the underlying problem:
  - **2020**: AMSURG raised $1.1B of new-money first-lien debt and
    exchanged ~$2.0B of existing debt into ~$1.4B of AMSURG second-lien
    debt, capturing ~$600M of discount (i.e., creditors accepted less
    than face value, reducing the total debt balance on paper).
  - **2022**: a further exercise raised $300M of new-money "first out"
    term loans and converted $3.7B of existing term loans into "second
    out" and "third out" tranches — capturing **>$1 billion** in discount
    and extending maturities on over 97% of the relevant debt.
- **At the Petition Date**: **$655 million** of cash on hand and
  approximately **$7.7 billion** in aggregate principal amount of funded
  debt (¶814) across a complex multi-tranche, two-silo structure (see §4).
- **The sponsors never exited.** Unlike Red Lobster's Golden Gate Capital,
  the "Consenting Sponsors" (KKR and co-investors) **"continue to own
  Envision today"** as of the May 2023 filing — holding 99.67% of the
  equity in Debtor Enterprise Parent Holdings, Inc. (the remainder held by
  management) — and had, by the time of filing, **also bought ~$146
  million of the company's own distressed "second out"/"third out" Term
  Loans and ~$253 million of its Senior Notes** (¶27), i.e. doubled down
  with debt purchases on top of the original equity position rather than
  exiting.

## 4. The capital structure at filing (the "dual-silo" structure)

Envision's $7.7B of funded debt was split across two largely separate
financing "silos" corresponding to its two operating segments — a
structural detail distinctive to this deal (neither Toys "R" Us nor Red
Lobster had anything like it):

- **EHC silo (Envision Physician Services / Physician Services)**:
  Revolving Credit Facility ($300M), Term Loan Facility ($5.45B
  aggregate principal, split into "first out" through "fourth out"
  tranches of varying seniority), and an ABL facility (up to $550M-$1.0B
  capacity, $440M drawn at filing).
- **AMSURG silo**: Revolving Credit Facility ($300M), First Lien Term
  Loan (~$1.1B + incremental facility, ~$1,358M total), Second Lien Term
  Loan (~$1.3B face, ~$1,493M outstanding after various repurchases).
- **Intercompany loans** between the silos: ~$983M short-term + ~$848M
  long-term outstanding as of May 14, 2023.
- The Restructuring Support Agreement, backed by the sponsors and more
  than 60% of the ~$7.7B of funded debt, contemplated deleveraging the
  EHC silo by ~$4.1 billion and AMSURG by ~$1.5 billion — a total
  reduction of **~$5.6 billion** excluding intercompany claims, or **~$7.4
  billion** including them.

## 5. The outcome

**Source**: press reporting on the October 11, 2023 plan confirmation and
November 3, 2023 emergence — notably
[Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/radiology-provider-envision-healthcare-successfully-emerges-bankruptcy-process),
[PE Stakeholder Project](https://pestakeholder.org/news/texas-bankruptcy-court-approves-envision-healthcares-split-into-two-companies-with-new-owners/),
and [BusinessWire](https://www.businesswire.com/news/home/20231011719176/en/Envision-Healthcare-Announces-Successful-Confirmation-of-Plans-of-Reorganization).

- Both silos' reorganization plans were confirmed **October 11, 2023**;
  the reorganized companies emerged **November 3, 2023** — 172 days after
  filing.
- **~70% of prepetition funded debt was eliminated.**
- Envision **split into two fully separate, independent companies**:
  **AmSurg** and **Envision Physician Services (EVPS)**, each with its
  own new ownership and leadership.
- Former senior creditors — led by **Pacific Investment Management
  (PIMCO)**, with **Blackstone** (which also owns Envision competitor
  TeamHealth as a private-credit lender) and **Brigade Capital** among
  others — converted debt into equity and became the new majority owners.
- **KKR's original $3.5 billion equity commitment was eliminated as a
  controlling stake.** Sources reviewed for this project disagree on the
  precise residual: one report states KKR retained a **minority** stake in
  reorganized AmSurg; another states KKR **"will no longer retain
  ownership of either company."** Both are shown rather than silently
  picking one — what both agree on is that KKR's $3.5B controlling equity
  position, and effectively all of its economic value, did not survive
  the restructuring.

## What this repo does NOT claim

- No continuous annual financial panel exists for 2018-2022 — Envision
  deregistered from SEC reporting immediately after the 2018 deal closed,
  and no comparable disclosure (like Red Lobster's Thai Union anchor
  point) was found for this gap. The 2020 and 2022 liability-management
  figures in §3 are real data points for those specific transactions, not
  a substitute for annual revenue/EBITDA figures.
- Whether KKR retained any residual stake in reorganized AmSurg is
  reported inconsistently across sources and is presented as an open
  discrepancy, not resolved by this project.
- The exact dollar size of KKR's total realized loss (equity + the ~$399M
  of debt instruments purchased pre-filing) is not calculated here —
  press reports of "$5 billion lost" likely include some combination of
  the $3.5B equity and some of the debt position, but no source reviewed
  gives a precise reconciliation, so this repo reports the $3.5B equity
  commitment and the ~$399M debt position as separate, individually
  cited figures rather than summing them into an unverified total.
