from position import Position

class Wall:
    def __init__(self, row, col, turn_token, game_id):
        self.pos = Position(row, col)
        self.orientation = None 
        self.turn_token = turn_token
        self.game_id = game_id

    def json(self):
        return {
            'row': self.pos.row // 2,
            'col': self.pos.col // 2,
            'orientation': self.orientation,
            'turn_token': self.turn_token,
            'game_id': self.game_id
        }

    def blocks(self):
        pos1 = Position(self.pos.row + 1, self.pos.col)
        pos2 = Position(self.pos.row + 1, self.pos.col + 2)
        pos3 = Position(self.pos.row, self.pos.col + 1)
        pos4 = Position(self.pos.row + 2, self.pos.col + 1)
        return [pos1, pos2, pos3, pos4]
