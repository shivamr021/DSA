from sys import *
from collections import *
from math import *

from typing import *

def minimizeIt(A: List[int], K: int) ->int:
    # Write your code here.
    n = len(A)
    A.sort()

    ans = A[-1] - A[0]

    for i in range(n-1):
        high = max(A[-1] - K, A[i] + K)
        low = min(A[0] + K, A[i+1] - K)

        if low < 0:
            continue
        
        ans = min(ans, high - low)
    
    return ans
