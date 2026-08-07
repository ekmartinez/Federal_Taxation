# Tax Planning Strategies & Limitations — Notes

*Personal notes based on my textbook reading, rewritten in my own words.*

## Table of Contents
- [Overview](#overview)
- [Timing Strategies](#timing-strategies)
- [Income Shifting](#income-shifting)
- [Conversion Strategies](#conversion-strategies)
- [Judicial Doctrines (Anti-Abuse Rules)](#judicial-doctrines-anti-abuse-rules)
- [Tax Avoidance vs. Tax Evasion](#tax-avoidance-vs-tax-evasion)

---

## Overview

The goal of tax planning isn't just to pay less tax — it's to **maximize after-tax wealth**, which sometimes means accepting a higher tax bill in exchange for a better *non-tax* outcome (e.g., liquidity, risk reduction, personal goals). You have to weigh both the tax and non-tax costs/benefits of a transaction, not just the tax line.

There are three basic levers for tax planning:

1. **Timing** — accelerate or defer income and deductions.
2. **Income shifting** — move income from a taxpayer in a high bracket to one in a low bracket.
3. **Conversion** — change the *character* of income/expense so it gets better tax treatment.

---

## Timing Strategies

The core idea: *when* income is taxed or an expense is deducted changes its present value — money today is worth more than the same amount later (time value of money).

**Rule of thumb:**
- For cash **inflows** → prefer a higher present value (get it sooner, or push the *tax* on it later).
- For cash **outflows** (like taxes) → prefer a lower present value (pay later if possible).

### When tax rates stay constant

Two straightforward moves:
- **Accelerate deductions** — take the deduction now, not later, since the tax savings are worth more today. The trick is to accelerate the *deduction* without necessarily accelerating the actual cash spent (e.g., depreciation, LIFO vs. FIFO, prepaid expense deductions). This matters a lot for large corporations, so tax planners spend real effort optimizing recognition timing.
- **Defer income** — push recognition to a later year so the tax owed has a lower present value. This shows up in accounting method choice (cash vs. accrual), billing timing, depreciation method choice, and retirement/investment planning generally.

These strategies matter more when: tax rates are higher, rates of return are higher, the transaction is larger, or you actually have flexibility to shift timing.

### When tax rates change

Now you also need to think about *which* rate applies in which year:
- Take deductions in **high-rate** years (bigger tax savings).
- Recognize income in **low-rate** years (lower tax cost).

### Limits on timing strategies

- Deferral generally requires staying invested — if you cash out, you usually can't defer.
- Deferral isn't smart if: you're cash-strapped, the investment's return is weak relative to alternatives, or staying in adds unnecessary risk.
- The **constructive receipt doctrine** limits how much cash-basis taxpayers can defer income — if you had access to the income, the IRS can treat it as received even if you didn't formally take it.

---

## Income Shifting

Since tax rates differ across people and jurisdictions, you can sometimes shift income to a lower-taxed party (or shift deductions to a higher-taxed party) and reduce the group's total tax bill. Works best between:

- Related parties (family, or owners and their businesses) willing to cooperate as a group.
- Taxpayers operating across multiple jurisdictions with different rates.

### Family members

Classic case: high-bracket parents want to shift income to low-bracket kids. Limitations:

- **Assignment of income doctrine** — income is taxed to whoever actually *earns* it. You can't just relabel your paycheck as your kid's income; the shift only works if the other person genuinely earns it.
- Paying a child through the family business (e.g., a token wage for minimal work) is one workaround, but the IRS scrutinizes related-party transactions closely, since unlike arm's-length deals, family members have every incentive to structure things purely for tax benefit rather than real economic terms.
- Shifting *investment* income to a child requires actually transferring ownership of the asset — most parents aren't willing to give that up.

### Owners and their businesses

- **Sole proprietorships**: no benefit to shifting — it's all reported on the owner's personal return either way.
- **C corporations**: shifting *can* help, since the corporation is a separate taxable entity with its own rate. To move income from the corporation to the owner, the corporation needs a deduction to match — common methods: paying compensation (deductible to the corp, taxable to the owner), or having the owner rent property or lend money to the corporation (again: deduction for the corp, income for the owner).
- **Dividends don't work for this** — they aren't deductible by the corporation, so paying them creates double taxation (taxed at the corporate level, then again to the shareholder). Not an efficient shifting tool.

### Across jurisdictions (states/countries)

Same idea, applied to transfer pricing between jurisdictions with different rates. Limitations:

- Tax authorities actively watch for this — the IRS scrutinizes international transfer pricing, and states watch interstate transactions between related parties.
- Moving to a low-tax jurisdiction can carry **implicit taxes** (indirect costs of being in that jurisdiction).
- There can be reputational/publicity costs to visibly moving jobs/operations offshore or out of state, which can outweigh the tax savings.

---

## Conversion Strategies

Different types of income get different tax treatment:
- Ordinary income (salary, interest, business income) → taxed at ordinary rates.
- Long-term capital gains and qualified dividends → lower preferential rates (up to ~20%, generally).
- Some income (municipal bond interest, certain benefits) → tax-exempt entirely.

Same logic applies to expenses — business expenses are usually fully deductible, investment-related deductions are often limited, and personal expenses are usually not deductible at all.

**Conversion strategy** = restructuring income or expenses so they fall into the more favorably-taxed category. Examples: changing the character of income/deductions, choosing investments taxed at better rates, structuring compensation to be non-taxable rather than taxable.

To evaluate this, compare **after-tax** returns rather than pre-tax returns:

```
After-Tax Rate of Return = Pre-Tax Rate of Return × (1 − Marginal Tax Rate)
```

Holding an investment over a year often combines both the timing *and* conversion strategies at once: you defer the gain until sale (lower present value of the eventual tax) *and* that gain may qualify for the lower long-term capital gains rate.

For comparing investments across different holding periods, use the **annualized after-tax return**: (FV/I)^(1/n) − 1, where FV = after-tax future value, I = after-tax dollars invested, n = number of periods.

### Limits on conversion

The tax code has specific anti-conversion provisions, e.g.:
- Depreciation recapture rules (claw back some of the benefit of prior deductions on sale).
- Luxury auto depreciation caps.
- Implicit taxes can eat into or wipe out the benefit of tax-preferred investments.

---

## Judicial Doctrines (Anti-Abuse Rules)

Beyond the written tax code, courts have developed doctrines the IRS can invoke when it suspects a transaction exists purely to dodge tax:

- **Business Purpose Doctrine** — the IRS can disallow deductions for transactions that have no real business rationale behind them.
- **Step-Transaction Doctrine** — the IRS can treat a series of individually-structured steps as a single combined transaction if that's the real substance of what happened.
- **Substance-Over-Form Doctrine** — the IRS looks at what a transaction *actually* is, economically, rather than how it's formally labeled or structured, and can recharacterize it accordingly.
- **Economic Substance Doctrine** — for a transaction to get its claimed tax benefits, it needs to (1) meaningfully change the taxpayer's economic position aside from the tax effect, and (2) have a real non-tax purpose.

---

## Tax Avoidance vs. Tax Evasion

- **Tax avoidance** = legally arranging your affairs to minimize tax (e.g., municipal bonds). Courts and Congress have long accepted this — you're not morally obligated to pay more than the law requires (see *Commissioner v. Newman*).
- **Tax evasion** = willfully defrauding the government. This is illegal and can lead to federal prison — a completely different category from avoidance.
