import copy
import config


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.depth = None
        self.parent = None

    def __repr__(self) -> str:
        return f'[{self.row}, {self.col}, {self.depth}, {self.parent}]'

    def __eq__(self, o: object) -> bool:
        return (o is not None) and (self.row == o.row and self.col == o.col)

    def up(self, amt=1):
        self.row -= amt
    
    def down(self, amt=1):
        self.row += amt

    def right(self, amt=1):
        self.col += amt

    def left(self, amt=1):
        self.col -= amt

    def rotate(self, matrix, rotation=1):
        for i in range(rotation):
            r = self.row
            c = self.col
            self.row = c
            self.col = len(matrix[0]) - 1 - r

def rotate_moves(moves, matrix):
    for move in moves:
        move.rotate(matrix)
    return moves

def append_pos(pos, array):
    if pos not in array:
        array.append(pos)
    return array

def get_shortest_path(cell, moves, path):
    if cell is None:
        return path
    path.append(cell)

    prev_cell = None
    if cell.parent > 0:
        prev_cell = moves[cell.parent]

    return get_shortest_path(prev_cell, moves, path)