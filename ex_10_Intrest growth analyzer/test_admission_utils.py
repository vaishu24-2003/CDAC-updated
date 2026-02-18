from admission_utils import check_admission

try:
    print(check_admission(75, 20, "Mumbai"))   # Approved
    print(check_admission(60, 19, "Delhi"))    # Denied
    print(check_admission(80, 17, "Pune"))     # Denied
    print(check_admission(85, 21, "Chennai"))  # Error

except Exception as e:
    print("Error:", e)
