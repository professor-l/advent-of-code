cal = 0
max_cals = [0, 0, 0]

with open("input", "r") as f:
    for line in f:
        try:
            c = int(line.strip())
            cal += c
            m = min(max_cals)
            if (cal > m):
                max_cals[max_cals.index(m)] = cal
        except ValueError:
            cal = 0

print(sum(max_cals))
