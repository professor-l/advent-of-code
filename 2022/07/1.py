all_directories = []
current_dir = []

class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_file(self, size, name):
        self.contents.append(File(size, name))

    def add_dir(self, d):
        self.contents.append(d)
        all_directories.append(d)

    def get_size(self):
        size = 0
        for c in self.contents:
            size += c.get_size()
        return size

    def __str__(self):
        f = ""
        for c in self.contents:
            if isinstance(c, Directory):
                f += "\ndir " + c.name
            else:
                f += "\n" + str(c.size) + c.name
        return f


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def get_size(self):
        return self.size

    def __str__(self):
        return self.name

def command(c):
    if (c[0] == "ls"):
        return
    if (c[0] == "cd"):
        cd(c[1])

def cd(s):
    if (s == ".."):
        current_dir.pop()
    else:
        d = Directory(s)
        if (len(current_dir)):
            current_dir[-1].add_dir(d)
        current_dir.append(d)


with open("input", "r") as f:
    lines = [l.strip().split() for l in f.readlines()]

for line in lines:
    if line[0] == "$":
        command(line[1:])
    elif line[0] == "dir":
        continue
    else:
        current_dir[-1].add_file(int(line[0]), line[1])

size = 0

for d in all_directories:
    s = d.get_size()
    if s <= 100000:
        size += s

print(size)
