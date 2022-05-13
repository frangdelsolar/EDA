import config
import copy
from position import (
    Position, 
    append_pos, 
    rotate_moves,
    get_shortest_path
)


class Pawn:
    def __init__(self, row, col, side):
        self.pos = Position(row, col)
        self.side = side
        self.base = 0 if self.side == 'N' else config.ROWS - 1 
        self.target = config.ROWS - 1 if self.side == 'N' else 0

        self.distance = 999999

    def __repr__(self) -> str:
        return f'{self.side}({self.pos.row}, {self.pos.col})'


def get_valid_moves(pos, side, state):
    from game_state import (
        is_cell_wall, 
        is_cell_engaged, 
        is_cell_engaged_by_opponent, 
        rotate_matrix,
        within_boundaries,
    )

    neighbours = []
    cursor = copy.deepcopy(pos)
    
    # Rotate matrix four times to find the free cells
    for i in range(4):
        state = rotate_matrix(state)
        cursor = copy.deepcopy(pos)
        cursor.rotate(state, i+1)
        neighbours = rotate_moves(neighbours, state)
        
        # Si hay pared contigua, salir de iteración
        cursor.right()
        if is_cell_wall(cursor, state):
            continue

        cursor.right()
        if not is_cell_engaged(cursor, state):
            neighbours = append_pos(copy.deepcopy(cursor), neighbours)
            continue
        else:
            if is_cell_engaged_by_opponent(cursor, state, side):
                cursor.right()
                if not is_cell_wall(cursor, state):
                    cursor.right()
                    if not is_cell_engaged(cursor, state):
                        neighbours = append_pos(copy.deepcopy(cursor), neighbours)
                        continue
        
        cursor = copy.deepcopy(pos)
        cursor.rotate(state, i+1)
        cursor.right(2)
        if is_cell_engaged_by_opponent(cursor, state, side):
            cursor.right()
            if is_cell_wall(cursor, state) and cursor.col < config.COLS:
                cursor.left()
                cursor.up()
                if not is_cell_wall(cursor, state) and cursor.col < config.COLS-1:
                    cursor.up()
                    if not is_cell_engaged(cursor, state):
                        neighbours = append_pos(copy.deepcopy(cursor), neighbours)

            cursor = copy.deepcopy(pos)
            cursor.rotate(state, i+1)
            cursor.right(2)
            cursor.down()

            if not is_cell_wall(cursor, state) and cursor.col < config.COLS-1:
                cursor.down()
                if not is_cell_engaged(cursor, state):
                    neighbours = append_pos(copy.deepcopy(cursor), neighbours)

    # Clean up those that are off limits
    definitive = []
    for n in neighbours:
        if within_boundaries(n):
            definitive.append(n)
    return definitive

def bfs(pawn, state):
    path = []
    visited = []
    depth = 0
    parent = -1
    pawn.pos.depth = depth    
    pawn.pos.parent = depth    
    queue = [copy.deepcopy(pawn.pos)]   

    while len(queue) > 0:
        current = queue.pop(0)
        visited.append(current)
        print('Current', current)

        moves = get_valid_moves(current, pawn.side, state)
        print('Moves', moves)

        for move in moves:
            if not move in visited and not move in queue:
                queue.append(move)
                print('Queue', queue)

    print('No hay camino de salida')
    return path