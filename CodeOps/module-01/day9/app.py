


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
        self.history = []
    
    def deposit(self,amount):
        if amount  <= 0:
            raise ValueError("amount must be positive")
        self._bal += amount
        self.history.append(("deposit", amount))
        return f' you have deposited {amount} '
    def withdraw(self,amount):
        if amount  >= self._bal:
            raise ValueError("amount must be less then you balnace")
        self._bal -= amount
        self.history.append(("withdraw", amount))
        return f' you have withdraw {amount} '
    @property
    def statement(self):
        return ( f"Account Type: Account\n"
            f"Owner: {self.owner}\n"
            f"Account No: {self.account_no}\n"
            f"Balance: {self._bal}")
    def total_transactions(self):
        def _count(history):
            if not history:
                return 0
            return 1 + _count(history[1:])
        return _count(self.history)

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
# print(accs1.statement)

print('=--------------------------------------')

accs2 = AccountFactory.create("current", "Almaz", "CBE-1", 1500 )
accs2.withdraw(200)
# print(accs2.statement)






class AccountRegistry:
    def __init__(self):
        self.number = {}
        self.order = []
    def add(self,acc):
        self.number[acc.account_no] = acc
        self.order.append(acc.account_no)
        return acc
    def find(self,number):
        account = self.number.get(number)
        if account is None:
            raise ValueError("account not found")
        return account
    def list_all(self):
        return [self.number[n] for n in self.order]
    def top_balance(self,n):
        return sorted(self.number.values(),key=lambda acc:acc._bal,reverse=True)[:n]
    def binary_search(self,list , target):
        left = 0
        right = len(list) - 1
        while left <= right:
            mid = (left + right) // 2
            if list[mid] == target:
                return mid
            elif target > list[mid]:
                left = mid + 1
                
            else:
                right = mid - 1
            
        return -1
    def find_by_number(self,number):
        sorted_no = sorted(self.number.keys())
        i = self.binary_search(sorted_no, number)
        if i == -1:
             raise ValueError("account not found")
        return self.number[sorted_no[i]]

            
            
class Branch:
    def __init__(self,name):
        self.name = name
        self.children = []
        self.accounts = []
    def add_branch(self,branch):
        self.children.append(branch)
        return branch
    def add_account(self,acc):
        self.accounts.append(acc)
        return acc
    def total_balance(self):
        own = 0
        for acc in self.accounts:
            own += acc._bal
        for child in self.children:
            own += child.total_balance()
        return own
def bfs(graph , start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node , []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


accs1 = AccountFactory.create("savings", "Almaz", "CBE-1", 1500  )
accs1.add_interest()
# print(accs1.statement)

print('=--------------------------------------')

accs2 = AccountFactory.create("current", "Almaz", "CBE-1", 1500 )
accs2.withdraw(200)
# print(accs2.statement)





    

registry = AccountRegistry()
registry.add(AccountFactory.create("savings", "alador", "CBE-1", 1500))
acc = registry.find("CBE-1")


# print(acc.statement)


registry = AccountRegistry()

registry.add(AccountFactory.create("savings", "Almaz", "CBE-1", 1500))
registry.add(AccountFactory.create("current", "Bereket", "CBE-2", 3000))

acc = registry.find("CBE-1")
acc.deposit(100)
acc.withdraw(50)

# print(acc.statement)
# print("total_transactions:", acc.total_transactions())

# print(registry.top_balance(1)[0].statement)

# print(registry.find_by_number("CBE-2").statement)



head_office = Branch("Head Office")

addis_region = Branch("Addis Region")
tigray_region = Branch("Tigray Region")

head_office.add_branch(addis_region)
head_office.add_branch(tigray_region)

bole_branch = addis_region.add_branch(Branch("Bole Branch"))
piassa_branch = addis_region.add_branch(Branch("Piassa Branch"))
mekelle_branch = tigray_region.add_branch(Branch("Mekelle Branch"))

bole_branch.add_account(registry.find("CBE-1"))
bole_branch.add_account(registry.find("CBE-2"))



print("Bank total balance:", head_office.total_balance())

transfers = {
        "CBE-1": ["CBE-2", "CBE-3"],
        "CBE-2": ["CBE-4"],
        "CBE-3": ["CBE-1"],
        "CBE-4": [],
    }

reachable = bfs(transfers, "CBE-1")
print("CBE-1 can reach:", reachable)