#employee creation

def create_employee(emp_id: str, name: str, city: str, salary: float) -> tuple:
    """
    Returns an employee record as a tuple.
    Validate inputs properly.
    """

    if not isinstance(emp_id, str) or not emp_id.strip():
        raise ValueError("Employee ID must be a non-empty string")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")

    if not isinstance(city, str) or not city.strip():
        raise ValueError("City must be a non-empty string")

    if not isinstance(salary, (int, float)) or salary <= 0:
        raise ValueError("Salary must be a positive number")

    return (emp_id.strip(), name.strip(), city.strip(), float(salary))
#Update Salary
def update_salary(employee: tuple, new_salary: float) -> tuple:
    """
    Since tuples are immutable, return a new tuple with updated salary.
    Original tuple must not be modified.
    """

    if not isinstance(employee, tuple) or len(employee) != 4:
        raise ValueError("Invalid employee record")

    if not isinstance(new_salary, (int, float)) or new_salary <= 0:
        raise ValueError("New salary must be positive")

    # Creating a NEW tuple instead of modifying the old one
    return (employee[0], employee[1], employee[2], float(new_salary))
#Get Employee Details
def get_employee_details(employee: tuple) -> str:
    """
    Returns formatted string containing employee details.
    """

    if not isinstance(employee, tuple) or len(employee) != 4:
        raise ValueError("Invalid employee record")

    emp_id, name, city, salary = employee

    return (
        f"Employee ID: {emp_id}\n"
        f"Name: {name}\n"
        f"City: {city}\n"
        f"Salary: ₹{salary:.2f}"
    )
#Demonstrating Immutability
emp1 = create_employee("E101", "Rahul", "Bangalore", 45000)

print("Original Employee Tuple:")
print(emp1)
print("Original ID:", id(emp1))

updated_emp = update_salary(emp1, 50000)

print("\nUpdated Employee Tuple:")
print(updated_emp)
print("Updated ID:", id(updated_emp))

print("\nOriginal Tuple Still Unchanged:")
print(emp1)

