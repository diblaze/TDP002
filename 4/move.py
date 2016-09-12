import search_board

def can_player_move(direction, player, board):
    """
        Returns a tile IF the player can move to it.
    """
    if direction.lower() == "d":
        return move(1, 0, player, board)
    elif direction.lower() == "a":
        return move(-1, 0, player, board)
    elif direction.lower() == "w":
        return move(0, -1, player, board)
    elif direction.lower() == "s":
        return move(0, 1, player, board)
    else:
        return None, None

def get_new_x_cord(old_x_cord, length):
    return(old_x_cord + length)

def get_new_y_cord(old_y_cord, length):
    return(old_y_cord + length)


def move(x_delta, y_delta, obj, board, is_box=False):
    """
        Checks if the tile given is moveable to.
        If a box is in the way, check if the box can be pushed.
    """
    new_x_cord = get_new_x_cord(obj[1], x_delta)
    new_y_cord = get_new_y_cord(obj[2], y_delta)
    item = search_board.find_in_board(new_x_cord, new_y_cord, board) #find all items on the tile specified
    #print(new_x_cord, new_y_cord, obj, item, is_box)
    if len(item) == 0: # if there is nothing on the tile, or if there is a storage area
        return (new_x_cord, 1) if y_delta == 0 else (new_y_cord, 2) #player can move there, return tile from players POV.
    elif item[0][0] == '.' and len(item) == 1: # if there's a storage area on place and only a dot
        return (new_x_cord, 1) if y_delta == 0 else (new_y_cord, 2) #player can move there, return tile from players POV.
    elif item[0][0] == "#": #if there is a wall on the tile - nothing can move to it then.
        return None, None
    elif item[0][0] == "o" and is_box == False: #if the tile has a box on it, check if it can be moved and move
        return(move_box(x_delta, y_delta, item[0], obj, board))
    elif len(item) > 1 and item[1][0] == "o" and is_box == False:
            return(move_box(x_delta, y_delta, item[1], obj, board))
    else:
        return None, None

def move_box(x_delta, y_delta, box, player, board):
    """
       Moves box if possible and returns player position for player
    """
    new_x_cord = get_new_x_cord(player[1], x_delta)
    new_y_cord = get_new_y_cord(player[2], y_delta)
    #print(x_delta, y_delta, box, player)
    box_tile, box_axis = move(x_delta, y_delta, box, board, is_box=True) #recursive - check if the box can move to the next time by using "move" function again.
    if box_tile != None and box_axis != None: #if the box can be moved
        board[board.index(box)][box_axis] = box_tile #move the box
        return (new_x_cord, 1) if y_delta == 0 else (new_y_cord, 2) #return tile for player to move to.
    else:
        return None, None


def player_move(direction, board):
    """
        Moves the player in the direction specified.
    """

    player = search_board.find_player(board) #find player in level
    player_index = board.index(player) #find player index in level list
    tile_to_move_to, axis = can_player_move(direction, player, board) #get tile to move to, if possible

    try:
        board[player_index][axis] = tile_to_move_to #move player if possible
    except TypeError:
        print("Can not go in that direction!") #print error message - if the player can't move.
