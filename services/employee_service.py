from utils.validation_utils import (
    validate_employee_id,
    validate_salary,
    validate_non_empty
)


def add_employee(emp_list: list, emp_id: str, name: str, city: str, salary: float) -> None:
    validate_employee_id(emp_id)
    validate_non_empty(name, "Name")
    validate_non_empty(city, "City")
    validate_salary(salary)

    for emp in emp_list:
        if emp["id"] == emp_id:
            raise ValueError("Employee ID already exists.")

    emp_list.append({
        "id": emp_id,
        "name": name,
        "city": city,
        "salary": salary
    })


def edit_employee(emp_list: list, emp_id: str, **updates) -> None:
    for emp in emp_list:
        if emp["id"] == emp_id:
            if "name" in updates:
                validate_non_empty(updates["name"], "Name")
                emp["name"] = updates["name"]

            if "city" in updates:
                validate_non_empty(updates["city"], "City")
                emp["city"] = updates["city"]

            if "salary" in updates:
                validate_salary(float(updates["salary"]))
                emp["salary"] = float(updates["salary"])

            return

    raise ValueError("Employee ID not found.")


def delete_employee(emp_list: list, emp_id: str) -> None:
    for emp in emp_list:
        if emp["id"] == emp_id:
            emp_list.remove(emp)
            return

    raise ValueError("Employee ID not found.")


def list_employees(emp_list: list) -> list:
    return emp_list