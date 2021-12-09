with open('day1input.txt', 'r') as f:
    data = [int(i) for i in f.readlines()]

# Part 1

count = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        count += 1

print(count)

# Another way with list comprehension

print(sum([1 for i in range(1, len(data)) if data[i] > data[i-1]]))

# Part 2

count = 0
prev_sum = sum(data[:3])
for i in range(3, len(data)):
    curr_sum = sum(data[i-2:i+1])
    if curr_sum > prev_sum:
        count += 1
    prev_sum = curr_sum

print(count)
