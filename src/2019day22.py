f = open("../inputs/day22_2019.txt", "r")

lines = f.read().split("\n")

def forwards(k, MOD):
    for line in lines:
        words = line.split(" ")

        if words[0] == "deal":
            if words[1] == "into":
                k = (MOD - 1 - k) % MOD
            else:
                n = int(words[-1])
                k = (k * n) % MOD
        else:
            n = int(words[-1])
            k = (k - n) % MOD
    return k

print("part 1:", forwards(2019, 10007))

k = 2020
MOD = 119315717514047

def inv(x, MOD):
    return pow(x, MOD-2, MOD)

def pow(a, b, MOD):
    if b == 0:
        return 1
    temp = pow(a, b // 2, MOD)
    temp *= temp
    if b % 2 == 1:
        temp *= a
    return temp % MOD

def backwards(k, MOD):
    for line in lines[::-1]:
        words = line.split(" ")

        if words[0] == "deal":
            if words[1] == "into":
                k = (MOD - 1 - k) % MOD
            else:
                n = int(words[-1])
                k = (k * inv(n, MOD)) % MOD
        else:
            n = int(words[-1])
            k = (k + n) % MOD
    return k

def backwards(k, MOD):
    a = 1
    b = 0
    for line in lines[::-1]:
        words = line.split(" ")

        if words[0] == "deal":
            if words[1] == "into":
                # k = (-k + (MOD-1)) % MOD
                a = (-a) % MOD
                b = (-b + MOD -1) % MOD

            else:
                n = int(words[-1])
                # k = (k * inv(n, MOD)) % MOD
                a = (a * inv(n, MOD)) % MOD
                b = (b * inv(n, MOD)) % MOD
        else:
            n = int(words[-1])
            k = (k + n) % MOD
            b = (b + n) % MOD
    return a, b

a, b = backwards(k, MOD)

N = 101741582076661

# let f(x) = ax + b (mod MOD)
# need to compute f^N (k)

# f^N (k) = a^N * x + b * (1 + a + a^2 + a^3 + ... a^N-1)
#         = a^N * x + b * (1 - a ^ N) / (1 - a)

powa = pow(a, N, MOD)
ans = (powa * k + b * (powa - 1) * inv(a - 1, MOD)) % MOD

print("part 2: ", ans)