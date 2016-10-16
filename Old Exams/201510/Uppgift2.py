#! /usr/bin/env python3
import date

if __name__ == "__main__":
    userInput = input("Mata in ett datum: ")

    d = date.to_date(userInput)

    for i in range(10000):
        d = date.next_date(date.year(d), date.month(d), date.day(d))

    d = date.to_string(d)
    print("10 000 dagar senare: " + d)