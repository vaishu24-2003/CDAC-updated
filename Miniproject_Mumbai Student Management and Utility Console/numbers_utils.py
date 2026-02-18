def reverse_number(n):
    """Reverses a positive integer using while loop."""
    if n < 0:
        raise ValueError("Negative number not allowed")

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num

def sum_of_digits(n):
    """Reduces number to single digit using while loop."""
    if n < 0:
        raise ValueError("Negative number not allowed")

    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total

    return n