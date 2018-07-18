import re

class CheckSystem():
    def check_account(self, acc):
        pattern = r'(?P<Account>[A-Z][a-zA-Z0-9]{5,12})'
        match = re.search(pattern, acc)
        if(match):
            return True
        else:
            print("The format of your account is wrong! You have input:", acc)
            return False
    def check_password(self, pas):
        pattern = r'(?P<Password>[a-z0-9]{6,})'
        match = re.search(pattern, pas)
        if(match):
            return True
        else:
            print("The format of your password is wrong! You have input:", pas)
            return False
    def final_check(self, acc, pas):
        check1 = self.check_account(acc)
        check2 = self.check_password(pas)
        if(check1 and check2):
            print("Welcome, ", acc,"!",sep='')

account = input("Account:")
password = input("Password:")
check = CheckSystem()
check.final_check(account, password)