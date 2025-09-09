from os import *
from sys import *
from collections import *
from math import *

def flipSomeBits(num, arr, n):
	# Write your code here.
	for pos in arr:
		mask = 1 << (pos - 1)
		num ^= mask
	return num
