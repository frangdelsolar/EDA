import unittest
from position import *

class TestPosition(unittest.TestCase):
    
    def test_constructor(self):
        # print('Test Position Constructor')
        row = 5
        col = 11
        pos = Position(row, col)

        self.assertEqual(pos.row, row)
        self.assertEqual(pos.col, col)
        self.assertIsNone(pos.depth)
        self.assertIsNone(pos.depth)

    def test_eq(self):
        # print('Test Position Equality')
        pos1 = Position(0, 0)
        pos2 = Position(0, 0)
        pos3 = Position(1, 0)

        self.assertEqual(pos1, pos2)
        self.assertNotEqual(pos1, pos3)
        self.assertNotEqual(pos2, pos3)

    def test_up(self):
        # print('Test position up')
        r = 5
        c = 5
        pos = Position(r, c)
        amt = 4
        pos.up(amt)
        self.assertEqual(pos.row, r - amt)
        self.assertEqual(pos.col, c)
        
    def test_down(self):
        # print('Test position down')
        r = 5
        c = 5
        pos = Position(r, c)
        amt = 3
        pos.down(amt)
        self.assertEqual(pos.row, r + amt)
        self.assertEqual(pos.col, c)

    def test_right(self):
        # print('Test position right')
        r = 5
        c = 5
        pos = Position(r, c)
        pos.right()
        self.assertEqual(pos.row, r)
        self.assertEqual(pos.col, c + 1)

    def test_left(self):
        # print('Test position left')
        r = 5
        c = 5
        pos = Position(r, c)
        amt = 2
        pos.left(amt)
        self.assertEqual(pos.row, r)
        self.assertEqual(pos.col, c - amt)

    def test_rotate(self):
        # print('Test Position Matrix Rotation')
        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
            [3, 4, 5, 6]
        ]
        pos = Position(0, 0)
        pos.rotate(m)
        self.assertEqual(pos.row, 0)
        self.assertEqual(pos.col, 3)     

        pos2 = Position(2, 1)
        pos2.rotate(m)
        self.assertEqual(pos2.row, 1)
        self.assertEqual(pos2.col, 1)   

    def test_append_pos(self):
        # print('Test append pos to array')
        p1 = Position(0, 0)
        p2 = Position(0, 2)
        p3 = Position(0, 0)
        array = []
        self.assertEqual(len(array), 0)

        array = append_pos(p1, array)
        self.assertEqual(len(array), 1)

        array = append_pos(p2, array)
        self.assertEqual(len(array), 2)

        array = append_pos(p3, array)
        self.assertEqual(len(array), 2)
    
    def test_rotate_moves(self):
        m1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
            [3, 4, 5, 6]
        ]
        p1 = Position(0, 0)
        array = append_pos(p1, [])
        
        p2 = Position(1, 1)
        array = append_pos(p2, array)

        rotated = rotate_moves(array, m1)

        self.assertEqual(p1.row, 0)
        self.assertEqual(p1.col, 3)
        self.assertEqual(p2.row, 1)
        self.assertEqual(p2.col, 2)
        self.assertEqual(len(array), len(rotated))




    def test_get_shortest_path(self):
        print('Test get shortest path')
        # p1 = Position(0, 0)
        # p1.depth = 0
        # p2 = Position(1, 0)
        # p2.depth = 1
        # pos = [
            
        # ]
        print('*******Hay que implementarlo********')
        return False


if __name__ == '__main__':
    unittest.main()