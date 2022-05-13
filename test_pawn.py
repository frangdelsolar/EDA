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

    def test_get_valid_moves(self):
        self.game.update_from_decoded(boards.BOARD_PAWN)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        self.game.show(moves)
        # moves = get_valid_moves(p.pos, p.side, boards.BOARD_PAWN)
        # print(moves)


if __name__ == '__main__':
    unittest.main()