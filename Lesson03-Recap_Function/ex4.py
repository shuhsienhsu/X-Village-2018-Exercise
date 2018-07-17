import random

answer = [None] * 4

def set_answer():
    for i in range(4):
        answer[i] = random.randint(0,9)
def judge_guess(guess):
    amount_a = 0
    amount_b = 0
    for i in range(4):
        if(int(guess[i]) == answer[i]):
            amount_a += 1
        else:
            for j in range(4):
                if(i != j):
                    if(int(guess[i]) == answer[j]):
                        amount_b += 1
    return [amount_a,amount_b]

set_answer()
choice = True

while(choice):
    guess = input('Your guess:')
    print(judge_guess(guess))
    if(judge_guess(guess) == [4, 0]):
        print('Correct!')
        c = input('Do you want to start a new game?(y/n)')
        if(c == 'n'):
            choice = False
        elif(c == 'y'):
            set_answer()