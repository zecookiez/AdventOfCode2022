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
    #input = file.read().rstrip().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().rstrip().split("\n\n")



# 1 if a > b, -1 if b > a, 0 otherwise
def cmp(a, b):
    return (a > b) - (a < b)

# Utility function to update a previous coord given its new one
def update_coord(pt_a, pt_b):
    x, y = pt_a   # current coord
    px, py = pt_b # previous coord
    # If the two cells aren't touching
    if abs(x - px) >= 2 or abs(y - py) >= 2:
        px += cmp(x, px)
        py += cmp(y, py)
    return px, py

part1, part2 = set(), set()
knots = [[0, 0]] + [(0, 0) for i in range(9)]
for line in input:
    direction, quantity = line.split()
    # Repeat
    for _ in range(int(quantity)):
        # Direction update
        if direction == "R": knots[0][1] += 1
        elif direction == "L": knots[0][1] -= 1
        elif direction == "U": knots[0][0] += 1
        else: knots[0][0] -= 1
        # Update rope
        for i in range(1, 10):
            knots[i] = update_coord(knots[i-1], knots[i])
        # Add coords
        part1.add(knots[1])
        part2.add(knots[9])

print(len(part1), len(part2))



