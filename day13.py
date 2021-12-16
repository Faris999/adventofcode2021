with open('day13input.txt', 'r') as f:
    coordinates = []
    folds = []
    # stop until newline
    for line in f:
        line = line.strip()
        if line == '':
            break
        coordinates.append(tuple(int(i) for i in line.split(',')))

    for line in f:
        axis, value = line.strip().split()[2].split('=')
        folds.append((axis, int(value)))

HEIGHT = max(coordinates, key=lambda x: x[1])[1] + 1
WIDTH = max(coordinates, key=lambda x: x[0])[0] + 1

matrix = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

for x, y in coordinates:
    matrix[y][x] = 1

for fold in folds:
    axis, value = fold
    if axis == 'x':
        new_width = value
        new_matrix = [[0 for x in range(new_width)] for y in range(HEIGHT)]
        for y in range(HEIGHT):
            for x in range(2*new_width - WIDTH + 1, value):
                # print(x, y)
                new_matrix[y][x] = matrix[y][x] | matrix[y][2 * value - x]
        WIDTH = new_width
    elif axis == 'y':
        new_height = value
        new_matrix = [[0 for x in range(WIDTH)] for y in range(new_height)]
        for y in range(2*new_height - HEIGHT + 1, new_height):
            for x in range(WIDTH):
                # print(x, y)
                new_matrix[y][x] = matrix[y][x] | matrix[2 * value - y][x]
        HEIGHT = new_height
    matrix = new_matrix
    print('1 fold')

print(sum(sum(row) for row in new_matrix))
print(matrix)

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            if item == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()

print_matrix(matrix)