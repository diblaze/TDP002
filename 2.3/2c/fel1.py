#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factor(multiplicator):
    return 10*multiplicator

def fraction(divisor):
    return 10.0 / divisor

def power(exponent):
    return 10**exponent
 
#RÄTTAT: Parantes fattades.
print("with x = 1 to 10:")
# print 10 multiplicated by numbers 1 to 10
numbers = []
for x in range(10):
    #RÄTTAT: facor -> factor
    numbers.append(str(factor(x)))
print("   10 multiplicated with x:", ", ".join(numbers))


# print 10 divided by the numbers 1 to 10
numbers = []
#RÄTTAT: Kan inte dela med 0! Bytte från range(10) till range(1,11)
for x in range(1,11):
    numbers.append(str(fraction(x)))
print("   10 divided by x:", ", ".join(numbers))

# print 10 raised to the power of the numbers 1 to 10
numbers = []
for x in range(10):
    #RÄTTAT: kan inte skicka in "int" när den förväntar sig "sträng".
    numbers.append(str(power(x)))    
print("   10 raised to x:", ", ".join(numbers))
