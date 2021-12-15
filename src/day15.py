from collections import defaultdict
import heapq
from copy import deepcopy

f = open("../inputs/day15.txt", "r")

lines = f.read().split("\n")
grid = list(list(int(c) for c in line) for line in lines)

N = len(grid)
M = len(grid[0])

def bellmanford(weights):
    dp = {}
    for i in range(N):
        for j in range(M):
            dp[(i, j)] = 100000000000
    dp[(0, 0)] = 0

    # print(1000 * N * M)

    for _ in range(300):
        for i in range(N):
            for j in range(M):
                if i > 0:
                    dp[(i-1, j)] = min(dp[(i-1, j)], dp[(i, j)] + weights[i-1][j])
                if j > 0:
                    dp[(i, j-1)] = min(dp[(i, j-1)], dp[(i, j)] + weights[i][j-1])
                if i < N-1:
                    dp[(i+1, j)] = min(dp[(i+1, j)], dp[(i, j)] + weights[i+1][j])
                if j < M-1:
                    dp[(i, j+1)] = min(dp[(i, j+1)], dp[(i, j)] + weights[i][j+1])

    return dp

def dijkstra(src, weights):
    si, sj = src
    unvisited = [(0, si, sj)]
    dist = {(si, sj): 0}
    for i in range(N):
        for j in range(M):
            if (i, j) != (si, sj):
                unvisited.append((100000000, i, j))
                dist[(i, j)] = 100000000

    heapq.heapify(unvisited)

    while len(unvisited) > 0:
        d, i, j = heapq.heappop(unvisited)

        if i > 0 and d + weights[i-1][j] < dist[(i-1, j)]:
            # heapq.((dist[(i-1, j)], i-1, j))

            dist[(i-1, j)] = d + weights[i-1][j]

        if j > 0 and d + weights[i][j-1] < dist[(i, j-1)]:
            dist[(i, j-1)] = d + weights[i][j-1]

        if i < N-1 and d + weights[i+1][j] < dist[(i+1, j)]:
            dist[(i+1, j)] = d + weights[i+1][j]

        if i < M-1 and d + weights[i][j+1] < dist[(i, j+1)]:
            dist[(i, j+1)] = d + weights[i][j+1]



grids = []
for k in range(5):
    gridk = deepcopy(grid)
    for i in range(N):
        for j in range(M):
            gridk[i][j] += k
            if gridk[i][j] > 9:
                gridk[i][j] -= 9
    grids.append(gridk)

# print("part 1:", bellmanford(grids[0])[(N - 1, M - 1)])
