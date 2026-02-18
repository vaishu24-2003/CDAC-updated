revenues = (120000, 150000, 90000, 200000, 175000)
#Get Highest Revenue
def get_highest_revenue(revenues: tuple) -> int:
    """
    Returns the highest revenue.
    """

    if not isinstance(revenues, tuple) or not revenues:
        raise ValueError("Revenues must be a non-empty tuple")

    return max(revenues)
#Get Lowest Revenue
def get_lowest_revenue(revenues: tuple) -> int:
    """
    Returns the lowest revenue.
    """

    if not isinstance(revenues, tuple) or not revenues:
        raise ValueError("Revenues must be a non-empty tuple")

    return min(revenues)
#Count Revenue Occurrence
def count_revenue_occurrence(revenues: tuple, value: int) -> int:
    """
    Returns how many times a revenue value appears.
    """

    if not isinstance(revenues, tuple):
        raise ValueError("Revenues must be a tuple")

    return revenues.count(value)
#Demonstration
if __name__ == "__main__":
    revenues = (120000, 150000, 90000, 200000, 175000)

    print("Revenues:", revenues)

    print("Highest Revenue:", get_highest_revenue(revenues))
    print("Lowest Revenue:", get_lowest_revenue(revenues))
    print("Count of 150000:", count_revenue_occurrence(revenues, 150000))

    print("\nOriginal Tuple Still Unchanged:")
    print(revenues)
