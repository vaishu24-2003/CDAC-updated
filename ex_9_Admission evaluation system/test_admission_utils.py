from admission_utils import check_admission

try:
    marks = float(input("Enter marks: "))
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    result = check_admission(marks, age, city)
    print(result)

except TypeError as e:
    print("Type Error:", e)

except ValueError as e:
    print("Value Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
