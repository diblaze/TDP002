#! /usr/bin/env python3
from functools import reduce

def operations():
    """
        Laboration 1a omgjord till lambda funktioner.
    """
    #lambda for adding two numbers together
    plus = lambda x1, x2: x1 + x2
    #lambda for multiplying two numbers
    multiply = lambda x1, x2: x1 * x2

    operators = [plus, multiply]
    for func in operators:
        print(reduce(func,range(1,513)))


def dbsearch(field_to_match, search):
    db = [
            {"name": "Jakob", "position": "assistant"},
            {"name": "Åke", "position": "assistant"},
            {"name": "Ola", "position": "examiner"},
            {"name": "Henrik", "position": "assistant"}
            ]

    matched_entries = [item for item in db if item[field_to_match] == search]
    return matched_entries

def contains(word_to_search_for, sentence):
    return bool(list(filter(lambda word: word == word_to_search_for, sentence)))


if __name__ == "__main__":
    operations()

    print(dbsearch("name", "Jakob"))

    haystack = "Can you find the needle in this haystack?".split()
    print(contains("needle", haystack))
    print(contains("on", haystack))
