class IncomeTax:
    def __init__(self, status, age, gross_income):
        self.status = status
        self.age = age
        self.gross_income = gross_income

        """
        "SNG": Single
        "MFJ": Married Filing Jointly
        "MFS": Married Filing Separately
        "QSS": Qualifiying Surviving Spouse
        "HOH": Head of Household
        """
        self.standard_deduction = {
            "SNG": 16100, 
            "MFJ": 32200, 
            "MFS": 16100, 
            "QSS": 32200, 
            "HOH": 24150, 
        }

        self.preferential = {
            "rates": [0, .15, .20],
            "SNG": [0, 49450, 545500], 
            "MFJ": [0, 98900, 613700], 
            "MFS": [0, 49450, 306850], 
            "QSS": [0, 98900, 613700], 
            "HOH": [0, 66200, 579600], 
        }

        self.ordinary = {
            "rates": [.10, .12, .22, .24, .32, .35, .37],
            "SNG": [[0, 12400, 50400, 105700, 201775, 256225, 640600],   # Limits
                    [0, 1240, 5800, 17966, 41024, 58448, 192979.25]], # Pay this amount
            "MFJ": [[0, 24800, 100800, 211400, 403550, 512450, 768700],
                    [0, 2480, 11600, 35932, 82048, 116896, 206583.50]], 
            "MFS": [[0, 12400, 50400, 105700, 201775, 256225, 384350],
                    [0, 1240, 5800, 17966, 41024, 58448, 103291.75]],
            "QSS": [[0, 24800, 100800, 211400, 403550, 512450, 768700],
                    [0, 2480, 11600, 35932, 82048, 116896, 206583.50]],
            "HOH": [[0, 17700, 67450, 105700, 201750, 256200, 640600], 
                    [0, 1770, 7740, 16155, 39207, 56631, 191171]],
        }

class OrdinaryIncomeTax(IncomeTax):
    def __init__(self, status, age, gross_income, adjustments, itemized):
        super().__init__(status, age, gross_income)
        self.adjustments = adjustments
        self.itemized = itemized
        self.rates = self.ordinary["rates"]
        self.schedule = self.ordinary[self.status]

        self.from_agi_deduction = max(self.itemized, self.standard_deduction[self.status])

    def calculate_tax(self):
        qbi_deduction = 0 # Module is pending
        tax_rate = 0
        ordinary_tax = 0
        adjusted_gross_income = self.gross_income - self.adjustments
        taxable_income = adjusted_gross_income - self.from_agi_deduction - qbi_deduction

        data_return = {
            "status": self.status,
            "age": self.age,
            "gross_income": self.gross_income,
            "adjustments": self.adjustments,
            "standard_deduction": self.standard_deduction[self.status], # type: ignore
            "itemized_deduction": self.itemized,
            "deduction": self.from_agi_deduction,
            "qbi_deduction": qbi_deduction,
            "marginal_tax_rate": tax_rate,
            "ordinary_tax": ordinary_tax,
        }
        data_return["adjusted_gross_income"] = self.gross_income - self.adjustments
        data_return["taxable_income"] = data_return["adjusted_gross_income"] - self.from_agi_deduction - qbi_deduction
        
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
    # TODO: Raise error if losses are not negative
    def __init__(self, st_cap_gains, st_cap_losses, lt_cap_gains, lt_cap_losses):
        self.st_cap_gains = st_cap_gains
        self.st_cap_losses = st_cap_losses
        self.lt_cap_gains = lt_cap_gains
        self.lt_cap_losses = lt_cap_losses

        self.net = {
            "short_term": [],
            "long_term": [],
            "net_capital_gain_loss": []
        }
    
    def netting_process(self):

        net_short_term_capital_gain_loss = self.st_cap_gains + self.st_cap_losses
        if net_short_term_capital_gain_loss > 0:
            self.net["short_term"].append("Net Short-Term Capital Gain")
        else:
            self.net["short_term"].append("Net Short-Term Capital loss")
        self.net["short_term"].append(net_short_term_capital_gain_loss)

        net_long_term_capital_gain_loss = self.lt_cap_gains + self.lt_cap_losses
        if net_long_term_capital_gain_loss > 0:
            self.net["long_term"].append("Net Long-Term Capital Gain")
        else:
            self.net["long_term"].append("Net Long-Term Capital loss")
        self.net["long_term"].append(net_long_term_capital_gain_loss)

        

        """
        {'short_term': ['Net Short-Term Capital Gain', 300],
        'long_term': ['Net Long-Term Capital Gain', 4500]}
        """


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

if __name__ == "__main__":
    status = "HOH"
    age = 30
    ordinary_income = 106000
    capital_gains = 4000
    itemized = 0
    # taxes = OrdinaryIncomeTax(status, age, ordinary_income, itemized).calculate_tax()
    # taxes = PreferentialIncomeTax(status, age, ordinary_income, 0, capital_gains).calculate_tax()
    # print(taxes)