# Tic Tac Toe
# v.0.1.1

from MathFunctionLib import mathplus

turn_1 = "Player 1's Turn"
turn_2 = "Player 2's Turn"

loop_activator = 0

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

while board:
    while loop_activator == 0:
        print(turn_1)
        circle = input("> ")

        if circle == "1":
            board[0][0] = 0
            
            mathplus.row(board)

            loop_activator = 1
        if circle == "2":
            board[0][1] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "3":
            board[0][2] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "4":
            board[1][0]

            mathplus.row(board)

            loop_activator = 1
        if circle == "5":
            board[1][1] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "6":
            board[1][2] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "7":
            board[2][0] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "8":
            board[2][1] = 0

            mathplus.row(board)

            loop_activator = 1
        if circle == "9":
            board[2][2]

            mathplus.row(board)

            loop_activator = 1
    while loop_activator == 1:
        print(turn_2)
        x = input("> ")

        if x == "1":
            board[0][0] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "2":
            board[0][1] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "3":
            board[0][2] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "4":
            board[1][0] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "5":
            board[1][1] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "6":
            board[1][2] ="x"

            mathplus.row(board)

            loop_activator = 0
        if x == "7":
            board[2][0] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "8":
            board[2][1] = "x"

            mathplus.row(board)

            loop_activator = 0
        if x == "9":
            board[2][2] = "x"

            mathplus.row(board)

            loop_activator = 0
        if circle == "goaway":
            quit(0)