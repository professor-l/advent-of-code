rope = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

tail_positions = []

def move(direction, count):
    for i in range(count):
        match direction:
            case "R":
                rope[0][0] += 1
            case "L":
                rope[0][0] -= 1
            case "U":
                rope[0][1] += 1
            case "D":
                rope[0][1] -= 1

        resolve()
        tail_positions.append(rope[-1].copy())

def resolve():
    for i in range(len(rope) - 1):
        head = rope[i]
        tail = rope[i + 1]

        diffx = head[0] - tail[0]
        diffy = head[1] - tail[1]

        if abs(diffx) > 1 and abs(diffy) > 1:
            tail[0] += diffx // 2
            tail[1] += diffy // 2
        elif abs(diffx) > 1:
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
