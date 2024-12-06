import re
from collections import defaultdict
import heapq

map = []
start_i = 0
start_j = 0
with open('6.txt', 'r') as f:
    get_updates = False
    x = 0
    for line in f:
        l = list(line.strip())
        map.append(l)
        for k in range(len(l)):
            if l[k] == '^':
                start_i = x
                start_j = k

        x += 1

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

dirs = [up, right, down, left]

rows = len(map)
cols = len(map[0])

def solve():
    p1 = 0
    p2 = 0
    for i in range(rows):
        for j in range(cols):
            curr_i, curr_j = start_i, start_j
            d = 0
            seen, unique_steps = set(), set()
            while True:
                di,dj = dirs[d]
                next_i, next_j = curr_i+di, curr_j+dj

                if (curr_i,curr_j,d) in seen:
                    p2 += 1
                    break

                seen.add((curr_i,curr_j,d))
                unique_steps.add((curr_i,curr_j))

                if not (0 <= next_i < rows and 0 <= next_j < cols):
                    if map[i][j]=='#':
                        p1 = len(unique_steps)
                    break

                if map[next_i][next_j]=='#' or next_i==i and next_j==j:
                    d = (d + 1) % len(dirs)
                else:
                    curr_i,curr_j = next_i, next_j
    return p1, p2

print(solve())