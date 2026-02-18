def validate_password(password):
    """ password must be Minimum 8 characters
At least 1 digit
At least 1 uppercase letter"""
    if len(password)<8:
        raise ValueError("password must be minimum 8 chracters")
    if not any(char.isdigit() for char in password):
        raise ValueError("password must contain atleast 1 digit")
    if not any(char.isupper() for char in password):
        raise ValueError("password should contains atleast 1 uppercase letter")
    return "valid password"
    

    
    
       







