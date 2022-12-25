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


tot = 0
for ind, line in enumerate(input):
    cur = 0
    for i, j in enumerate(line.strip()[::-1]):
        if "0" <= j <= "2":
            cur += int(j) * pow(5, i)
        elif j == "-":
            cur += -pow(5, i)
        else:
            cur += -2 * pow(5, i)
    tot += cur

ans = ""
while tot:
    ch = tot % 5
    if ch == 3:
        ans += "="
        tot += 5 #(3 --> -2)
    elif ch == 4:
        ans += "-"
        tot += 5 #(4 --> -1)
    else:
        ans += str(ch)
    tot //= 5

print(ans[::-1])
