letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0

with open("input", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        l1 = lines[i].strip()
        l2 = lines[i + 1].strip()
        l3 = lines[i + 2].strip()

        for letter in l1:
            if letter in l2 and letter in l3:
                priority += letters.index(letter)
                break

print(priority)
