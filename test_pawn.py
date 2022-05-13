import unittest
import config
from pawn import *


class TestPawn(unittest.TestCase):
    
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

        
if __name__ == '__main__':
    unittest.main()