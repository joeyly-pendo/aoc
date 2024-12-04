import re

d = []

with open('4.txt', 'r') as f:
    for line in f:
        d.append(list(line.strip()))

def search(tree, i, j):
    if tree[i][j] != 'X':
        return 0
    
    found = 0
    for k in (-1, 0, 1):
        for h in (-1, 0, 1):
            if k == 0 and h == 0:
                continue
            
            f =  search_xmas(tree, 'X', i, j, k, h)
            found += f
    return found
    
def search_xmas(tree, letter, i, j, iv=0, jv=0):
    l = len(tree)

    if i < 0 or i >= l:
        return 0
    
    h = len(tree[i])
    if j < 0 or j >= h:
        return 0
    
    if tree[i][j] != letter:
        return 0

    match letter:
        case 'X':
            next_letter = 'M'
        case 'M':
            next_letter = 'A'
        case 'A':
            next_letter = 'S'
        case 'S':
            return 1

    return search_xmas(tree, next_letter, i + iv, j + jv, iv, jv)

box = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
dia = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def search_stupid_xmas(d, i, j):
    def is_match(o):
        mat = o[:]
        for _ in range(4):
            (w_i, w_j), (x_i, x_j), (y_i, y_j), (z_i, z_j) = mat
            if d[i + w_i][j + w_j] == 'M' and d[i + x_i][j + x_j] == 'M' and d[i + y_i][j + y_j] == 'S' and d[i + z_i][j + z_j] == 'S':
                return 1
   
            mat.insert(0, mat.pop())
        return 0
    
    if d[i][j] != 'A' or i == 0 or i >= len(d) - 1 or j == 0 or j >= len(d[i]) - 1: 
        return 0

    found = 0
    found += is_match(box)
    # found += is_match(dia)
    return found

xmas = 0
xxxxxmas = 0
for i in range(len(d)):
    for j in range (len(d[i])):
        xmas += search(d, i, j)

        xxxxxmas += search_stupid_xmas(d, i, j)

print(xmas)
print(xxxxxmas)