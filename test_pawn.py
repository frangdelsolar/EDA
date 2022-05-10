import unittest
import json
from pawn import *
import board_states

class TestGameState(unittest.TestCase):


    def test_moves_cross(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN
        moves = pawn.get_valid_moves(board)
        expected_output = [{'row': 8, 'col': 10}, {'row': 6, 'col': 8}, {'row': 10, 'col': 8}, {'row': 8, 'col': 6}]
        print('Testing basic move')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)

    def test_moves_cross_obstacles(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN_OBSTACLE
        moves = pawn.get_valid_moves(board)
        expected_output = []
        print('Testing basic move with obstacles')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)

    def test_moves_jump(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN_PAWN
        moves = pawn.get_valid_moves(board)
        expected_output = [{'row': 8, 'col': 12}, {'row': 4, 'col': 8}, {'row': 12, 'col': 8}, {'row': 8, 'col': 4}]
        print('Testing jump')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)


    def test_moves_obstacles(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN_OBSTACLE_PAWN
        moves = pawn.get_valid_moves(board)
        expected_output = []
        print('Testing jump with obstacles')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)

    def test_moves_l_jump_vertical(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN_PAWN_OBSTACLE_1
        moves = pawn.get_valid_moves(board)
        expected_output = [{'row': 6, 'col': 10}, {'row': 10, 'col': 10}, {'row': 6, 'col': 6}, {'row': 10, 'col': 6}]
        print('Testing L jump vertical')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)

    def test_moves_l_jump_horizontal(self):
        pawn = Pawn(8, 8, 'N')
        board = board_states.BOARD_PAWN_PAWN_OBSTACLE_2
        moves = pawn.get_valid_moves(board)
        expected_output = [{'row': 6, 'col': 10}, {'row': 10, 'col': 10}, {'row': 6, 'col': 6}, {'row': 10, 'col': 6}]
        print('Testing L jump horizontal')
        show_state(board, moves)
        self.assertEqual(moves, expected_output)


if __name__ == '__main__':
    unittest.main()