import config
import utils

class Pawn:
    def __init__(self, row, col, side):
        self.row = row
        self.col = col
        self.side = side
        self.base = 0 if self.side == 'N' else config.ROWS - 1 
        self.target = config.ROWS - 1 if self.side == 'N' else 0
        self.path = None

    def move(self, state):
        moves = self.path = self.bfs(state)
        if len(moves) >= 2:
            move = {
                'from_row': moves[0]['row'] // 2,
                'from_col': moves[0]['col'] // 2,
                'to_row': moves[1]['row'] // 2,
                'to_col': moves[1]['col'] // 2,
                'distance': moves[-1]['depth']
            }
            return move
        return None

    def bfs(self, state):
        visited = []
        depth = 0
        parent = -1    
        queue = [{'row': self.row, 'col': self.col, 'depth': depth, 'parent': parent}]   

        while len(queue) > 0:
            cell = queue.pop(0)

            visited.append(cell)
            parent = visited.index(cell)
            depth = cell['depth'] + 1

            if cell['row'] == self.target:
                # print('Arrived')
                self.path = get_shortest_path(cell, visited)
                # show_state(state, path)
                self.path.reverse()
                return self.path

            for move in self.get_valid_moves(state, cell):
                if not move_included(move, visited) and not move_included(move, queue):
                    move['parent'] = parent
                    move['depth'] = depth 
                    queue.append(move)
        
        print('No hay camino de salida')
        return []
 
    def get_valid_moves(self, state, pos=None):
        if not pos:
            pos = {'row': self.row, 'col': self.col}

        neighbours = []
        vicinity = [
            [-2, 0],
            [0, -2],
            [0, 2],
            [2, 0]
        ]
        for i, j in vicinity:
            cell = {
                'row': i + pos['row'], 
                'col': j + pos['col']
            }
            
            if utils.within_boundaries(cell):
                # check if there's another pawn there
                if is_cell_engaged(cell, state):
                    # pawn can jump
                    cell = get_next_available(pos, cell, self.side, state)

                if cell:
                    if not is_blocked(pos, cell, state):
                        neighbours.append(cell) 

        return neighbours

def is_blocked(from_pos, to_pos, state):
    if from_pos['row'] == to_pos['row']:
        if to_pos['col'] > from_pos['col']:
            for col in range(from_pos['col'], to_pos['col']):
                if is_cell_wall({'row': to_pos['row'], 'col': col}, state):
                    return True
        else:
            for col in range(from_pos['col'], to_pos['col'], -1):
                if is_cell_wall({'row': to_pos['row'], 'col': col}, state):
                    return True

    if from_pos['col'] == to_pos['col']:
        if to_pos['row'] > from_pos['row']:
            for row in range(from_pos['row'], to_pos['row']):
                if is_cell_wall({'row': row, 'col': to_pos['col']}, state):
                    return True
        else:
            for row in range(from_pos['row'], to_pos['row'], -1):
                if is_cell_wall({'row': row, 'col': to_pos['col']}, state):
                    return True
    return False

def is_cell_wall(cell, state):
    return state[cell['row']][cell['col']] in ['|', '*', '-']

def is_cell_engaged(cell, state):
    return state[cell['row']][cell['col']] in ['S', 'N']

def get_next_available(from_pos, to_pos, from_side, state):
    if state[to_pos['row']][to_pos['col']] == from_side:
        return None

    # obstacle to the left
    if from_pos['row'] == to_pos['row'] and from_pos['col'] == to_pos['col'] + 2:
        cell = {
            'row': to_pos['row'],
            'col': to_pos['col'] - 2
        }
    
    # obstacle to the right
    elif from_pos['row'] == to_pos['row'] and from_pos['col'] == to_pos['col'] - 2:
        cell = {
            'row': to_pos['row'],
            'col': to_pos['col'] + 2
        }
    
    # obstacle to the bottom
    elif from_pos['col'] == to_pos['col'] and from_pos['row'] == to_pos['row'] + 2:
        cell = {
            'row': to_pos['row'] - 2,
            'col': to_pos['col']
        }
    
    # obstacle to the top
    elif from_pos['col'] == to_pos['col'] and from_pos['row'] == to_pos['row'] - 2:
        cell = {
            'row': to_pos['row'] + 2,
            'col': to_pos['col']
        }

    else: 
        return None
    
    if utils.within_boundaries(cell) and not is_cell_engaged(cell, state):
            return cell
    return None

def get_shortest_path(cell, moves, path = []):
    if cell == None:
        return path

    path.append(cell)

    prev_cell= None
    if cell['parent'] >= 0:
        prev_cell = moves[cell['parent']]

    return get_shortest_path(prev_cell, moves, path)


def move_included(move, moves):
    for m in moves:
        if m['row'] == move['row'] and m['col'] == move['col']:
            return True
    return False


def show_state(state, array):
    complete = lambda s: str(s).ljust(3)
    for i, row in enumerate(state):
        for j, item in enumerate(row):
            printed = False

            if item != ' ': # in ['|', '-', '*']:
                print(f' {item} ', end=" ")
                printed = True

            else:
                for pos in array:
                    if pos['row'] == i and pos['col'] == j:
                        
                        if 'depth' in pos:
                            print(complete(pos['depth']), end=" ")
                        else:
                            print(complete('v'), end=" ")
                        printed = True
            if not printed:
                print(' . ', end=' ')
        print()
    