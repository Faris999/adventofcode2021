from re import L
import tqdm
from collections import Counter

# input handling
with open('day6input.txt', 'r') as f:
    lanternfishes = [int(i) for i in f.read().split(',')]

def update(lanternfish):
    if lanternfish == 0:
        return 6
    return lanternfish - 1

for i in tqdm.tqdm(range(80)):
    new_lanternfishes = [8 for lanternfish in lanternfishes if lanternfish == 0]
    lanternfishes = [update(lanternfish) for lanternfish in lanternfishes]
    lanternfishes += new_lanternfishes
    # print(f'Day {i+1}: {lanternfishes}')

print(len(lanternfishes))

# Part 2
# this needs rework because of the exponential growth of the list
# the current solution is not optimal
# rewrote the code to use a counter

with open('day6input.txt', 'r') as f:
    lanternfishes = Counter(int(i) for i in f.read().split(','))

DAYS = 256

for day in range(DAYS):
    new_lanternfishes = Counter()
    for i in range(8):
        new_lanternfishes[i] = lanternfishes[i+1]
    new_lanternfishes[8] = lanternfishes[0]
    new_lanternfishes[6] += lanternfishes[0]
    lanternfishes = new_lanternfishes
    count = sum(lanternfishes.values())
    print(f'Day {day+1}: {count}')


print(lanternfishes)
print(count)