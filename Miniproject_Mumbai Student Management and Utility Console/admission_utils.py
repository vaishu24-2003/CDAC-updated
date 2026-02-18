def check_admission(marks, age, city):
    """Checks admission eligibility."""

    if marks < 0 or age < 0:
        raise ValueError("Invalid marks or age")

    valid_cities = ["Mumbai", "Pune", "Delhi"]

    if city not in valid_cities:
        raise ValueError("City not eligible")

    if marks >= 70 and age >= 18:
        return "Admission Approved"
    else:
        return "Admission Denied"
