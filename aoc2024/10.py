g = [[int(x) if x != '.' else -1 for x in line.strip()] for line in open('10.txt', 'r')]
trailheads = [(y, x) for y, row in enumerate(g) for x, col in enumerate(row) if col == 0]

def print_sol(g, visited):
    for y, row in enumerate(g):
        print(''.join([str(col) if (y,x) in visited else '.' for x, col in enumerate(row)]))

def search(pos, p2, visited, n = 0):
    y, x = pos
    if not p2 and pos in visited or y < 0 or y >= len(g) or x < 0 or x >= len(g[y]) or g[y][x] != n: return 0
    visited.add(pos)
    return 1 if n == 9 else sum(search((y + dy, x + dx), p2, visited, n + 1) for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)])

p1 = sum(search(t, False, set()) for t in trailheads)
p2 = sum(search(t, True, set()) for t in trailheads)
print(p1, p2)