# Import functionality to generate random integers
from random import randint

def make_board():
    """
    Create board to contain game
    """
    # Gives the variable "board" global scope so it can be used in other functions
    global board
    board = []
    
    for x in range(0, 5):
        board.append(["0"] * 5)
    
    for row in board:
        print("---".join(row))

def ship_row(board):
    """
    Ship placement at random row
    """
    return randint(0, len(board) - 1)

def ship_col(board):
    """
    Ship placement at random column
    """
    return randint(0, len(board) - 1)


print("Welcome to Battleships!\n")
print("Please choose a number between 0 and 4")
print("Legend: Top left is row 0 and column 0\n")
make_board()
ship_row = ship_row(board)
print(ship_row)
ship_col = ship_col(board)
print(ship_col)


