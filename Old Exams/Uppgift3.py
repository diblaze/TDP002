#! /usr/bin/env python3

def counting_sort(list_to_sort):
    r = []

    for value in list_to_sort:
        if len(r) <= value:
            r.extend(0 for _ in range(value+2))
        r[value] += 1
    u = []


    for i, v in enumerate(r):
        u.extend(i for _ in range(v))

    return u

if __name__ == "__main__":

    #numbers = input("Mata in heltal: ")
    numbers = "3 5 2 6 2 6 9 0 19 22 5 23"
    
    numbers = [int(x) for x in numbers.split()]

    print(counting_sort(numbers))