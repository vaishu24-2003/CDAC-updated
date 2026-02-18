def safe_integer_input(prompt: str) -> int:
    """
    Takes user input and safely converts it to integer.
    Raises TypeError if conversion fails.
    Returns valid integer.
    """
    user_input = input(prompt)

    try:
        return int(user_input)
    except ValueError:
        raise TypeError("Invalid input! Please enter a valid integer.")
