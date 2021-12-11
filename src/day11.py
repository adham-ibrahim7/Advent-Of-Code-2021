from copy import deepcopy

f = open("../inputs/day11.txt", "r")

lines = f.read().split("\n")

nums = list()
for line in lines:
    nums.append(list(int(c) for c in line))
orig = deepcopy(nums)

N = len(nums)
M = len(nums[0])

def simulate():
    # def flash(i, j):
    #     if nums[i][j] != 10:
    #         return
    #
    #     for k in range(i-1, i+1):
    #         for h in range(j-1, j+1):
    #             if k != i or h != j and 0 <= k < N and 0 <= h < M:
    #                 nums[k][h] += 1
    #                 # flash(k, h)

    flashed = []
    for i in range(N):
        for j in range(M):
            nums[i][j] += 1
            if nums[i][j] == 10:
                flashed.append((i, j))

    # printnums()

    while(True):
        temp = []
        for i, j in flashed:
            for k in range(i - 1, i + 2):
                for h in range(j - 1, j + 2):
                    if (k != i or h != j) and 0 <= k < N and 0 <= h < M:
                        nums[k][h] += 1
                        if nums[k][h] == 10:
                            temp.append((k, h))

        if len(temp) == 0:
            break
        flashed = temp


    count = 0
    for i in range(N):
        for j in range(M):
            if nums[i][j] > 9:
                nums[i][j] = 0
                count += 1
    return count

def printnums():
    for line in nums:
        print(line)
    print()

s = sum(simulate() for _ in range(100))
print("part 1:", s)

nums = orig

i = 1
while(True):
    count = simulate()
    if count == 100:
        break
    i += 1

print("part 2:", i)