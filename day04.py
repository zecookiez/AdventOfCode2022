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
    input = [i.strip() for i in file.readlines()]
    #input = file.read().strip().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().strip().split("\n\n")

"""
arr = []
seen = set()
part1 = part2 = 0
for ind, line in enumerate(input):
    arr.append(GI(line))
"""

part1 = part2 = 0
for ind, line in enumerate(input):
    ran_L1, ran_R1, ran_L2, ran_R2 = pos_gi(line)
    if ran_L1 <= ran_L2 <= ran_R2 <= ran_R1 or \
            ran_L2 <= ran_L1 <= ran_R1 <= ran_R2:
        part1 += 1
    elif ran_L1 <= ran_L2 <= ran_R1 or \
            ran_L2 <= ran_L1 <= ran_R2:
        part2 += 1
print(part1, part1 + part2)