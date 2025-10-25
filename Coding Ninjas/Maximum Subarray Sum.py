from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
	# Your code here
    max_sum = 0
    sm = 0
    for num in arr:
        sm += num
        max_sum = max(max_sum, sm)
        if sm < 0:
            sm = 0
    
    # return the answer
    return max_sum
































#taking inpit using fast I/O
def takeInput() :
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
