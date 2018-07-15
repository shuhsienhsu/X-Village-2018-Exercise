def deter_quadrant(x, y):
    if(x > 0):
        if(y > 0):
            print(1)
        elif(y < 0):
            print(4)
    elif(x < 0):
        if(y > 0):
            print(2)
        elif(y < 0):
            print(3)

deter_quadrant(-1, -10)
deter_quadrant(5, -5)
deter_quadrant(1, 1)
deter_quadrant(-2, 3)