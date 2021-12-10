# parsing data

with open('day5input.txt', 'r') as f:
    data = f.readlines()

def mapping(line):
    line = line.strip().split()
    point1 = tuple(map(int, line[0].split(',')))
    point2 = tuple(map(int, line[2].split(',')))
    return (point1, point2)

lines = list(map(mapping, data))

horizontal_lines = [line for line in lines if line[0][1] == line[1][1]]
vertical_lines = [line for line in lines if line[0][0] == line[1][0]]

print(horizontal_lines)
print(vertical_lines)

coordinate_map = [[0 for i in range(1000)] for j in range(1000)]

for line in horizontal_lines:
    # swap if descending
    if line[0][0] > line[1][0]:
        line = (line[1], line[0])
    for i in range(line[0][0], line[1][0] + 1):
        coordinate_map[line[0][1]][i] += 1

for line in vertical_lines:
    # swap if descending
    if line[0][1] > line[1][1]:
        line = (line[1], line[0])
    for i in range(line[0][1], line[1][1] + 1):
        coordinate_map[i][line[0][0]] += 1

print(coordinate_map)

count = 0
for row in coordinate_map:
    for col in row:
        if col > 1:
            count += 1

print(count)
