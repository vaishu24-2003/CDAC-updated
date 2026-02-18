from stipend_utils import calculate_stipend_bonus

def main():
    stipend=float(input("enter the amount:"))
    rating=int(input("enter the rating(1-5):"))
    
    b=calculate_stipend_bonus(stipend,rating)
    print(id(b))
    print(f"stipend of {stipend} is {b}")
main()
