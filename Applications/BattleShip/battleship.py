#!/usr/bin/python3

'''
Author:      Michel Zaal
Name:        Battleship CLI version
Description: Simple CLI version of
             the game Battleship
'''

from random import randint

board = []

for x in range(5):
    board.append(['O'] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!\n")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print()
# print(ship_row)
# print(ship_col)


def gues(type):
    try:
        _gues = int(input(f'Guess {type}:'))
    except ValueError:
        _gues = 0
        print('Try again')
        gues(type)
    return int(_gues)


for i in range(5):
    guess_row = gues('Row')
    guess_col = gues('col')

    if guess_row == ship_row and guess_col == ship_col:
        print("\nCongratulations! You sunk my battleship!")
        break
    else:
        if (0 < guess_row > 4) or (0 < guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = 'X'
        print_board(board)

input('\ngame Over')
