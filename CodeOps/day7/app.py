


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


class AccountRegistry:
    def __init__(self):
        self.number = {}
        self.order = []

    def add(self,acc):
        self.number[acc.account_no] = acc
        self.order.append(acc.account_no)
        return acc
    def find(self, number):
        account = self.number.get(number)
        if account is None:
            raise ValueError(f"Account {number} not found")
        return account
    def list_all(self):
        return [self.number[n] for n in self.order]
  



accs1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500  )
accs1.add_interest()
# print(accs1.statement)

print('=--------------------------------------')

accs2 = AccountFactory.create("current", "Almaz", "CBE-1", 1500 )
accs2.withdraw(200)
# print(accs2.statement)





    

registry = AccountRegistry()
registry.add(AccountFactory.create("savings", "Almaz", "CBE-1", 1500))
acc = registry.find("CBE-1")


print(acc.statement)










# # x = 5
# # sum = 1
# # while 1 <= x:
# #     sum *= x 
   
# #     x -= 1

# # print(sum)

# # a = 'a'
# # c = 'a'
# # print(a is c)


# # def linear_search(list , target):
# #     for i,x in enumerate(list):
# #         print(f'{i} => {x}')
# #         if x == target:
# #             return f' it is on{i}'
# #     return 'not found'

# # # print(linear_search(list , 12))






# # def binary_search(list , target):
# #     x ,y = 0, len(list) - 1

# #     while x <= y:
# #         mid = (x+y) // 2
# #         if list[mid] == target:
# #             return mid
# #         elif list[mid] < target:
# #             x = mid - 1
# #         else:
# #             x = mid + 1
# #     return -1
# # print(binary_search(list , 3))




# def binary_search(list , target):
#     left = 0
#     right = len(list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if list[mid] == target:
#             return mid
#         elif target > list[mid]:
#              right = mid + 1
             
#         elif target < list[mid]:
#             left = mid - 1
#         else:
#              return 'not found'
            
            
   
# list = [1,3,5,2,12] 
# print(binary_search(list , 1))


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
