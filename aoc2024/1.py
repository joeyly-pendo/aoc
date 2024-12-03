from collections import Counter

list_a = []
list_b = []
counter = Counter()
with open('input.txt', 'r') as f:
    for line in f:
        a, b = line.strip().split('   ')
        a = int(a)

        list_a.append(a)
        list_b.append(b)

        counter[b] += 1
 
list_a.sort()
list_b.sort()

print(list_a)

diff = 0
simm = 0

for i in range(len(list_a)):
    a = list_a[i]
    b = list_b[i]
    diff += abs(a - int(list_b[i]))
    simm += a * counter[str(a)]
    print(a, counter[str(a)])

print(diff, simm)