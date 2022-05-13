import unittest
from game_state import *
import board_states as boards
from position import Position



class TestGameState(unittest.TestCase):
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
    encoded = "               |                *           N    |                        N     N                                                                                                     S    -*-                                                                                  S         S      "
    decoded = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', '|', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', 'N', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' '], 
        ['-', '*', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
        ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
    game = GameState(data)
    
    def test_constructor(self):
        self.assertEqual(self.game.board, self.data['board'])
        self.assertEqual(self.game.player_1, self.data['player_1'])
        self.assertEqual(self.game.player_2, self.data['player_2'])
        self.assertEqual(self.game.side, self.data['side'])
        self.assertEqual(self.game.remaining_moves, self.data['remaining_moves'])
        self.assertEqual(self.game.turn_token, self.data['turn_token'])
        self.assertEqual(self.game.game_id, self.data['game_id'])
        self.assertEqual(self.game.state, boards.BOARD_TEST)
        self.assertEqual(self.game.opponent, 'S')
        self.assertEqual(len(self.game.player_pawns), 3)
        self.assertEqual(len(self.game.opponent_pawns), 3)

    def test_decode_board(self):
        result = decode_board(self.encoded)
        self.assertEqual(self.decoded, result)

    def test_encode_board(self):
        result = encode_board(self.decoded)
        self.assertEqual(self.encoded, result) 

    def test_create_pawns(self):
        pawns = create_pawns('N', self.decoded)
        self.assertEqual(len(pawns), 3)

    def test_within_boundaries(self):
        in_pos = Position(5, 5)
        out_pos = Position(-1, 19)

        self.assertTrue(within_boundaries(in_pos))
        self.assertFalse(within_boundaries(out_pos))
        
    def test_is_cell_wall(self):
        wv = Position(0, 15)
        wh = Position(11, 0)
        nw = Position(0, 0)

        self.assertTrue(is_cell_wall(wv, self.decoded))
        self.assertTrue(is_cell_wall(wh, self.decoded))
        self.assertFalse(is_cell_wall(nw, self.decoded))

    def test_is_cell_engaged(self):
        s = Position(16, 0)
        n = Position(2, 10)
        empty = Position(0, 0)

        self.assertTrue(is_cell_engaged(s, self.decoded))
        self.assertTrue(is_cell_engaged(n, self.decoded))
        self.assertFalse(is_cell_engaged(empty, self.decoded))

    def test_is_cell_engaged_by_opponent(self):
        pos_s = Position(16, 0)
        pos_n = Position(2, 10)
        pos_empty = Position(0, 0)

        s_side = 'S'
        n_side = 'N'

        self.assertTrue(is_cell_engaged_by_opponent(pos_s, self.decoded, n_side))
        self.assertFalse(is_cell_engaged_by_opponent(pos_s, self.decoded, s_side))
        self.assertTrue(is_cell_engaged_by_opponent(pos_n, self.decoded, s_side))
        self.assertFalse(is_cell_engaged_by_opponent(pos_n, self.decoded, n_side))
        self.assertFalse(is_cell_engaged_by_opponent(pos_empty, self.decoded, s_side))

if __name__ == '__main__':
    unittest.main()