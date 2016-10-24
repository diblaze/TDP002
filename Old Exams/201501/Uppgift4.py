#! /usr/bin/env python3


import random, sys



if __name__ == "__main__":

    message = input("Meddelande: ")
    #print(len(message))

    encrypt = ""
    

    print(chr(len(message)+32), end="")

    for char in message:
        print(char, end="")
        #print(char)
        for r in range(2):
            i = random.randint(1, 95)
            print(chr(i+32), end="")
            
            for x in range(i):
                print(chr(random.randint(1, 95)), end="")
                
    

