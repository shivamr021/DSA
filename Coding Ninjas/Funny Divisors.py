# from os import *
# from sys import *
# from collections import *
# from math import *

def findSum(n, arr):
    # Write your Code Here.
    sum_ = 0
    for num in arr:
        if num%2 == 0 or num%3 == 0:
            sum_ += num
    # Return an integer denoting the answer
    return sum_    
