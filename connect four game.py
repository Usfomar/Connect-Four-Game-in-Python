import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
game_over = False
turn = 0

def create_board(row, col):# initialize the board
    print("\n")
    board = np.full((row, col), '   ')
    return board

def get_col_number(COL_COUNT):#get the number of column
    for x in range(COL_COUNT):
        print("    " + str(x), end='|')

get_col_number(COL_COUNT)

def drop_piece(board, row, col, piece):# put the player choice
    board[row][col] = piece

def is_valid_location(board, col):#to check if the location isvalid 
    if board[ROW_COUNT-1][col] == '   ':
        return board[ROW_COUNT-1][col] == '   '

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == '   ':
            return r

def print_board(board):# starts from bottom to up
    print("\n")
    print(np.flip(board, 0))

def winning_move(board, piece):#To check if this move lead to win
    for w in range(COL_COUNT-3): #check horizontal
        for c in range(ROW_COUNT):
            if board[c][w] == piece and board[c][w+1] == piece and board[c][w+2] == piece and board[c][w+3] == piece:
                return True

    for w in range(COL_COUNT): #check vertical
        for c in range(ROW_COUNT-3):
            if board[c][w] == piece and board[c+1][w] == piece and board[c+2][w] == piece and board[c+3][w] == piece:
                return True

    for w in range(COL_COUNT-3):# check positive digonals
        for c in range(ROW_COUNT-3):
            if board[c][w] == piece and board[c+1][w+1] == piece and board[c+2][w+2] == piece and board[c+3][w+3] == piece:
                return True

    for w in range(COL_COUNT-3):# check negative digonals
        for c in range(3,ROW_COUNT):
            if board[c][w] == piece and board[c-1][w+1] == piece and board[c-2][w+2] == piece and board[c-3][w+3] == piece:
                return True


board = create_board(ROW_COUNT, COL_COUNT)
print(board)


while not game_over:
    # Ask player 1 to play
    if turn == 0:
        col = int(input("Player X turn: "))
        if col > COL_COUNT:
            print("No More Space try another slot")
        else:
            if is_valid_location(board, col):
                row = get_next_open_row(board,col)
                get_col_number(COL_COUNT)
                drop_piece(board,row, col, ' X ')
                if winning_move(board, ' X '):
                    print_board(board)
                    print("\n")
                    print("Player X wins !!!")
                    game_over = True
                    break

    # Ask player 2 to play
    else:
        col = int(input("Player O turn: "))
        if col > COL_COUNT:
            print("No More Space try another slot")
        else:

            if is_valid_location(board, col):
                row = get_next_open_row(board,col)
                get_col_number(COL_COUNT)
                drop_piece(board,row, col, ' O ')
                if winning_move(board, ' O '):
                    print_board(board)
                    print("\n")
                    print("Player O wins !!!")
                    game_over = True
                    break

    print_board(board)
    turn += 1
    turn = turn % 2
