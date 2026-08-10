from stackCalc import RPNEngine

class OrdinaryTax:
    def __init__(self, classification, taxable_income):
        self.classification = classification
        self.taxable_income = taxable_income

    def tax_schedules(self):
        """Returns 2026 US Federal Income Tax Tables
        SNG = Single
        MFJ = Married Filling Jointly
        """


        """
        # 2024 Schedules
        self.schedules = {
            "SNG": [[.10, .12, .22, .24, .32, .35, .37], 
                    [12400, 50400, 105700, 201775, 256225, 640600]],
            "MFJ": [[.10, .12, .22, .24, .32, .35, .37], 
                    [23200, 94300, 201050, 383900, 487450, 731200]]
        }
        """
        # 2026 Schedules
        # SNG: Single
        # MFJ: Married Filling Jointly
        # QSS: Qualifying Surving Spouse
        self.schedules = {
            "SNG": [[.10, .12, .22, .24, .32, .35, .37], 
                    [12400, 50400, 105700, 201775, 256225, 640600]],
            "MFJ": [[.10, .12, .22, .24, .32, .35, .37], 
                    [24800, 100800, 211400, 403550, 512450, 768700]],
            "QSS": [[.10, .12, .22, .24, .32, .35, .37], 
                    [24800, 100800, 211400, 403550, 512450, 768700]]
            }
        
        return self.schedules[self.classification]

    def compute_tax(self):    
        data = self.tax_schedules()

        tax = 0
     
        if self.taxable_income <= data[1][0]:
            tax = self.taxable_income * data[0][0]
        elif self.taxable_income > data[1][0] and self.taxable_income <= data[1][1]:
            tax += data[1][0] * data[0][0]
            tax += (self.taxable_income - data[1][0]) * data[0][1]
        elif self.taxable_income > data[1][1] and self.taxable_income <= data[1][2]:
            tax += data[1][0] * data[0][0]
            tax += (data[1][1] - data[1][0]) * data[0][1]
            tax += (self.taxable_income - data[1][1]) * data[0][2]
        elif self.taxable_income > data[1][2] and self.taxable_income <= data[1][3]:
            tax += data[1][0] * data[0][0]
            tax += (data[1][1] - data[1][0]) * data[0][1]
            tax += (data[1][2] - data[1][1]) * data[0][2]
            tax += (self.taxable_income - data[1][2]) * data[0][3]
        elif self.taxable_income > data[1][3] and self.taxable_income <= data[1][4]:
            tax += data[1][0] * data[0][0]
            tax += (data[1][1] - data[1][0]) * data[0][1]
            tax += (data[1][2] - data[1][1]) * data[0][2]
            tax += (data[1][3] - data[1][2]) * data[0][3]
            tax += (self.taxable_income - data[1][3]) * data[0][4]
        elif self.taxable_income > data[1][4] and self.taxable_income <= data[1][5]:
            tax += data[1][0] * data[0][0]
            tax += (data[1][1] - data[1][0]) * data[0][1]
            tax += (data[1][2] - data[1][1]) * data[0][2]
            tax += (data[1][3] - data[1][2]) * data[0][3]
            tax += (data[1][4] - data[1][3]) * data[0][4]
            tax += (self.taxable_income - data[1][4]) * data[0][5]
        elif self.taxable_income > data[1][5]:
            tax += data[1][0] * data[0][0]
            tax += (data[1][1] - data[0]) * data[0][1]
            tax += (data[1][2] - data[1]) * data[0][2]
            tax += (data[1][3] - data[2]) * data[0][3]
            tax += (data[1][4] - data[3]) * data[0][4]
            tax += (data[1][5] - data[4]) * data[0][5]
            tax += (self.taxable_income - data[1][5]) * data[0][6]

        return tax

class CapitalGains(OrdinaryTax):
    def __init__(self, classification, taxable_income, capital_gains):
        super().__init__(classification, taxable_income)
        self.capital_gains = capital_gains
        self.tax_rates = [0, .15, .20]
        self.limits = {
            "SNG": [0, 49450, 545500], # 2026 Single
            "MFJ": [0, 98900, 613700], # 2026 Married Filing Jointly
            "QSS": [0, 98900, 613700], # 2026 Qualifiying Surviving Spouse
            "HHD": [0, 66200, 579600], # 2026 Head of Household
            "MFS": [0, 49450, 306850], # 2026 Married Filing Separately
            "TAE": [0, 3300, 16250], # 2026 Trust and Estates
        }

    def capital_gains_tax(self):
        if self.classification == "SNG":
            if self.taxable_income > self.limits["SNG"][0] and self.taxable_income <= self.limits["SNG"][1]:
                return 0 
            elif self.taxable_income > self.limits["SNG"][1] and self.taxable_income <= self.limits["SNG"][2]:
                return self.capital_gains * self.tax_rates[1]
            elif self.taxable_income > self.limits["SNG"][2]:
                return self.capital_gains * self.tax_rates[2]
        elif self.classification == "MFJ":
            if self.taxable_income > self.limits["MFJ"][0] and self.taxable_income <= self.limits["MFJ"][1]:
                return 0 
            elif self.taxable_income > self.limits["MFJ"][1] and self.taxable_income <= self.limits["MFJ"][2]:
                return self.capital_gains * self.tax_rates[1]
            elif self.taxable_income > self.limits["MFJ"][2]:
                return self.capital_gains * self.tax_rates[2]


class Planning(OrdinaryTax):
    def __init__(self, classification, taxable_income, non_taxable_income=0, change=0):
        super().__init__(classification, taxable_income)
        self.change = change
        self.non_taxable_income = non_taxable_income

    def change_in_taxable_income(self):
        return (self.taxable_income + self.change) - self.taxable_income

    def new_tax(self):
        self.taxable_income += self.change
        return(self.compute_tax())

    def change_in_tax(self):
        current_tax = super().compute_tax() 
        new_tax = self.new_tax()
        return new_tax - current_tax

    def marginal_tax_rate(self):
        return self.change_in_tax() / self.change_in_taxable_income()
    
    def average_tax_rate(self):
        return self.compute_tax() / self.taxable_income
    
    def effective_tax_rate(self):
        total_tax = self.compute_tax()
        total_income = self.taxable_income + self.non_taxable_income 
        return total_tax / total_income

def timming_strategy(cat, amount, cost, rr, data):
    """ Returns the after-tax cost / cash-flow
    cat: category: income, expense
    amount: before tax amount
    cost: when a gain is needed, else N/A
    rr: rate of return
    data: a dictionary holding each scenario:
        mtr: Marginal Tax Rate
        scenarios = {
            "Scenario_1": [0, mtr] -> 0: Current year, mtr
            "Scenario_2": [1, mtr] -> 1: Next year, mtr
            "on so on...
        }
    """

    for k, v in data.items():
        print(f"{k}\n{"-"*33}")
        print(f"{"Income:" if cat == "income" else "Deduction"} ${amount:,.0f}")
        print(f"Marginal Tax Rate: {v[1]*100:.0f}%")
        tax = RPNEngine(f"{v[1]} {amount} {cost} - *").safe_evaluate().value
        print(f"Tax {"on gain" if cat == "income" else "savings"}: ${tax:,.0f}")
        pv = RPNEngine(f"{rr} {v[0]} {0} {tax} pv").safe_evaluate().value
        print(f"Present Value of {"tax cost" if cat == "income" else "tax savings"}: ${-pv:,.0f}")
        print(f"After-tax {"cash flow" if cat == "income" else "cost"}: ${amount + pv:,.0f}")
        print(f"{"-"*33}\n")

if __name__ == "__main__":
    capital_gains = 5000
    taxable_income = 96400
    status = "MFJ"

    cap = CapitalGains(status, taxable_income, capital_gains).capital_gains_tax()
    print(cap)