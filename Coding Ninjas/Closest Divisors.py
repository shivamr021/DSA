from os import *
from sys import *
from collections import *
from math import *

def closestDivisors(num):
    # Write your code here.
    best_diff = float('inf')
    best_pair = ()

    for target in [num+1, num+2]:
        for i in range(1, int(sqrt(target))+1):
            if target % i  == 0:
                a, b = i, target // i
                diff = abs(a-b)
                if diff < best_diff:
                    best_diff = diff
                    best_pair = (a, b)
    return best_pair
