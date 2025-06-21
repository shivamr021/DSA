from typing import *

def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    n = N-1
    xor1, xor2 = 0, 0
    for i in range(n):
        xor2 ^= a[i]
        xor1 ^= (i+1)
    xor1 ^= N 
    return xor1 ^ xor2
