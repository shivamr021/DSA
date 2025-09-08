# from os import *
# from sys import *
# from collections import *
# from math import *
from typing import *

def max_shares(k: int, n: int, shares: List[int]) -> int:
    # Write your code here.
    days = [(shares[i], i+1) for i in range(n)]

    days.sort()

    total_shares = 0

    for price, limit in days:
        if k < price:
            break
        
        can_buy = min(limit, k // price)
        total_shares += can_buy
        k -= can_buy * price

    return total_shares
