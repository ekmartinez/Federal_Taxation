from datetime import date

import pytest

from qualifying_child_residency import QualifyingChildResidencyTest


class TestQualifyingChildResidencyTest:
    """Tests for QualifyingChildResidencyTest."""

    # -------------------------------------------------------------------------
    # Basic cases
    # -------------------------------------------------------------------------

    def test_full_year_passes(self):
        test = QualifyingChildResidencyTest(
            date(2023, 1, 1),
            date(2023, 12, 31),
        )

        assert test.passed() is True

    def test_one_day_fails(self):
        test = QualifyingChildResidencyTest(
            date(2023, 6, 15),
            date(2023, 6, 15),
        )

        assert test.passed() is False

    # -------------------------------------------------------------------------
    # Non-leap year (365 days)
    #
    # More than half of 365 days = 183 days
    # -------------------------------------------------------------------------

    def test_183_days_passes_in_non_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2023, 7, 2),
            date(2023, 12, 31),
        )

        assert test.passed() is True

    def test_182_days_fails_in_non_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2023, 7, 3),
            date(2023, 12, 31),
        )

        assert test.passed() is False

    def test_first_183_days_passes_in_non_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2023, 1, 1),
            date(2023, 7, 2),
        )

        assert test.passed() is True

    def test_first_182_days_fails_in_non_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2023, 1, 1),
            date(2023, 7, 1),
        )

        assert test.passed() is False

    # -------------------------------------------------------------------------
    # Leap year (366 days)
    #
    # More than half of 366 days = 184 days
    # -------------------------------------------------------------------------

    def test_184_days_passes_in_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2024, 7, 1),
            date(2024, 12, 31),
        )

        assert test.passed() is True

    def test_183_days_fails_in_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2024, 7, 2),
            date(2024, 12, 31),
        )

        assert test.passed() is False

    def test_first_184_days_passes_in_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2024, 1, 1),
            date(2024, 7, 2),
        )

        assert test.passed() is True

    def test_first_183_days_fails_in_leap_year(self):
        test = QualifyingChildResidencyTest(
            date(2024, 1, 1),
            date(2024, 7, 1),
        )

        assert test.passed() is False

    # -------------------------------------------------------------------------
    # Specific example
    # -------------------------------------------------------------------------

    def test_june_15_through_december_31_2024(self):
        test = QualifyingChildResidencyTest(
            date(2024, 6, 15),
            date(2024, 12, 31),
        )

        assert test.passed() is True

    # -------------------------------------------------------------------------
    # Leap year identification
    # -------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "year",
        [2020, 2024, 2028, 2032],
    )
    def test_leap_year_boundary(self, year):
        # July 2 through December 31 is 183 days.
        # Therefore it should fail in a leap year.
        test = QualifyingChildResidencyTest(
            date(year, 7, 2),
            date(year, 12, 31),
        )

        assert test.passed() is False

    @pytest.mark.parametrize(
        "year",
        [2019, 2021, 2022, 2023, 2025, 2026],
    )
    def test_non_leap_year_boundary(self, year):
        # July 2 through December 31 is 183 days.
        # Therefore it should pass in a non-leap year.
        test = QualifyingChildResidencyTest(
            date(year, 7, 2),
            date(year, 12, 31),
        )

        assert test.passed() is True

    # -------------------------------------------------------------------------
    # Inclusive date testing
    # -------------------------------------------------------------------------

    def test_start_and_end_date_are_inclusive(self):
        test = QualifyingChildResidencyTest(
            date(2023, 7, 2),
            date(2023, 12, 31),
        )

        # July 2 through December 31 inclusive = 183 days.
        assert (test.end_date - test.start_date).days + 1 == 183
        assert test.passed() is True

    def test_same_start_and_end_date_is_one_day(self):
        test = QualifyingChildResidencyTest(
            date(2024, 6, 15),
            date(2024, 6, 15),
        )

        assert (test.end_date - test.start_date).days + 1 == 1
        assert test.passed() is False

    # -------------------------------------------------------------------------
    # Invalid date ranges
    # -------------------------------------------------------------------------

    def test_end_date_before_start_date_raises_error(self):
        with pytest.raises(ValueError, match="Start date must not be after end date"):
            QualifyingChildResidencyTest(
                date(2024, 12, 31),
                date(2024, 1, 1),
            )

    # -------------------------------------------------------------------------
    # Cross-tax-year ranges
    # -------------------------------------------------------------------------

    def test_cross_year_range_raises_error(self):
        with pytest.raises(
            ValueError,
            match="Residency period must be within a single tax year",
        ):
            QualifyingChildResidencyTest(
                date(2023, 12, 31),
                date(2024, 1, 1),
            )

    def test_cross_year_range_starting_in_2024_raises_error(self):
        with pytest.raises(
            ValueError,
            match="Residency period must be within a single tax year",
        ):
            QualifyingChildResidencyTest(
                date(2024, 1, 1),
                date(2025, 1, 1),
            )

    # -------------------------------------------------------------------------
    # Tax year
    # -------------------------------------------------------------------------

    def test_tax_year_is_derived_from_start_date(self):
        test = QualifyingChildResidencyTest(
            date(2024, 6, 15),
            date(2024, 12, 31),
        )

        assert test.tax_year == 2024

    def test_start_date_is_stored(self):
        start = date(2024, 6, 15)
        test = QualifyingChildResidencyTest(
            start,
            date(2024, 12, 31),
        )

        assert test.start_date == start

    def test_end_date_is_stored(self):
        end = date(2024, 12, 31)
        test = QualifyingChildResidencyTest(
            date(2024, 6, 15),
            end,
        )

        assert test.end_date == end
