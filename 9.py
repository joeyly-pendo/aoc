with open(__file__.split('/')[-1].split('.')[0]+ ".txt") as inputfile:
    x = inputfile.read().rstrip().split('\n')

class Node(object):
    def __init__(self, head=None, tail=None, x=0, y=0):
        self.x = x
        self.y = y
        self.tail = tail
        self.head = head
    def move(self, s):
        head_x, head_y, x, y = self.head.x, self.head.y, self.x, self.y
        xdiff = head_x - x
        ydiff = head_y - y
        abs_slope = abs((ydiff)/(xdiff)) if (xdiff) != 0 else 0
        if abs_slope == 2.0 or abs_slope == 0.5: 
            x += 1 if xdiff > 0 else -1
            y += 1 if ydiff > 0 else -1
        else:
            x += int(xdiff / 2)
            y += int(ydiff / 2)
        
        self.x = x
        self.y = y

        if not self.tail:
            s.add((self.x, self.y))
def setup_snake(num_tails):
    head = Node()
    curr = head
    for _ in range(num_tails):
        tail = Node(curr)
        curr.tail = tail
        curr = tail

    return head

def propagate_movement(tail, s):
    if tail:
        tail.move(s)
        propagate_movement(tail.tail, s)

def get_score(m):
    return len(m)

def solve(n):
    s = set()
    head = setup_snake(n)
    for row in x:
        dir, num = row.split()

        for _ in range(int(num)):
            if dir == 'R':
                head.x += 1
            elif dir == 'L':
                head.x -= 1
            elif dir == 'D':
                head.y -= 1
            elif dir == 'U':
                head.y += 1
            propagate_movement(head.tail, s)

    print(len(s))

solve(1)
solve(9)