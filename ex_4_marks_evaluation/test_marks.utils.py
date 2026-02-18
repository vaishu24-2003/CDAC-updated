from evaluate_marks_utils import evaluate_marks

def main():
    marks=int(input("enter the marks:"))
    attendance=int(input("enter the attendance:"))
    a=evaluate_marks(marks,attendance)
    print(a)
main()
