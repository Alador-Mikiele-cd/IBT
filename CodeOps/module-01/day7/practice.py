list = [1,2,4,5,6]

# print(list[5]) this is O(1) because it finds it by memorey

for number in list:
    print(number)
# O(n) The loop runs once for every item in the list
# If there are n items, there are n operations

for i in list:
    for j in list:
        print( i , j)

# O(n^2) it loops n * n

students = {
    "alador":18,
    "bereket":20
}

print(students["alador"])
 # O(n) it just go to alador directly without going throue every items


def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50, 60]

print(binary_search(numbers, 40))

# O(log n) each step cuts the search space in half