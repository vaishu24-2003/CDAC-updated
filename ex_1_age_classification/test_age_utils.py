from age_utils import categorize_person

def main():
    n = int(input("Enter a number: "))
    a=categorize_person(n)
    print(type(a))
    print(id(a))
    print(f"category of {n} is {a}")

main()
   

    
