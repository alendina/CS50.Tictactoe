import tictactoe as ttt

board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
print('\nminimax: ', ttt.minimax(board), '\n')