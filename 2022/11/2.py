MOD = 2*3*5*7*11*13*17*19
class Monkey:
    def __init__(self, description):
        # starting items
        items = description[0].split("Starting items: ")[-1]
        self.items = [int(d) for d in items.split(", ")]

        # operation
        self.operation = description[1].split("Operation: new = ")[-1]

        # divisibility test
        self.div_by = int(description[2].split("Test: divisible by ")[-1])

        # where to throw based on div test results
        self.true = int(description[3][-1])
        self.false = int(description[4][-1])

        # total items inspected in lifetime
        self.total_inspected = 0

    def inspect(self):
        self.total_inspected += 1

        item = self.items.pop(0)
        item = self.calc(item) % MOD

        passed = item % self.div_by == 0
        return (item, self.true if passed else self.false)

    def calc(self, old):
        return eval(self.operation)

    def __str__(self):
        f = ""
        f += "items: " + ", ".join([str(i) for i in self.items]) + "\n"
        f += "op: " + self.operation + "\n"
        f += "div: " + str(self.div_by) + "\n"
        f += "throw: " + str(self.index_true) + " or " + str(self.index_false) + "\n"
        return f

lines = []
with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

monkeys = []
for i in range(1, len(lines), 7):
    monkeys.append(Monkey(lines[i:i+5]))

def take_turn(monkey):
    while len(monkey.items):
        r = monkey.inspect()
        monkeys[r[1]].items.append(r[0])

def round():
    for m in monkeys:
        take_turn(m)

for i in range(10000):
    round()

inspections = sorted([m.total_inspected for m in monkeys])

print(inspections[-2] * inspections[-1])





