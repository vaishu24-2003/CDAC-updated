def withdraw(balance, amount):
    """ATM withdrawal logic with validation."""
    if not isinstance(balance, int) or not isinstance(amount, int):
        raise TypeError("Balance and amount must be integers")

    if amount % 100 != 0:
        raise ValueError("Amount must be multiple of 100")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
