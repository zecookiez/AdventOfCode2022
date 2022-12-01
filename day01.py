# You get to see my template this year because I don't have the time to change it out

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

OUTPUT = True
if OUTPUT:
    file = open("input.txt", "r")
    #input = [i.strip() for i in file.readlines()]
    input = file.read().split("\n\n")
else:
    """ctrl-d for EOF"""
    #input = [i.strip() for i in stdin.readlines()]
    input = stdin.read().split("\n\n")

arr = [sum(gi(line)) for line in input]

print(max(arr))
print(sum(sorted(arr,reverse=True)[:3]))

