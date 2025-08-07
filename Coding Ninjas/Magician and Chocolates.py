# from os import *
# from sys import *
# from collections import *
# from math import *
import heapq
MOD = 10**9 + 7

def maximumChocolates(arr, k):
    # Write your code here.
    max_heap = [-val for val in arr]
    heapq.heapify(max_heap)

    total = 0
    for _ in range(k):
        max_choco = -heapq.heappop(max_heap)
        total = (total + max_choco) % MOD

        heapq.heappush(max_heap, - (max_choco // 2))

    return total
