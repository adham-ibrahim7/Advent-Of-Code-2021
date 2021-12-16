f = open("../inputs/day16.txt", "r")

s = f.read()
t = ""
for c in s:
    t += bin(int(c, 16))[2:].zfill(4)
s = t

ans1 = 0
def decode(packet, start):
    version = int(packet[start: start+3], 2)
    global ans1
    ans1 += version
    typeid = int(packet[start+3: start+6], 2)
    if typeid == 4:
        num = ""
        for i in range(start+6, len(packet), 5):
            num += packet[i+1: i+5]
            if packet[i] == "0":
                break
        return i + 5, int(num, 2)
    else:
        nums = []

        lengthtypeid = int(packet[start+6])
        if lengthtypeid == 0:
            length = int(packet[start+7: start+7+15], 2)
            i = start+7+15
            while i - (start+7+15) < length:
                i, n = decode(packet, i)
                nums.append(n)
        else:
            count = int(packet[start+7: start+7+11], 2)
            i = start+7+11
            for _ in range(count):
                i, n = decode(packet, i)
                nums.append(n)

        if typeid == 0:
            final = sum(nums)
        elif typeid == 1:
            final = 1
            for n in nums:
                final *= n
        elif typeid == 2:
            final = min(nums)
        elif typeid == 3:
            final = max(nums)
        elif typeid == 5:
            final = 1 if nums[0] > nums[1] else 0
        elif typeid == 6:
            final = 1 if nums[0] < nums[1] else 0
        else:
            final = 1 if nums[0] == nums[1] else 0

        return i, final

_, ans2 = decode(s, 0)

print("part 1:", ans1)
print("part 2:", ans2)