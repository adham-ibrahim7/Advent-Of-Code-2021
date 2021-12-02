f = open("../inputs/day2.txt", "r")

lines = f.read().split("\n")
lines = lines[:-1]

x = 0
y = 0
for line in lines:
    ins, n = line.split(" ")
    n = int(n)
    if ins == "forward":
        x += n
    elif ins == "down":
        y += n
    else:
        y -= n

print("part1:", x * y)

x = 0
aim = 0
y = 0
for line in lines:
    ins, n = line.split(" ")
    n = int(n)
    if ins == "forward":
        x += n
        y += n * aim
    elif ins == "down":
        aim += n
    else:
        aim -= n

print("part2:", x * y)