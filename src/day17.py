xmin = 79
xmax = 137

ymin = -176
ymax = -117

def lands(vx, vy):
    x = 0
    y = 0

    besty = 0

    while(True):
        x += vx
        y += vy

        besty = max(besty, y)

        if vx > 0:
            vx -= 1
        vy -= 1
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return besty
        if y < ymin:
            return -1

ans1 = 0
ans2 = 0
for vx in range(0, 300):
    for vy in range(-300, 300):
        y = lands(vx, vy)
        if y > -1:
            ans2 += 1
        ans1 = max(ans1, y)

print("part 1:", ans1)
print("part 2:", ans2)
