import random

grid = []

n = int(input('What size of sudoku (n x n)? n = '))

# create 4x4 grid
for i in range(n):
    grid.append(['x']*n)

def print_grid(lst):
    for row in lst:
        print(' '.join(row))

# create starting grid
place_number = [x for x in range(n)]
for row in grid:
    place = random.choice(place_number)
    number = random.randrange(0,n-1)
    row[place] = str(number)
    place_number.remove(place)
