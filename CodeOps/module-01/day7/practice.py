x = 5
sum = 1
while 1 <= x:
    sum *= x 
   
    x -= 1

print(sum)

a = 'a'
c = 'a'
print(a is c)


def linear_search(list , target):
    for i,x in enumerate(list):
        print(f'{i} => {x}')
        if x == target:
            return f' it is on{i}'
    return 'not found'

# print(linear_search(list , 12))







def binary_search(list , target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif target > list[mid]:
             right = mid + 1
             
        elif target < list[mid]:
            left = mid - 1
        else:
             return 'not found'
            
            
   
list = [1,3,5,2,12] 
print(binary_search(list , 1))


class Bankconfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance
    
x = Bankconfig()
print(x)
y =  Bankconfig()
print(y == x)
        

class Animal:
    def __init__(self,sound,name):
        self.sound = sound
    def speak(self):
        return f'{self.sound}'
    
class dog(Animal):
    def __init__(self, sound,bav):
        super().__init__(sound)
        self.bav = bav

    def how(self):
        return self.bav

dog = dog("wooo",'loyal')

print(dog.speak())
print(dog.how())
print(dog.sound)
