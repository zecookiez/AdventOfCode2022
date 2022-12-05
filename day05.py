from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product
from heapq import heappush, heappop
from time import time

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

cr, mov = input

is_part_1 = True

"""
Parsing outline:
    Walk through the input's indices line
    If there is a digit, then grab letters aligned in that position
"""

pos = []
ind = cr.split("\n")[-1]
for i in range(len(ind)):
    if ind[i].isdigit():
        crates = [j[i] for j in cr.split("\n")[:-1] if j and j[i] != " "]
        pos.append(crates[::-1])

for line in mov.split("\n"):
    a, b, c = gi(line)
    take = pos[b - 1][-a:]
    pos[b - 1] = pos[b - 1][:-a]
    pos[c - 1].extend(take[::-1] if is_part_1 else take)

print("".join(i[-1] for i in pos))