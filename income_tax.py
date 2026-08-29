import calendar
import pandas as pd
from datetime import date

class IncomeTax:
    def __init__(self, status, age, gross_income):
        self.status = status
        self.age = age
        self.gross_income = gross_income

        """
        Tax year: 2025
        "SNG": Single
        "MFJ": Married Filing Jointly
        "MFS": Married Filing Separately
        "QSS": Qualifiying Surviving Spouse
        "HOH": Head of Household
        """
        self.standard_deduction = {
            "SNG": 15750, 
            "MFJ": 31500, 
            "MFS": 15750, 
            "QSS": 31500, 
            "HOH": 23625, 
        }

        self.preferential = {
            "rates": [0, .15, .20],

            "SNG": [0, 48350, 533400], 
            "MFJ": [0, 96700, 600050], 
            "MFS": [0, 48350, 300000], 
            "QSS": [0, 96700, 600050], 
            "HOH": [0, 64750, 566700], 
        }

        self.ordinary = {
            "rates": [.10, .12, .22, .24, .32, .35, .37],

            "SNG": [[0, 11925, 48475, 103350, 197300, 250525, 626350],   # Limits
                    [0, 1192.50, 5578.50, 17651, 40199, 57231, 188769.75]], # Pay this amount

            "MFJ": [[0, 23850, 96950, 206700, 394600, 501050, 751600 ],  
                    [0, 2385, 11157, 35302, 80398, 114462, 202154.5]], 

            "MFS": [[0, 11925, 48475, 103350, 197300, 250525, 375800],
                    [0, 1192.50, 5578.50, 17651, 40199, 57231, 101077.25]],

            "QSS": [[0, 23850, 96950, 206700, 394600, 501050, 751600 ],  
                    [0, 2385, 11157, 35302, 80398, 114462, 202154.5]], 
            
            "HOH": [[0, 17000, 64850, 103350, 197300, 250500, 626350], 
                    [0, 1770, 7740, 16155, 39207, 56631, 191171]],
        }

class OrdinaryIncomeTax(IncomeTax):
    def __init__(self, status, age, gross_income, adjustments, itemized, qbi_deduction):
        super().__init__(status, age, gross_income)
        self.adjustments = adjustments
        self.itemized = itemized
        self.qbi_deduction = qbi_deduction
        self.rates = self.ordinary["rates"]
        self.schedule = self.ordinary[self.status]

        self.from_agi_deduction = max(self.itemized, self.standard_deduction[self.status])

    def calculate_tax(self):
        tax_rate = 0
        ordinary_tax = 0
        adjusted_gross_income = self.gross_income - self.adjustments
        taxable_income = adjusted_gross_income - self.from_agi_deduction - self.qbi_deduction

        data_return = {
            "status": self.status,
            "age": self.age,
            "gross_income": self.gross_income,
            "adjustments": self.adjustments,
            "standard_deduction": self.standard_deduction[self.status], # type: ignore
            "itemized_deduction": self.itemized,
            "deduction": self.from_agi_deduction,
            "qbi_deduction": self.qbi_deduction,
            "marginal_tax_rate": tax_rate,
            "ordinary_tax": ordinary_tax,
        }

        data_return["adjusted_gross_income"] = self.gross_income - self.adjustments
        data_return["taxable_income"] = data_return["adjusted_gross_income"] - self.from_agi_deduction - self.qbi_deduction
        
        for k, v in enumerate(self.schedule[0]):
            if taxable_income < self.schedule[0][0]:
                break
            elif taxable_income > self.schedule[0][6]:
                excess = taxable_income - self.schedule[0][6]
                tax_rate = self.rates[6]
                data_return["marginal_tax_rate"] = tax_rate
                pay = self.schedule[1][6]
                data_return["ordinary_tax"] = pay + (excess * tax_rate)  

            elif taxable_income > v and taxable_income <= self.schedule[0][k+1]:
                excess = taxable_income - v
                tax_rate = self.rates[k]
                data_return["marginal_tax_rate"] = tax_rate
                pay = self.schedule[1][k]
                data_return["ordinary_tax"] = pay + (excess * tax_rate)
        
        return data_return

class PreferentialIncomeTax(IncomeTax):
    """Handles preferential treatment of capital gains and dividends"""
    def __init__(self, status, age, gross_income, dividends, capital_gains):
        super().__init__(status, age, gross_income)
        self.dividends = dividends
        self.capital_gains = capital_gains

        self.rates = self.preferential["rates"]
        self.schedule = self.preferential[self.status]

    def calculate_tax(self):
        capital_gains_rate = 0
        capital_gains_tax = 0

        if self.gross_income >= self.schedule[0] and self.gross_income <= self.schedule[1]:
            capital_gains_rate = self.rates[0]
            capital_gains_tax = self.capital_gains * self.rates[0]
        elif self.gross_income > self.schedule[1] and self.gross_income <= self.schedule[2]:
            capital_gains_rate = self.rates[1]
            capital_gains_tax = self.capital_gains * self.rates[1]
        elif self.gross_income > self.schedule[2]:
            capital_gains_rate = self.rates[2]
            capital_gains_tax = self.capital_gains * self.rates[2]

        return [capital_gains_rate, capital_gains_tax]

class NetCapitalGainLoss:
    """
    Performs the netting process for capital gains and losses per
    US Federal Taxation rules (short-term vs. long-term).

    Convention: gains are entered as positive numbers (or 0),
    losses are entered as negative numbers (or 0).
    """

    def __init__(self, st_gains, st_losses, lt_gains, lt_losses):
        if st_losses > 0 or lt_losses > 0:
            raise ValueError("Losses must be entered as negative numbers (or zero).")
        if st_gains < 0 or lt_gains < 0:
            raise ValueError("Gains must be entered as positive numbers (or zero).")

        self.st_gains = st_gains
        self.st_losses = st_losses
        self.lt_gains = lt_gains
        self.lt_losses = lt_losses
        self.net = {
            "Net ST": 0,
            "Net LT": 0,
            "Overall": 0,
            "Character": ""
        }

    def netting_process(self):
        net_st = self.st_gains + self.st_losses
        net_lt = self.lt_gains + self.lt_losses
        overall = net_st + net_lt

        self.net["Net ST"] = net_st
        self.net["Net LT"] = net_lt
        self.net["Overall"] = overall

        if net_st == 0 and net_lt == 0:
            self.net["Character"] = "None"
        elif net_st >= 0 and net_lt >= 0:
            # Same sign (or one side is exactly zero): nothing offsets,
            # both sides keep their own character.
            self.net["Character"] = "Net Short-term and Long-term Capital Gain"
        elif net_st <= 0 and net_lt <= 0:
            self.net["Character"] = "Net Short-term and Long-term Capital Loss"
        else:
            # Opposite signs: whichever side has the bigger magnitude
            # determines the overall character. overall's own sign
            # already tells us who won, so no extra abs() comparison needed.
            if overall == 0:
                self.net["Character"] = "None"
            elif overall > 0:
                self.net["Character"] = (
                    "Net Short-term Capital Gain" if net_st > 0 else "Net Long-term Capital Gain"
                )
            else:
                self.net["Character"] = (
                    "Net Short-term Capital Loss" if net_st < 0 else "Net Long-term Capital Loss"
                )

        return self.net

class TaxCredits(IncomeTax):
    def __init__(self, status, age, gross_income, credits, prepayments):
        super().__init__(status, age, gross_income)
        self.credits = credits
        self.prepayments = prepayments

        # This class will handle tax credits, limits, phase offs, etc. For now we just return 
        # what is given.

    def tax_credits(self):
        return self.credits

    def tax_prepayments(self):
        return self.prepayments

class TaxMetrics(IncomeTax):
    def __init__(self, income, non_taxable_income, change):
        super.__init__(income)
        self.non_taxable_income = non_taxable_income
        self.change = change

    def marginal_rate(self):
        pass
    def average_rate(self):
        pass
    def effective_rate(self):
        pass

class DependencyTest:
    def residence_tests(self, start_date: date, end_date: date):
        tax_year = start_date.year
        days_lived_with_taxpayer = (end_date - start_date).days + 1
        days_in_tax_year = 366 if calendar.isleap(tax_year) else 365

        return days_lived_with_taxpayer > days_in_tax_year / 2
    
    def core_dependency_test(self, dependent_taxpayer_test, citizenship_residency_test, joint_return_test):
        core_dependency = all([dependent_taxpayer_test, citizenship_residency_test, joint_return_test])

        return [core_dependency, f"""
Core Dependency Tests:
    1) Dependent Taxpayer Test:         {dependent_taxpayer_test}
    2) Citizen or Resident Test:       {citizenship_residency_test}
    3) Joint Return Test:              {joint_return_test}
Core Dependency Test Result:           {core_dependency}"""]
        
    def qualifying_child_test(self, relationship_test, age_test, residence_test, half_support_test):
        qualifying_child = all([relationship_test, age_test, residence_test, half_support_test])

        return [qualifying_child, f"""
Qualifying Child Tests:
    1) Relationship Test:              {relationship_test}
    2) Age Test:                       {age_test}
    3) Residence Test:                 {residence_test}
    4) Support Test:                   {half_support_test}
Qualifying Child Test Results:         {qualifying_child}"""]

    def qualifying_relative_test(self, relationship_test, support_test, gross_income_test):
        qualifying_relative = all([relationship_test, support_test, gross_income_test])

        return [qualifying_relative, f"""
Qualifying Relative Tests:
    1) Relationship Test:              {relationship_test}
    2) Support Test:                   {support_test}
    3) Gross Income Test:              {gross_income_test}
Qualifying Relative Test Result:       {qualifying_relative}"""]

class IncomeTaxSummary:
    def __init__(
            self,
            gross_income, 
            adjustments,     # Adjustments to arrive at agi
            deduction,       # From AGI deduction      
            qbi_deduction,   # From AGI deduction
            capital_gains, 
            ordinary_tax, 
            capital_gains_tax, 
            credits, 
            prepayments
            ):
            self.gross_income = gross_income
            self.adjustments = adjustments
            self.deduction = deduction
            self.qbi_deduction = qbi_deduction
            self.capital_gains = capital_gains
            self.ordinary_tax = ordinary_tax
            self.capital_gains_tax = capital_gains_tax
            self.credits = credits
            self.prepayments = prepayments

    def income_tax_summary(self):
    
        self.gross_income += self.capital_gains
        adjusted_gross_income = self.gross_income - self.adjustments
        taxable_income = adjusted_gross_income - self.deduction - self.qbi_deduction
        taxable_ordinary_income = taxable_income - self.capital_gains
        total_tax = self.ordinary_tax + self.capital_gains_tax
        tax_due_refund = total_tax + self.credits + self.prepayments
        results = "Tax due" if tax_due_refund >= 0 else "Tax refund"

        df = pd.DataFrame([
                ["Gross income", self.gross_income],
                ["Adjustments", self.adjustments],
                [""],
                ["Adjusted gross income", adjusted_gross_income],
                ["From AGI deductions:"],
                ["Standard / itemized deduction", self.deduction],
                ["QBI deduction", self.qbi_deduction],
                [""],
                ["Taxable income", taxable_income],
                [""],
                ["Taxable ordinary income", taxable_ordinary_income],
                ["Taxable capital gains", self.capital_gains],
                [""],
                ["Ordinary income tax", self.ordinary_tax],
                ["Capital gains tax", self.capital_gains_tax],
                [""],
                ["Tax before credits", total_tax],
                [""],
                ["Credits", self.credits],
                ["Prepayments", self.prepayments],
                [""],
                [results, tax_due_refund],
            ], columns=["", ""])

        def format_number(x):
            if pd.isna(x):
                return ""
            if x < 0:
                return f"({abs(x):,.0f})"
            return f"{x:,.0f}"
        amount_col = df.iloc[:, 1].astype(object).apply(format_number)
        df.isetitem(1, amount_col) # type: ignore

        return df

class TaxableSocialSecurity:
    def __init__(self, magi, social_security):
        self.magi = magi
        self.social_security = social_security

        self.limits = {
            "single": [[25000, 34000], 4500],
            "married": [[32000, 44000], 6000],
        }

        self.fifty_pct_of_ss = self.social_security *.50
        self.eightyfive_pct_ss = self.social_security * .85
        self.magi_plus_fifty = self.magi + self.fifty_pct_of_ss
        self.taxable_ss = 0

    def single(self):
        if self.magi_plus_fifty <= self.limits["single"][0][0]:
            return self.taxable_ss
        elif self.magi_plus_fifty > self.limits["single"][0][0] and self.magi_plus_fifty <= self.limits["single"][0][1]:
            a = self.fifty_pct_of_ss
            b = (self.magi_plus_fifty - self.limits["single"][0][0]) * .50
            self.taxable_ss = min(a, b)
            return self.taxable_ss
        elif self.magi_plus_fifty > self.limits["single"][0][1]:
            a = self.eightyfive_pct_ss
            b = ((self.magi_plus_fifty - self.limits["single"][0][1]) * .85) + min(self.limits["single"][1], self.fifty_pct_of_ss)
            self.taxable_ss = min(a, b)
            return self.taxable_ss
    
    def married(self):
        if self.magi_plus_fifty <= self.limits["married"][0][0]:
            return self.taxable_ss
        elif self.magi_plus_fifty > self.limits["married"][0][0] and self.magi_plus_fifty <= self.limits["married"][0][1]:
            a = self.fifty_pct_of_ss
            b = (self.magi_plus_fifty - self.limits["married"][0][0]) * .50
            self.taxable_ss = min(a, b)
            return self.taxable_ss
        elif self.magi_plus_fifty > self.limits["married"][0][1]:
            a = self.eightyfive_pct_ss
            b = ((self.magi_plus_fifty - self.limits["married"][0][1]) * .85) + min(self.limits["married"][1], self.fifty_pct_of_ss)
            self.taxable_ss = min(a, b)
            return self.taxable_ss

    def married_filing_separately(self):
        a = self.eightyfive_pct_ss
        b = (self.magi + self.fifty_pct_of_ss) *.85
        self.taxable_ss = min(a, b)
        return self.taxable_ss
        
if __name__ == "__main__":
    pass
