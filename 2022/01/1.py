cal = 0
max_cal = 0

with open("input", "r") as f:
    for line in f:
        try:
            c = int(line.strip())
            cal += c
        except ValueError:
            cal = 0

        if cal > max_cal:
            max_cal = cal

print(max_cal)
