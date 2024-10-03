"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    # Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
    

def player(board):
    # Returns player who has the next turn on a board.
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    return 'X' if x_count <= o_count else 'O'


def actions(board):
    # Returns set of all possible actions (i, j) available on the board.
    #print({(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY})
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}  


def result(board, action):
    # Returns the board that results from making move (i, j) on the board.
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception('Invalid action')
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    # Returns the winner of the game, if there is one.
    for player in ['X', 'O']:
        winner_line = [player, player, player]
        # check rows
        for row in board:
            if row == winner_line:
                return player
        # check columns
        for col in range(3):
            if [board[row][col] for row in range(3)] == winner_line:
                return player
        # check diagonals
        if [board[i][i] for i in range(3)] == winner_line:
            return player
        if [board[i][2 - i] for i in range(3)] == winner_line:  
            return player
    return None


def terminal(board):
    # Returns True if game is over, False otherwise.
    if winner(board) is not None:
        return True
    elif not any(EMPTY in row for row in board):
        return True
    return False


def utility(board):
    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    winner_player = winner(board)
    if winner_player == 'X':
        return 1
    elif winner_player == 'O':
        return -1
    else:
        return 0    
    

def minimax(board):
    #Returns the optimal action for the current player on the board.
    
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        #print('max_value, value: ', v)
        return v
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        #print('min_value, value: ', v)
        return v
   
    if terminal(board):
        return None 

    current_player = player(board)
    optimal_value = -math.inf if current_player == X else math.inf
    optimal_action = None

    for action in actions(board):
        if current_player == 'X':    
            v = -math.inf
            value = min_value(result(board, action))
            #print('value: ', value)
            if value > optimal_value:
                optimal_value = value
                optimal_action = action
        elif current_player== 'O':
            v = math.inf
            value = max_value(result(board, action))
            #print('value: ', value)
            if value < optimal_value:
                optimal_value = value
                optimal_action = action
        #print(current_player, ': ', 'Optimal action: ', optimal_action, ' Optimal value: ', optimal_value)
    
    return optimal_action
    
    
 
