def f(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,'*',j,'=',end=' ')
            print('{:<2}'.format(i*j),end='   ')
        print()

m = int(input('Enter an integer:'))
f(m)