def find_player(board):
    """
        Finds the player in the level.
    """

    for item in board:
        if item[0] == "@":
            return item
    return None

def find_in_board(x, y, board):
    """
        Finds all objects on a specific tile in the level
    """
    item_list = [] # temp list
    for item in board: # go through each object in level
        if x == item[1] and y == item[2]: #if object matches the x and y coordinates
            item_list.append(item) #add the item to the temp list.

    return item_list #returns a list with all objects on the specific tile.
