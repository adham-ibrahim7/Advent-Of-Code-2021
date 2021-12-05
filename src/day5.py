f = open("../inputs/day5.txt", "r")

lines = list(line.split(" -> ") for line in f.read().split("\n"))

N = 1000
grid1 = list(list(0 for _ in range(N)) for _ in range(N))
grid2 = list(list(0 for _ in range(N)) for _ in range(N))

for line in lines:
    x0, y0 = map(int, line[0].split(","))
    x1, y1 = map(int, line[1].split(","))
    # print(x0, y0, x1, y1)

    if x0 == x1:
        a = min(y0, y1)
        b = max(y0, y1)
        for y in range(a, b+1):
            grid1[x0][y] += 1
            grid2[x0][y] += 1
    elif y0 == y1:
        a = min(x0, x1)
        b = max(x0, x1)
        for x in range(a, b+1):
            grid1[x][y0] += 1
            grid2[x][y0] += 1
    else:
        d = abs(x0 - x1) + 1
        for i in range(0, d):
            grid2[x0 + (i if x0 < x1 else -i)][y0 + (i if y0 < y1 else -i)] += 1

s1 = sum(sum(n > 1 for n in line) for line in grid1)
s2 = sum(sum(n > 1 for n in line) for line in grid2)

# for i in range(N):
#     for j in range(N):
#         print(grid2[j][i], end=" ")
#     print()

print("part 1:", s1)
print("part 2:", s2)