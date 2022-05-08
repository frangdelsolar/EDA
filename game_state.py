import config
from pawn import Pawn


class GameState:
    def __init__(self):
        self.state = [[0] * config.COLS for i in range(config.ROWS)]
        self.turn = None
        self.player = '' # S or N
        self.opponent = '' # S or N
        self.player_pawns = []
        self.opponent_pawns = []

    def update(self, data):
        self.state = self.decode_board(data['board'])
        self.player = data['side']
        self.opponent = 'N' if self.player == 'S' else 'S'
        self.player_pawns = self.create_pawns(self.player)
        self.opponent_pawns = self.create_pawns(self.opponent)

    def create_pawns(self, side):
        pawns = []
        for i, row in enumerate(self.state):
            for j, item in enumerate(row):
                if item == side:
                    pawns.append(Pawn(i, j, side))
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

    def analize(self):
        

    def move(self):
        pass

    # def move(self):
    #     pawn_1 = self.pawns[0]
    #     pawn_2 = self.pawns[1]
    #     pawn_3 = self.pawns[2]
        
    #     move_1 = pawn_1.move(self.state)
    #     move_2 = pawn_2.move(self.state)
    #     move_3 = pawn_3.move(self.state)


    #     # move_1 = pawn_1.bfs(self.state)
    #     # move_2 = pawn_2.bfs(self.state)
    #     # move_3 = pawn_3.bfs(self.state)
    #     # all_paths = move_1 + move_2 + move_3
    #     # self.show(all_paths)

    #     move = None
    #     if move_1:
    #         move = move_1

    #     if move_2 and move_2['distance'] < move['distance']:
    #         move = move_2
        
    #     if move_3 and move_3['distance'] < move['distance']:
    #         move = move_3

    #     # pawn = random.choice(self.pawns)
    #     # move = pawn.move(self.state)

    #     if move:
    #         move.pop('distance', None)
    #     return move


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