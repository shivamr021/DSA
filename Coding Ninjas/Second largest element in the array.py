from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    if len(sequenceOfNumbers) < 2:
        return -1
    max_ele = sec_max_ele = float('-inf')

    for num in sequenceOfNumbers:
        if num > max_ele:
            sec_max_ele = max_ele
            max_ele = num
        elif num > sec_max_ele and num != max_ele:
            sec_max_ele = num

    return sec_max_ele if sec_max_ele != float('-inf') else -1


# Taking input using fast I/O.
def takeInput():
    n = int(input())
    sequenceOfNumbers = list(map(int, input().strip().split(" ")))
    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
