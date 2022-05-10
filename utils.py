import config
import copy


def rotate(grid, pos, cursor, neighbours):
    grid_copia = copy.deepcopy(grid)
    pos_row, pos_col = pos['row'], pos['col']
    cursor_row, cursor_col = cursor['row'], cursor['col']
    new_neighbours = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            row = j
            col = len(grid[i])-1-i
            grid_copia[row][col] = grid[i][j]
            if i == pos_row and j == pos_col:
                pos['row'] = row
                pos['col'] = col

            if i == cursor_row and j == cursor_col:
                cursor['row'] = row
                cursor['col'] = col

            for neig in neighbours:
                if i == neig['row'] and j == neig['col']:
                    n = {}
                    n['row'] = row
                    n['col'] = col
                    new_neighbours.append(n)
    return grid_copia, pos, cursor, new_neighbours


def within_boundaries(pos):
    if not pos['row'] in range(0, config.ROWS): return False
    if not pos['col'] in range(0, config.COLS): return False
    return True