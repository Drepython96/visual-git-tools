def calculate_total(price, quantity, tax_rate=0.06):
    """Calculate the purchase total including sales tax."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be nonnegative")
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return round(total, 2)


print(calculate_total(12.50, 2))