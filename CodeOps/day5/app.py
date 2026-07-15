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
