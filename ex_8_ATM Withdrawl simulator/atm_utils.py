def withdraw(balance, amount):
    """
    Simulates ATM withdrawal.

    Rules:
    - Both balance and amount must be integers.
    - Amount must be multiple of 100.
    - Amount cannot exceed balance.

    Raises:
    - TypeError
    - ValueError

    Returns updated balance.
    """

   
    if not isinstance(balance, int) or not isinstance(amount, int):
        raise TypeError("Balance and amount must be integers")

   
    if amount % 100 != 0:
        raise ValueError("Amount must be multiple of 100")

    
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
