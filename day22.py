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

OUTPUT =1
if OUTPUT:
    file = open("input.txt", "r")
    #input = [i.strip() for i in file.readlines()]
    input = file.read().split("\n\n")
else:
    """ctrl-d for EOF"""
    #input = [i.strip() for i in stdin.readlines()]
    input = stdin.read().split("\n\n")


grid, path = input
grid = grid.split("\n")
H = len(grid)
W = max(map(len, grid))
grid = [i + " " * W for i in grid]

def leftmost(grid, i):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            return i, j
    assert False

cnt = [0,0,0]
def log(x, y, nx, ny):
    tp = list(map(list, grid))
    tp[x][y] = "A"
    tp[nx][ny] = "B"
    for i in tp:
        print("".join(i))

def move(x, y, dx, dy):
    A = x // 50, y // 50
    reg = {
        (0, 1): 0,
        (0, 2): 1,
        (1, 1): 2,
        (2, 0): 3,
        (2, 1): 4,
        (3, 0): 5
    }
    """
    .AB
    .C.
    ED.  <- yea 12am me did not know my alphabet ordering 
    F..
    """
    A = reg[A]
    nx, ny = (x + dx) % H, (y + dy) % W
    d1, d2 = dx, dy
    if A == 0 and x == 0 and dx == -1: # AF
        nx, ny = 3 * 50 + y % 50, 0
        d1, d2 = 0, 1
    if A == 0 and y == 50 and dy == -1: # AE
        nx, ny = 3 * 50 - x % 50 - 1, 0
        d1, d2 = 0, 1
    if A == 1 and x == 0 and dx == -1: # BF
        nx, ny = H - 1, y % 50
        d1, d2 = -1, 0
    if A == 1 and y == W - 1 and dy == 1: # BD
        nx, ny = 3 * 50 - 1 - x % 50, 2 * 50 - 1
        d1, d2 = 0, -1
    if A == 1 and x == 49 and dx == 1:  # BC
        nx, ny = 50 + y % 50, 2 * 50 - 1
        d1, d2 = 0, -1
    if A == 2 and y == 50 and dy == -1: # CE
        nx, ny = 2 * 50, x % 50
        d1, d2 = 1, 0
    if A == 2 and y == 50 * 2 - 1 and dy == 1: # CB
        nx, ny = 49, 2 * 50 + x % 50
        d1, d2 = -1, 0
    if A == 3 and y == 0 and dy == -1: # EA
        nx, ny = 49 - x % 50, 50
        d1, d2 = 0, 1
    if A == 3 and x == 2*50 and dx == -1: # EC
        nx, ny = 50 + y, 50
        d1, d2 = 0, 1
    if A == 4 and x == 3 * 50 - 1 and dx == 1: # DF
        nx, ny = 3 * 50 + y % 50, 49
        d1, d2 = 0, -1
    if A == 4 and y == 2 * 50 - 1 and dy == 1: # DB
        nx, ny = 49 - x % 50, 3 * 50 - 1
        d1, d2 = 0, -1
    if A == 5 and y == 0 and dy == -1: # FA
        nx, ny = 0, 50 + x % 50
        d1, d2 = 1, 0
    if A == 5 and y == 49 and dy == 1: # FD
        nx, ny = 3 * 50 - 1, 50 + x % 50
        d1, d2 = -1, 0
    if A == 5 and x == H - 1 and dx == 1: # FB
        nx, ny = 0, y % 50 + 2 * 50
        d1, d2 = 1, 0
    return nx, ny, d1, d2

x, y = leftmost(grid, 0)
dx, dy = 0, 1

di = [i for i in path if i in "LR"] + [" "]
num = gi(path)
for i, j in zip(di, num):
    for _ in range(j):
        X, Y, dx1, dy1 = move(x, y, dx, dy)
        #while grid[X][Y] == " ":
        #    X += dx
        #    Y += dy
        if grid[X][Y] == "#":
            break
        x, y, dx, dy = X, Y, dx1, dy1
    #x %= H
    #y %= W
    if i == "R":
        dx, dy = dy, -dx
    elif i == "L":
        dx, dy = -dy, dx
di = {
    (0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3
}
print((x + 1) * 1000 + 4 * (y + 1) + di[dx, dy])