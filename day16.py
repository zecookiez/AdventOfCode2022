from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product, combinations
from heapq import heappush, heappop
from time import time
#from math import gcd
from functools import cmp_to_key

def pos_gi(line):
    return list(map(int, re.findall(r"\d+", line)))
def gi(line):
    #(?:(?<!\d)-)?\d+
    return list(map(int, re.findall(r"-?\d+", line)))
def GI(line):
    return int(re.findall(r"-?\d+", line)[0])
def gf(line):
    return list(map(float, re.findall(r"-?\d+(?:\.\d+)?", line)))
def pos_gf(line):
    return list(map(float, re.findall(r"\d+(?:\.\d+)?", line)))
def gs(line):
    return re.findall(r"[a-zA-Z]+", line)
def neigh4(x, y, H, W):
    for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)
def neigh8(x, y, H, W):
    for nx, ny in (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)

OUTPUT = 1
if OUTPUT:
    file = open("input.txt", "r")
    input = [i.strip() for i in file.readlines()]
    #input = file.read().rstrip().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().rstrip().split("\n\n")

arr = defaultdict(list)
seen = set()
tot = 0
good = []
for ind, line in enumerate(input):
    amount = GI(line)
    line = line.split()
    A = line[1]
    child = line[9:]
    arr[A] = amount, [i.replace(",", "") for i in child]
    if amount:
        good.append(A)
assert len(good) == len(set(good))
good = set(good)
memo = {}
def solve(time, cur, open):
    if time == 0 or len(open) == 0:
        return 0
    label = time, cur, frozenset(open)
    if label in memo: return memo[label]
    t1, nxt1 = arr[cur]
    best = 0
    if cur in open and t1 != 0:
        best = solve(time - 1, cur, open - {cur}) + t1 * (time - 1)
    for ch in nxt1:
        case = solve(time - 1, ch, open)
        best = max(best, case)
    memo[label] = best
    return best

# Never finished running LOL
# I have an exam tomorrow I will maybe optimize this later..............................
best = 2292
for r in range(6, len(good)+1):
    for half_a in combinations(list(good), r):
        half_a = set(half_a)
        half_b = set(good - set(half_a))
        best = max(best, solve(26, "AA", half_a) + solve(26, "AA", half_b))
    print(best)

print(best)