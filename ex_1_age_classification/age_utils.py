def categorize_person(age):
    """
    Classify and categorize a person based on age.
    """

    if type(age)!=int:
        raise TypeError("only int type is allowed")

    if age < 0 or age > 120:
        raise ValueError("enter a valid age")

    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"

