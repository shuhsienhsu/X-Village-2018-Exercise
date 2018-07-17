# TODO: 按照敘述定義出兩個 Exception
class FallDownException(Exception):
    def __init__(self, amount):
        self.status = amount
    def __str__(self):
        return "在" + str(self.status) + "樓被接住了"
class FallDownStrongerException(Exception):
    def __init__(self, amount):
        self.status = amount
    def __str__(self):
        return "在" + str(self.status) + "樓被接住了"

def slip(floor):
    try:
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))

            if floor == 80:
                raise FallDownException(floor)
                # TODO: 要 raise 一個 exception
                
    except FallDownException as e:
        print(e)
        print("突破機關！")
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))
            
            if floor == 5:
                raise FallDownStrongerException(floor)
                # TODO: 要 raise 一個 exception
     
# TODO: 用 try...except 把 slip(106) 包起來
try:
    slip(106)
except FallDownStrongerException as e:
    print(e)
    print("安全")