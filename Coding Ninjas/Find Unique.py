import sys

def findUnique(arr, n) :
    #write your code here 
    xor = 0
    for i in range(n):
        xor ^= arr[i]
    return xor
