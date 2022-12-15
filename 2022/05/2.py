"""
    [H]         [D]     [P]
[W] [B]         [C] [Z] [D]
[T] [J]     [T] [J] [D] [J]
[H] [Z]     [H] [H] [W] [S]     [M]
[P] [F] [R] [P] [Z] [F] [W]     [F]
[J] [V] [T] [N] [F] [G] [Z] [S] [S]
[C] [R] [P] [S] [V] [M] [V] [D] [Z]
[F] [G] [H] [Z] [N] [P] [M] [N] [D]
 1   2   3   4   5   6   7   8   9
"""

stacks = [
    ["F", "C", "J", "P", "H", "T", "W"],
    ["G", "R", "V", "F", "Z", "J", "B", "H"],
    ["H", "P", "T", "R"],
    ["Z", "S", "N", "P", "H", "T"],
    ["N", "V", "F", "Z", "H", "J", "C", "D"],
    ["P", "M", "G", "F", "W", "D", "Z"],
    ["M", "V", "Z", "W", "S", "J", "D", "P"],
    ["N", "D", "S"],
    ["D", "Z", "S", "F", "M"]
]

with open("input", "r") as f:
    for line in f:
        line = line.strip().split("move ")[-1]
        count = int(line.split()[0])
        line = line.split("from ")[-1]
        c1 = int(line.split()[0]) - 1
        c2 = int(line.split("to ")[-1]) - 1

        move = stacks[c1][count * -1:]
        for m in move:
            stacks[c2].append(m)
        stacks[c1] = stacks[c1][:count * -1]

print("".join([s[-1] for s in stacks]))
