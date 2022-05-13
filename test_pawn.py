import unittest
import config
from pawn import *
import board_states as boards
from game_state import GameState


class TestPawn(unittest.TestCase):
    data = {
            "player_2": "uno",
            "player_1": "dos",
            "score_2": 0.0,
            "walls": 10.0,
            "score_1": 0.0,
            "side": "N",
            "remaining_moves": 50.0,
            "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ",
            "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
            "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        }
    game = GameState(data)

    
    def test_constructor(self):
        row = 0
        col = 5
        side = 'N'
        base = 0
        target = config.ROWS - 1
        
        pawn = Pawn(row, col, side)

        self.assertEqual(pawn.pos.row, row)
        self.assertEqual(pawn.pos.col, col)
        self.assertEqual(pawn.side, side)
        self.assertEqual(pawn.base, base)
        self.assertEqual(pawn.target, target)

    def test_repr(self):
        row = 0
        col = 1
        side = 'N'
        p = Pawn(row, col, side)

        result = f'{side}({row}, {col})'
        self.assertEqual(p.__repr__(), result)

    def test_get_valid_moves_cross(self):
        self.game.update_from_decoded(boards.BOARD_PAWN)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(6, 8),
            Position(8, 6), 
            Position(10, 8),
            Position(8, 10)
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_edge(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_EDGE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(14, 16),
            Position(16, 14), 
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_edge_2(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_EDGE_2)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(12, 16),
            Position(14, 14), 
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_sorrounded(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_OBSTACLE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = []
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_jump(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(4, 8),
            Position(8, 4), 
            Position(12, 8),
            Position(8, 12)
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_jump_edge(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_EDGE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(10, 16),
            Position(14, 14), 
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_jump_edge_sorrounded(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_OBSTACLE_PAWN)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = []
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_corner_1(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_1)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(6, 6),
            Position(6, 10),
            Position(10, 10),
            Position(10, 6),

        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_corner_2(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_2)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(10, 6),
            Position(6, 6),
            Position(6, 10),
            Position(10, 10),
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_corner_3(self):
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_OBSTACLE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(6, 10)
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)



if __name__ == '__main__':
    unittest.main()