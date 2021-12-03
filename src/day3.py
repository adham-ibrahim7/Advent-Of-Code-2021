f = open("../inputs/day3.txt", "r")

lines = f.read().split("\n")
n = len(lines[0])

count0 = list(0 for _ in range(n))
count1 = list(0 for _ in range(n))
for line in lines:
    for i, bit in enumerate(line):
        if bit == "0":
            count0[i] += 1
        else:
            count1[i] += 1

# print(count0)
# print(count1)

B = list(1 if count0[i] < count1[i] else 0 for i in range(n))

gamma = 0
epsilon = 0
for i in range(n):
    gamma = 2 * gamma + (B[i])
    epsilon = 2 * epsilon + (1-B[i])

print("part 1:", gamma * epsilon)

# print(B)
# print(int("".join(list(str(x) for x in B)), 2) * int("".join(list(str(1-x) for x in B)), 2))

def find(winner, f,  lines):
    for i in range(n):
        count = 0
        for line in lines:
            count += 1 if int(line[i]) == 1 else -1

        b = winner if count == 0 else f(1) if count > 0 else f(0)
        # print(count, b)

        lines = list(line for line in lines if int(line[i]) == b)
        # print(lines)
        if len(lines) == 1:
            break
    return lines[0]

# print(lines)
oxygen = find(1, lambda x : x, lines)
# print()
co2 = find(0, lambda x : 1 - x, lines)

# print(int(oxygen, 2), int(co2, 2))
print("part 2:", int(oxygen, 2) * int(co2, 2))