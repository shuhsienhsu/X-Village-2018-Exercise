def printout(num):
    mid=num*(num-1)
    def f(x,y):
        if(y == 1 or y == x):
            return 1
        else:
            return f(x-1,y-1) + f(x-1,y)
    for i in range(num):
        for k in range(mid - 2*i):
            print(end=' ')
        for j in range(i+1):
            print('{:<4}'.format(f(i+1,j+1)),end='')
        print()

printout(5)