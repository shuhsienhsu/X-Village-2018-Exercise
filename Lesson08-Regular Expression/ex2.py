import re

class CheckSystem():
    pattern_account = r'(?P<Account>[A-Z][a-z]{2})'
    pattern_password = r'(?P<Password>[a-z]{3}[0][0-9]{5})'
    def checking_account(self, acc):
        match = re.search(self.pattern_account, acc)
        if(match):
            return True
        else:
            print("The format of your account is wrong! You have input:", acc)
            return False
    def checking_password(self, pas):
        match = re.search(self.pattern_password, pas)
        if(match):
            return True
        else:
            print("The format of your password is wrong! You have input:", pas)
            return False
    def final_check(self, acc, pas): #notyet!!!!!!!!!!!!!
        check1 = self.checking_account(acc)
        check2 = self.checking_password(pas)
        if(check1 and check2):
            print("Welcome, ", acc, "!", sep='')
        '''if(self.checking_account(acc) and self.checking_password(pas)):
            print("Valid User!")
            return 
        elif not self.checking_account(acc):
            self.checking_password(pas)
            return'''

account = input("Account:")
password = input("Password:")
check = CheckSystem()
check.final_check(account, password)