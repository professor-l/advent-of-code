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

for i in range(6):
    line = ""
    for j in range(40):
        value = signal[(i * 40) + j]
        if abs(value - j) <= 1:
            line += "@"
        else:
            line += " "
    print(line)
