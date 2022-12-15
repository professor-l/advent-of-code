def overlaps(l1, l2):
    if l2[0] >= l1[0] and l2[0] <= l1[1]:
        return True
    return False

total = 0

with open("input") as f:
    for line in f:
        line = line.strip().split(",")
        a1 = [int(x) for x in line[0].split("-")]
        a2 = [int(x) for x in line[1].split("-")]

        total += 1 if (overlaps(a1, a2) or overlaps(a2, a1)) else 0

print(total)
