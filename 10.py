with open(__file__.split('/')[-1].split('.')[0]+ ".txt") as inputfile:
    lines = inputfile.read().rstrip().split('\n')

cycle = 1
cycles_left = 0
signal_strength_thing = 20
val_to_add = 0

# part 2
curr_row = ''
rows = []

def print_rows():
    for r in rows:
        print(r)

x = 1

res = 0
while lines:
    if cycles_left == 0:
        x += val_to_add
        line = lines.pop(0)

        if line.startswith("noop"):
            cycles_left = 1
            val_to_add = 0
        elif line.startswith("addx"):
            cmd, num = line.split()
            val_to_add = int(num)
            cycles_left = 2

    crt_pos = (cycle - 1) % 40
    curr_row += '#' if x - 1 <= crt_pos and crt_pos <= x + 1 else '.'
    
    if cycle >= signal_strength_thing:
        res += cycle * x
        signal_strength_thing += 40

    if cycle % 40 == 0:

        rows.append(curr_row)
        curr_row = ''

    cycle += 1
    cycles_left -= 1

print(res)
print_rows()
