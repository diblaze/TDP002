#! /usr/bin/env python3
import timeit


def insertion_sort(list_to_sort, field=lambda l: l[0]):
    """
        Insertion sort.
    """
    #goes through the unsorted list
    for i in range(1, len(list_to_sort)):
        j = i - 1
        key = list_to_sort[i]
        #checks if the current iterated field is less then the field we are checking
        while j >= 0 and field(list_to_sort[j]) > field(key):
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        list_to_sort[j + 1] = key


print("_" * 40)
db = [("j", "g"), ("a", "u"), ("k", "l"), ("o", "i"),
      ("b", "s"), ("@", "."), ("p", "s"), ("o", "e")]
print("Before insertion sort")
print(db)
insertion_sort(db, lambda e: e[0])
print("After insertion sort")
print(db)

#db1 = [1,5,8,2,4,9,10]
#insertion_sort(db1, lambda e: e)
# print(db1)


def quick_sort(list_to_sort, field=lambda l: l[0]):
    # three empty arrays
    less, equal, greater = [], [], []
    
    # if we have something to sort
    if len(list_to_sort) > 1:
        
        #take the middle item (any item works)
        pivot = list_to_sort[len(list_to_sort) // 2]
        
        #for each item in the unsorted list, check if the middle item is lesser,greater or equal to the iterated item - do the right action.
        for obj in list_to_sort:
            if field(obj) < field(pivot):
                less.append(obj)
            elif field(obj) == field(pivot):
                equal.append(obj)
            elif field(obj) > field(pivot):
                greater.append(obj)

        return quick_sort(less, field) + equal + quick_sort(greater, field)
    else:
        return list_to_sort
print("_" * 40)

db2 = [1, 5, 6, 7, 3, 2, 1, 5, 6, 3, 2, 6, 9, 8]
print("Before quick sort")
print(db2)
db2 = quick_sort(db2, lambda l: l)
print("After quick sort")
print(db2)
