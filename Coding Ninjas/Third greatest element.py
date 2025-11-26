from os import *
from sys import *
from collections import *
from math import *

def findThirdLagrest(arr):
	# Write your code here
	mx = smx = tmx = -inf

	for num in arr:
		if num > mx:
			tmx = smx
			smx = mx
			mx = num

		elif num > smx:
			tmx = smx
			smx = num
		
		elif num > tmx:
			tmx = num
	
	return tmx
