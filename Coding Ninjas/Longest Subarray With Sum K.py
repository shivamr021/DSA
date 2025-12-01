from sys import *
from collections import *
from math import *

def getLongestSubarray(nums, k):
    prefix_index = {} 
    s = 0
    longest = 0

    for i, val in enumerate(nums):
        s += val

        if s == k:
            longest = max(longest, i + 1)

        if (s - k) in prefix_index:
            longest = max(longest, i - prefix_index[s - k])

        if s not in prefix_index:
            prefix_index[s] = i

    return longest
