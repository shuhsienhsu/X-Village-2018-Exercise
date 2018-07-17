"""def f(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,'*',j,'=',end=' ')
            print('{:<2}'.format(i*j),end='| ')
        print()

m = int(input('Enter an integer:'))
f(m)"""

RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0], RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            print(str(i) + k['sign'] + str(j) + '=' + '{:>2}'.format(str(k['result'])), end="| ")
    print()