import re
from collections import defaultdict
import heapq
from itertools import combinations
from copy import deepcopy

def print_blocks(q):
    print([(i - 1, j) for (i, j) in q if i - 1 >= 0])

def get_input(p2 = False):
    # (i, d), i = ID + 1, d = count of this block
    l = [(i // 2 + 1 if i % 2 else 0, int(d)) for i, d in enumerate(open('9_test.txt').readline().strip(), 1)]
    if not p2:
        # this is dumb
        l = [(i, 1) for i, d in l for _ in range(d)]
    return l

def solve(b):
    # right to left
    for r in range(len(b) - 1, -1, -1):
        # forward to right, n(n-1)/2 ~= O(n^2)
        for l in range(r):
            (ld, ls), (rd, rs)  =  b[l], b[r]
            
            # left empty, right nonempty, can fill space
            if rd > 0 and not ld and rs <= ls:
                # reduce the empty space on the left and set the right to nothing
                b[l], b[r] = (0, ls - rs), (0, rs)

                # insert the block
                b.insert(l, (rd, rs))

    # print_blocks(b)

    expanded = lambda x: ([d] * s for d, s in x)
    flatten = lambda x: [x for x in x for x in x]
    return sum(i * (c - 1) for i, c in enumerate(flatten(expanded(b))) if c)

print(solve(get_input()))
print(solve(get_input(True)))