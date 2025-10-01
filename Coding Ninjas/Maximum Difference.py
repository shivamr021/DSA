from os import *
from sys import *
from collections import *
from math import *

def maximumDifferece(n, arr):
    # Write your code here.
    arr.sort()
    max_diff = arr[n-1] - arr[0]
    if max_diff % 2 == 0:
        return "EVEN"
    return "ODD"
