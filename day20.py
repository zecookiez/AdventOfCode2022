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

arr = []
seen = set()
tot = 0
for ind, line in enumerate(input):
    arr.append(GI(line) * 811589153)

#assert len(set(arr)) == len(arr)
id = defaultdict(int)
res = deque([(j, i) for i, j in enumerate(arr)])
for _ in range(10):
    for ind, i in enumerate(arr):
        j = list(res).index((i, ind))
        res.rotate(-j)
        res.popleft()
        res.rotate(-i)
        res.appendleft((i, ind))

a = [i for i, j in res].index(0)
print(sum(res[(a + i) % len(res)][0] for i in (1000, 2000, 3000)))
