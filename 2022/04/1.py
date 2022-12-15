def contains(l1, l2):
    if l1[0] <= l2[0] and l1[1] >= l2[1]:
        return True
    return False

total = 0

with open("input") as f:
    for line in f:
        line = line.strip().split(",")
        a1 = [int(x) for x in line[0].split("-")]
        a2 = [int(x) for x in line[1].split("-")]

        total += 1 if (contains(a1, a2) or contains(a2, a1)) else 0

print(total)
