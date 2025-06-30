from os import *
from sys import *
from collections import *
from math import *

def lookAndSaySequence(n):

	# Write your code here
	if n == 1:
		return "1"
	
	result = "1"
	for _ in range(1, n):
		curr = result
		result = ""
		i = 0

		while i < len(curr):
			cnt = 1
			while i+1 < len(curr) and curr[i] == curr[i+1]:
				cnt += 1
				i += 1
			result += str(cnt) + curr[i]
			i += 1
	return result
