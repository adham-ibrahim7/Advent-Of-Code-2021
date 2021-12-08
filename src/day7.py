f = open("../inputs/day7.txt", "r")

nums = list(map(int, f.read().split(",")))

def solve(dist):
    best = 10000000000000000
    for x in range(0, 10000):
        d = sum(dist(abs(x - n)) for n in nums)
        if d < best:
            best = d
    return best

print("part1:", solve(lambda d: d))
print("part2:", solve(lambda d: d * (d+1) // 2))
