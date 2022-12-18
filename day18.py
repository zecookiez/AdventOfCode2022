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


# This is so ugly
def adj(x, y, z):
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            for dz in -1, 0, 1:
                if [dx,dy,dz].count(0) == 2:
                    yield (x + dx, y + dy, z + dz)

pt1 = pt2 = 0
pt = set()
for ind, line in enumerate(input):
    x, y, z = map(int, line.split(","))
    pt.add((x, y, z))

inside = defaultdict(int)
for x, y, z in pt:
    for X, Y, Z in adj(x, y, z):
        if (X, Y, Z) not in pt:
            pt1 += 1
            inside[X, Y, Z] += 1

bs = set()
outside = set()
for x, y, z in inside:
    if (x, y, z) in bs: continue
    queue = [(x, y, z)]
    cur = set()
    for x, y, z in queue:
        # Imaginary boundary
        if not -5 <= x <= 25: continue
        elif not -5 <= y <= 25: continue
        elif not -5 <= z <= 25: continue
        for X, Y, Z in adj(x, y, z):
            if (X, Y, Z) not in pt and (X, Y, Z) not in bs:
                cur.add((X, Y, Z))
                bs.add((X, Y, Z))
                queue.append((X, Y, Z))
    # This compartment is the outside
    if (-5, -5, -5) in cur:
        outside = cur
        break

for x, y, z in pt:
    for X, Y, Z in adj(x, y, z):
        if (X, Y, Z) not in pt and (X, Y, Z) in outside:
            pt2 += 1

print(pt1, pt2)