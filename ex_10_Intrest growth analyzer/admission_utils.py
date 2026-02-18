def check_admission(marks, age, city):
    """
    Create check_admission(marks, age, city)

    Criteria:
    - Marks ≥ 70
    - Age ≥ 18
    - City must be Mumbai, Pune, or Delhi

    Raises:
    - TypeError
    - ValueError

    Returns:
    - "Admission Approved"
    - "Admission Denied"
    """

   
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a number")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if not isinstance(city, str):
        raise TypeError("City must be a string")

   
    if marks < 0:
        raise ValueError("Marks cannot be negative")

    if age < 0:
        raise ValueError("Age cannot be negative")

    valid_cities = ["Mumbai", "Pune", "Delhi"]

    if city not in valid_cities:
        raise ValueError("City not eligible for admission")

   
    if marks >= 70 and age >= 18:
        return "Admission Approved"
    else:
        return "Admission Denied"
