import copy
import config


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.origin = [row, col]

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'

    def __eq__(self, o: object) -> bool:
        return self.row == o.row and self.col == o.col

    def up(self, amt=1):
        self.row -= amt
    
    def down(self, amt=1):
        self.row += amt

    def right(self, amt=1):
        self.col += amt

    def left(self, amt=1):
        self.col -= amt

    def reset(self, rotation=0, matrix=None):
        self.row = self.origin[0]
        self.col = self.origin[1]
        for i in range(rotation):
            self.rotate(matrix)

    def rotate(self, matrix):
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

def rotate_matrix(grid):
    grid_copy = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row = j
            col = len(grid[i])-1-i
            grid_copy[row][col] = grid[i][j]

    return grid_copy