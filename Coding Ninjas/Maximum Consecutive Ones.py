from collections import *
from math import *
from typing import List


def consecutiveOnes(arr: List[int]) -> int:
    # Write your code here.
    maxi = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    return maxi
