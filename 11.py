import re
import heapq
import mpmath

with open(__file__.split('/')[-1].split('.')[0]+ ".txt") as inputfile:
    lines = inputfile.read().rstrip().split('\n')

worry_level = 0
class Monkey(object):
    def __init__(self, items, op, op_val, test_divisible, if_true, if_false):
        self.items = [mpmath.convert(item) for item in items]
        self.op = op
        self.op_val = mpmath.convert(op_val) if op_val != 'old' else op_val
        self.inspections = 0
        self.test_divisible = mpmath.convert(test_divisible)
        self.if_true = int(if_true)
        self.if_false = int(if_false)
    
    def do_op(self, worry_level):
        val = worry_level if self.op_val == 'old' else self.op_val
        if self.op == '*':
            return worry_level * val
        elif self.op == '+':
            return worry_level + val
        elif self.op == '-':
            return worry_level - val
        elif self.op == '/':
            return worry_level / val
    
    def do_round(self, monkeys):
        for item in self.items:
            self.inspections += 1
            item = self.do_op(item)
            # item = int(item / 3)
            if item % self.test_divisible == 0:
                monkeys[self.if_true].items.append(item)
            else:
                monkeys[self.if_false].items.append(item)
        self.items = []

def build_monkey():
    return

monkeys = []
round = 0
for i in range(0, len(lines), 7):
    monkey_lines = lines[i: i + 7]
    starting_items = [n.strip() for n in monkey_lines[1].split(':')[1].split(',')]
    op_group = re.search(r".*new \= old ([\+\-\*]) ([0-9]+|old)", monkey_lines[2])
    op, op_val = op_group.group(1), op_group.group(2)
    test_divisible = monkey_lines[3].split()[-1]
    if_true = monkey_lines[4].split()[-1]
    if_false = monkey_lines[5].split()[-1]
    monkeys.append(Monkey(starting_items, op, op_val, test_divisible, if_true, if_false))

for i in range(10000):
    print(i)
    for monkey in monkeys:
        monkey.do_round(monkeys)
m, n = heapq.nlargest(2, [monkey.inspections for monkey in monkeys])

print(m * n)
