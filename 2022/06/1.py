with open("input", "r") as f:
    signal = f.readline().strip()

    found = False
    index = 4

    while not found:
        test = signal[:4]

        if len(set(test)) != len(test):
            index += 1
            signal = signal[1:]
        else:
            found = True

print(index)
