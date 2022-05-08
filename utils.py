import config


def within_boundaries(pos):
    if not pos['row'] in range(0, config.ROWS): return False
    if not pos['col'] in range(0, config.COLS): return False
    return True