from os import *
from sys import *
from collections import *
from math import *

def countOfDivisiblePairs(n, m):
    # Write your code here.
    count_x = [0] * 5
    for i in range(1, n+1):
        count_x[i % 5] += 1
    
    count_y = [0] * 5
    for j in range(1, m+1):
        count_y[j % 5] += 1

    total = 0
    for r1 in range(5):
        r2 = (5 - r1) % 5
        total += count_x[r1] * count_y[r2]

    return total
