#! /usr/bin/env python3
import re
import imp


def strip_down_to_AZ(string_to_strip):
    pattern = "[A-Z]"
    string_to_strip = str(string_to_strip).upper()
    return re.findall(pattern, string_to_strip)

if __name__ == "__main__":
    open_file,file_name,descripion = imp.find_module("3.2.1.py")
    imp.load_module("3.2.2.py", open_file, file_name,descripion)
    #ask for string to encrypt
    string_to_encrypt = input("Input string to encrypt: ")

    #only allow A-Z characters
    print(strip_down_to_AZ(string_to_encrypt))
