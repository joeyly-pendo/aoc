import re
from collections import defaultdict
import heapq
from itertools import combinations

grid = []
frequencies = defaultdict(list)
visited = set()
visited2 = set()
r, c, = 0, 0
with open('8.txt', 'r') as f:
    for line in f:
        c = len(line)
        row = list(line.strip())
        grid.append(row)
        for i, a in enumerate(row):
            if a.isdigit() or a.isalpha():
                frequencies[a].append((r, i))
        
        r += 1

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def dist(c1, c2):
    visited2.add(c1)
    visited2.add(c2)
    (x1, y1), (x2, y2) = c1, c2
    dx, dy = x2 - x1, y2 - y1
    
    def visit(dir):
        m = 1
        while True:
            x, y = x2 + dir * dx * m, y2 + dir * dy * m
            if 0 <= x < r and 0 <= y < c:
                grid[x][y] = '#'
                if m == 1: visited.add((x, y))
                visited2.add((x, y))
            else:
                break

            m += 1

    visit(1)
    visit(-1)

for a, coords in frequencies.items():
    for c1, c2 in combinations(coords, 2):
        dist(c1, c2)

print_grid(grid)
# p1 is broken, can't be bothered to fix :P
print(len(visited), len(visited2))