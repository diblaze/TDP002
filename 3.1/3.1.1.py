#! /usr/bin/env python3
import random

# acc. to assignment we only need two suits (half of deck)
suits = {"spades": 1, "hearts": 2}
values = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
          "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13}

joker_a = ["joker_a", 27]
joker_b = ["joker_b", 27]


def create_deck():
    """Creates a deck of 26 cards (-2 jokers)"""
    # list to hold the deck
    _deck = []
    for i in range(1, 3):
        for j in range(1, 14):
            _deck.append([i, j])

    return _deck


def shuffle_deck(deck_to_shuffle):
    """Shuffles a deck.
    The shuffle occurs IN PLACE, but for others to better understand this function I will return the same deck but shuffeled."""
    random.shuffle(deck_to_shuffle)

    return deck_to_shuffle


def pick_card(deck_to_pick_from):
    """Returns a random card from the deck"""
    return random.choice(deck_to_pick_from)


def insert_card_by_name(card_in_text, deck_to_insert_into):
    """Adds a new card to the last postion of the deck
    Use by inputting card either by text or by [i,j].
    """
    splitted_string = card_in_text.split()
    value = splitted_string[0]
    value = values[value]

    suit = splitted_string[2]
    if suit == "spades" or suit == "Spades":
        suit = 0
    elif suit == "hearts" or suit == "Hearts":
        suit = 1

    card_to_add = [suit, value]

    deck_to_insert_into.append(card_to_add)


def insert_card_by_dict(card, deck_to_insert_into):
    """Adds a new card to the last postion of the deck
    Use by inputting card by [i,j].
    """
    deck_to_insert_into.append(card)
    print(card)


def get_value_of_card(position_of_card, deck):
    """Returns the value of the card that has the specific position in the deck"""
    print(deck[position_of_card])
    value_int = deck[position_of_card][1]

    return value_int


def get_suit_of_card(position_of_card, deck):
    """Returns the suit of the card that has the specific position in the deck"""
    suit_int = list(deck[position_of_card][0])

    if suit_int == 0:
        return "Spades"
    elif suit_int == 1:
        return "Hearts"


def display_card(position_of_card, deck):
    """Displays the card in the specific position in the deck."""
    suit = get_suit_of_card(position_of_card, deck)
    value = str(get_value_of_card(position_of_card, deck))

    text_printed = value + " of " + suit
    return text_printed


def solitaire_keystream(length=30, deck=create_deck()):

    # inserts the jokers into the deck
    insert_card_by_dict(joker_a, deck)
    insert_card_by_dict(joker_b, deck)
    # shuffles the deck
    solitaire_deck = []
    solitaire_deck = shuffle_deck(deck)

    deck_a = []
    deck_b = []
    deck_c = []

    # solitare alfabet
    keys_list = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
                 "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
                 "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
                 "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

    # solitaire key
    key = ""

    while len(key) != length:

        position_of_joker_a = 0
        position_of_joker_b = 0
        # find joker a
        for position, i in enumerate(solitaire_deck):
            if i == joker_a:
                position_of_joker_a = position
        # find joker b
        for position, i in enumerate(solitaire_deck):
            if i == joker_b:
                position_of_joker_b = position

        # TODO: Refactor to MoveJokers()
        # if joker_a is the last card in deck, remove it and insert it under the
        # first card on top.
        if position_of_joker_a == len(solitaire_deck) - 1:
            solitaire_deck.pop(solitaire_deck.index(joker_a))
            solitaire_deck.insert(1, joker_a)
            position_of_joker_a = 1
        # if joker_a is not last card in deck, then move it down one card.
        else:
            solitaire_deck.pop(solitaire_deck.index(joker_a))
            solitaire_deck.insert(position_of_joker_a + 1, joker_a)
            position_of_joker_a += 1

        # if joker_b is last card in deck, then remove it and insert it under the
        # second top card
        if position_of_joker_b == len(solitaire_deck) - 1:
            solitaire_deck.pop(solitaire_deck.index(joker_b))
            solitaire_deck.insert(2, joker_b)
            position_of_joker_b = 2

        # if joker_b is second last card in deck, remove it and insert it under
        # the top card
        elif position_of_joker_b == len(solitaire_deck) - 2:
            solitaire_deck.pop(solitaire_deck.index(joker_b))
            solitaire_deck.insert(1, joker_b)
            position_of_joker_b = 1
        # joker_b is not last/second last, move it back two positions
        else:
            solitaire_deck.pop(solitaire_deck.index(joker_b))
            solitaire_deck.insert(position_of_joker_b + 2, joker_b)
            position_of_joker_b += 2

        joker_postions = [0, 0]
        if position_of_joker_a > position_of_joker_b:
            joker_postions[0] = position_of_joker_b
            joker_postions[1] = position_of_joker_a
        else:
            joker_postions[0] = position_of_joker_a
            joker_postions[1] = position_of_joker_b


        # TODO: Refactor to SplitDecks()
        # all cards from top to first joker
        deck_a = solitaire_deck[0:joker_postions[0]]
        # all cards between first and second joker, including jokers
        deck_b = solitaire_deck[joker_postions[0]:joker_postions[1] + 1]
        # all cards after the last joker
        deck_c = solitaire_deck[joker_postions[1] + 1:len(deck) - 1]
        # updated deck
        solitaire_deck = deck_c + deck_b + deck_a


        # TODO:FIX THIS SHIT
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


        value_of_key_card = 0;
        # top cards value
        print("here")
        value_of_top_card = get_value_of_card(0, solitaire_deck)
        if value_of_top_card != 27:
            # card to use to encode into key
            value_of_key_card = get_value_of_card(
                value_of_top_card + 1, solitaire_deck)

        if value_of_key_card != 27:
            for i, item in enumerate(keys_list):
                if(i == value_of_key_card):
                    print(str(i) + " - " + item)


    return key


def debug_functions():
    """Debugs all functions by testing them once"""
    #debug_deck = create_deck()
    # print(debug_deck)  # should print out all cards in the newly created deck.
    #debug_card = display_card(10, debug_deck)
    # print(debug_card)
    # print(pick_card(debug_card))
    #insert_card_by_name("three of spades", debug_deck)
    #insert_card_by_dict(joker_a, debug_deck)

    deck = create_deck()
    print(solitaire_keystream(30, deck))

if __name__ == "__main__":
    debug_functions()
