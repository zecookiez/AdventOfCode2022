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

blocked = set()
for line in input:
    line = [gi(i) for i in line.split(" -> ")]
    pt = line.pop(0)
    blocked.add((pt[0], pt[1]))
    for x, y in line:
        old = x, y
        blocked.add((x, y))
        while x != pt[0] or y != pt[1]:
            blocked.add((x, y))
            if x != pt[0]:
                x += 1 if x < pt[0] else -1
            if y != pt[1]:
                y += 1 if y < pt[1] else -1
        pt = old[0], old[1]

def low(b):
    return max(j for i, j in b)

floor = low(blocked) + 2
cnt = 0
while True:
    x, y = 500, 0
    if (x, y) in blocked:
        print(cnt)
        exit(0)
    while True:
        for nx, ny in (x,y+1),(x-1,y+1),(x+1,y+1):
            if (nx, ny) not in blocked and y + 1 < floor:
                x, y = nx, ny
                break
        else:
            blocked.add((x, y))
            break
    cnt += 1
