import re
from collections import defaultdict
import heapq

class Node(object):
    def __init__(self, val: int, rules):
        self.val = val
        self.rules = rules

    def __repr__(self):
        return f'Node value: {self.val}'

    def __lt__(self, other):
        return other in self.rules

rules = defaultdict(set)
updates = []
p1 = 0
p2 = 0

with open('5.txt', 'r') as f:
    get_updates = False
    for line in f:
        l = line.strip()

        if l == "":
            get_updates = True
            continue

        if get_updates:
            updates.append([int(x) for x in l.split(',')])
        else:
            page1, page2 = l.split('|')
            rules[int(page1)].add(int(page2))

def is_correct(u):
    update_len = len(u)
    for i in range(update_len - 1):
        p = u[i]
        for j in range(i + 1, update_len):
            if p in rules[u[j]]:
                return False
            
    return True
            
def fix_update(u):
    invalid = False
    valid = False
    while not valid:
        valid = True
        update_len = len(u)
        for i in range(update_len - 1):
            p = u[i]
            for j in range(i + 1, update_len):
                if p in rules[u[j]]:
                    valid = False
                    invalid = True
                    u[i], u[j] = u[j], u[i]
    print(u)
    return u[update_len // 2] if invalid else 0

for update in updates:
    print(is_correct(update))
    if is_correct(update):
        p1 += update[len(update) // 2]
    else:
        print(update)
        fixed = fix_update(update)
        print(fixed)
        p2 += fixed

print(p1)
print(p2)