letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0

with open("input", "r") as f:
    for line in f:
        line = line.strip()
        l = len(line) // 2
        c1 = line[:l]
        c2 = line[l:]

        for letter in c1:
            if letter in c2:
                priority += letters.index(letter)
                break

print(priority)
