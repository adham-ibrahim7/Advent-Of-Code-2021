from collections import defaultdict

f = open("../inputs/day14.txt", "r")

s, t = f.read().split("\n\n")
orig = s

replacements = {}
for instr in t.split("\n"):
    a, b = instr.split(" -> ")
    replacements[a] = b

def iterate():
    global s
    i = 0
    while i < len(s):
        if s[i:i+2] in replacements:
            s = s[:i+1] + replacements[s[i:i+2]] + s[i+1:]
            i += 1
        i += 1

for _ in range(10):
    iterate()

counts = defaultdict(int)
for c in s:
    counts[c] += 1

chars = sorted(counts, key=lambda x: counts[x])

print("part 1:", counts[chars[-1]] - counts[chars[0]])

s = orig

counts = defaultdict(int)
for i in range(len(s)-1):
    counts[s[i:i+2]] += 1

def iterate():
    temp = defaultdict(int)
    for pair in counts:
        a, b = pair[0], pair[1]

        n = counts[pair]
        if pair in replacements:
            c = replacements[pair]

            temp[a+c] += n
            temp[c+b] += n
            counts[pair] -= n
    for pair in temp:
        counts[pair] += temp[pair]

for _ in range(40):
    iterate()

chars = defaultdict(int)
for pair in counts:
    a, b = pair[0], pair[1]
    chars[a] += counts[pair]
    chars[b] += counts[pair]

for c in chars:
    chars[c] = (chars[c] + 1) // 2

schars = sorted(chars, key=lambda x: chars[x])
print("part 2:", chars[schars[-1]] - chars[schars[0]])
