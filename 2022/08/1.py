# 90 deg each time
def rotate(a):
    s = len(a)
    for i in range(s // 2):
        for j in range(i, s-i-1):

            t = a[i][j]
            a[i][j] = a[j][s-1-i]
            a[j][s-1-i] = a[s-1-i][s-1-j]
            a[s-1-i][s-1-j] = a[s-1-j][i]
            a[s-1-j][i] = t


trees = []
visible = []

with open("input", "r") as f:
    for line in f:
        trees.append([int(c) for c in line.strip()])
        visible.append([False for _ in line.strip()])

for _ in range(4):
    for i, line in enumerate(trees):
        height = -1
        for j, tree in enumerate(line):
            if tree > height:
                visible[i][j] = True
                height = tree
            elif height == 9:
                break

    rotate(trees)
    rotate(visible)

print(sum([l.count(True) for l in visible]))
