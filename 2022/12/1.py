from math import inf

values = []
fastest = []
h_fastest = []
start = (-1,-1)
goal = (-1,-1)

open_set = set()
came_from = {}

def convert(c):
    if c == "S":
        return -1
    elif c == "E":
        return 26
    else:
        return ord(c) - 97

def get(arr, coords):
    return arr[coords[0]][coords[1]]

def setv(arr, coords, value):
    arr[coords[0]][coords[1]] = value

def heuristic(i, j):
    return get(values, goal) - values[i][j]

def f_score(a):
    return get(h_fastest, a)

def g_score(a):
    return get(fastest, a)

def get_lowest():
    current = 0
    min_score = inf
    for node in open_set:
        f = f_score(node)
        if f < min_score:
            current = node
            min_score = f

    return current

def neighbors(a):
    r = set()
    if a[0] > 0:
        r.add((a[0] - 1, a[1]))
    if a[0] < len(values) - 1:
        r.add((a[0] + 1, a[1]))
    if a[1] > 0:
        r.add((a[0], a[1] - 1))
    if a[1] < len(values[0]) - 1:
        r.add((a[0], a[1] + 1))

    for n in list(r):
        if get(values, n) > get(values, a) + 1:
            r.remove(n)

    return r

def path(a):
    p = [a]
    while a in came_from.keys():
        a = came_from[a]
        p.append(a)
    return p

with open("input", "r") as f:
    for line in f:
        a = [convert(c) for c in line.strip()]
        values.append(a)

for i in range(len(values)):
    fastest.append([])
    h_fastest.append([])
    for j in range(len(values[i])):
        if values[i][j] == -1:
            start = (i, j)
            fastest[i].append(0)
            h_fastest[i].append(heuristic(i, j))
            continue
        if values[i][j] == 26:
            goal = (i, j)
        fastest[i].append(inf)
        h_fastest[i].append(inf)

open_set.add(start)

while len(open_set) > 0:

    # node in set with lowest f_score
    current = get_lowest()
    if current == goal:
        print(len(path(current)) - 1)

    open_set.remove(current)

    for n in neighbors(current):
        potential = g_score(current) + 1
        if potential  < g_score(n):
            came_from[n] = current
            setv(fastest, n, potential)
            setv(h_fastest, n, potential + heuristic(n[0], n[1]))
            open_set.add(n)

