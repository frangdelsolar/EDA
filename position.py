class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'