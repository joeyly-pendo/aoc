with open(__file__.split('/')[-1].split('.')[0]+ ".txt") as inputfile:
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

    return max(row[:j]) < tree or max(row[j+1:]) < tree or max(col[:i]) < tree or max(col[i+1:]) < tree

def get_scenic_score(trees, i, j):
    tree = trees[i][j]
    row = trees[i]
    col = []

    for z in range(len(trees)):
        col.append(trees[z][j])
    
    left, right, up, down = row[j-1::-1], row[j+1:], col[i-1::-1], col[i+1:]

    def get_score(arr):
        score = 0
        # to improve time complexity, create a Tree class to store highest height and distance from highest height in each direction to avoid using another for-loop
        for t in arr:
            score += 1
            if tree <= t:
                break
        return score

    return get_score(left) * get_score(right) * get_score(up) * get_score(down)

# build trees
for line in x:
    trees.append([int(tree) for tree in line])

highest_scenic_score = 0
visible_trees = 0
# iterate trees ad solve for part 1 & 2
for i in range(len(trees)):
    for j in range(len(trees[i])):
        visible_trees += 1 if is_visible(trees, i, j) else 0
        highest_scenic_score = max(highest_scenic_score, get_scenic_score(trees, i, j))
print("a: ", visible_trees)
print("b: ", highest_scenic_score)