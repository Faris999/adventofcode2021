from collections import Counter

with open('day14input.txt', 'r') as f:
    template = f.readline().strip()
    f.readline()
    insertion_rules = {}
    for line in f:
        line = line.strip()
        a, b = line.split(' -> ')
        insertion_rules[a] = b

print(insertion_rules)

def insertion_step(template, insertion_rules):
    to_insert = []
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair in insertion_rules:
            to_insert.append(insertion_rules[pair])
    new_template = template[0]
    for i in range(len(to_insert)):
        new_template += to_insert[i]
        new_template += template[i+1]
    return new_template

new_template = template
for i in range(10):
    new_template = insertion_step(new_template, insertion_rules)

    counter = Counter(new_template)
    print(counter)
    # pairs = Counter(new_template[i:i+2] for i in range(len(new_template)-1))
    # print(pairs)
# most common minus least common
print(counter.most_common()[0][1] - counter.most_common()[-1][1])


# Part 2
# the above approach is too slow (exponential time)
# we need to rewrite the algorithm to use a dictionary
# instead of a list

optimized_insertion_rules = {}
for key in insertion_rules:
    optimized_insertion_rules[key] = (key[0] + insertion_rules[key], insertion_rules[key] + key[1])

def insertion_step2(pairs, atoms, insertion_rules):
    new_pairs = Counter()
    for pair, total in pairs.items():
        if total > 0:
            a, b = insertion_rules[pair]
            new_pairs.update({a: total, b: total})
            atoms.update({b[0]: total})
            pairs.subtract({pair: total})
    new_pairs.update(pairs)
    return new_pairs, atoms
# count pairs from template
pairs = Counter(template[i:i+2] for i in range(len(template)-1))
atoms = Counter(template)

for i in range(40):
    pairs, atoms = insertion_step2(pairs, atoms, optimized_insertion_rules)
    print(atoms)

print(atoms.most_common()[0][1] - atoms.most_common()[-1][1])