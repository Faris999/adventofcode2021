from collections import Counter

with open('day12input.txt') as f:
    lines = f.read().splitlines()

edges = [tuple(j for j in i.split('-')) for i in lines]

edges_dict = {}
for edge in edges:
    if edge[0] not in edges_dict:
        edges_dict[edge[0]] = [edge[1]]
    else:
        edges_dict[edge[0]].append(edge[1])
    if edge[1] not in edges_dict:
        edges_dict[edge[1]] = [edge[0]]
    else:
        edges_dict[edge[1]].append(edge[0])

del edges_dict['end']
for edge in edges_dict:
    if 'start' in edges_dict[edge]:
        edges_dict[edge].remove('start')
    edges_dict[edge] = sorted(edges_dict[edge])

count = 0
def traverse(start, edges_dict, stack):
    global count
    edges = edges_dict[start]
    for edge in edges:
        stack.append(edge)
        if edge == 'end':
            count += 1
        elif edge[0].isupper():
            traverse(edge, edges_dict, stack)
        elif edge not in stack[:-1]:
            traverse(edge, edges_dict, stack)
        stack.pop()
    return stack

print(traverse('start', edges_dict, ['start']))
print(count)

def no_small_twice(stack):
    counter = Counter(i for i in stack if i[0].islower())
    return counter.most_common(1)[0][1] == 1

# part 2
count = 0
def traverse2(start, edges_dict, stack):
    global count
    edges = edges_dict[start]
    for edge in edges:
        stack.append(edge)
        if edge == 'end':
            count += 1
        elif edge[0].isupper():
            traverse2(edge, edges_dict, stack)
        elif edge not in stack[:-1]:
            traverse2(edge, edges_dict, stack)
        elif no_small_twice(stack[:-1]) and stack[:-1].count(edge) <= 1:
            traverse2(edge, edges_dict, stack)
        stack.pop()
    return stack

print(traverse2('start', edges_dict, ['start']))
print(count)