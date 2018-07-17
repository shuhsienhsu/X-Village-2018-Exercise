import random

class HungryException(Exception):
    def __init__(self, amount):
        self.status = amount
    def __str__(self):
        return "I'm hungry(status:" + str(self.status) + "), need to eat!"
class ThirstyException(Exception):
    def __init__(self, amount):
        self.status = amount
    def __str__(self):
        return "I'm thirsty(status:" + str(self.status) + "), need to drink!"
class BoredException(Exception):
    def __init__(self, amount):
        self.status = amount
    def __str__(self):
        return "I'm bored(status:" + str(self.status) + "), need to play!"

def check(man):
    if(man["hunger"] < 0):
        raise HungryException(man["hunger"])
    elif(man["water"] < 0):
        raise ThirstyException(man["water"])
    elif(man["mood"] < 0):
        raise BoredException(man["mood"])
    # TODO: in what condition need to raise exception?
    
def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)
def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)
def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)
    
actionList = [play, eat, drink]
    
child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    #cnt -= 1
    rand = random.randint(0,2)
    try:
        actionList[rand](child)
    except HungryException as e:
        print(e)
        break
    except ThirstyException as e:
        print(e)
        break
    except BoredException as e:
        print(e)
        break
    # TODO: 把隨機的動作用 try...except 包起來   
    #actionList[rand](child)
    # TIPS: 記得只要抓到 exception 之後就要 break 了，不然會造成無窮迴圈 