from input_utils import safe_integer_input


#Age Classification 
age = safe_integer_input("Enter your age: ")

if age < 18:
    print("Minor")
else:
    print("Adult")


#Even or Odd 
number = safe_integer_input("Enter a number: ")

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
