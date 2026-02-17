def evaluate_marks(marks, attendance):
    """
    Grade is calculated based on marks and attendance.

    Rules:
    If attendance < 75, maximum grade is C.
    Otherwise:
    >= 90 -> A
    >= 75 -> B
    >= 50 -> C
    < 50 -> Fail
    """

    
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100")

    if not (0 <= attendance <= 100):
        raise ValueError("Attendance must be between 0 and 100")

  
    if attendance < 75:
        if marks >= 50:
            return "C"
        else:
            return "Fail"

    
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

