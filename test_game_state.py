import unittest
from game_state import *
from wall import Wall
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
        self.assertEqual(len(self.game.player_distances), 3)
        self.assertEqual(len(self.game.opponent_distances), 3)

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
        self.assertEqual(len(p1.path), 9)
        self.assertEqual(p1.distance, 9)
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
    
    def test_get_pawn_distances(self):
        # print('Test Game State Get Pawn Distances')
        p1 = Pawn(0, 0, 'S')
        p1.distance = 9

        p2 = Pawn(0, 4, 'S')
        p2.distance = 6

        p3 = Pawn(4, 5, 'S')
        p3.distance = 5

        pawns = [p1, p2, p3]

        distances = get_pawn_distances(pawns)
        result = [9, 6, 5]

        self.assertEqual(distances, result)

    def test_move_shortest(self):
        # print('Test Game State Move')
        move = self.game.move_shortest()
        result = {
            'from_row': 0, 
            'from_col': 1, 
            'to_row': 0, 
            'to_col': 0, 
            'game_id': 'ab16e71c-caeb-11eb-975e-0242c0a80004', 
            'turn_token': '087920d0-0e6b-4716-9e77-add550a006aa'
        }
        self.assertEqual(move, result)

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
            "side": "N",
            "remaining_moves": 50.0,
            "board": "              N N                 N                                                                    |           |    *           *    |           |S                          |S               *          | |   |          * *              | |    S      |                *                | ",
            "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
            "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        }
        game = GameState(data)
        # game.show()
        self.assertAlmostEqual(game.score, -0.0166667)

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
        self.assertEqual(new_game.side, 'S')
        self.assertEqual(new_game.player_distances, [5, 5, 8])
        self.assertEqual(new_game.opponent_distances, [7, 8, 6])
        self.assertAlmostEqual(new_game.score, 0.012499999999999997)

    # def test_move_minimax(self):
    #     move = self.game.move_minimax(2)
    #     result = {
    #         'from_row': 0, 
    #         'from_col': 1, 
    #         'to_row': 0, 
    #         'to_col': 0, 
    #         'game_id': 'ab16e71c-caeb-11eb-975e-0242c0a80004', 
    #         'turn_token': '087920d0-0e6b-4716-9e77-add550a006aa'
    #     }
    #     # self.game.show()
    #     # print(move)
    #     self.assertEqual(move, result)

    def test_get_possible_moves(self):
        # print('Not yet implemented')
        return False

    def test_can_place_wall(self):
        # print('Test Game State Can Place Wall')
        turn_token = 'token123'
        game_id = 'game123'
        
        w1 = Wall(0, 14, turn_token, game_id)

        w1.orientation = 'v'
        w1v = can_place_wall(w1, self.decoded)
        self.assertFalse(w1v)

        w1.orientation = 'h'
        w1h = can_place_wall(w1, self.decoded)
        self.assertTrue(w1h)

        w2 = Wall(2, 14, turn_token, game_id)

        w2.orientation = 'v'
        w2v = can_place_wall(w2, self.decoded)
        self.assertFalse(w2v)

        w2.orientation = 'h'
        w2h = can_place_wall(w2, self.decoded)
        self.assertTrue(w2h)
        

        w3 = Wall(10, 0, turn_token, game_id)

        w3.orientation = 'v'
        w3v = can_place_wall(w3, self.decoded)
        self.assertTrue(w3v)

        w3.orientation = 'h'
        w3h = can_place_wall(w3, self.decoded)
        self.assertFalse(w3h)
        
       
        w4 =  Wall(10, 2, turn_token, game_id)

        w4.orientation = 'v'
        w4v = can_place_wall(w4, self.decoded)
        self.assertTrue(w4v)

        w4.orientation = 'h'
        w4h = can_place_wall(w4, self.decoded)
        self.assertFalse(w4h)
     
        w5 =  Wall(0, 0, turn_token, game_id)
        
        w5.orientation = 'v'
        w5v = can_place_wall(w5, self.decoded)
        self.assertTrue(w5v)

        w5.orientation = 'h'
        w5h = can_place_wall(w5, self.decoded)
        self.assertTrue(w5h)

    # def test_new_wall(self):
    #     self.game.new_wall()

    def test_index_of_range(self):
        data = {"side": "S", "score_2": 2635.0, "board": "      N N   N    -*- -*- -*-   -*-         |         -*-    *                |       -*-   -*-         |                *  -*-           |                   -*-                             -*-                                                                 -*-         -*-  S S       S    ", "remaining_moves": 31.0, "score_1": 3816.0, "player_1": "frangdelsolar@gmail.com", "player_2": "frangdelsolar@gmail.com", "walls": 1.0, "turn_token": "ecf03bbb-3ca6-4e0c-8f34-0cb9b139f56e", "game_id": "1385a7d0-daee-11ec-aef0-7ecdf393f9cc"}
        game = GameState(data)
        game.move_shortest()
        game.new_wall()

if __name__ == '__main__':
    unittest.main()