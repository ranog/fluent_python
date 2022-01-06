def _print_tic_tac_toe_board(board: list):
    for lines in board:
        print(lines)


board = [['_'] * 3 for i in range(3)]
print('A tic-tac-toe board:')
_print_tic_tac_toe_board(board=board)

print()

board[1][2] = 'X'
print("board[1][2] = 'X'")
_print_tic_tac_toe_board(board=board)

print()

print('A list with three references to the same list:')
weird_board = [['_'] * 3] * 3
_print_tic_tac_toe_board(weird_board)

print()

weird_board[1][2] = 'O'
print("weird_board[1][2] = 'O'")
_print_tic_tac_toe_board(weird_board)
