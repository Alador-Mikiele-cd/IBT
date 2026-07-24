def isDual(list):
     for i in list:
        if list.count(i) != 2:
            return 0
     return 1

list = [1,1,2,2,4,4]
print(isDual(list))