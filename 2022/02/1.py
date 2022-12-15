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
            return 1
        case "Z":
            return 2

def get_res(p1, p2):
    p1 = translate(p1)
    p2 = translate(p2)

    if (p1 - p2) % 3 == 1:
        return 0
    elif (p2 - p1) % 3 == 1:
        return 6

    return 3

def final_score(p1, p2):
    return get_res(p1, p2) + translate(p2) + 1

total = 0

with open("input", "r") as f:
    for i, line in enumerate(f):
        p = line.strip().split()
        total += final_score(p[0], p[1])

print(total)

