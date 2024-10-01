import unittest
from tictactoe import player

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

if __name__ == '__main__':
    unittest.main()