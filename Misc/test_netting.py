"""
Comprehensive test suite for netting.py.

Run with:  pytest -v
"""

import pytest
from netting import NetCapitalGainLoss


# ---------------------------------------------------------------------
# SECTION 1: Same-sign scenarios (no cross-offsetting between ST/LT)
# ---------------------------------------------------------------------

@pytest.mark.parametrize(
    "st_gains, st_losses, lt_gains, lt_losses, exp_st, exp_lt, exp_overall, exp_character",
    [
        (5000, -2000, 3000, -1000, 3000, 2000, 5000, "Net Short-term and Long-term Capital Gain"),
        (1000, -6000, 2000, -9000, -5000, -7000, -12000, "Net Short-term and Long-term Capital Loss"),
        # One side is a pure gain, the other is exactly zero -> still "same sign" (0 counts as >=0 / <=0)
        (4000, 0, 0, 0, 4000, 0, 4000, "Net Short-term and Long-term Capital Gain"),
        (0, 0, 4000, 0, 0, 4000, 4000, "Net Short-term and Long-term Capital Gain"),
        (0, -4000, 0, 0, -4000, 0, -4000, "Net Short-term and Long-term Capital Loss"),
        (0, 0, 0, -4000, 0, -4000, -4000, "Net Short-term and Long-term Capital Loss"),
    ],
)
def test_same_sign_scenarios(st_gains, st_losses, lt_gains, lt_losses,
                              exp_st, exp_lt, exp_overall, exp_character):
    obj = NetCapitalGainLoss(st_gains, st_losses, lt_gains, lt_losses)
    result = obj.netting_process()

    assert result["Net ST"] == exp_st
    assert result["Net LT"] == exp_lt
    assert result["Overall"] == exp_overall
    assert result["Character"] == exp_character


# ---------------------------------------------------------------------
# SECTION 2: Opposite-sign scenarios (one side offsets the other)
# ---------------------------------------------------------------------

@pytest.mark.parametrize(
    "st_gains, st_losses, lt_gains, lt_losses, exp_overall, exp_character",
    [
        # ST gain, LT loss, ST wins -> overall gain, ST character
        (9000, -1000, 1000, -6000, 3000, "Net Short-term Capital Gain"),
        # ST gain, LT loss, LT wins -> overall loss, LT character
        (3000, -1000, 1000, -6000, -3000, "Net Long-term Capital Loss"),
        # ST loss, LT gain, LT wins -> overall gain, LT character
        (1000, -6000, 9000, -1000, 3000, "Net Long-term Capital Gain"),
        # ST loss, LT gain, ST wins -> overall loss, ST character
        (1000, -6000, 3000, -1000, -3000, "Net Short-term Capital Loss"),
    ],
)
def test_opposite_sign_quadrants(st_gains, st_losses, lt_gains, lt_losses,
                                  exp_overall, exp_character):
    obj = NetCapitalGainLoss(st_gains, st_losses, lt_gains, lt_losses)
    result = obj.netting_process()

    assert result["Overall"] == exp_overall
    assert result["Character"] == exp_character


# ---------------------------------------------------------------------
# SECTION 3: Zero / boundary edge cases
# ---------------------------------------------------------------------

def test_all_zeros():
    obj = NetCapitalGainLoss(0, 0, 0, 0)
    result = obj.netting_process()

    assert result["Net ST"] == 0
    assert result["Net LT"] == 0
    assert result["Overall"] == 0
    assert result["Character"] == "None"


def test_full_wash_both_sides_cancel():
    obj = NetCapitalGainLoss(5000, -5000, 3000, -3000)
    result = obj.netting_process()

    assert result["Net ST"] == 0
    assert result["Net LT"] == 0
    assert result["Overall"] == 0
    assert result["Character"] == "None"


def test_opposite_signs_that_tie_overall_to_zero():
    # net_st = +3000, net_lt = -3000: individually nonzero, but cancel overall.
    obj = NetCapitalGainLoss(4000, -1000, 2000, -5000)
    result = obj.netting_process()

    assert result["Net ST"] == 3000
    assert result["Net LT"] == -3000
    assert result["Overall"] == 0
    assert result["Character"] == "None"


def test_zero_loss_is_valid_not_rejected():
    # A loss of exactly 0 must be accepted -- it's a boundary value, not
    # a violation of the "losses must be negative" rule.
    obj = NetCapitalGainLoss(1000, 0, 500, 0)
    result = obj.netting_process()

    assert result["Net ST"] == 1000
    assert result["Net LT"] == 500
    assert result["Overall"] == 1500
    assert result["Character"] == "Net Short-term and Long-term Capital Gain"


def test_zero_gain_is_valid_not_rejected():
    obj = NetCapitalGainLoss(0, -1000, 0, -500)
    result = obj.netting_process()

    assert result["Net ST"] == -1000
    assert result["Net LT"] == -500
    assert result["Overall"] == -1500
    assert result["Character"] == "Net Short-term and Long-term Capital Loss"


# ---------------------------------------------------------------------
# SECTION 4: Decimal / cents inputs
# ---------------------------------------------------------------------
# Real tax figures rarely land on round numbers. Floats can introduce
# rounding artifacts (e.g. 0.1 + 0.2 != 0.3 in raw binary floating point),
# so it's worth confirming the netting math and comparisons still behave
# with cents involved. pytest.approx() handles the tiny float imprecision
# for us instead of demanding an exact ==.

def test_decimal_gain_and_loss_same_sign():
    obj = NetCapitalGainLoss(1234.56, -234.56, 500.10, -100.10)
    result = obj.netting_process()

    assert result["Net ST"] == pytest.approx(1000.00)
    assert result["Net LT"] == pytest.approx(400.00)
    assert result["Overall"] == pytest.approx(1400.00)
    assert result["Character"] == "Net Short-term and Long-term Capital Gain"


def test_decimal_opposite_signs():
    obj = NetCapitalGainLoss(900.25, -100.25, 200.00, -800.00)
    result = obj.netting_process()

    assert result["Net ST"] == pytest.approx(800.00)
    assert result["Net LT"] == pytest.approx(-600.00)
    assert result["Overall"] == pytest.approx(200.00)
    assert result["Character"] == "Net Short-term Capital Gain"


def test_decimal_exact_wash_with_cents():
    # Chosen so the cents cancel out exactly to zero.
    obj = NetCapitalGainLoss(150.75, -150.75, 89.30, -89.30)
    result = obj.netting_process()

    assert result["Overall"] == pytest.approx(0.0)
    assert result["Character"] == "None"


# ---------------------------------------------------------------------
# SECTION 5: Input validation
# ---------------------------------------------------------------------

@pytest.mark.parametrize(
    "st_gains, st_losses, lt_gains, lt_losses",
    [
        (100, 500, 0, 0),        # st_losses positive
        (0, 0, 100, 500),        # lt_losses positive
        (-100, 0, 0, 0),         # st_gains negative
        (0, 0, -100, 0),         # lt_gains negative
        (-100, 500, -200, 300),  # everything wrong at once
    ],
)
def test_invalid_inputs_raise_value_error(st_gains, st_losses, lt_gains, lt_losses):
    with pytest.raises(ValueError):
        NetCapitalGainLoss(st_gains, st_losses, lt_gains, lt_losses)


def test_boundary_zero_does_not_raise():
    # Zero is the boundary value for both checks (> 0 and < 0) -- it must
    # be accepted, not rejected. This guards against an off-by-one style
    # mistake like using >= 0 or <= 0 instead of > 0 / < 0 in __init__.
    try:
        NetCapitalGainLoss(0, 0, 0, 0)
    except ValueError:
        pytest.fail("Zero gains/losses should be valid, but raised ValueError.")


def test_error_message_mentions_losses():
    with pytest.raises(ValueError, match="Losses"):
        NetCapitalGainLoss(100, 500, 0, 0)


def test_error_message_mentions_gains():
    with pytest.raises(ValueError, match="Gains"):
        NetCapitalGainLoss(-100, 0, 0, 0)


# ---------------------------------------------------------------------
# SECTION 6: Return type / dict shape sanity checks
# ---------------------------------------------------------------------
# These aren't about the tax math -- they guard against someone later
# renaming a dict key or changing the return type, which would silently
# break any code that calls this class.

def test_netting_process_returns_dict_with_expected_keys():
    obj = NetCapitalGainLoss(1000, -500, 2000, -1000)
    result = obj.netting_process()

    assert isinstance(result, dict)
    assert set(result.keys()) == {"Net ST", "Net LT", "Overall", "Character"}


def test_netting_process_return_value_is_same_object_as_self_net():
    # Confirms netting_process() returns self.net rather than a copy,
    # which matters if calling code expects to reuse obj.net directly.
    obj = NetCapitalGainLoss(1000, -500, 2000, -1000)
    result = obj.netting_process()

    assert result is obj.net
