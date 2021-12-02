f = open("../inputs/day1.txt", "r")

nums = [int(s) for s in f.read().split("\n")]

ans = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        ans += 1

print("part 1:", ans)

ans = 0
prev = -100000
for i in range(0, len(nums)-3):
    curr = sum(n for n in nums[i:i+3])
    if i < 5:
        print(curr)
    if curr > prev:
        ans += 1
    prev = curr

print("part 2:", ans)