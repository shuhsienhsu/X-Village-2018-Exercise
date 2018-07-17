def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        div(i, j)