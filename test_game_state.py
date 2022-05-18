import unittest
from game_state import *
import board_states as boards
from position import Position, append_pos, rotate_moves


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
        # print('Test Game State Constructor')
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
        self.assertEqual(len(self.game.player_scores), 3)
        self.assertEqual(len(self.game.opponent_scores), 3)

    def test_update_from_decoded(self):
        # print('Test Game State Update from Decoded')
        self.game.update_from_decoded(boards.BOARD_PAWN)
        self.assertEqual(len(self.game.player_pawns), 1)
        self.assertEqual(len(self.game.opponent_pawns), 0)
        self.assertEqual(self.game.state, boards.BOARD_PAWN)
        self.game = GameState(self.data)
    
    def test_decode_board(self):
        # print('Test Game State Decode Board')
        result = decode_board(self.encoded)
        self.assertEqual(self.decoded, result)

    def test_encode_board(self):
        # print('Test Game State Encode Board')
        result = encode_board(self.decoded)
        self.assertEqual(self.encoded, result) 

    def test_create_pawns(self):
        # print('Test Game State Create Pawns')
        pawns = create_pawns('N', self.game)
        p1 = pawns[0]
        self.assertEqual(p1.score(), 1)
        self.assertEqual(len(pawns), 3)

    def test_within_boundaries(self):
        # print('Test Game State Pos Within Boundaries')
        in_pos = Position(5, 5)
        out_pos = Position(-1, 19)

        self.assertTrue(within_boundaries(in_pos))
        self.assertFalse(within_boundaries(out_pos))
        
    def test_is_cell_wall(self):
        # print('Test Game State Pos Is Wall')
        wv = Position(0, 15)
        wh = Position(11, 0)
        nw = Position(0, 0)

        self.assertTrue(is_cell_wall(wv, self.decoded))
        self.assertTrue(is_cell_wall(wh, self.decoded))
        self.assertFalse(is_cell_wall(nw, self.decoded))

    def test_is_cell_engaged(self):
        # print('Test Game State Pos Is Engaged')
        s = Position(16, 0)
        n = Position(2, 10)
        empty = Position(0, 0)

        self.assertTrue(is_cell_engaged(s, self.decoded))
        self.assertTrue(is_cell_engaged(n, self.decoded))
        self.assertFalse(is_cell_engaged(empty, self.decoded))

    def test_is_cell_engaged_by_opponent(self):
        # print('Test Game State Pos is engaged by opponent')
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

    def test_rotate_matrix(self):
        # print('Test Game State Rotate Matrix')
        m1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
            [3, 4, 5, 6]
        ]

        result = [
            [3, 9, 5, 1],
            [4, 0, 6, 2],
            [5, 1, 7, 3],
            [6, 2, 8, 4]
        ]

        m1_r = rotate_matrix(m1)

        self.assertEqual(m1_r, result)
    
    def test_get_pawn_scores_S(self):
        # print('Test Game State Get Pawn Distances')
        p1 = Pawn(16, 0, 'S')
        p2 = Pawn(16, 4, 'S')
        p3 = Pawn(0, 5, 'S')

        pawns = [p1, p2, p3]

        distances = get_pawn_scores(pawns)
        result = [1, 1, 256]

        self.assertEqual(distances, result)

    def test_get_pawn_scores_N(self):
        # print('Test Game State Get Pawn Distances')
        p1 = Pawn(0, 0, 'N')
        p2 = Pawn(0, 4, 'N')
        p3 = Pawn(16, 5, 'N')

        pawns = [p1, p2, p3]

        distances = get_pawn_scores(pawns)
        result = [1, 1, 256]

        self.assertEqual(distances, result)

    def test_get_board_score(self):
        # print('Test Game State Score')
        score = get_board_score(self.game)
        self.assertEqual(score, 0)
        
    def test_get_board_score_2(self):
        # print('Test Game State Score 2')
        data = {
            "player_2": "uno",
            "player_1": "dos",
            "score_2": 0.0,
            "walls": 10.0,
            "score_1": 0.0,
            "side": "S",
            "remaining_moves": 50.0,
            "board": "              N N                 N                                                                    |           |    *           *    |           |S                          |S               *          | |   |          * *              | |    S      |                *                | ",
            "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
            "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        }
        game = GameState(data)
        # game.show()

        self.assertAlmostEqual(game.score, 22)

    def test_update_state_from_move(self):
        data = {
            "player_2": "uno",
            "player_1": "dos",
            "score_2": 0.0,
            "walls": 10.0,
            "score_1": 0.0,
            "side": "N",
            "remaining_moves": 50.0,
            "board": "              N N                 N                                                                    |           |    *           *    |           |S                          |S               *          | |   |          * *              | |    S      |                *                | ",
            "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
            "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        }
        game = GameState(data)
        move = {
            'from_col': 0,
            'from_row': 1,
            'game_id': 'ab16e71c-caeb-11eb-975e-0242c0a80004',
            'side': 'N',
            'to_col': 0,
            'to_row': 2,
            'turn_token': '087920d0-0e6b-4716-9e77-add550a006aa'
        }

        # game.show()        
        game.update_state_from_move(move)
        board = encode_board(game.state)
        result = "              N N                                                   N                                  |           |    *           *    |           |S                          |S               *          | |   |          * *              | |    S      |                *                | "
        self.assertEqual(board, result)

    def test_create_state_from_move(self):
        # print('Test Game State create from move')
        data = {
            "player_2": "uno",
            "player_1": "dos",
            "score_2": 0.0,
            "walls": 10.0,
            "score_1": 0.0,
            "side": "N",
            "remaining_moves": 50.0,
            "board": "              N N                 N                                                                    |           |    *           *    |           |S                          |S               *          | |   |          * *              | |    S      |                *                | ",
            "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
            "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        }
        game = GameState(data)
        move = {
            'from_col': 0,
            'from_row': 1,
            'game_id': 'ab16e71c-caeb-11eb-975e-0242c0a80004',
            'side': 'N',
            'to_col': 0,
            'to_row': 2,
            'turn_token': '087920d0-0e6b-4716-9e77-add550a006aa'
        }
        new_game = create_state_from_move(move, game)
        # new_game.show()
        self.assertEqual(new_game.side, 'S')
        self.assertEqual(new_game.player_scores, [16, 8, 2])
        self.assertEqual(new_game.opponent_scores, [1, 1, 4])
        self.assertAlmostEqual(new_game.score, 20)

    def test_move_minimax(self):
        move = self.game.move_minimax(3)
        result = {
            'from_row': 0, 
            'from_col': 1, 
            'to_row': 0, 
            'to_col': 0, 
            'game_id': 'ab16e71c-caeb-11eb-975e-0242c0a80004', 
            'turn_token': '087920d0-0e6b-4716-9e77-add550a006aa'
        }
        self.game.show()
        self.assertEqual(move, result)

    def test_get_possible_moves(self):
        # print('Test Game State Get Possible Moves')
        # n1 = get_valid_moves(self.game.player_pawns[0].pos, self.game.player_pawns[0].side, self.game.state)
        # n2 = get_valid_moves(self.game.player_pawns[1].pos, self.game.player_pawns[1].side, self.game.state)
        # n3 = get_valid_moves(self.game.player_pawns[2].pos, self.game.player_pawns[2].side, self.game.state)
        # neighbours = n1 + n2 + n3
        # self.game.show(neighbours)
        
        moves = self.game.get_possible_moves()
        result = [{'from_row': 0, 'from_col': 1, 'to_row': 0, 'to_col': 0, 'side': 'N'}, {'from_row': 0, 'from_col': 1, 'to_row': 1, 'to_col': 1, 'side': 'N'}, {'from_row': 0, 'from_col': 1, 'to_row': 0, 'to_col': 2, 'side': 'N'}, {'from_row': 0, 'from_col': 4, 'to_row': 0, 'to_col': 3, 'side': 'N'}, {'from_row': 0, 'from_col': 4, 'to_row': 1, 'to_col': 4, 'side': 'N'}, {'from_row': 0, 'from_col': 4, 'to_row': 0, 'to_col': 5, 'side': 'N'}, {'from_row': 0, 'from_col': 7, 'to_row': 0, 'to_col': 6, 'side': 'N'}, {'from_row': 0, 'from_col': 7, 'to_row': 1, 'to_col': 7, 'side': 'N'}, {'from_row': 0, 'from_col': 7, 'to_row': 0, 'to_col': 8, 'side': 'N'}]

        self.assertEqual(moves, result)

if __name__ == '__main__':
    unittest.main()