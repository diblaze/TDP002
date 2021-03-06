#! /usr/bin/env python3
from functools import reduce

def operations(func):
    """
        Laboration 1a omgjord till lambda funktioner.
    """
    print(reduce(func,range(1,513)))


#lambda for adding two numbers together
plus = lambda x1, x2: x1 + x2
#lambda for multiplying two numbers
multiply = lambda x1, x2: x1 * x2


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

def generate_list(function, amount):
    """
        Uses the inputted function for every index and returns a list
    """
    return list(map(function, range(1, amount + 1)))

def partial(function, amount):
    """
        Returns a lambda function that takes the inputted function and and hard copies the second parameter into the first lambda argument.
    """
    return lambda x: function(amount, x)

def compose(first_function, second_function):
    """
        Takes the second function and uses it as a input for first function.
    """
    return lambda x: first_function(second_function(x))

def make_filter_map(first_filter, second_filter):
    """

    """
    map_fixed = partial(map, second_filter)
    filter_fixed = partial(filter, first_filter)

    return compose(list, compose(filter_fixed, map_fixed))


if __name__ == "__main__":
    operations(plus)
    operations(multiply)

    print(dbsearch("name", "Jakob"))

    haystack = "Can you find the needle in this haystack?".split()
    print(contains("needle", haystack))
    print(contains("on", haystack))

