def f(x,y):
    return y,x

a = 1
b = 2
(a,b) = f(a,b)

print('a=',a)
print('b=',b)