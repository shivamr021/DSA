from os import *
from sys import *
from collections import *
from math import *

def splitArray(arr,k):    
    #Your code goes here.
    total_sum = sum(arr)

    if total_sum % k != 0:
        return False
    
    target = total_sum // k
    n = len(arr)
    arr.sort(reverse = True)

    if arr[0] > target:
        return False

    visited = [False] * n

    def backtrack(start, k, curr_sum):
        if k == 1:
            return True

        if curr_sum == target:
            return backtrack(0, k-1, 0)

        for i in range(start, n):
            if not visited[i] and curr_sum + arr[i] <= target:
                visited[i] = True

                if backtrack(i+1, k, curr_sum + arr[i]):
                    return True
                visited[i] = False

                if curr_sum == 0:
                    break

            while i + 1 < n and arr[i] == arr[i+1]:
                i += 1
        
        return False
    
    return backtrack(0, k, 0)
