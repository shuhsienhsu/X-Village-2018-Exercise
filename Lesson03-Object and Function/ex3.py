def f(x,y):
    if(x > y):
        return 'a > b'
    elif(x == y):
        return 'a = b'
    elif(x < y):
        return 'a < b'

a = 5
b = 2
result = f(a,b)
print(result)