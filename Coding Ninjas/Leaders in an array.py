from os import *
from sys import *
from collections import *
from math import *

def findLeaders(elements, n):
    # Write your code here.
    ans = []
    ans.append(elements[-1])
    max_el_r = elements[-1]

    for i in range(n-2, -1, -1):
        if elements[i] > max_el_r:
            ans.append(elements[i])
        max_el_r = max(max_el_r, elements[i])
    
    ans.reverse()
    return ans

# Taking input using fast I/O.
def takeInput():
    n = int(input())
    elements = list(map(int, input().strip().split(" ")))

    return n, elements

# Main.
t = int(input())
while t:
    n, elements = takeInput()
    answer = findLeaders(elements, n)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t-1
