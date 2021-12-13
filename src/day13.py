f = open("../inputs/day13.txt", "r")

coords, instrs = f.read().split("\n\n")
coords = list(map(int, coord.split(",")) for coord in coords.split("\n"))
instrs = list(line[len("fold along "):] for line in instrs.split("\n"))

def f(x, y, instr):
    n = int(instr[2:])
    if instr[0] == "y":
        if y >= n:
            return x, 2 * n - y
        else:
            return x, y
    else:
        if x >= n:
            return 2 * n - x, y
        else:
            return x, y

res = set()

def perform(instr, res):
    temp = set()
    for (x, y) in res:
        temp.add(f(x, y, instr))
    return temp

res = perform(instrs[0], coords)

print("part 1:", len(res))

for instr in instrs[1:]:
    res = perform(instr, res)

out = ""
for y in range(10):
    for x in range(50):
        out += "# " if (x, y) in res else ". "
    out += "\n"

print("part 2:")
print(out)
