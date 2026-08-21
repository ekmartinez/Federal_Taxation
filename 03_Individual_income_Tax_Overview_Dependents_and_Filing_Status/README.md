# Individual Income Tax Overview, Dependents, and Filing Status

## Examples & Excercises

- [Examples](03_Individual_Income_Tax_Overview_Dependents_and_Filing_Status_Examples.ipynb)
- [Exercises](03_Individual_Income_Tax_Overview_Dependents_and_Filing_Status_Exercises.ipynb)
- [Comprehensive Problems](03_Individual_income_Tax_Overview_Dependents_and_Filing_Status_Exercises/Comprehensive_Problems/)

## Overview

This chapter walks through how an individual's tax liability actually gets built, step by step: from gross income down to taxable income, through credits and prepayments, to the final amount owed or refunded. It then covers two things that plug directly into that formula — who counts as a taxpayer's **dependent**, and what **filing status** a taxpayer uses — since both drive which tax rates, standard deduction, and credit thresholds apply.

## Table of Contents
- [The Individual Income Tax Formula](#the-individual-income-tax-formula)
  - [Gross Income](#gross-income)
  - [Character of Income](#character-of-income)
  - [Deductions](#deductions)
    - [For AGI Deductions](#for-agi-deductions)
    - [From AGI Deductions](#from-agi-deductions)
  - [Income Tax Calculation](#income-tax-calculation)
  - [Other Taxes](#other-taxes)
  - [Tax Credits](#tax-credits)
  - [Tax Prepayments](#tax-prepayments)
- [Dependents of the Taxpayer](#dependents-of-the-taxpayer)
  - [Dependency Requirements](#dependency-requirements)
  - [Qualifying Child](#qualifying-child)
    - [Relationship Test](#relationship-test)
    - [Age Test](#age-test)
    - [Residence Test](#residence-test)
    - [Support Test](#support-test)
    - [Tiebreaking Rules](#tiebreaking-rules)
  - [Qualifying Relative](#qualifying-relative)
    - [Relationship Test](#relationship-test-1)
    - [Support Test](#support-test-1)
    - [Gross Income Test](#gross-income-test)
    - [Dependents Summary](#dependents-summary)
- [Filing Status](#filing-status)
  - [Married Filing Jointly and Married Filing Separately](#married-filing-jointly-and-married-filing-separately)
  - [Married Individuals Treated as Unmarried (Abandoned Spouse)](#married-individuals-treated-as-unmarried-abandoned-spouse)
  - [Qualifying Surviving Spouse](#qualifying-surviving-spouse)
  - [Single](#single)
  - [Head of Household](#head-of-household)

---

## The Individual Income Tax Formula

Taxable income is the base the individual income tax is actually calculated on. The formula that gets you there:

```
        | Gross Income
Minus:  | For AGI (above the line) deductions
        | -----------------------------------
Equals: | Adjusted gross income (AGI)
Minus:  | From AGI (below the line) deductions:
        |    (1) Greater of:
        |        (a) Standard deduction or
        |        (b) Itemized deductions
        |    (2) Deduction for qualified business income
        | ------------------------------------------------
Equals: | Taxable income
Times:  | Tax rates
        | ---------------
Equals: | Income tax liability
Plus:   | Other taxes
        | --------------------
Equals: | Total tax
Minus:  | Credits
Minus:  | Prepayments
        | --------------------
Equals: | Tax due or (refund)
```

### Gross Income

U.S. tax law runs on the **all-inclusive income concept** — basically, everything you realize as income is taxable unless a specific rule says otherwise. "**Realized**" income generally means income from a transaction with another party where property rights measurably changed hands.

Two carve-outs from the default "everything's taxable" rule:
- **Exclusions** — income that's permanently off the tax base (never taxed).
- **Deferrals** — income that's still taxable, just not until a later year.

**Common income items and their character:**

| Income Item | Character |
| --- | :---: |
| Compensation for services including fringe benefits | Ordinary |
| Business income | Ordinary |
| Gains from selling property | Ordinary or capital |
| Interest and dividends | Ordinary or qualified dividend |
| Rents and royalties | Ordinary |
| Alimony received (pre-2019 decree) and annuities | Ordinary |
| Retirement income | Ordinary |
| Income from the discharge of indebtedness | Ordinary |

**Common exclusions and deferrals:**

| Exclusion or Deferral Item | Exclusion or Deferral |
| --- | :---: |
| Interest income from municipal bonds | Exclusion |
| Gifts and inheritance | Exclusion |
| Alimony received (post-2018 decree) | Exclusion |
| Gain on sale of personal residence | Exclusion |
| Life insurance proceeds | Exclusion |
| Installment sale | Deferral |
| Like-kind exchange | Deferral |

### Character of Income

Not all gross income is taxed the same way — the **character** of the income (its type, for tax purposes) matters just as much as the amount.

- **Ordinary income** — taxed at the standard tax rate schedules.
- **Capital gain/loss** — gain or loss from selling a *capital asset*. A capital asset is basically anything that isn't: (1) receivables from selling goods/services, (2) inventory/goods held for sale, or (3) assets used in the trade or business itself. So capital assets end up being things like personal-use property (your car, your house) and investment assets (stocks, bonds).

Whether a capital gain/loss is **long-term** (held over a year) or **short-term** (held a year or less) matters a lot. When counting the holding period, the day you *bought* doesn't count, but the day you *sold* does. At year-end, taxpayers net all their long-term gains/losses together, then all their short-term ones together. If both groups land on the same sign (both gains or both losses), you're done. If they land on opposite signs, you net the two groups against each other, and the character (long- or short-term) of the final result follows whichever group had the larger absolute value.

A few consequences of this netting:
- Up to $3,000 of net capital loss ($1,500 if married filing separately) is deductible for the year, as a for-AGI deduction. Anything beyond that limit carries forward to next year.
- Net short-term gains are taxed like ordinary income.
- Net long-term gains ("net capital gains") get preferential, lower rates.

**2026 Long-Term Capital Gains rate brackets:**

| LTCG Tax | Single Filers | Married Filing Jointly | Head of Household | Married Filing Separately | Estates & Trusts |
| --- | --- | --- | --- | --- | --- |
| 0% | 49,450 or < | 98,900 or < | 66,200 or < | 49,450 or < | 3,300 or < |
| 15% | > 49,450 and < 545,500 | > 98,900 and < 613,700 | > 66,200 and < 579,600 | > 49,450 and < 306,850 | > 3,300 and < 16,250 |
| 20% | 545,500 or > | 613,700 or > | 579,600 or > | 306,850 or > | 16,250 or more |
*(2026 figures)*

**Qualified dividends** get the same preferential rate as net long-term capital gains, but they're a separate category — they don't get folded into the capital gain/loss netting process. Dividends that don't meet the "qualified" requirements are just taxed as ordinary income.

### Deductions

Unlike income (which is taxable by default), **deductions only exist because a specific law grants them** — they're a matter of legislative grace, not a default right. The tax code splits deductions into two buckets, and which bucket a deduction falls into is set by the law that creates it:

- **For AGI deductions** ("above the line") — reduce AGI directly, and are generally worth more, since AGI is the trigger point for a lot of other phase-outs and thresholds (child tax credit, education credits, etc.).
- **From AGI deductions** ("below the line") — subtracted *after* AGI is already determined, to get to taxable income.

#### For AGI Deductions

These tend to be business- and investment-related. Common examples:

| For AGI Deduction |
| --- |
| Alimony paid (pre-2019 decree) |
| Health insurance deduction for self-employed taxpayers |
| Rental and royalty expenses |
| Net capital losses [limited to 3,000 (1,500 MFJ)] |
| One-half of self-employment taxes paid |
| Business expenses |
| Losses on dispositions of assets used in a trade or business |
| Contributions to qualified retirement accounts |

#### From AGI Deductions

This bucket includes the standard deduction, itemized deductions, and the qualified business income (QBI) deduction. You take whichever is larger: the standard deduction, or your total itemized deductions.

**Main itemized deduction categories:**
- **Medical/dental** — only the portion exceeding 7.5% of AGI.
- **Taxes** — state/local income tax, sales tax, real estate tax, personal property tax, etc. (capped at a combined $10,000/year, $5,000 if MFS — excludes foreign income tax).
- **Interest expense** — mortgage and investment interest.
- **Charitable contributions**.
- **Miscellaneous** — e.g., gambling losses, capped at gambling winnings.

**2026 standard deduction amounts:**

| Filing Status | Standard Deduction |
| --- | ---: |
| Single | 16,100 |
| Married filing jointly and Qualifying Widow | 32,200 |
| Married Filing Separately | 16,100 |
| Head of Household | 24,150 |
| Enhanced deduction for seniors (per individual) | up to 6,000 |

The standard deduction also gets bumped up for age/blindness: +$1,650 per married taxpayer who's 65+ or blind ($3,300 if both), or +$2,050 for a single taxpayer who's 65+ or blind ($4,100 if both).

### Income Tax Calculation

Once taxable income is known, you look up the actual tax liability using either a tax table or a tax rate schedule, depending on filing status and income level.

### Other Taxes

Beyond the regular income tax, individuals may owe additional taxes on different bases entirely — most notably the alternative minimum tax (AMT) and self-employment tax. High earners (above certain AGI thresholds) also owe an extra 3.8% net investment income tax on unearned income and an extra 0.9% Medicare tax on earned income.

### Tax Credits

Credits are also a matter of specific legislative grant (like deductions), but they work differently: a deduction only saves you your marginal rate times the deduction amount, while a **credit reduces the tax bill dollar-for-dollar**. That makes credits generally more valuable than an equal-sized deduction.

Common credits: Child Tax Credit, Child and Dependent Care Credit, Earned Income Credit, American Opportunity Credit, Lifetime Learning Credit — most phase out at higher income levels. The Child Tax Credit is the big one: $2,000 per qualifying child under 17, plus a smaller $500 credit for other dependents who don't meet the full qualifying-child criteria.

### Tax Prepayments

After credits are applied, the final step is subtracting what's already been prepaid:
1. Withholding from wages/other income.
2. Estimated tax payments made during the year.
3. Prior-year overpayment applied forward instead of refunded.

If prepayments exceed the remaining tax owed, you get a refund (or apply it forward). If prepayments fall short, you owe the difference — plus possibly an underpayment penalty.

## Dependents of the Taxpayer

There's no longer a deduction for claiming a dependent, but dependent status still matters — it feeds into filing status, credit eligibility, and other calculations.

### Dependency Requirements

To be someone's dependent, a person must:
1. Be a U.S. citizen, or a resident of the U.S., Canada, or Mexico.
2. Not file a joint return with a spouse (unless that joint return and each separate return would owe zero tax anyway).
3. Qualify as either a **qualifying child** or a **qualifying relative**.

The qualifying relative category is broader than qualifying child, even though the two overlap somewhat.

### Qualifying Child

Four tests all must be met:

#### Relationship Test
Must be an eligible relative — a child (including adopted, step, or foster) or descendant of a child, or a sibling (including half- and step-siblings) or descendant of a sibling. This reaches further than it might sound — a grandchild qualifies, and so does a sister's grandchild.

#### Age Test
Must be younger than the taxpayer, and either under 19 at year-end, or under 24 at year-end *and* a full-time student (in school full-time for some part of at least 5 months in the year). Permanently and totally disabled individuals meet this test regardless of age.

#### Residence Test
Must share the taxpayer's main home for more than half the year. Temporary absences (illness, school, etc.) still count as "living at home."

#### Support Test
The child must not have covered more than half of their *own* support for the year. "Support" is broadly defined — food, clothing, medical/dental care, child care, recreation, allowances, lodging, education, even wedding costs. Scholarships are excluded when evaluating a full-time student's support.

#### Tiebreaking Rules
When a person could qualify as a dependent to more than one taxpayer:
1. Parent beats non-parent.
2. Between two parents, whoever the child lived with longer wins (with a special override letting the noncustodial parent claim the child if the custodial parent signs a release). If time is exactly equal, the parent with the higher AGI wins.
3. Between two non-parents, higher AGI wins.

### Qualifying Relative

Someone who isn't a qualifying child can still be a dependent if they pass three tests:

#### Relationship Test
Broader than the qualifying-child version. Satisfied either by a **qualifying family relationship** (descendant/ancestor, sibling — including step-siblings, a niece/nephew via a sibling, an aunt/uncle, or an in-law) **or** by simply living in the taxpayer's household as a member of it for the entire year, family relationship or not.

#### Support Test
The taxpayer must provide *more than half* of this person's support (a stricter standard than the qualifying-child support test). Scholarships are still excluded for full-time student children. A **multiple support agreement** lets a group of people who collectively provide over half the support — but where no single person provides more than half — designate one of them (who contributed over 10%) to claim the dependent, as long as everyone else who contributed over 10% signs off (Form 2120). This comes up a lot with siblings jointly supporting an aging parent.

#### Gross Income Test
The dependent's own gross income must be under $5,200 (2026).

#### Dependents Summary
Key differences between the two categories:
- Relationship rules are broader for qualifying relatives.
- Age restrictions apply only to qualifying children.
- Gross income limits apply only to qualifying relatives.
- For a qualifying child, the child just can't fund more than half of their *own* support; for a qualifying relative, the taxpayer must fund more than half of *their* support.
- Only qualifying children face a residence requirement.

One more wrinkle: a person who is themselves a dependent can't claim any dependents of their own.

## Filing Status

Filing status is based on marital status at year-end plus dependent situation, and it drives: the applicable rate schedule, the standard deduction amount, and the AGI thresholds for various credit/deduction phase-outs.

Five possible statuses: married filing jointly, married filing separately, qualifying surviving spouse, single, and head of household.

### Married Filing Jointly and Married Filing Separately

Marital status is locked in as of the last day of the year (a surviving spouse who hasn't remarried is still treated as married in the year the other spouse died). Joint filers combine income/deductions and share joint-and-several liability for the resulting tax bill — both spouses are on the hook.

Filing **separately** means each spouse reports only their own income and deductions. To prevent separate filing from being used to game combined benefits, MFS numbers (rate brackets, standard deduction, etc.) are generally just half of MFJ numbers, and if one spouse itemizes, the other is forced to itemize too (even if the standard deduction would've been bigger for them). Net result: filing separately rarely makes sense purely for tax savings — but it can make sense for non-tax reasons, like not wanting liability for a spouse's tax situation, or being estranged.

### Married Individuals Treated as Unmarried (Abandoned Spouse)

Sometimes a couple is legally married at year-end but living apart, and joint filing isn't appealing since each spouse would be on the hook for the other's reported (or unreported) income. Normally the only other option would be the less favorable MFS status — but there's relief available.

A taxpayer can be treated as **unmarried** for filing purposes if all of the following hold:
- Still married at year-end (not legally separated).
- Doesn't file jointly with the spouse.
- Pays more than half the cost of maintaining a home that's the main residence of a dependent child (biological, adopted, step, or foster) for more than half the year.
- Lived apart from the spouse for the last six months of the year (temporary absences like school, illness, business, or military service don't break this).

Meeting these conditions also qualifies the taxpayer for head of household status. This provision — commonly called **abandoned spouse** treatment — exists mainly to help someone left caring for a child after separation, but it applies regardless of whether an actual "abandonment" occurred (e.g., a mutual separation). It's even possible for both spouses to independently qualify in the same year.

### Qualifying Surviving Spouse

After a spouse's death, a taxpayer is no longer legally married — but for up to two years following the year of death, they may still qualify for **qualifying surviving spouse** status if they (1) remain unmarried and (2) pay over half the cost of maintaining a home where a dependent child lived the entire year. The child must be the taxpayer's own child or stepchild (foster children don't count here).

### Single

The default status for unmarried taxpayers who don't meet the head of household requirements.

### Head of Household

Sits between MFJ/qualifying surviving spouse (more favorable) and MFS/single (less favorable) in terms of rates and standard deduction. Requirements:
- Unmarried at year-end (or treated as such under the abandoned-spouse rule).
- Not a qualifying surviving spouse.
- Pays more than half the cost of maintaining the home for the year.
- Has a "qualifying person" living with them more than half the year — except a dependent parent doesn't actually need to live with the taxpayer.

A few extra wrinkles:
- The same qualifying person can't support head of household status for more than one taxpayer.
- A dependent claimed only through a multiple support agreement doesn't count as a qualifying person here.
- A custodial-parent release letting the noncustodial parent claim the dependency exemption is ignored for head of household purposes — the child still counts as the custodial parent's qualifying person.
