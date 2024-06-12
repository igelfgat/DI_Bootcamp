"""
Given this list:

list1 = [5, 10, 15, 20, 25, 50, 20]

find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

Hint : Look at the index method
"""
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)): #ex with range
    if list1[i] == 20:
        list1[i] *= 10
        break
print(list1)
# example with enumerate
for i, value in enumerate(list1): #ex with range
    if value == 20:
        list1[i] *= 10
        break
print(list1)

#example with index method
list2 = [5, 10, 15, 20, 25, 50, 20]
first_location_20 = list2.index(20)
list2[first_location_20] *= 10
print(list2)


