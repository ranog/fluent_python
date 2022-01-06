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
