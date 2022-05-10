import config
import utils
import copy

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
        
        old_state = copy.deepcopy(state)
        pos_copy = pos

        neighbours = []
        
        cursor = pos.copy()
        for i in range(4):
            cursor['col'] += 1 # mover un casillero a la derecha
            if not is_cell_wall(cursor, state):
                cursor['col'] += 1 # comprobar siguiente col 6
                if not is_cell_engaged(cursor, state):
                    neighbours.append({'row': pos['row'], 'col': pos['col'] + 2 })
                    # No seguir avanzando         
                else:
                    cursor['col'] += 1 # g
                    if not is_cell_wall(cursor, state): # puedo seguir avanzando?
                        cursor['col'] += 1
                        if not is_cell_engaged(cursor, state): # saltar obstáculo
                            neighbours.append({'row': pos['row'], 'col': pos['col'] + 4 })
                        cursor['col'] -= 1

                    else: # mirar a los costados
                        cursor['col'] -= 1 # 6

                        #ir hacia arriba
                        cursor['row'] -= 1 #re c6

                        if not is_cell_wall(cursor, state): # puedo seguir avanzando?
                            cursor['row'] -= 1 #r4 c6
                            if not is_cell_engaged(cursor, state): # saltar obstáculo
                                neighbours.append({'row': pos['row'] - 2, 'col': pos['col'] + 2})
                            cursor['row'] += 1
                        cursor['row'] += 1
                        
                        #ir hacia abajo
                        cursor['row'] += 1
                        if not is_cell_wall(cursor, state): # puedo seguir avanzando?
                            cursor['row'] += 1
                            if not is_cell_engaged(cursor, state): # saltar obstáculo
                                neighbours.append({'row': pos['row'] + 2, 'col': pos['col'] + 2 })
                            cursor['row'] -= 1
                        cursor['row'] -= 1
                cursor['col'] -= 1
            cursor['col'] -= 1

            state, pos, cursor, neighbours = utils.rotate(state, pos, cursor, neighbours)
        return neighbours



def is_cell_wall(cell, state):
    return state[cell['row']][cell['col']] in ['|', '*', '-']

def is_cell_engaged(cell, state):
    return state[cell['row']][cell['col']] in ['S', 'N']

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
    board = [[i for i in row] for row in state]
    if array:
        for move in array:
            board[move['row']][move['col']] = 'v'

    headers = '0a1b2c3d4e5f6g7h8'
    print('    ', end='')
    for ch in headers:
        print(ch + '  ', end='')
    print()
    print('   --------------------------------------------------')
    for i, row in enumerate(board):
        print(headers[i] + ' | ', end='')
        for j, item in enumerate(row):
            if item != ' ' or item != 0:
                print(item, end="")
            else:
                print(' ', end="")
            print('  ', end='')
        print()