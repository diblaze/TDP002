#! /usr/bin/env python3
import random
import re

if __name__ == "__main__":
    number = input("Mata in ett heltal: ")
    number = int(number)

    list_of_random_numbers = [format(random.randint(0, 59), "02") for x in range(number)]
    

    print(list_of_random_numbers)

    found = []

    notDone = True
    while notDone:
        i = 0

        if i > len(list_of_random_numbers):
            notDone = False
            continue

        time = str(list_of_random_numbers[i]) + ":" + str(list_of_random_numbers[i+1])
        if(re.match("^[0-2][1-3]:[0-5][0-9]$", time)):
            found.append(time)
        i += 2

        notDone = False

