from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product
from heapq import heappush, heappop
from time import time
from math import gcd
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

t0 = time()
beacons = []
for ind, line in enumerate(input):
    a, b, c, d = gi(line)
    beacons.append((a, b, abs(a-c) + abs(d-b)))

tot = 0
for y in range(0, 4000001):
    # Generate possible beacon locations
    # Find boundary given a beacon, then manually verify if it can contain it
    cand = defaultdict(int)
    for a, b, d2 in beacons:
        # abs(a-x) <= d2 - abs(y-b)
        # -x <= d2 - abs(y-b) - a
        # x >= -(d2 - abs(y-b) + a)
        RHS = d2 - abs(y-b) + a
        LHS = abs(y-b) - d2 + a
        if LHS < RHS:
            cand[LHS - 1] += 1
            cand[RHS + 1] -= 1
    # Reused from part 1, this checks if (x, y) could contain a beacon
    for x, cnt in cand.items():
        if cnt == 0 and 0 <= x <= 4000000 and all(abs(a - x) + abs(b - y) > d2 for a, b, d2 in beacons):
            print(x * 4000000 + y)
            print(time() - t0)
            exit(0) # 3 seconds in pypy

print(tot)
