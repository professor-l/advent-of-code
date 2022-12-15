from functools import cmp_to_key

values = [[[2]], [[6]]]

with open("input", "r") as f:
    for line in [l.strip() for l in f]:
        if line:
            values.append(eval(line))

def compare(v1, v2):
    # if either is a list
    if (type(v1) == list or type(v2) == list):
        if type(v1) == int:
            v1 = [v1]
        elif type(v2) == int:
            v2 = [v2]

        for i in range(min([len(v1), len(v2)])):
            c = compare(v1[i], v2[i])
            if c:
                return c

        l = len(v1) - len(v2)
        return l // abs(l) if l else l

    elif v1 < v2:
        return -1
    elif v1 > v2:
        return 1

    return 0

values = sorted(values, key=cmp_to_key(compare))
a = values.index([[2]]) + 1
b = values.index([[6]]) + 1

print(a * b)
