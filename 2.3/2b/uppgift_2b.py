#! usr/bin/env python3
import os

def create_shopping_list():
	return ["Kurslitteratur", "Anteckningsblock", "Penna"]

def show_shopping_list(slist):
	for i, item in enumerate(slist):
		print((str(i+1) + ". " + item))

def add_shopping_list(slist):
	clear_terminal()	
	show_shopping_list(slist)

	item_to_add = input("Vad ska läggas till i listan? ")
	slist.append(item_to_add)

	clear_terminal();
	show_shopping_list(slist)

def remove_shopping_list(slist):
	clear_terminal()	
	show_shopping_list(slist)

	item_to_remove = input("Vad ska tas bort from listan? (Namn krävs) ")

	if item_to_remove in slist:
		slist.remove(item_to_remove)
		clear_terminal()	
	else:
		clear_terminal();
		print("Finns inget i listan med det namnet!")

	show_shopping_list(slist)

def edit_shopping_list(slist):
	clear_terminal()	
	show_shopping_list(slist)

	item_to_edit = input("Vad ska ändras i listan? (Namn krävs) ")
	
	if item_to_edit in slist:
		edited = input("Vad ska stå istället för \"" + item_to_edit + "\"? ")
		index_of_item = slist.index(item_to_edit)
		slist[index_of_item] = edited
		clear_terminal()	
	else:
		clear_terminal()	
		print("Finns inget i listan med det namnet!")
	
	show_shopping_list(slist)

def clear_terminal():
	os.system("cls" if os.name == "nt" else "clear")