from starting_grid import *
from col_check import *
from row_check import *

turns = 0

while True:
    print_grid(grid)

    number = input('What number? > ')
    row = int(input('What row? > '))
    col = int(input('What column? > '))

    if col_check(number, grid, col - 1) == True or row_check(number, grid, row - 1) == True:
        continue
    else:
        grid[row-1][col-1] = number

    turns += 1

    blanks = 0
    for wor in grid:
        blanks += wor.count('x')

    if blanks == 0:
        print('You won the game with %s turns!' % turns)
        break
    else:
        continue
