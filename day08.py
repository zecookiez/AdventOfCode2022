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

grid = [list(map(int, i)) for i in input]
H = len(grid)
W = len(grid[0])
tot_visible = most_scenic = 0
for X in range(H):
    for Y in range(W):
        prod = 1
        seen = 0
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            cnt = 0
            x = X + dx
            y = Y + dy
            while 0 <= x < H and 0 <= y < W and grid[X][Y] > grid[x][y]:
                x += dx
                y += dy
                cnt += 1
            if 0 <= x < H and 0 <= y < W:
                cnt += 1
            else:
                seen = 1
            prod *= cnt
        tot_visible += seen
        most_scenic = max(most_scenic, prod)

print(tot_visible, most_scenic)

