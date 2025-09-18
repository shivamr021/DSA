from os import *
from sys import *
from collections import *
from math import *

def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k - 1]
