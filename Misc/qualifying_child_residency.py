import calendar
from datetime import date

class QualifyingChildResidencyTest:
    def __init__(self, start_date: date, end_date: date):
        if start_date > end_date:
            raise ValueError("Start date most not be after end date.")

        if start_date.year != end_date.year:
            raise ValueError("Residency period must be within a singe tax year")

        self.start_date = start_date
        self.end_date = end_date
        self.tax_year = start_date.year

    def passed(self) -> bool:
        # Both the start and end dates are included in the residency period.
        days_lived_with_taxpayer = (self.end_date - self.start_date).days + 1
        days_in_tax_year = 366 if calendar.isleap(self.tax_year) else 365
        return days_lived_with_taxpayer > days_in_tax_year / 2
