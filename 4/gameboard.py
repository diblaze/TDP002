import search_board

def sokoban_load_levels(filename):
    """
        Loads all sokoban levels from a file.
        The levels have to be seperated with a new line.
    """
    level_list = []
    board = []
    with open(filename) as level_file:  # open file
        y_axis = 0  # current y_axis we are on.
        for line in level_file:  # for every line in file
            if line == "\n":  # if the current line is a "new line", we reached a new level. Save current level to level list and reset the temp lists.
                level_list.append(board)
                board = []
                y_axis = 0  # reset y_axis
            objects_in_line = list(line) #convert the current line in to a list
            for x, obj in enumerate(objects_in_line): # go through each object in the list
                if obj not in "\n ": #if the object is not a new line, add it to correct temp list
                    add_to_objectlist(obj, x, y_axis,board)

            y_axis += 1 #increment y_axis because we are moving down a line in the file
    return level_list

def sokoban_load(level, level_list):
    """
        Loads a level from level_list
        Index - 0 - 48
    """

    if len(level_list) > 0: #make sure we have a list with levels in them
        amount_of_boxes = 0 #amount of boxes in level
        temp_list = level_list[level] #get the level requested from level_list and put it in a temp list.
        for tile in temp_list: #go through each tile in the level
            if "o" in tile: #if there is a box on the tile
                amount_of_boxes += 1

        return temp_list, amount_of_boxes #return the level requested and the amount_of_boxes in level

def add_to_objectlist(obj, x, y, board):
    """
        Adds the current object to the board
    """

    if obj == '#' or obj == '@' or obj =='o' or obj=='.' :
        board.append([obj, x, y])

def max_x_y(board):
    """Finds the boundaries of the level"""
    x_highest = 0
    y_highest = 0

    for obj in board:
        # make sure obj is a wall
        if obj[0] == "#":
            # if obj x is higher than current x highest
            if x_highest < obj[1]:
                x_highest = obj[1]
            # if obj y is higher than current y highest
            if y_highest < obj[2]:
                y_highest = obj[2]

    return x_highest + 1, y_highest + 1

def sokoban_display(board):
    """Displays the board"""
    x_max, y_max = max_x_y(board) #find the boundaries of the level

    visual_board = ""

    for y in range(y_max): #go from top line of level to bottom
        for x in range(x_max): #go from left to right in level
            items_to_print = search_board.find_in_board(x, y, board) #find all objects on the current tile of the level
            if len(items_to_print) == 1: #if there is only one item on the tile
                print(items_to_print[0][0], end = '') #print the item
            elif len(items_to_print) == 2: #if there is two items on the tile
                for items in items_to_print: #go through the items and print the correct symbol
                    if "@" in items: #if player is standing on a storage area
                        print("+", end = '')
                    elif "o" in items: #if a box is on a storage area
                        print("*", end = '')
            else: #if there is nothing on the tile
                print(" ", end = '')

        print("")

def isGameOver(level, objectives):
    """
        Checks if the game is over.
    """

    correct_boxes = 0

    for tile in level: #go through each tile in level
        if "o" in tile: #if there is a box on tile
            list_of_items = search_board.find_in_board(tile[1], tile[2], level) #find all items on the tile
            if len(list_of_items) > 1: #if there is two items on tile
                for item in list_of_items:
                    if "o" in item: #is the box on a storage area?
                        correct_boxes += 1

    return correct_boxes == objectives
