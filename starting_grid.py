import random

grid = []

# create 4x4 grid
for i in range(4):
    grid.append(['x']*4)

def print_grid(lst):
    for row in lst:
        print(' '.join(row))

# create starting grid
place_number = [0,1,2,3]
for row in grid:
    place = random.choice(place_number)
    number = random.randrange(1,5)
    row[place] = str(number)
    place_number.remove(place)
