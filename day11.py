with open('day11input.txt') as f:
    octopuses = [[int(x) for x in line] for line in f.read().splitlines()]

# returns a list of the adjacent octopuses including diagonals
def get_adjacents(row, col, height, width):
    adjacents = []
    if row > 0:
        adjacents.append((row-1, col))
    if row < height-1:
        adjacents.append((row+1, col))
    if col > 0:
        adjacents.append((row, col-1))
    if col < width-1:
        adjacents.append((row, col+1))
    if row > 0 and col > 0:
        adjacents.append((row-1, col-1))
    if row > 0 and col < width-1:
        adjacents.append((row-1, col+1))
    if row < height-1 and col > 0:
        adjacents.append((row+1, col-1))
    if row < height-1 and col < width-1:
        adjacents.append((row+1, col+1))
    return adjacents

def flash(row, col, octopuses):
    global flash_count
    flash_count += 1

    # if it's larger than 9, set it to 0, and increment the adjacent octopuses
    octopuses[row][col] = 0
    adjacents = get_adjacents(row, col, len(octopuses), len(octopuses[0]))
    for row, col in adjacents:
        if octopuses[row][col] > 0:
            octopuses[row][col] += 1
        if octopuses[row][col] > 9:
            octopuses = flash(row, col, octopuses)
    return octopuses

def simulate_step(octopuses):
    # increment each octopus by 1
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1
    # if it's larger than 9, set it to 0, and increment the adjacent octopuses
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if octopuses[i][j] > 9:
                octopuses = flash(i, j, octopuses)

    return octopuses

def print_matrix(octopuses):
    for row in octopuses:
        for col in row:
            print(col, end='')
        print()

flash_count = 0
i = 0
while True:
    octopuses = simulate_step(octopuses)
    # check if all zeros
    if all(all(x == 0 for x in row) for row in octopuses):
        print('Sync found after {} iterations'.format(i+1))
        print_matrix(octopuses)
        break
    if i % 10 == 0:
        print(f'After {i+1} steps:')
        print_matrix(octopuses)
        print()
    i += 1


print(flash_count)

