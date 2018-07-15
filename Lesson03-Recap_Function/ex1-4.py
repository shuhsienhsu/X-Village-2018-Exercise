def income(score,hour):
    amount = 0
    if(score > 90):
        amount += 8000
    elif(score >= 70 and score <=90):
        amount +=6000
    else:
        amount +=4000
    amount += hour*200
    return amount

a = income(55,14)
b = income(96,13)
c = income(85,22)

print(a)
print(b)
print(c)