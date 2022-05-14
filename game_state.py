import copy
import config
from pawn import Pawn


class GameState:
    def __init__(self, data):
        self.board = data['board']
        self.player_1 = data['player_1']
        self.player_2 = data['player_2']
        self.side = data['side']
        self.remaining_moves = data['remaining_moves']
        self.turn_token = data['turn_token']
        self.game_id = data['game_id']

        self.state = decode_board(self.board)
        self.opponent = 'S' if self.side == 'N' else 'N'
        self.player_pawns = create_pawns(self.side, self.state)
        self.opponent_pawns = create_pawns(self.opponent, self.state)
    
    def update_from_decoded(self, decoded):
        self.state = decoded
        self.player_pawns = create_pawns(self.side, self.state)
        self.opponent_pawns = create_pawns(self.opponent, self.state)

    def show(self, moves=None):
        print()
        print(f'Playing {self.side}')
        print(f'Çhallenge id: {self.game_id}')
        print(f'{self.player_1} vs. {self.player_2}')
        # print('Board Score: ', self.score)

        board = [[i for i in row] for row in self.state]
        if moves:
            for move in moves:
                # if move['depth'] > 0:
                board[move.row][move.col] = move.depth

        headers = '0a1b2c3d4e5f6g7h8'
        print('    ', end='')
        for ch in headers:
            print(ch + '  ', end='')
        print()
        print('   --------------------------------------------------')
        for i, row in enumerate(board):
            print(headers[i] + ' | ', end='')
            for j, item in enumerate(row):
                if item != ' ':
                    print(item, end="")
                else:
                    print(' ', end="")
                print('  ', end='')
            print()


def within_boundaries(pos):
    if not pos.row in range(0, config.ROWS): return False
    if not pos.col in range(0, config.COLS): return False
    return True


def is_cell_wall(pos, state):
    if within_boundaries(pos):
        return state[pos.row][pos.col] in ['|', '*', '-']
    return True


def is_cell_engaged(pos, state):
    if within_boundaries(pos):
        return state[pos.row][pos.col] in ['S', 'N']
    return True


def is_cell_engaged_by_opponent(pos, state, own_side):
    other_side = 'N' if own_side == 'S' else 'S'
    if within_boundaries(pos):
        return state[pos.row][pos.col] == other_side
    return True


def create_pawns(side, state):
    pawns = []
    for i, row in enumerate(state):
        for j, item in enumerate(row):
            if item == side:
                p = Pawn(i, j, side)
                pawns.append(p)
    return pawns


def decode_board(board):
    state = [[None for c in range(config.COLS)] for r in range(config.ROWS)]
    for i, val in enumerate(board):
        r = i // config.ROWS
        c = i % config.COLS
        state[r][c] = val
    return state


def encode_board(board):
    result = ''
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            result += item
    return result

def rotate_matrix(grid):
    grid_copy = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row = j
            col = len(grid[i])-1-i
            grid_copy[row][col] = grid[i][j]

    return grid_copy