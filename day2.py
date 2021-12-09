with open('day2input.txt', 'r') as f:
    data = f.readlines()
    data = [i.split(' ') for i in data]
    data = [(direction, int(length)) for direction, length in data]

# --------- Part 1 ----------

x = 0
y = 0

for direction, length in data:
    if direction == 'down':
        y += length
    elif direction == 'up':
        y -= length
    elif direction == 'forward':
        x += length

print(x, y)
print(x*y)

# --------- Part 2 ----------

aim = 0
x = 0
y = 0

for direction, length in data:
    if direction == 'down':
        aim += length
    elif direction == 'up':
        aim -= length
    elif direction == 'forward':
        x += length
        y += aim * length
    if x == 0 and y == 0:
        aim += 1

print(x, y)
print(x*y)
