def div(a,b):
    if(b == 0):
        raise ValueError("divisor cannot be zero!")
    else:
        return a/b

try:
    div(1,0)
except Exception as e:
    print(e)
