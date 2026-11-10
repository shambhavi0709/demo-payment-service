import pytest

from app.payment import calculate_total


def test_calculate_total_without_tax():
    assert calculate_total(100) == 100.00


def test_calculate_total_with_tax():
    assert calculate_total(100, 0.18) == 118.00


def test_calculate_total_rounds_to_two_decimal_places():
    assert calculate_total(10.555, 0) == 10.55


def test_negative_amount_is_rejected():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        calculate_total(-1)


def test_negative_tax_rate_is_rejected():
    with pytest.raises(ValueError, match="Tax rate cannot be negative"):
        calculate_total(100, -0.1)
