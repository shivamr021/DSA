# from os import *
# from sys import *
# from collections import *
# from math import *
from itertools import combinations

def calculateArea(n, points):
	# Write your code here.
	max_area = 0.0
	
	for (x1,y1), (x2,y2), (x3,y3) in combinations(points, 3):
		area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
		max_area = max(max_area, area)

	return max_area
