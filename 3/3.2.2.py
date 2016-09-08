#! /usr/bin/env python3
import re
import keystream


def strip_down_to_AZ(string_to_strip):
    """Makes a string to uppercase and strips the string of non-alphabet characters"""
    # only allow A-Z characters
    pattern = "[A-Z]"
    # cast all letters to uppercase.
    string_to_strip = str(string_to_strip).upper()
    # return all letters found.
    return "".join(re.findall(pattern, string_to_strip))


def convert_to_numbers(string_to_convert):
    """Converts A-Z strings to numbers."""
    numbers_from_string = []
    for letter in string_to_convert:
        numbers_from_string.append(keystream.letters_to_keys_list[letter])
    return numbers_from_string


def convert_to_letters(list_to_convert):
    """Converts 0-9 lists to letters."""
    final_string = ""
    for number in list_to_convert:
        final_string += keystream.keys_to_letters_list[number]
    return final_string


def sum_numbers_from_lists(list1, list2):
    temp_list = []
    for i in range(len(list1)):
        temp_num = list1[i] + list2[i]
        if temp_num > 26:
            temp_num -= 26
        temp_list.append(temp_num)
    return temp_list

def subtract_numbers_from_lists(list1, list2):
    temp_list = []
    for i in range(len(list1)):
        temp_num = list1[i] - list2[i]
        if temp_num < 1:
            temp_num += 26
        temp_list.append(temp_num)
    return temp_list



def encrypt_string():
    # ask for string to encrypt
    string_to_encrypt = input("Input string to encrypt: ")
    # strip string
    string_to_encrypt = strip_down_to_AZ(string_to_encrypt)

    # get keystream
    encrypt_key = keystream.solitaire_keystream(len(string_to_encrypt))

    # convert string to numbers
    numbers_from_string = convert_to_numbers(string_to_encrypt)
    print(numbers_from_string)

    # convert encrypt_key to numbers
    encrypt_key_numbers = convert_to_numbers(encrypt_key)
    print(encrypt_key_numbers)

    # sum the numbers list with each other
    # numbers_from_string = [1,5,3]
    # encrypt_key_numbers = [3,6,2]
    # this gives us (1+3),(5+6),(3,2)
    # if number is higher than 26, then remove 26 from number.
    list_of_summed_numbers = sum_numbers_from_lists(
        numbers_from_string, encrypt_key_numbers)
    print(list_of_summed_numbers)
    #print (keystream.keys_to_letters_list[17])

    # convert the final summed list to letters
    encrypted_string = convert_to_letters(list_of_summed_numbers)
    print("Your encrypted string is: " + encrypted_string)

def decrypt_string():
    # ask for string to encrypt
    string_to_decrypt = input("Input string to decrypt: ")
    # strip string
    string_to_decrypt = strip_down_to_AZ(string_to_decrypt)

    # get keystream
    encrypt_key = keystream.solitaire_keystream(len(string_to_decrypt))

    # convert string to numbers
    numbers_from_string = convert_to_numbers(string_to_decrypt)
    #print(numbers_from_string)

    # convert encrypt_key to numbers
    encrypt_key_numbers = convert_to_numbers(encrypt_key)
    #print(encrypt_key_numbers)

    # subtract the numbers list with each other
    # numbers_from_string = [1,5,3]
    # encrypt_key_numbers = [3,6,2]
    # this gives us (1-3+26),(5-6+26),(3-2)
    # if number is lower than 1, then add 26 to number.
    list_of_subtracted_numbers = subtract_numbers_from_lists(numbers_from_string, encrypt_key_numbers)

    decrypted_string = convert_to_letters(list_of_subtracted_numbers)
    print("Your decrypted string is: " + decrypted_string)


if __name__ == "__main__":
    user_input = input("1. Encrypt \n2. Decrypt\nPick an option: ")
    if user_input=="1":
        encrypt_string()
    elif user_input=="2":
        decrypt_string()

    print("Thanks for using my Solitaire encrypter/decrypter!")
