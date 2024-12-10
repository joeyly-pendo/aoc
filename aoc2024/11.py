from math import pow
from collections import defaultdict
from functools import cache
rocks = [int(n) for n in open('11_test.txt', 'r').readline().strip().split(' ')]

@cache
def transform(rock):
    length = len(str(rock))
    if rock == 0:
        return [1]
    elif length % 2 == 0:
        exp = int(pow(10, length//2))
        l, r = rock // exp, rock % exp
        return [l, r]
    else:
        return [rock * 2024]
    
def blink(rocks, blinks):
    memo = defaultdict(int)
    for s in rocks:
        memo[s] += 1

    for _ in range(blinks):
        new_memo = defaultdict(int)
        for stone, count in memo.items():
            for rock in transform(stone):
                new_memo[rock] += count
        memo = new_memo
    return sum(memo.values())

def blink_helper(rock, dp, blink):
    if (rock, blink) in dp:
        return dp[(rock, blink)]
    elif blink < 0:
        return 1
    
    stepped = transform(rock)
    count = sum(blink_helper(step, dp, blink - 1) for step in stepped)
    if len(stepped) == 2:
        dp[(rock, blink)] = count

    return count

def blink_rec(rocks, blinks):
    return sum([blink_helper(rock, {}, blinks - 1) for rock in rocks])

p1 = blink_rec(rocks, 25)
p2 = blink_rec(rocks, 75)

print(p1, p2)
