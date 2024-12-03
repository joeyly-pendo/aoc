from collections import Counter

nums = []
safe = 0
safe_d = 0

def safe_level(line, dampen=False):
    data = [int(n) for n in line.split()]

    incrementing = None
    prev = data[0]
    for i in range(1, len(data)):
        n = data[i]
        diff = n - prev
        curr_dir = diff > 0

        if incrementing is None:
            incrementing = diff > 0

        unsafe = incrementing != curr_dir or abs(diff) > 3 or diff == 0

        if unsafe:
            if dampen:
                data = line.split()
                return any(safe_level(' '.join(data[:j] + data[j + 1:])) for j in range(len(data)))
            else:
                return False
        
        prev = n
        
    return True

with open('input2.txt', 'r') as f:
    for line in f:
        safe += 1 if safe_level(line) else 0

with open('input2.txt', 'r') as f:
    for line in f:
        safe_d += 1 if safe_level(line, True) else 0
            
print(safe, safe_d)