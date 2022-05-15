import copy
import config
from pawn import *


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
        self.player_pawns = create_pawns(self.side, self)
        self.opponent_pawns = create_pawns(self.opponent, self)
        self.player_distances = get_pawn_distances(self.player_pawns)
        self.opponent_distances = get_pawn_distances(self.opponent_pawns)
        self.score = get_board_score(self)
    
    def update_from_decoded(self, decoded):
        self.state = decoded
        self.player_pawns = create_pawns(self.side, self)
        self.opponent_pawns = create_pawns(self.opponent, self)

    def move_shortest(self):
        best_pawn = self.player_pawns[self.player_distances.index(min(self.player_distances))]
        move = best_pawn.move()
        move.pop('side')
        move['game_id'] = self.game_id
        move['turn_token'] = self.turn_token
        return move

    def get_possible_moves(self):
        return [
            self.player_pawns[0].move(),
            self.player_pawns[1].move(),
            self.player_pawns[2].move(),
        ]

    def move_minimax(self, depth):

        # print("************** MINIMAX **************")

        moves = self.get_possible_moves()
        best_score = -99999
        best_move = moves[0]

        for move in moves:
            new_state = create_state_from_move(move, self)
            score = minimax(new_state, depth, -9999, 9999, True)
            if score > best_score:
                best_score = score
                best_move = move

        if best_move:
            best_move.pop('side')
            best_move['game_id'] = self.game_id
            best_move['turn_token'] = self.turn_token
        return best_move
        


    def update_state_from_move(self, move):
        from_row = move['from_row'] * 2
        from_col = move['from_col'] * 2
        to_row = move['to_row'] * 2
        to_col = move['to_col'] * 2
        self.state[from_row][from_col] = ' '
        self.state[to_row][to_col] = move['side']

    def show(self, moves=None):
        print()
        print(f'Playing {self.side}')
        print(f'Çhallenge id: {self.game_id}')
        print(f'{self.player_1} vs. {self.player_2}')
        print('Board Score: ', self.score)

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

def minimax(game, depth, alpha, beta, maximizing):
    # game.show()
    if depth <= 0:
        return game.score
    
    moves = game.get_possible_moves()

    if maximizing:
        best_score = -999999
        
        for move in moves:
            new_state = create_state_from_move(move, game)
            score = minimax(new_state, depth-1, alpha, beta, False)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break            
        
        return best_score
    
    else:
        best_score = 999999

        for move in moves:
            new_state = create_state_from_move(move, game)
            score = minimax(new_state, depth-1, alpha, beta, True)
            best_score = min(best_score, score)  
            beta = min(beta, score)


        return best_score
        



def create_state_from_move(move, game):
    new_game = copy.deepcopy(game)
    new_game.side = game.opponent
    new_game.opponent = game.side
    new_game.update_state_from_move(move)
    new_game.player_pawns = create_pawns(new_game.side, new_game)
    new_game.opponent_pawns = create_pawns(new_game.opponent, new_game)
    new_game.player_distances = get_pawn_distances(new_game.player_pawns)
    new_game.opponent_distances = get_pawn_distances(new_game.opponent_pawns)
    new_game.score = get_board_score(new_game)
    return new_game


def get_board_score(game):
    max_distance_posible = (9 * 9 * 3) - 3
    opponent = sum(game.opponent_distances) / max_distance_posible
    player = sum(game.player_distances) / max_distance_posible
    return opponent - player

def get_pawn_distances(pawns):
    distances = []
    for p in pawns:
        distances.append(p.distance)
    return distances


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


def create_pawns(side, game):
    pawns = []
    for i, row in enumerate(game.state):
        for j, item in enumerate(row):
            if item == side:
                p = Pawn(i, j, side)
                bfs(p, game)
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