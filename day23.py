from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product, combinations
from heapq import heappush, heappop
from time import time
#from math import gcd
from functools import cmp_to_key
from fractions import Fraction

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
    #input = file.read().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().split("\n\n")

grid = input[:]
pt = set()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "#":
            pt.add((i, j))

for rnd in range(10**5):
    prop = defaultdict(list)
    for x, y in pt:
        isn = all((x-1, ny) not in pt for ny in (y-1,y,y+1))
        iss = all((x+1, ny) not in pt for ny in (y - 1, y, y + 1))
        isw = all((nx, y-1) not in pt for nx in (x-1,x,x+1))
        ise = all((nx, y+1) not in pt for nx in (x-1,x,x+1))
        if isn and iss and isw and ise: continue
        cycle = [
            (isn, -1, 0),
            (iss, 1, 0),
            (isw, 0, -1),
            (ise, 0, 1)
        ]
        for b, dx, dy in cycle[rnd%4:] + cycle[:rnd%4]:
            if b:
                prop[x+dx, y+dy].append((x, y))
                break
    npt = set()
    rem = set()
    for (nx, ny), pts in prop.items():
        if len(pts) == 1:
            npt.add((nx, ny))
            pt -= {pts[0]}
    if not npt:
        print(rnd + 1)
        break
    pt |= npt
    if rnd == 9:
        X = sorted(i for i, j in pt)
        Y = sorted(j for i, j in pt)
        area = (X[-1] - X[0] + 1) * (Y[-1] - Y[0] + 1)
        print(area - len(pt))