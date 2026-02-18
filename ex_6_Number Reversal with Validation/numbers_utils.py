def reverse_number(n: int) -> int:
    """
    Reverses a positive integer using while loop.
    Raises ValueError if negative.
    Prints intermediate values inside loop.
    Returns reversed number.
    """

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

        print("Intermediate reversed value:", reversed_num)

    return reversed_num
