# Introduction to Tax — Notes

## Examples & Excercises

- [Examples](01_An_Introduction_to_Tax_Examples.ipynb)
- [Exercises](01_An_Introduction_to_Tax_Exercises.ipynb)

## Overview

This chapter lays the groundwork for everything else in tax planning: what actually counts as a "tax," how to calculate one, the different ways to measure a tax rate, the three basic rate structures (proportional, progressive, regressive), a survey of the major federal/state/local taxes, and finally a framework for judging whether a tax system is any good (sufficiency, equity, certainty, convenience, economy).

## Table of Contents
- [What Qualifies As A Tax](#what-qualifies-as-a-tax)
- [How To Calculate a Tax](#how-to-calculate-a-tax)
- [Different Ways To Measure Tax Rates](#different-ways-to-measure-tax-rates)
- [Tax Rate Structures](#tax-rate-structures)
  - [Proportional Tax Rate Structure](#proportional-tax-rate-structure)
  - [Progressive Tax Rate Structure](#progressive-tax-rate-structure)
  - [Regressive Tax Rate Structure](#regressive-tax-rate-structure)
- [Types of Taxes](#types-of-taxes)
  - [Federal Taxes](#federal-taxes)
    - [Income Tax](#income-tax)
    - [Employment and Unemployment Taxes](#employment-and-unemployment-taxes)
    - [Excise Taxes](#excise-taxes)
  - [State and Local Taxes](#state-and-local-taxes)
    - [Income Taxes](#income-taxes)
    - [Sales and Use Taxes](#sales-and-use-taxes)
    - [Property Taxes](#property-taxes)
  - [Implicit Taxes](#implicit-taxes)
- [Evaluating Alternative Tax Systems](#evaluating-alternative-tax-systems)
  - [Sufficiency](#sufficiency)
  - [Equity](#equity)
  - [Certainty](#certainty)
  - [Convenience](#convenience)
  - [Economy](#economy)
  - [Trade-Offs](#evaluating-tax-systems--the-trade-offs)

---

## What Qualifies As A Tax?

A **tax** is a mandatory payment to the government that isn't tied to a specific benefit received in return — it's not a fee-for-service. Its main job is raising revenue to fund government operations. That distinguishes it from a fine or penalty, which exists to punish or deter, not to fund anything.

That said, the tax system does shape behavior indirectly: deductions incentivize things like charitable giving, retirement saving, and R&D, while "sin taxes" (alcohol, tobacco) discourage certain consumption through higher surcharges.

**Three defining features of a tax:**
- Mandatory, not voluntary.
- Imposed by a government (federal, state, or local).
- Not directly tied to a specific benefit the payer receives.

Even though a given tax isn't earmarked to a specific service, taxpayers collectively benefit from what taxes fund — defense, courts, law enforcement, infrastructure, public schools, etc. An **earmarked tax** is the exception: it's designated for a specific purpose (e.g., a 1% local sales tax dedicated to education funding).

## How to Calculate a Tax

The basic formula:

```
Tax = Tax Base × Tax Rate
```

- **Tax base** = what's actually being taxed, expressed in dollars (e.g., taxable income, purchase amount, property value).
- **Tax rate** = the percentage applied to that base.

Governments use many different tax bases: income (income tax), purchases (sales tax), real estate value (property tax), personal property value, etc.

A tax base isn't always taxed at one uniform rate. A **flat tax** applies a single rate to the entire base. A **graduated tax** splits the base into brackets, each taxed at a different (usually increasing) rate.

## Different Ways To Measure Tax Rates

Three distinct rate concepts that matter for comparing tax structures:

- **Marginal tax rate** — the rate applied to the *next* dollar of income (or the rate on a specific incremental change in income/deductions). This is the most useful rate for planning purposes, since it tells you the actual tax cost/benefit of an additional transaction.

  ```
  Marginal Tax Rate = Change in Tax / Change in Taxable Income
  ```

- **Average tax rate** — total tax paid divided by total taxable income. Useful for budgeting — i.e., what fraction of taxable income actually goes to tax.

  ```
  Average Tax Rate = Total Tax / Taxable Income
  ```

- **Effective tax rate** — total tax paid divided by *total* income, including nontaxable income. This gives the most realistic picture of a taxpayer's overall burden, since it accounts for income the tax base doesn't even capture.

  ```
  Effective Tax Rate = Total Tax / Total Income
  ```

## Tax Rate Structures

Three basic patterns for how the rate behaves as the base grows:

### Proportional Tax Rate Structure

Also called a flat tax — the rate stays constant no matter how large the base gets, so tax owed scales proportionally with the base. Because the rate never changes, marginal rate = average rate here.

```
Proportional Tax = Tax Base × Tax Rate
```

### Progressive Tax Rate Structure

The marginal rate *increases* as the base grows (the classic bracket system — U.S. federal income tax and most state income taxes work this way). Under this structure, the average rate is always ≤ the marginal rate.

### Regressive Tax Rate Structure

The marginal rate *decreases* as the base grows. Social Security tax and federal/state unemployment taxes work this way in the U.S.

Some taxes are only regressive when you look past the stated rate to the *effective* burden. Sales tax, for example, is technically proportional (same rate regardless of purchase amount) — but since lower earners tend to spend a larger share of their total income on taxable purchases, the effective burden falls more heavily on them as income drops. So in practice, it behaves regressively.

## Types of Taxes

### Federal Taxes

The federal government funds things like defense, Social Security, highways, and Medicare mainly through income taxes, corporate taxes, employment taxes, estate/gift taxes, and excise taxes.

#### Income Tax

The single biggest source of federal revenue — roughly 51% of total federal tax collections in FY2022. Current top rates: 37% for individuals, estates, and trusts; a flat 21% for corporations. High earners also pay an extra 3.8% tax on net investment income.

#### Employment and Unemployment Taxes

The second-largest federal tax category.

- **Social Security tax (OASDI)** — funds retirement, survivor, and disability benefits. 12.4% total, split 6.2%/6.2% between employer and employee. For 2024, only wages up to $168,600 are subject to this tax (no cap on Medicare).
- **Medicare tax (MHI)** — funds medical insurance for elderly/disabled individuals. 2.9% total, split 1.45%/1.45%. No wage cap. High earners pay an additional 0.9% on income above a threshold.
- Self-employed people pay both halves themselves — this combined liability is the **self-employment tax**.
- **Unemployment taxes** fund benefits for workers laid off through no fault of their own. The federal version (FUTA) is 6.0% on the first $7,000 of each employee's wages, but employers typically get up to a 5.4% credit for state unemployment tax paid, bringing the effective FUTA rate down to as low as 0.6%.

#### Excise Taxes

Levied on the sale of specific goods/services, and unlike most taxes, the base is usually a *quantity* rather than a dollar amount. Common examples: alcohol, tobacco, gasoline, diesel, airline tickets, tanning services. The producer/seller technically pays these to the government, but the cost gets built into the price, so consumers bear it even though they rarely see it as a separate line item.

Federal **estate and gift taxes** are smaller in total revenue but can be significant for wealthy individuals. Both are based on fair market value of transferred wealth (at death or by gift). Current max rate: 40%. Most people never owe these thanks to generous exclusions — a $18,000/year per-recipient gift exclusion, and a $13,610,000 (2024) lifetime unified credit covering both gifts and bequests. Only very wealthy estates actually get taxed.

### State and Local Taxes

States and localities fund things like schools, roads, and police/fire through income tax, sales/use tax, excise tax, and property tax. States lean most heavily on income and sales tax; localities lean on sales and property tax.

#### Income Taxes

Most states (plus D.C.) tax individuals and corporations that live/operate or earn income there, requiring a separate state return alongside the federal one. State taxable income calculations generally start from the federal calculation (California is a notable exception, with many of its own adjustments). State rates are much lower than federal rates. Some cities (e.g., NYC) layer on their own local income tax too.

#### Sales and Use Taxes

- **Sales tax** — based on the retail price of goods/some services; collected by the retailer at the point of sale.
- **Use tax** — applies to goods used/owned/consumed in-state that weren't purchased in-state (e.g., bought tax-free from an out-of-state seller). It exists to stop people from dodging sales tax by shopping outside the state, and it levels the playing field for local retailers who otherwise have a competitive disadvantage.
- States generally give residents a credit for sales tax already paid elsewhere, so you're not double-taxed on the same purchase.

#### Property Taxes

Two flavors, both **ad valorem** (based on fair market value), both usually assessed annually:

- **Real property tax** — land, buildings, permanent improvements.
- **Personal property tax** — everything else. Tangible examples: cars, boats, planes, business inventory/equipment. Intangible examples (stocks, bonds, IP) technically exist as a category, but no state actually taxes intangible personal property in practice.

### Implicit Taxes

Everything above is an **explicit tax** — directly imposed and easy to measure. An **implicit tax** is different: it's not paid to any government directly. Instead, it's the *reduced pre-tax return* an asset produces because it's tax-advantaged.

The logic: when an asset gets favorable tax treatment (income excluded from tax, a lower rate, or big deductions), demand for that asset rises. Higher demand pushes the asset's price up, which mechanically lowers its pre-tax rate of return. That built-in return reduction *is* the implicit tax — investors are effectively "paying" for the tax break through a lower yield, even though no check goes to the IRS.

## Evaluating Alternative Tax Systems

Five criteria for judging whether a tax system is well-designed: sufficiency, equity, certainty, convenience, and economy.

### Sufficiency

Does the system actually raise enough revenue to cover government spending? Sounds simple in theory (estimate spending, design a system to match) but is genuinely hard in practice, because both expenditures and taxpayer behavior are difficult to predict — especially when the tax law itself changes.

- **Static forecasting** — projects revenue assuming taxpayers *don't* change behavior in response to a law change. Simple, but can be way off if people do react.
- **Dynamic forecasting** — tries to account for behavioral responses. More realistic in principle, but only as good as the assumptions baked in — not a guarantee of accuracy.

Two competing behavioral predictions matter here:
- **Income effect** — taxed more → people work *harder* to maintain the same after-tax income.
- **Substitution effect** — taxed more → people shift toward untaxed activities (like leisure) since taxable work now has less marginal value.

### Equity

This is about fairness — specifically, whether tax burden tracks ability to pay. Fairness is inherently subjective, so this is the most debated criterion.

- **Horizontal equity** — similarly-situated taxpayers should pay the same tax. Looks true at a glance, but breaks down on closer inspection: two people with identical income don't pay the same tax if one earns it as salary and the other as tax-exempt muni bond interest or capital gains; two people with equal purchases pay different sales tax depending on the mix of goods bought (e.g., groceries taxed lower); farmland gets preferential property tax treatment; charitable/spousal bequests escape estate tax. These gaps exist because of deliberate tax preferences — carve-outs designed to encourage specific behavior or social goals.
- **Vertical equity** — people with greater ability to pay should pay more. Two different lenses on what "more" means: flat-tax/sales-tax advocates argue it's satisfied as long as higher earners pay more total dollars (which happens automatically even at a constant rate); progressive-tax advocates argue true vertical equity requires a *higher rate* for higher earners, since a flat rate is a proportionally heavier burden on people with less income to spare.

### Certainty

Can taxpayers clearly know when, where, and how much to pay? Sales tax, property tax, and excise tax score well here — they're calculated automatically and collected at the point of transaction, no return required. Income tax is the opposite case: what counts as taxable income, what's deductible, when to recognize it — these get genuinely complicated for business owners and investors, and yearly law changes make it worse.

### Convenience

Good tax systems collect revenue at the point where it's easiest for both sides — ideally tied directly to the transaction that generates the tax. Sales tax collected at checkout, income/Social Security tax withheld straight from paychecks — both minimize the chance of evasion and administrative friction. When withholding isn't enough (e.g., self-employed taxpayers), quarterly estimated payments fill the gap: individuals pay April 15, June 15, September 15, and January 15; corporations pay the 15th of the 3rd, 6th, 9th, and 12th months of their fiscal year.

### Economy

How much does the system cost to comply with and administer, for both the government and the taxpayer?

- From the **government's side**, most U.S. taxes are cheap to run — the entire IRS budget is roughly a third of a percent of what it collects, which is low compared to typical collection-agency costs.
- From the **taxpayer's side**, it varies a lot. Sales tax, excise tax, and property tax impose minimal burden (retailers do the heavy lifting; out-of-state sellers do complain about the compliance burden of collecting use tax across many jurisdictions). Income tax is the clear outlier — record-keeping, accountants, and attorneys can add up to real money for taxpayers with complex situations.

### Evaluating Tax Systems — The Trade-Offs

The recurring tension across all these criteria really boils down to **simplicity vs. fairness**. Simple-to-administer taxes (like sales tax) tend to be viewed as less fair; fairer-feeling taxes (like the progressive income tax) tend to be more complex to administer. You generally can't maximize both at once.
