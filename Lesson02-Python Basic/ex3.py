import random

answer = random.randint(1,100)
guess = 0

while True:
    guess = int(input('Enter a number :'))
    if(guess < answer):
        print('Too small')
    elif(guess > answer):
        print('Too big')
    elif(guess == answer):
        print('Correct')
        break