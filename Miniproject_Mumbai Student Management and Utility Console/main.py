import vinod_utils
from student_utils import categorize_person, calculate_stipend_bonus
from atm_utils import withdraw
from numbers_utils import reverse_number, sum_of_digits
from admission_utils import check_admission
def main():
    """Main console application."""

    operations_count = 0
    student_data = {}

    while True:
        try:
            print("\n==== Mumbai Student Management Console ====")
            print("1. Register Student")
            print("2. Age Categorization")
            print("3. Stipend Bonus Calculation")
            print("4. ATM Withdrawal")
            print("5. Reverse Roll Number")
            print("6. Digit Reduction Tool")
            print("7. Admission Evaluation")
            print("8. Module Inspector")
            print("9. System Diagnostics")
            print("10. Exit")

            choice = int(input("Enter choice: "))

            # 1 Register Student
            if choice == 1:
                name = input("Name: ")
                age = int(input("Age: "))
                marks = float(input("Marks: "))
                city = input("City: ")

                if age < 0 or marks < 0:
                    raise ValueError("Invalid age or marks")

                student_data = {
                    "name": name,
                    "age": age,
                    "marks": marks,
                    "city": city
                }

                print("Memory IDs:")
                for key, value in student_data.items():
                    print(key, "->", id(value))

                operations_count += 1

            # 2 Age Categorization
            elif choice == 2:
                if not student_data:
                    print("Please register student first.")
                else:
                    print(categorize_person(student_data["age"]))
                    operations_count += 1

            # 3 Stipend Bonus
            elif choice == 3:
                stipend = float(input("Enter stipend: "))
                score = float(input("Performance score: "))
                print("Updated stipend:",
                      calculate_stipend_bonus(stipend, score))
                operations_count += 1

            # 4 ATM
            elif choice == 4:
                balance = int(input("Balance: "))
                amount = int(input("Withdraw amount: "))
                print("Remaining:", withdraw(balance, amount))
                operations_count += 1

            # 5 Reverse
            elif choice == 5:
                roll = int(input("Roll number: "))
                print("Reversed:", reverse_number(roll))
                operations_count += 1

            # 6 Digit Reduction
            elif choice == 6:
                num = int(input("Enter number: "))
                print("Reduced:", sum_of_digits(num))
                operations_count += 1

            # 7 Admission
            elif choice == 7:
                if not student_data:
                    print("Please register student first.")
                else:
                    print(check_admission(
                        student_data["marks"],
                        student_data["age"],
                        student_data["city"]
                    ))
                    operations_count += 1

            # 8 Module Inspector
            elif choice == 8:
                print("dir:", dir(vinod_utils))
                print("type:", type(vinod_utils))
                print("module id:", id(vinod_utils))
                print("function id:", id(vinod_utils.square))
                help(vinod_utils.square)
                operations_count += 1

            # 9 Diagnostics
            elif choice == 9:
                print("Total operations:", operations_count)
                print("Student data types:")
                for key, value in student_data.items():
                    print(key, "->", type(value))
                print("IDs:",
                      {k: id(v) for k, v in student_data.items()})
                print("\nBuilt-in functions:")
                print(dir(__builtins__))
                operations_count += 1

            # 10 Exit
            elif choice == 10:
                print("\n=== Summary ===")
                print("Name:", student_data.get("name"))
                print("City:", student_data.get("city"))
                print("Total operations:", operations_count)
                print("Exiting safely...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)
