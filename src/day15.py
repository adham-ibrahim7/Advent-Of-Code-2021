from collections import defaultdict
import heapq
from copy import deepcopy

f = open("../inputs/day15.txt", "r")

lines = f.read().split("\n")
grid = list(list(int(c) for c in line) for line in lines)

N = len(grid)
M = len(grid[0])

dp = {}
for i in range(N):
    for j in range(M):
        dp[(i, j)] = 10000000 if i + j != 0 else 0
        if i > 0:
            dp[(i, j)] = min(dp[(i, j)], dp[(i-1, j)] + grid[i][j])
        if j > 0:
            dp[(i, j)] = min(dp[(i, j)], dp[(i, j-1)] + grid[i][j])

print(dp[(N-1, M-1)])