import re
from collections import defaultdict
import heapq
from itertools import combinations
from copy import deepcopy

g = [[int(x) if x != '.' else -1 for x in line.strip()] for line in open('10.txt', 'r')]
trailheads = [(y, x) for y, row in enumerate(g) for x, col in enumerate(row) if col == 0]

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

dirs = [up, right, down, left]

def print_sol(g, visited):
    for y, row in enumerate(g):
        print(''.join([str(col) if (y,x) in visited else '.' for x, col in enumerate(row)]))

def search(pos, p2, visited, n = 0):
    y, x = pos

    if not p2 and pos in visited or y < 0 or y >= len(g) or x < 0 or x >= len(g[y]):
        return 0
    elif g[y][x] == n:
        visited.add(pos)
        return 1 if n == 9 else sum(search((y + dy, x + dx), p2, visited, n + 1) for (dy, dx) in dirs)
    
    return 0

def solve():
    p1 , p2 = 0, 0
    for t in trailheads:
        p1 += search(t, False, set())
        p2 += search(t, True, set())
    
    print(p1, p2)

solve()