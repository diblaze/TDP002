import os
import gameboard
import move
import getch

def clear_terminal():
    """Clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    # if game is started as a program - start game loop

    # load all levels
    levels = gameboard.sokoban_load_levels("sokoban_levels.txt")

    level_choosen = False

    #repeat until user has choosen a level.
    while not level_choosen:
        choosen_level = input("Choose level (1 - {})".format(len(levels))) #get how many levels are loaded in and ask user for level
        if choosen_level.strip().isdigit(): #check if input is a level
            choosen_level = int(choosen_level) #convert to int while removing all spaces.
            choosen_level -= 1 #decrement because level list starts from 0.
            if choosen_level >= 0 and choosen_level <= len(levels): #make sure user enters a level in the level list.
                level_choosen = True

    # load choosen level
    level, objectives = gameboard.sokoban_load(choosen_level, levels)

    # while game is not over, display level and allow player to play.
    while not gameboard.isGameOver(level, objectives):
        #clear terminal
        clear_terminal()
        #display level
        gameboard.sokoban_display(level)

        print("(W/w)up, (S/w)down, (A/a)left, (D/d)right, (Q/q)exit")

        user_input = getch.getch() #get user input
        if user_input.lower() != "q":
            move.player_move(user_input, level)
        else: #user wants to quit
            user_sure = input("Are you sure you want to quit? (y/n)")
            if user_sure.lower() == "y":
                break
    else: #player won!
        clear_terminal()
        gameboard.sokoban_display(level)
        print("You cleared the level!")
