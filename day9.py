with open('day9input.txt', 'r') as f:
    matrix = [[int(x) for x in line.strip()] for line in f.readlines()]

# find local minima from adjacent values
# if the value is less than the adjacent values, it is a local minima

def check_minima(row, col, matrix):
    if row == 0 and col == 0:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row+1][col]
    elif row == 0 and col == len(matrix[0])-1:
        return matrix[row][col] < matrix[row][col-1] and matrix[row][col] < matrix[row+1][col]
    elif row == len(matrix)-1 and col == 0:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row-1][col]
    elif row == len(matrix)-1 and col == len(matrix[0])-1:
        return matrix[row][col] < matrix[row][col-1] and matrix[row][col] < matrix[row-1][col]
    elif row == 0:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row+1][col] and matrix[row][col] < matrix[row][col-1]
    elif row == len(matrix)-1:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row-1][col] and matrix[row][col] < matrix[row][col-1]
    elif col == 0:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row-1][col] and matrix[row][col] < matrix[row+1][col]
    elif col == len(matrix[0])-1:
        return matrix[row][col] < matrix[row][col-1] and matrix[row][col] < matrix[row-1][col] and matrix[row][col] < matrix[row+1][col]
    else:
        return matrix[row][col] < matrix[row][col+1] and matrix[row][col] < matrix[row-1][col] and matrix[row][col] < matrix[row+1][col] and matrix[row][col] < matrix[row][col-1]

def get_adjacents(row, col, matrix):
    adjacents = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
    if row == 0:
        adjacents.remove((row-1, col))
    if row == len(matrix)-1:
        adjacents.remove((row+1, col))
    if col == 0:
        adjacents.remove((row, col-1))
    if col == len(matrix[0])-1:
        adjacents.remove((row, col+1))
    return adjacents


def find_basin(local_minima, matrix):
    found_basins = set() 
    to_search = [local_minima]
    
    while to_search:
        current = to_search.pop()
        adjacents = get_adjacents(current[0], current[1], matrix)
        for row, col in adjacents:
            if (row, col) not in found_basins and matrix[row][col] != 9:
                found_basins.add((row, col))
                to_search.append((row, col))
    return found_basins

local_minima = []
total = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if check_minima(row, col, matrix):
            print(f'{row}, {col}')
            print(matrix[row][col])
            local_minima.append((row, col))
            total += matrix[row][col] + 1

print(total)

print(find_basin(local_minima[0], matrix))

basins = []
for minima in local_minima:
    print(minima)
    basin = find_basin(minima, matrix)
    print(basin)
    basin_size = len(basin) 
    basins.append(basin_size)


# multiply three largest basins
basins.sort(reverse=True)
print(basins)
print(basins[0]*basins[1]*basins[2])
