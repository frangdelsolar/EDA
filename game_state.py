import config
from pawn import Pawn


class GameState:
    def __init__(self):
        self.state = [[0] * config.COLS for i in range(config.ROWS)]
        self.player = '' # S or N
        self.opponent = '' # S or N
        self.player_pawns = []
        self.opponent_pawns = []

    def update(self, data):
        self.state = self.decode_board(data['board'])
        self.player = data['side']
        self.opponent = 'N' if data['side'] == 'S' else 'S'
        self.player_pawns = self.create_pawns(self.player)
        self.opponent_pawns = self.create_pawns(self.opponent)

    def create_pawns(self, side):
        pawns = []
        for i, row in enumerate(self.state):
            for j, item in enumerate(row):
                if item == side:
                    pawn = Pawn(i, j, side)
                    pawns.append(pawn)
        return pawns
    
    def decode_board(self, encoded):
        state = [[0] * config.COLS for i in range(config.ROWS)]
        for i in range(len(encoded)):
            row = i // config.ROWS
            col = i % config.COLS
            state[row][col] = encoded[i]
        return state
    
    def encode_board(self, state=None):
        if not state:
            state = self.state

        encoded = ''
        for i in range(len(state)):
            for j in range(len(state[i])):
                encoded += state[i][j]
        return encoded

    def move(self):
        move_1 = self.player_pawns[0].move(self.state)
        move_2 = self.player_pawns[1].move(self.state)
        move_3 = self.player_pawns[2].move(self.state)

        # paths = []

        move = None
        if move_1:
            move = move_1
            # paths += self.player_pawns[0].path
        if move:
            if move_2:
                # paths += self.player_pawns[1].path

                if move_2['distance'] < move['distance']:
                    move = move_2
        else:
            if move_2:
                move = move_2
        
        
        if move:
            if move_3:
                # paths += self.player_pawns[2].path

                if move_3['distance'] < move['distance']:
                    move = move_3
        else:
            if move_3:
                move = move_3

        # self.show(paths)

        if move:
            move.pop('distance', None)
        return move


    def show(self, paths=None):
        # os.system('CLS')

        board = [[i for i in row] for row in self.state]
        if paths:
            for move in paths:
                if move['depth'] > 0:
                    board[move['row']][move['col']] = move['depth']

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