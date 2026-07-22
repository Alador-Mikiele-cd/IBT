class BankConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
    

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
    def __init__(self, owner, account_no, bal):
        super().__init__(owner, account_no, bal)
        self.rate = BankConfig().interest_rate
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
    def __init__(self, owner, account_no, bal):
        super().__init__(owner, account_no, bal)
        self.over = BankConfig().overdraft_limit

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



class AccountFactory:
    @staticmethod
    def create(kind,owner,number,balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown type: {kind}")    







accs1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500  )
accs1.add_interest()
print(accs1.statement)

print('=--------------------------------------')

accs2 = AccountFactory.create("current", "Almaz", "CBE-1", 1500 )
accs2.withdraw(200)
print(accs2.statement)








# accounts = [acc, sav, cur]

# for account in accounts:
#     print(account.statement)
    














