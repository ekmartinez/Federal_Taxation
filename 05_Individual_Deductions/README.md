# Individual Deductions

## Examples & Exercises

- [Examples](05_Individual_Deductions_Examples.ipynb)
- [Exercises](05_Individual_Deductions_Exercises.ipynb)
- [Comprehensive Problems](./Comprehensive_Problems/)

## Overview

This chapter covers how individuals actually reduce taxable income through deductions. It splits into three big pieces: **for-AGI deductions** (business-related, and a grab-bag of other above-the-line items Congress allows), **from-AGI deductions** (the itemized deductions on Schedule A, plus the standard deduction as the alternative to itemizing), and the **qualified business income (QBI) deduction**, which sits on top of either one.

## Table of Contents
- [Deductions For AGI](#deductions-for-agi)
  - [Deductions Directly Related to Business Activities](#deductions-directly-related-to-business-activities)
    - [Trade or Business Expense](#trade-or-business-expense)
    - [Rent and Royalty Expenses](#rent-and-royalty-expenses)
    - [Losses on Dispositions](#losses-on-dispositions)
    - [Flow-Through Entities](#flow-through-entities)
    - [Excess Business Loss Limitation](#excess-business-loss-limitation)
  - [Deductions Indirectly Related to Business Activities](#deductions-indirectly-related-to-business-activities)
    - [Moving Expenses](#moving-expenses)
    - [Health Insurance Deduction by Self-Employed Taxpayers](#health-insurance-deduction-by-self-employed-taxpayers)
    - [Self-Employment Tax Deduction](#self-employment-tax-deduction)
    - [Deductions for Individual Retirement Accounts (IRAs)](#deductions-for-individual-retirement-accounts-iras)
    - [Deductions for Health Savings Accounts](#deductions-for-health-savings-accounts)
    - [Penalty for Early Withdrawal of Savings](#penalty-for-early-withdrawal-of-savings)
    - [Deduction for Interest on Qualified Education Loans](#deduction-for-interest-on-qualified-education-loans)
- [Deductions from AGI: Itemized Deductions](#deductions-from-agi-itemized-deductions)
  - [Medical Expenses](#medical-expenses)
    - [Transportation and Travel for Medical Purposes](#transportation-and-travel-for-medical-purposes)
    - [Hospitals and Long-Term Care Facilities](#hospitals-and-long-term-care-facilities)
    - [Medical Expense Deduction Limitation](#medical-expense-deduction-limitation)
  - [Taxes](#taxes)
  - [Interest](#interest)
  - [Charitable Contributions](#charitable-contributions)
    - [Contributions of Money](#contributions-of-money)
    - [Contributions of Property Other Than Money](#contributions-of-property-other-than-money)
    - [Charitable Contribution Deduction Limitations](#charitable-contribution-deduction-limitations)
  - [Casualty and Theft Losses on Personal-Use Assets](#casualty-and-theft-losses-on-personal-use-assets)
  - [Other Itemized Deductions](#other-itemized-deductions)
- [The Standard Deduction](#the-standard-deduction)
  - [Bunching Itemized Deductions](#bunching-itemized-deductions)
- [Deduction for Qualified Business Income](#deduction-for-qualified-business-income)
  - [Limitations](#limitations)

---

## Deductions For AGI

For-AGI deductions fall into three buckets:
1. Directly tied to business activity.
2. Indirectly tied to business activity.
3. Deductions Congress created to subsidize specific behavior.

### Deductions Directly Related to Business Activities

The underlying fairness argument here: if business revenue is taxable, the expenses used to generate it should be deductible against it.

First, a key distinction — **business activities** (a trade or business, requiring meaningful ongoing involvement) vs. **investment activities** (profit-motivated but passive, e.g., holding property for appreciation or income). Both are "profit-motivated," but they're treated very differently for deduction purposes.

- Nearly all **business expenses** are deductible for AGI — the one exception is unreimbursed employee expenses, which aren't deductible at all anymore.
- Only two types of **investment expenses** are deductible: rental/royalty expenses (for AGI, regardless of whether the activity counts as investment or business), and investment interest expense (from AGI, as an itemized deduction). Everything else investment-related is simply nondeductible.

**Summary table:**

| Activity Type | Deduction for AGI | Deduction from AGI | Not Deductible |
| --- | --- | --- | --- |
| Business activities | Self-employed business expenses | Qualified business income deduction | Unreimbursed employee business expenses |
| Investment activities | Rental and royalty expenses | Investment interest expense | Other investment expenses |

#### Trade or Business Expense

To be deductible, a business expense must be directly connected to the activity and "ordinary and necessary" — i.e., a normal, helpful cost of generating profit. These show up on **Schedule C**, not directly on page 1 of Form 1040 — net income/loss flows from Schedule C → Schedule 1, line 3 → Form 1040 line 8 (total income).

#### Rent and Royalty Expenses

Deductible for AGI, same general treatment as business expenses, but reported on **Schedule E** rather than Schedule C — flowing to Schedule 1, line 5 → Form 1040 line 8. Even though rental/royalty activity is usually classified as investment rather than business, it still gets the for-AGI treatment. That said, deducting a rental *loss* is limited by several overlapping rules: basis, at-risk amount, passive activity loss rules, and the excess business loss limitation.

#### Losses on Dispositions

Losses on selling business assets are deductible for AGI. Losses on selling investment (capital) assets are first netted against capital gains; if losses exceed gains, up to $3,000 of the excess is deductible in the current year, with anything beyond that carried forward indefinitely (subject to the same rules each future year).

#### Flow-Through Entities

Partnerships, LLCs, and S corporations pass income (and losses) through to owners, reported on the owner's **Schedule E** (same routing as rental/royalty income: → Schedule 1, line 5 → Form 1040 line 8). Losses are still subject to basis, at-risk, and passive-loss limitations at the owner level.

#### Excess Business Loss Limitation

Even after clearing the basis/at-risk/passive-loss hurdles, a business loss can be further capped. An **excess business loss** — aggregate business deductions exceeding aggregate business income/gain plus a threshold — isn't deductible currently; it carries forward as a net operating loss instead. The 2024 threshold is $610,000 (MFJ) / $305,000 (others), inflation-indexed. For partnerships/S corps, this limitation applies at the individual partner/shareholder level, not the entity level.

### Deductions Indirectly Related to Business Activities

These are costs a taxpayer wouldn't have incurred if not for being in business, even though they aren't directly generating business revenue.

#### Moving Expenses

Generally **not deductible** anymore (and employer reimbursement of moving costs is taxable), even for a job-related move. The one carve-out: active-duty military members (or their spouse/dependents) moving under military orders for a permanent change of station — their moving costs are excluded if employer-paid, or deductible if not.

#### Health Insurance Deduction by Self-Employed Taxpayers

Employees get health insurance premiums excluded from income when an employer pays them; self-employed people don't have that mechanism since they're not "employees." As a fairness fix, self-employed taxpayers can deduct their own health insurance premiums (covering themselves, spouse, dependents, and children under 27 regardless of dependent status) for AGI — but only up to the income actually earned from that specific business. This deduction disappears entirely if the taxpayer is eligible for coverage under an employer plan (their own or their spouse's), whether or not they actually enroll in it.

#### Self-Employment Tax Deduction

Employers get to deduct their share of Social Security/Medicare tax paid on employee wages. Self-employed individuals pay both the employee and "employer" share themselves (self-employment tax) but can't treat the whole thing as a business expense — as a partial offset, they're allowed to deduct the employer-equivalent half of what they paid, for AGI.

#### Deductions for Individual Retirement Accounts (IRAs)

Anyone with earned income can contribute to a traditional IRA; how much of that contribution is deductible depends on filing status, active participation in an employer plan, and modified AGI. Deductible contributions are for AGI. Distributions are taxed as ordinary income, with a 10% penalty for withdrawals before age 59½. Taxpayers who can't deduct contributions can still make nondeductible ones — on distribution, only the earnings (not the original nondeductible contributions) get taxed.

#### Deductions for Health Savings Accounts

HSAs are available to people enrolled in a qualifying high-deductible health plan with no other coverage, to cover qualified medical/dental costs for themselves, spouse, and dependents.

2024 figures:
- Minimum deductible for the underlying health plan: $1,600 self-only / $3,200 family.
- Max out-of-pocket cap on that plan: $8,050 self-only / $16,100 family.
- HSA contribution limit (deductible for AGI): $4,150 self-only / $8,300 family, plus an extra $1,000 catch-up if 55+.

Funds sit in the account and can grow tax-free; distributions are tax-free as long as they cover qualified medical expenses of the account holder, spouse, or dependents incurred *after* the HSA was opened (the distribution itself can happen in a later year, even after losing high-deductible coverage — you just need receipts). Non-qualified distributions are taxed as ordinary income plus a 20% penalty, unless the account holder is disabled, 65+, or deceased.

#### Penalty for Early Withdrawal of Savings

If a bank charges an early-withdrawal penalty on a CD (forfeited interest), that forfeited amount is deductible for AGI — netting the taxpayer's reportable interest income down to what they actually kept, rather than forcing them to report the full gross interest and separately lose the penalty as a nondeductible investment expense.

#### Deduction for Interest on Qualified Education Loans

Covers loans used for qualified higher-education costs (tuition, fees, books, required supplies, room/board, even travel) for the taxpayer, spouse, or dependent. Up to $2,500 of interest paid is deductible, phased out based on filing status and modified AGI (AGI computed before this deduction). MFS filers get no deduction at all, regardless of income.

**Phase-out summary (2024-style figures used in the text):**

| Modified AGI | Deduction |
| --- | --- |
| ≤ $80,000 ($165,000 MFJ) | Full amount paid, up to $2,500 |
| $80,000–$95,000 ($165,000–$195,000 MFJ) | $2,500 max, reduced by a phase-out percentage |
| ≥ $95,000 ($195,000 MFJ) | Zero |

Phase-out percentage: (Modified AGI − $80,000) / $15,000 for single/HoH; (Modified AGI − $165,000) / $30,000 for MFJ.

## Deductions from AGI: Itemized Deductions

Many itemized deductions exist to subsidize socially favored activities (homeownership, charitable giving); others (like medical expenses) provide relief when a taxpayer's ability to pay has been involuntarily reduced. These follow the order they appear on Schedule A.

### Medical Expenses

Covers unreimbursed payments for care, prevention, diagnosis, or cure of injury/disease/bodily function — for the taxpayer, spouse, and dependents. Includes prescriptions, insulin, medical aids (glasses, wheelchairs), provider/facility payments, medical transportation, long-term care facilities, and health insurance premiums (if not already deducted for AGI by a self-employed taxpayer). Over-the-counter medicine generally doesn't count. Cosmetic procedures are excluded unless they correct a congenital defect, an injury from an accident/trauma, or a disfiguring disease.

#### Transportation and Travel for Medical Purposes

Lodging (with restrictions) and transportation costs while traveling primarily to receive essential medical care are deductible. Using a personal car: a standard mileage rate applies (21¢/mile for 2024) instead of actual costs.

#### Hospitals and Long-Term Care Facilities

Meals/lodging at a hospital are deductible. At other facilities (like nursing homes), meals/lodging are only deductible if the main reason for being there is medical care, not just convenience — actual medical care costs are deductible regardless of the facility type.

#### Medical Expense Deduction Limitation

Only unreimbursed medical expenses **exceeding 7.5% of AGI** are deductible — this is a "floor," meaning everything below that threshold produces zero benefit. Because the floor is set relatively high, this deduction rarely helps, especially for higher-income taxpayers.

### Taxes

Deductible taxes include: state/local/foreign income tax (including amounts withheld, estimated payments, and prior-year overpayments applied forward), state/local real estate tax (personal or investment property), and state/local personal property tax based on assessed value. Taxpayers can elect to deduct state/local **sales tax** instead of income tax — useful in states with no income tax. Total state/local tax deduction (SALT) is capped at $10,000 ($5,000 MFS); foreign income tax isn't subject to this cap.

### Interest

**Mortgage interest** on acquisition debt secured by a qualified residence (main home plus one other) is deductible. "Acquisition indebtedness" means debt used to buy, build, or substantially improve the residence — including a home equity loan used for that purpose. The cap depends on when the debt originated:
- Debt from after 12/15/2017: capped at $750,000 ($375,000 MFS).
- Debt from before 12/16/2017: capped at $1,000,000 ($500,000 MFS), even if later refinanced.
- If a taxpayer has both old and new debt, the $750,000/$375,000 cap for new debt is reduced (not below zero) by the amount of pre-2017 debt.

**Investment interest** (on loans to buy stocks, bonds, land, etc.) is deductible only up to net investment income, with any excess carried forward. Personal credit card interest and interest on personal-use auto loans are never deductible.

### Charitable Contributions

Qualifying recipients include educational, religious, scientific, governmental, and other public-purpose organizations. Political/campaign contributions don't qualify, even though they indirectly support government functions. Deductions generally require written substantiation.

#### Contributions of Money

Cash gifts (cash, check, EFT, credit card, payroll deduction) are deductible in the year paid. Travel/transportation costs for charitable purposes count as a cash contribution too, as long as there's no significant personal enjoyment element — personal vehicle use gets a standard mileage rate (14¢/mile). The value of *time/services* donated is never deductible, only actual out-of-pocket costs. If something of value is received in return for a donation (e.g., a gala dinner), only the excess over the fair market value of what was received is deductible.

#### Contributions of Property Other Than Money

Treatment depends on whether the donated property is **capital gain property** or **ordinary income property**.

- **Capital gain property** (appreciated assets that would've produced long-term capital gain if sold — investments, eligible business assets, personal-use assets held over a year) is generally deductible at full **fair market value**, without ever recognizing the built-in gain — which is what makes donating appreciated property especially tax-efficient. Exception: tangible personal property (not real estate) that the charity puts to a use unrelated to its charitable purpose is capped at adjusted basis instead — unless the taxpayer reasonably expected a related use at the time of the gift.
- **Ordinary income property** (assets held a year or less, inventory, depreciation-recapture-tainted business property, or anything that's declined in value below basis) is deductible only at the **lesser of** fair market value or adjusted basis.

#### Charitable Contribution Deduction Limitations

The maximum deductible amount for the year depends on both what's donated and who it's donated to. Public charities and private *operating* foundations get more favorable limits than private *nonoperating* foundations.

| Contribution Type | Public Charity / Private Operating Foundation | Private Nonoperating Foundation |
| --- | --- | --- |
| Cash | Cash amount, up to 60% of AGI | Cash amount, up to 30% of AGI |
| Capital gain property | FMV, up to 30% of AGI | Basis (FMV if publicly-traded stock), up to 20% of AGI |
| Ordinary income property | Lesser of basis or FMV, up to 50% of AGI | Lesser of basis or FMV, up to 30% of AGI |

When multiple categories apply in the same year, they're layered in order (60% bucket first, then 50%, then 30%, then 20% — each subsequent limit reduced by what was already absorbed by the higher-priority buckets). Contributions exceeding the ceiling carry forward for **5 years**, using current-year contributions first before drawing down the carryforward. In practice, these ceilings are generous enough that most taxpayers never hit them.

### Casualty and Theft Losses on Personal-Use Assets

Losses from simply selling/disposing of personal-use property aren't deductible at all. Casualty losses (sudden/unexpected events like fire, storm, or theft) on personal-use property are also nondeductible **unless** tied to a federally declared disaster — in which case they're deductible subject to a $100 floor per casualty event, plus an overall 10%-of-AGI floor for the year.

### Other Itemized Deductions

Gambling losses/expenses are deductible as itemized deductions, but only up to gambling winnings for the year (winnings are still fully included in gross income — losses don't net directly against them). Also here: casualty/theft losses on *investment* property (as opposed to personal-use property), and the unrecovered cost basis of a life annuity when the annuitant dies before fully recovering their investment.

## The Standard Deduction

The standard deduction is a flat amount taxpayers can claim instead of itemizing — you take whichever is bigger. The amount depends on filing status, with extra add-ons for being 65+ or blind.

From the government's side, it serves two purposes: it shields a baseline amount of income from tax automatically (helping lower earners), and it removes the need to audit itemized deductions for anyone who takes the standard amount instead. From the taxpayer's side, it's simpler — no need to track and substantiate itemized expenses if you're not going to use them.

The catch: because the standard deduction is often quite large, it effectively "absorbs" itemized deductions up to its own amount — meaning itemized deductions only produce a real tax benefit once they exceed what the standard deduction already gives you for free.

### Bunching Itemized Deductions

Some taxpayers' itemized deductions consistently land just below the standard deduction, producing zero extra benefit year after year. The fix is a timing strategy called **bunching**: concentrate two years' worth of itemizable expenses (charitable giving is the classic example) into a single year — pushing that year's itemized total above the standard deduction — then take the standard deduction the following (lighter) year.

Since most individuals are cash-method taxpayers, this mainly works by accelerating discretionary payments (e.g., making December's and next January's charitable gift both in December). It's more limited for expenses with fixed due dates or automatic withholding (property tax deadlines, state tax withholding), but works well for genuinely discretionary items like charitable contributions.

## Deduction for Qualified Business Income

This is a **from-AGI** deduction, on top of the standard/itemized deduction, available to taxpayers with qualified business income (QBI) from a partnership, S corp, or sole proprietorship. It equals the **lesser of**:
- (a) 20% of QBI from a qualified trade or business (after the wage limit, discussed below) plus 20% of qualified REIT dividends and qualified PTP income, or
- (b) 20% of (taxable income minus net capital gains, including qualified dividends).

With multiple qualified businesses, the taxable-income limit applies to the *combined* QBI (after applying the wage limit separately to each business).

A **qualified trade or business** excludes being an employee and excludes "specified service trades or businesses" (SSTBs) — health, law, consulting, accounting, actuarial science, performing arts, athletics, financial/brokerage services, investment management, or any business where the main asset is the reputation/skill of its owners/employees. (Architecture and engineering are specifically carved *out* of the SSTB exclusion, so they still qualify.) Rental activity can qualify too, if it rises to the level of a genuine trade or business based on the facts.

For lower-income taxpayers, the SSTB exclusion doesn't apply at all: below $191,950 taxable income ($383,900 MFJ), an SSTB is still treated as a qualified business. Above that, the exclusion phases in over a $50,000 range ($100,000 MFJ), fully excluding SSTBs once taxable income exceeds $241,950 ($483,900 MFJ).

QBI itself is net qualified income/gain/deduction/loss from the qualifying business, excluding investment-type items (capital gains, dividends, interest not tied to the business). For self-employed taxpayers, QBI gets reduced by the deductible half of self-employment tax, the self-employed health insurance deduction, and retirement plan contributions. A net QBI loss carries forward to offset next year's QBI.

### Limitations

Once taxable income exceeds the same $191,950/$383,900 thresholds, a **wage-based limit** kicks in, capping the deduction at the greater of:
- (i) 50% of wages paid by the business, or
- (ii) 25% of wages paid, plus 2.5% of the unadjusted basis of qualified property in the business.

This wage limit is applied separately per business; for partners/S-corp shareholders, "wages" means their allocable share from the entity. Like the SSTB exclusion, it phases in ratably over the same $50,000/$100,000 range, fully applying above $241,950/$483,900.
