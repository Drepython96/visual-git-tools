def calculate_total(price, quantity, tax_rate=0.06):
    """Calculate the purchase total including sales tax."""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return round(subtotal + tax, 2)


print(calculate_total(12.50, 2))