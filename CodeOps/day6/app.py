# class Bankconfig:
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.interest_rate = 0.05
#             cls._instance.overdraft_limit = 1000
#         return cls._instance
    
# x = Bankconfig()
# print(x)
# y =  Bankconfig()
# print(y == x)
        

# class Animal:
#     def __init__(self,sound,name):
#         self.sound = sound
#     def speak(self):
#         return f'{self.sound}'
    
# class dog(Animal):
#     def __init__(self, sound,bav):
#         super().__init__(sound)
#         self.bav = bav

#     def how(self):
#         return self.bav

# dog = dog("wooo",'loyal')

# print(dog.speak())
# print(dog.how())
# print(dog.sound)








class Account:
    def __init__(self,owner,account_no,bal):
        self.owner = owner
        self.account_no = account_no
        self._bal = bal
    
    def deposit(self,amount):
        if amount  <= 0:
            raise ValueError("amount must be positive")
        self._bal += amount
        return f' you have deposited {amount} '
    def withdraw(self,amount):
        if amount  >= self._bal:
            raise ValueError("amount must be less then you balnace")
        self._bal -= amount
        return f' you have withdraw {amount} '
    @property
    def statement(self):
        return ( f"Account Type: Account\n"
            f"Owner: {self.owner}\n"
            f"Account No: {self.account_no}\n"
            f"Balance: {self._bal}")
    

class SavingsAccount(Account):
    def __init__(self, owner, account_no, bal,rate=0.10):
        super().__init__(owner, account_no, bal)
        self.rate = rate
    def add_interest(self):
        interest = self._bal * self.rate
        self._bal += interest
    @property
    def statement(self):
        return ( f"Account Type:Saving Account\n"
            f"Owner: {self.owner}\n"
            f"Account No: {self.account_no}\n"
            f"Balance: {self._bal}")
        
    
class CurrentAccount(Account):
    def __init__(self, owner, account_no, bal,over=1000):
        super().__init__(owner, account_no, bal)
        self.over = over

    def withdraw(self,amount):
        if amount  > self._bal + self.over:
            raise ValueError("amount must be less then you balnace")
        self._bal -= amount
        return f' you have withdraw {amount} ' 
    @property
    def statement(self):
        return ( f"Account Type:curreny Account\n"
            f"Owner: {self.owner}\n"
            f"Account No: {self.account_no}\n"
            f"Balance: {self._bal}")   

class BankConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
    


class AccountFactory:
    @staticmethod
    def create(kind,owner,number,balance=0,**kwargs):
        if kind == "savings":
            return SavingsAccount(owner, number, balance,**kwargs)
        if kind == "current":
            return CurrentAccount(owner, number, balance,**kwargs)
        raise ValueError(f"Unknown type: {kind}")    


config = BankConfig()





accs1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500 , rate= config.interest_rate )
accs1.add_interest()
print(accs1.statement)

print('=--------------------------------------')

accs2 = AccountFactory.create("current", "Almaz", "CBE-1", 1500 , over = config.overdraft_limit)
accs2.withdraw(200)
print(accs2.statement)








# accounts = [acc, sav, cur]

# for account in accounts:
#     print(account.statement)
    














