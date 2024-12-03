import re

with open('3.txt', 'r') as f:
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    s = 0
    for line in f:
        for (a, b) in re.findall(pattern, line):
            s += int(a) * int(b)

    print(s)
with open('3.txt', 'r') as f:
    pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))")
    s = 0
    mul = True
    for line in f:
        for (a,b,do,dont) in re.findall(pattern, line):
            if do == "do()":
                mul = True
            if dont == "don't()":
                mul = False

            if mul and a != "" and b != "":
                s += int(a) * int(b)

    print(s)