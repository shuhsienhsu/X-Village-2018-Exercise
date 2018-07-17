def mul(num):
    value = 1
    for i in range(num):
        value *= (i + 1)
    return value

print(mul(10))