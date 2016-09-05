#! usr/bin/env python3

def Stars(amount_of_stars, is_flag):
	"""Returns the amount of stars asked for"""
	if not is_flag:
		return ("*" * (amount_of_stars+4)) #Adds four extra stars to close the gaps
	elif is_flag:
		return ("*" * (amount_of_stars))

def Flag(width):
	flag = []
	proper_width = width*22
	for i in range (1,5):
		flag.append(Stars(proper_width//2, True) + " " + Stars(proper_width//2, True))
	flag.append("")
	for i in range (1,5):
                flag.append(Stars(proper_width//2, True) + " " + Stars(proper_width//2, True)) 
	return flag

def BlockOffWithStars(string):
	"""Puts a star at the beginning and at the end of a string"""
	return ("* " + string + " *")

def SurroundWithStars(string):
	"""Surronds a string with stars"""
	#Get length of string to output correct amount of stars under and over
	length_of_string = len(string)
	print(Stars(length_of_string, False))
	print(BlockOffWithStars(string))
	print(Stars(length_of_string, False))

SurroundWithStars("Hello")

for i in Flag(2):
	print(i)
