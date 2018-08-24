def col_check(number, grid, col):
    col_elements = []
    for row in grid:
        col_elements.append(row[col])
    if number in col_elements:
        return True
    return False
