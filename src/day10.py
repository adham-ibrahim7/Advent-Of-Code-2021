f = open("../inputs/day10.txt", "r")

lines = f.read().split("\n")

match = {"(": ")", "{": "}", "[": "]", "<": ">"}
points1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {"(": 1, "[": 2, "{": 3, "<": 4}

def solve(line):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        elif c != match[stack[-1]]:
            return points1[c], []
        else:
            stack.pop()
    return 0, stack

ans1 = 0
scores2 = []
for line in lines:
    s, stack = solve(line)
    ans1 += s
    if s == 0:
        t = 0
        for c in stack[::-1]:
            t = 5 * t + points2[c]
        scores2.append(t)

scores2 = sorted(scores2)

print("part 1:" , ans1)
print("part 2:" , scores2[len(scores2) // 2])