#! /usr/bin/env python3
import random
import deck


# solitare alfabet
letters_to_keys_list = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
                        "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
                        "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
                        "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

keys_to_letters_list = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G",
                        8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N",
                        15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",
                        22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

def __find_jokers(deck):
    """Find all the jokers in the deck"""
    jokers = [0, 0]

    for position, item in enumerate(deck):
        if item == joker_a:
            jokers[0] = position
    for position, item in enumerate(deck):
        if item == joker_b:
            jokers[1] = position
    # print(jokers)
    return jokers


def __move_jokers(deck, pos_a=None, pos_b=None):
    """Move the specificed joker in deck"""
    # if joker_a is the last card in deck, remove it and insert it under the
    # first card on top.
    if pos_a != None and pos_b == None:
        if pos_a == len(deck):
            deck.pop(deck.index(joker_a))
            deck.insert(1, joker_a)
            pos_a = 1
        # if joker_a is not last card in deck, then move it down one card.
        else:
            deck.pop(deck.index(joker_a))
            deck.insert(pos_a + 1, joker_a)
            pos_a += 1

    if pos_b != None and pos_a == None:
        # if joker_b is last card in deck, then remove it and insert it under the
        # second top card
        if pos_b == len(deck) - 1:
            deck.pop(deck.index(joker_b))
            deck.insert(2, joker_b)
            pos_b = 2

        # if joker_b is second last card in deck, remove it and insert it under
        # the top card
        elif pos_b == len(deck) - 2:
            deck.pop(deck.index(joker_b))
            deck.insert(1, joker_b)
            pos_b = 1
        # joker_b is not last/second last, move it back two positions
        else:
            deck.pop(deck.index(joker_b))
            deck.insert(pos_b + 2, joker_b)
            pos_b += 2

    if pos_a != None:
        #print("New position for first joker is: " + str(pos_a))
        return pos_a
    else:
        #print("New position for second joker is: " + str(pos_b))
        return pos_b


def __rearrange_joker_list(joker_list):
    """Sorts the joker list according to position in deck."""

    if joker_list[0] > joker_list[1]:
        joker_list[0], joker_list[1] = joker_list[1], joker_list[0]

    return joker_list


def solitaire_keystream(length=30, deck=deck.create_deck()):
    """Creates the keystream needed for encrypting the string"""

    # inserts the jokers into the deck
    deck.insert_card_by_dict(joker_a, deck)
    deck.insert_card_by_dict(joker_b, deck)
    # shuffles the deck
    solitaire_deck = []
    solitaire_deck = deck.shuffle_deck(deck)

    deck_a = []
    deck_b = []
    deck_c = []

    # solitaire key
    key = ""

    while len(key) != length:

        jokers = [0, 0]
        # find jokers
        jokers = __find_jokers(solitaire_deck)

        # move joker a
        jokers[0] = __move_jokers(solitaire_deck, jokers[0], None)

        # find jokers again because deck changed because of joker a
        jokers = __find_jokers(solitaire_deck)
        # move joker b
        jokers[1] = __move_jokers(solitaire_deck, None, jokers[1])
        # rearrange the joker list to them in correct order
        jokers = __rearrange_joker_list(jokers)
        #print("Jokers: " + str(jokers))

        # all cards from top to first joker
        deck_a = solitaire_deck[0:jokers[0]]
        # all cards between first and second joker, including jokers
        deck_b = solitaire_deck[jokers[0]:jokers[1] + 1]
        # all cards after the last joker
        deck_c = solitaire_deck[jokers[1] + 1:len(deck) - 1]
        # updated deck
        solitaire_deck = deck_c + deck_b + deck_a

        # get value of bottom card
        value_of_top_card = get_value_of_card(
            len(solitaire_deck) - 1, solitaire_deck)

        # split deck from top to number of cards needed
        deck_a = solitaire_deck[0:value_of_top_card]
        # split deck from the rest remaining to second last card
        deck_b = solitaire_deck[value_of_top_card:len(deck) - 2]
        # takes the last card
        deck_c = solitaire_deck[len(deck) - 2: len(deck) - 1]

        # reorder the deck -> card that were NOT rearranged + cards that were
        # rearranged + last card that was not touched
        solitaire_deck = deck_b + deck_a + deck_c

        value_of_key_card = 0
        # top cards value

        #get value of top card
        value_of_top_card = get_value_of_card(0, solitaire_deck)
        #get suit of top card
        suit_of_top_card = get_suit_of_card(0, solitaire_deck)

        #if top card is Hearts, then double the value according to the assignment.
        if(suit_of_top_card == "Hearts"):
            value_of_top_card += 13

        #get the key card to be used
        if value_of_top_card <= 27:
            value_of_key_card = get_value_of_card(
                value_of_top_card + 1, solitaire_deck)

        #if key card is not a joker then add the correct letter to keypass.
        if value_of_key_card != 27:
            key += keys_to_letters_list[value_of_key_card]
            # print(key)

    return key


def __debug_functions():
    """Debugs all functions by testing them once"""
    #debug_deck = create_deck()
    #print(debug_deck)  # should print out all cards in the newly created deck.
    #debug_card = display_card(10, debug_deck)
    # print(debug_card)
    # print(pick_card(debug_card))
    #insert_card_by_name("three of spades", debug_deck)
    #insert_card_by_dict(joker_a, debug_deck)

    deck = create_deck()
    print(solitaire_keystream(30, deck))

#if __name__ == "__main__":
    #print(solitaire_keystream(30, deck=create_deck()))
