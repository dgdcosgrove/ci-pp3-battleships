# Import functionality to generate random integers
from random import randint


def make_board():
    """
    Create board to contain game
    """
    # Gives the variable "board" global scope
    global board
    board = []

    for x in range(0, 5):
        board.append(["0"] * 5)

    for row in board:
        print(" --- ".join(row))


def ship_position(board):
    """
    Ship placement at random row and column
    """
    return [randint(0, len(board) - 1), randint(0, len(board) - 1)]


def guess_position():

    """
    Function to allow user to guess ship position
    """
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))
    return [guess_row, guess_col]



print("Welcome to Battleships!\n")
print("Please choose a number between 0 and 4")
print("Legend: Top left is row 0 and column 0\n")
make_board()
print("\n")
ship_location = ship_position(board)
print(ship_location)
user_guess = guess_position()
print(user_guess)
