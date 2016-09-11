#! /usr/bin/env python3
import random

# acc. to assignment we only need two suits (half of deck)
#spades = 1..13
#hearts = 1..13 * 2
suits = {"spades": 1, "hearts": 2}
values = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
          "eight": 8, "nine": 9, "ten": 10, "elseven": 11, "twelve": 12, "thirteen": 13}

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
    #random seed is set to 10 to ensure same passkey.
    random.seed(10)
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
    # print(card)


def get_value_of_card(position_of_card, deck):
    """Returns the value of the card that has the specific position in the deck"""
    # print(deck[position_of_card])
    value_int = deck[position_of_card][1]

    return value_int

def get_suit_of_card(position_of_card, deck):
    """Returns the suit of the card that has the specific position in the deck"""
    suit_int = deck[position_of_card][0]

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
