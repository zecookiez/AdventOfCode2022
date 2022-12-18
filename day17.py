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

S = input[0]
block = [
    ["####"],
    [
        ".#.",
        "###",
        ".#."
    ],
    [
        "###",
        "..#",
        "..#"
    ],
    ["#", "#", "#", "#"],
    [
        "##",
        "##"
    ]
]

def isgood(x, y, bl, grid):
    H = len(bl)
    W = len(bl[0])
    for i in range(x, x + H):
        for j in range(y, y + W):
            if not (0 <= i and 0 <= j < 7): return False
            if bl[i-x][j-y] == ".": continue
            if (i, j) in grid:
                return False
    return True


# This is so god awful and ugly but it works
# I am not touching this

grid = set()
pt = mx = it = ADD = 0
memo = {}
target = 1000000000000

while it < target:
    depth = [0] * 7
    for a,b in grid:
        depth[b] = max(depth[b], a)
    depth = [i - min(depth) for i in depth]
    label = it % len(block), pt % len(S), tuple(depth)
    if label in memo:
        prev_id, p_mx = memo[label]
        cycle = it - prev_id + 1
        height = mx - p_mx
        qt = (target - it) // cycle
        ADD += (3 + height) * qt
        it += cycle * qt
        memo = {}
    b = block[it % len(block)]
    x = mx + 3
    y = 2
    while True:
        if S[pt % len(S)] == "<":
            if isgood(x, y - 1, b, grid):
                y -= 1
        else:
            if isgood(x, y + 1, b, grid):
                y += 1
        pt += 1
        if not isgood(x - 1, y, b, grid):
            break
        x -= 1
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == "#":
                grid.add((i+x, j+y))
    mx = max(i + 1 for i, j in grid)
    it += 1
    memo[label] = it, mx

print(mx + ADD)
