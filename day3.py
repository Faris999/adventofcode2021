from collections import Counter

with open('day3input.txt', 'r') as f:
    data = [[int(j) for j in i.strip()] for i in f.readlines()]

# transpose
data = list(zip(*data))

# Part 1

def find_mode(line):
    c = Counter(line)
    return c.most_common(1)[0][0]

def flip(line):
    flipped = ''
    for i in line:
        if i == '1':
            flipped += '0'
        else:
            flipped += '1'
    return flipped

gamma = ''
for line in data:
    mode = find_mode(line)
    gamma += str(mode)
    print(mode)

epsilon = flip(gamma)
print(gamma)
print(epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma, epsilon)
print(gamma * epsilon)
