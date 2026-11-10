def calculate_total(amount: float, tax_rate: float = 0.0) -> float:
    """Calculate the total amount after applying tax."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return round(amount * (1 + tax_rate), 2)
