current = 1
signal = []

def parse(reg, value):
    if (value != 0):
        signal.append(reg)
    signal.append(reg)
    return reg + value

with open("input", "r") as f:
    for line in f:
        t = line.strip().split()
        if t[0] == "noop":
            current = parse(current, 0)
        elif t[0] == "addx":
            current = parse(current, int(t[1]))

total = 0
for i in range(19, 220, 40):
    total += signal[i] * (i + 1)

print(total)
