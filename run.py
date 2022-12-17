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

def check_guess(ship_location, user_guess):
    """
    Function to check user guess against ship position
    """
    row, col = user_guess

    if ship_location == user_guess:
        print("You have guessed correctly, the battleship has been sunk!")
    elif row not in range(5) or col not in range(5):
        print("Please select a number between 0-4..")
    elif board[row][col] == "X":
        print("Duplicate selection, please make unique selection..")
    else:
        print("Your guess was incorrect!")
        board[row][col] = "X"
        for row in board:
            print(" --- ".join(row))

def main():
    print("Welcome to Battleships!\n")
    print("Please choose a number between 0 and 4")
    print("Legend: Top left is row 0 and column 0\n")
    make_board()
    ship_location = ship_position(board)
    print("\n")
    user_guess = guess_position()
    print("\n")
    check_guess(ship_location, user_guess)

main()
