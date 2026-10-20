"""
Assembles data/processed/*.csv from the figures cited in docs/sources.md.
Same discipline as the other two projects: every number here is transcribed
from a specific cited source. No interpolation -- the 2018-2022 gap is a
real, stated gap, not filled in.
"""
import csv
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
os.makedirs(OUT_DIR, exist_ok=True)


def write_csv(name, header, rows):
    path = os.path.join(OUT_DIR, name)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print("wrote", path, len(rows), "rows")


# --- 1. Pre-2018 operating history (docs/sources.md §1) ---
write_csv(
    "pre_2018_operating_history.csv",
    ["period", "net_revenue_musd", "operating_income_musd", "operating_margin_pct", "source", "notes"],
    [
        ("FY2015", None, None, 24.1, "FY2017 10-K common-size table", "Pre-AmSurg-merger entity -- not directly comparable to FY2017's combined-company revenue base"),
        ("FY2016", None, None, 10.6, "FY2017 10-K common-size table", "Year of the Envision Healthcare Holdings / AmSurg 'merger of equals' (Dec 2016) -- mixed-perimeter year"),
        ("FY2017", 7819.3, 189.2, 2.4, "FY2017 10-K selected financial data", "First full year as the combined company -- the entry-year financial picture KKR was buying into"),
    ],
)

# --- 2. The 2018 deal (docs/sources.md §2) ---
write_csv(
    "deal_2018.csv",
    ["item", "value_musd", "source", "notes"],
    [
        ("Total transaction value", 9900, "Press / widely reported", "Includes assumption/repayment of existing debt"),
        ("Per-share merger consideration", 46.00, "DEFM14A", "USD per share, cash, 32% premium to VWAP since Nov 1 2017"),
        ("KKR equity commitment", 3500, "DEFM14A", "'An aggregate amount in cash equal to $3.5 billion'"),
        ("Debt financing commitment (up to)", 8050, "DEFM14A", "Commitment letters from Credit Suisse, Citi, Morgan Stanley, Barclays, Goldman Sachs et al. -- sized with headroom, not necessarily fully drawn"),
        ("Senior Notes issued at close (Oct 11 2018)", 1225, "2023 first-day declaration ¶76", "The one piece of acquisition financing that was itself a registered/public instrument"),
    ],
)

# --- 3. The crisis narrative, as discrete cited events (docs/sources.md §3) ---
write_csv(
    "crisis_events.csv",
    ["event", "value_musd", "period", "source"],
    [
        ("COVID-19 revenue impact", -1100, "2020", "First-day declaration"),
        ("COVID-19 EBITDA impact", -415, "2020", "First-day declaration"),
        ("COVID-19 revenue impact", -380, "2021", "First-day declaration"),
        ("Payor dispute cumulative revenue impact (>$400M stated)", -400, "2018-2022", "First-day declaration"),
        ("...of which: unilateral contract term change", -100, "2018", "First-day declaration"),
        ("...of which: additional rate reduction", -100, "n/a", "First-day declaration"),
        ("...of which: denied payments (annual rate since 2021)", -50, "per year since 2021", "First-day declaration"),
        ("...of which: underpayment on paid claims", -200, "cumulative", "First-day declaration"),
        ("Arbitration award won against the payor", 91, "n/a", "First-day declaration"),
        ("Inflationary cost increase vs. 2019 spend", -330, "since 2019", "First-day declaration"),
        ("2020 liability management: new-money first lien raised (AMSURG)", 1100, "2020", "First-day declaration"),
        ("2020 liability management: debt exchanged into AMSURG 2nd lien", -2000, "2020", "First-day declaration (into ~$1.4B of new debt)"),
        ("2020 liability management: discount captured", 600, "2020", "First-day declaration"),
        ("2022 liability management: new-money first-out term loans", 300, "2022", "First-day declaration"),
        ("2022 liability management: existing term loans converted to 2nd/3rd out", -3700, "2022", "First-day declaration"),
        ("2022 liability management: discount captured", 1000, "2022", "First-day declaration, '>$1 billion'"),
        ("Cash on hand at Chapter 11 filing", 655, "2023-05-15", "First-day declaration ¶ (petition date)"),
        ("Total funded debt at filing", 7700, "2023-05-15", "First-day declaration ¶814"),
        ("KKR's purchased distressed Term Loans at filing", 146, "2023-05-15", "First-day declaration ¶27, 'second out'/'third out'"),
        ("KKR's purchased distressed Senior Notes at filing", 253, "2023-05-15", "First-day declaration ¶27"),
    ],
)

# --- 4. Capital structure detail -- the dual-silo breakdown (docs/sources.md §4) ---
write_csv(
    "capital_structure_silos_2023.csv",
    ["silo", "facility", "amount_musd", "detail", "source"],
    [
        ("EHC (Physician Services)", "Revolving Credit Facility", 300, "committed", "First-day declaration"),
        ("EHC (Physician Services)", "Term Loan Facility (all tranches)", 5450, "'first out' through 'fourth out'", "First-day declaration"),
        ("EHC (Physician Services)", "ABL Facility drawn", 440, "of up to $550M-$1.0B capacity", "First-day declaration"),
        ("AMSURG", "Revolving Credit Facility", 300, "committed", "First-day declaration"),
        ("AMSURG", "First Lien Term Loan (incl. incremental)", 1358, "", "First-day declaration"),
        ("AMSURG", "Second Lien Term Loan outstanding", 1493, "after repurchases", "First-day declaration"),
        ("Intercompany", "Short-term loans outstanding", 983, "as of 2023-05-14", "First-day declaration"),
        ("Intercompany", "Long-term loans outstanding", 848, "as of 2023-05-14", "First-day declaration"),
    ],
)

# --- 5. Restructuring support agreement targets (docs/sources.md §4) ---
write_csv(
    "rsa_deleveraging_targets.csv",
    ["item", "value_musd", "source"],
    [
        ("EHC silo deleveraging target", 4100, "First-day declaration"),
        ("AMSURG silo deleveraging target", 1500, "First-day declaration"),
        ("Total reduction excl. intercompany claims", 5600, "First-day declaration"),
        ("Total reduction incl. intercompany claims", 7400, "First-day declaration"),
        ("RSA support, % of funded debt", 60, "First-day declaration ('more than 60%')"),
    ],
)

# --- 6. Outcome (docs/sources.md §5) ---
write_csv(
    "bankruptcy_outcome_2023.csv",
    ["item", "value", "source"],
    [
        ("Filing date", "2023-05-15", "First-day declaration"),
        ("Court", "US Bankruptcy Court, Southern District of Texas, Houston Division, Case 23-90342 (CML)", "First-day declaration"),
        ("Plans confirmed", "2023-10-11", "Press (BusinessWire)"),
        ("Emergence date", "2023-11-03", "Press"),
        ("Days in Chapter 11", "172", "Press"),
        ("Prepetition funded debt eliminated", "~70%", "Press"),
        ("Outcome structure", "Split into two independent companies: AmSurg and Envision Physician Services (EVPS)", "Press"),
        ("New majority owner(s)", "Former creditors led by PIMCO, with Blackstone and Brigade Capital among others, via debt-to-equity conversion", "Press"),
        ("KKR equity outcome", "Original $3.5B controlling equity commitment eliminated. Residual stake disputed across sources: one report states KKR retained a minority stake in AmSurg; another states KKR retains no ownership of either company. Both shown; not resolved here.", "Press (conflicting reports -- see sources.md)"),
    ],
)
