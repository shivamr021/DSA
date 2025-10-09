from os import *
from sys import *
from collections import *
from math import *
import heapq
def kthSmallest(arr, n, k):
    # Write your code here
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]
