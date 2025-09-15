from os import *
from sys import *
from collections import *
from math import *

def predictTheWinner(n, k):
    # Josephus position (0-based)
    res = 0
    for i in range(2, n+1):
        res = (res + k) % i
    return res + 1  # convert to 1-based
