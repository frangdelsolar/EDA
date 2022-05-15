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
        # print('Test Pawn Constructor')
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
        self.assertEqual(pawn.distance, 999999)
        self.assertEqual(pawn.path, [])

    def test_repr(self):
        # print('Test Pawn Repr')
        row = 0
        col = 1
        side = 'N'
        p = Pawn(row, col, side)

        result = f'{side}({row}, {col})'
        self.assertEqual(p.__repr__(), result)

    def test_get_valid_moves_cross(self):
        # print('Test Pawn Get Valid Moves 1')
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
        # print('Test Pawn Get Valid Moves 2')
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
        # print('Test Pawn Get Valid Moves 3')
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
        # print('Test Pawn Get Valid Moves 4')
        self.game.update_from_decoded(boards.BOARD_PAWN_OBSTACLE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = []
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_cross_jump(self):
        # print('Test Pawn Get Valid Moves 5')
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
        # print('Test Pawn Get Valid Moves 6')
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
        # print('Test Pawn Get Valid Moves 7')
        self.game.update_from_decoded(boards.BOARD_PAWN_OBSTACLE_PAWN)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = []
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_corner_1(self):
        # print('Test Pawn Get Valid Moves 8')
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
        # print('Test Pawn Get Valid Moves 9')
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
        # print('Test Pawn Get Valid Moves 10')
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_OBSTACLE)
        p = self.game.player_pawns[0]
        moves = get_valid_moves(p.pos, p.side, self.game.state)
        result = [
            Position(6, 10)
        ]
        # self.game.show(moves)
        # print(moves)
        self.assertEqual(moves, result)

    def test_get_valid_moves_two_pawns(self):
        # print('Test Pawn Get Valid For Two Pawns')
        self.game.update_from_decoded(boards.BOARD_TEST)
        
        p1 = self.game.player_pawns[0]
        moves1 = get_valid_moves(p1.pos, p1.side, self.game.state)

        p2 = self.game.player_pawns[1]
        moves2 = get_valid_moves(p2.pos, p2.side, self.game.state)

        self.assertNotEqual(id(moves1), id(moves2))

    def test_get_valid_moves_in_iterator(self):
        # print('Test Pawn Get Valid Moves 10')
        self.game.update_from_decoded(boards.BOARD_TEST)
        
        p1 = self.game.player_pawns[0]

        moves1 = get_valid_moves(p1.pos, p1.side, self.game.state)
        # self.game.show(moves1)

        p1.pos.right(2)
        
        moves2 = get_valid_moves(p1.pos, p1.side, self.game.state)
        # self.game.show(moves2)
 
        self.assertNotEqual(moves1, moves2)

    def test_bfs(self):
        # print('Test Pawn Breadth First Search Algorithm')
        self.game.update_from_decoded(boards.BOARD_TEST)
        p = self.game.player_pawns[0]
        moves = bfs(p, self.game)
        # self.game.show(moves)
        self.assertEqual(len(moves), 9)

    def test_bfs_2(self):
        # print('Test Pawn Breadth First Search Algorithm 2')
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_OBSTACLE)
        p = self.game.player_pawns[0]
        moves = bfs(p, self.game)
        # self.game.show(moves)
        self.assertEqual(len(moves), 9)
        
    def test_move(self):
        # print('Test Pawn Move')
        self.game.update_from_decoded(boards.BOARD_PAWN_PAWN_OBSTACLE_OBSTACLE)
        p = self.game.player_pawns[0]
        move = p.move()
        result = {
            'from_row': 4,
            'from_col': 4,
            'to_row': 3,
            'to_col': 5,
            'side': 'N'
        }
        self.assertEqual(move, result)

    def test_score_N(self):
        self.game.update_from_decoded(boards.BOARD_BASE)
        p = self.game.player_pawns[0]
        self.assertEqual(p.score(), 1)
        
        p.pos.down(2)
        self.assertEqual(p.score(), 2)

        p.pos.down(14)
        self.assertEqual(p.score(), 256)

    def test_score_S(self):
        self.game.update_from_decoded(boards.BOARD_BASE)
        p = self.game.opponent_pawns[0]
        self.assertEqual(p.score(), 1)
        
        p.pos.up(2)
        self.assertEqual(p.score(), 2)

        p.pos.up(14)
        self.assertEqual(p.score(), 256)

if __name__ == '__main__':
    unittest.main()