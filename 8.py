with open("8.txt") as inputfile:
    x = inputfile.read().rstrip().split('\n')

trees = []

def is_visible(trees, i, j):
    # edge case
    if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[i]) - 1:
        return True
    
    tree = trees[i][j]
    row = trees[i]
    col = []

    for z in range(len(trees)):
        col.append(trees[z][j])

    #print(tree, i, j, col, col[:j], col[j+1:], max(row[:i]) < tree or max(row[i+1:]) < tree or max(col[:j]) < tree or max(col[j+1:]) < tree)
    if max(row[:j]) < tree or max(row[j+1:]) < tree or max(col[:i]) < tree or max(col[i+1:]) < tree:
        return True
    return False

def get_scenic_score(trees, i, j):
    tree = trees[i][j]
    row = trees[i]
    col = []

    for z in range(len(trees)):
        col.append(trees[z][j])
    
    left, right, up, down = row[:j], row[j+1:], col[:i], col[i+1:]

    left_score, right_score, up_score, down_score = 0,0,0,0

    for t in list(reversed(left)):
        left_score += 1
        if tree <= t:
            break

    for t in list(reversed(up)):
        up_score += 1
        if tree <= t:
            break

    for t in right:
        right_score += 1
        if tree <= t:
            break

    for t in down:
        down_score += 1
        if tree <= t:
            break

    return left_score * right_score* up_score * down_score

for line in x:
    trees.append([int(tree) for tree in line])


highest_scenic_score = 0
visible_trees = 0
for i in range(len(trees)):
    for j in range(len(trees[i])):
        visible_trees += 1 if is_visible(trees, i, j) else 0
        highest_scenic_score = max(highest_scenic_score, get_scenic_score(trees, i, j))
print(visible_trees)
print(highest_scenic_score)