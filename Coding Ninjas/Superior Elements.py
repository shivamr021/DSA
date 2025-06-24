from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    n = len(a)
    maxi = float('-inf')
    for i in range(n-1, -1, -1):
        if a[i] > maxi:
            maxi = a[i]
            a.append(a[i])
    a[n:] = sorted(a[n:])
    return a[n:]
