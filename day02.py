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
    #input = file.read().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().split("\n\n")


part1 = part2 = 0
for line in input:
    # Part 1
    a, b = line.split()
    P1 = "RPS"["ABC".find(a)]
    P2 = "RPS"["XYZ".find(b)]
    if P1 == P2:
        part1 += 3
    elif P2 + P1 in "RS SP PR":
        part1 += 6
    part1 += "RPS".find(P2) + 1

    # Part 2
    part2 += "XYZ".find(b) * 3
    if b == "X":
        P1 = "RSP"["PRS".find(P1)]
    elif b == "Z":
        P1 = "SPR"["PRS".find(P1)]
    part2 += "RPS".find(P1) + 1

print(part1, part2)
