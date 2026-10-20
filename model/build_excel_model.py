"""
Builds EnvisionHealthcare_LBO_Model.xlsx. Same discipline as the other two
models: blue = cited input, black = formula, red = flagged assumption.
This one has no red cells at all -- unlike the other two projects, every
figure used here (including the crisis attribution and the liability
management transactions) comes directly from the first-day declaration;
there was no need for an illustrative modeling assumption this time.
"""
import csv
import os

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "data", "processed")

FONT = "Calibri"
TITLE_FONT = Font(name=FONT, size=16, bold=True, color="FFFFFF")
HEADER_FONT = Font(name=FONT, size=10, bold=True, color="FFFFFF")
SECTION_FONT = Font(name=FONT, size=11, bold=True)
LABEL_FONT = Font(name=FONT, size=10)
INPUT_FONT = Font(name=FONT, size=10, color="0000FF")
CALC_FONT = Font(name=FONT, size=10, color="000000")
NOTE_FONT = Font(name=FONT, size=9, italic=True, color="808080")

DARK_FILL = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
LIGHT_FILL = PatternFill(start_color="D9E2F3", end_color="D9E2F3", fill_type="solid")

THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

MONEY = '#,##0.0;(#,##0.0)'
MONEY0 = '#,##0;(#,##0)'
PCT1 = '0.0%'


def read_csv(name):
    with open(os.path.join(DATA, name), newline="") as f:
        return list(csv.DictReader(f))


def title_bar(ws, text, span, row=1):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text)
    c.font = TITLE_FONT
    c.fill = DARK_FILL
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[row].height = 28


def section(ws, row, col, text, span=1):
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col + span - 1)
    c = ws.cell(row=row, column=col, value=text)
    c.font = SECTION_FONT
    c.fill = LIGHT_FILL
    return row + 1


def kv(ws, row, label, value, col=1, number_format=None, font=CALC_FONT, note=None):
    lc = ws.cell(row=row, column=col, value=label)
    lc.font = LABEL_FONT
    vc = ws.cell(row=row, column=col + 1, value=value)
    vc.font = font
    if number_format:
        vc.number_format = number_format
    if note:
        vc.comment = Comment(note, "model")
    return row + 1


wb = openpyxl.Workbook()
wb.remove(wb.active)

# ======================================================================
# TAB 1: Cover
# ======================================================================
ws = wb.create_sheet("Cover")
ws.column_dimensions["A"].width = 100
title_bar(ws, "Envision Healthcare -- LBO Case Study Model", span=1)
r = 3
intro = ("A reconstruction of KKR's 2018 take-private of Envision Healthcare ($9.9B) through its "
         "May 2023 Chapter 11 filing. See docs/sources.md for every citation -- the core source is a "
         "177-page bankruptcy court declaration with unusually granular financial detail.")
ws.cell(row=r, column=1, value=intro).font = LABEL_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.row_dimensions[r].height = 30
r += 2

r = section(ws, r, 1, "THE THIRD PATTERN")
diffs = [
    "Toys R Us: one sponsor holds conventional debt for 12 years until it breaks the company.",
    "Red Lobster: the sponsor who engineered the real-estate sale-leaseback exits in 2020, 4 years before the collapse.",
    "Envision Healthcare: KKR never exited -- still held 99.67% of equity at filing, and had bought ~$399M of the company's own distressed debt on top of its original $3.5B equity stake.",
    "This was also Envision's SECOND leveraged buyout -- CD&R took the EmCare predecessor private in 2011 too.",
    "The capital structure was split into two largely separate 'silos' (EHC/Physician Services and AMSURG) -- a structural feature unique to this deal among the three.",
]
for d in diffs:
    ws.cell(row=r, column=1, value="• " + d).font = LABEL_FONT
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
    r += 1
r += 1

r = section(ws, r, 1, "TABS IN THIS WORKBOOK")
tabs = [
    ("2018 Deal", "KKR's $3.5B equity commitment vs. up to $8.05B of debt financing commitments."),
    ("Pre-2018 Operating History", "Envision's thin and shrinking operating margin going into the deal."),
    ("Crisis Attribution", "COVID, the payor dispute, and inflation -- each quantified separately in the declaration."),
    ("Liability Management", "Two rounds of pre-bankruptcy debt exchanges (2020, 2022) that delayed but didn't prevent the filing."),
    ("Capital Structure 2023", "The dual-silo debt breakdown at the May 2023 filing."),
    ("Ownership & Outcome", "KKR's position through the filing, and the final debt-to-equity conversion outcome."),
]
for name, desc in tabs:
    ws.cell(row=r, column=1, value=f"{name}:  {desc}").font = LABEL_FONT
    r += 1
r += 1
r = section(ws, r, 1, "KEY DISCLAIMER")
disclaimer = ("Blue font = pulled directly from a cited source. Black font = formula computed from those "
              "inputs. Unlike the other two projects in this series, this workbook has NO red-flagged "
              "illustrative assumption cells -- every figure, including the crisis-cause attribution and "
              "the liability-management transaction details, comes directly from the cited bankruptcy "
              "declaration or merger proxy. Where sources disagree (KKR's exact residual stake post-"
              "emergence), both versions are shown rather than resolved by guessing.")
ws.cell(row=r, column=1, value=disclaimer).font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.row_dimensions[r].height = 60

# ======================================================================
# TAB 2: 2018 Deal
# ======================================================================
deal = read_csv("deal_2018.csv")
ws = wb.create_sheet("2018 Deal")
ws.column_dimensions["A"].width = 44
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 24
ws.column_dimensions["D"].width = 60
title_bar(ws, "2018 Take-Private: Envision → KKR (docs/sources.md §2)", span=4)
r = 3
hdr = r + 1
for i, h in enumerate(["Item", "$M", "Source", "Notes"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
deal_start = r
deal_rows = {}
for row in deal:
    ws.cell(row=r, column=1, value=row["item"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY
    ws.cell(row=r, column=3, value=row["source"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["notes"]).font = NOTE_FONT
    deal_rows[row["item"]] = r
    r += 1
deal_end = r - 1
r += 1
r = section(ws, r, 1, "FINANCING MIX", span=4)
eq_row = deal_rows["KKR equity commitment"]
debt_row = deal_rows["Debt financing commitment (up to)"]
r = kv(ws, r, "Debt commitment / equity commitment ratio", f"=B{debt_row}/B{eq_row}", font=Font(name=FONT, bold=True), number_format='0.00"x"')
for row in ws.iter_rows(min_row=hdr, max_row=deal_end, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 3: Pre-2018 Operating History
# ======================================================================
pre2018 = read_csv("pre_2018_operating_history.csv")
ws = wb.create_sheet("Pre-2018 Operating History")
ws.column_dimensions["A"].width = 44
for i in range(3):
    ws.column_dimensions[get_column_letter(2 + i)].width = 14
ws.column_dimensions["E"].width = 60
title_bar(ws, "Operating History Going Into the Deal (docs/sources.md §1)", span=5)
r = 3
hdr = r + 1
for i, h in enumerate(["Period", "Net Revenue $M", "Operating Income $M", "Op. Margin", "Notes"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
for row in pre2018:
    ws.cell(row=r, column=1, value=row["period"]).font = INPUT_FONT
    rev = ws.cell(row=r, column=2, value=float(row["net_revenue_musd"]) if row["net_revenue_musd"] else None)
    rev.font = INPUT_FONT
    rev.number_format = MONEY
    oi = ws.cell(row=r, column=3, value=float(row["operating_income_musd"]) if row["operating_income_musd"] else None)
    oi.font = INPUT_FONT
    oi.number_format = MONEY
    m = ws.cell(row=r, column=4, value=float(row["operating_margin_pct"]) / 100)
    m.font = INPUT_FONT
    m.number_format = PCT1
    ws.cell(row=r, column=5, value=row["notes"]).font = NOTE_FONT
    ws.cell(row=r, column=5).alignment = Alignment(wrap_text=True)
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=5):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 4: Crisis Attribution
# ======================================================================
crisis = read_csv("crisis_events.csv")
ws = wb.create_sheet("Crisis Attribution")
ws.column_dimensions["A"].width = 58
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 24
ws.column_dimensions["D"].width = 40
title_bar(ws, "What Broke the Company, Quantified (docs/sources.md §3)", span=4)
r = 3
hdr = r + 1
for i, h in enumerate(["Event", "$M", "Period", "Source"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
crisis_start = r
crisis_rows = {}
for row in crisis:
    ws.cell(row=r, column=1, value=row["event"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY
    ws.cell(row=r, column=3, value=row["period"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["source"]).font = NOTE_FONT
    crisis_rows[row["event"]] = r
    r += 1
crisis_end = r - 1
for row in ws.iter_rows(min_row=hdr, max_row=crisis_end, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER
r += 1
r = section(ws, r, 1, "COMBINED IMPACT (COVID + PAYOR + INFLATION ONLY)", span=4)
covid20 = crisis_rows["COVID-19 revenue impact"]  # first match = 2020 row (appears first in CSV)
# Find rows precisely by re-scanning since dict only keeps last match for duplicate keys
impact_rows = [i for i, row in enumerate(crisis, start=crisis_start) if row["event"] in (
    "COVID-19 revenue impact", "Payor dispute cumulative revenue impact (>$400M stated)", "Inflationary cost increase vs. 2019 spend")]
refs = "+".join(f"B{i}" for i in impact_rows)
r = kv(ws, r, "Sum of quantified negative impacts shown above", f"=SUM({','.join(f'B{i}' for i in impact_rows)})",
       font=Font(name=FONT, bold=True), number_format=MONEY,
       note="Simple sum of the discrete, separately-cited impact figures above -- not a formal bridge to a single consolidated EBITDA decline, since the declaration quantifies these as distinct management-cited factors, not line items of one waterfall.")

# ======================================================================
# TAB 5: Liability Management
# ======================================================================
ws = wb.create_sheet("Liability Management")
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 24
ws.column_dimensions["D"].width = 18
title_bar(ws, "Pre-Bankruptcy 'Extend and Pretend' (docs/sources.md §3)", span=4)
r = 3
note = ("Two rounds of debt-exchange transactions before the actual Chapter 11 filing. Both captured real "
        "accounting discount (creditors accepted less than face value) -- neither fixed the underlying problem.")
ws.cell(row=r, column=1, value=note).font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
ws.row_dimensions[r].height = 30
r += 2
hdr = r
headers = ["Round", "New Money Raised ($M)", "Existing Debt Exchanged ($M)", "Discount Captured ($M)"]
for i, h in enumerate(headers):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r += 1
lm_data = [("2020 (AMSURG)", 1100, 2000, 600), ("2022", 300, 3700, 1000)]
lm_start = r
for label, nm, ex, disc in lm_data:
    ws.cell(row=r, column=1, value=label).font = INPUT_FONT
    for ci, val in enumerate([nm, ex, disc], start=2):
        c = ws.cell(row=r, column=ci, value=val)
        c.font = INPUT_FONT
        c.number_format = MONEY0
    r += 1
lm_end = r - 1
ws.cell(row=r, column=1, value="Total").font = Font(name=FONT, bold=True)
for ci in (2, 3, 4):
    col = get_column_letter(ci)
    c = ws.cell(row=r, column=ci, value=f"=SUM({col}{lm_start}:{col}{lm_end})")
    c.font = Font(name=FONT, bold=True)
    c.number_format = MONEY0
total_lm_row = r
r += 2
r = kv(ws, r, "Total funded debt still outstanding at the actual May 2023 filing ($M)", 7700, font=INPUT_FONT, number_format=MONEY0,
       note="Despite >$1.6B of combined discount captured across both liability-management rounds, $7.7B of funded debt remained at filing -- the exchanges delayed the problem, they didn't solve it.")

for row in ws.iter_rows(min_row=hdr, max_row=total_lm_row, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 6: Capital Structure 2023
# ======================================================================
capstruct = read_csv("capital_structure_silos_2023.csv")
ws = wb.create_sheet("Capital Structure 2023")
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 36
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 24
title_bar(ws, "The Dual-Silo Capital Structure at Filing (docs/sources.md §4)", span=4)
r = 3
hdr = r + 1
for i, h in enumerate(["Silo", "Facility", "$M", "Detail"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
cs_start = r
for row in capstruct:
    ws.cell(row=r, column=1, value=row["silo"]).font = INPUT_FONT
    ws.cell(row=r, column=2, value=row["facility"]).font = INPUT_FONT
    c = ws.cell(row=r, column=3, value=float(row["amount_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY0
    ws.cell(row=r, column=4, value=row["detail"]).font = NOTE_FONT
    r += 1
cs_end = r - 1
for row in ws.iter_rows(min_row=hdr, max_row=cs_end, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER
r += 1
r = section(ws, r, 1, "TOTAL BY SILO", span=4)
silos = sorted(set(row["silo"] for row in capstruct))
for silo in silos:
    label_rows = [i for i, row in enumerate(capstruct, start=cs_start) if row["silo"] == silo]
    refs = "+".join(f"C{i}" for i in label_rows)
    r = kv(ws, r, silo, f"={refs}", font=Font(name=FONT, bold=True), number_format=MONEY0)
r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
ws.cell(row=r, column=1, value="Reconciliation note: these three totals sum to more than the declaration's "
        "headline '$7.7 billion total funded debt' figure. That's expected, not an error -- this table mixes "
        "committed facility SIZES (e.g. the $300M revolvers) with actually-DRAWN balances (e.g. the $440M ABL "
        "draw), and the consolidated $7.7B figure nets out intercompany loans between the silos, which are "
        "shown here as a separate, additive line instead. See docs/sources.md §4 for the exact wording of "
        "each figure as disclosed.").font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.row_dimensions[r].height = 60

# ======================================================================
# TAB 7: Ownership & Outcome
# ======================================================================
outcome = read_csv("bankruptcy_outcome_2023.csv")
ws = wb.create_sheet("Ownership & Outcome")
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 90
title_bar(ws, "KKR's Position Through Filing, and the Outcome", span=2)
r = 3
timeline = [
    ("2011", "CD&R takes EmCare (Envision's predecessor) private for ~$3B -- Envision's FIRST leveraged buyout."),
    ("2013", "Goes public again as Envision Healthcare."),
    ("2016", "'Merger of equals' with AmSurg Corp forms Envision Healthcare Corporation (NYSE: EVHC)."),
    ("2018", "KKR take-private: $9.9B total, $3.5B KKR equity commitment, up to $8.05B debt financing. Deal closes Oct 11; SEC deregistration filed Oct 22."),
    ("2020", "COVID hits (~$1.1B revenue / $415M EBITDA impact). AMSURG liability management #1: $1.1B new money, $2.0B debt exchanged, $600M discount captured."),
    ("2022", "Liability management #2: $300M new money, $3.7B debt converted to 2nd/3rd-out tranches, >$1B discount captured."),
    ("May 2023", "Chapter 11 filed with $655M cash and $7.7B funded debt. KKR still holds 99.67% of parent equity AND has bought ~$399M of the company's own distressed debt."),
    ("Oct-Nov 2023", "Plans confirmed (Oct 11) and company emerges (Nov 3) as two independent companies: AmSurg and Envision Physician Services. ~70% of funded debt eliminated. Former creditors (PIMCO, Blackstone, Brigade Capital) become new majority owners via debt-to-equity conversion."),
]
hdr = r
ws.cell(row=hdr, column=1, value="Year").font = HEADER_FONT
ws.cell(row=hdr, column=1).fill = DARK_FILL
ws.cell(row=hdr, column=2, value="Event").font = HEADER_FONT
ws.cell(row=hdr, column=2).fill = DARK_FILL
r += 1
for year, event in timeline:
    ws.cell(row=r, column=1, value=year).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=event)
    c.font = INPUT_FONT
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 42
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=2):
    for cell in row:
        cell.border = BORDER
r += 1
r = section(ws, r, 1, "FINAL OUTCOME DETAIL", span=2)
for row in outcome:
    ws.cell(row=r, column=1, value=row["item"]).font = LABEL_FONT
    v = ws.cell(row=r, column=2, value=row["value"])
    v.font = INPUT_FONT
    v.alignment = Alignment(wrap_text=True)
    ws.row_dimensions[r].height = 30
    r += 1

out_path = os.path.join(HERE, "EnvisionHealthcare_LBO_Model.xlsx")
wb.save(out_path)
print("wrote", out_path)
