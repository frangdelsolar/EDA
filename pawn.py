import config
import utils
import copy
from position import (
    Position, 
    append_pos, 
    rotate_matrix, 
    rotate_moves
)


class Pawn:
    def __init__(self, row, col, side):
        self.pos = Position(row, col)
        self.side = side
        self.base = 0 if self.side == 'N' else config.ROWS - 1 
        self.target = config.ROWS - 1 if self.side == 'N' else 0

    def __repr__(self) -> str:
        return f'{self.side}({self.pos.row}, {self.pos.col})'


def get_valid_moves(pos, side, state):
    from game_state import (
        is_cell_wall, 
        is_cell_engaged, 
        is_cell_engaged_by_opponent, 
        within_boundaries,
    )

    neighbours = []
    cursor = copy.deepcopy(pos)
    
    # Rotate matrix four times to find the free cells
    for i in range(4):
        state = rotate_matrix(state)
        cursor.reset(i+1, state)
        neighbours = rotate_moves(neighbours, state)
        
        print('Iteracion ', i, ' Cursor ', cursor)

        # Si hay pared contigua, salir de iteración
        cursor.right()
        if is_cell_wall(cursor, state):
            continue

        cursor.right()
        if not is_cell_engaged(cursor, state):
            neighbours = append_pos(copy.deepcopy(cursor), neighbours)
            continue






    # Clean up those that are off limits
    definitive = []
    for n in neighbours:
        if within_boundaries(n):
            definitive.append(n)
    return definitive
