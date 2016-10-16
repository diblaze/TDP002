#! /usr/bin/env python3
import math

def binary_search(x):
    start = 0
    end = x

    while start <= end:
        mid = (start + end) // 2

        if mid*mid == x:
            return mid
        elif mid < x:
            start  = mid+1
        else:
            end = mid-1
    
    return start-1

 
if __name__ == "__main__":
    print("{:<6s}{:>4s}".format("Tal", "Rot"))
    for x in range(1, 21):
        print("{:<6d}{:>4d}".format(x, binary_search(x)))