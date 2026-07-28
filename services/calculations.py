def protein_per_dollar(protein, price):
    """
    Calculate the amount of protein per dollar spent.

    Args:
        protein (float): The amount of protein in grams.
        price (float): The price in dollars.

    Returns:
        float: The amount of protein per dollar, or None if price is zero.
    """
    if price == 0:
        return None
    return protein / price

def calorie_per_dollar(calories, price):
    """
    Calculate the amount of calories per dollar spent.

    Args:
        calories (float): The amount of calories.
        price (float): The price in dollars.

    Returns:
        float: The amount of calories per dollar, or None if price is zero.
    """
    if price == 0:
        return None
    return calories / price