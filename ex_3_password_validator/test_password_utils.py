from validate_password import validate_password

def main():
    password=input("enter the password:")
    a=validate_password(password)
    print(a)
main()