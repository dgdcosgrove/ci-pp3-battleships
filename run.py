#Import functionality to generate random integers
from random import randint

def make_board():
    """
    Create board to contain game
    """
    board = []
    
    for x in range(0, 5):
        board.append(["0"] * 5)
    
    for row in board:
        print("---".join(row))

print("Welcome to Battleships!")
print("Please choose a number between 0 and 4")
print("Legend: Top left is row 0 and column 0")
make_board()


