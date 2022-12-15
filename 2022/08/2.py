trees = []
scores = []

with open("input", "r") as f:
    for line in f:
        trees.append([int(c) for c in line.strip()])

def get_score(x, y):
    height = trees[x][y]
    score = 1

    current = 0
    for i in range(x + 1, len(trees)):
        current += 1
        if trees[i][y] >= height:
            break

    score *= current

    current = 0
    for i in range(x - 1, -1, -1):
        current += 1
        if trees[i][y] >= height:
            break

    score *= current

    current = 0
    for i in range(y + 1, len(trees)):
        current += 1
        if trees[x][i] >= height:
            break

    score *= current

    current = 0
    for i in range(y - 1, -1, -1):
        current += 1
        if trees[x][i] >= height:
            break

    score *= current

    return score

for i in range(len(trees)):
    scores.append([])
    for j in range(len(trees[i])):
        scores[i].append(get_score(i, j))

print(max([max(row) for row in scores]))
