def sum_of_digits(n: int) -> int:
    """
    Accepts a positive integer.
    Repeatedly reduces number by summing digits
    until a single digit remains.
    Uses only while loop.
    Raises ValueError if negative.
    """

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Negative numbers are not allowed")

    while n >= 10:   
        total = 0

        while n > 0:
            digit = n % 10
            total += digit
            n = n // 10

        print("Intermediate sum:", total)

        n = total   

    return n
