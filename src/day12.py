f = open("../inputs/day12.txt", "r")

lines = f.read().split("\n")

adj = {}

def add(u, v):
    if u not in adj:
        adj[u] = list()
    adj[u].append(v)

for line in lines:
    u, v = line.split("-")
    add(u, v)
    add(v, u)

count = 0
path = []

def dfs1(u):
    global count, path, twice
    if u in path and u.islower():
        return False
    path.append(u)

    if u == "end":
        count += 1

    for v in adj[u]:
        if dfs1(v):
            path.pop()

    return True


dfs1("start")

print("part 1:", count)

count = 0
twice = None
path = []

def dfs2(u):
    global count, path, twice
    if u in path and u.islower():
        if u == "start" or u == "end" or twice is not None:
            return False
        else:
            twice = u
    path.append(u)

    if u == "end":
        count += 1
        # print(path)

    for v in adj[u]:
        if dfs2(v):
            path.pop()
            if v == twice:
                twice = None

    return True

dfs2("start")

print("part 2:", count)
