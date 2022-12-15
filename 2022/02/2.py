# A B C  /  X Y Z

def translate(letter):
    match letter:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6

def final_score(p, r):
    if (r == "X"):
        letter = (translate(p) - 1) % 3
    elif (r == "Y"):
        letter = translate(p)
    elif (r == "Z"):
        letter = (translate(p) + 1) % 3

    return letter + translate(r) + 1

total = 0

with open("input", "r") as f:
    for i, line in enumerate(f):
        p = line.strip().split()
        total += final_score(p[0], p[1])

print(total)

