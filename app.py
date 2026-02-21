from services.employee_service import (
    add_employee,
    edit_employee,
    delete_employee,
    list_employees
)

from utils.file_utils import (
    load_employees,
    save_employees
)


FILE_PATH = "data/employees.txt"


def main():
    try:
        employees = load_employees(FILE_PATH)
    except FileNotFoundError:
        employees = []

    while True:
        try:
            print("\n--- Employee Management ---")
            print("1. Add Employee")
            print("2. Edit Employee")
            print("3. Delete Employee")
            print("4. List Employees")
            print("5. Save to File")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                emp_id = input("ID: ")
                name = input("Name: ")
                city = input("City: ")
                salary = float(input("Salary: "))

                add_employee(employees, emp_id, name, city, salary)

            elif choice == "2":
                emp_id = input("Enter ID to edit: ")
                field = input("Field to update (name/city/salary): ")
                value = input("New value: ")

                if field == "salary":
                    edit_employee(employees, emp_id, salary=float(value))
                else:
                    edit_employee(employees, emp_id, **{field: value})

            elif choice == "3":
                emp_id = input("Enter ID to delete: ")
                delete_employee(employees, emp_id)

            elif choice == "4":
                for emp in list_employees(employees):
                    print(emp)

            elif choice == "5":
                save_employees(FILE_PATH, employees)
                print("Data saved successfully.")

            elif choice == "6":
                save = input("Save before exit? (y/n): ")
                if save.lower() == "y":
                    save_employees(FILE_PATH, employees)
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except ValueError as ve:
            print("Error:", ve)
        except FileNotFoundError as fe:
            print("File Error:", fe)
        except Exception as e:
            print("Unexpected Error:", e)


if __name__ == "__main__":
    main()