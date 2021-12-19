from copy import deepcopy

f = open("../inputs/day18.txt", "r")

def parse(s):
    A = []
    d = 0
    for c in s:
        if c == "[":
            d += 1
        elif c == "]":
            d -= 1
        elif c != ",":
            A.append((int(c), d))
    return A

def add(A, B):
    C = []
    for n, d in A:
        C.append((n, d+1))
    for n, d in B:
        C.append((n, d+1))

    def explode(i):
        if i - 1 >= 0:
            C[i - 1] = (C[i - 1][0] + C[i][0], C[i-1][1])
        if i + 2 <= len(C) - 1:
            C[i + 2] = (C[i + 2][0] + C[i + 1][0], C[i + 2][1])
        C[i] = (0, 4)
        del C[i + 1]

    def split(i):
        k = C[i][0] // 2
        j = C[i][0] - k
        C[i] = (k, C[i][1] + 1)
        C.insert(i+1, (j, C[i][1]))
        if C[i][1] == 5:
            explode(i)
            if i > 0 and C[i-1][0] >= 10:
                split(i-1)
            if i+1 < len(C) and C[i+1][0] >= 10:
                split(i+1)

    i = 0
    while i < len(C):
        n, d = C[i]
        if d == 5:
            explode(i)
            # print(C)
        i += 1

    # print(C)

    i = 0
    while i < len(C):
        if C[i][0] >= 10:
            split(i)
            # print(C)
        i += 1

    return C

def magnitude(A):
    if len(A) == 1:
        return A[0][0]

    B = []
    for i in range(len(A)):
        B.append((i, i, A[i][1]))
    while len(B) > 2:
        i = 0
        reduced = False
        while i < len(B):
            if i < len(B)-1 and B[i][2] == B[i+1][2]:
                B[i] = (B[i][0], B[i+1][1], B[i][2]-1)
                del B[i+1]
                reduced = True
            i += 1
        if not reduced:
            return 0
    k = B[0][1] + 1
    return 3 * magnitude(A[:k]) + 2 * magnitude(A[k:])

lines = f.read().split("\n")
parsed = []

for line in lines:
    parsed.append(parse(line))

A = parsed[0]
for i in range(1, len(parsed)):
    A = add(A, parsed[i])

print("part 1:", magnitude(A))

ans2 = 0
for i in range(len(parsed)):
    for j in range(len(parsed)):
        if i == j:
            continue
        ans2 = max(ans2, magnitude(add(parsed[i], parsed[j])))

print("part 2:", ans2)