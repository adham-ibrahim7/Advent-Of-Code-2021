f = open("../inputs/day9.txt", "r")

nums = []
for line in f.read().split("\n"):
    nums.append(list(int(c) for c in line))

s = 0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        good = True
        if i > 0 and nums[i-1][j] <= nums[i][j]:
            good = False
        if i < len(nums)-1 and nums[i+1][j] <= nums[i][j]:
            good = False
        if j > 0 and nums[i][j-1] <= nums[i][j]:
            good = False
        if j < len(nums[0])-1 and nums[i][j+1] <= nums[i][j]:
            good = False
        if good:
            s += nums[i][j] + 1

print("part 1:", s)

count = 0
vis = list(list(False for _ in range(len(nums[0]))) for _ in range(len(nums)))

def dfs(i, j):
    if vis[i][j] or nums[i][j] == 9:
        return
    vis[i][j] = True

    global count
    count += 1
    if i > 0:
        dfs(i-1, j)
    if i < len(nums)-1:
        dfs(i+1, j)
    if j > 0:
        dfs(i, j-1)
    if j < len(nums[0])-1:
        dfs(i, j+1)

counts = []
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if not vis[i][j]:
            count = 0
            dfs(i, j)
            if count > 0:
                counts.append(count)

counts = sorted(counts)

print("part 2:", counts[-1] * counts[-2] * counts[-3])