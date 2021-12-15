with open('day10input.txt', 'r') as f:
    data = f.read().splitlines()

def get_matching(char):
    if char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'
    elif char == '<':
        return '>'

# returns the invalid char
def is_corrupted(line):
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            if len(stack) == 0:
                return True, char
            if get_matching(stack.pop()) != char:
                return True, char
    return False, None

score_mapping = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
total = 0
for line in data:
    is_corrupt, char = is_corrupted(line)
    if is_corrupt:
        total += score_mapping[char]

print(total)

# part 2

def complete(line):
    stack = []
    completion = ''
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            stack.pop() 

    for char in reversed(stack):
        completion += get_matching(char)
    return completion

def completion_score(line):
    score_mapping = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    total = 0
    for char in line:
        total *= 5
        total += score_mapping[char]
    return total

scores = []
for line in data:
    is_corrupt, char = is_corrupted(line)
    if not is_corrupt:
        remaining = complete(line)
        score = completion_score(remaining)
        scores.append(score)

scores.sort()
# print the median
print(scores[len(scores)//2])
