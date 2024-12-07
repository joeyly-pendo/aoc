import re
from collections import defaultdict
import heapq


def is_valid(target, nums, p2):
    if len(nums) == 1:
        return nums[0] == target
    
    a,b = nums[0], nums[1]
    next = nums[2:]
    added = is_valid(target, [a + b] + next, p2)
    multed = is_valid(target, [a * b] + next, p2)
    if added or multed:
        return True
    
    if p2 and is_valid(target, [int(str(a)+str(b))] + next, p2):
        return True
    
    return False

with open('7.txt', 'r') as f:
    p1, p2 = 0, 0
    for line in f:
        v, nums = line.strip().split(':')
        v = int(v)
        nums = [int(x) for x in nums.strip().split(' ')]
        if is_valid(v, nums, False):
            p1 += v
        if is_valid(v, nums, True):
            p2 += v
    
    print(p1, p2)