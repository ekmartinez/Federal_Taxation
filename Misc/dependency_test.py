import calendar
from datetime import date

class DependencyTest:

    # --- Core requirements (apply to both qualifying child and qualifying relative) ---

    def core_requirements_test(self, *, citizen_or_resident: bool, joint_return: bool) -> dict:
        # joint_return should be True if the dependent does NOT file a joint return
        # (or files one only to claim a refund, with no tax liability for either spouse).
        results = {
            "citizenship_residency_test": citizen_or_resident,
            "joint_return_test": joint_return,
        }
        failed_tests = [name for name, passed in results.items() if not passed]
        results["passed"] = len(failed_tests) == 0
        results["failed_tests"] = failed_tests # type: ignore
        return results

    # --- Qualifying child sub-tests ---

    def qualifying_child_residency_test(self, start_date: date, end_date: date) -> bool:
        if start_date > end_date:
            raise ValueError("Start date must not be after end date.")
        if start_date.year != end_date.year:
            raise ValueError("Residency period must be within a single tax year")
        tax_year = start_date.year
        # Both the start and end dates are included in the residency period.
        days_lived_with_taxpayer = (end_date - start_date).days + 1
        days_in_tax_year = 366 if calendar.isleap(tax_year) else 365
        return days_lived_with_taxpayer > days_in_tax_year / 2

    def qualifying_child_age_test(self, age: int, taxpayer_age: int, student: bool,
                                   permanently_and_totally_disabled: bool = False) -> bool:
        if age < 0 or taxpayer_age < 0:
            raise ValueError("Age must not be negative.")
        # No age limit applies if the person is permanently and totally disabled.
        if permanently_and_totally_disabled:
            return True
        # Age here means age as of December 31 of the tax year.
        is_younger_than_taxpayer = age < taxpayer_age
        meets_age_threshold = age < 19 or (age < 24 and student)
        return is_younger_than_taxpayer and meets_age_threshold

    def qualifying_child_test(self, *, relationship: bool, age: int, taxpayer_age: int,
                               student: bool, start_date: date, end_date: date,
                               support: bool, disabled: bool = False) -> dict:
        results = {
            "relationship_test": relationship,
            "age_test": self.qualifying_child_age_test(age, taxpayer_age, student, disabled),
            "residence_test": self.qualifying_child_residency_test(start_date, end_date),
            "support_test": support,
        }
        failed_tests = [name for name, passed in results.items() if not passed]
        results["passed"] = len(failed_tests) == 0
        results["failed_tests"] = failed_tests
        return results

    # --- Qualifying relative sub-tests ---

    # 2026 IRS gross income limit for the qualifying relative test. This threshold
    # is adjusted for inflation most years — update it (or pass a different value
    # via gross_income_limit) when working problems set in a different tax year.
    GROSS_INCOME_LIMIT = 5300

    def qualifying_relative_not_a_qualifying_child_test(self, is_qualifying_child: bool) -> bool:
        # A person who meets the qualifying child test for ANY taxpayer cannot
        # also be that (or another) taxpayer's qualifying relative.
        return not is_qualifying_child

    def qualifying_relative_relationship_or_household_test(self, *, related: bool,
                                                             member_of_household_all_year: bool) -> bool:
        # Passes if either: related to the taxpayer in a way the IRS lists (parent,
        # sibling, etc. — relationship alone, residency not required), OR
        # lived with the taxpayer as a member of the household for the entire year.
        return related or member_of_household_all_year

    def qualifying_relative_gross_income_test(self, gross_income: float,
                                               gross_income_limit: float = GROSS_INCOME_LIMIT) -> bool:
        if gross_income < 0:
            raise ValueError("Gross income must not be negative.")
        return gross_income < gross_income_limit

    def qualifying_relative_support_test(self, taxpayer_support_percentage: float) -> bool:
        # Taxpayer must provide more than half the dependent's total support for the year.
        if not 0 <= taxpayer_support_percentage <= 1:
            raise ValueError("Support percentage must be between 0 and 1.")
        return taxpayer_support_percentage > 0.5

    def qualifying_relative_test(self, *, is_qualifying_child: bool, related: bool,
                                  member_of_household_all_year: bool, gross_income: float,
                                  taxpayer_support_percentage: float,
                                  gross_income_limit: float = GROSS_INCOME_LIMIT) -> dict:
        results = {
            "not_a_qualifying_child_test": self.qualifying_relative_not_a_qualifying_child_test(
                is_qualifying_child
            ),
            "relationship_or_household_test": self.qualifying_relative_relationship_or_household_test(
                related=related, member_of_household_all_year=member_of_household_all_year
            ),
            "gross_income_test": self.qualifying_relative_gross_income_test(
                gross_income, gross_income_limit
            ),
            "support_test": self.qualifying_relative_support_test(taxpayer_support_percentage),
        }
        failed_tests = [name for name, passed in results.items() if not passed]
        results["passed"] = len(failed_tests) == 0
        results["failed_tests"] = failed_tests
        return results

    # --- Top-level orchestrator ---

    def evaluate_dependency(self, *, core: dict, qualifying_child_args: dict = None,
                             qualifying_relative_args: dict = None) -> dict:
        core_result = self.core_requirements_test(**core)

        if not core_result["passed"]:
            return {
                "core": core_result,
                "qualifying_child": None,
                "qualifying_relative": None,
                "dependent_status": "Not a dependent",
                "reason": "Failed core requirements: " + ", ".join(core_result["failed_tests"]),
            }

        qc_result = self.qualifying_child_test(**qualifying_child_args)

        if qc_result["passed"]:
            return {
                "core": core_result,
                "qualifying_child": qc_result,
                "qualifying_relative": None,
                "dependent_status": "Qualifying child",
                "reason": None,
            }

        # Qualifying child failed — fall through to qualifying relative.
        # is_qualifying_child is always False here, since qc_result["passed"] is False.
        qualifying_relative_args = dict(qualifying_relative_args or {})
        qualifying_relative_args["is_qualifying_child"] = False
        qr_result = self.qualifying_relative_test(**qualifying_relative_args)

        return {
            "core": core_result,
            "qualifying_child": qc_result,
            "qualifying_relative": qr_result,
            "dependent_status": "Qualifying relative" if qr_result["passed"] else "Not a dependent",
            "reason": None if qr_result["passed"] else "Failed: " + ", ".join(qr_result["failed_tests"]),
        }
