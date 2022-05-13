import unittest
from position import Position

class TestPosition(unittest.TestCase):
    
    def test_constructor(self):
        row = 5
        col = 11
        pos = Position(row, col)

        self.assertEqual(pos.row, row)
        self.assertEqual(pos.col, col)

        
if __name__ == '__main__':
    unittest.main()