def mul(num):
    if(num == 1):
        return 1
    return num*mul(num-1)

print(mul(10))