def make_board():

    board = {}
    columns = 'abcdefgh'
    for i in range(1,9):
        board[i] = {c: ' ' for c in columns}
    

    board[1] = {'a' : '\N{WHITE CHESS ROOK}',
                'b' : '\N{WHITE CHESS KNIGHT}',
                'c' : '\N{WHITE CHESS BISHOP}',
                'd' : '\N{WHITE CHESS QUEEN}',
                'e' : '\N{WHITE CHESS KING}',
                'f' : '\N{WHITE CHESS BISHOP}',
                'g' : '\N{WHITE CHESS KNIGHT}',
                'h' : '\N{WHITE CHESS ROOK}'}
    board[2] = {c : '\N{WHITE CHESS PAWN}' for c in columns}

    board[7] = {c : '\N{BLACK CHESS PAWN}' for c in columns}
    board[8] = {'a' : '\N{BLACK CHESS ROOK}',
                'b' : '\N{BLACK CHESS KNIGHT}',
                'c' : '\N{BLACK CHESS BISHOP}',
                'd' : '\N{BLACK CHESS QUEEN}',
                'e' : '\N{BLACK CHESS KING}',
                'f' : '\N{BLACK CHESS BISHOP}',
                'g' : '\N{BLACK CHESS KNIGHT}',
                'h' : '\N{BLACK CHESS ROOK}'}

    return board

def split(play):
    return play[0], int(play[1])

def make_play(play, board):
    start_pos, end_pos = play.split('-')
    start_pos = split(start_pos)
    end_pos = split(end_pos)
    board[end_pos[1]][end_pos[0]] = board[start_pos[1]][start_pos[0]]
    board[start_pos[1]][start_pos[0]] = ' '

def print_board(board):
    for i in range(8,0,-1):
        for c in 'abcdefgh':
            print(board[i][c], end='')
        print()

board = make_board()

print('Mata in drag:')
while True:
    play = input().strip()
    if not play: break
    make_play(play,board)
print_board(board)