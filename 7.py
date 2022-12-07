with open("input.txt") as inputfile:
    x = inputfile.read().rstrip().split('\n')

class Node(object):
    def __init__(self, name, type, parent, size=0):
        self.name = name
        self.type = type
        self.parent = parent # should always be a dir
        self.children = {}
        self.size = size
        self.only_files = True

    def add_child(self, name, obj):
        if obj.type == 'dir':
            self.only_files = False
        self.children[name] = obj

def backtrack_file_size(node, file_size):
    if node.parent != None:
        node.parent.size += file_size
        backtrack_file_size(node.parent, file_size)

def build_filesystem(lines):
    root = Node('/', 'dir', None)
    curr = root
    for line in lines:
        if line.startswith('$ cd'):
            name = line.split()[2]

            if name == '/':
                curr = root
            elif name == '..':
                curr = curr.parent
            else:
                curr = curr.children[name]
        elif line == '$ ls': # toss, don't care
            continue
        elif line.startswith('dir'):
            name = line.split()[1]
            new_dir = Node(name, 'dir', curr)
            curr.add_child(name, new_dir)
        else: # assuming it's a file
            size, filename = line.split()
            size = int(size)
            new_file = Node(filename, 'file', curr, size)
            backtrack_file_size(new_file, size)
    return root

def find_dir_size(node, size):
    if node.type == 'dir':
        children = node.children.values()
        return (node.size if node.size <= size else 0) + (sum([find_dir_size(n, size) for n in children]) if not node.only_files else 0)
    return 0

def find_min_delete_amount(root, total, target_unused):
    def delete_helper(node, min_delete_amount):
        if node.type == 'file':
            return float('inf')
        elif node.type == 'dir':
            if node.only_files:
                return node.size 
            else:
                child_vals = [delete_helper(n, min_delete_amount) for n in node.children.values() if n.type == 'dir' and n.size >= min_delete_amount]

                return min(child_vals + [node.size])

    curr_unused = total - root.size
    delete_amount = target_unused - curr_unused
    return delete_helper(root, delete_amount)


total = 70000000
target_unused = 30000000
root = build_filesystem(x)

print("a: ", find_dir_size(root, 100000))
print("b: ", find_min_delete_amount(root, total, target_unused))