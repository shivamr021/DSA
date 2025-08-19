from os import *
from sys import *
from collections import *
from math import *

def divideString(word, n):
	# Write your code here
	if len(word) % n != 0:
		return []

	part_len = len(word) // n
	res = []

	for i in range(0, len(word), part_len):
		res.append(word[i:i+part_len])
	
	return res
