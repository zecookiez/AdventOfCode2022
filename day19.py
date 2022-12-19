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


# Global maximum and repeated states
glob = [0]
seen = set()

# Upper bound of geodes
def opt(m, q, t):
    return m + q * t + t * (t + 1) // 2

def solve(t, QT, MAT, bp):
    # Cap robots to blueprint max
    COST = [max(bp[0], bp[1], bp[2], bp[4]), bp[3], bp[5], 10**9]
    for ind, i in enumerate(QT):
        if i > COST[ind]: return 0
        # Cap material when we produce more than we can purchase
        if ind < 3 and MAT[ind] >= t * COST[ind] - i * (t - 1): MAT[ind] = t * COST[ind] - i * (t - 1)
        else: MAT[ind] += i
    if opt(MAT[3], QT[3], t) <= glob[-1]: return 0
    if t == 0:
        glob.append(MAT[3])
        return MAT[3]
    label = t, tuple(QT), tuple(MAT)
    if label in seen: return 0
    seen.add(label)
    best = solve(t - 1, QT[:], MAT[:], bp[:])
    if MAT[0] >= bp[4] and MAT[2] >= bp[5]: # geode
        tmp1 = QT[:]
        tmp2 = MAT[:]
        tmp1[3] += 1
        tmp2[0] -= bp[4]
        tmp2[2] -= bp[5]
        tmp2[3] -= 1
        best = max(best, solve(t - 1, tmp1, tmp2, bp))
    if MAT[0] >= bp[2] and MAT[1] >= bp[3]: # obsidian
        tmp1 = QT[:]
        tmp2 = MAT[:]
        tmp1[2] += 1
        tmp2[0] -= bp[2]
        tmp2[1] -= bp[3]
        tmp2[2] -= 1
        best = max(best, solve(t - 1, tmp1, tmp2, bp))
    if MAT[0] >= bp[1]: # clay
        tmp1 = QT[:]
        tmp2 = MAT[:]
        tmp1[1] += 1
        tmp2[0] -= bp[1]
        tmp2[1] -= 1
        best = max(best, solve(t - 1, tmp1, tmp2, bp))
    if MAT[0] >= bp[0]: # ore
        tmp1 = QT[:]
        tmp2 = MAT[:]
        tmp1[0] += 1
        tmp2[0] -= bp[0]
        tmp2[0] -= 1
        best = max(best, solve(t - 1, tmp1, tmp2, bp))
    return best

tot = 0
prod = 1
for ind, line in enumerate(input):
    id1, ore, clay, obsOre, obsClay, geoOre, geoObs = gi(line)
    seen = set()
    glob = [0]
    qt = [1, 0, 0, 0]
    mat = [-1, 0, 0, 0]
    bp = [ore, clay, obsOre, obsClay, geoOre, geoObs]
    ans = solve(24, qt[:], mat[:], bp[:])
    print(ans)
    qual = id1 * ans
    tot += qual
    if ind < 3:
        prod *= solve(32, qt[:], mat[:], bp[:])
print(tot, prod)
