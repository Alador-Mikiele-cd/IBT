







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
    def __init__(self, owner, account_no, bal,rate):
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
    def __init__(self, owner, account_no, bal,over):
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

acc = Account("Alador", "CBE-10001", 1000)
acc2 = Account("abel","111",200)


sav = SavingsAccount("Abel", "CBE-10002", 2000, 0.10)
sav.add_interest()

cur = CurrentAccount("John", "CBE-10003", 500, 1000)
cur.withdraw(1200)

accounts = [acc, sav, cur]

for account in accounts:
    print(account.statement)
    














