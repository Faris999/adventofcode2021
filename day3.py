from collections import Counter
from copy import deepcopy

with open('day3input.txt', 'r') as f:
    data = [i.strip() for i in f.readlines()]


# data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

# transpose to list of lists
data = [list(i) for i in zip(*data)]

# Part 1

def find_mode(line, keep='1'):
    count = {
        '1': 0,
        '0': 0
    }
    for i in line:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    if count['0'] == count['1']:
        return keep
    return max(count, key=count.get)

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
gamma_num = int(gamma, 2)
epsilon_num = int(epsilon, 2)
print(gamma_num, epsilon_num)
print(gamma_num * epsilon_num)

# Part 2
#with open('day3input.txt', 'r') as f:
#    data = f.readlines()

# data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def remove(data, to_remove):
    for j in range(len(data)):
        for i in to_remove:
            del data[j][i]
    return data

# oxygen

# deepcopy
oxygen_data = deepcopy(data)

for line in oxygen_data:
    if len(line) == 1:
        break
    mode = find_mode(line)
    to_remove = []
    for i in range(len(line)):
        if line[i] != mode:
            to_remove.insert(0, i)
    oxygen_data = remove(oxygen_data, to_remove)

print(oxygen_data)
oxygen = ''.join(list(zip(*oxygen_data))[0])
print(oxygen)

# co2

co2_data = deepcopy(data)

for line in co2_data:
    if len(line) == 1:
        break
    mode = find_mode(line, keep='1')
    to_remove = []
    for i in range(len(line)):
        if line[i] == mode:
            to_remove.insert(0, i)
    co2_data = remove(co2_data, to_remove)

print(co2_data)
co2 = ''.join(list(zip(*co2_data))[0])
print(co2)

oxygen_num = int(oxygen, 2)
co2_num = int(co2, 2)
print(oxygen_num, co2_num)
print(oxygen_num * co2_num)