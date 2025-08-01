from os import *
from sys import *
from collections import *
from math import *

from typing import *

def beautifulIndex(N: int, A: List[int]) -> int:
    # Write your code here.
    total = sum(A)
    prefix_sum = 0

    for i in range(N):
        if prefix_sum == total - prefix_sum - A[i]:
            return i+1
        prefix_sum += A[i]
    return -1
