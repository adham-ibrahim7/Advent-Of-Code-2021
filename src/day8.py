f = open("../inputs/day8.txt", "r")

lines = f.read().split("\n")

# possible = list([] for _ in range(10))
segments = {0: [0, 1, 2, 4, 5, 6],
            1: [2, 5],
            2: [0, 2, 3, 4, 6],
            3: [0, 2, 3, 5, 6],
            4: [1, 2, 3, 5],
            5: [0, 1, 3, 5, 6],
            6: [0, 1, 3, 4, 5, 6],
            7: [0, 2, 5],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 3, 5, 6]}

count = 0
for line in lines:
    output = line.split(" | ")[1]
    for word in output.split():
        if len(word) in [2, 3, 4, 7]:
            count += 1

print("part 1:", count)



def number(str, positions):
    for i in range(0, 10):
        good = True
        for c in str:
            if positions[c] not in segments[i]:
                good = False
        for c in "abcdefg":
            if c not in str and positions[c] in segments[i]:
                good = False
        if good:
            return i

s = 0
for line in lines:
    positions = {}

    inputs, outputs = line.split(" | ")
    inputs = inputs.split()
    outputs = outputs.split()

    counts = {}
    one = ""
    four = ""
    for word in inputs:
        if len(word) == 2:
            one = word
        elif len(word) == 4:
            four = word

        for c in word:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

    easy = {6: 1, 4: 4, 9: 5}

    for c in counts:
        for e in easy:
            if counts[c] == e:
                positions[c] = easy[e]

    for c in one:
        if c not in positions:
            positions[c] = 2

    for c in counts:
        if counts[c] == 8 and c not in positions:
            positions[c] = 0

    for c in four:
        if c not in positions:
            positions[c] = 3

    for c in "abcdefgh":
        if c not in positions:
            positions[c] = 6

    n = ""
    for word in outputs:
        n += str(number(word, positions))
    s += int(n)

print("part 2:", s)
