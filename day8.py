contexts = []
outputs = []

with open('day8input.txt', 'r') as f:
    for line in f.readlines():
        context, output = line.strip().split('|')
        contexts.append(context.strip().split())
        outputs.append(output.strip().split())

print(sum(1 for output in outputs for digit in output if len(digit) in [2, 3, 4, 7]))

segments_to_num = {
    frozenset('ABCEFG'): 0,
    frozenset('CF'): 1,
    frozenset('ACDEG'): 2,
    frozenset('ACDFG'): 3,
    frozenset('BCDF'): 4,
    frozenset('ABDFG'): 5,
    frozenset('ABDEFG'): 6,
    frozenset('ACF'): 7,
    frozenset('ABCDEFG'): 8,
    frozenset('ABCDFG'): 9
}

# Part 2

def unscramble(context):
    length_2 = [frozenset(i) for i in context if len(i) == 2][0]
    length_3 = [frozenset(i) for i in context if len(i) == 3][0]
    length_4 = [frozenset(i) for i in context if len(i) == 4][0]
    length_5 = set(frozenset(i) for i in context if len(i) == 5)
    length_6 = set(frozenset(i) for i in context if len(i) == 6)
    length_7 = [frozenset(i) for i in context if len(i) == 7][0]

    mapping = {}

    A = list(length_3.difference(length_2))[0]
    eq_2 = length_7.difference(length_4)
    eq_3 = length_7.difference(length_7.intersection(*length_6))
    E = list(eq_3.intersection(eq_2))[0]
    G = list(eq_2.difference({A}).difference({E}))[0]
    print(eq_3)
    print(A)
    print(E)
    print(G)

    C = list(eq_3.intersection(length_2))[0]
    D = list(eq_3.difference({C}).difference({E}))[0]
    print(C)
    print(D)

    F = list(length_2.difference({C}))[0]

    print(F)
    
    B = list(length_4.difference({C, D, F}))[0]

    mapping[A] = 'A'
    mapping[B] = 'B'
    mapping[C] = 'C'
    mapping[D] = 'D'
    mapping[E] = 'E'
    mapping[F] = 'F'
    mapping[G] = 'G'
    return mapping

def decode(output, mapping):
    digits = ''
    for num in output: # num = 'db'
        unscrambled = ''.join(mapping[char] for char in num) # unscrambled = 'CF'
        digit = segments_to_num[frozenset(unscrambled)] # digit = '1'
        digits += str(digit)
    return int(digits)

total = 0
for context, output in zip(contexts, outputs):
    mapping = unscramble(context)
    decoded = decode(output, mapping)
    total += decoded

print(total)

print(unscramble(contexts[0]))
