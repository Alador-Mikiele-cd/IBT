def getEven(list):
    evenlist = []
    for i ,x in enumerate(list):
        if i % 2 == 0 and x % 2 == 0 :
            
            evenlist.append(x)
    return evenlist
list1 = [1, 2, 3, 6, 4, 8]
list2 = [0, 1, 2, 3, 4]

print(getEven(list2))
