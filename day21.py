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
    #input = file.read().rstrip().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().rstrip().split("\n\n")

op = defaultdict(list)
for ind, line in enumerate(input):
    a = line.split()
    a[0] = a[0][:-1]
    if len(a) == 2:
        op[a[0]] = [Fraction(GI(line), 1)]
    else:
        op[a[0]] = a[1:]

def solve(cur, x):
    if cur == "humn":
        return Fraction(x, 1)
    line = op[cur]
    if len(line) == 1: return line[0]
    elif "+" in line:
        return solve(line[0], x) + solve(line[2], x)
    elif "-" in line:
        return solve(line[0], x) - solve(line[2], x)
    elif "*" in line:
        return solve(line[0], x) * solve(line[2], x)
    elif "/" in line:
        return solve(line[0], x) / solve(line[2], x)
    assert False

# Saw that C remained as a constant
# And noticed that A was an linear equation

a, _, c = op["root"]
const = solve(c, 0)
slope = solve(a, 1) - solve(a, 0)

ans = (const - solve(a, 0)) / slope
assert solve(a, ans) == solve(c, ans)
print(ans)