import unittest
from wall import *

class TestPosition(unittest.TestCase):
    
    def test_constructor(self):
        # print('Test Wall Constructor')
        row = 4
        col = 6
        orientation = 'h'
        turn_token = 'token123'
        game_id = 'gameId123'

        wall = Wall(row, col, turn_token, game_id)
        wall.orientation = orientation


        self.assertEqual(wall.pos.row, row)
        self.assertEqual(wall.pos.col, col)
        self.assertEqual(wall.orientation, orientation)
        self.assertEqual(wall.turn_token, turn_token)
        self.assertEqual(wall.game_id, game_id)

    def test_json(self):
        # print('Test Wall Json')
        row = 2
        col = 6
        orientation = 'h'
        turn_token = 'token123'
        game_id = 'gameId123'

        wall = Wall(row, col, turn_token, game_id)
        wall.orientation = orientation     

        json_data = wall.json()
        result = {"row": 1, "col": 3, "orientation": "h", "turn_token": "token123", "game_id": "gameId123"}

        self.assertEqual(json_data, result)

    def test_blocks(self):
        # print('Test Wall Blocks')

        row = 2
        col = 6
        orientation = 'h'
        turn_token = 'token123'
        game_id = 'gameId123'

        wall = Wall(row, col, turn_token, game_id)
        wall.orientation = orientation

        blocks = wall.blocks()

        pos1 = Position(3, 6)
        pos2 = Position(3, 8)
        pos3 = Position(2, 7)
        pos4 = Position(4, 7)
        result = [pos1, pos2, pos3, pos4]
        
        self.assertEqual(blocks, result)


if __name__ == '__main__':
    unittest.main()