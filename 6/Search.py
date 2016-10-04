#! /usr/bin/env python3

imdb = [{"title": "Raise your voice", "actress": "Hilary Duff", "score": 6},
        {"title": "Coherence", "actress": "Emily Baldoni", "score": 7},
        {"title": "Pulp Fiction", "actor": "John Travolta", "score": 9},
        {"title": "Lie To Me", "actor": "Tim Roth", "score": 10},
        {"title": "Perception", "actress": "Rachael Leigh Cook", "actor": "Eric McCormack", "score": 10}]

def linear_search(list_to_search_in, key_to_search_for, field = lambda item: item["title"]):
    """
        Does a linear search through a list.
        Defaults to searching for "title" if no other field is specified.
    """

    if len(list_to_search_in) == 0 or key_to_search_for == None:
        return "Error"

    #list to put all found items in
    list_with_found_items = []

    #go through every item in the list
    for item in list_to_search_in:
        #if the search key is in list[field], append to list and go on
        if str(key_to_search_for).lower() in str(field(item)).lower():
            list_with_found_items.append(item)
            continue
    return list_with_found_items

def binary_search(list_to_search_in, key_to_search_for, field = lambda item: item["title"]):
    """
        Does a binary search through a list containing dictionaries.
        Defaults to searching for "title" if no other filed is specified.
    """

    if len(list_to_search_in) == 0:
        return "Error"

    #to make the search work with lowercase and uppercase - make everything to lowercase.
    field_to_use = lambda l: field(l).lower()

    key_to_search_for = key_to_search_for.lower()
    #sort the list, because binary only works on sorted lists.
    list_to_search_in = sorted(list_to_search_in, key = field_to_use)

    #init low, high.
    low = 0
    high = len(list_to_search_in) - 1

    #while we have not found the item yet
    while low <= high:
        #get middle of list
        mid = (low + high) // 2
        #if search key is at a lower index than mid
        if field_to_use(list_to_search_in[mid]) > key_to_search_for:
            high = mid - 1
        #if search key is at a higher index than mid
        elif field_to_use(list_to_search_in[mid]) < key_to_search_for:
            low = mid + 1
            #item is found
        else:
            return list_to_search_in[mid]

    #if nothing was found in list.
    return "No such item in list."


if __name__ == "__main__":
    #print(linear_search(imdb, "voice"))
    #print(linear_search(imdb, 10, lambda item: item["score"]))
    #print(binary_search(imdb, "Lie to me", lambda item: item["title"]))



