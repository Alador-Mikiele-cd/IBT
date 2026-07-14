class Account:
    def __init__(self,owner,account_no,bal):
        self.owner = owner
        self.account_no = account_no
        self.__bal = bal
    
    def deposit(self,amount):
        if amount  <= 0:
            raise ValueError("amount must be positive")
        self.__bal += amount
        return f' you have deposited {amount} '
    def withdraw(self,amount):
        if amount  >= self.__bal:
            raise ValueError("amount must be less then you balnace")
        self.__bal -= amount
        return f' you have withdraw {amount} '
    @property
    def statement(self):
        return self.__bal
    
alador = Account("Alador",'CBE-100025',10)
abel = Account("alador",'CBE-100066',100)

print(alador.deposit(3000))
print(alador.statement)
print(alador.withdraw(300))
print(alador.statement)



print(alador.deposit(2400))
print(alador.statement)
