with open('day7input.txt') as f:
    data = [int(i) for i in f.read().split(',')]

maximum = max(data)

def calc_distance_part_1(data, point):
    return sum(abs(i - point) for i in data)

def calc_distance_part_2(data, point):
    total = 0
    for i in data:
        n = abs(i - point)
        n = n * (n + 1) // 2
        total += n
    return total

min_distance = 9999999999999
for i in range(maximum + 1):
    distance = calc_distance(data, i)
    if distance < min_distance:
        min_distance = distance

print(min_distance)
