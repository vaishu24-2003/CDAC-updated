def categorize_person(age):
    """Categorizes person based on age."""
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"
    
def calculate_stipend_bonus(stipend, performance_score):
    """Calculates stipend bonus based on performance."""
    if stipend < 0 or performance_score < 0:
        raise ValueError("Values cannot be negative")

    if performance_score >= 90:
        return stipend * 1.20
    elif performance_score >= 75:
        return stipend * 1.10
    else:
        return stipend
