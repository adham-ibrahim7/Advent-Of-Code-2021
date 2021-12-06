f = open("../inputs/day6.txt", "r")

nums = map(int, f.read().split(","))

N = 9
counts = list(0 for _ in range(N))
for n in nums:
    counts[n] += 1

def solve(M, counts):
    for _ in range(M):
        z = counts[0]
        for i in range(1, N):
            counts[i-1] = counts[i]
        counts[6] += z
        counts[8] = z
        # print(counts, sum(counts))
    return sum(counts)

print("part 1:", solve(80, counts.copy()))
print("part 2:", solve(256, counts.copy()))