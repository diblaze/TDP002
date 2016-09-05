#! usr/bin/env python3
import time


#Uppgift 1a - Summera alla naturliga tal upp till och med 512
a = 0

for i in range (0, 513):
    a = a + i

print("Summan av alla naturliga tal upp till och med 512 är: " + str(a))

#Uppgift 1b - Produkten av alla positiva heltal upp till och med 512
a = 1

for i in range (1,513):
    a = a * i

print("Produkten av alla positiva heltal upp till och med 512 är: " + str(a))

#Uppgift 1c - Minsta positiva heltalet som är jämt delbart med siffrorna 1 till och med 13
x=1
y=False
#while we have not found a number that is divisble by 1..13 - loop
while y == False:
    x += 1
    i = 1
    #check if 'x' is divisable by 'i', while 'i' is not 13
    #this while-loop will exit itself if 'x' is divisable by all numbers between 1..13.
    #if 'x' is not divisable by 'i', exit loop and try with a higher number.
    while x % i == 0 and i <= 13:
        i += 1 
        if i > 13:
            y=True    
print("Minsta positiva heltalet som är jämnt delbart med siffrorna 1 till och med 13 är: " + str(x))

#Uppgift 1d - Summera alla primtal under 1000
sum_of_prime = 0;

def is_prime(number):
    #check if number given is larger than 1
    if number > 1:
        #check if number given can be divisible by all numbers between 1 up to the number given.
        for i in range(2, number):
            #if number is divisible by anything between 1 up to the number itself - it is not prime
            if number % i == 0:
                return False
        return True
    #number given is either 1, or lower than 1.
    else:
        return False

start = time.time()
#interval to check
for i in range(1, 1001):
    #if i is prime - add to sum_of_prime
    if is_prime(i):
        sum_of_prime += i    
end = time.time()
#print out the sum of all primes under 1000.
print("Summan av alla primtal under 1000 är: " + str(sum_of_prime))
print("Det tog " + str((end - start) * 1000) + " ms att hitta alla primtal under 1000")

