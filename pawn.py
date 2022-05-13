import config
import utils
import copy
from position import Position

class Pawn:
    def __init__(self, row, col, side):
        self.pos = Position(row, col)
        self.side = side
        self.base = 0 if self.side == 'N' else config.ROWS - 1 
        self.target = config.ROWS - 1 if self.side == 'N' else 0

    def __repr__(self) -> str:
        return f'{self.side}({self.row}, {self.col})'

