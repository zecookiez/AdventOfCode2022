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
H = len(grid)
W = len(grid[0])

wind_r = defaultdict(list)
wind_c = defaultdict(list)
for i in range(H):
    for j, ch in enumerate(grid[i]):
        if ch == "^": wind_c[j].append((i, -1))
        elif ch == ">": wind_r[i].append((j, 1))
        elif ch == "<": wind_r[i].append((j, -1))
        elif ch == "v": wind_c[j].append((i, 1))

# Instead of checking all blizzards, check the ones that are:
#    blizzards that move horizontally and are on the same row as (x, y)
#    blizzards that move vertically and are on the same column as (x, y)

# You can still optimize this by precalculating blizzard positions level-by-level because of how bfs increments time
def good(x, y, t):
    # Check vertical blizzards
    if any(1 + (a - 1 + t * delta) % (H - 2) == x for a, delta in wind_c[y]):
        return False
    # Check horizontal blizzards
    if any(1 + (a - 1 + t * delta) % (W - 2) == y for a, delta in wind_r[x]):
        return False
    return True

def solve(start, sx, sy, tgt):
    queue = [(start, sx, sy)]
    seen = set()
    for t, x, y in queue:
        if x == tgt[0] and y == tgt[1]:
            return t
        for nx, ny in neigh4(x, y, H, W):
            if grid[nx][ny] == "#": continue
            elif (t + 1, nx, ny) in seen: continue
            elif good(nx, ny, t + 1):
                seen.add((t + 1, nx, ny))
                queue.append((t + 1, nx, ny))
        if (t + 1, x, y) not in seen and good(x, y, t + 1):
            seen.add((t + 1, x, y))
            queue.append((t + 1, x, y))
    assert False

x, y = 0, 1
tgt = H - 1, W - 2
firstTrip = solve(0, x, y, tgt) # go there
backTrip = solve(firstTrip, tgt[0], tgt[1], (0, 1)) # go back
secondTrip = solve(backTrip, x, y, tgt) # go there (again)
print(firstTrip, secondTrip)