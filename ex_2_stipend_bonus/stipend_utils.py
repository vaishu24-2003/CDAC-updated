def calculate_stipend_bonus(stipend,rating):
    """ Bonus is calculated using rating.
    for eg:if stipend is 20000 and rating is 3 then bonus is 2000
    if rating is 5 bonus is 30 percent which is equal to 0.30 """
    print("ID of stipend:", id(stipend))
    print("ID of rating:", id(rating))
    if stipend<=0:
        raise ValueError("value should only be positive")
    if (type(rating) != int and rating != 0) or (rating > 5):
        raise TypeError("rating should be int only and should be less than 5")

    if(rating==5):
       bonus=stipend*0.30
    elif(rating==4):
        bonus=stipend*0.20
    elif(rating==3):
        bonus=stipend*0.10
    else:
        bonus=0
    return bonus


        