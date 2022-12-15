head = [0,0]
tail = [0,0]
tail_positions = []

def move(direction, count):
    for i in range(count):
        match direction:
            case "R":
                head[0] += 1
            case "L":
                head[0] -= 1
            case "U":
                head[1] += 1
            case "D":
                head[1] -= 1

        resolve()
        tail_positions.append(tail.copy())

def resolve():
    diffx = head[0] - tail[0]
    diffy = head[1] - tail[1]

    if abs(diffx) > 1:
        tail[0] += diffx // 2
        tail[1] = head[1]
    elif abs(diffy) > 1:
        tail[1] += diffy // 2
        tail[0] = head[0]

with open("input", "r") as f:
    for line in f:
        t = line.strip().split()
        move(t[0], int(t[1]))

s = [str(t[0]) + "," + str(t[1]) for t in tail_positions]

print(len(set(s)))
