def meera(list):
    for i in list:
        for j in list:
            if i * 2 == j:
                return "I am not a Meera array"
           
    return "I am a Meera array"
    
list1 =  [3, 5, -2]
print(meera(list1))

def check(list):
    for i in list:
        if i * 2 in list:
            return "I am not a Meera array"
           
    return "I am a Meera array"
      

print(check(list1))