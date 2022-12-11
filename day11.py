from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product
from heapq import heappush, heappop
from time import time
from math import gcd

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

monk = defaultdict(list)
tot = defaultdict(int)
rem = 1

def lcm(a, b):
    return a * b // gcd(a, b)
for ind, monkey in enumerate(input):
    rem = lcm(rem, GI(monkey.split("\n")[3]))

for ind, monkey in enumerate(input):
    monkey = monkey.split("\n")[1:]
    st = gi(monkey[0]) + monk[ind]
    tot[ind] += len(st)
    monk[ind] = []
    op = monkey[1][monkey[1].find(":")+1:].strip()
    div = GI(monkey[2])
    tru = GI(monkey[3])
    fal = GI(monkey[4])
    for old in st:
        new = eval(op[op.find("=")+1:]) #// 3
        new %= rem
        if new % div == 0:
            monk[tru].append(new)
        else:
            monk[fal].append(new)

for _ in range(1, 10000):
    for ind, monkey in enumerate(input):
        monkey = monkey.split("\n")[1:]
        st = monk[ind]
        tot[ind] += len(st)
        monk[ind] = []
        op = monkey[1][monkey[1].find(":")+1:].strip()
        div = GI(monkey[2])
        tru = GI(monkey[3])
        fal = GI(monkey[4])
        for old in st:
            new = eval(op[op.find("=")+1:]) #// 3
            new %= rem
            if new % div == 0:
                monk[tru].append(new)
            else:
                monk[fal].append(new)

vals = sorted(tot.values())
print(vals[-1] * vals[-2])