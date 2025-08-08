from sys import *
from collections import *
from math import *

from sys import stdin
import sys


def findAnagramsIndices(n, m, s, ptr):
    # Write your code here.
    s = s.strip()
    ptr = ptr.strip()
    s = s.upper()
    ptr = ptr.upper()

    if m == 0 or n == 0 or m > len(s):
        return []

    target_count = [0] * 26
    for ch in ptr:
        target_count[ord(ch) - ord('A')] += 1

    window_count = [0] * 26
    for i in range(m):
        window_count[ord(s[i]) - ord('A')] += 1
    
    res = []
    if window_count == target_count:
        res.append(0)
    
    for i in range(m, n):
        window_count[ord(s[i]) - ord('A')] += 1

        window_count[ord(s[i-m]) - ord('A')] -= 1

        if window_count == target_count:
            res.append(i - m + 1)
    
    return res


# Taking input using fast I/O.
def takeInput():

    nums = list(map(int, input().strip().split(" ")))
    st = input()
    ptr = input()

    return nums, st, ptr


# Main.
t = int(input())
while t:
    nums, st, ptr = takeInput()
    n, m = nums
    answer = findAnagramsIndices(n, m, st, ptr)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t-1
