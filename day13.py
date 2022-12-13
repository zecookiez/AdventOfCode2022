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
    #input = [i.strip() for i in file.readlines()]
    input = file.read().rstrip().split("\n\n")
else:
    """ctrl-d for EOF"""
    #input = [i.strip() for i in stdin.readlines()]
    input = stdin.read().rstrip().split("\n\n")

def is_list(a):
    return type(a) is list
def is_int(a):
    return type(a) is int

def comp(a, b):
    if is_int(a) and is_int(b):
        return (a < b) - (a > b)
    elif is_list(a) and is_list(b):
        for i, j in zip(a, b):
            k = comp(i, j)
            if k != 0: return k
        return (len(a) < len(b)) - (len(a) > len(b))
    elif is_int(a):
        return comp([a], b)
    else:
        return comp(a, [b])

arr = [[[2]], [[6]]]
seen = set()
tot = 0
for ind, line in enumerate(input, 1):
    a, b = list(map(eval, line.split("\n")))
    arr.append(a)
    arr.append(b)
    if comp(a, b) == 1:
        tot += ind

arr.sort(key=cmp_to_key(comp), reverse=True)
print(tot)
print((1 + arr.index([[2]])) * (1 + arr.index([[6]])))

