import unittest
from tictactoe import player, actions, winner, terminal, utility, result, minimax



class TestTicTacToe(unittest.TestCase):

    def test_player_initial(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(player(board), 'X')

    def test_player_after_one_move(self):
        board = [
            ['X', None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(player(board), 'O')

    def test_player_after_two_moves(self):
        board = [
            ['X', 'O', None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(player(board), 'X')

    def test_player_mid_game(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', None],
            [None, None, None]
        ]
        self.assertEqual(player(board), 'O')

    # test actions function

    def test_actions_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        expected_actions = {(i, j) for i in range(3) for j in range(3)}
        self.assertEqual(actions(board), expected_actions)

    def test_actions_partial_board(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
        expected_actions = {(0, 1), (1, 0), (1, 2), (2, 0), (2, 1)}
        self.assertEqual(actions(board), expected_actions)

    def test_actions_full_board(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        expected_actions = set()
        self.assertEqual(actions(board), expected_actions)

    # test winner function

    def test_winner_initial(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(winner(board), None)
    
    def test_winner_mid_game(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', None],
            [None, None, None]
        ]
        self.assertEqual(winner(board), None)

    def test_winner_draw(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertEqual(winner(board), None)

    def test_winner_x_row(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'O'],
            ['X', 'X', 'X']
        ]
        self.assertEqual(winner(board), 'X')
    
    def test_winner_x_col(self):
        board = [
            ['X', 'O', 'O'],
            ['X', 'X', 'O'],
            ['X', 'O', 'X']
        ]
        self.assertEqual(winner(board), 'X')
    
    def test_winner_o_row(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(winner(board), 'O')

    def test_winner_o_col(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'O', 'X']
        ]
        self.assertEqual(winner(board), 'O')
    
    def test_winner_x_diag(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(winner(board), 'X')
    
    def test_winner_o_diag(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(winner(board), 'O')

    # test terminal function 

    def test_terminal_initial(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertFalse(terminal(board))

    def test_terminal_winning_board(self):
        board = [
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
            [None, None, None]
        ]
        self.assertTrue(terminal(board))

    def test_terminal_full_board_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(terminal(board))

    def test_terminal_ongoing_game(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', None],
            [None, None, 'O']
        ]
        self.assertFalse(terminal(board))

    # test utility function

    def test_utility_initial(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.assertEqual(utility(board), 0)


    def test_utility_x_wins(self):
        board = [
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
            [None, None, None]
        ]
        self.assertEqual(utility(board), 1)

    def test_utility_o_wins(self):
        board = [
            [None, 'X', 'O'],
            [None, 'O', 'X'],
            ['O', None, None]
        ]
        self.assertEqual(utility(board), -1)

    def test_utility_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertEqual(utility(board), 0)

    def test_utility_ongoing_game(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', None],
            [None, None, 'O']
        ]
        self.assertEqual(utility(board), 0)

    # test result function

    def test_result_valid_move(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
        action = (1, 0)
        if player(board) == 'X':
            expected_board = [
                ['X', None, 'O'],
                ['X', 'X', None],
                [None, None, 'O']
            ]
        elif player(board) == 'O':
            expected_board = [
                ['X', None, 'O'],
                ['O', 'X', None],
                [None, None, 'O']
            ]
        self.assertEqual(result(board, action), expected_board)

    def test_result_invalid_move(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
        action = (0, 0)  # Invalid move, position already taken
        with self.assertRaises(Exception):
            result(board, action)

    def test_result_next_player(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
        action = (2, 0)
        new_board = result(board, action)
        self.assertEqual(new_board[action[0]][action[1]], player(board))

    # test minimax function

    def test_minimax_terminal_state(self):
        board = [
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
            [None, None, None]
        ]
        self.assertEqual(minimax(board), utility(board))

    def test_minimax_x_turn(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, 'O']
        ]
        # X should make a move that maximizes its chances of winning
        optimal_action = (1, 2)  # Example optimal action
        self.assertEqual(minimax(board) , optimal_action)

    def test_minimax_o_turn(self):
        board = [
            ['X', 'X', None],
            [None, 'O', None],
            [None, None, None]
        ]
        # O should make a move that minimizes X's chances of winning
        optimal_action = (0, 2)  # Example optimal action
        self.assertEqual(minimax(board), optimal_action)


if __name__ == '__main__':
    unittest.main()