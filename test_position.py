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
        none = None
        
        self.assertEqual(pos1, pos2)
        self.assertNotEqual(pos1, pos3)
        self.assertNotEqual(pos2, pos3)
        self.assertNotEqual(pos1, none)


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
        # print('Test Rotate Move')
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
        # print('Test get shortest path')
        path = []
        pos = None
        moves = []
        shortest = get_shortest_path(pos, moves, path)
        result = []
        self.assertEqual(shortest, result)

    def test_get_shortest_path_1(self):
        # print('Test get shortest path')
        path = []
        pos = Position(0, 0)
        pos.depth = 0
        pos.parent = -1
        moves = [pos]
        shortest = get_shortest_path(pos, moves, path)
        result = [pos]
        self.assertEqual(shortest, result)
    
    def test_get_shortest_path_2(self):
        # print('Test get shortest path 2')
        pos = Position(0, 0)
        pos.depth = 0
        pos.parent = -1

        pos2 = Position(1, 0)
        pos2.depth = 1
        pos2.parent = 0

        path = []
        moves = [pos, pos2]
        result = [pos2]
        
        shortest = get_shortest_path(pos2, moves, path)
        self.assertEqual(shortest, result)

    def test_get_shortest_path_3(self):
        # print('Test get shortest path 2')
        initial = [16, 0, 9, 40]
        steps = [[0, 2, 0, 0], [0, 0, 1, 0], [2, 2, 1, 0], [0, 4, 1, 0], [2, 0, 2, 1], [4, 2, 2, 2], [2, 4, 2, 2], [0, 6, 2, 3], [4, 0, 3, 4], [6, 2, 3, 5], [4, 4, 3, 5], [2, 6, 3, 6], [6, 0, 4, 8], [8, 2, 4, 9], [6, 4, 4, 9], [4, 6, 4, 10], [2, 8, 4, 11], [8, 0, 5, 12], [10, 2, 5, 13], [8, 4, 5, 13], [6, 6, 5, 14], [4, 8, 5, 15], [2, 10, 5, 16], [10, 0, 6, 17], [12, 2, 6, 18], [10, 4, 6, 18], [8, 6, 6, 19], [6, 8, 6, 20], [4, 10, 6, 21], [0, 10, 6, 22], [2, 12, 6, 22], [12, 0, 7, 23], [14, 2, 7, 24], [12, 4, 7, 24], [10, 6, 7, 25], [8, 8, 7, 26], [6, 10, 7, 27], [4, 12, 7, 28], [0, 12, 7, 29], [2, 14, 7, 30], [14, 0, 8, 31], [14, 4, 8, 32], [12, 6, 8, 33], [10, 8, 8, 34], [8, 10, 8, 35], [6, 12, 8, 36], [4, 14, 8, 37], [2, 16, 8, 39], [16, 0, 9, 40]]
       
        pos_initial = Position(initial[0], initial[1])
        pos_initial.depth = initial[2]
        pos_initial.parent = initial[3]

        visited = []
        for step in steps:
            pos = Position(step[0], step[1])
            pos.depth = step[2]
            pos.parent = step[3]     
            visited.append(pos)   

        result_steps = [[0, 0, 1, 0], [2, 0, 2, 1], [4, 0, 3, 4], [6, 0, 4, 8], [8, 0, 5, 12], [10, 0, 6, 17], [12, 0, 7, 23], [14, 0, 8, 31], [16, 0, 9, 40]]
        result = []
        for step in result_steps:
            pos = Position(step[0], step[1])
            pos.depth = step[2]
            pos.parent = step[3]     
            result.append(pos) 
        result.reverse()
        shortest = get_shortest_path(pos_initial, visited, [])

        self.assertEqual(shortest, result)
        

if __name__ == '__main__':
    unittest.main()